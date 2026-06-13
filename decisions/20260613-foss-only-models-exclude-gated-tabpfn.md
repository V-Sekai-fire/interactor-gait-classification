---
title: FOSS-only model policy — exclude license-gated TabPFN 2.5/v3
date: 2026-06-13
status: accepted
tier: baseline
decision-makers: K. S. Ernest (iFire) Lee
---

## Context and Problem Statement

AutoGluon 1.5 exposes strong tabular foundation models. The standout, RealTabPFN-2.5/v3
(Prior Labs), is the top single model on TabArena — but its weights are gated behind a
`TABPFN_TOKEN` and a custom `tabpfn-3-license-v1.0` that is **non-commercial, not OSI open
source**. The project mandates FOSS only.

## Decision Drivers

- FOSS-only (OSI/permissive licenses, open weights, no token gate).
- Still want high-performance deep/foundation tabular models.

## Considered Options

- Use RealTabPFN-2.5/v3 with a Prior Labs token.
- Use only the FOSS models.

## Decision Outcome

Chosen option: **FOSS models only**. Permitted: RealMLP (pytabkit), TabM, LightGBM, XGBoost,
CatBoost, ExtraTrees, EBM, and the Apache-licensed **TabPFN-Mix** / **TabDPT** (open weights,
no token). Excluded: RealTabPFN-2.5 and v3 (gated, non-commercial). TabPFN-v2 classic is FOSS
(Apache, ungated) and allowed but unused.

### Consequences

- (+) Fully redistributable/commercial-safe stack; no external token for weights.
- (-) Forgo the single strongest TabArena model.
- See [20260613-foundation-models-blocked-by-max-classes-guard].
