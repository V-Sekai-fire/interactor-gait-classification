---
title: pixi toolchain with a numpy<2 pin for nimblephysics B3D/FK
date: 2026-06-13
status: accepted
tier: baseline
decision-makers: K. S. Ernest (iFire) Lee
---

## Context and Problem Statement

The gait/biomechanics work reads AddBiomechanics `.b3d` files via `nimblephysics`, which ships
manylinux cp39/cp311 wheels only — there is no wheel for the system Python 3.14 (Fedora 44).
nimblephysics is also built against NumPy 1.x: calling skeleton forward-kinematics
(`readSkel(...).setPositions(...)`) **segfaults** under NumPy 2.x (ABI mismatch), while
`readFrames` happens to survive.

## Decision Drivers

- Reproducible, per-project environments without touching the system Python.
- nimblephysics must both import and run FK (not just read frames).
- Keep the conversion/ML deps (pandas/pyarrow/scipy/torch) co-installable.

## Considered Options

- System Python 3.14 + venv + pip.
- conda/mamba.
- **pixi** project envs, pinning Python + numpy as needed.

## Decision Outcome

Chosen option: **pixi**. Main env pins Python 3.11; a dedicated `addb-extract` env pins
Python 3.9 + **numpy<2 (1.26.4)** specifically for FK. readFrames works in 3.11/numpy2, but any
`setPositions` FK must run in the numpy<2 env or it segfaults. Separate `agl/` pixi env isolates
AutoGluon (needs pandas<2.2, conflicts with the main pandas 3.x).

### Consequences

- (+) FK is stable; envs are reproducible and isolated.
- (-) Multiple pixi envs to keep in sync; FK and the rest of the pipeline live in different envs.
