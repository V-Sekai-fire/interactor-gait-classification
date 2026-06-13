"""WEAR diversity run: the FOSS foundation models only — TabPFN-Mix + TabDPT.
Trains on all train-subject windows, reports internal-val leaderboard + ensemble weights,
predicts the test windows, encodes with the competition LABEL_MAP, writes a submission.
(Cheaper models TabM/GBM/RealMLP already validated separately.)
"""
import numpy as np, pandas as pd
from autogluon.tabular import TabularPredictor
from build_wear_baseline import win_feats

LABEL_MAP = {'null':0,'jogging':1,'jogging (rotating arms)':2,'jogging (skipping)':3,'jogging (sidesteps)':4,
 'jogging (butt-kicks)':5,'stretching (triceps)':6,'stretching (lunging)':7,'stretching (shoulders)':8,
 'stretching (hamstrings)':9,'stretching (lumbar rotation)':10,'push-ups':11,'push-ups (complex)':12,
 'sit-ups':13,'sit-ups (complex)':14,'burpees':15,'lunges':16,'lunges (complex)':17,'bench-dips':18}

df = pd.read_parquet("wear_features.parquet").drop(columns=["sbj"])
print(f"train windows={len(df)} classes={df['label'].nunique()}", flush=True)

pred = TabularPredictor(label="label", problem_type="multiclass", eval_metric="f1_macro",
                        path="models_foundation", verbosity=2)
# foundation models only; generous budget so neither gets squeezed out
pred.fit(df, time_limit=3600,
         hyperparameters={"TABPFNMIX": {}, "TABDPT": {}}, fit_weighted_ensemble=True)

print("\n=== leaderboard (internal val f1_macro) ===")
lb = pred.leaderboard(silent=True)
print(lb[["model", "score_val", "fit_time"]].to_string(index=False))

# predict test windows -> submission
test = np.load("test/test_inertial_data.npy", allow_pickle=True)
Xte = np.array([win_feats(np.asarray(w)) for w in test])
feat = pd.DataFrame(Xte, columns=[f"f{i}" for i in range(Xte.shape[1])])
labels = pred.predict(feat)
ss = pd.read_csv("sample_submission.csv")
ss["target_feature"] = [LABEL_MAP[l] for l in labels]
ss.to_csv("submission_foundation.csv", index=False)
print("\nwrote submission_foundation.csv", ss.shape,
      "| dist:", dict(sorted(ss["target_feature"].value_counts().items())))
