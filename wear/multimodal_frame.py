"""THE FRAME IS MULTIMODAL: single-limb IMU + full-frame video + limb-id, FUSED (not solo).
Test gives, per window: one limb's accel (50x3) + the whole-frame video (768x15, sees all 12 trackers'
worth of body) + sensor_location + sbj_id. Solo video=0.38, solo single-limb=0.54 both throw the frame
away. Here we fuse: inertial CNN branch (single limb) + video branch (whole-body context) + limb
embedding -> joint head. Target = the 12-tracker whole-body ceiling 0.69. Held-out subj16-19, INDUCTIVE
(global video norm, no per-subject 'time-travel'). Also an optional per-subject-norm (transductive) row.
"""
import numpy as np, pandas as pd, glob, os, torch, torch.nn as nn, time
from sklearn.metrics import f1_score
LM={'null':0,'jogging':1,'jogging (rotating arms)':2,'jogging (skipping)':3,'jogging (sidesteps)':4,'jogging (butt-kicks)':5,'stretching (triceps)':6,'stretching (lunging)':7,'stretching (shoulders)':8,'stretching (hamstrings)':9,'stretching (lumbar rotation)':10,'push-ups':11,'push-ups (complex)':12,'sit-ups':13,'sit-ups (complex)':14,'burpees':15,'lunges':16,'lunges (complex)':17,'bench-dips':18}
LIMBS=[["right_arm_acc_x","right_arm_acc_y","right_arm_acc_z"],["right_leg_acc_x","right_leg_acc_y","right_leg_acc_z"],["left_leg_acc_x","left_leg_acc_y","left_leg_acc_z"],["left_arm_acc_x","left_arm_acc_y","left_arm_acc_z"]]
HARD=[6,7,8,9,11,12,13,16,17,18]; DEV="cuda"; STRIDE=25
def build():
    A,V,Y,G,L=[],[],[],[],[]
    for csv in sorted(glob.glob("train/inertial_feat/sbj_*.csv")):
        stem=os.path.basename(csv)[:-4]; vp=f"train/videomae_feat/{stem}.npy"
        if not os.path.exists(vp): continue
        df=pd.read_csv(csv,low_memory=False); sbj=int(df.sbj_id.iloc[0]); lab=df.label.fillna("null").astype(str).values
        vid=np.load(vp,mmap_mode="r"); arrs=[np.nan_to_num(df[c].values.astype(np.float32)) for c in LIMBS]
        for k in range(0,len(df)-50,STRIDE):
            seg=lab[k:k+50]; v,c=np.unique(seg,return_counts=True)
            if c.max()<40: continue
            vs=int(k*0.6)+7
            if vs+15>vid.shape[0]: continue
            w=np.asarray(vid[vs:vs+15]); vp3=np.concatenate([w.mean(0),w.max(0),w.std(0)]).astype(np.float32)
            lbl=LM[v[c.argmax()]]
            for li,a in enumerate(arrs): A.append(a[k:k+50]); V.append(vp3); Y.append(lbl); G.append(sbj); L.append(li)
    return np.array(A,np.float32),np.array(V,np.float32),np.array(Y),np.array(G),np.array(L)
def chans(A):
    mag=np.sqrt((A**2).sum(2,keepdims=True)); jerk=np.concatenate([np.zeros((len(A),1,3),np.float32),np.diff(A,axis=1)],1)
    return np.concatenate([A,mag,jerk],2).transpose(0,2,1)
class Frame(nn.Module):
    def __init__(s,vdim):
        super().__init__()
        s.cnn=nn.Sequential(nn.Conv1d(7,64,7,padding=3),nn.BatchNorm1d(64),nn.ReLU(),nn.MaxPool1d(2),
            nn.Conv1d(64,128,5,padding=2),nn.BatchNorm1d(128),nn.ReLU(),nn.MaxPool1d(2),
            nn.Conv1d(128,128,3,padding=1),nn.BatchNorm1d(128),nn.ReLU(),nn.AdaptiveAvgPool1d(1),nn.Flatten())
        s.vid=nn.Sequential(nn.Linear(vdim,512),nn.BatchNorm1d(512),nn.ReLU(),nn.Dropout(.5),nn.Linear(512,256),nn.ReLU())
        s.limb=nn.Embedding(4,16)
        s.head=nn.Sequential(nn.Dropout(.4),nn.Linear(128+256+16,256),nn.ReLU(),nn.Dropout(.4),nn.Linear(256,19))
    def forward(s,a,v,l): return s.head(torch.cat([s.cnn(a),s.vid(v),s.limb(l)],1))
def run(Xc,V,y,L,tr,te,tag):
    m=Frame(V.shape[1]).to(DEV); opt=torch.optim.AdamW(m.parameters(),1e-3,weight_decay=1e-4); sch=torch.optim.lr_scheduler.CosineAnnealingLR(opt,55); lf=nn.CrossEntropyLoss(label_smoothing=.05)
    a=torch.tensor(Xc[tr],device=DEV); v=torch.tensor(V[tr],device=DEV); l=torch.tensor(L[tr],device=DEV); yt=torch.tensor(y[tr],device=DEV)
    t=time.time()
    for ep in range(55):
        m.train(); p=torch.randperm(len(a),device=DEV)
        for i in range(0,len(a),512):
            b=p[i:i+512]; opt.zero_grad(); lf(m(a[b],v[b],l[b]),yt[b]).backward(); opt.step()
        sch.step()
    m.eval(); ae=torch.tensor(Xc[te],device=DEV); ve=torch.tensor(V[te],device=DEV); le=torch.tensor(L[te],device=DEV)
    with torch.no_grad(): pr=np.concatenate([m(ae[i:i+8192],ve[i:i+8192],le[i:i+8192]).argmax(1).cpu().numpy() for i in range(0,te.sum(),8192)])
    f1=f1_score(y[te],pr,average=None,labels=range(19))
    print(f"[{tag:24s}] macro={f1.mean():.4f} hard={f1[HARD].mean():.4f} ({time.time()-t:.0f}s)  [single-limb 0.54, 12-track 0.69]",flush=True)
print("building multimodal frame...",flush=True); A,V,y,g,L=build(); Xc=chans(A)
mc=Xc.mean((0,2),keepdims=True); sc=Xc.std((0,2),keepdims=True)+1e-6; Xc=np.nan_to_num((Xc-mc)/sc)
HO={16,17,18,19}; te=np.isin(g,list(HO)); tr=~te
# inductive: global video norm
mv=V[tr].mean(0); sv=V[tr].std(0)+1e-6; Vi=((V-mv)/sv).astype(np.float32)
run(Xc,Vi,y,L,tr,te,"FRAME imu+video+limb")
# transductive: per-subject video norm (your call whether legit)
Vt=V.copy()
for s in np.unique(g): mm=g==s; Vt[mm]-=Vt[mm].mean(0)
Vt=((Vt-Vt[tr].mean(0))/(Vt[tr].std(0)+1e-6)).astype(np.float32)
run(Xc,Vt,y,L,tr,te,"FRAME + psn (transductive)")
print("=== if FRAME approaches 0.69, single-limb+video recovers whole-body context -> rank-1 path ===",flush=True)
