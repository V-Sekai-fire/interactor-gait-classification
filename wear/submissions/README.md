# WEAR Challenge submissions (Kaggle 3rd-wear-dataset-challenge-hasca-2026)

Metric: **macro-F1**. Task: classify 1s single-limb accel windows (50×3) into 19 classes,
held-out test = unseen subjects 22–25. `SUBMISSIONS.csv` = full Kaggle history (refresh with
`KAGGLE_API_TOKEN=$(cat ~/.kaggle/access_token) kaggle competitions submissions 3rd-wear-dataset-challenge-hasca-2026 -v`).

| File | Model | Encoding | Public F1 |
|---|---|---|---|
| submission_tabm.csv | TabM (FOSS deep MLP) | alphabetical (WRONG) | 0.0364 |
| submission_tabm_canon.csv | TabM | WEAR-repo canonical null=−1 (WRONG) | 0.0397 |
| **submission_tabm_labelmap.csv** | **TabM** | **starter-kernel LABEL_MAP (null=0)** | **0.5530** ✅ best |
| submission_ensemble.csv | TabM+LightGBM+RealMLP+CatBoost | LABEL_MAP | 0.5108 |

## Key learnings
- **Encoding is everything**: same predictions, 0.04 → 0.55 just by the correct `target_feature` map
  (null=0, jogging=1 … bench-dips=18; in the `hmnshudhmn24` starter kernel, NOT the WEAR-repo default).
- **Diversity hurt here**: the GBM/tree models generalize worse to the cross-subject + single-limb
  shift than TabM alone, so the weighted ensemble (0.511) < solo TabM (0.553). The deep MLP wins on OOD.
- **Foundation models (TabPFN-Mix, TabDPT) excluded**: hard `max_classes=10` guard, WEAR has 19.
- Held-out (subjects 16–19) macro-F1 of the ensemble was 0.51 — consistent with the leaderboard.

## Repro
Models in `../models_wear` (ensemble) and `../models_tabm_submit` (solo TabM). Features `../wear_features.parquet`.
Re-encode/submit via the LABEL_MAP in `../submit_tabm.py` / `../wear_foundation.py`.

## Augmentation ablation (NOT submitted)
- `submission_tabm_aug.csv` — TabM trained on 3× placement-augmented data (rot ±45°, tilt ±15°,
  noise σ=0.03g). **Held-out macro-F1 = 0.4927 < 0.51 no-aug baseline → augmentation HURT.**
  TabM is already placement-robust; rotated copies diluted signal. Not submitted (would be < 0.553).
  Conclusion: placement is not the gap; body-size normalization (canonical ANNY) is the better lever.

## 1D-CNN (raw temporal) — NEW BEST
- `submission_cnn.csv` — torch 1D-CNN on raw 50x3 windows, full data, LABEL_MAP encoding.
  Held-out (subj 16-19) macro-F1 **0.539** > TabM 0.51; **public LB 0.597** (vs TabM 0.553).
  Lever = raw-sequence conv (hand-crafted features capped ~0.55). Leaderboard top ~0.79 → headroom remains.
