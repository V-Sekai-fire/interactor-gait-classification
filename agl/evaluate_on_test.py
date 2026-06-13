"""Evaluate the trained ANNY-phenotype models on the held-out caldata_test_jc set.
Labels are MASKED: the model never sees test phenotype; we predict from x, then compare
to the ground-truth phenotype fitted from the test subjects' anthropometrics.

Reproduces the exact train-time PCA(64) (fit on the 46 train subjects, seed 0) so the saved
predictors receive features in the same space.
"""
import numpy as np, pandas as pd
from sklearn.decomposition import PCA
from autogluon.tabular import TabularPredictor

ROOT = "/chibifire-assets-2026w24/files/gait_classification"
TRAIN = "/home/ernest.lee/Downloads/caldata_train_jc.parquet"
TEST = "/home/ernest.lee/Downloads/caldata_test_jc.parquet"
ROWS_PER_SUBJECT = 60
N_PCA = 64
TEST_FRAC_SUBJECTS = 0.25


def subsample(path):
    d = pd.read_parquet(path, columns=["subject", "x"])
    keep = d.groupby("subject", group_keys=False).apply(
        lambda g: g.sample(min(ROWS_PER_SUBJECT, len(g)), random_state=0))
    X = np.stack(keep["x"].values).astype(np.float32)
    return X, keep["subject"].values


def main():
    # --- reproduce train PCA (fit on the 46 train subjects only, identical to training) ---
    Xtr, subtr = subsample(TRAIN)
    subs = np.array(sorted(set(subtr))); rng = np.random.default_rng(0); rng.shuffle(subs)
    n_test = max(8, int(len(subs) * TEST_FRAC_SUBJECTS))
    held = set(subs[:n_test])
    is_held = np.array([s in held for s in subtr])
    pca = PCA(n_components=N_PCA, random_state=0).fit(Xtr[~is_held])

    # --- held-out caldata_test set (labels MASKED) ---
    Xte, subte = subsample(TEST)
    Zte = pca.transform(Xte)
    feat = pd.DataFrame(Zte, columns=[f"pc{i}" for i in range(N_PCA)])
    feat["subject"] = subte

    gt = pd.read_parquet(f"{ROOT}/test_subject_phenotypes.parquet").set_index("subject")

    print(f"TEST: {len(Xte)} rows, {len(set(subte))} subjects (labels masked)\n")
    rep = {}
    for tgt, ptype in [("pheno_gender", "binary"), ("pheno_height", "reg"),
                       ("pheno_weight", "reg"), ("pheno_muscle", "reg")]:
        pred = TabularPredictor.load(f"{ROOT}/agl/models_{tgt}")
        row_pred = pred.predict(feat.drop(columns=["subject"]))
        df = pd.DataFrame({"subject": subte, "pred": row_pred.values})
        # aggregate to subject level
        if ptype == "binary":
            agg = df.groupby("subject")["pred"].agg(lambda s: int(round(s.mean())))
            truth = gt.loc[agg.index, tgt].round().astype(int)
            err = float((agg.values != truth.values).mean())
            print(f"[{tgt}] subject error rate = {err:.3f}  ({int(err*len(agg))}/{len(agg)} wrong)")
            rep[tgt] = ("error_rate", err)
        else:
            agg = df.groupby("subject")["pred"].mean()
            truth = gt.loc[agg.index, tgt]
            mae = float(np.abs(agg.values - truth.values).mean())
            within = float((np.abs(agg.values - truth.values) <= 0.1).mean())
            ss = ((truth.values - agg.values) ** 2).sum()
            r2 = 1 - ss / (((truth.values - truth.values.mean()) ** 2).sum() + 1e-9)
            print(f"[{tgt}] MAE={mae:.3f}  within±0.1={within:.2f}  R2={r2:.3f}")
            rep[tgt] = ("MAE", mae)

    print("\n=== TEST ERROR SUMMARY (caldata_test_jc, 25 subjects, labels masked) ===")
    for t, (m, v) in rep.items():
        print(f"  {t}: {m}={v:.3f}")


if __name__ == "__main__":
    main()
