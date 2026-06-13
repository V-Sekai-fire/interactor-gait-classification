"""Quick standalone TabM -> WEAR test predictions -> Kaggle submission.csv.
Trains TabM (deep MLP, FOSS) on ALL train-subject windows, predicts the test windows,
maps class strings -> integer target_feature.
NOTE: the competition's exact label->int encoding isn't published; we use sorted-label
order (LabelEncoder). If the leaderboard uses a different order the score is off — but
this validates the full submission pipeline ("for giggles").
"""
import numpy as np, pandas as pd
from autogluon.tabular import TabularPredictor
from build_wear_baseline import win_feats

# --- train features (cached) ---
df = pd.read_parquet("wear_features.parquet")
classes = sorted(df["label"].unique())
enc = {c: i for i, c in enumerate(classes)}
print("classes (sorted) ->", enc)
tr = df.drop(columns=["sbj"])

pred = TabularPredictor(label="label", problem_type="multiclass",
                        eval_metric="f1_macro", path="models_tabm_submit", verbosity=1)
pred.fit(tr, hyperparameters={"TABM": {}}, fit_weighted_ensemble=False, time_limit=600)

# --- test features from the provided 50x3 windows ---
test = np.load("test/test_inertial_data.npy", allow_pickle=True)   # (12234, 50, 3)
Xte = np.array([win_feats(np.asarray(w)) for w in test])
feat = pd.DataFrame(Xte, columns=[f"f{i}" for i in range(Xte.shape[1])])
labels = pred.predict(feat)
ss = pd.read_csv("sample_submission.csv")
ss["target_feature"] = [enc[l] for l in labels]
ss.to_csv("submission_tabm.csv", index=False)
print("wrote submission_tabm.csv", ss.shape, "| pred dist:", ss["target_feature"].value_counts().to_dict())
