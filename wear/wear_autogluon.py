"""WEAR baseline with AutoGluon — single-limb 1s windows, subject-level holdout, macro-F1.
Caches features to wear_features.parquet so it's built once.
"""
import os, glob, numpy as np, pandas as pd
from autogluon.tabular import TabularPredictor
from build_wear_baseline import windows_from_subject, win_feats  # reuse windowing

CACHE = "wear_features.parquet"


def build_features():
    if os.path.exists(CACHE):
        return pd.read_parquet(CACHE)
    rows = []
    for p in sorted(glob.glob("train/inertial_feat/sbj_*.csv")):
        X, y, g = windows_from_subject(p)
        df = pd.DataFrame(X, columns=[f"f{i}" for i in range(X.shape[1])])
        df["label"] = y; df["sbj"] = g
        rows.append(df)
        print(f"  {p.split('/')[-1]}: {len(df)} windows", flush=True)
    out = pd.concat(rows, ignore_index=True)
    out.to_parquet(CACHE, index=False)
    return out


def main():
    df = build_features()
    print(f"TOTAL {len(df)} windows, {df['sbj'].nunique()} subjects, {df['label'].nunique()} classes")
    subs = sorted(df["sbj"].unique())
    holdout = set(subs[-4:])                       # subject-level holdout (4 unseen subjects)
    tr = df[~df["sbj"].isin(holdout)].drop(columns=["sbj"])
    te = df[df["sbj"].isin(holdout)].drop(columns=["sbj"])
    print(f"train subjects={len(subs)-4}  holdout subjects={sorted(holdout)}  "
          f"(train={len(tr)} rows, test={len(te)} rows)")

    pred = TabularPredictor(label="label", problem_type="multiclass",
                            eval_metric="f1_macro", path="models_wear", verbosity=2)
    # FOSS deep-learning + foundation ensemble (all Apache/permissive, open weights, no token):
    #   TabPFN-Mix + TabDPT (open foundation models) + RealMLP + TabM (deep MLPs) + CatBoost/LightGBM.
    # Gated models (RealTabPFN-2.5, v3) excluded per FOSS-only policy.
    pred.fit(tr, time_limit=2400,
             hyperparameters={"TABPFNMIX": {}, "TABDPT": {}, "REALMLP": {}, "TABM": {},
                              "CAT": {}, "GBM": {}},
             fit_weighted_ensemble=True)
    perf = pred.evaluate(te, silent=True)
    print("\n=== WEAR AutoGluon holdout (unseen subjects) ===")
    print("macro-F1 =", round(perf.get("f1_macro", perf.get("f1", float("nan"))), 4))
    print("full:", {k: round(v, 4) for k, v in perf.items()})
    lb = pred.leaderboard(te, silent=True)
    print(lb[["model", "score_test", "score_val"]].head(6).to_string(index=False))


if __name__ == "__main__":
    main()
