# Decision log — gait / biomechanics / WEAR

MADR-style records (house format: `YYYYMMDD-kebab-title.md`, front-matter `title/date/status/tier/
decision-makers`, sections Context / Decision Drivers / Considered Options / Decision Outcome /
Consequences). Citations in `references.bib` (dataset citation also in `../citation.bib`).
Style ref: https://v-sekai-multiplayer-fabric.github.io/manuals/decisions.html

| Date | Tier | Status | Record |
|------|------|--------|--------|
| 2026-06-13 | baseline | accepted | [pixi toolchain + numpy<2 pin for nimblephysics](20260613-pixi-toolchain-numpy-pin-for-nimblephysics.md) |
| 2026-06-13 | baseline | accepted | [FOSS-only models — exclude gated TabPFN 2.5/v3](20260613-foss-only-models-exclude-gated-tabpfn.md) |
| 2026-06-13 | proof of concept | accepted | [Keep max_classes=10 guard — foundation models out for 19-class WEAR](20260613-foundation-models-blocked-by-max-classes-guard.md) |
| 2026-06-13 | baseline | accepted | [Run GPU jobs via podman quadlet](20260613-run-gpu-jobs-via-podman-quadlet.md) |
| 2026-06-13 | proof of concept | accepted | [WEAR target_feature encoding (starter-kernel LABEL_MAP)](20260613-wear-target-feature-label-encoding.md) |
| 2026-06-13 | proof of concept | accepted | [Solo TabM over ensemble for WEAR OOD](20260613-solo-tabm-over-ensemble-for-wear-ood.md) |
| 2026-06-13 | proof of concept | accepted | [Extract UCI phenotype from body-size, not motion](20260613-extract-uci-phenotype-from-body-size-not-motion.md) |
| 2026-06-13 | stretch | proposed | [Sensor-placement augmentation bounds](20260613-sensor-placement-augmentation-bounds.md) |
| 2026-06-13 | proof of concept | accepted | [1D-CNN raw-temporal is the WEAR lever](20260613-1dcnn-raw-temporal-is-the-wear-lever.md) |
| 2026-06-13 | stretch | accepted | [WEAR hexagon: Lean4+Plausible core, slangtorch adapter deferred](20260613-wear-hexagon-lean-core-slangtorch-adapter.md) |
| 2026-06-13 | proof of concept | accepted | [Video fusion rejected (scene confound)](20260613-video-fusion-rejected-scene-confound.md) |
| 2026-06-13 | stretch | accepted | [Add arXiv/Kaggle/Fetch MCP servers](20260613-add-arxiv-kaggle-fetch-mcps.md) |
| 2026-06-13 | proof of concept | accepted | [Oracle decomposition — rank-1 ≈ null-gate + within-family](20260613-oracle-decomposition-null-gate-within-family.md) |
| 2026-06-13 | stretch | rejected | [Whole-body distillation — ground video in pose via 12-tracker teacher](20260613-whole-body-distillation-video-grounded-in-pose.md) |
| 2026-06-13 | proof of concept | accepted | [Exhaust the single-limb well — limb-conditioning + TTA](20260613-exhaust-single-limb-well-limb-conditioning-tta.md) |
