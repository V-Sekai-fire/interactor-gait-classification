"""SMOKING-LEVER PROBE: is the VideoMAE signal hiding in the TEMPORAL axis we keep pooling away?
We've only ever mean/max/std-pooled the (15,768) per-window video -> 0.40 F1. Here we keep the 15
frames and run a real sequence model (BiGRU + attention pool). One row PER WINDOW (not x4 limbs -
video is shared). Held-out subj 16-19. Apples-to-apples: pooled-MLP vs temporal, raw vs per-subj-norm.
If temporal video alone jumps 0.40 -> 0.6+, that's the rank-1 lever and everything reorients to it.
"""
import numpy as np, pandas as pd, glob, os, torch, torch.nn as nn, time
from sklearn.metrics import f1_score
LM={'null':0,'jogging':1,'jogging (rotating arms)':2,'jogging (skipping)':3,'jogging (sidesteps)':4,'jogging (butt-kicks)':5,'stretching (triceps)':6,'stretching (lunging)':7,'stretching (shoulders)':8,'stretching (hamstrings)':9,'stretching (lumbar rotation)':10,'push-ups':11,'push-ups (complex)':12,'sit-ups':13,'sit-ups (complex)':14,'burpees':15,'lunges':16,'lunges (complex)':17,'bench-dips':18}
DEV="cuda"; STRIDE=25

def build():  # one row PER WINDOW (video shared across limbs) -> (N,15,768) f16, y, g
    Vf,Y,G=[],[],[]
    for csv in sorted(glob.glob("train/inertial_feat/sbj_*.csv")):
        stem=os.path.basename(csv)[:-4]; vp=f"train/videomae_feat/{stem}.npy"
        if not os.path.exists(vp): continue
        df=pd.read_csv(csv,low_memory=False); sbj=int(df.sbj_id.iloc[0]); lab=df.label.fillna("null").astype(str).values
        vid=np.load(vp,mmap_mode="r")
        for k in range(0,len(df)-50,STRIDE):
            seg=lab[k:k+50]; v,c=np.unique(seg,return_counts=True)
            if c.max()<40: continue
            vs=int(k*0.6)+7
            if vs+15>vid.shape[0]: continue
            Vf.append(np.asarray(vid[vs:vs+15],np.float16)); Y.append(LM[v[c.argmax()]]); G.append(sbj)
    return np.stack(Vf),np.array(Y),np.array(G)

def psn(V,G):  # per-subject scene removal: subtract each subject's mean frame
    Vn=V.astype(np.float32).copy()
    for s in np.unique(G):
        m=G==s; Vn[m]-=Vn[m].reshape(-1,768).mean(0)
    return Vn

class Pool(nn.Module):  # baseline: mean|max|std pooled -> MLP (the 0.40 path)
    def __init__(s,d=768): super().__init__(); s.n=nn.Sequential(nn.Linear(3*d,512),nn.BatchNorm1d(512),nn.ReLU(),nn.Dropout(.5),nn.Linear(512,256),nn.ReLU(),nn.Dropout(.5),nn.Linear(256,19))
    def forward(s,x): p=torch.cat([x.mean(1),x.amax(1),x.std(1)],1); return s.n(p)

class Temporal(nn.Module):  # BiGRU over 15 frames + attention pool
    def __init__(s,d=768,h=256):
        super().__init__(); s.gru=nn.GRU(d,h,batch_first=True,bidirectional=True); s.attn=nn.Linear(2*h,1)
        s.head=nn.Sequential(nn.LayerNorm(2*h),nn.Dropout(.5),nn.Linear(2*h,256),nn.ReLU(),nn.Dropout(.5),nn.Linear(256,19))
    def forward(s,x):
        o,_=s.gru(x); w=torch.softmax(s.attn(o),1); return s.head((w*o).sum(1))

def run(Model,Xtr,ytr,Xte,yte,epochs=60,bs=256):
    m=Model().to(DEV); opt=torch.optim.AdamW(m.parameters(),1e-3,weight_decay=1e-4)
    sch=torch.optim.lr_scheduler.CosineAnnealingLR(opt,epochs); lf=nn.CrossEntropyLoss(label_smoothing=.05)
    xt=torch.tensor(Xtr,device=DEV); yt=torch.tensor(ytr,device=DEV); t=time.time()
    for ep in range(epochs):
        m.train(); p=torch.randperm(len(xt),device=DEV)
        for i in range(0,len(xt),bs): b=p[i:i+bs]; opt.zero_grad(); lf(m(xt[b]),yt[b]).backward(); opt.step()
        sch.step()
    m.eval(); out=[]
    with torch.no_grad():
        xe=torch.tensor(Xte,device=DEV)
        for i in range(0,len(xe),8192): out.append(m(xe[i:i+8192]).argmax(1).cpu().numpy())
    return f1_score(yte,np.concatenate(out),average="macro"),time.time()-t

print("building per-window 15-frame video...",flush=True); V,y,g=build()
print(f"windows={len(y)} V={V.shape} ({V.nbytes/1e9:.1f}GB f16)",flush=True)
HO={16,17,18,19}; te=np.isin(g,list(HO)); tr=~te
print(f"train={tr.sum()} test={te.sum()} (subj16-19)",flush=True)
for tag,Vx in [("raw",V.astype(np.float32)),("psn",psn(V,g))]:
    mu=Vx[tr].reshape(-1,768).mean(0); sd=Vx[tr].reshape(-1,768).std(0)+1e-6
    Z=((Vx-mu)/sd).astype(np.float32)
    fp,tp=run(Pool,Z[tr],y[tr],Z[te],y[te]); print(f"  [{tag}] POOLED-MLP  F1={fp:.4f} ({tp:.0f}s)",flush=True)
    ft,tt=run(Temporal,Z[tr],y[tr],Z[te],y[te]); print(f"  [{tag}] TEMPORAL    F1={ft:.4f} ({tt:.0f}s)  <-- {'SMOKING LEVER' if ft>0.55 else 'meh'}",flush=True)
print("=== probe done: temporal>>pooled means video temporal axis is the rank-1 lever ===",flush=True)
