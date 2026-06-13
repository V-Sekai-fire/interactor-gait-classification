"""Extract ANNY phenotype for the UCI #561 subjects from their OWN gait data.

UCI columns are anonymous, but distributional profiling located body-size columns whose
values are in human-stature metres and are person-stable / person-discriminative:
  col46 (~1.45-1.90 m)  -> primary STATURE signal  (UCI 'Height'/finger-tip-height group)
  col37, col39 (~1.4 m) -> secondary height-related signals

We invert the differentiable ANNY model to find the `height` phenotype param whose generated
mesh matches each subject's stature (gender/age/weight/muscle held neutral at 0.5 — UCI gait
carries no mass signal, so weight/muscle phenotype is NOT identifiable and left neutral).
Output: per-UCI-person ANNY height phenotype (16 people), aggregated over their 3 samples.
"""
import numpy as np, pandas as pd, torch, anny
from anny.anthropometry import Anthropometry

STATURE_COL = "Var46"   # 1-indexed col46

_m = anny.create_fullbody_model()
_a = Anthropometry(_m)


def _stature_curve(n=21):
    """Precompute monotonic height-param -> stature(m) curve ONCE (neutral other params)."""
    hp = np.linspace(0.0, 1.0, n)
    statures = []
    with torch.no_grad():
        for h in hp:
            ph = {k: torch.tensor([0.5]) for k in _m.phenotype_labels}
            ph["height"] = torch.tensor([float(h)])
            statures.append(float(_a.height(_m(phenotype_kwargs=ph)["vertices"])[0]))
    return np.array(statures), hp


_STAT, _HP = _stature_curve()


def height_param_for_stature(stature_m):
    """Invert the monotonic curve by interpolation (instant, exact enough)."""
    return float(np.interp(stature_m, _STAT, _HP))


def main():
    X = pd.read_parquet("gait_features.parquet")
    y = pd.read_parquet("gait_labels.parquet").iloc[:, 0].values
    stature = X[STATURE_COL].values
    df = pd.DataFrame({"person": y, "stature_m": stature}).dropna()
    # per-person stature (median of 3 samples) -> ANNY height phenotype
    out = []
    for person, g in df.groupby("person"):
        s = float(g["stature_m"].median())
        hp = height_param_for_stature(s)
        out.append({"person": int(person), "stature_m": round(s, 3),
                    "pheno_height": round(hp, 3),
                    "n_samples": len(g),
                    "stature_within_std": round(float(g["stature_m"].std()), 3)})
    R = pd.DataFrame(out).sort_values("person")
    R.to_parquet("uci_phenotype.parquet", index=False)
    R.to_csv("uci_phenotype.csv", index=False)
    print(R.to_string(index=False))
    print(f"\nstature range {df['stature_m'].min():.2f}-{df['stature_m'].max():.2f} m; "
          f"height phenotype range {R['pheno_height'].min():.2f}-{R['pheno_height'].max():.2f}")
    print("wrote uci_phenotype.parquet / .csv")


if __name__ == "__main__":
    main()
