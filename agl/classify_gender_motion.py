"""Does CLEAN body motion carry gender signal?
Subject(person)-level CV gender classification from raw-b3d kinematic gait features,
EXCLUDING body-size features (mass, height, absolute lengths). Contrast with a
body-size-only model on the same subjects.
"""
import re, numpy as np, pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GroupKFold

R = "/chibifire-assets-2026w24/files/gait_classification"
d = pd.read_parquet(f"{R}/clean_kinematics.parquet")
d = d[d["sex"].astype(str).str.lower().str[0].isin(["m", "f"])].copy()
d["y"] = (d["sex"].str.lower().str[0] == "f").astype(int)
d["person"] = d["subject"].map(lambda s: re.sub(r"_split\d+$", "", str(s)))

SIZE = {"mass_kg", "height_m", "stride_length_m"}            # body-size -> excluded from MOTION test
META = {"subject", "trial", "sex", "age_years", "study_member", "activity",
        "n_frames", "n_good_grf", "y", "person"}
motion = [c for c in d.columns if c not in META | SIZE and d[c].dtype != object]
motion = [c for c in motion if not c.endswith("_m")]          # drop absolute-length metres
print(f"rows={len(d)} persons={d['person'].nunique()} sex(rows)={d['y'].value_counts().to_dict()}")
print(f"motion features ({len(motion)}): {motion[:8]}...")

persons = d.groupby("person")["y"].first()
base = max(persons.mean(), 1 - persons.mean())
print(f"persons={len(persons)} ({(persons==1).sum()}F/{(persons==0).sum()}M)  baseline={base:.3f}")


def cv(feats, name):
    X = np.nan_to_num(d[feats].values.astype(float)); y = d["y"].values; g = d["person"].values
    n = min(5, d["person"].nunique())
    pred = np.zeros(len(y))
    for tr, te in GroupKFold(n_splits=n).split(X, y, g):
        clf = RandomForestClassifier(400, random_state=0).fit(X[tr], y[tr])
        pred[te] = clf.predict(X[te])
    df = pd.DataFrame({"person": g, "true": y, "pred": pred})
    a = df.groupby("person").agg(true=("true", "first"), pred=("pred", lambda s: int(round(s.mean()))))
    acc = (a.true == a.pred).mean()
    print(f"  {name}: person-level {n}-fold acc={acc:.3f} ({(a.true==a.pred).sum()}/{len(a)})  err={1-acc:.3f}")


cv(motion, "MOTION only (kinematics)")
cv([c for c in ["mass_kg", "height_m"] if c in d.columns], "body size (mass+height)")
