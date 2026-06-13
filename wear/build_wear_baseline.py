"""WEAR challenge baseline — single-limb 1s window activity classification, leave-subjects-out F1.

Train CSVs have 4 limbs x 3 axes @50Hz + label. Test is single-limb 50x3 windows (sensor_location
varies), subjects 22-25 held out. So we reshape train into SINGLE-LIMB 50-sample windows (mirrors
test), extract hand-crafted accel features, and estimate generalization with GroupKFold over subjects.
Macro-F1 (competition metric is F1).
"""
import glob, numpy as np, pandas as pd
from scipy import stats
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GroupKFold
from sklearn.metrics import f1_score

WIN = 50  # 1s @ 50Hz
LIMBS = {"right_arm": ["right_arm_acc_x", "right_arm_acc_y", "right_arm_acc_z"],
         "right_leg": ["right_leg_acc_x", "right_leg_acc_y", "right_leg_acc_z"],
         "left_leg":  ["left_leg_acc_x", "left_leg_acc_y", "left_leg_acc_z"],
         "left_arm":  ["left_arm_acc_x", "left_arm_acc_y", "left_arm_acc_z"]}


def win_feats(w):  # w: (WIN,3)
    f = []
    for a in range(3):
        x = w[:, a]
        f += [x.mean(), x.std(), x.min(), x.max(), np.median(x),
              np.percentile(x, 25), np.percentile(x, 75), np.mean(np.abs(x - x.mean())),
              (x[:-1] * x[1:] < 0).sum(), np.sum(x ** 2)]
    mag = np.sqrt((w ** 2).sum(1))
    f += [mag.mean(), mag.std(), mag.min(), mag.max()]
    f += [np.corrcoef(w[:, i], w[:, j])[0, 1] for i, j in [(0, 1), (0, 2), (1, 2)]]
    return np.nan_to_num(f)


def windows_from_subject(path):
    df = pd.read_csv(path)
    sbj = int(df["sbj_id"].iloc[0]); lab = df["label"].fillna("null").astype(str).values
    X, Y = [], []
    n = len(df) // WIN
    for limb, cols in LIMBS.items():
        arr = df[cols].values
        for k in range(n):
            s = slice(k * WIN, (k + 1) * WIN)
            seg_lab = lab[s]
            # pure-label windows only (majority must cover the window)
            vals, cnts = np.unique(seg_lab, return_counts=True)
            if cnts.max() < WIN * 0.8:
                continue
            X.append(win_feats(arr[s])); Y.append(vals[cnts.argmax()])
    return np.array(X), np.array(Y), np.full(len(Y), sbj)


def main():
    paths = sorted(glob.glob("train/inertial_feat/sbj_*.csv"))
    Xs, Ys, Gs = [], [], []
    for p in paths:
        x, y, g = windows_from_subject(p)
        Xs.append(x); Ys.append(y); Gs.append(g)
        print(f"  {p.split('/')[-1]}: {len(y)} windows", flush=True)
    X = np.vstack(Xs); y = np.concatenate(Ys); g = np.concatenate(Gs)
    print(f"\nTOTAL {len(y)} windows, {X.shape[1]} feats, {len(set(g))} subjects, {len(set(y))} classes")

    gkf = GroupKFold(n_splits=5)
    f1s = []
    for i, (tr, te) in enumerate(gkf.split(X, y, g)):
        clf = RandomForestClassifier(300, n_jobs=-1, random_state=0).fit(X[tr], y[tr])
        pred = clf.predict(X[te])
        f1 = f1_score(y[te], pred, average="macro")
        f1s.append(f1)
        print(f"  fold {i} (test subj {sorted(set(g[te]))}): macro-F1={f1:.3f}")
    print(f"\n=== leave-subjects-out macro-F1 = {np.mean(f1s):.3f} +/- {np.std(f1s):.3f} ===")
    # also weighted-F1 (closer to typical leaderboard)
    np.save("/tmp/wear_X.npy", X); np.save("/tmp/wear_y.npy", y); np.save("/tmp/wear_g.npy", g)


if __name__ == "__main__":
    main()
