---
title: WEAR target_feature encoding from the starter kernel LABEL_MAP (null=0)
date: 2026-06-13
status: accepted
tier: proof of concept
decision-makers: K. S. Ernest (iFire) Lee
---

## Context and Problem Statement

Kaggle WEAR challenge submissions need integer `target_feature`, but train labels are strings and
the competition publishes no class->int map. A held-out string-vs-string F1 of 0.51 collapsed to
0.04 on the leaderboard — a pure encoding mismatch (correct permutation Q != our guessed P).

## Decision Drivers

- The model is good (0.51 held-out); only the label permutation is wrong.
- Need the competition's exact Q, not a plausible default.

## Considered Options

- Alphabetical (sklearn LabelEncoder): null=9 -> 0.0364.
- WEAR-repo canonical `label_dict` (0..17, null=-1) [@bock2024wear]: -> 0.0397.
- **Starter-kernel `LABEL_MAP`** (null=0, jogging=1 ... bench-dips=18).

## Decision Outcome

Chosen option: **starter-kernel LABEL_MAP** (public kernel `hmnshudhmn24`): null=0 then the
canonical WEAR order shifted +1. Same TabM predictions jumped 0.04 -> **0.553** public macro-F1.

### Consequences

- (+) Correct, verified encoding; recorded in project memory and `wear/submissions/README.md`.
- (-) Encoding lives only in a community kernel, not the official data — fragile if it changes.
