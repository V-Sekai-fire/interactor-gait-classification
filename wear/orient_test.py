"""ANNY in/out, done right. The energy(std) rule-out only tested MOTION. A held static pose has ~0
motion but the accelerometer reads GRAVITY -> the per-axis MEAN encodes limb ORIENTATION (arm up vs
bent vs down). That orientation channel is exactly what ANNY synthesizes (static pose -> gravity
projection, 6D rotation). Test: hard-class-vs-null separability using ORIENTATION features (per-axis
mean = gravity direction) vs MOTION features. If orientation AUC >> motion AUC, the signal EXISTS and
ANNY is the right tool. Also split by limb: arm-exercises on LEG sensors are unclassifiable (legs idle)
-> quantifies the single-limb ceiling.
"""
import numpy as np, pandas as pd, glob
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
LM={'null':0,'jogging':1,'jogging (rotating arms)':2,'jogging (skipping)':3,'jogging (sidesteps)':4,'jogging (butt-kicks)':5,'stretching (triceps)':6,'stretching (lunging)':7,'stretching (shoulders)':8,'stretching (hamstrings)':9,'stretching (lumbar rotation)':10,'push-ups':11,'push-ups (complex)':12,'sit-ups':13,'sit-ups (complex)':14,'burpees':15,'lunges':16,'lunges (complex)':17,'bench-dips':18}
N=['null','jog','jog-rot','jog-skip','jog-side','jog-butt','str-tri','str-lunge','str-shldr','str-ham','str-lumbar','pushup','pushup-cx','situp','situp-cx','burpee','lunge','lunge-cx','bench-dip']
LIMBS=[["right_arm_acc_x","right_arm_acc_y","right_arm_acc_z"],["right_leg_acc_x","right_leg_acc_y","right_leg_acc_z"],["left_leg_acc_x","left_leg_acc_y","left_leg_acc_z"],["left_arm_acc_x","left_arm_acc_y","left_arm_acc_z"]]
HARD=[6,7,8,9,11,12,13,16,17,18]; STRIDE=25
A,Y,Lb=[],[],[]
for csv in sorted(glob.glob("train/inertial_feat/sbj_*.csv")):
    df=pd.read_csv(csv,low_memory=False); lab=df.label.fillna("null").astype(str).values
    arrs=[np.nan_to_num(df[c].values.astype(np.float32)) for c in LIMBS]
    for k in range(0,len(df)-50,STRIDE):
        seg=lab[k:k+50]; v,c=np.unique(seg,return_counts=True)
        if c.max()<40: continue
        lbl=LM[v[c.argmax()]]
        for li,a in enumerate(arrs): A.append(a[k:k+50]); Y.append(lbl); Lb.append(li)
A=np.array(A,np.float32); Y=np.array(Y); Lb=np.array(Lb)
ORI=A.mean(1)                                   # (N,3) per-axis mean = gravity/orientation
MOT=np.concatenate([A.std(1),np.abs(np.diff(A,axis=1)).mean(1),np.sqrt((A**2).sum(2)).std(1,keepdims=True)],1)  # motion-only
rng=np.random.default_rng(0)
def auc(X,c,limb=None):
    yc=Y==c; yn=Y==0
    if limb is not None: yc=yc&(Lb==limb); yn=yn&(Lb==limb)
    ic=np.where(yc)[0]; ino=rng.choice(np.where(yn)[0],min(len(ic)*2,yn.sum()),replace=False)
    if len(ic)<20: return np.nan
    Xb=np.concatenate([X[ic],X[ino]]); yb=np.concatenate([np.ones(len(ic)),np.zeros(len(ino))])
    return roc_auc_score(yb,LogisticRegression(max_iter=300,class_weight='balanced').fit(Xb,yb).decision_function(Xb))
print(f"{'class':12s} {'MOTION':>7s} {'ORIENT':>7s} {'gain':>6s}   per-limb ORIENT AUC [Rarm Rleg Lleg Larm]",flush=True)
for c in HARD:
    am,ao=auc(MOT,c),auc(ORI,c)
    pl=[auc(ORI,c,li) for li in range(4)]
    plate=' '.join(f'{x:.2f}' if not np.isnan(x) else ' -- ' for x in pl)
    flag=' <-- ORIENTATION SIGNAL' if ao-am>0.05 else ''
    print(f"{N[c]:12s} {am:7.3f} {ao:7.3f} {ao-am:+6.3f}   [{plate}]{flag}",flush=True)
print("\nIf ORIENT >> MOTION for static classes -> gravity/posture carries the signal -> ANNY (static pose",flush=True)
print("FK -> gravity projection, 6D rot) CAN generate it. Per-limb spread shows which limbs are idle (unclassifiable).",flush=True)
