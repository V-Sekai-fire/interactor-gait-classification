"""Train AutoGluon to predict ANNY phenotype from caldata gait features.

Data: real caldata train set (61 subjects, x=7200-dim caldata, subject-level anthropometrics).
Labels: subject ANNY phenotype fitted earlier (subject_phenotypes.parquet).
Targets with variance: gender (classification), height/weight/muscle (regression).

Compute-bounded: subsample rows/subject + PCA-reduce the 7200-dim x.
Split is SUBJECT-LEVEL so test subjects are unseen (no within-subject leakage).
"""
import numpy as np, pandas as pd
from sklearn.decomposition import PCA
from autogluon.tabular import TabularPredictor

ROOT = "/chibifire-assets-2026w24/files/gait_classification"
SRC = "/home/ernest.lee/Downloads/caldata_train_jc.parquet"
ROWS_PER_SUBJECT = 60
N_PCA = 64
TEST_FRAC_SUBJECTS = 0.25
TIME_LIMIT = 90  # per target


def load():
    d = pd.read_parquet(SRC, columns=["subject", "x"])
    ph = pd.read_parquet(f"{ROOT}/subject_phenotypes.parquet")
    rng = np.random.default_rng(0)
    # subsample rows per subject
    keep = d.groupby("subject", group_keys=False).apply(
        lambda g: g.sample(min(ROWS_PER_SUBJECT, len(g)), random_state=0))
    X = np.stack(keep["x"].values).astype(np.float32)        # (rows, 7200)
    subj = keep["subject"].values
    return X, subj, ph


def main():
    X, subj, ph = load()
    print(f"rows={len(X)} feat={X.shape[1]} subjects={len(set(subj))}")
    # subject-level split
    subs = np.array(sorted(set(subj)))
    rng = np.random.default_rng(0); rng.shuffle(subs)
    n_test = max(8, int(len(subs) * TEST_FRAC_SUBJECTS))
    test_subs = set(subs[:n_test]);
    is_test = np.array([s in test_subs for s in subj])
    print(f"train subjects={len(subs)-n_test}  test subjects={n_test}")

    # PCA fit on train rows only
    pca = PCA(n_components=N_PCA, random_state=0).fit(X[~is_test])
    Z = pca.transform(X)
    feat = pd.DataFrame(Z, columns=[f"pc{i}" for i in range(N_PCA)])
    feat["subject"] = subj
    lab = ph.set_index("subject")

    results = {}
    for tgt, ptype in [("pheno_gender", "binary"), ("pheno_height", "regression"),
                       ("pheno_weight", "regression"), ("pheno_muscle", "regression")]:
        df = feat.copy()
        df[tgt] = [lab.loc[s, tgt] for s in subj]
        tr = df[~is_test].drop(columns=["subject"])
        te = df[is_test].drop(columns=["subject"])
        if ptype == "binary":
            tr = tr.copy(); te = te.copy()
            tr[tgt] = tr[tgt].astype(int); te[tgt] = te[tgt].astype(int)
        pred = TabularPredictor(label=tgt, problem_type=ptype,
                                path=f"{ROOT}/agl/models_{tgt}", verbosity=0)
        pred.fit(tr, presets="medium_quality", time_limit=TIME_LIMIT)
        perf = pred.evaluate(te, silent=True)
        results[tgt] = perf
        key = "accuracy" if ptype == "binary" else "r2"
        sc = perf.get(key, perf)
        print(f"[{tgt}] {ptype}: {key}={sc if isinstance(sc,float) else sc:.3f}  full={ {k:round(v,3) for k,v in perf.items()} }")

    print("\n=== SUMMARY (test, subject-level split) ===")
    for t, p in results.items():
        k = "accuracy" if "gender" in t else "r2"
        print(f"  {t}: {k}={p[k]:.3f}")


if __name__ == "__main__":
    main()
