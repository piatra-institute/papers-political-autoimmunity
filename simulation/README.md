# Simulation — Political Autoimmunity

Reproduces every modelled number in the paper.

```bash
cd simulation
uv run run_all.py
```

Writes `output/results.json` and two figures to `output/figures/`. Requires
`uv` (which resolves numpy, scipy, matplotlib from `pyproject.toml`); no other
setup.

## What it computes

The model scores three synthetic 2024 group-candidate pairings (LGBTQ, Muslim,
and Latino support for Trump). The exposure, dependence, hostility,
implementation, magnitude, salience, and awareness values in `analyses.py` are
**stipulated to exhibit the model's geometry, not measured**. Only the
vote-share anchors point at reported figures, and the paper records their
provenance and quality per source. The numbers are facts about a precisely
specified model, offered because that model is the simplest in which the claimed
phenomena appear.

- `analyses.py` — the data block and the four analyses:
  - **deterministic** — per-cell risk `R = E·D·H·P·M`, the foreseeability gate
    `K`, priority risk `R·K·S`, and, under each of seven interest functions, net
    alignment `Σ W(B−R)` and autoimmunity `Σ W·max(0, R−B−τ)`.
  - **ranking** — how the most-misaligned ordering moves across the seven
    interest functions and between the per-supporter and population-weighted
    counting frames; which groups change verdict sign.
  - **monte_carlo** — every input drawn from a Beta calibrated to its point
    value (concentration `κ`), 40000 seeded samples, quantiles and rank
    probabilities propagated through.
  - **variance_attribution** — exact `Var(log PR)` decomposition on each group's
    dominant cell (a product of independent Beta factors), plus a one-at-a-time
    tornado on the rights-model score.
- `figures.py` — two plotters reading only from the results dict.
- `run_all.py` — orchestrator; prints the headline numbers.

Deterministic scores use exact float arithmetic; the Monte-Carlo layer is seeded
(`analyses.SEED = 20240`), so the run reproduces to the last digit.
