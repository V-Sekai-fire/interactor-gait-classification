"""Sensor-placement augmentation -> retrain TabM -> validate on held-out subjects -> submit.
Augments RAW train windows (rotate about limb axis +-45deg, tilt +-15deg, accel noise sigma=0.03g,
amplitude scale +-5%), 1 clean + 2 perturbed, then re-featurizes. Held-out subjects 16-19 and the
Kaggle test are featurized CLEAN. Reports held-out macro-F1 vs the 0.51 no-aug baseline (ablation
guardrail) before writing the submission.
"""
import sys, numpy as np, pandas as pd
from scipy.spatial.transform import Rotation
from autogluon.tabular import TabularPredictor
from build_wear_baseline import win_feats

LABEL_MAP = {'null':0,'jogging':1,'jogging (rotating arms)':2,'jogging (skipping)':3,'jogging (sidesteps)':4,
 'jogging (butt-kicks)':5,'stretching (triceps)':6,'stretching (lunging)':7,'stretching (shoulders)':8,
 'stretching (hamstrings)':9,'stretching (lumbar rotation)':10,'push-ups':11,'push-ups (complex)':12,
 'sit-ups':13,'sit-ups (complex)':14,'burpees':15,'lunges':16,'lunges (complex)':17,'bench-dips':18}

YAW_DEG = float(sys.argv[1]) if len(sys.argv) > 1 else 45.0   # limb/radial axis (z)
TILT_DEG = float(sys.argv[2]) if len(sys.argv) > 2 else 15.0  # off-axis (x,y)
NOISE = 0.03
SCALE = 0.05
N_AUG = 2
HOLDOUT = {16, 17, 18, 19}


def perturb(w, rng):
    yaw = rng.uniform(-YAW_DEG, YAW_DEG)
    tx, ty = rng.uniform(-TILT_DEG, TILT_DEG, 2)
    R = Rotation.from_euler("zxy", [yaw, tx, ty], degrees=True).as_matrix().astype(np.float32)
    w2 = w @ R.T
    w2 = w2 * (1 + rng.uniform(-SCALE, SCALE, 3)).astype(np.float32)
    w2 = w2 + rng.normal(0, NOISE, w2.shape).astype(np.float32)
    return w2


def featurize(W):
    return np.array([win_feats(w) for w in W])


def main():
    d = np.load("wear_raw.npz", allow_pickle=True)
    X, y, g = d["X"], d["y"], d["g"]
    tr = ~np.isin(g, list(HOLDOUT)); ho = ~tr
    print(f"raw: train windows={tr.sum()} holdout={ho.sum()}  yaw=+-{YAW_DEG} tilt=+-{TILT_DEG}", flush=True)

    rng = np.random.default_rng(0)
    feats, labs = [], []
    Xtr, ytr = X[tr], y[tr]
    feats.append(featurize(Xtr)); labs.append(ytr)                 # 1 clean copy
    for a in range(N_AUG):                                          # N_AUG perturbed copies
        feats.append(featurize(np.array([perturb(w, rng) for w in Xtr]))); labs.append(ytr)
        print(f"  augmented copy {a+1}/{N_AUG} done", flush=True)
    F = np.vstack(feats); L = np.concatenate(labs)
    cols = [f"f{i}" for i in range(F.shape[1])]
    train_df = pd.DataFrame(F, columns=cols); train_df["label"] = L
    print(f"augmented train rows={len(train_df)} ({N_AUG}x+1)", flush=True)

    pred = TabularPredictor(label="label", problem_type="multiclass", eval_metric="f1_macro",
                            path="models_aug", verbosity=1)
    pred.fit(train_df, hyperparameters={"TABM": {}}, fit_weighted_ensemble=False, time_limit=1200)

    # held-out eval (CLEAN features)
    from sklearn.metrics import f1_score
    hof = pd.DataFrame(featurize(X[ho]), columns=cols)
    hp = pred.predict(hof)
    f1 = f1_score(y[ho], hp.values, average="macro")
    print(f"\n=== HELD-OUT macro-F1 (subjects 16-19, aug-trained) = {f1:.4f}  (no-aug baseline 0.51) ===")

    # test submission (CLEAN features)
    test = np.load("test/test_inertial_data.npy", allow_pickle=True)
    tf = pd.DataFrame(featurize(np.array([np.asarray(w) for w in test])), columns=cols)
    labels = pred.predict(tf)
    ss = pd.read_csv("sample_submission.csv"); ss["target_feature"] = [LABEL_MAP[l] for l in labels]
    ss.to_csv("submission_tabm_aug.csv", index=False)
    print("wrote submission_tabm_aug.csv")


if __name__ == "__main__":
    main()
