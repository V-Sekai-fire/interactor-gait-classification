"""Multimodal (inertial + VideoMAE) TabM: held-out eval (subjects 16-19) + test submission.
Targets the weak, accel-ambiguous classes (stretching/push-ups/lunges) with visual cues.
"""
import numpy as np, pandas as pd
from sklearn.metrics import f1_score, classification_report
from autogluon.tabular import TabularPredictor
from build_wear_baseline import win_feats

LABEL_MAP = {'null':0,'jogging':1,'jogging (rotating arms)':2,'jogging (skipping)':3,'jogging (sidesteps)':4,
 'jogging (butt-kicks)':5,'stretching (triceps)':6,'stretching (lunging)':7,'stretching (shoulders)':8,
 'stretching (hamstrings)':9,'stretching (lumbar rotation)':10,'push-ups':11,'push-ups (complex)':12,
 'sit-ups':13,'sit-ups (complex)':14,'burpees':15,'lunges':16,'lunges (complex)':17,'bench-dips':18}

df = pd.read_parquet("wear_mm.parquet")
feat = [c for c in df.columns if c[0] in "iv" and c not in ("label",)]
HO = {16,17,18,19}; tr = df[~df.sbj.isin(HO)]; te = df[df.sbj.isin(HO)]
print(f"multimodal rows={len(df)} feats={len(feat)} (37 inertial + {len(feat)-37} video)", flush=True)

pred = TabularPredictor(label="label", problem_type="multiclass", eval_metric="f1_macro",
                        path="models_mm", verbosity=1)
pred.fit(tr[feat+["label"]], hyperparameters={"TABM": {}}, fit_weighted_ensemble=False, time_limit=1800)

p = pred.predict(te[feat])
f1 = f1_score(te.label, p, average="macro")
print(f"\n=== MULTIMODAL HELD-OUT macro-F1 (subj 16-19) = {f1:.4f}  (inertial-only baseline 0.51) ===")
rep = classification_report(te.label, p, output_dict=True, zero_division=0)
weak = sorted((v['f1-score'], k) for k,v in rep.items() if k in
              ('stretching (shoulders)','push-ups (complex)','lunges','push-ups','sit-ups'))
print("weak-class F1 now:", {k: round(f,2) for f,k in weak})

# --- test submission ---
ti = np.load("test/test_inertial_data.npy", allow_pickle=True)
tv = np.asarray(np.load("test/test_videomae_data.npy", allow_pickle=True))  # actual: (N,768,15)
Xi = np.array([win_feats(np.asarray(w)) for w in ti])
frame_ax = 1 if tv.shape[1] == 15 else 2                               # 15 frames -> pool that axis
Xv = tv.mean(axis=frame_ax)                                            # (N,768)
assert Xv.shape[1] == 768, f"video feat dim {Xv.shape}"
T = pd.DataFrame(np.hstack([Xi, Xv]), columns=feat)
labels = pred.predict(T)
ss = pd.read_csv("sample_submission.csv"); ss["target_feature"] = [LABEL_MAP[l] for l in labels]
ss.to_csv("submission_mm.csv", index=False)
print("wrote submission_mm.csv | dist:", dict(sorted(ss.target_feature.value_counts().items())))
