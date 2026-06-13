import numpy as np, pandas as pd, glob, torch, torch.nn as nn, time
from sklearn.metrics import f1_score
LM={'null':0,'jogging':1,'jogging (rotating arms)':2,'jogging (skipping)':3,'jogging (sidesteps)':4,'jogging (butt-kicks)':5,'stretching (triceps)':6,'stretching (lunging)':7,'stretching (shoulders)':8,'stretching (hamstrings)':9,'stretching (lumbar rotation)':10,'push-ups':11,'push-ups (complex)':12,'sit-ups':13,'sit-ups (complex)':14,'burpees':15,'lunges':16,'lunges (complex)':17,'bench-dips':18}
LIMBS=[["right_arm_acc_x","right_arm_acc_y","right_arm_acc_z"],["right_leg_acc_x","right_leg_acc_y","right_leg_acc_z"],["left_leg_acc_x","left_leg_acc_y","left_leg_acc_z"],["left_arm_acc_x","left_arm_acc_y","left_arm_acc_z"]]
def windows(stride):
    Xs,ys,gs=[],[],[]
    for csv in sorted(glob.glob("train/inertial_feat/sbj_*.csv")):
        df=pd.read_csv(csv); sbj=int(df.sbj_id.iloc[0]); lab=df.label.fillna("null").astype(str).values
        for cols in LIMBS:
            a=np.nan_to_num(df[cols].values.astype(np.float32))
            for k in range(0,len(df)-50,stride):
                seg=lab[k:k+50]; v,c=np.unique(seg,return_counts=True)
                if c.max()<40: continue
                Xs.append(a[k:k+50]); ys.append(LM[v[c.argmax()]]); gs.append(sbj)
    return np.array(Xs,np.float32),np.array(ys),np.array(gs)
dev="cuda"; HO={16,17,18,19}
class CNN(nn.Module):
    def __init__(s): super().__init__(); s.n=nn.Sequential(nn.Conv1d(3,64,7,padding=3),nn.BatchNorm1d(64),nn.ReLU(),nn.MaxPool1d(2),nn.Conv1d(64,128,5,padding=2),nn.BatchNorm1d(128),nn.ReLU(),nn.MaxPool1d(2),nn.Conv1d(128,128,3,padding=1),nn.BatchNorm1d(128),nn.ReLU(),nn.AdaptiveAvgPool1d(1),nn.Flatten(),nn.Dropout(.3),nn.Linear(128,19))
    def forward(s,x): return s.n(x)
class DeepConvLSTM(nn.Module):
    def __init__(s):
        super().__init__(); s.c=nn.Sequential(nn.Conv1d(3,64,5,padding=2),nn.ReLU(),nn.Conv1d(64,64,5,padding=2),nn.ReLU(),nn.Conv1d(64,64,5,padding=2),nn.ReLU())
        s.l=nn.LSTM(64,128,2,batch_first=True,dropout=.3); s.f=nn.Linear(128,19)
    def forward(s,x): h=s.c(x).transpose(1,2); o,_=s.l(h); return s.f(o[:,-1])
class TinyHAR(nn.Module):  # compact conv + temporal self-attention pooling
    def __init__(s):
        super().__init__(); s.c=nn.Sequential(nn.Conv1d(3,64,5,padding=2),nn.BatchNorm1d(64),nn.ReLU(),nn.Conv1d(64,64,3,padding=1),nn.BatchNorm1d(64),nn.ReLU())
        s.att=nn.Linear(64,1); s.f=nn.Linear(64,19)
    def forward(s,x): h=s.c(x).transpose(1,2); w=torch.softmax(s.att(h),1); return s.f((w*h).sum(1))
class TCN(nn.Module):  # dilated causal-ish convs
    def __init__(s):
        super().__init__(); L=[]
        ch=[3,64,64,128]
        for i in range(3): L+=[nn.Conv1d(ch[i],ch[i+1],3,padding=2**i,dilation=2**i),nn.BatchNorm1d(ch[i+1]),nn.ReLU()]
        s.n=nn.Sequential(*L,nn.AdaptiveAvgPool1d(1),nn.Flatten(),nn.Dropout(.3),nn.Linear(128,19))
    def forward(s,x): return s.n(x)
class BiGRU(nn.Module):
    def __init__(s): super().__init__(); s.g=nn.GRU(3,96,2,batch_first=True,bidirectional=True,dropout=.3); s.f=nn.Linear(192,19)
    def forward(s,x): o,_=s.g(x.transpose(1,2)); return s.f(o.mean(1))
X,y,g=windows(25); te=np.isin(g,list(HO)); tr=~te
mu=X[tr].reshape(-1,3).mean(0); sd=X[tr].reshape(-1,3).std(0)+1e-6
Xn=np.nan_to_num((X-mu)/sd).transpose(0,2,1)
xt=torch.tensor(Xn[tr],device=dev); yt=torch.tensor(y[tr],device=dev); xe=torch.tensor(Xn[te],device=dev)
print(f"train_windows={tr.sum()} holdout={te.sum()} (stride25)",flush=True)
def fit(M):
    m=M().to(dev); opt=torch.optim.Adam(m.parameters(),1e-3); lf=nn.CrossEntropyLoss(label_smoothing=.05); t=time.time()
    for ep in range(40):
        m.train(); p=torch.randperm(len(xt),device=dev)
        for i in range(0,len(xt),512): b=p[i:i+512]; opt.zero_grad(); lf(m(xt[b]),yt[b]).backward(); opt.step()
    m.eval()
    with torch.no_grad(): prob=torch.softmax(torch.cat([m(xe[i:i+8192]) for i in range(0,len(xe),8192)]),1).cpu().numpy()
    return prob,time.time()-t
probs={}
for name,M in [("CNN",CNN),("DeepConvLSTM",DeepConvLSTM),("TinyHAR",TinyHAR),("TCN",TCN),("BiGRU",BiGRU)]:
    pr,dt=fit(M); probs[name]=pr
    print(f"  {name:13s} held-out_F1={f1_score(y[te],pr.argmax(1),average='macro'):.4f} ({dt:.0f}s)",flush=True)
# equity-prior ensemble (divide by class prior to floor minority classes) + plain avg
ens=sum(probs.values())/len(probs)
print(f"  ENSEMBLE(avg) F1={f1_score(y[te],ens.argmax(1),average='macro'):.4f}",flush=True)
prior=np.bincount(y[tr],minlength=19)/len(y[tr])
ens_eq=ens/ (prior+1e-6)
print(f"  ENSEMBLE(equity-prior) F1={f1_score(y[te],ens_eq.argmax(1),average='macro'):.4f}",flush=True)
