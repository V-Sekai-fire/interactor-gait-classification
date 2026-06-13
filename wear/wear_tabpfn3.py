"""WEAR with TabPFN v3 (called directly — AutoGluon's registry only wires <=v2.5).
TabPFN is in-context: we give it a stratified context of train-subject windows, then predict
held-out subjects' windows. v3 multiclass checkpoint handles the 19 classes; GPU.
"""
import numpy as np, pandas as pd
from sklearn.metrics import f1_score, accuracy_score
from tabpfn import TabPFNClassifier

df = pd.read_parquet("wear_features.parquet")
feat = [c for c in df.columns if c.startswith("f")]
subs = sorted(df["sbj"].unique())
holdout = set(subs[-4:])
tr = df[~df["sbj"].isin(holdout)]
te = df[df["sbj"].isin(holdout)]
print(f"classes={df['label'].nunique()} | train rows={len(tr)} test rows={len(te)} | holdout {sorted(holdout)}")

# TabPFN context limit -> stratified subsample of train windows
CTX = 10000
g = tr.groupby("label", group_keys=False)
ctx = g.apply(lambda x: x.sample(min(len(x), max(1, CTX // df["label"].nunique())), random_state=0))
print(f"context windows: {len(ctx)} (stratified over {ctx['label'].nunique()} classes)")

clf = TabPFNClassifier(
    model_path="tabpfn-v3-classifier-v3_20260417_multiclass.ckpt",  # v3 multiclass
    device="cuda", ignore_pretraining_limits=True, n_estimators=4, random_state=0)
clf.fit(ctx[feat].values.astype(np.float32), ctx["label"].values)

# predict held-out subjects in batches (GPU memory)
preds = []
Xte = te[feat].values.astype(np.float32)
B = 4000
for i in range(0, len(Xte), B):
    preds.append(clf.predict(Xte[i:i+B]))
    print(f"  predicted {min(i+B,len(Xte))}/{len(Xte)}", flush=True)
pred = np.concatenate(preds)
yte = te["label"].values
print("\n=== WEAR TabPFN-v3 (held-out subjects) ===")
print(f"macro-F1 = {f1_score(yte, pred, average='macro'):.4f}")
print(f"weighted-F1 = {f1_score(yte, pred, average='weighted'):.4f}")
print(f"accuracy = {accuracy_score(yte, pred):.4f}")
