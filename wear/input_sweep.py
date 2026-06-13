import numpy as np, pandas as pd, glob, torch, torch.nn as nn, time
from sklearn.metrics import f1_score
LM={'null':0,'jogging':1,'jogging (rotating arms)':2,'jogging (skipping)':3,'jogging (sidesteps)':4,'jogging (butt-kicks)':5,'stretching (triceps)':6,'stretching (lunging)':7,'stretching (shoulders)':8,'stretching (hamstrings)':9,'stretching (lumbar rotation)':10,'push-ups':11,'push-ups (complex)':12,'sit-ups':13,'sit-ups (complex)':14,'burpees':15,'lunges':16,'lunges (complex)':17,'bench-dips':18}
LIMBS=[["right_arm_acc_x","right_arm_acc_y","right_arm_acc_z"],["right_leg_acc_x","right_leg_acc_y","right_leg_acc_z"],["left_leg_acc_x","left_leg_acc_y","left_leg_acc_z"],["left_arm_acc_x","left_arm_acc_y","left_arm_acc_z"]]
def windows(stride):
    Xs,ys,gs,ls=[],[],[],[]
    for csv in sorted(glob.glob("train/inertial_feat/sbj_*.csv")):
        df=pd.read_csv(csv); sbj=int(df.sbj_id.iloc[0]); lab=df.label.fillna("null").astype(str).values
        for li,cols in enumerate(LIMBS):
            a=np.nan_to_num(df[cols].values.astype(np.float32))
            for k in range(0,len(df)-50,stride):
                seg=lab[k:k+50]; v,c=np.unique(seg,return_counts=True)
                if c.max()<40: continue
                Xs.append(a[k:k+50]); ys.append(LM[v[c.argmax()]]); gs.append(sbj); ls.append(li)
    return np.array(Xs,np.float32),np.array(ys),np.array(gs),np.array(ls)
dev="cuda"; HO={16,17,18,19}
X,y,g,limb=windows(25); te=np.isin(g,list(HO)); tr=~te
mu=X[tr].reshape(-1,3).mean(0); sd=X[tr].reshape(-1,3).std(0)+1e-6
base=np.nan_to_num((X-mu)/sd)  # (N,50,3)
def add_channels(Z):  # +magnitude +jerk(3)
    mag=np.sqrt((Z**2).sum(2,keepdims=True))
    jerk=np.concatenate([np.zeros((len(Z),1,3),np.float32),np.diff(Z,axis=1)],1)
    return np.concatenate([Z,mag,jerk],2)  # (N,50,7)
class CNN(nn.Module):
    def __init__(s,cin,limb_emb=False):
        super().__init__(); s.le=limb_emb
        s.c=nn.Sequential(nn.Conv1d(cin,64,7,padding=3),nn.BatchNorm1d(64),nn.ReLU(),nn.MaxPool1d(2),nn.Conv1d(64,128,5,padding=2),nn.BatchNorm1d(128),nn.ReLU(),nn.MaxPool1d(2),nn.Conv1d(128,128,3,padding=1),nn.BatchNorm1d(128),nn.ReLU(),nn.AdaptiveAvgPool1d(1),nn.Flatten())
        if limb_emb: s.emb=nn.Embedding(4,16); s.f=nn.Linear(128+16,19)
        else: s.f=nn.Linear(128,19)
    def forward(s,x,l=None):
        h=s.c(x)
        if s.le: h=torch.cat([h,s.emb(l)],1)
        return s.f(h)
def fit(Xin,use_limb,tag):
    Xn=Xin.transpose(0,2,1); cin=Xn.shape[1]
    xt=torch.tensor(Xn[tr],device=dev); yt=torch.tensor(y[tr],device=dev); xe=torch.tensor(Xn[te],device=dev)
    lt=torch.tensor(limb[tr],device=dev); leN=torch.tensor(limb[te],device=dev)
    m=CNN(cin,use_limb).to(dev); opt=torch.optim.Adam(m.parameters(),1e-3); lf=nn.CrossEntropyLoss(label_smoothing=.05); t=time.time()
    for ep in range(40):
        m.train(); p=torch.randperm(len(xt),device=dev)
        for i in range(0,len(xt),512):
            b=p[i:i+512]; opt.zero_grad(); lf(m(xt[b],lt[b] if use_limb else None),yt[b]).backward(); opt.step()
    m.eval()
    with torch.no_grad(): pr=m(xe,leN if use_limb else None).argmax(1).cpu().numpy()
    print(f"  {tag:32s} F1={f1_score(y[te],pr,average='macro'):.4f} ({time.time()-t:.0f}s)",flush=True)
fit(base,False,"baseline 3ch")
fit(add_channels(base),False,"+magnitude+jerk (7ch)")
fit(base,True,"+sensor-location embed")
fit(add_channels(base),True,"+mag+jerk +sensor-location")
