---
title: Run long/GPU jobs as podman quadlet systemd user services
date: 2026-06-13
status: accepted
tier: baseline
decision-makers: K. S. Ernest (iFire) Lee
---

## Context and Problem Statement

Long training/extraction jobs were launched as background bash (`nohup ... &`) and repeatedly
got orphaned or lost their output. Need durable, observable, GPU-capable job execution.

## Decision Drivers

- Survive the interactive session; journald logs; lifecycle/restart control.
- GPU passthrough on the host RTX 4090.
- Reuse the existing pixi envs without rebuilding images.

## Considered Options

- Background bash / nohup.
- tmux/screen.
- **podman quadlet** `.container` units as `systemctl --user` services.

## Decision Outcome

Chosen option: **podman quadlet**. Fedora 44, podman 5.8.2. Installed
`nvidia-container-toolkit`, generated a CDI spec (`nvidia.com/gpu=all`), and units use
`AddDevice=nvidia.com/gpu=all` + `SecurityLabelDisable=true` (SELinux blocked /dev/nvidia*).
Containers mount the project at its real path and exec the pixi env's python directly
(torch cu130 sees the GPU). Units: `wear-train`, `wear-foundation`, `wear-augment`.

### Consequences

- (+) Robust jobs, journald logs (`journalctl --user -u <unit> -f`), GPU works rootless.
- (-) Requires nvidia-container-toolkit + CDI setup; one-time SELinux relabel-disable.
