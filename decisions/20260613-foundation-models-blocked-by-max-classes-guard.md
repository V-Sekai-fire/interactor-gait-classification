---
title: Keep AutoGluon's max_classes=10 guard — foundation models out for 19-class WEAR
date: 2026-06-13
status: accepted
tier: proof of concept
decision-makers: K. S. Ernest (iFire) Lee
---

## Context and Problem Statement

We wanted TabPFN-Mix and TabDPT in the WEAR ensemble for diversity. AutoGluon skips both with
`ag.max_classes=10` but WEAR has 19 classes. The guard can be overridden via
`ag_args_fit={'max_classes':25}` and both then train on a 19-class smoke test.

## Decision Drivers

- The 10-class limit reflects these foundation models' design regime.
- Avoid silently pushing models past their validated operating range.

## Considered Options

- Override the guard and run TabPFN-Mix/TabDPT at 19 classes.
- Respect the guard; use only no-cap models (TabM, RealMLP, GBMs, EBM).
- Coarse-grouping/hierarchical two-stage to keep stage-1 <=10 classes.

## Decision Outcome

Chosen option: **respect the guard**. Foundation tabular models stay out of the 19-class WEAR
task. Diversity comes from the no-cap deep/tree models. Hierarchical grouping left as a future
option if foundation-model diversity is wanted.

### Consequences

- (+) Models used within their validated regime; no surprise degradation.
- (-) No foundation-model diversity for WEAR (turned out moot — see
  [20260613-solo-tabm-over-ensemble-for-wear-ood]).
