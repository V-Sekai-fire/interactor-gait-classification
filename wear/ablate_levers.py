"""Isolate the 'exhaust' levers (CNN-only, held-out subj16-19) to find which actually help vs the
0.558 base. Base = 10ch + equity-aug + sqrt-balance. Test: +limb-conditioning, +TTA(jitter-only),
+relaxed-window-filter (keep ALL windows like the test distribution, per the starter kernel).
"""
import numpy as np, pandas as pd, glob, torch, torch.nn as nn, time
from sklearn.metrics import f1_score
LM={'null':0,'jogging':1,'jogging (rotating arms)':2,'jogging (skipping)':3,'jogging (sidesteps)':4,'jogging (butt-kicks)':5,'stretching (triceps)':6,'stretching (lunging)':7,'stretching (shoulders)':8,'stretching (hamstrings)':9,'stretching (lumbar rotation)':10,'push-ups':11,'push-ups (complex)':12,'sit-ups':13,'sit-ups (complex)':14,'burpees':15,'lunges':16,'lunges (complex)':17,'bench-dips':18}
LN=["right_arm","right_leg","left_leg","left_arm"]; LIMBS=[[f"{n}_acc_x",f"{n}_acc_y",f"{n}_acc_z"] for n in LN]
HARD=[6,7,8,9,11,12,13,16,17,18]; DEV="cuda"; STRIDE=25
def build(relax=False):
    A,Y,G,L=[],[],[],[]
    for csv in sorted(glob.glob("train/inertial_feat/sbj_*.csv")):
        df=pd.read_csv(csv,low_memory=False); sbj=int(df.sbj_id.iloc[0]); lab=df.label.fillna("null").astype(str).values
        arrs=[np.nan_to_num(df[c].values.astype(np.float32)) for c in LIMBS]
        for k in range(0,len(df)-50,STRIDE):
            seg=lab[k:k+50]; v,c=np.unique(seg,return_counts=True)
            if not relax and c.max()<40: continue
            lbl=LM[v[c.argmax()]]
            for li,a in enumerate(arrs): A.append(a[k:k+50]); Y.append(lbl); G.append(sbj); L.append(li)
    return np.array(A,np.float32),np.array(Y),np.array(G),np.array(L)
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
def aug(A3,y,Ls,rng,k=3,sc=0.25):
    m=np.isin(y,HARD); Ah=A3[m]; yh=y[m]; Lh=Ls[m]; oA=[A3]; oY=[y]; oL=[Ls]
    for _ in range(k):
        R=rot6d(len(Ah),rng,sc); Ar=np.einsum('nij,ntj->nti',R,Ah).astype(np.float32)
        Ar=Ar*rng.uniform(0.85,1.15,(len(Ah),1,1)).astype(np.float32)+rng.normal(0,0.02,Ah.shape).astype(np.float32)
        oA.append(Ar); oY.append(yh); oL.append(Lh)
    return np.concatenate(oA),np.concatenate(oY),np.concatenate(oL)
class CNN(nn.Module):
    def __init__(s,limb=False):
        super().__init__(); s.use=limb
        s.f=nn.Sequential(nn.Conv1d(10,64,7,padding=3),nn.BatchNorm1d(64),nn.ReLU(),nn.MaxPool1d(2),nn.Conv1d(64,128,5,padding=2),nn.BatchNorm1d(128),nn.ReLU(),nn.MaxPool1d(2),nn.Conv1d(128,128,3,padding=1),nn.BatchNorm1d(128),nn.ReLU(),nn.AdaptiveAvgPool1d(1),nn.Flatten())
        if limb: s.emb=nn.Embedding(4,8); s.h=nn.Sequential(nn.Dropout(.3),nn.Linear(136,19))
        else: s.h=nn.Sequential(nn.Dropout(.3),nn.Linear(128,19))
    def forward(s,x,l):
        z=s.f(x); return s.h(torch.cat([z,s.emb(l)],1)) if s.use else s.h(z)
def fit(A3,y,Ls,rng,mu,sd,w,limb):
    Aa,ya,La=aug(A3,y,Ls,rng); X=np.nan_to_num((ch10(Aa)-mu)/sd)
    m=CNN(limb).to(DEV); opt=torch.optim.AdamW(m.parameters(),1e-3,weight_decay=1e-4); sch=torch.optim.lr_scheduler.CosineAnnealingLR(opt,50)
    lf=nn.CrossEntropyLoss(label_smoothing=.05,weight=torch.tensor(w,device=DEV,dtype=torch.float32))
    xt=torch.tensor(X,device=DEV); yt=torch.tensor(ya,device=DEV); lt=torch.tensor(La,device=DEV)
    for ep in range(50):
        m.train(); p=torch.randperm(len(xt),device=DEV)
        for i in range(0,len(xt),512): b=p[i:i+512]; opt.zero_grad(); lf(m(xt[b],lt[b]),yt[b]).backward(); opt.step()
        sch.step()
    return m
def prob(m,A3,Ls,mu,sd,rng,tta=0):
    views=[A3]+[A3+rng.normal(0,0.03,A3.shape).astype(np.float32) for _ in range(tta)]  # jitter-only TTA
    m.eval(); acc=np.zeros((len(A3),19)); lt=torch.tensor(Ls,device=DEV)
    with torch.no_grad():
        for vw in views:
            X=np.nan_to_num((ch10(vw)-mu)/sd); xt=torch.tensor(X,device=DEV)
            acc+=np.concatenate([torch.softmax(m(xt[i:i+8192],lt[i:i+8192]),1).cpu().numpy() for i in range(0,len(X),8192)])
    return acc/len(views)
def run(tag,A,y,g,L,rng,limb=False,tta=0):
    HO={16,17,18,19}; te=np.isin(g,list(HO)); tr=~te
    freq=np.bincount(y,minlength=19).astype(float); w=np.sqrt(freq.max()/freq)
    mu=ch10(A[tr]).mean((0,2),keepdims=True); sd=ch10(A[tr]).std((0,2),keepdims=True)+1e-6
    t=time.time(); m=fit(A[tr],y[tr],L[tr],rng,mu,sd,w,limb); pv=prob(m,A[te],L[te],mu,sd,rng,tta)
    print(f"[{tag:22s}] held-out={f1_score(y[te],pv.argmax(1),average='macro'):.4f} ({time.time()-t:.0f}s)",flush=True)
rng=np.random.default_rng(0)
print("building strict...",flush=True); A,y,g,L=build(False)
run("base (strict)",A,y,g,L,rng)
run("+limb",A,y,g,L,rng,limb=True)
run("+TTA(jitter x4)",A,y,g,L,rng,tta=4)
print("building relaxed (all windows)...",flush=True); Ar,yr,gr,Lr=build(True)
run("relaxed-window",Ar,yr,gr,Lr,rng)
print("=== pick the levers that beat base; drop the rest ===",flush=True)
