"""Cross-reference anonymous gait_features columns (Var1..Var321) against the
named biomech feature distributions derived from AddBiomechanics .b3d trials.

We have two DIFFERENT populations (48 lab samples vs. AddBiomechanics trials), so
we match by DISTRIBUTIONAL similarity of physically-comparable quantities, not by
row identity. A column is labelled ONLY when:
  (a) scales are consistent  -> ratio of medians within [0.5, 2] and ranges overlap
  (b) the best-matching biomech feature is clearly better than the 2nd best
      (separation margin), so the assignment is non-ambiguous.
Otherwise the column keeps its Var### name. Conservative by design.
"""
import numpy as np, pandas as pd

GAIT = pd.read_parquet('gait_features.parquet')
BIO = pd.read_parquet('cache/biomech_features.parquet')

EXCLUDE = {'activity', 'dataset', 'member', 'subject', 'trial', 'n_frames',
           'n_good_grf'}
bio_feats = [c for c in BIO.columns if c not in EXCLUDE]


def robust(v):
    v = np.asarray(v, float); v = v[np.isfinite(v)]
    if len(v) < 5:
        return None
    return dict(med=np.median(v), p5=np.percentile(v, 5), p95=np.percentile(v, 95),
                iqr=np.percentile(v, 75) - np.percentile(v, 25),
                mn=v.min(), mx=v.max())


def overlap(a, b):
    lo = max(a['p5'], b['p5']); hi = min(a['p95'], b['p95'])
    inter = max(0.0, hi - lo)
    span = max(a['p95'] - a['p5'], b['p95'] - b['p5'], 1e-9)
    return inter / span


def score(col, feat):
    """Higher = more similar. 0 if scale-inconsistent."""
    if col is None or feat is None:
        return 0.0
    m1, m2 = col['med'], feat['med']
    denom = max(abs(m1), abs(m2), 1e-6)
    med_ratio = abs(m1 - m2) / denom            # 0 = identical medians
    if med_ratio > 0.5:                          # medians differ by >50% -> reject scale
        return 0.0
    ov = overlap(col, feat)
    return ov * (1.0 - med_ratio)


bio_stats = {f: robust(BIO[f]) for f in bio_feats}
gait_stats = {vc: robust(GAIT[vc]) for vc in GAIT.columns}

# score every (column, feature) pair
pairs = []
for j, vc in enumerate(GAIT.columns):
    cstat = gait_stats[vc]
    scored = sorted(((score(cstat, bio_stats[f]), f) for f in bio_feats), reverse=True)
    best_s, best_f = scored[0]
    margin = best_s - (scored[1][0] if len(scored) > 1 else 0.0)
    pairs.append((best_s, margin, vc, j + 1, best_f, cstat))

# GREEDY ONE-TO-ONE: a biomech feature can label at most ONE column (its best),
# preventing the many-columns->one-feature magnitude-binning degeneracy.
ACCEPT_S, ACCEPT_M = 0.55, 0.20
used = set()
rows = []
for best_s, margin, vc, col, best_f, cstat in sorted(pairs, reverse=True):
    take = best_f not in used and best_s >= ACCEPT_S and margin >= ACCEPT_M
    if take:
        used.add(best_f)
    rows.append(dict(var=vc, col=col,
                     gait_med=round(cstat['med'], 3) if cstat else None,
                     gait_range=f"[{cstat['mn']:.2f},{cstat['mx']:.2f}]" if cstat else None,
                     best_feature=best_f, best_score=round(best_s, 3),
                     margin=round(margin, 3), label=best_f if take else ''))

R = pd.DataFrame(rows).sort_values('col')
assigned = R[R.label != '']
print(f"columns labelled: {len(assigned)} / {len(R)}")
print("\n=== assigned labels (col -> biomech feature) ===")
with pd.option_context('display.max_rows', None, 'display.width', 160):
    print(assigned[['col', 'var', 'gait_med', 'gait_range', 'label',
                    'best_score', 'margin']].to_string(index=False))

# how many distinct biomech features got used
print("\nbiomech features matched (count):")
print(assigned['label'].value_counts().to_string())

R.to_csv('cross_reference_report.csv', index=False)
print("\nfull report -> cross_reference_report.csv")
