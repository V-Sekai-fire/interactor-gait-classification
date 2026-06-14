"""BANK THE LEGIT STACK -> submission. Combine the four proven inductive single-limb levers:
  (1) 10ch gravity-orientation channels   (+0.018 hard)
  (2) equity 6D-rotation augmentation on hard classes  (+0.031)
  (3) sqrt-balanced loss (mild null rebalance)  (+0.021)
  (4) prior-correction at inference (macro-F1 trick)  (+~0.016)
Validate the COMBINED stack on held-out subj16-19 (vs single-limb baseline 0.536) + pick decision rule,
then full-data train -> test submission (test_inertial_data is single-limb 50x3). LABEL_MAP encoding.
"""
import numpy as np, pandas as pd, glob, torch, torch.nn as nn, time
from sklearn.metrics import f1_score
LM={'null':0,'jogging':1,'jogging (rotating arms)':2,'jogging (skipping)':3,'jogging (sidesteps)':4,'jogging (butt-kicks)':5,'stretching (triceps)':6,'stretching (lunging)':7,'stretching (shoulders)':8,'stretching (hamstrings)':9,'stretching (lumbar rotation)':10,'push-ups':11,'push-ups (complex)':12,'sit-ups':13,'sit-ups (complex)':14,'burpees':15,'lunges':16,'lunges (complex)':17,'bench-dips':18}
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
def ch10(A):
    g=A.mean(1,keepdims=True); lin=A-g; gb=np.broadcast_to(g,A.shape)
    gdir=g/(np.linalg.norm(g,axis=2,keepdims=True)+1e-6); gdirb=np.broadcast_to(gdir,A.shape)
    mag=np.sqrt((lin**2).sum(2,keepdims=True))
    return np.concatenate([lin,gb,gdirb,mag],2).transpose(0,2,1)
def rot6d(n,rng,sc):
    base=np.tile(np.eye(3,2,dtype=np.float32),(n,1,1))+rng.normal(0,sc,(n,3,2)).astype(np.float32)
    a1,a2=base[:,:,0],base[:,:,1]; b1=a1/np.linalg.norm(a1,axis=1,keepdims=True)
    a2=a2-(b1*a2).sum(1,keepdims=True)*b1; b2=a2/np.linalg.norm(a2,axis=1,keepdims=True); b3=np.cross(b1,b2)
    return np.stack([b1,b2,b3],2)
def augment(A3,y,rng,k=3,sc=0.25):  # on RAW (N,50,3) hard-class windows
    mask=np.isin(y,HARD); Ah=A3[mask]; yh=y[mask]; oA=[A3]; oY=[y]
    for _ in range(k):
        R=rot6d(len(Ah),rng,sc); Ar=np.einsum('nij,ntj->nti',R,Ah).astype(np.float32)
        Ar=Ar*rng.uniform(0.85,1.15,(len(Ah),1,1)).astype(np.float32)+rng.normal(0,0.02,Ah.shape).astype(np.float32)
        oA.append(Ar); oY.append(yh)
    return np.concatenate(oA),np.concatenate(oY)
class CNN(nn.Module):
    def __init__(s): super().__init__(); s.n=nn.Sequential(nn.Conv1d(10,64,7,padding=3),nn.BatchNorm1d(64),nn.ReLU(),nn.MaxPool1d(2),
        nn.Conv1d(64,128,5,padding=2),nn.BatchNorm1d(128),nn.ReLU(),nn.MaxPool1d(2),
        nn.Conv1d(128,128,3,padding=1),nn.BatchNorm1d(128),nn.ReLU(),nn.AdaptiveAvgPool1d(1),nn.Flatten(),nn.Dropout(.3),nn.Linear(128,19))
    def forward(s,x): return s.n(x)
def train(A3,y,rng,mu,sd,w,epochs=50):
    Aa,ya=augment(A3,y,rng); Xtr=np.nan_to_num((ch10(Aa)-mu)/sd)
    m=CNN().to(DEV); opt=torch.optim.AdamW(m.parameters(),1e-3,weight_decay=1e-4); sch=torch.optim.lr_scheduler.CosineAnnealingLR(opt,epochs)
    lf=nn.CrossEntropyLoss(label_smoothing=.05,weight=torch.tensor(w,device=DEV,dtype=torch.float32))
    xt=torch.tensor(Xtr,device=DEV); yt=torch.tensor(ya,device=DEV)
    for ep in range(epochs):
        m.train(); p=torch.randperm(len(xt),device=DEV)
        for i in range(0,len(xt),512): b=p[i:i+512]; opt.zero_grad(); lf(m(xt[b]),yt[b]).backward(); opt.step()
        sch.step()
    return m
def probs(m,A3,mu,sd):
    X=np.nan_to_num((ch10(A3)-mu)/sd); m.eval(); out=[]
    with torch.no_grad():
        for i in range(0,len(X),8192): out.append(torch.softmax(m(torch.tensor(X[i:i+8192],device=DEV)),1).cpu().numpy())
    return np.concatenate(out)
print("building...",flush=True); A,y,g=build(); rng=np.random.default_rng(0)
freq=np.bincount(y,minlength=19).astype(float); wsqrt=np.sqrt(freq.max()/freq); prior=freq/freq.sum()
# ---- held-out validation (subj16-19) ----
HO={16,17,18,19}; te=np.isin(g,list(HO)); tr=~te
mu=ch10(A[tr]).mean((0,2),keepdims=True); sd=ch10(A[tr]).std((0,2),keepdims=True)+1e-6
m=train(A[tr],y[tr],rng,mu,sd,wsqrt); pv=probs(m,A[te],mu,sd)
for t in [0.0,0.2,0.4]:
    pr=(pv/(prior**t+1e-9)).argmax(1); f=f1_score(y[te],pr,average='macro')
    print(f"[held-out stack] prior^{t}: macro={f:.4f} (single-limb baseline 0.536)",flush=True)
bestt=max([0.0,0.2,0.4],key=lambda t:f1_score(y[te],(pv/(prior**t+1e-9)).argmax(1),average='macro'))
print(f"  chosen prior^t={bestt}",flush=True)
# ---- full-data train -> submission ----
muf=ch10(A).mean((0,2),keepdims=True); sdf=ch10(A).std((0,2),keepdims=True)+1e-6
mf=train(A,y,rng,muf,sdf,wsqrt)
ti=np.load("test/test_inertial_data.npy",allow_pickle=True).astype(np.float32)  # (N,50,3) single limb
tp=probs(mf,ti,muf,sdf); pred=(tp/(prior**bestt+1e-9)).argmax(1)
ss=pd.read_csv("sample_submission.csv"); ss["target_feature"]=pred.astype(int); ss.to_csv("submissions/submission_legit_stack.csv",index=False)
print(f"wrote submissions/submission_legit_stack.csv  dist={dict(sorted(pd.Series(pred).value_counts().items()))}",flush=True)
print("=== banked the legit single-limb stack (orientation+equity-aug+sqrt-bal+prior) ===",flush=True)
