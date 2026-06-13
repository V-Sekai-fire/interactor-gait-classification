"""LOSO-fusion harness — one-time cache.
Runs leave-one-subject-out for the inertial CNN, saving each held-out fold's PROBABILITIES (not just
argmax) into a full (N,19) array, plus the pooled video features (mean|max|std = 2304) + labels + subjects.
After this, any video method is a cheap LOSO sweep: train video-MLP per fold, fuse vs the cached inertial
probs, score — no inertial retraining. -> loso_cache.npz
"""
import numpy as np, pandas as pd, glob, os, torch, torch.nn as nn, time
from sklearn.metrics import f1_score
LM={'null':0,'jogging':1,'jogging (rotating arms)':2,'jogging (skipping)':3,'jogging (sidesteps)':4,'jogging (butt-kicks)':5,'stretching (triceps)':6,'stretching (lunging)':7,'stretching (shoulders)':8,'stretching (hamstrings)':9,'stretching (lumbar rotation)':10,'push-ups':11,'push-ups (complex)':12,'sit-ups':13,'sit-ups (complex)':14,'burpees':15,'lunges':16,'lunges (complex)':17,'bench-dips':18}
LIMBS=[["right_arm_acc_x","right_arm_acc_y","right_arm_acc_z"],["right_leg_acc_x","right_leg_acc_y","right_leg_acc_z"],["left_leg_acc_x","left_leg_acc_y","left_leg_acc_z"],["left_arm_acc_x","left_arm_acc_y","left_arm_acc_z"]]
DEV="cuda"; STRIDE=25

def build():
    A,V,Y,G=[],[],[],[]
    for csv in sorted(glob.glob("train/inertial_feat/sbj_*.csv")):
        stem=os.path.basename(csv)[:-4]; vp=f"train/videomae_feat/{stem}.npy"
        if not os.path.exists(vp): continue
        df=pd.read_csv(csv, low_memory=False); sbj=int(df.sbj_id.iloc[0]); lab=df.label.fillna("null").astype(str).values
        vid=np.load(vp,mmap_mode="r"); arrs=[np.nan_to_num(df[c].values.astype(np.float32)) for c in LIMBS]
        for k in range(0,len(df)-50,STRIDE):
            seg=lab[k:k+50]; v,c=np.unique(seg,return_counts=True)
            if c.max()<40: continue
            vs=int(k*0.6)+7
            if vs+15>vid.shape[0]: continue
            w=np.asarray(vid[vs:vs+15]); vp3=np.concatenate([w.mean(0),w.max(0),w.std(0)]).astype(np.float32)
            lbl=LM[v[c.argmax()]]
            for a in arrs: A.append(a[k:k+50]); V.append(vp3); Y.append(lbl); G.append(sbj)
    return np.array(A,np.float32),np.array(V,np.float32),np.array(Y),np.array(G)

def chans(A):
    mag=np.sqrt((A**2).sum(2,keepdims=True)); jerk=np.concatenate([np.zeros((len(A),1,3),np.float32),np.diff(A,axis=1)],1)
    return np.concatenate([A,mag,jerk],2).transpose(0,2,1)

class CNN(nn.Module):
    def __init__(s): super().__init__(); s.n=nn.Sequential(nn.Conv1d(7,64,7,padding=3),nn.BatchNorm1d(64),nn.ReLU(),nn.MaxPool1d(2),
        nn.Conv1d(64,128,5,padding=2),nn.BatchNorm1d(128),nn.ReLU(),nn.MaxPool1d(2),
        nn.Conv1d(128,128,3,padding=1),nn.BatchNorm1d(128),nn.ReLU(),nn.AdaptiveAvgPool1d(1),nn.Flatten(),nn.Dropout(.3),nn.Linear(128,19))
    def forward(s,x): return s.n(x)

print("building...",flush=True); A,V,y,g=build(); Ac=chans(A); print(f"windows={len(y)} V={V.shape}",flush=True)
subs=sorted(set(g)); iprob=np.zeros((len(y),19),np.float32); f1s=[]
for s in subs:
    te=g==s; tr=~te
    mu=Ac[tr].reshape(-1,7,1).mean((0,2)).reshape(1,7,1); sd=Ac[tr].reshape(-1,7,1).std((0,2)).reshape(1,7,1)+1e-6
    Xn=np.nan_to_num((Ac-mu)/sd)
    xt=torch.tensor(Xn[tr],device=DEV); yt=torch.tensor(y[tr],device=DEV); xe=torch.tensor(Xn[te],device=DEV)
    m=CNN().to(DEV); opt=torch.optim.AdamW(m.parameters(),1e-3,weight_decay=1e-4); sch=torch.optim.lr_scheduler.CosineAnnealingLR(opt,50); lf=nn.CrossEntropyLoss(label_smoothing=.05); t=time.time()
    for ep in range(50):
        m.train(); p=torch.randperm(len(xt),device=DEV)
        for i in range(0,len(xt),512): b=p[i:i+512]; opt.zero_grad(); lf(m(xt[b]),yt[b]).backward(); opt.step()
        sch.step()
    m.eval()
    with torch.no_grad():
        pr=np.concatenate([torch.softmax(m(xe[i:i+8192]),1).cpu().numpy() for i in range(0,te.sum(),8192)])
    iprob[te]=pr; fs=f1_score(y[te],pr.argmax(1),average="macro"); f1s.append(fs)
    print(f"  fold sbj {s}: inertial F1={fs:.4f} ({time.time()-t:.0f}s)",flush=True)
print(f"=== inertial LOSO mean={np.mean(f1s):.4f}+/-{np.std(f1s):.4f} pooled={f1_score(y,iprob.argmax(1),average='macro'):.4f} ===",flush=True)
np.savez("loso_cache.npz", iprob=iprob, V=V, y=y, g=g)
print("saved loso_cache.npz (inertial fold-probs + video features) -> video methods now cheap",flush=True)
