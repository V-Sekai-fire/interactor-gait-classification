"""DEEP ENSEMBLE on the legit single-limb stack: diverse architectures (CNN, TCN, BiGRU) on 10ch
gravity-orientation + equity 6D-aug + sqrt-balance, probability-averaged. Diversity decorrelates errors
-> macro-F1 lift over the solo CNN (0.5554 held-out). Validate held-out subj16-19, then full-data ->
submission_ensemble.csv.
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
def augment(A3,y,rng,k=3,sc=0.25):
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
class TCN(nn.Module):  # dilated temporal conv
    def __init__(s):
        super().__init__(); L=[]
        ch=[10,64,64,128,128]; d=[1,2,4,8]
        for i in range(4): L+=[nn.Conv1d(ch[i],ch[i+1],3,padding=d[i],dilation=d[i]),nn.BatchNorm1d(ch[i+1]),nn.ReLU(),nn.Dropout(.2)]
        s.n=nn.Sequential(*L,nn.AdaptiveAvgPool1d(1),nn.Flatten(),nn.Linear(128,19))
    def forward(s,x): return s.n(x)
class BiGRU(nn.Module):
    def __init__(s): super().__init__(); s.g=nn.GRU(10,96,2,batch_first=True,bidirectional=True,dropout=.2); s.h=nn.Sequential(nn.LayerNorm(192),nn.Dropout(.3),nn.Linear(192,19))
    def forward(s,x): o,_=s.g(x.transpose(1,2)); return s.h(o.mean(1))
def train(Model,A3,y,rng,mu,sd,w,epochs=50):
    Aa,ya=augment(A3,y,rng); Xtr=np.nan_to_num((ch10(Aa)-mu)/sd)
    m=Model().to(DEV); opt=torch.optim.AdamW(m.parameters(),1e-3,weight_decay=1e-4); sch=torch.optim.lr_scheduler.CosineAnnealingLR(opt,epochs)
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
MODELS=[("CNN",CNN),("TCN",TCN),("BiGRU",BiGRU)]
print("building...",flush=True); A,y,g=build(); rng=np.random.default_rng(0)
freq=np.bincount(y,minlength=19).astype(float); wsqrt=np.sqrt(freq.max()/freq)
HO={16,17,18,19}; te=np.isin(g,list(HO)); tr=~te
mu=ch10(A[tr]).mean((0,2),keepdims=True); sd=ch10(A[tr]).std((0,2),keepdims=True)+1e-6
acc=np.zeros((te.sum(),19))
for nm,M in MODELS:
    t=time.time(); m=train(M,A[tr],y[tr],rng,mu,sd,wsqrt); pv=probs(m,A[te],mu,sd); acc+=pv
    print(f"  [{nm}] solo held-out={f1_score(y[te],pv.argmax(1),average='macro'):.4f} ({time.time()-t:.0f}s)",flush=True)
print(f"[ENSEMBLE held-out] macro={f1_score(y[te],acc.argmax(1),average='macro'):.4f}  (solo CNN 0.5554)",flush=True)
# full-data -> submission
muf=ch10(A).mean((0,2),keepdims=True); sdf=ch10(A).std((0,2),keepdims=True)+1e-6
ti=np.load("test/test_inertial_data.npy",allow_pickle=True).astype(np.float32); tacc=np.zeros((len(ti),19))
for nm,M in MODELS:
    mf=train(M,A,y,rng,muf,sdf,wsqrt); tacc+=probs(mf,ti,muf,sdf)
pred=tacc.argmax(1)
ss=pd.read_csv("sample_submission.csv"); ss["target_feature"]=pred.astype(int); ss.to_csv("submissions/submission_ensemble.csv",index=False)
print(f"wrote submissions/submission_ensemble.csv dist={dict(sorted(pd.Series(pred).value_counts().items()))}",flush=True)
print("=== deep ensemble banked ===",flush=True)
