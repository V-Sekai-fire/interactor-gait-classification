"""AMDAHL'S LAW FOR MACRO-F1. macro-F1 = (1/19) * sum_c F1_c, so each class contributes EQUALLY (1/19)
regardless of its sample count. Amdahl analogue: the achievable speedup (here, macro gain) is bounded by
each class's HEADROOM (ceiling_c - current_c) weighted by its fixed 1/19 share. A class already near its
information ceiling yields ~0 gain no matter how hard we push -> it's the 'serial' part that caps us.

We estimate ceiling_c two ways and report where F1 is RECOVERABLE vs WALLED:
  - current_c  : inertial LOSO per-class F1 (from cache)
  - sep_AUC_c  : optimistic one-vs-rest separability on simple stats (how distinguishable at all)
  - null_band  : % of class windows sitting in NULL's energy band (physically rest-like -> unrecoverable)
Gain_c = (1/19) * (ceiling_c - current_c). Rank classes by Gain_c -> where to spend effort. Sum -> macro ceiling.
Also rules out ANNY: classes with high null-band% + low margin are physics-walled (held pose = ~0 accel).
"""
import numpy as np, pandas as pd, glob
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, roc_auc_score
LM={'null':0,'jogging':1,'jogging (rotating arms)':2,'jogging (skipping)':3,'jogging (sidesteps)':4,'jogging (butt-kicks)':5,'stretching (triceps)':6,'stretching (lunging)':7,'stretching (shoulders)':8,'stretching (hamstrings)':9,'stretching (lumbar rotation)':10,'push-ups':11,'push-ups (complex)':12,'sit-ups':13,'sit-ups (complex)':14,'burpees':15,'lunges':16,'lunges (complex)':17,'bench-dips':18}
N=['null','jog','jog-rot','jog-skip','jog-side','jog-butt','str-tri','str-lunge','str-shldr','str-ham','str-lumbar','pushup','pushup-cx','situp','situp-cx','burpee','lunge','lunge-cx','bench-dip']
LIMBS=[["right_arm_acc_x","right_arm_acc_y","right_arm_acc_z"],["right_leg_acc_x","right_leg_acc_y","right_leg_acc_z"],["left_leg_acc_x","left_leg_acc_y","left_leg_acc_z"],["left_arm_acc_x","left_arm_acc_y","left_arm_acc_z"]]
STRIDE=25
A,Y=[],[]
for csv in sorted(glob.glob("train/inertial_feat/sbj_*.csv")):
    df=pd.read_csv(csv,low_memory=False); lab=df.label.fillna("null").astype(str).values
    arrs=[np.nan_to_num(df[c].values.astype(np.float32)) for c in LIMBS]
    for k in range(0,len(df)-50,STRIDE):
        seg=lab[k:k+50]; v,c=np.unique(seg,return_counts=True)
        if c.max()<40: continue
        lbl=LM[v[c.argmax()]]
        for a in arrs: A.append(a[k:k+50]); Y.append(lbl)
A=np.array(A,np.float32); Y=np.array(Y)
mag=np.sqrt((A**2).sum(2)); energy=mag.std(1)
def feats(A):
    m=np.sqrt((A**2).sum(2)); return np.stack([m.mean(1),m.std(1),m.max(1)-m.min(1),np.abs(np.diff(A,axis=1)).mean((1,2)),A.std(1).mean(1),A.std(1).max(1)],1)
F=feats(A)
d=np.load('loso_cache.npz'); cur=f1_score(d['y'],d['iprob'].argmax(1),average=None,labels=range(19))
p90=np.percentile(energy[Y==0],90)
rng=np.random.default_rng(0)
rows=[]
for c in range(19):
    if c==0: rows.append((c,cur[c],1.0,0.0,0.0)); continue
    inband=np.mean(energy[Y==c]<=p90)*100
    idxc=np.where(Y==c)[0]; idxn=rng.choice(np.where(Y!=c)[0],min(len(idxc)*2,(Y!=c).sum()),replace=False)
    Xb=np.concatenate([F[idxc],F[idxn]]); yb=np.concatenate([np.ones(len(idxc)),np.zeros(len(idxn))])
    auc=roc_auc_score(yb,LogisticRegression(max_iter=300,class_weight='balanced').fit(Xb,yb).decision_function(Xb))
    # ceiling proxy: map separability AUC -> achievable F1 (AUC 0.5->~cur, 1.0->~0.9). conservative.
    ceil=min(0.92, max(cur[c], (auc-0.5)*1.8))
    rows.append((c,cur[c],auc,inband,ceil))
print(f"{'class':12s} {'cur':>5s} {'AUC':>5s} {'null%':>6s} {'ceil':>5s} {'gain/19':>8s}  verdict",flush=True)
tot_cur=0; tot_ceil=0
for c,curc,auc,inb,ceil in sorted(rows,key=lambda r:-(r[4]-r[1])):
    gain=(ceil-curc)/19; tot_cur+=curc/19; tot_ceil+=ceil/19
    vd='WALLED (physics/info)' if (inb>60 and auc<0.8) else ('RECOVERABLE' if ceil-curc>0.08 else 'near-ceiling')
    print(f"{N[c]:12s} {curc:5.2f} {auc:5.2f} {inb:5.0f}% {ceil:5.2f} {gain:8.3f}  {vd}",flush=True)
print(f"\ncurrent macro={tot_cur:.3f}  Amdahl macro-ceiling(optimistic separability)={tot_ceil:.3f}",flush=True)
print(f"=> max recoverable by better single-limb modeling = {tot_ceil-tot_cur:+.3f}. Gap to 0.80 beyond that needs NEW signal.",flush=True)
