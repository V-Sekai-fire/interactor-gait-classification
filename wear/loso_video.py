import numpy as np, torch, torch.nn as nn, time
from sklearn.metrics import f1_score
d=np.load("loso_cache.npz"); iprob=d["iprob"]; V=d["V"].astype(np.float32); y=d["y"]; g=d["g"]; dev="cuda"
subs=np.unique(g)
def losoF1(prob): return np.mean([f1_score(y[g==s],prob[g==s].argmax(1),average="macro") for s in subs])
print(f"inertial LOSO mean={losoF1(iprob):.4f}",flush=True)
# per-subject normalize video (subtract each subject's mean)
Vn=V.copy()
for s in subs: m=g==s; Vn[m]-=Vn[m].mean(0)
class VMLP(nn.Module):
    def __init__(s,d): super().__init__(); s.n=nn.Sequential(nn.Linear(d,512),nn.BatchNorm1d(512),nn.ReLU(),nn.Dropout(.5),nn.Linear(512,256),nn.ReLU(),nn.Dropout(.5),nn.Linear(256,19))
    def forward(s,x): return s.n(x)
vprob=np.zeros((len(y),19),np.float32); t0=time.time()
for s in subs:
    te=g==s; tr=~te
    mu=Vn[tr].mean(0); sd=Vn[tr].std(0)+1e-6; Z=((Vn-mu)/sd).astype(np.float32)
    xt=torch.tensor(Z[tr],device=dev); yt=torch.tensor(y[tr],device=dev); xe=torch.tensor(Z[te],device=dev)
    m=VMLP(V.shape[1]).to(dev); opt=torch.optim.AdamW(m.parameters(),1e-3,weight_decay=1e-4); lf=nn.CrossEntropyLoss(label_smoothing=.05)
    for ep in range(50):
        m.train(); p=torch.randperm(len(xt),device=dev)
        for i in range(0,len(xt),512): b=p[i:i+512]; opt.zero_grad(); lf(m(xt[b]),yt[b]).backward(); opt.step()
    m.eval()
    with torch.no_grad(): vprob[te]=np.concatenate([torch.softmax(m(xe[i:i+8192]),1).cpu().numpy() for i in range(0,te.sum(),8192)])
print(f"video LOSO mean={losoF1(vprob):.4f}  ({time.time()-t0:.0f}s)",flush=True)
for w in [0,.15,.2,.25,.3,.35,.4]:
    print(f"  fuse w_vid={w}: LOSO mean={losoF1((1-w)*iprob+w*vprob):.4f}",flush=True)
np.save("loso_vprob.npy",vprob)
