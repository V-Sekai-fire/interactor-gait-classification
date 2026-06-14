"""WHAT DOES THE FULL 12-TRACKER CAPTURE SCORE? (the whole-body ceiling)
Training captures the entire body: 4 limbs x xyz = 12 synchronized channels per timestep, + full-frame
video. The single-limb framing is only how the TEST is sliced. Measure the macro-F1 of a model that
sees ALL 12 channels at once (whole-body pose) vs the single-limb 0.54. If 12ch >> single-limb, the
whole-body signal is the lever, and the path is to bring whole-body context to each single-limb test
window via the full-frame video (which sees all 12 trackers). Held-out subj16-19.
"""
import numpy as np, pandas as pd, glob, torch, torch.nn as nn, time
from sklearn.metrics import f1_score
LM={'null':0,'jogging':1,'jogging (rotating arms)':2,'jogging (skipping)':3,'jogging (sidesteps)':4,'jogging (butt-kicks)':5,'stretching (triceps)':6,'stretching (lunging)':7,'stretching (shoulders)':8,'stretching (hamstrings)':9,'stretching (lumbar rotation)':10,'push-ups':11,'push-ups (complex)':12,'sit-ups':13,'sit-ups (complex)':14,'burpees':15,'lunges':16,'lunges (complex)':17,'bench-dips':18}
COLS=["right_arm_acc_x","right_arm_acc_y","right_arm_acc_z","right_leg_acc_x","right_leg_acc_y","right_leg_acc_z","left_leg_acc_x","left_leg_acc_y","left_leg_acc_z","left_arm_acc_x","left_arm_acc_y","left_arm_acc_z"]
HARD=[6,7,8,9,11,12,13,16,17,18]; DEV="cuda"; STRIDE=25
def build():
    A,Y,G=[],[],[]
    for csv in sorted(glob.glob("train/inertial_feat/sbj_*.csv")):
        df=pd.read_csv(csv,low_memory=False); sbj=int(df.sbj_id.iloc[0]); lab=df.label.fillna("null").astype(str).values
        M=np.nan_to_num(df[COLS].values.astype(np.float32))   # (T,12) all limbs synced
        for k in range(0,len(df)-50,STRIDE):
            seg=lab[k:k+50]; v,c=np.unique(seg,return_counts=True)
            if c.max()<40: continue
            A.append(M[k:k+50]); Y.append(LM[v[c.argmax()]]); G.append(sbj)
    return np.array(A,np.float32),np.array(Y),np.array(G)
def chans(A):  # 12 limbs + per-limb mag(4) + jerk(12) = 28
    mags=[np.sqrt((A[:,:,3*i:3*i+3]**2).sum(2,keepdims=True)) for i in range(4)]
    jerk=np.concatenate([np.zeros((len(A),1,12),np.float32),np.diff(A,axis=1)],1)
    return np.concatenate([A]+mags+[jerk],2).transpose(0,2,1)
class CNN(nn.Module):
    def __init__(s,cin): super().__init__(); s.n=nn.Sequential(nn.Conv1d(cin,96,7,padding=3),nn.BatchNorm1d(96),nn.ReLU(),nn.MaxPool1d(2),
        nn.Conv1d(96,192,5,padding=2),nn.BatchNorm1d(192),nn.ReLU(),nn.MaxPool1d(2),
        nn.Conv1d(192,192,3,padding=1),nn.BatchNorm1d(192),nn.ReLU(),nn.AdaptiveAvgPool1d(1),nn.Flatten(),nn.Dropout(.3),nn.Linear(192,19))
    def forward(s,x): return s.n(x)
def fit_eval(X,y,tr,te,cin):
    mu=X[tr].reshape(-1,cin,1).mean((0,2)).reshape(1,cin,1); sd=X[tr].reshape(-1,cin,1).std((0,2)).reshape(1,cin,1)+1e-6
    Xn=np.nan_to_num((X-mu)/sd)
    xt=torch.tensor(Xn[tr],device=DEV); yt=torch.tensor(y[tr],device=DEV); xe=torch.tensor(Xn[te],device=DEV)
    m=CNN(cin).to(DEV); opt=torch.optim.AdamW(m.parameters(),1e-3,weight_decay=1e-4); sch=torch.optim.lr_scheduler.CosineAnnealingLR(opt,50); lf=nn.CrossEntropyLoss(label_smoothing=.05)
    for ep in range(50):
        m.train(); p=torch.randperm(len(xt),device=DEV)
        for i in range(0,len(xt),512): b=p[i:i+512]; opt.zero_grad(); lf(m(xt[b]),yt[b]).backward(); opt.step()
        sch.step()
    m.eval()
    with torch.no_grad(): pr=np.concatenate([m(xe[i:i+8192]).argmax(1).cpu().numpy() for i in range(0,te.sum(),8192)])
    return f1_score(y[te],pr,average=None,labels=range(19))
print("building 12-channel whole-body windows...",flush=True); A,y,g=build(); print(f"windows={len(y)} (one per time-slice, all 4 limbs)",flush=True)
Ac=chans(A); HO={16,17,18,19}; te=np.isin(g,list(HO)); tr=~te
t=time.time(); f1=fit_eval(Ac,y,tr,te,Ac.shape[1])
print(f"[FULL 12-tracker]  macro={f1.mean():.4f} hard={f1[HARD].mean():.4f}  ({time.time()-t:.0f}s)  [single-limb was 0.54]",flush=True)
print("=== if >> 0.54, whole-body capture is the lever; bring it to single-limb test via full-frame video ===",flush=True)
