"""ORIENTATION AS A FIRST-CLASS FEATURE (the limb always falls -> always reads gravity -> orientation).
My CNN under-used static orientation (global pooling washes out absolute gravity direction). Here we
EXPLICITLY compute, per window: gravity direction (3D unit = pitch/roll), the 6D-recovered orthonormal
basis (gravity as axis-1, principal linear-accel direction as axis-2, Gram-Schmidt + cross -> 3x3=9D),
and gravity magnitude. These go to an MLP, FUSED with the temporal CNN (motion). Tests the claim that
'idle' limbs (plank legs in push-ups, bent legs in lunges) are recoverable by orientation. Held-out
subj16-19; report macro + hard-class + the push/sit/lunge leg-window recovery vs raw CNN baseline.
"""
import numpy as np, pandas as pd, glob, torch, torch.nn as nn, time
from sklearn.metrics import f1_score
LM={'null':0,'jogging':1,'jogging (rotating arms)':2,'jogging (skipping)':3,'jogging (sidesteps)':4,'jogging (butt-kicks)':5,'stretching (triceps)':6,'stretching (lunging)':7,'stretching (shoulders)':8,'stretching (hamstrings)':9,'stretching (lumbar rotation)':10,'push-ups':11,'push-ups (complex)':12,'sit-ups':13,'sit-ups (complex)':14,'burpees':15,'lunges':16,'lunges (complex)':17,'bench-dips':18}
LIMBS=[["right_arm_acc_x","right_arm_acc_y","right_arm_acc_z"],["right_leg_acc_x","right_leg_acc_y","right_leg_acc_z"],["left_leg_acc_x","left_leg_acc_y","left_leg_acc_z"],["left_arm_acc_x","left_arm_acc_y","left_arm_acc_z"]]
HARD=[6,7,8,9,11,12,13,16,17,18]; DEV="cuda"; STRIDE=25
def build():
    A,Y,G,L=[],[],[],[]
    for csv in sorted(glob.glob("train/inertial_feat/sbj_*.csv")):
        df=pd.read_csv(csv,low_memory=False); sbj=int(df.sbj_id.iloc[0]); lab=df.label.fillna("null").astype(str).values
        arrs=[np.nan_to_num(df[c].values.astype(np.float32)) for c in LIMBS]
        for k in range(0,len(df)-50,STRIDE):
            seg=lab[k:k+50]; v,c=np.unique(seg,return_counts=True)
            if c.max()<40: continue
            lbl=LM[v[c.argmax()]]
            for li,a in enumerate(arrs): A.append(a[k:k+50]); Y.append(lbl); G.append(sbj); L.append(li)
    return np.array(A,np.float32),np.array(Y),np.array(G),np.array(L)
def temporal_ch(A):  # 7ch motion: xyz + mag + jerk
    mag=np.sqrt((A**2).sum(2,keepdims=True)); jerk=np.concatenate([np.zeros((len(A),1,3),np.float32),np.diff(A,axis=1)],1)
    return np.concatenate([A,mag,jerk],2).transpose(0,2,1)
def orient_feats(A):  # explicit orientation: gravity dir (3) + 6D basis (9) + |g| (1) = 13
    g=A.mean(1); gn=np.linalg.norm(g,axis=1,keepdims=True)+1e-6; b1=g/gn          # gravity axis (pitch/roll)
    lin=A-A.mean(1,keepdims=True)                                                 # linear accel
    # principal linear direction (second axis) via max-variance sample direction
    a2=lin[np.arange(len(A)),np.abs(lin).sum(2).argmax(1)]                        # accel dir at peak motion
    a2=a2-(b1*a2).sum(1,keepdims=True)*b1; n2=np.linalg.norm(a2,axis=1,keepdims=True)
    b2=np.where(n2>1e-3,a2/(n2+1e-6),np.roll(b1,1,axis=1))                        # Gram-Schmidt (fallback if static)
    b2=b2-(b1*b2).sum(1,keepdims=True)*b1; b2=b2/(np.linalg.norm(b2,axis=1,keepdims=True)+1e-6)
    b3=np.cross(b1,b2)                                                            # cross product completes basis
    return np.concatenate([b1,b1,b2,b3,gn],1).astype(np.float32)                 # 3+3+3+3+1=13
class HybridCNN(nn.Module):
    def __init__(s,odim=13):
        super().__init__()
        s.cnn=nn.Sequential(nn.Conv1d(7,64,7,padding=3),nn.BatchNorm1d(64),nn.ReLU(),nn.MaxPool1d(2),
            nn.Conv1d(64,128,5,padding=2),nn.BatchNorm1d(128),nn.ReLU(),nn.MaxPool1d(2),
            nn.Conv1d(128,128,3,padding=1),nn.BatchNorm1d(128),nn.ReLU(),nn.AdaptiveAvgPool1d(1),nn.Flatten())
        s.ori=nn.Sequential(nn.Linear(odim,64),nn.BatchNorm1d(64),nn.ReLU(),nn.Linear(64,64),nn.ReLU())
        s.head=nn.Sequential(nn.Dropout(.3),nn.Linear(128+64,19))
    def forward(s,x,o): return s.head(torch.cat([s.cnn(x),s.ori(o)],1))
class RawCNN(nn.Module):
    def __init__(s): super().__init__(); s.n=nn.Sequential(nn.Conv1d(7,64,7,padding=3),nn.BatchNorm1d(64),nn.ReLU(),nn.MaxPool1d(2),
        nn.Conv1d(64,128,5,padding=2),nn.BatchNorm1d(128),nn.ReLU(),nn.MaxPool1d(2),
        nn.Conv1d(128,128,3,padding=1),nn.BatchNorm1d(128),nn.ReLU(),nn.AdaptiveAvgPool1d(1),nn.Flatten(),nn.Dropout(.3),nn.Linear(128,19))
    def forward(s,x,o=None): return s.n(x)
def fit_eval(Model,Xc,Xo,y,tr,te,hybrid):
    m=Model().to(DEV); opt=torch.optim.AdamW(m.parameters(),1e-3,weight_decay=1e-4); sch=torch.optim.lr_scheduler.CosineAnnealingLR(opt,45); lf=nn.CrossEntropyLoss(label_smoothing=.05)
    xc=torch.tensor(Xc[tr],device=DEV); xo=torch.tensor(Xo[tr],device=DEV); yt=torch.tensor(y[tr],device=DEV)
    for ep in range(45):
        m.train(); p=torch.randperm(len(xc),device=DEV)
        for i in range(0,len(xc),512):
            b=p[i:i+512]; opt.zero_grad(); lf(m(xc[b],xo[b]),yt[b]).backward(); opt.step()
        sch.step()
    m.eval(); xce=torch.tensor(Xc[te],device=DEV); xoe=torch.tensor(Xo[te],device=DEV)
    with torch.no_grad(): pr=np.concatenate([m(xce[i:i+8192],xoe[i:i+8192]).argmax(1).cpu().numpy() for i in range(0,te.sum(),8192)])
    return pr
print("building...",flush=True); A,y,g,L=build()
Xc=temporal_ch(A); Xo=orient_feats(A)
mc=Xc.mean((0,2),keepdims=True); sc=Xc.std((0,2),keepdims=True)+1e-6; Xc=np.nan_to_num((Xc-mc)/sc)
mo=Xo.mean(0,keepdims=True); so=Xo.std(0,keepdims=True)+1e-6; Xo=np.nan_to_num((Xo-mo)/so)
HO={16,17,18,19}; te=np.isin(g,list(HO)); tr=~te
for tag,Model,hyb in [("RAW-CNN (7ch)",RawCNN,False),("HYBRID +orient6D",HybridCNN,True)]:
    t=time.time(); pr=fit_eval(Model,Xc,Xo,y,tr,te,hyb)
    f1=f1_score(y[te],pr,average=None,labels=range(19))
    # push/sit/lunge LEG-window recovery (limbs 1,2 = legs)
    legmask=te&np.isin(L,[1,2])&np.isin(y,[11,12,13,14,16,17])
    legrec=f1_score(y[legmask],pr[(np.isin(L,[1,2])&np.isin(y,[11,12,13,14,16,17]))[te]],average='macro') if legmask.sum() else 0
    print(f"[{tag:18s}] macro={f1.mean():.4f} hard={f1[HARD].mean():.4f} (push/sit/lunge LEG-win F1={legrec:.4f}) {time.time()-t:.0f}s",flush=True)
print("=== if HYBRID hard >> RAW hard, explicit orientation recovers the 'idle'-limb static poses ===",flush=True)
