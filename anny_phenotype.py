"""Map known anthropometrics (sex, age_years, height_m, mass_kg) -> ANNY 6-param phenotype.

The ANNY/SOMA-X full-body model is differentiable, so we set gender+age directly and
gradient-descend the (height, weight, muscle) params to match the measured (height, mass)
of the generated mesh (Anthropometry: height = z-extent, mass = volume*980 kg/m^3).
proportions is left at 0.5 (no anthropometric signal for it).

phenotype order: [gender, age, muscle, weight, height, proportions], all in [0,1].
"""
import torch, anny
from anny.anthropometry import Anthropometry

_M = None
_A = None


def _model():
    global _M, _A
    if _M is None:
        _M = anny.create_fullbody_model()
        _A = Anthropometry(_M)
    return _M, _A


def age_to_param(age_years):
    """MakeHuman-style age axis: 1->0.0, 25->0.5, 90->1.0 (piecewise linear)."""
    if age_years is None or age_years <= 0:
        return 0.5
    if age_years <= 25:
        return max(0.0, (age_years - 1) / (25 - 1) * 0.5)
    return min(1.0, 0.5 + (age_years - 25) / (90 - 25) * 0.5)


def fit_phenotype(sex, age_years, height_m, mass_kg, iters=300, lr=0.05):
    m, a = _model()
    gender = 1.0 if str(sex).lower().startswith("f") else 0.0
    age = age_to_param(age_years)
    # free params (logit-space -> sigmoid keeps them in [0,1])
    raw = torch.zeros(3, requires_grad=True)  # [height, weight, muscle]
    opt = torch.optim.Adam([raw], lr=lr)
    tgt_h = torch.tensor(float(height_m)); tgt_m = torch.tensor(float(mass_kg))
    for _ in range(iters):
        p = torch.sigmoid(raw)
        ph = {"gender": torch.tensor([gender]), "age": torch.tensor([age]),
              "muscle": p[2:3], "weight": p[1:2], "height": p[0:1],
              "proportions": torch.tensor([0.5])}
        v = m(phenotype_kwargs=ph)["vertices"]
        h = a.height(v)[0]; ms = a.mass(v)[0]
        loss = ((h - tgt_h) / 0.1) ** 2 + ((ms - tgt_m) / 5.0) ** 2
        opt.zero_grad(); loss.backward(); opt.step()
    p = torch.sigmoid(raw).detach()
    height_p, weight_p, muscle_p = [float(x) for x in p]
    # report achieved fit
    with torch.no_grad():
        ph = {"gender": torch.tensor([gender]), "age": torch.tensor([age]),
              "muscle": p[2:3], "weight": p[1:2], "height": p[0:1],
              "proportions": torch.tensor([0.5])}
        v = m(phenotype_kwargs=ph)["vertices"]
        ach_h = float(a.height(v)[0]); ach_m = float(a.mass(v)[0])
    return {"gender": gender, "age": age, "muscle": muscle_p, "weight": weight_p,
            "height": height_p, "proportions": 0.5,
            "_fit_height_m": ach_h, "_fit_mass_kg": ach_m}


if __name__ == "__main__":
    import json
    for sex, age, h, mkg in [("male", 28, 1.76, 64.8), ("female", 24, 1.60, 55.0),
                             ("male", 30, 1.85, 90.0)]:
        r = fit_phenotype(sex, age, h, mkg)
        print(f"{sex} {age}y {h}m {mkg}kg -> "
              f"gender={r['gender']} age={r['age']:.2f} height_p={r['height']:.3f} "
              f"weight_p={r['weight']:.3f} muscle_p={r['muscle']:.3f} "
              f"| achieved H={r['_fit_height_m']:.3f}m mass={r['_fit_mass_kg']:.1f}kg")
