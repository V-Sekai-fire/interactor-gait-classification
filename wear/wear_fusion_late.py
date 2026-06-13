"""WEAR LATE-fusion (the cheap-validated 0.80-path recipe):
  - inertial 1D-CNN on overlap(stride25) raw windows + mag/jerk channels (7ch)
  - video MLP on VideoMAE [mean|max|std] pooling, PER-SUBJECT normalized (transductive scene removal)
  - late fusion: w*video_probs + (1-w)*inertial_probs, w tuned on held-out (subj 16-19)
Independent branches (joint training let video's scene shortcut dominate -> 0.35; late fusion avoids it).
Then full-data train -> test submission (per-test-subject video norm via test_meta sbj_id).
"""
import numpy as np, pandas as pd, glob, os, torch, torch.nn as nn, time
from sklearn.metrics import f1_score
LABEL_MAP={'null':0,'jogging':1,'jogging (rotating arms)':2,'jogging (skipping)':3,'jogging (sidesteps)':4,
 'jogging (butt-kicks)':5,'stretching (triceps)':6,'stretching (lunging)':7,'stretching (shoulders)':8,
 'stretching (hamstrings)':9,'stretching (lumbar rotation)':10,'push-ups':11,'push-ups (complex)':12,
 'sit-ups':13,'sit-ups (complex)':14,'burpees':15,'lunges':16,'lunges (complex)':17,'bench-dips':18}
LIMBS=[["right_arm_acc_x","right_arm_acc_y","right_arm_acc_z"],["right_leg_acc_x","right_leg_acc_y","right_leg_acc_z"],
       ["left_leg_acc_x","left_leg_acc_y","left_leg_acc_z"],["left_arm_acc_x","left_arm_acc_y","left_arm_acc_z"]]
DEV="cuda"; STRIDE=25

def build():
    A,V,Y,G=[],[],[],[]
    for csv in sorted(glob.glob("train/inertial_feat/sbj_*.csv")):
        stem=os.path.basename(csv)[:-4]; vp=f"train/videomae_feat/{stem}.npy"
        if not os.path.exists(vp): continue
        df=pd.read_csv(csv, low_memory=False); sbj=int(df.sbj_id.iloc[0]); lab=df.label.fillna("null").astype(str).values
        vid=np.load(vp,mmap_mode="r"); arrs=[np.nan_to_num(df[c].values.astype(np.float32)) for c in LIMBS]
        for k in range(0,len(df)-50,STRIDE):
            seg=lab[k:k+50]; v,c=np.unique(seg,return_counts=True)
            if c.max()<40: continue
            vs=int(k*0.6)+7
            if vs+15>vid.shape[0]: continue
            w=np.asarray(vid[vs:vs+15]); vp3=np.concatenate([w.mean(0),w.max(0),w.std(0)]).astype(np.float32)
            lbl=LABEL_MAP[v[c.argmax()]]
            for a in arrs: A.append(a[k:k+50]); V.append(vp3); Y.append(lbl); G.append(sbj)
    return np.array(A,np.float32),np.array(V,np.float32),np.array(Y),np.array(G)

def chans(A):
    mag=np.sqrt((A**2).sum(2,keepdims=True)); jerk=np.concatenate([np.zeros((len(A),1,3),np.float32),np.diff(A,axis=1)],1)
    return np.concatenate([A,mag,jerk],2).transpose(0,2,1)

def psn(V,G):  # per-subject normalize (subtract each subject's mean)
    Vn=V.copy()
    for s in np.unique(G): m=G==s; Vn[m]-=Vn[m].mean(0)
    return Vn

class CNN(nn.Module):
    def __init__(s): super().__init__(); s.n=nn.Sequential(nn.Conv1d(7,64,7,padding=3),nn.BatchNorm1d(64),nn.ReLU(),nn.MaxPool1d(2),
        nn.Conv1d(64,128,5,padding=2),nn.BatchNorm1d(128),nn.ReLU(),nn.MaxPool1d(2),
        nn.Conv1d(128,256,3,padding=1),nn.BatchNorm1d(256),nn.ReLU(),nn.AdaptiveAvgPool1d(1),nn.Flatten(),nn.Dropout(.4),nn.Linear(256,19))
    def forward(s,x): return s.n(x)
class VMLP(nn.Module):
    def __init__(s,d): super().__init__(); s.n=nn.Sequential(nn.Linear(d,512),nn.BatchNorm1d(512),nn.ReLU(),nn.Dropout(.5),nn.Linear(512,256),nn.ReLU(),nn.Dropout(.5),nn.Linear(256,19))
    def forward(s,x): return s.n(x)

def fit(model,X,ytr,epochs):
    xt=torch.tensor(X,device=DEV); yt=torch.tensor(ytr,device=DEV); opt=torch.optim.AdamW(model.parameters(),1e-3,weight_decay=1e-4)
    sch=torch.optim.lr_scheduler.CosineAnnealingLR(opt,epochs); lf=nn.CrossEntropyLoss(label_smoothing=.05)
    for ep in range(epochs):
        model.train(); p=torch.randperm(len(xt),device=DEV)
        for i in range(0,len(xt),512): b=p[i:i+512]; opt.zero_grad(); lf(model(xt[b]),yt[b]).backward(); opt.step()
        sch.step()
    return model
def prob(model,X):
    model.eval(); out=[]
    with torch.no_grad():
        for i in range(0,len(X),8192): out.append(torch.softmax(model(torch.tensor(X[i:i+8192],device=DEV)),1).cpu().numpy())
    return np.concatenate(out)

print("building...",flush=True); A,V,y,g=build(); print(f"windows={len(y)} acc={A.shape} vid={V.shape}",flush=True)
HO={16,17,18,19}; te=np.isin(g,list(HO)); tr=~te
# inertial
Ac=chans(A); muA=Ac[tr].reshape(-1,7,1).mean((0,2)).reshape(1,7,1); sdA=Ac[tr].reshape(-1,7,1).std((0,2)).reshape(1,7,1)+1e-6
An=np.nan_to_num((Ac-muA)/sdA)
ci=fit(CNN().to(DEV),An[tr],y[tr],80); ip=prob(ci,An[te])
# video (per-subject normalized within each split's subjects)
Vn=psn(V,g); muV=Vn[tr].mean(0); sdV=Vn[tr].std(0)+1e-6; Vz=((Vn-muV)/sdV).astype(np.float32)
vmodel=fit(VMLP(V.shape[1]).to(DEV),Vz[tr],y[tr],60); vp=prob(vmodel,Vz[te])
print(f"  inertial F1={f1_score(y[te],ip.argmax(1),average='macro'):.4f}  video F1={f1_score(y[te],vp.argmax(1),average='macro'):.4f}",flush=True)
best=(0,0)
for w in [0,.2,.3,.35,.4,.5]:
    f=f1_score(y[te],((1-w)*ip+w*vp).argmax(1),average='macro')
    print(f"  fuse w_vid={w}: {f:.4f}",flush=True); best=max(best,(f,w))
print(f"=== LATE-FUSION HELD-OUT best macro-F1={best[0]:.4f} @w_vid={best[1]} (inertial-CNN 0.539) ===",flush=True)
W=best[1]

# full-data -> submission
muA=chans(A).reshape(-1,7,1).mean((0,2)).reshape(1,7,1); sdA=chans(A).reshape(-1,7,1).std((0,2)).reshape(1,7,1)+1e-6; Anf=np.nan_to_num((chans(A)-muA)/sdA)
Vnf=psn(V,g); muV=Vnf.mean(0); sdV=Vnf.std(0)+1e-6; Vzf=((Vnf-muV)/sdV).astype(np.float32)
cif=fit(CNN().to(DEV),Anf,y,80); vmf=fit(VMLP(V.shape[1]).to(DEV),Vzf,y,60)
ti=np.load("test/test_inertial_data.npy",allow_pickle=True).astype(np.float32)
tip=prob(cif,np.nan_to_num((chans(ti)-muA)/sdA))
tvr=np.asarray(np.load("test/test_videomae_data.npy",allow_pickle=True)); fa=1 if tvr.shape[1]==15 else 2
tvp=np.concatenate([tvr.mean(fa),tvr.max(fa),tvr.std(fa)],1).astype(np.float32)
tm=pd.read_csv("test/test_meta_data.csv"); tsub=tm["sbj_id"].values  # per-TEST-subject norm
tvn=tvp.copy()
for s in np.unique(tsub): m=tsub==s; tvn[m]-=tvn[m].mean(0)
tvz=((tvn-muV)/sdV).astype(np.float32); tvpv=prob(vmf,tvz)
pred=((1-W)*tip+W*tvpv).argmax(1)
ss=pd.read_csv("sample_submission.csv"); ss["target_feature"]=pred.astype(int); ss.to_csv("submission_fusion_late.csv",index=False)
print("wrote submission_fusion_late.csv | dist:",dict(sorted(pd.Series(pred).value_counts().items())),flush=True)
