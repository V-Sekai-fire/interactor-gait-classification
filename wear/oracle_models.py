"""BUILD THE ORACLES (real models toward the oracle ceilings).
The oracle decomposition says rank-1 = solve (A) the active/null gate [85% of loss] + (B) within-family
complex-variant pairs. We build both, fully inductive, held-out subj16-19, vs ceilings base 0.525,
gate-oracle 0.633, both-oracle 0.764.

Stage1 GATE: binary null-vs-active, gravity/orientation channels (static pose differs from rest in
ORIENTATION not motion -> AUC 0.9 on active limb).  Stage2 ACT: 18-way over active classes.
Soft hierarchical combine: P(null)=gate_null; P(c>0)=gate_active * act(c).
Stage3 SPECIALISTS: binary heads for confusable pairs (jog/jogR, pu/puC, su/suC, lun/lunC); override
the combined prediction when it lands in a pair.
"""
import numpy as np, pandas as pd, glob, torch, torch.nn as nn, time
from sklearn.metrics import f1_score
LM={'null':0,'jogging':1,'jogging (rotating arms)':2,'jogging (skipping)':3,'jogging (sidesteps)':4,'jogging (butt-kicks)':5,'stretching (triceps)':6,'stretching (lunging)':7,'stretching (shoulders)':8,'stretching (hamstrings)':9,'stretching (lumbar rotation)':10,'push-ups':11,'push-ups (complex)':12,'sit-ups':13,'sit-ups (complex)':14,'burpees':15,'lunges':16,'lunges (complex)':17,'bench-dips':18}
LIMBS=[["right_arm_acc_x","right_arm_acc_y","right_arm_acc_z"],["right_leg_acc_x","right_leg_acc_y","right_leg_acc_z"],["left_leg_acc_x","left_leg_acc_y","left_leg_acc_z"],["left_arm_acc_x","left_arm_acc_y","left_arm_acc_z"]]
PAIRS=[(1,2),(11,12),(13,14),(16,17)]   # base vs complex-ish variant
DEV="cuda"; STRIDE=25
def build():
    A,Y,G=[],[],[]
    for csv in sorted(glob.glob("train/inertial_feat/sbj_*.csv")):
        df=pd.read_csv(csv,low_memory=False); sbj=int(df.sbj_id.iloc[0]); lab=df.label.fillna("null").astype(str).values
        arrs=[np.nan_to_num(df[c].values.astype(np.float32)) for c in LIMBS]
        for k in range(0,len(df)-50,STRIDE):
            seg=lab[k:k+50]; v,c=np.unique(seg,return_counts=True)
            if c.max()<40: continue
            lbl=LM[v[c.argmax()]]
            for a in arrs: A.append(a[k:k+50]); Y.append(lbl); G.append(sbj)
    return np.array(A,np.float32),np.array(Y),np.array(G)
def ch10(A):  # linear(3)+gravity(3)+gravity-direction(3)+linear-mag(1)
    g=A.mean(1,keepdims=True); lin=A-g; gb=np.broadcast_to(g,A.shape)
    gdir=g/(np.linalg.norm(g,axis=2,keepdims=True)+1e-6); gdirb=np.broadcast_to(gdir,A.shape)
    mag=np.sqrt((lin**2).sum(2,keepdims=True))
    return np.concatenate([lin,gb,gdirb,mag],2).transpose(0,2,1)
class CNN(nn.Module):
    def __init__(s,nout,cin=10): super().__init__(); s.n=nn.Sequential(nn.Conv1d(cin,64,7,padding=3),nn.BatchNorm1d(64),nn.ReLU(),nn.MaxPool1d(2),
        nn.Conv1d(64,128,5,padding=2),nn.BatchNorm1d(128),nn.ReLU(),nn.MaxPool1d(2),
        nn.Conv1d(128,128,3,padding=1),nn.BatchNorm1d(128),nn.ReLU(),nn.AdaptiveAvgPool1d(1),nn.Flatten(),nn.Dropout(.3),nn.Linear(128,nout))
    def forward(s,x): return s.n(x)
def fit(X,yt,nout,epochs=45,w=None):
    m=CNN(nout).to(DEV); opt=torch.optim.AdamW(m.parameters(),1e-3,weight_decay=1e-4); sch=torch.optim.lr_scheduler.CosineAnnealingLR(opt,epochs)
    wt=None if w is None else torch.tensor(w,device=DEV,dtype=torch.float32); lf=nn.CrossEntropyLoss(label_smoothing=.05,weight=wt)
    xt=torch.tensor(X,device=DEV); yy=torch.tensor(yt,device=DEV)
    for ep in range(epochs):
        m.train(); p=torch.randperm(len(xt),device=DEV)
        for i in range(0,len(xt),512): b=p[i:i+512]; opt.zero_grad(); lf(m(xt[b]),yy[b]).backward(); opt.step()
        sch.step()
    return m
def prob(m,X):
    m.eval(); out=[]
    with torch.no_grad():
        for i in range(0,len(X),8192): out.append(torch.softmax(m(torch.tensor(X[i:i+8192],device=DEV)),1).cpu().numpy())
    return np.concatenate(out)

print("building...",flush=True); A,y,g=build(); X=ch10(A)
mu=X.mean((0,2),keepdims=True); sd=X.std((0,2),keepdims=True)+1e-6; X=np.nan_to_num((X-mu)/sd)
HO={16,17,18,19}; te=np.isin(g,list(HO)); tr=~te
print(f"train={tr.sum()} test={te.sum()}",flush=True)
# baseline 19-way
t=time.time(); base=fit(X[tr],y[tr],19); bp=prob(base,X[te])
print(f"[baseline 19-way]   macro={f1_score(y[te],bp.argmax(1),average='macro'):.4f}  ({time.time()-t:.0f}s)",flush=True)
# Stage1 gate (binary null vs active) -- weight active up to catch static poses
gy=(y>0).astype(int); t=time.time()
gate=fit(X[tr],gy[tr],2,w=[1.0,1.3]); gpb=prob(gate,X[te])  # gpb[:,1]=P(active)
print(f"  gate active-recall={f1_score(gy[te],gpb.argmax(1)):.3f} acc={(gpb.argmax(1)==gy[te]).mean():.3f} ({time.time()-t:.0f}s)",flush=True)
# Stage2 active head (18-way over true-active windows), classes 1..18 -> 0..17
am=tr&(y>0); ah=fit(X[am],y[am]-1,18); apb=prob(ah,X[te])  # (Nte,18)
# soft hierarchical combine
P=np.zeros((te.sum(),19),np.float32); P[:,0]=gpb[:,0]; P[:,1:]=gpb[:,1:2]*apb
hp=P.argmax(1)
print(f"[gate+active soft]  macro={f1_score(y[te],hp,average='macro'):.4f}   (gate-oracle 0.633)",flush=True)
# Stage3 specialists for confusable pairs
spec={}
for a,b in PAIRS:
    m=tr&((y==a)|(y==b)); ys=(y[m]==b).astype(int)
    spec[(a,b)]=fit(X[m],ys,2)
fp=hp.copy()
for (a,b),sm in spec.items():
    idx=np.where((fp==a)|(fp==b))[0]
    if len(idx)==0: continue
    sp=prob(sm,X[te][idx]); fp[idx]=np.where(sp[:,1]>0.5,b,a)
print(f"[+ specialists]     macro={f1_score(y[te],fp,average='macro'):.4f}   (both-oracle 0.764)",flush=True)
print("=== held-out: if gate+active >> 0.525 and approaches 0.633, promote to LOSO ===",flush=True)
