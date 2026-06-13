---
title: Extract ANNY phenotype for UCI #561 from body-size features, not a learned motion model
date: 2026-06-13
status: accepted
tier: proof of concept
decision-makers: K. S. Ernest (iFire) Lee
---

## Context and Problem Statement

Goal: label UCI #561 [@uci561gait] gait subjects with the ANNY 6-param phenotype
[gender,age,muscle,weight,height] from SOMA-X/ANNY [@bregier2025anny]. A regressor from caldata
motion -> phenotype FAILED on unseen subjects (gender ~baseline 0.63; height/weight/muscle R2<0):
gait MOTION does not encode body ANTHROPOMETRY.

## Decision Drivers

- Phenotype is a body-shape property; it lives in anthropometrics, not gait dynamics.
- UCI #561 columns are anonymous and carry no mass signal.

## Considered Options

- Train caldata-motion -> phenotype regressor and apply to UCI. (Failed; R2<0.)
- **Use UCI's own body-size features** (stature column) and invert the differentiable ANNY model.

## Decision Outcome

Chosen option: **body-size route**. UCI `Var46` (1.45-1.90 m, person-stable, corroborated by a
6-column height family incl. Max-Heel-Height) is the stature signal; invert ANNY (height=z-extent,
mass=volume*980) to recover the **height** phenotype per subject. gender/weight/muscle are NOT
identifiable from UCI (no mass, no per-person sex labels).

### Consequences

- (+) Defensible, direct height phenotype for all 16 UCI subjects.
- (-) Only 1 of 6 phenotype dims recoverable from UCI; ANNY model runs fully local (bundled MPFB2).
