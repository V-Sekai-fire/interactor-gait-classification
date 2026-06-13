---
title: Add arXiv / Kaggle / Fetch MCP servers (user scope) for leader + research tracking
date: 2026-06-13
status: accepted
tier: stretch
decision-makers: K. S. Ernest (iFire) Lee
---

## Context and Problem Statement

Tracking WEAR leaderboard leaders and their methods needs programmatic Kaggle access, paper search,
and JS-page fetching beyond the built-in WebFetch.

## Decision Outcome

Added three MCP servers to user-global config (`~/.claude.json`), launched via `uvx` (installed uv
0.11.21 — no npx/node present, which is why the pre-existing playwright MCP fails):
- **fetch** (`mcp-server-fetch`) — page fetch/markdown.
- **arxiv** (`arxiv-mcp-server`, ARXIV_STORAGE_PATH=~/.arxiv-mcp-storage) — paper search/read.
- **kaggle** (`kaggle-mcp`, KAGGLE_API_TOKEN from ~/.kaggle/access_token) — leaderboard/kernels/discussions.
All three health-check ✔ Connected.

### Consequences

- (+) Live tools for tracking leaders + pulling HAR/fusion research.
- (-) Kaggle token baked into user config (already plaintext in ~/.kaggle/access_token). New servers
  are live for new sessions.
