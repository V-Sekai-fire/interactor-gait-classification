"""EQUITY-SYNTHETIC GATE: does augmenting the low-scoring STATIC-POSE classes lift their F1,
or are they information-theoretically overlapped (=> no synthetic data can ever help)?
Cheap proxy for the full ANNY/SOMA-X physics sim: apply 6D-rotation sensor-orientation perturbation
+ magnitude/time warp ONLY to the hard classes, held-out subj 16-19, compare per-class F1 vs baseline.
6D rotation rep (Zhou et al.): sample 2 vecs -> Gram-Schmidt -> SO(3), rotate the accel xyz. Continuous,
no Euler gimbal artifacts. If hard classes move -> build the body-model sim. If flat -> classes overlap.
"""
import numpy as np, pandas as pd, glob, os, torch, torch.nn as nn, time
from sklearn.metrics import f1_score
LM={'null':0,'jogging':1,'jogging (rotating arms)':2,'jogging (skipping)':3,'jogging (sidesteps)':4,'jogging (butt-kicks)':5,'stretching (triceps)':6,'stretching (lunging)':7,'stretching (shoulders)':8,'stretching (hamstrings)':9,'stretching (lumbar rotation)':10,'push-ups':11,'push-ups (complex)':12,'sit-ups':13,'sit-ups (complex)':14,'burpees':15,'lunges':16,'lunges (complex)':17,'bench-dips':18}
N=['null','jog','jog-rot','jog-skip','jog-side','jog-butt','str-tri','str-lunge','str-shldr','str-ham','str-lumbar','pushup','pushup-cx','situp','situp-cx','burpee','lunge','lunge-cx','bench-dip']
LIMBS=[["right_arm_acc_x","right_arm_acc_y","right_arm_acc_z"],["right_leg_acc_x","right_leg_acc_y","right_leg_acc_z"],["left_leg_acc_x","left_leg_acc_y","left_leg_acc_z"],["left_arm_acc_x","left_arm_acc_y","left_arm_acc_z"]]
HARD=[6,7,8,9,11,12,13,16,17,18]  # the 0.38-0.46 static-pose band (+str-shldr 0.085)
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

def rot6d(n,rng,scale):  # n random rotation matrices near identity, parameterized 6D (Gram-Schmidt)
    base=np.tile(np.eye(3,2,dtype=np.float32),(n,1,1))            # (n,3,2) identity cols
    base=base+rng.normal(0,scale,base.shape).astype(np.float32)  # perturb in 6D space
    a1,a2=base[:,:,0],base[:,:,1]
    b1=a1/np.linalg.norm(a1,axis=1,keepdims=True)
    a2=a2-(b1*a2).sum(1,keepdims=True)*b1; b2=a2/np.linalg.norm(a2,axis=1,keepdims=True)
    b3=np.cross(b1,b2)
    return np.stack([b1,b2,b3],axis=2)                            # (n,3,3) SO(3)

def augment(A,y,rng,k=3,scale=0.25):  # k synthetic copies per hard-class window
    mask=np.isin(y,HARD); Ah=A[mask]; yh=y[mask]; outA=[A]; outY=[y]
    for _ in range(k):
        R=rot6d(len(Ah),rng,scale)                               # sensor-orientation perturb (6D)
        Ar=np.einsum('nij,ntj->nti',R,Ah).astype(np.float32)     # rotate accel xyz
        mag=rng.uniform(0.85,1.15,(len(Ah),1,1)).astype(np.float32); Ar=Ar*mag       # magnitude warp
        # time warp: random resample of the 50-step window
        for i in range(len(Ar)):
            sp=np.sort(rng.uniform(0,49,50)); Ar[i]=np.stack([np.interp(np.arange(50),np.linspace(0,49,50),Ar[i,:,c]) for c in range(3)],1)
        Ar=Ar+rng.normal(0,0.02,Ar.shape).astype(np.float32)     # jitter
        outA.append(Ar); outY.append(yh)
    return np.concatenate(outA),np.concatenate(outY)

def chans(A):
    mag=np.sqrt((A**2).sum(2,keepdims=True)); jerk=np.concatenate([np.zeros((len(A),1,3),np.float32),np.diff(A,axis=1)],1)
    return np.concatenate([A,mag,jerk],2).transpose(0,2,1)

class CNN(nn.Module):
    def __init__(s): super().__init__(); s.n=nn.Sequential(nn.Conv1d(7,64,7,padding=3),nn.BatchNorm1d(64),nn.ReLU(),nn.MaxPool1d(2),
        nn.Conv1d(64,128,5,padding=2),nn.BatchNorm1d(128),nn.ReLU(),nn.MaxPool1d(2),
        nn.Conv1d(128,128,3,padding=1),nn.BatchNorm1d(128),nn.ReLU(),nn.AdaptiveAvgPool1d(1),nn.Flatten(),nn.Dropout(.3),nn.Linear(128,19))
    def forward(s,x): return s.n(x)

def fit_eval(Atr,ytr,Ate,yte):
    Ac=chans(Atr); mu=Ac.reshape(-1,7,1).mean((0,2)).reshape(1,7,1); sd=Ac.reshape(-1,7,1).std((0,2)).reshape(1,7,1)+1e-6
    Xtr=np.nan_to_num((Ac-mu)/sd); Xte=np.nan_to_num((chans(Ate)-mu)/sd)
    xt=torch.tensor(Xtr,device=DEV); yt=torch.tensor(ytr,device=DEV); xe=torch.tensor(Xte,device=DEV)
    m=CNN().to(DEV); opt=torch.optim.AdamW(m.parameters(),1e-3,weight_decay=1e-4); sch=torch.optim.lr_scheduler.CosineAnnealingLR(opt,50); lf=nn.CrossEntropyLoss(label_smoothing=.05)
    for ep in range(50):
        m.train(); p=torch.randperm(len(xt),device=DEV)
        for i in range(0,len(xt),512): b=p[i:i+512]; opt.zero_grad(); lf(m(xt[b]),yt[b]).backward(); opt.step()
        sch.step()
    m.eval()
    with torch.no_grad(): pr=np.concatenate([m(xe[i:i+8192]).argmax(1).cpu().numpy() for i in range(0,len(xe),8192)])
    return pr

print("building...",flush=True); A,y,g=build(); print(f"windows={len(y)}",flush=True)
rng=np.random.default_rng(0)
HO={16,17,18,19}; te=np.isin(g,list(HO)); tr=~te
print(f"train={tr.sum()} test={te.sum()}",flush=True)
for tag,aug in [("BASELINE",False),("EQUITY-AUG",True)]:
    t=time.time()
    if aug: Atr,ytr=augment(A[tr],y[tr],rng,k=3,scale=0.25)
    else: Atr,ytr=A[tr],y[tr]
    pr=fit_eval(Atr,ytr,A[te],y[te])
    f1=f1_score(y[te],pr,average=None,labels=range(19)); macro=f1.mean()
    hard=f1[HARD].mean(); easy=np.delete(f1,HARD).mean()
    print(f"[{tag}] macro={macro:.4f} hard-class={hard:.4f} easy-class={easy:.4f} (n_train={len(ytr)} {time.time()-t:.0f}s)",flush=True)
    if tag=="BASELINE": bf1=f1.copy()
print("--- per-hard-class delta (EQUITY - BASELINE) ---",flush=True)
for c in HARD: print(f"  {N[c]:11s} {bf1[c]:.3f} -> {f1[c]:.3f}  ({f1[c]-bf1[c]:+.3f})",flush=True)
print("=== gate: if hard-class macro rises, the ANNY body-model synth is greenlit ===",flush=True)
