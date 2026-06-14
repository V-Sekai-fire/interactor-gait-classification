"""SERIOUS video model on frozen VideoMAE features (the lever I prematurely abandoned at 0.475).
Fully INDUCTIVE (no cross-test-window info -> no 'time travel' cheating): a per-window transformer
over the 15 frames + CLS + positional encoding, heavy feature augmentation, and a domain-adversarial
SUBJECT head (gradient reversal) that strips the scene/subject confound AT TRAINING TIME (so we don't
need illegitimate test-time per-subject norm). Held-out subj16-19, video-ALONE macro-F1 vs 0.475.
If this breaks past ~0.55, frozen video was undermodeled and Hypothesis A (video is the lever) is live.
"""
import numpy as np, pandas as pd, glob, os, torch, torch.nn as nn, time
from sklearn.metrics import f1_score
LM={'null':0,'jogging':1,'jogging (rotating arms)':2,'jogging (skipping)':3,'jogging (sidesteps)':4,'jogging (butt-kicks)':5,'stretching (triceps)':6,'stretching (lunging)':7,'stretching (shoulders)':8,'stretching (hamstrings)':9,'stretching (lumbar rotation)':10,'push-ups':11,'push-ups (complex)':12,'sit-ups':13,'sit-ups (complex)':14,'burpees':15,'lunges':16,'lunges (complex)':17,'bench-dips':18}
DEV="cuda"; STRIDE=25
def build():
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

class GRL(torch.autograd.Function):
    @staticmethod
    def forward(ctx,x,lamb): ctx.lamb=lamb; return x.view_as(x)
    @staticmethod
    def backward(ctx,gr): return -ctx.lamb*gr,None

class VidT(nn.Module):
    def __init__(s,nsubj,d=256,L=4,H=8):
        super().__init__()
        s.proj=nn.Linear(768,d); s.cls=nn.Parameter(torch.zeros(1,1,d)); s.pos=nn.Parameter(torch.zeros(1,16,d))
        enc=nn.TransformerEncoderLayer(d,H,dim_feedforward=2*d,dropout=0.3,batch_first=True,activation='gelu')
        s.enc=nn.TransformerEncoder(enc,L); s.drop=nn.Dropout(0.4)
        s.head=nn.Sequential(nn.LayerNorm(d),nn.Linear(d,d),nn.GELU(),nn.Dropout(.4),nn.Linear(d,19))
        s.subj=nn.Sequential(nn.Linear(d,d),nn.GELU(),nn.Linear(d,nsubj))
    def forward(s,x,lamb=0.0):
        z=s.proj(x); b=z.shape[0]
        z=torch.cat([s.cls.expand(b,-1,-1),z],1)   # (b,16,d): CLS + 15 frames
        z=z+s.pos[:,:z.shape[1]]                    # positional encoding over 16 tokens
        h=s.enc(z)[:,0]; h=s.drop(h)               # CLS token
        return s.head(h), s.subj(GRL.apply(h,lamb))

def aug(x,rng):  # frame-mask + mixup + noise, feature space
    x=x.clone()
    m=(torch.rand(x.shape[0],x.shape[1],1,device=x.device)>0.15).float(); x=x*m   # mask 15% frames
    if rng.random()<0.5:                                                          # mixup
        p=torch.randperm(x.shape[0],device=x.device); lam=0.7+0.3*torch.rand(x.shape[0],1,1,device=x.device)
        x=lam*x+(1-lam)*x[p]
    x=x+0.05*torch.randn_like(x)
    return x

def run(Vtr,ytr,gtr,Vte,yte,epochs=120):
    subs=sorted(set(gtr.tolist())); s2i={s:i for i,s in enumerate(subs)}; gs=np.array([s2i[s] for s in gtr])
    mu=Vtr.reshape(-1,768).mean(0); sd=Vtr.reshape(-1,768).std(0)+1e-6
    Xtr=((Vtr-mu)/sd).astype(np.float32); Xte=((Vte-mu)/sd).astype(np.float32)
    m=VidT(len(subs)).to(DEV); opt=torch.optim.AdamW(m.parameters(),1.5e-3,weight_decay=5e-2)
    sch=torch.optim.lr_scheduler.CosineAnnealingLR(opt,epochs); lf=nn.CrossEntropyLoss(label_smoothing=.1)
    xt=torch.tensor(Xtr,device=DEV); yt=torch.tensor(ytr,device=DEV); st=torch.tensor(gs,device=DEV)
    rng=np.random.default_rng(0); t=time.time()
    for ep in range(epochs):
        m.train(); p=torch.randperm(len(xt),device=DEV); lamb=0.3*min(1.0,ep/40)  # ramp adversary
        for i in range(0,len(xt),256):
            b=p[i:i+256]; opt.zero_grad()
            xa=aug(xt[b],rng); ya,sa=m(xa,lamb)
            loss=lf(ya,yt[b])+0.3*lf(sa,st[b]); loss.backward(); opt.step()
        sch.step()
    m.eval()
    with torch.no_grad():
        xe=torch.tensor(Xte,device=DEV); pr=np.concatenate([m(xe[i:i+4096])[0].argmax(1).cpu().numpy() for i in range(0,len(xe),4096)])
    return f1_score(yte,pr,average="macro"),time.time()-t

print("building 15-frame video...",flush=True); V,y,g=build(); print(f"windows={len(y)} V={V.shape}",flush=True)
HO={16,17,18,19}; te=np.isin(g,list(HO)); tr=~te
f,dt=run(V[tr].astype(np.float32),y[tr],g[tr],V[te].astype(np.float32),y[te])
print(f"=== SERIOUS video-alone (transformer+adv+aug) held-out F1={f:.4f}  ({dt:.0f}s)  [BiGRU was 0.475] ===",flush=True)
print("if >>0.475 -> frozen video was undermodeled; promote to LOSO + fuse with inertial toward rank-1",flush=True)
