# interactor-gait-classification

Gait and inertial-sensor pipelines: ANNY body phenotypes fitted from gait features, and activity recognition from one limb's sensors.

## What it is for

One pipeline turns a public gait dataset's features into ANNY phenotype parameters for each subject. The other classifies activities in the WEAR dataset from a single limb's inertial sensors, with a Lean 4 and Plausible model of which changes could still raise its score. The decision records in `decisions/` say why each stage is shaped as it is.

## Build and run

    pixi install

Each stage is a Python script run in that environment, which expects the ANNY checkout its `pixi.toml` names beside this repository.

## Licence

The repository states no licence. `citation.bib` cites the gait dataset.
