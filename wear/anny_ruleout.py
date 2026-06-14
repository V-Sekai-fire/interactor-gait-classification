"""FAST RULE-OUT for the ANNY physics sim. Hard static-pose classes leak to NULL because low-motion
windows look like rest. ANNY would generate body-correct poses, but a HELD pose has ~zero limb accel
regardless of body -> it cannot add discriminative signal where physics produces a flat trace.
Test: per-window signal energy (std of accel magnitude). If hard-class windows heavily overlap NULL's
energy band, those windows are physically indistinguishable from rest -> ANNY ruled out for them.
Also: a quick hard-vs-null linear separability check (logistic on simple stats) = optimistic upper bound.
"""
import numpy as np, pandas as pd, glob
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
LM={'null':0,'jogging':1,'jogging (rotating arms)':2,'jogging (skipping)':3,'jogging (sidesteps)':4,'jogging (butt-kicks)':5,'stretching (triceps)':6,'stretching (lunging)':7,'stretching (shoulders)':8,'stretching (hamstrings)':9,'stretching (lumbar rotation)':10,'push-ups':11,'push-ups (complex)':12,'sit-ups':13,'sit-ups (complex)':14,'burpees':15,'lunges':16,'lunges (complex)':17,'bench-dips':18}
N=['null','jog','jog-rot','jog-skip','jog-side','jog-butt','str-tri','str-lunge','str-shldr','str-ham','str-lumbar','pushup','pushup-cx','situp','situp-cx','burpee','lunge','lunge-cx','bench-dip']
LIMBS=[["right_arm_acc_x","right_arm_acc_y","right_arm_acc_z"],["right_leg_acc_x","right_leg_acc_y","right_leg_acc_z"],["left_leg_acc_x","left_leg_acc_y","left_leg_acc_z"],["left_arm_acc_x","left_arm_acc_y","left_arm_acc_z"]]
HARD=[6,7,8,9,11,12,13,16,17,18]; STRIDE=25

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
# per-window energy = std of accel magnitude over the 50 samples (motion intensity)
mag=np.sqrt((A**2).sum(2)); energy=mag.std(1)
# simple stat features for separability test
def feats(A):
    m=np.sqrt((A**2).sum(2))
    return np.stack([m.mean(1),m.std(1),m.max(1)-m.min(1),np.abs(np.diff(A,axis=1)).mean((1,2)),A.std(1).mean(1),A.std(1).max(1)],1)
F=feats(A)
nullE=energy[Y==0]; p10,p50,p90=np.percentile(nullE,[10,50,90])
print(f"NULL energy band: p10={p10:.3f} p50={p50:.3f} p90={p90:.3f}",flush=True)
print("class           %windows in NULL energy band   hard-vs-null AUC (optimistic separability)",flush=True)
for c in HARD:
    he=energy[Y==c]; inband=np.mean(he<=p90)*100
    # binary hard-c vs null separability on simple stats (subsample null for balance)
    idxn=np.where(Y==0)[0]; idxc=np.where(Y==c)[0]
    rng=np.random.default_rng(0); idxn=rng.choice(idxn,min(len(idxc)*2,len(idxn)),replace=False)
    Xb=np.concatenate([F[idxc],F[idxn]]); yb=np.concatenate([np.ones(len(idxc)),np.zeros(len(idxn))])
    auc=roc_auc_score(yb,LogisticRegression(max_iter=300).fit(Xb,yb).decision_function(Xb))
    print(f"  {N[c]:11s} {inband:5.0f}% look like rest      AUC={auc:.3f}",flush=True)
print("\nINTERPRETATION: high %-in-null-band + low AUC => physically rest-like => ANNY cannot help (signal absent).",flush=True)
print("Low %-in-band + high AUC => motion exists, model just undertrained => richer synth (ANNY) COULD help.",flush=True)
