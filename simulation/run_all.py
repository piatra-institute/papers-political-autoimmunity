"""Orchestrator: reproduces every modelled number in the paper.

    cd simulation
    uv run run_all.py

Writes output/results.json and output/figures/. Every numeric value cited in
the modelled sections is a key in the JSON file. The deterministic scores are
exact; the Monte-Carlo layer is seeded (analyses.SEED), so the run is
reproducible to the last digit.
"""
from __future__ import annotations

import json
from pathlib import Path

from analyses import run, GROUPS
from figures import plot_exposure, plot_verdict

OUT = Path(__file__).parent / "output"


def main() -> None:
    (OUT / "figures").mkdir(parents=True, exist_ok=True)
    results = run()
    (OUT / "results.json").write_text(json.dumps(results, indent=2))
    plot_exposure(results, str(OUT / "figures" / "exposure.png"))
    plot_verdict(results, str(OUT / "figures" / "verdict.png"))

    det, rk, mc = results["deterministic"], results["ranking"], results["monte_carlo"]
    tor, var = results["tornado"], results["variance_attribution"]
    print("gross-risk order   :", " > ".join(rk["gross_order"]))
    print("priority-risk order:", " > ".join(rk["priority_order"]))
    print("distinct orderings across 7 interest models:", rk["n_distinct_orderings"])
    print("most-misaligned by model:", rk["most_misaligned_by_model"])
    for g in GROUPS:
        d = det["groups"][g]
        print(f"  {g:7s} attrition {d['awareness_attrition']*100:4.0f}%  "
              f"priority/supporter {d['priority_risk_per_supporter']:.3f}  "
              f"pop-weighted {d['priority_risk_pop_weighted']:.3f}")
    print("P(order holds):", round(mc["p_priority_order_holds"], 3),
          "| P(most-misaligned, rights):", mc["p_most_misaligned_rights_model"])
    print("top uncertainty driver per group:",
          {g: (var[g]["top_factor"], round(var[g]["top_two_share"], 2)) for g in GROUPS})
    print(f"tornado: {tor['group']} rights score most sensitive to "
          f"{tor['top_input']} (swing {tor['top_input_swing']:.2f})")
    print("wrote", OUT / "results.json")


if __name__ == "__main__":
    main()
