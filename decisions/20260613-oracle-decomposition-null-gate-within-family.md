---
title: Oracle decomposition — rank-1 ≈ null-gate + within-family, no cross-family loss
date: 2026-06-13
status: accepted
tier: proof of concept
decision-makers: K. S. Ernest (iFire) Lee
---

## Context and Problem Statement

We were stuck ~0.20 macro-F1 below rank-1 (our LB 0.597, rank-1 ~0.79) and kept finding only
+0.02 levers. Earlier "ceiling" claims (Amdahl proof, frozen-video 0.475) were built on weak
estimators and wrongly implied rank-1 needs pixels we don't have. The user pushed back ("clearly
it's possible" — 0.79 exists on the *same* features) and asked to enumerate, exhaustively, *where*
the missing F1 actually lives, then compare against an oracle.

macro-F1 over 19 classes is finite: all lost signal is off-diagonal mass in the 19×19 confusion
matrix. From the LOSO cache (`loso_cache.npz`), the 33 cells with ≥1000 mass cover 74% of all loss.

## Decision Drivers

- Need to know whether the gap is information-walled (pixel-gated) or addressable from our features.
- Distinguish *places* of loss that share a remedy from scattered, unfixable error.
- Avoid illegitimate "time travel" remedies (test re-stitching / label propagation): inductive only.

## Considered Options

- **Threshold reclaim** (lower per-class decision thresholds): Plausible-searched, net ≤ 0 —
  reclaim precision 0.11–0.20, null tax > gains. Dead (see [[WearMissingF1]]).
- **Better frozen-video model** (transformer + adversarial debias): 0.376 inductive, *below* the
  0.475 that needed transductive per-subject norm. Architecture is not the lever.
- **Oracle decomposition**: classify every significant confusion cell, then measure macro-F1 if an
  oracle fixed each *kind* of cell. Quantifies the ceiling of each remedy.

## Decision Outcome

Chosen: **oracle decomposition**, formalized in Lean4+Plausible (`WearSignalPlaces.lean`).

Exhaustive classification (`theorem no_cross_leak` by `decide`; logic Plausible-swept over all
19×19 pairs): every significant leak is one of exactly **two** structures — there are **zero**
cross-family leaks.

| kind | cells | mass |
|---|---|---|
| null-sink (true active → pred null) | 15 | 82,975 (null-boundary, with source) |
| null-source (true null → pred active) | 10 | ↑ |
| within-family (e.g. push-ups ↔ push-ups-complex) | 8 | 14,991 |
| **cross-family** | **0** | **0** |

Oracle macro-F1 (from cache):

| oracle fixes… | macro-F1 | gain |
|---|---|---|
| baseline | 0.525 | — |
| active/null gate (rest vs holding a pose) | 0.633 | +0.108 |
| within-family slips | 0.652 | +0.127 |
| **both (= perfect family)** | **0.764** | **+0.240** |

Solving the two places ≈ **0.764 ≈ rank-1**. The null-gate is rest-vs-pose = the gravity/orientation
signal (active-limb separability AUC 0.9, see [[per-joint-orientation-recovers-static-pose-f1]]);
within-family is subtle temporal discrimination. Both are plausibly **inertial-addressable** — rank-1
is reframed from "needs pixels" to "needs an orientation active/null gate + within-family specialists".

### Consequences

- (+) Concrete, well-defined target: two remedies, each with a measured oracle ceiling.
- (+) No cross-family loss to chase — the model already separates families; effort is focused.
- (+) Reopens a FOSS, no-pixel path toward ~0.76 (vs the earlier pessimistic ~0.62 ceiling).
- (−) Oracles are *upper* bounds; real gate/specialist models won't be perfect. The within-family
  ceiling especially depends on whether fine motion differences are separable from single-limb accel.
- (−) Supersedes the "single-limb ceiling 0.58, rank-1 needs pixels" framing in
  [[WearLevers]] `wear_080_unreachable`, whose premises (logistic-on-6-stats ceilings) were too low.

## Next

1. Orientation-based **active/null gate** (gravity channels already +0.018; add per-joint 6D).
2. **Within-family specialist** heads (per-family fine temporal models), routed by the coarse model.
