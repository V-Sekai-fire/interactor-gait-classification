"""Train AutoGluon TabularPredictor classifiers with a stratified train/test split on:
  (1) GAIT classification  — UCI #561, predict person (16 classes) from 321 anonymous features
  (2) BIOMECHANICS          — AddBiomechanics .b3d trials, predict movement activity (gait/sts/other)
                              from 52 named biomech features

Feature semantics are unknown for (1); AutoGluon doesn't need them. Small data, so we use a
stratified split and a compute-bounded preset.
"""
import sys, numpy as np, pandas as pd
from sklearn.model_selection import train_test_split
from autogluon.tabular import TabularPredictor

ROOT = "/chibifire-assets-2026w24/files/gait_classification"


def run(name, X, y, test_frac, seed=0, time_limit=120):
    df = X.copy(); df["__label__"] = y.values
    tr, te = train_test_split(df, test_size=test_frac, stratify=df["__label__"],
                              random_state=seed)
    print(f"\n{'='*70}\n[{name}] train={len(tr)} test={len(te)} "
          f"features={X.shape[1]} classes={df['__label__'].nunique()}\n{'='*70}")
    pred = TabularPredictor(label="__label__", problem_type="multiclass",
                            path=f"{ROOT}/agl/models_{name}", verbosity=1)
    pred.fit(tr, presets="medium_quality", time_limit=time_limit)
    perf = pred.evaluate(te, silent=True)
    print(f"[{name}] TEST accuracy = {perf['accuracy']:.3f}")
    lb = pred.leaderboard(te, silent=True)
    print(lb[["model", "score_test", "score_val"]].head(8).to_string(index=False))
    return perf["accuracy"]


def gait():
    X = pd.read_parquet(f"{ROOT}/gait_features.parquet")
    y = pd.read_parquet(f"{ROOT}/gait_labels.parquet").iloc[:, 0].astype(str)
    # 16 classes x 3 samples -> 1 test per class (test_frac=1/3 -> 16 test / 32 train)
    return run("gait_person16", X, y, test_frac=1/3)


def biomech():
    df = pd.read_parquet(f"{ROOT}/cache/biomech_features.parquet")
    drop = {"activity", "dataset", "member", "subject", "trial", "trial_name"}
    feats = [c for c in df.columns if c not in drop]
    X = df[feats].select_dtypes("number")
    y = df["activity"].astype(str)
    return run("biomech_activity", X, y, test_frac=0.3)


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "both"
    res = {}
    if which in ("gait", "both"):
        res["gait_person16"] = gait()
    if which in ("biomech", "both"):
        res["biomech_activity"] = biomech()
    print("\n=== SUMMARY (test accuracy) ===")
    for k, v in res.items():
        print(f"  {k}: {v:.3f}")
