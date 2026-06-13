"""Fast ANNY phenotype ground-truth for a caldata file's subjects.
Precompute, per gender, a (height_param x weight_param) grid -> (stature_m, mass_kg)
ONCE (muscle=age=0.5), then invert each subject by nearest-grid lookup. No per-subject
optimization -> seconds for any number of subjects.
"""
import sys, numpy as np, pandas as pd, torch, anny
from anny.anthropometry import Anthropometry

_m = anny.create_fullbody_model(); _a = Anthropometry(_m)
GRID = np.linspace(0.05, 0.95, 19)


def _build_grid(gender):
    H = np.zeros((len(GRID), len(GRID))); M = np.zeros_like(H)
    with torch.no_grad():
        for i, hp in enumerate(GRID):
            for j, wp in enumerate(GRID):
                ph = {"gender": torch.tensor([gender]), "age": torch.tensor([0.5]),
                      "muscle": torch.tensor([0.5]), "weight": torch.tensor([float(wp)]),
                      "height": torch.tensor([float(hp)]), "proportions": torch.tensor([0.5])}
                v = _m(phenotype_kwargs=ph)["vertices"]
                H[i, j] = float(_a.height(v)[0]); M[i, j] = float(_a.mass(v)[0])
    return H, M


_GRIDS = {0.0: _build_grid(0.0), 1.0: _build_grid(1.0)}


def fit_fast(sex, height_m, mass_kg):
    gender = 1.0 if str(sex).lower().startswith("f") else 0.0
    H, M = _GRIDS[gender]
    cost = ((H - height_m) / 0.05) ** 2 + ((M - mass_kg) / 5.0) ** 2
    i, j = np.unravel_index(np.argmin(cost), cost.shape)
    return {"gender": gender, "age": 0.5, "muscle": 0.5,
            "weight": float(GRID[j]), "height": float(GRID[i]), "proportions": 0.5,
            "_fit_H": float(H[i, j]), "_fit_M": float(M[i, j])}


def main():
    src = sys.argv[1]; out = sys.argv[2]
    d = pd.read_parquet(src, columns=["subject", "recorded_sex", "height_m", "mass_kg"])
    ps = d.groupby("subject").first().reset_index()
    rows = []
    for _, r in ps.iterrows():
        ph = fit_fast(r["recorded_sex"], r["height_m"], r["mass_kg"])
        rows.append({"subject": r["subject"], "recorded_sex": r["recorded_sex"],
                     **{f"pheno_{k}": ph[k] for k in
                        ["gender", "age", "muscle", "weight", "height", "proportions"]}})
    o = pd.DataFrame(rows); o.to_parquet(out, index=False)
    print(f"fitted {len(o)} subjects -> {out}; gender={o.pheno_gender.value_counts().to_dict()} "
          f"height {o.pheno_height.min():.2f}-{o.pheno_height.max():.2f}")


if __name__ == "__main__":
    main()
