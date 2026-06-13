"""Fit ANNY 6-param phenotype for each subject in the real caldata train set
(/home/ernest.lee/Downloads/caldata_train_jc.parquet), using its per-subject
recorded_sex + height_m + mass_kg. age is unavailable -> neutral 0.5.
Writes subject_phenotypes.parquet (61 rows).
"""
import pandas as pd
from anny_phenotype import fit_phenotype

SRC = "/home/ernest.lee/Downloads/caldata_train_jc.parquet"


def main():
    d = pd.read_parquet(SRC, columns=["subject", "recorded_sex", "height_m", "mass_kg", "study"])
    ps = d.groupby("subject").first().reset_index()
    rows = []
    for _, r in ps.iterrows():
        ph = fit_phenotype(r["recorded_sex"], None, r["height_m"], r["mass_kg"])
        rows.append({"subject": r["subject"], "study": r["study"],
                     "recorded_sex": r["recorded_sex"], "height_m": r["height_m"],
                     "mass_kg": r["mass_kg"],
                     **{f"pheno_{k}": ph[k] for k in
                        ["gender", "age", "muscle", "weight", "height", "proportions"]},
                     "fit_H": round(ph["_fit_height_m"], 3), "fit_M": round(ph["_fit_mass_kg"], 1)})
        print(f"{r['subject']}: {r['recorded_sex']} {r['height_m']:.2f}m {r['mass_kg']:.1f}kg "
              f"-> g={ph['gender']} h={ph['height']:.2f} w={ph['weight']:.2f} m={ph['muscle']:.2f}",
              flush=True)
    out = pd.DataFrame(rows)
    out.to_parquet("subject_phenotypes.parquet", index=False)
    print(f"\nwrote subject_phenotypes.parquet: {len(out)} subjects")
    print("pheno_height range:", round(out.pheno_height.min(), 2), "-", round(out.pheno_height.max(), 2),
          "| pheno_weight:", round(out.pheno_weight.min(), 2), "-", round(out.pheno_weight.max(), 2),
          "| gender counts:", out.pheno_gender.value_counts().to_dict())


if __name__ == "__main__":
    main()
