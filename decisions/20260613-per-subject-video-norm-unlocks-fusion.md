---
title: Per-subject video normalization unlocks cross-subject VideoMAE fusion (the 0.80 path)
date: 2026-06-13
status: accepted
tier: proof of concept
decision-makers: K. S. Ernest (iFire) Lee
---

## Context and Problem Statement

Inertial-only is ceilinged at ~0.59 (3KA published 0.588; us 0.597 [@bock2024wear]); the 0.20 gap to
the leaders (0.79) is VideoMAE. Earlier video fusion was REJECTED (joint 0.35) due to egocentric
scene confound (video predicts subject-id 0.85). This revisits WHY and finds the fix.

## Decision Drivers

- The scene confound is largely a per-subject additive offset (background embedding).
- Cheap-gate before full build; validate cross-subject (held-out 16-19) with a NEURAL classifier
  (ExtraTrees was the artifact that made video look dead).

## Considered Options

- Temporal GRU over the 15x768 sequence — 0.369 (WORSE than mean; VideoMAEv2 already bakes per-frame temporal context).
- Video mean-pool, raw — 0.40 cross-subject.
- **Video mean-pool + per-subject normalization** (subtract each subject's mean video embedding; transductive, legal at test).

## Decision Outcome

Chosen: **per-subject-normalized video**. Cross-subject video 0.40 -> 0.436; and crucially
**late-fusion (inertial CNN + normalized-video MLP) = 0.509 > both modalities** (inertial 0.391,
video 0.436 at subsample scale). Un-normalized fusion had failed (0.35). The normalization removes
the static scene offset, leaving transferable activity-appearance. This is the realizable 0.80 path:
strong-video (normalized) + inertial fusion.

### Full-scale validation (2026-06-13)

Confirmed against the STRONG inertial baseline (not the weak subsample): inertial-CNN 0.545, video(norm) 0.354,
**late-fusion @w_vid=0.3 = 0.5585 (+0.0135 over inertial-alone)**. First model to beat the pure CNN held-out
(0.539). Modest but real; global-weight fusion leaves most of the 0.20 gap open -> diverse fusion strategies next.

### Fusion-strategy sweep (diverse ideas)

Global-weight fusion (+0.013) leaves headroom. Cheap sweep: **per-class fusion weights** (video-heavy
for accel-ambiguous classes) hit a leaky-oracle upper bound 0.551 vs global 0.503 (+0.048 potential);
**stacking meta-LR worse** (0.453, overfits). Realizable next: CV-learned per-class weights. Honest:
none of these is the 0.20 jump — that needs a stronger VIDEO model (frozen-feature MLP caps ~0.44);
the leaders' 0.79 likely fine-tunes/learns a richer video branch.

### Consequences

- (+) Reverses the video rejection for the NORMALIZED case; fusion now beats single modalities.
- (-) Subsample-scale only so far; must validate vs the STRONG full inertial-CNN (0.539). Supersedes
  the un-normalized conclusion in [[20260613-video-fusion-rejected-scene-confound]].
