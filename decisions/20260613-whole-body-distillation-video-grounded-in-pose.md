---
title: Whole-body distillation — ground the video in pose via a 12-tracker teacher
date: 2026-06-13
status: rejected
tier: stretch
decision-makers: K. S. Ernest (iFire) Lee
---

## Context and Problem Statement

The WEAR test slices each window to a SINGLE limb (`test_inertial_data` is (12234,50,3), with
`sensor_location` + `sbj_id` + full-frame video). Single-limb inertial caps ~0.54 held-out: a leg
sensor during push-ups/sit-ups/bench-dips reads "horizontal on floor" for all three — the
discriminating info is in body parts that limb can't see.

But the *training* capture is the whole body: the FULL 12-tracker model scores **0.69 held-out / 0.64
on hard classes** (vs single-limb 0.54/0.39). So the activities are NOT unclassifiable — single-limb
slicing throws the signal away. With the measured +0.072 LOSO→LB transfer, 0.69 → ~0.76 LB, near rank-1
([[oracle-decomposition-null-gate-within-family]], [[WearSignalTracker]]).

The per-window "frame" also carries the **full-frame video** (sees all 12 trackers' worth of body).
The lever: deliver whole-body context to the single-limb test window via that video.

## Decision Drivers

- Whole-body signal exists (0.69) but is unavailable at single-limb test.
- Naive joint imu+video fusion FAILS: 0.40 inductive / 0.49 psn, both below single-limb 0.54 — the
  frozen VideoMAE branch carries scene/subject confound and crowds out the reliable inertial signal.
- Must stay inductive / legitimate (no test re-stitching "time travel"; per-subject-norm is a
  separate, milder transductive question).

## Considered Options

- **Naive joint fusion** (imu + video + limb → head): scene shortcut dominates → 0.40/0.49. Rejected.
- **Late fusion** (combine probs): safe but small (+0.02); does not reach the whole-body ceiling.
- **Raw-video fine-tune of VideoMAE**: the clean route to pose features, but needs raw pixels we lack.
- **Whole-body distillation** (chosen): a 12-tracker TEACHER produces a pose-driven embedding e_wb
  (IMU-derived → scene-free). The STUDENT's video branch is supervised to PREDICT e_wb (MSE), forcing
  the video to encode whole-body POSE rather than scene. Student = single-limb IMU emb + (video→e_wb)
  + limb-id → 19-way. At test the video reconstructs the missing-limb context.

## Decision Outcome

Chosen: **whole-body distillation** (`distill_wholebody.py`). Rationale: scene does not predict the
IMU-derived e_wb, so the distillation target structurally suppresses the confound that broke every
naive fusion. It is the only inductive, no-pixel path that could close single-limb 0.54 → whole-body
0.69 (→ ~0.76 LB). Status `proposed` pending the held-out result vs the 0.54 floor / 0.69 ceiling.

### Consequences

- (+) If it works, a legitimate rank-1 path with the data we have (per-window video + one limb).
- (+) Reusable teacher: the 12-tracker model also bounds what any single-limb method can hope for.
- (−) Bounded by the video's actual pose content; if frozen VideoMAE features are pose-poor, the
  student's video→e_wb regression saturates and the gain is small.
- (−) Adds a teacher-training stage; more moving parts than late fusion.
- Supersedes [[video-fusion-rejected-scene-confound]] only if the distilled student beats single-limb;
  otherwise that rejection stands and the honest ceiling is the ~0.56–0.62 late-fusion stack.

## Outcome (rejected)

Held-out: teacher (12-track) **0.701**; student (single-limb + distilled video) **0.404** — *below*
single-limb 0.54, same regime as naive fusion (0.40 inductive / 0.49 psn). Distillation did NOT rescue
it. Diagnosis: frozen VideoMAE features do not transfer across subjects (subject-predictable at 0.85;
held-out subj 16-19 = unseen scenes, as are test subj 22-25 in different locations). Every jointly-
trained video head loses to IMU-alone on unseen scenes — the same mechanism that regressed the earlier
video submission on the LB (0.573 < 0.597). Not mode-collapse (a conditional flow would fix that) but
non-transfer, which no generative model over the same features repairs.

**Consequence:** the whole-body 0.70 is a training-only artifact (needs all 12 trackers); frozen video
cannot proxy it. Legitimate inductive ceiling stands at single-limb ~0.54 LOSO / 0.597 LB (+ small
orientation/aug/prior gains → ~0.60-0.62 LB). Rank-1 requires raw pixels to fine-tune VideoMAE into
scene-invariant pose features; flow models become useful only *after* that. [[video-fusion-rejected-scene-confound]] stands.
