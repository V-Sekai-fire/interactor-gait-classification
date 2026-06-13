---
title: WEAR hexagon — Lean4+Plausible proven core; slangtorch adapter deferred (toolchain)
date: 2026-06-13
status: accepted
tier: stretch
decision-makers: K. S. Ernest (iFire) Lee
---

## Context and Problem Statement

Productionize the validated 1D-CNN as a fabric hexagon: a proven Lean4+Plausible core + a differentiable
Slang GPU kernel (slangtorch) adapter, matching the house pattern (entity_packet, connection-fsm).

## Decision Outcome

- **Lean4 + Plausible core: BUILT & verified** (`wear/hexagon/`). Models the competition LABEL_MAP as a
  total injective Activity↔code encoding; PROVES `encode_lt_19` (codes ∈ 0..18), `decode_encode`
  (round-trip), `encode_injective` (no collisions) — no `sorry`; Plausible property-tests pass over Fin 19.
  Lean 4.31.0-rc2, plausible [@plausible].
- **slangtorch adapter: DEFERRED.** slangtorch 1.3.20 installs, imports, and compiles Slang→CUDA, but the
  torch cpp-extension build fails on a torch-cu130 + CUDA-13 `ulonglong4` vector-type deprecation
  (reproduces on cuda-nvcc 13.0 and 13.3; slangtorch can't pass -Wno-error). Upstream toolchain bug.

### Consequences

- (+) The data-pipeline encoding contract is formally proven (the valuable, novel part).
- (-) The Slang kernel is unbuilt — but it's numerically identical to the validated `torch.nn.Conv1d`
  (0 F1 impact); revisit when torch/CUDA-13 cpp-extension is fixed, or build a standalone slangc kernel
  outside torch cpp-extension.
