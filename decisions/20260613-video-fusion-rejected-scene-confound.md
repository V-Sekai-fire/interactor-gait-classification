---
title: VideoMAE multimodal fusion rejected for WEAR — egocentric scene confound
date: 2026-06-13
status: accepted
tier: proof of concept
decision-makers: K. S. Ernest (iFire) Lee
---

## Context and Problem Statement

WEAR ships VideoMAEv2 features alongside inertial; the leaderboard gap (ours 0.597 vs top 0.79)
suggested video was the missing signal. We tested whether to fuse it.

## Decision Drivers

- Cross-subject generalization (test = unseen subjects 22-25, new locations).
- Honest baseline: compare fusion to the STRONG inertial-CNN (held-out 0.539), not a weak one.

## Considered Options

- Tree fusion (ExtraTrees on mean-pooled video) — gave 0.165 (artifact).
- Late fusion (independent inertial-CNN + video-MLP, prob-avg) — 0.483 vs WEAK inertial 0.408.
- Joint two-branch net (CNN + video MLP) — 0.352 held-out.
- Inertial-only.

## Decision Outcome

Chosen option: **inertial-only; reject video fusion**. Joint fusion 0.352 << inertial-CNN 0.539:
the video branch keys on per-subject SCENE/background (video predicts subject-id at 0.85; within-subject
activity F1 0.59 but cross-subject ~0.35), so it overfits train scenes and poisons the joint model on
unseen subjects. The earlier "fusion +0.075" was an artifact of comparing to an UNDERTRAINED inertial
baseline (0.408); against the strong CNN, video hurts.

### Consequences

- (+) Avoided shipping a 0.35 model; clear that the cross-subject gap is not closed by naive fusion.
- (-) Video's real (within-subject) signal needs domain-adversarial / scene-invariant training to use —
  a research bet, deferred. Confirmed inertial levers (overlap, mag/jerk channels, diverse deep ensemble)
  are the realizable path. See [[20260613-1dcnn-raw-temporal-is-the-wear-lever]].
