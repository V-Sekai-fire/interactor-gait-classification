"""SMOKING LEVER: hard static-pose classes leak 30-73% of their mass to NULL (42% of data), NOT to
their siblings (within-family leak <28%). So this is class-imbalance, not a sensor wall. Test null
rebalancing strategies (held-out subj16-19): class-weighted loss (balanced / sqrt / null-capped),
optionally stacked with equity 6D-rot augmentation. Report macro + hard-class F1 + null F1 (must hold).
"""
import numpy as np, pandas as pd, glob, os, torch, torch.nn as nn, time
from sklearn.metrics import f1_score
LM={'null':0,'jogging':1,'jogging (rotating arms)':2,'jogging (skipping)':3,'jogging (sidesteps)':4,'jogging (butt-kicks)':5,'stretching (triceps)':6,'stretching (lunging)':7,'stretching (shoulders)':8,'stretching (hamstrings)':9,'stretching (lumbar rotation)':10,'push-ups':11,'push-ups (complex)':12,'sit-ups':13,'sit-ups (complex)':14,'burpees':15,'lunges':16,'lunges (complex)':17,'bench-dips':18}
N=['null','jog','jog-rot','jog-skip','jog-side','jog-butt','str-tri','str-lunge','str-shldr','str-ham','str-lumbar','pushup','pushup-cx','situp','situp-cx','burpee','lunge','lunge-cx','bench-dip']
LIMBS=[["right_arm_acc_x","right_arm_acc_y","right_arm_acc_z"],["right_leg_acc_x","right_leg_acc_y","right_leg_acc_z"],["left_leg_acc_x","left_leg_acc_y","left_leg_acc_z"],["left_arm_acc_x","left_arm_acc_y","left_arm_acc_z"]]
HARD=[6,7,8,9,11,12,13,16,17,18]; DEV="cuda"; STRIDE=25

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

def rot6d(n,rng,sc):
    base=np.tile(np.eye(3,2,dtype=np.float32),(n,1,1))+rng.normal(0,sc,(n,3,2)).astype(np.float32)
    a1,a2=base[:,:,0],base[:,:,1]; b1=a1/np.linalg.norm(a1,1,keepdims=True) if False else a1/np.linalg.norm(a1,axis=1,keepdims=True)
    a2=a2-(b1*a2).sum(1,keepdims=True)*b1; b2=a2/np.linalg.norm(a2,axis=1,keepdims=True); b3=np.cross(b1,b2)
    return np.stack([b1,b2,b3],2)
def augment(A,y,rng,k=3,sc=0.25):
    mask=np.isin(y,HARD); Ah=A[mask]; yh=y[mask]; oA=[A]; oY=[y]
    for _ in range(k):
        R=rot6d(len(Ah),rng,sc); Ar=np.einsum('nij,ntj->nti',R,Ah).astype(np.float32)
        Ar=Ar*rng.uniform(0.85,1.15,(len(Ah),1,1)).astype(np.float32)+rng.normal(0,0.02,Ah.shape).astype(np.float32)
        oA.append(Ar); oY.append(yh)
    return np.concatenate(oA),np.concatenate(oY)

def chans(A):
    mag=np.sqrt((A**2).sum(2,keepdims=True)); jerk=np.concatenate([np.zeros((len(A),1,3),np.float32),np.diff(A,axis=1)],1)
    return np.concatenate([A,mag,jerk],2).transpose(0,2,1)
class CNN(nn.Module):
    def __init__(s): super().__init__(); s.n=nn.Sequential(nn.Conv1d(7,64,7,padding=3),nn.BatchNorm1d(64),nn.ReLU(),nn.MaxPool1d(2),
        nn.Conv1d(64,128,5,padding=2),nn.BatchNorm1d(128),nn.ReLU(),nn.MaxPool1d(2),
        nn.Conv1d(128,128,3,padding=1),nn.BatchNorm1d(128),nn.ReLU(),nn.AdaptiveAvgPool1d(1),nn.Flatten(),nn.Dropout(.3),nn.Linear(128,19))
    def forward(s,x): return s.n(x)

def fit_eval(Atr,ytr,Ate,yte,w=None):
    Ac=chans(Atr); mu=Ac.reshape(-1,7,1).mean((0,2)).reshape(1,7,1); sd=Ac.reshape(-1,7,1).std((0,2)).reshape(1,7,1)+1e-6
    xt=torch.tensor(np.nan_to_num((Ac-mu)/sd),device=DEV); yt=torch.tensor(ytr,device=DEV); xe=torch.tensor(np.nan_to_num((chans(Ate)-mu)/sd),device=DEV)
    m=CNN().to(DEV); opt=torch.optim.AdamW(m.parameters(),1e-3,weight_decay=1e-4); sch=torch.optim.lr_scheduler.CosineAnnealingLR(opt,50)
    wt=None if w is None else torch.tensor(w,device=DEV,dtype=torch.float32)
    lf=nn.CrossEntropyLoss(label_smoothing=.05,weight=wt)
    for ep in range(50):
        m.train(); p=torch.randperm(len(xt),device=DEV)
        for i in range(0,len(xt),512): b=p[i:i+512]; opt.zero_grad(); lf(m(xt[b]),yt[b]).backward(); opt.step()
        sch.step()
    m.eval()
    with torch.no_grad(): pr=np.concatenate([m(xe[i:i+8192]).argmax(1).cpu().numpy() for i in range(0,len(xe),8192)])
    return pr

print("building...",flush=True); A,y,g=build(); rng=np.random.default_rng(0)
HO={16,17,18,19}; te=np.isin(g,list(HO)); tr=~te; Atr0,ytr0=A[tr],y[tr]
freq=np.bincount(ytr0,minlength=19).astype(float)
W={
 "baseline": None,
 "balanced": (len(ytr0)/(19*freq)),
 "sqrt-bal": np.sqrt(freq.max()/freq),
 "null-cap0.2": np.where(np.arange(19)==0,0.2,1.0),
 "null-cap0.1": np.where(np.arange(19)==0,0.1,1.0),
}
def report(tag,pr):
    f1=f1_score(y[te],pr,average=None,labels=range(19)); print(f"[{tag:18s}] macro={f1.mean():.4f} hard={f1[HARD].mean():.4f} null-F1={f1[0]:.4f}",flush=True); return f1
for tag,w in W.items():
    report(tag,fit_eval(Atr0,ytr0,A[te],y[te],w))
# best rebalance + equity aug stacked
Aa,ya=augment(Atr0,ytr0,rng,k=3); print(f"--- + equity-aug (n={len(ya)}) ---",flush=True)
for tag in ["null-cap0.2","null-cap0.1","balanced"]:
    report(f"aug+{tag}",fit_eval(Aa,ya,A[te],y[te],W[tag]))
print("=== if hard-class F1 jumps toward 0.6+ while null-F1 holds, null-imbalance was the lever ===",flush=True)
