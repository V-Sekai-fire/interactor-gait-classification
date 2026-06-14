"""ORIENTATION LEVER (cheap ANNY-mechanism test). Static-pose signal lives in GRAVITY direction
(per-axis mean), AUC 0.9+ on the active limb. Test: explicitly split gravity (low-freq/window-mean
orientation) from linear accel, feed both as CNN channels (+ normalized gravity DIRECTION = pure
posture). If hard classes jump vs the 7ch baseline, orientation was underused -> ANNY (which generates
correct static limb orientation in 6D) is the amplifier. Held-out subj16-19. 7ch baseline vs 10ch grav.
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
def ch7(A):
    mag=np.sqrt((A**2).sum(2,keepdims=True)); jerk=np.concatenate([np.zeros((len(A),1,3),np.float32),np.diff(A,axis=1)],1)
    return np.concatenate([A,mag,jerk],2).transpose(0,2,1)
def ch10(A):  # gravity (window mean, broadcast) + linear(A-grav) + gravity unit-direction (pure posture)
    g=A.mean(1,keepdims=True); lin=A-g; gb=np.broadcast_to(g,A.shape)
    gdir=g/ (np.linalg.norm(g,axis=2,keepdims=True)+1e-6); gdirb=np.broadcast_to(gdir,A.shape)
    mag=np.sqrt((lin**2).sum(2,keepdims=True))
    return np.concatenate([lin,gb,gdirb,mag],2).transpose(0,2,1)  # 3+3+3+1=10
class CNN(nn.Module):
    def __init__(s,cin): super().__init__(); s.n=nn.Sequential(nn.Conv1d(cin,64,7,padding=3),nn.BatchNorm1d(64),nn.ReLU(),nn.MaxPool1d(2),
        nn.Conv1d(64,128,5,padding=2),nn.BatchNorm1d(128),nn.ReLU(),nn.MaxPool1d(2),
        nn.Conv1d(128,128,3,padding=1),nn.BatchNorm1d(128),nn.ReLU(),nn.AdaptiveAvgPool1d(1),nn.Flatten(),nn.Dropout(.3),nn.Linear(128,19))
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
    with torch.no_grad(): pr=np.concatenate([m(xe[i:i+8192]).argmax(1).cpu().numpy() for i in range(0,len(xe),8192)])
    f1=f1_score(y[te],pr,average=None,labels=range(19)); return f1
print("building...",flush=True); A,y,g=build(); HO={16,17,18,19}; te=np.isin(g,list(HO)); tr=~te
for tag,X,cin in [("7ch baseline",ch7(A),7),("10ch +gravity",ch10(A),10)]:
    t=time.time(); f1=fit_eval(X,y,tr,te,cin)
    print(f"[{tag:14s}] macro={f1.mean():.4f} hard={f1[HARD].mean():.4f} ({time.time()-t:.0f}s)",flush=True)
print("=== if 10ch hard>>7ch hard, explicit gravity-orientation is the lever -> build ANNY to generate it ===",flush=True)
