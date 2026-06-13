"""Build the phenotype-regression dataset:
  gait features per .b3d trial  (X)  +  subject ANNY 6-param phenotype  (Y, subject-level)

Runs in the gait pixi env (readFrames works; no FK needed for these features).
"""
import sys, glob
import pandas as pd
from extract_gait_features import subject_rows
from anny_phenotype import fit_phenotype

MAX_TRIALS = 12  # compute-bounded per subject


def main():
    paths = sys.argv[1:] or sorted(glob.glob("/run/media/ernest.lee/Bulk/motion_model/*.b3d"))
    rows = []
    for p in paths:
        r = subject_rows(p, max_trials=MAX_TRIALS)
        print(f"{p.split('/')[-1]}: {len(r)} trial-rows", flush=True)
        rows += r
    df = pd.DataFrame(rows)
    if df.empty:
        print("no rows"); return

    # one phenotype per distinct subject (from its anthropometrics)
    pheno = {}
    for subj, g in df.groupby("subject"):
        row = g.iloc[0]
        ph = fit_phenotype(row["sex"], row["age_years"], row["height_m"], row["mass_kg"])
        pheno[subj] = ph
        print(f"  pheno {subj}: sex={row['sex']} {row['age_years']:.0f}y "
              f"{row['height_m']:.2f}m {row['mass_kg']:.1f}kg -> "
              f"g={ph['gender']} h={ph['height']:.2f} w={ph['weight']:.2f} m={ph['muscle']:.2f} "
              f"(fit H={ph['_fit_height_m']:.2f} M={ph['_fit_mass_kg']:.1f})", flush=True)

    for dim in ["gender", "age", "muscle", "weight", "height", "proportions"]:
        df[f"pheno_{dim}"] = df["subject"].map(lambda s: pheno[s][dim])

    df.to_parquet("phenotype_dataset.parquet", index=False)
    print(f"\nwrote phenotype_dataset.parquet: {len(df)} rows, "
          f"{df['subject'].nunique()} subjects")


if __name__ == "__main__":
    main()
