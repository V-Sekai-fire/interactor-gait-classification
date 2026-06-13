"""Build multimodal (inertial + VideoMAE) features per window, aligned per the data card:
inertial 50Hz, video 30fps; for inertial window i the video is the middle 15 frames
[i*30+7 : i*30+22] mean-pooled to 768-d (matches test's (N,15,768)). Video is shared across
the 4 limbs at window i. Output wear_mm.parquet: 37 inertial feats + 768 video + label + sbj.
"""
import glob, os, numpy as np, pandas as pd
from build_wear_baseline import win_feats

WIN = 50
LIMBS = {"right_arm": ["right_arm_acc_x","right_arm_acc_y","right_arm_acc_z"],
         "right_leg": ["right_leg_acc_x","right_leg_acc_y","right_leg_acc_z"],
         "left_leg":  ["left_leg_acc_x","left_leg_acc_y","left_leg_acc_z"],
         "left_arm":  ["left_arm_acc_x","left_arm_acc_y","left_arm_acc_z"]}


def main():
    rows = []
    for csv in sorted(glob.glob("train/inertial_feat/sbj_*.csv")):
        stem = os.path.basename(csv).replace(".csv", "")
        vid_path = f"train/videomae_feat/{stem}.npy"
        if not os.path.exists(vid_path):
            print(f"  skip {stem}: no video"); continue
        df = pd.read_csv(csv, low_memory=False); vid = np.load(vid_path, mmap_mode="r")
        sbj = int(df["sbj_id"].iloc[0]); lab = df["label"].fillna("null").astype(str).values
        n = len(df) // WIN
        limb_arrs = {k: df[c].values.astype(np.float32) for k, c in LIMBS.items()}
        for i in range(n):
            s = slice(i*WIN, (i+1)*WIN)
            seg = lab[s]; vals, cnts = np.unique(seg, return_counts=True)
            if cnts.max() < WIN*0.8:
                continue
            label = vals[cnts.argmax()]
            vs = i*30 + 7
            if vs+15 > vid.shape[0]:
                continue
            vfeat = np.asarray(vid[vs:vs+15]).mean(0)               # (768,)
            for cols in limb_arrs.values():
                ifeat = win_feats(cols[s])                          # (37,)
                rows.append(np.concatenate([ifeat, vfeat, [label, sbj]]))
        print(f"  {stem}: {n} windows -> running total {len(rows)}", flush=True)
    arr = np.array(rows, dtype=object)
    nfeat = arr.shape[1] - 2
    cols = [f"i{i}" for i in range(37)] + [f"v{i}" for i in range(nfeat-37)]
    out = pd.DataFrame(arr[:, :nfeat].astype(np.float32), columns=cols)
    out["label"] = arr[:, -2]; out["sbj"] = arr[:, -1].astype(int)
    out.to_parquet("wear_mm.parquet", index=False)
    print(f"wrote wear_mm.parquet: {out.shape} (37 inertial + {nfeat-37} video)")


if __name__ == "__main__":
    main()
