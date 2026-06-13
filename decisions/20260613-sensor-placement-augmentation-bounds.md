---
title: Sensor-placement augmentation bounds for WEAR (limb-axis +-45 deg, tilt +-15 deg)
date: 2026-06-13
status: rejected
tier: stretch
decision-makers: K. S. Ernest (iFire) Lee
---

## Context and Problem Statement

WEAR's ceiling is the domain gap (unseen subjects, single-limb placement), not the model. We
augment raw 50x3 accel windows to teach TabM placement-invariance — but over-aggressive rotation
would wash out the gravity-orientation cue that distinguishes activities.

## Decision Drivers

- Match the real failure mode: strap "clock position" is wide; tilt is narrow.
- Preserve the activity signal (magnitude features are rotation-invariant; gravity dir is informative).

## Considered Options

- Full SO(3) random rotation (washes gravity cue).
- **Asymmetric**: large limb/radial-axis rotation, small off-axis tilt, light noise/scale.

## Decision Outcome

Chosen option: **asymmetric, validated**. Per window: rotation about the limb axis **+-45 deg**,
off-axis tilt **+-15 deg**, Gaussian accel noise **sigma=0.03 g**, amplitude scale **+-5%**,
**1 clean + 2 perturbed** copies. Bounds are a hyperparameter: validated on held-out subjects
16-19 (no-aug baseline 0.51); dial back tilt/noise first if held-out F1 drops. Run under quadlet.

### Outcome (2026-06-13)

Rejected: held-out macro-F1 **0.4927 < 0.51** no-aug baseline at ±45°/±15°. TabM is already placement-robust, so augmented copies diluted signal. Not submitted (< 0.553 best). Placement is not the dominant gap; body-size normalization (canonical ANNY) is the better-motivated lever next.

## Consequences

- (+) Targets the exact test conditions; magnitude features protect the core signal.
- (-) 3x train size; bounds need ablation; synthetic single-limb accel via sinew-mocap
  `b3d_to_motion` is the planned follow-up. (Result pending.)
