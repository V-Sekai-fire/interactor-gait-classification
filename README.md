# interactor-gait-classification

Gait and inertial-sensor pipelines: ANNY body phenotypes from gait, activity recognition from one limb's sensors, and traits from motion.

## What it is for

One pipeline turns a public gait dataset's features into ANNY phenotype parameters for each subject. A second classifies activities in the WEAR dataset from a single limb's inertial sensors, with a Lean 4 and Plausible model of which changes could still raise its score. The third, in `agl/` with its own pixi environment, classifies gender from motion, trains a phenotype regressor and evaluates both on the test split. The decision records in `decisions/` say why each stage is shaped as it is.

## Build and run

    pixi install

Each stage is a Python script run in that environment, on linux-64 only. The environment expects ANNY at `../anny_litert/thirdparty/anny`, inside a sibling `anny_litert` checkout, and several scripts read their data from the paths of the host they were written on.

## Licence

The repository states no licence. `citation.bib` cites the gait dataset.
