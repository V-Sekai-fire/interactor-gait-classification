"""WHOLE-BODY DISTILLATION: ground the video in POSE, not scene.
Naive imu+video fusion fails (video carries scene, crowds out inertial -> 0.40-0.49 < single-limb 0.54).
Fix: a 12-tracker TEACHER (whole-body, 0.69) produces a pose-driven embedding e_wb per window (IMU-derived
-> no scene). The STUDENT's video branch is supervised to PREDICT e_wb (MSE) -> video must encode whole-body
pose, scene is useless for that target. Student = single-limb IMU emb + video->whole-body emb + limb-id -> 19.
At test (single limb + full-frame video) the video reconstructs the missing-limb context. Held-out subj16-19.
Target: beat single-limb 0.54, approach teacher 0.69 -> +0.072 LB transfer -> rank-1.
"""
import numpy as np, pandas as pd, glob, os, torch, torch.nn as nn, time
from sklearn.metrics import f1_score
LM={'null':0,'jogging':1,'jogging (rotating arms)':2,'jogging (skipping)':3,'jogging (sidesteps)':4,'jogging (butt-kicks)':5,'stretching (triceps)':6,'stretching (lunging)':7,'stretching (shoulders)':8,'stretching (hamstrings)':9,'stretching (lumbar rotation)':10,'push-ups':11,'push-ups (complex)':12,'sit-ups':13,'sit-ups (complex)':14,'burpees':15,'lunges':16,'lunges (complex)':17,'bench-dips':18}
COLS=["right_arm_acc_x","right_arm_acc_y","right_arm_acc_z","right_leg_acc_x","right_leg_acc_y","right_leg_acc_z","left_leg_acc_x","left_leg_acc_y","left_leg_acc_z","left_arm_acc_x","left_arm_acc_y","left_arm_acc_z"]
HARD=[6,7,8,9,11,12,13,16,17,18]; DEV="cuda"; STRIDE=25
def build():
    W,Vd,Y,G=[],[],[],[]
    for csv in sorted(glob.glob("train/inertial_feat/sbj_*.csv")):
        stem=os.path.basename(csv)[:-4]; vp=f"train/videomae_feat/{stem}.npy"
        if not os.path.exists(vp): continue
        df=pd.read_csv(csv,low_memory=False); sbj=int(df.sbj_id.iloc[0]); lab=df.label.fillna("null").astype(str).values
        M=np.nan_to_num(df[COLS].values.astype(np.float32)); vid=np.load(vp,mmap_mode="r")
        for k in range(0,len(df)-50,STRIDE):
            seg=lab[k:k+50]; v,c=np.unique(seg,return_counts=True)
            if c.max()<40: continue
            vs=int(k*0.6)+7
            if vs+15>vid.shape[0]: continue
            w=np.asarray(vid[vs:vs+15]); W.append(M[k:k+50]); Vd.append(np.concatenate([w.mean(0),w.max(0),w.std(0)]).astype(np.float32)); Y.append(LM[v[c.argmax()]]); G.append(sbj)
    return np.array(W,np.float32),np.array(Vd,np.float32),np.array(Y),np.array(G)
def ch12(A):  # 12 + 4 mag + 12 jerk = 28
    mags=[np.sqrt((A[:,:,3*i:3*i+3]**2).sum(2,keepdims=True)) for i in range(4)]
    jerk=np.concatenate([np.zeros((len(A),1,12),np.float32),np.diff(A,axis=1)],1)
    return np.concatenate([A]+mags+[jerk],2).transpose(0,2,1)
def ch7(A3):  # single limb (N,50,3) -> 7ch
    mag=np.sqrt((A3**2).sum(2,keepdims=True)); jerk=np.concatenate([np.zeros((len(A3),1,3),np.float32),np.diff(A3,axis=1)],1)
    return np.concatenate([A3,mag,jerk],2).transpose(0,2,1)
class Teacher(nn.Module):
    def __init__(s): super().__init__(); s.f=nn.Sequential(nn.Conv1d(28,96,7,padding=3),nn.BatchNorm1d(96),nn.ReLU(),nn.MaxPool1d(2),
        nn.Conv1d(96,192,5,padding=2),nn.BatchNorm1d(192),nn.ReLU(),nn.MaxPool1d(2),
        nn.Conv1d(192,192,3,padding=1),nn.BatchNorm1d(192),nn.ReLU(),nn.AdaptiveAvgPool1d(1),nn.Flatten()); s.h=nn.Linear(192,19)
    def emb(s,x): return s.f(x)
    def forward(s,x): return s.h(s.f(x))
class Student(nn.Module):
    def __init__(s,vdim):
        super().__init__()
        s.cnn=nn.Sequential(nn.Conv1d(7,64,7,padding=3),nn.BatchNorm1d(64),nn.ReLU(),nn.MaxPool1d(2),
            nn.Conv1d(64,128,5,padding=2),nn.BatchNorm1d(128),nn.ReLU(),nn.MaxPool1d(2),
            nn.Conv1d(128,128,3,padding=1),nn.BatchNorm1d(128),nn.ReLU(),nn.AdaptiveAvgPool1d(1),nn.Flatten())
        s.vid=nn.Sequential(nn.Linear(vdim,512),nn.BatchNorm1d(512),nn.ReLU(),nn.Dropout(.5),nn.Linear(512,192))  # -> predict e_wb
        s.limb=nn.Embedding(4,16)
        s.head=nn.Sequential(nn.ReLU(),nn.Dropout(.4),nn.Linear(128+192+16,256),nn.ReLU(),nn.Dropout(.4),nn.Linear(256,19))
    def forward(s,a,v,l):
        vp=s.vid(v); return s.head(torch.cat([s.cnn(a),vp,s.limb(l)],1)), vp
def fit_teacher(Xt,y,tr,ep=50):
    m=Teacher().to(DEV); opt=torch.optim.AdamW(m.parameters(),1e-3,weight_decay=1e-4); sch=torch.optim.lr_scheduler.CosineAnnealingLR(opt,ep); lf=nn.CrossEntropyLoss(label_smoothing=.05)
    xt=torch.tensor(Xt[tr],device=DEV); yt=torch.tensor(y[tr],device=DEV)
    for e in range(ep):
        m.train(); p=torch.randperm(len(xt),device=DEV)
        for i in range(0,len(xt),512): b=p[i:i+512]; opt.zero_grad(); lf(m(xt[b]),yt[b]).backward(); opt.step()
        sch.step()
    return m
print("building whole-body + video...",flush=True); W,Vd,y,g=build(); print(f"windows={len(y)}",flush=True)
X12=ch12(W); m12=X12.reshape(-1,28,1).mean((0,2)).reshape(1,28,1); s12=X12.reshape(-1,28,1).std((0,2)).reshape(1,28,1)+1e-6; X12=np.nan_to_num((X12-m12)/s12)
mv=Vd.mean(0); sv=Vd.std(0)+1e-6; Vn=((Vd-mv)/sv).astype(np.float32)  # inductive video norm
HO={16,17,18,19}; te=np.isin(g,list(HO)); tr=~te
# TEACHER (12-tracker)
t=time.time(); T=fit_teacher(X12,y,tr); T.eval()
with torch.no_grad():
    ewb=np.concatenate([T.emb(torch.tensor(X12[i:i+8192],device=DEV)).cpu().numpy() for i in range(0,len(X12),8192)])
    tp=np.concatenate([T(torch.tensor(X12[te][i:i+8192],device=DEV)).argmax(1).cpu().numpy() for i in range(0,te.sum(),8192)])
es=ewb.std(0)+1e-6; ewbn=ewb/es  # normalize distill target
print(f"[teacher 12-track] macro={f1_score(y[te],tp,average='macro'):.4f} ({time.time()-t:.0f}s)",flush=True)
# STUDENT: per-limb samples (single limb + video + limb-id), distilled to e_wb
def expand(idx):
    A,V,Yy,Ll,E=[],[],[],[],[]
    for li in range(4):
        A.append(W[idx][:,:,3*li:3*li+3]); V.append(Vn[idx]); Yy.append(y[idx]); Ll.append(np.full(idx.sum(),li)); E.append(ewbn[idx])
    return np.concatenate(A),np.concatenate(V),np.concatenate(Yy),np.concatenate(Ll),np.concatenate(E)
Atr,Vtr,ytr,Ltr,Etr=expand(tr); Ate,Vte,yte,Lte,_=expand(te)
Xctr=ch7(Atr); mc=Xctr.reshape(-1,7,1).mean((0,2)).reshape(1,7,1); sc=Xctr.reshape(-1,7,1).std((0,2)).reshape(1,7,1)+1e-6
Xctr=np.nan_to_num((Xctr-mc)/sc); Xcte=np.nan_to_num((ch7(Ate)-mc)/sc)
S=Student(Vtr.shape[1]).to(DEV); opt=torch.optim.AdamW(S.parameters(),1e-3,weight_decay=1e-4); sch=torch.optim.lr_scheduler.CosineAnnealingLR(opt,55)
ce=nn.CrossEntropyLoss(label_smoothing=.05); mse=nn.MSELoss(); t=time.time()
at=torch.tensor(Xctr,device=DEV); vt=torch.tensor(Vtr,device=DEV); lt=torch.tensor(Ltr,device=DEV); yt=torch.tensor(ytr,device=DEV); et=torch.tensor(Etr,device=DEV)
for e in range(55):
    S.train(); p=torch.randperm(len(at),device=DEV)
    for i in range(0,len(at),512):
        b=p[i:i+512]; opt.zero_grad(); out,vp=S(at[b],vt[b],lt[b]); (ce(out,yt[b])+1.0*mse(vp,et[b])).backward(); opt.step()
    sch.step()
S.eval(); ae=torch.tensor(Xcte,device=DEV); ve=torch.tensor(Vte,device=DEV); le=torch.tensor(Lte,device=DEV)
with torch.no_grad(): pr=np.concatenate([S(ae[i:i+8192],ve[i:i+8192],le[i:i+8192])[0].argmax(1).cpu().numpy() for i in range(0,len(ae),8192)])
f1=f1_score(yte,pr,average=None,labels=range(19))
print(f"[STUDENT distilled] macro={f1.mean():.4f} hard={f1[HARD].mean():.4f} ({time.time()-t:.0f}s)  [single-limb 0.54, teacher {f1_score(y[te],tp,average='macro'):.3f}]",flush=True)
print("=== if student >> 0.54, video distilled from whole-body teacher delivers the missing context ===",flush=True)
