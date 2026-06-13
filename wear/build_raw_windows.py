"""Extract RAW single-limb 1s windows (N,50,3) + label + subject from the WEAR train CSVs,
cached to wear_raw.npz. Needed because sensor-placement augmentation acts on the raw 3-axis
signal (rotate, then re-featurize), not on the precomputed features.
"""
import glob, numpy as np, pandas as pd

WIN = 50
LIMBS = {"right_arm": ["right_arm_acc_x", "right_arm_acc_y", "right_arm_acc_z"],
         "right_leg": ["right_leg_acc_x", "right_leg_acc_y", "right_leg_acc_z"],
         "left_leg":  ["left_leg_acc_x", "left_leg_acc_y", "left_leg_acc_z"],
         "left_arm":  ["left_arm_acc_x", "left_arm_acc_y", "left_arm_acc_z"]}


def main():
    Xs, Ys, Gs = [], [], []
    for p in sorted(glob.glob("train/inertial_feat/sbj_*.csv")):
        df = pd.read_csv(p)
        sbj = int(df["sbj_id"].iloc[0]); lab = df["label"].fillna("null").astype(str).values
        n = len(df) // WIN
        for cols in LIMBS.values():
            arr = df[cols].values.astype(np.float32)
            for k in range(n):
                s = slice(k * WIN, (k + 1) * WIN)
                seg = lab[s]; vals, cnts = np.unique(seg, return_counts=True)
                if cnts.max() < WIN * 0.8:
                    continue
                Xs.append(arr[s]); Ys.append(vals[cnts.argmax()]); Gs.append(sbj)
        print(f"  {p.split('/')[-1]}: total {len(Ys)}", flush=True)
    X = np.stack(Xs); y = np.array(Ys); g = np.array(Gs)
    np.savez_compressed("wear_raw.npz", X=X, y=y, g=g)
    print(f"saved wear_raw.npz: X={X.shape} classes={len(set(y))} subjects={len(set(g))}")


if __name__ == "__main__":
    main()
