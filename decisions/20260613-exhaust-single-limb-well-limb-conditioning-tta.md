---
title: Exhaust the single-limb well — limb-conditioning + TTA + ensemble (legit ceiling)
date: 2026-06-13
status: accepted
tier: proof of concept
decision-makers: K. S. Ernest (iFire) Lee
---

## Context and Problem Statement

Confirmed LB: legit single-limb stack 0.634, deep ensemble 0.639 (new best). Rank-1 (~0.79) requires
raw-pixel VideoMAE fine-tuning, which is a HARD CONSTRAINT we cannot satisfy (no raw WEAR video access).
So rank-1 is unreachable; the task is to extract every remaining *legitimate* (inductive, single-limb,
no test re-stitching) point and document the true ceiling of this data.

## Decision Drivers

- All rank-1 paths gated on one of: 4-limb test (no), raw pixels (no), test re-stitching (rejected as
  time-travel). None available.
- Remaining headroom is small (~+0.01–0.02) but should be banked and the ceiling pinned precisely.
- Must stay fully deployable on the single-limb test (uses only given per-window inputs).

## Considered Options

- **Stop at 0.639** — clean, documented; leaves a little on the table.
- **Frozen-video fusion (again)** — rejected, doesn't transfer ([[whole-body-distillation-video-grounded-in-pose]]).
- **Exhaust the well** (chosen) — stack the last legitimate single-limb levers:
  - **Limb-conditioning**: feed `sensor_location` (known for every test window) as an embedding. A leg
    reading "horizontal" (floor exercise) vs an arm reading "horizontal" mean different activities;
    one model conditioned on limb beats one-model-for-all and is more data-efficient than 4 specialists.
  - **Orientation-preserving TTA**: average predictions over magnitude/jitter/time-warp copies of each
    test window — explicitly NOT rotations, which would destroy the gravity-orientation signal that
    drives the 10ch features ([[oracle-decomposition-null-gate-within-family]]).
  - **3-architecture ensemble** (CNN/TCN/BiGRU) on 10ch orientation + equity 6D-aug + sqrt-balance.

## Decision Outcome

Chosen: **exhaust the well** (`wear/exhaust_well.py` → `submission_exhaust.csv`). This pins the legitimate
single-limb ceiling of the WEAR features. Whatever it scores is, by construction + the session's proofs,
the honest frontier of this data without raw pixels.

### Consequences

- (+) Banks the last legitimate points; ceiling pinned with a concrete number.
- (+) Limb-conditioning is principled (the test literally provides `sensor_location`) and deployable.
- (−) Expected gain is small (~+0.01–0.02); does not approach rank-1.
- (−) TTA + 6-model train is more compute for fractional return — justified only as the final
  well-exhausting run, not a repeatable loop.
- Closes the WEAR optimization arc: the gap beyond is the documented pixel/whole-body wall, not effort.

## Outcome

(to fill once `exhaust_well.py` held-out + LB land — vs ensemble held-out 0.5705 / LB 0.639)
