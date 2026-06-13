---
title: Raw-temporal 1D-CNN is the WEAR signal lever (hand-crafted features capped ~0.55)
date: 2026-06-13
status: accepted
tier: proof of concept
decision-makers: K. S. Ernest (iFire) Lee
---

## Context and Problem Statement

Hand-crafted-feature models (TabM/GBM/RealMLP) plateaued at LB 0.553; cheap-gate screening showed
feature tweaks (spectral/autocorr/jerk) and normalizations were within ±0.02 noise, augmentation and
VideoMAE fusion HURT (placement already learned; egocentric video is scene/subject-confounded — predicts
subject-id at 0.85). Leaderboard top ~0.79 → large unextracted signal.

## Decision Drivers

- Cheap-gate discipline: prototype on a subsample before any full training.
- Diagnosis: weak classes (stretching/push-ups/lunges) collapse into null from summary stats; the
  discriminative signal is the raw temporal *shape*.

## Considered Options

- More hand-crafted features / tabular models (plateaued).
- AutoGluon on raw-flattened windows (cheap gate: 0.28 — dense nets lack conv inductive bias).
- **1D-CNN on raw 50x3 windows** (torch) [@bock2024wear].

## Decision Outcome

Chosen option: **1D-CNN on raw windows**. Cheap gate confirmed it SCALES with data (0.34→0.43→0.46 at
6k→13k→27k windows) while hand-crafted plateaus. Full-data held-out macro-F1 **0.539** (> TabM 0.51);
**public LB 0.597** (+0.044 over the 0.553 TabM best). The lever is architecture (temporal conv), not features.

### Consequences

- (+) New best 0.597; clear path (top ~0.79) via deeper/ensemble/overlap.
- (-) AutoGluon cannot host it (no conv); needs torch.
