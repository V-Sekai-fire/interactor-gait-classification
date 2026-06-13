---
title: Prefer solo TabM over the weighted ensemble for WEAR (OOD generalization)
date: 2026-06-13
status: accepted
tier: proof of concept
decision-makers: K. S. Ernest (iFire) Lee
---

## Context and Problem Statement

WEAR's test is unseen subjects, single-limb — a domain shift from the 4-limb, seen-subject train.
We compared a solo deep MLP against a diverse weighted ensemble.

## Decision Drivers

- Maximize leaderboard macro-F1 on the OOD test.
- AutoGluon weights members on a leaky internal (same-subject) validation split.

## Considered Options

- Solo TabM [@gorishniy2024tabm].
- Weighted ensemble TabM + LightGBM [@ke2017lightgbm] + RealMLP [@holzmuller2024better] + CatBoost [@prokhorenkova2018catboost].

## Decision Outcome

Chosen option: **solo TabM**. Public macro-F1 0.553 vs the ensemble's 0.511. The tree models
overfit subject-specific gait/calibration quirks and snap under the subject+placement shift,
dragging the leaked-weight ensemble below the MLP, which learns a more generalized activity
representation.

### Consequences

- (+) Best score from the simplest model; clear OOD lesson (deep MLP > trees here).
- (-) Ceiling now bounded by the data domain gap -> motivates augmentation
  [20260613-sensor-placement-augmentation-bounds].
