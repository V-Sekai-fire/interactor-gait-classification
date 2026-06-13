"""WEAR multimodal fusion: inertial 1D-CNN branch (raw 50x3 + mag/jerk) + video MLP branch
(VideoMAE 768 mean over the aligned 15 frames) -> joint head. Overlap windows (stride 25).
Held-out eval (subj 16-19) + full-data train -> submission. The cheap gate showed late-fusion
0.408->0.483; this is the full learned-fusion version.
"""
import numpy as np, pandas as pd, glob, os, torch, torch.nn as nn, time
from sklearn.metrics import f1_score

LABEL_MAP = {'null':0,'jogging':1,'jogging (rotating arms)':2,'jogging (skipping)':3,'jogging (sidesteps)':4,
 'jogging (butt-kicks)':5,'stretching (triceps)':6,'stretching (lunging)':7,'stretching (shoulders)':8,
 'stretching (hamstrings)':9,'stretching (lumbar rotation)':10,'push-ups':11,'push-ups (complex)':12,
 'sit-ups':13,'sit-ups (complex)':14,'burpees':15,'lunges':16,'lunges (complex)':17,'bench-dips':18}
LIMBS = [["right_arm_acc_x","right_arm_acc_y","right_arm_acc_z"],["right_leg_acc_x","right_leg_acc_y","right_leg_acc_z"],
         ["left_leg_acc_x","left_leg_acc_y","left_leg_acc_z"],["left_arm_acc_x","left_arm_acc_y","left_arm_acc_z"]]
DEV="cuda"; STRIDE=25


def build(stride=STRIDE):
    A,V,Y,G=[],[],[],[]
    for csv in sorted(glob.glob("train/inertial_feat/sbj_*.csv")):
        stem=os.path.basename(csv)[:-4]; vp=f"train/videomae_feat/{stem}.npy"
        if not os.path.exists(vp): continue
        df=pd.read_csv(csv); sbj=int(df.sbj_id.iloc[0]); lab=df.label.fillna("null").astype(str).values
        vid=np.load(vp,mmap_mode="r"); arrs=[np.nan_to_num(df[c].values.astype(np.float32)) for c in LIMBS]
        for k in range(0,len(df)-50,stride):
            seg=lab[k:k+50]; v,c=np.unique(seg,return_counts=True)
            if c.max()<40: continue
            vs=int(k*0.6)+7
            if vs+15>vid.shape[0]: continue
            vm=np.asarray(vid[vs:vs+15]).mean(0).astype(np.float32)
            lbl=LABEL_MAP[v[c.argmax()]]
            for a in arrs:
                A.append(a[k:k+50]); V.append(vm); Y.append(lbl); G.append(sbj)
    return np.array(A,np.float32), np.array(V,np.float32), np.array(Y), np.array(G)


def chans(A):  # (N,50,3) -> (N,7,50): xyz + magnitude + jerk(3)
    mag=np.sqrt((A**2).sum(2,keepdims=True))
    jerk=np.concatenate([np.zeros((len(A),1,3),np.float32),np.diff(A,axis=1)],1)
    return np.concatenate([A,mag,jerk],2).transpose(0,2,1)


class Fusion(nn.Module):
    def __init__(s, cin=7, vdim=768):
        super().__init__()
        s.cnn=nn.Sequential(nn.Conv1d(cin,64,7,padding=3),nn.BatchNorm1d(64),nn.ReLU(),nn.MaxPool1d(2),
            nn.Conv1d(64,128,5,padding=2),nn.BatchNorm1d(128),nn.ReLU(),nn.MaxPool1d(2),
            nn.Conv1d(128,256,3,padding=1),nn.BatchNorm1d(256),nn.ReLU(),nn.AdaptiveAvgPool1d(1),nn.Flatten())
        s.vid=nn.Sequential(nn.Linear(vdim,256),nn.BatchNorm1d(256),nn.ReLU(),nn.Dropout(0.4),nn.Linear(256,128),nn.ReLU())
        s.head=nn.Sequential(nn.Dropout(0.4),nn.Linear(256+128,19))
    def forward(s,a,v): return s.head(torch.cat([s.cnn(a),s.vid(v)],1))


def train(Atr,Vtr,ytr,muA,sdA,muV,sdV,epochs=80):
    a=torch.tensor(np.nan_to_num((chans(Atr)-muA)/sdA),device=DEV); v=torch.tensor((Vtr-muV)/sdV,device=DEV); yt=torch.tensor(ytr,device=DEV)
    m=Fusion().to(DEV); opt=torch.optim.AdamW(m.parameters(),1e-3,weight_decay=1e-4)
    sch=torch.optim.lr_scheduler.CosineAnnealingLR(opt,epochs); lf=nn.CrossEntropyLoss(label_smoothing=0.05); t=time.time()
    for ep in range(epochs):
        m.train(); p=torch.randperm(len(a),device=DEV)
        for i in range(0,len(a),512):
            b=p[i:i+512]; opt.zero_grad(); lf(m(a[b],v[b]),yt[b]).backward(); opt.step()
        sch.step()
    print(f"  trained {epochs}ep {time.time()-t:.0f}s",flush=True); return m


def predict(m,A,V,muA,sdA,muV,sdV):
    a=torch.tensor(np.nan_to_num((chans(A)-muA)/sdA),device=DEV); v=torch.tensor((V-muV)/sdV,device=DEV); m.eval(); out=[]
    with torch.no_grad():
        for i in range(0,len(a),8192): out.append(m(a[i:i+8192],v[i:i+8192]).argmax(1).cpu().numpy())
    return np.concatenate(out)


print("building multimodal overlap dataset...",flush=True)
A,V,y,g=build()
print(f"windows={len(y)} acc={A.shape} vid={V.shape}",flush=True)
HO={16,17,18,19}; te=np.isin(g,list(HO)); tr=~te
Ac=chans(A[tr]); muA=Ac.reshape(-1,7,1).mean((0,2)).reshape(1,7,1); sdA=Ac.reshape(-1,7,1).std((0,2)).reshape(1,7,1)+1e-6
muV=V[tr].mean(0); sdV=V[tr].std(0)+1e-6
m=train(A[tr],V[tr],y[tr],muA,sdA,muV,sdV)
p=predict(m,A[te],V[te],muA,sdA,muV,sdV)
print(f"=== FUSION HELD-OUT macro-F1 (subj16-19) = {f1_score(y[te],p,average='macro'):.4f}  (inertial-CNN 0.539) ===",flush=True)

# full-data -> submission
muA=chans(A).reshape(-1,7,1).mean((0,2)).reshape(1,7,1); sdA=chans(A).reshape(-1,7,1).std((0,2)).reshape(1,7,1)+1e-6
muV=V.mean(0); sdV=V.std(0)+1e-6
mf=train(A,V,y,muA,sdA,muV,sdV)
ti=np.load("test/test_inertial_data.npy",allow_pickle=True).astype(np.float32)
tvr=np.asarray(np.load("test/test_videomae_data.npy",allow_pickle=True))
fa=1 if tvr.shape[1]==15 else 2; tv=tvr.mean(axis=fa).astype(np.float32)
pred=predict(mf,ti,tv,muA,sdA,muV,sdV)
ss=pd.read_csv("sample_submission.csv"); ss["target_feature"]=pred.astype(int); ss.to_csv("submission_fusion.csv",index=False)
torch.save(mf.state_dict(),"models_fusion.pt")
print("wrote submission_fusion.csv | dist:",dict(sorted(pd.Series(pred).value_counts().items())),flush=True)
