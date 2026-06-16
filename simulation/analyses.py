"""Exact and Monte-Carlo analyses for *Political Autoimmunity*.

Every number cited in the paper's modelled sections is a key in the dict this
module returns. The deterministic scores use exact float arithmetic; the
uncertainty propagation draws from Beta distributions under a fixed seed
(SEED below), so the run is reproducible to the last digit.

The data block is a synthetic, illustrative parameterization of three 2024
group-candidate pairings (LGBTQ, Muslim, and Latino support for Trump). The
exposure, dependence, hostility, implementation, magnitude, salience, and
awareness values are stipulated to exhibit the model's geometry; they are not
empirical estimates. Only the vote-share anchors point at reported figures, and
their provenance and quality are recorded per source in the paper.
"""
from __future__ import annotations

import numpy as np

SEED = 20240
N_MC = 40000
KAPPA = 12.0          # Beta concentration: Beta(mean*KAPPA, (1-mean)*KAPPA)
LAMBDA = 0.5          # weight on public foreseeability F vs voter awareness a in K
TAU = 0.02            # tolerance threshold below which net adverse risk is not counted

# ---------------------------------------------------------------------------
# The synthetic dataset. Each cell is one (group, policy domain). Fields:
#   type : which interest a domain primarily engages (rights/material/security/
#          expressive); the interest functions weight domains through this tag.
#   E    : group exposure to the domain
#   D    : institutional dependence in the domain
#   H    : candidate hostility in the domain (from a -2..+2 policy score, here >0)
#   P    : implementation probability
#   M    : policy magnitude (severity if implemented)
#   S    : issue salience to the group
#   F    : public foreseeability of the adverse policy before the vote
#   a    : survey-style voter self-reported awareness
#   B    : protective benefit the candidate offers the group in the domain
#          (from a +2..-2 score; >0 only where the platform helps the group)
# All in [0,1] except as noted. Values are illustrative, not estimates.
# ---------------------------------------------------------------------------
GROUPS = {
    "lgbtq": {
        "vote_share": 0.12,    # exit-poll-summary order of magnitude (low quality)
        "cells": {
            "civil_rights":    dict(type="rights",   E=0.70, D=0.90, H=0.90, P=0.90, M=0.90, S=0.75, F=0.90, a=0.55, B=0.0),
            "trans_health":    dict(type="rights",   E=0.30, D=0.95, H=0.95, P=0.90, M=0.85, S=0.65, F=0.90, a=0.50, B=0.0),
            "hate_enforce":    dict(type="rights",   E=0.65, D=0.80, H=0.70, P=0.60, M=0.70, S=0.60, F=0.80, a=0.50, B=0.0),
        },
    },
    "muslim": {
        "vote_share": 0.21,    # advocacy exit poll (CAIR); not validated-voter quality
        "cells": {
            "entry_travel":    dict(type="security",  E=0.60, D=0.80, H=0.80, P=0.80, M=0.80, S=0.85, F=0.90, a=0.60, B=0.0),
            "gaza_protest":    dict(type="expressive", E=0.50, D=0.70, H=0.50, P=0.70, M=0.70, S=0.95, F=0.60, a=0.70, B=0.0),
            "religious_bias":  dict(type="rights",    E=0.60, D=0.80, H=0.70, P=0.65, M=0.65, S=0.70, F=0.80, a=0.55, B=0.0),
        },
    },
    "latino": {
        "vote_share": 0.46,    # validated-voter order of magnitude (Pew: near-even)
        "cells": {
            "immigration":     dict(type="security",  E=0.55, D=0.75, H=0.85, P=0.90, M=0.80, S=0.65, F=0.85, a=0.55, B=0.0),
            "economy":         dict(type="material",  E=0.45, D=0.55, H=0.30, P=0.70, M=0.50, S=0.80, F=0.75, a=0.60, B=0.5),
            "civil_rights":    dict(type="rights",    E=0.50, D=0.65, H=0.60, P=0.70, M=0.65, S=0.55, F=0.70, a=0.50, B=0.0),
        },
    },
}

# Interest functions. Four weight a domain by its type; two are special
# mechanisms (subjective weights by stated salience S; institutional weights by
# institutional dependence D); together they span the seven definitions of
# interest the paper separates. Type weights need not be normalized here; the
# scorer normalizes the realized weights over each group's domains.
TYPE_WEIGHTS = {
    "material":        {"rights": 0.10, "material": 0.55, "security": 0.15, "expressive": 0.10},
    "rights":          {"rights": 0.55, "material": 0.10, "security": 0.20, "expressive": 0.05},
    "expressive":      {"rights": 0.10, "material": 0.10, "security": 0.10, "expressive": 0.55},
    "coalition_entry": {"rights": 0.05, "material": 0.30, "security": 0.40, "expressive": 0.20},
    "protest":         {"rights": 0.10, "material": 0.05, "security": 0.10, "expressive": 0.65},
}
INTEREST_MODELS = ["material", "rights", "subjective", "expressive",
                   "coalition_entry", "protest", "institutional"]

FACTORS = ["E", "D", "H", "P", "M", "S", "K"]   # the multiplicative chain for priority risk


# ---------------------------------------------------------------------------
def _k(cell: dict) -> float:
    """Composite foreseeability/awareness gate K = lambda*F + (1-lambda)*a."""
    return LAMBDA * cell["F"] + (1.0 - LAMBDA) * cell["a"]


def _domain_weights(group: dict, model: str) -> dict:
    """Realized, normalized interest weights over a group's domains."""
    cells = group["cells"]
    if model == "subjective":
        raw = {k: c["S"] for k, c in cells.items()}
    elif model == "institutional":
        raw = {k: c["D"] for k, c in cells.items()}
    else:
        tw = TYPE_WEIGHTS[model]
        raw = {k: tw[c["type"]] for k, c in cells.items()}
    tot = sum(raw.values())
    return {k: v / tot for k, v in raw.items()}


def _cell_risk(c: dict) -> dict:
    """Gross, foreseeable, and priority risk for one cell, plus the gate K."""
    R = c["E"] * c["D"] * c["H"] * c["P"] * c["M"]
    K = _k(c)
    FR = R * K
    PR = FR * c["S"]
    return {"R": R, "K": K, "FR": FR, "PR": PR}


def _deterministic() -> dict:
    out = {"groups": {}, "params": {"lambda": LAMBDA, "tau": TAU, "kappa": KAPPA}}
    per_supporter_priority = {}
    for gname, group in GROUPS.items():
        V = group["vote_share"]
        cells = group["cells"]
        risk = {k: _cell_risk(c) for k, c in cells.items()}
        gross = sum(r["R"] for r in risk.values())
        fore = sum(r["FR"] for r in risk.values())
        prio = sum(r["PR"] for r in risk.values())
        attrition = prio / gross
        per_supporter_priority[gname] = prio

        # net alignment and autoimmunity under each interest model
        models = {}
        for m in INTEREST_MODELS:
            w = _domain_weights(group, m)
            net = sum(w[k] * (cells[k]["B"] - risk[k]["R"]) for k in cells)
            auto = sum(w[k] * max(0.0, risk[k]["R"] - cells[k]["B"] - TAU) for k in cells)
            models[m] = {
                "net_alignment_per_supporter": net,
                "autoimmunity_per_supporter": auto,
                "autoimmunity_pop_weighted": V * auto,
            }

        out["groups"][gname] = {
            "vote_share": V,
            "gross_risk_per_supporter": gross,
            "foreseeable_risk_per_supporter": fore,
            "priority_risk_per_supporter": prio,
            "gross_risk_pop_weighted": V * gross,
            "priority_risk_pop_weighted": V * prio,
            "awareness_attrition": attrition,
            "protective_benefit_total": sum(c["B"] for c in cells.values()),
            "cells": {k: {**risk[k]} for k in cells},
            "interest_models": models,
        }
    return out, per_supporter_priority


def _rank(score_by_group: dict) -> list:
    """Group names ordered most-misaligned first."""
    return [g for g, _ in sorted(score_by_group.items(), key=lambda kv: -kv[1])]


def _ranking_analysis(det: dict) -> dict:
    """How the most-misaligned ordering moves across the seven interest models."""
    orderings = {}
    most = {}
    for m in INTEREST_MODELS:
        scores = {g: det["groups"][g]["interest_models"][m]["autoimmunity_per_supporter"]
                  for g in GROUPS}
        order = _rank(scores)
        orderings[m] = order
        most[m] = order[0]
    distinct = {tuple(o) for o in orderings.values()}
    # population-weighted version: the politically operative count
    pop_orderings, pop_most = {}, {}
    for m in INTEREST_MODELS:
        scores = {g: det["groups"][g]["interest_models"][m]["autoimmunity_pop_weighted"]
                  for g in GROUPS}
        order = _rank(scores)
        pop_orderings[m] = order
        pop_most[m] = order[0]
    distinct_pop = {tuple(o) for o in pop_orderings.values()}
    # gross-risk ordering (the "voting against interests" naive view) for contrast
    gross_order = _rank({g: det["groups"][g]["gross_risk_per_supporter"] for g in GROUPS})
    prio_order = _rank({g: det["groups"][g]["priority_risk_per_supporter"] for g in GROUPS})
    prio_pop_order = _rank({g: det["groups"][g]["priority_risk_pop_weighted"] for g in GROUPS})
    # how often each group is named most-misaligned across the seven models
    tally = {g: sum(1 for m in INTEREST_MODELS if most[m] == g) for g in GROUPS}
    # net-alignment sign flips: which groups change verdict sign across models
    sign = {}
    for g in GROUPS:
        nets = [det["groups"][g]["interest_models"][m]["net_alignment_per_supporter"]
                for m in INTEREST_MODELS]
        sign[g] = {"min": min(nets), "max": max(nets),
                   "flips_sign": (min(nets) < 0 < max(nets))}
    return {
        "orderings": {m: orderings[m] for m in INTEREST_MODELS},
        "most_misaligned_by_model": most,
        "n_distinct_orderings": len(distinct),
        "pop_orderings": {m: pop_orderings[m] for m in INTEREST_MODELS},
        "most_misaligned_by_model_pop": pop_most,
        "n_distinct_orderings_pop": len(distinct_pop),
        "gross_order": gross_order,
        "priority_order": prio_order,
        "priority_order_pop_weighted": prio_pop_order,
        "counting_frame_inverts": prio_order[0] != prio_pop_order[0],
        "most_misaligned_per_supporter": prio_order[0],
        "most_misaligned_pop_weighted": prio_pop_order[0],
        "most_misaligned_tally": tally,
        "any_group_unanimous": any(t == len(INTEREST_MODELS) for t in tally.values()),
        "net_sign_by_group": sign,
        "n_groups_flip_sign": sum(1 for g in GROUPS if sign[g]["flips_sign"]),
    }


# ---------------------------------------------------------------------------
def _beta_draw(rng, mean: float, n: int) -> np.ndarray:
    mean = min(max(mean, 1e-4), 1 - 1e-4)
    return rng.beta(mean * KAPPA, (1 - mean) * KAPPA, size=n)


def _monte_carlo(det: dict) -> dict:
    rng = np.random.default_rng(SEED)
    # draw every cell factor once, vectorized
    samples = {}      # gname -> per-supporter priority risk array
    model_samples = {}  # gname -> model -> autoimmunity array
    for gname, group in GROUPS.items():
        cells = group["cells"]
        cell_draws = {}
        for k, c in cells.items():
            d = {f: _beta_draw(rng, c[f], N_MC) for f in ["E", "D", "H", "P", "M", "S"]}
            F = _beta_draw(rng, c["F"], N_MC)
            a = _beta_draw(rng, c["a"], N_MC)
            d["K"] = LAMBDA * F + (1 - LAMBDA) * a
            d["R"] = d["E"] * d["D"] * d["H"] * d["P"] * d["M"]
            d["PR"] = d["R"] * d["K"] * d["S"]
            cell_draws[k] = d
        prio = sum(cell_draws[k]["PR"] for k in cells)
        samples[gname] = prio
        mods = {}
        for m in INTEREST_MODELS:
            w = _domain_weights(group, m)
            auto = sum(w[k] * np.maximum(0.0, cell_draws[k]["R"] - cells[k]["B"] - TAU)
                       for k in cells)
            mods[m] = auto
        model_samples[gname] = mods

    def q(arr):
        lo, med, hi = np.quantile(arr, [0.05, 0.50, 0.95])
        return {"p05": float(lo), "p50": float(med), "p95": float(hi)}

    # quantiles of per-supporter priority risk
    prio_q = {g: q(samples[g]) for g in GROUPS}
    # probability each group is the most-misaligned under the rights model
    rights_stack = np.vstack([model_samples[g]["rights"] for g in GROUPS])
    glist = list(GROUPS)
    p_most_rights = {glist[i]: float(np.mean(np.argmax(rights_stack, axis=0) == i))
                     for i in range(len(glist))}
    # probability of the headline priority ordering holding draw by draw
    prio_stack = np.vstack([samples[g] for g in GROUPS])
    order = det["_priority_order"]
    idx = [glist.index(g) for g in order]
    holds = np.ones(N_MC, dtype=bool)
    for a, b in zip(idx, idx[1:]):
        holds &= prio_stack[a] > prio_stack[b]
    p_priority_order = float(np.mean(holds))
    # probability each group is the most-misaligned on priority risk
    p_most_prio = {glist[i]: float(np.mean(np.argmax(prio_stack, axis=0) == i))
                   for i in range(len(glist))}

    return {
        "n_samples": N_MC,
        "seed": SEED,
        "priority_risk_per_supporter": prio_q,
        "p_most_misaligned_rights_model": p_most_rights,
        "p_most_misaligned_priority": p_most_prio,
        "priority_order": list(order),
        "p_priority_order_holds": p_priority_order,
    }


# ---------------------------------------------------------------------------
def _variance_attribution(det: dict) -> dict:
    """Exact log-variance decomposition on each group's dominant risk cell.

    Priority risk of a single cell is a product of seven independent Beta
    factors, so Var(log PR) = sum_f Var(log factor_f) exactly. The share of each
    factor is its term over the total. For a Beta(p) factor the variance of its
    log is computed from the digamma' (trigamma) function of the shape params.
    """
    from scipy.special import polygamma  # trigamma = polygamma(1, .)

    def var_log_beta(mean):
        mean = min(max(mean, 1e-4), 1 - 1e-4)
        al, be = mean * KAPPA, (1 - mean) * KAPPA
        return float(polygamma(1, al) - polygamma(1, al + be))

    out = {}
    for gname, group in GROUPS.items():
        cells = group["cells"]
        # dominant cell = largest gross risk R
        dom = max(cells, key=lambda k: det["groups"][gname]["cells"][k]["R"])
        c = cells[dom]
        terms = {f: var_log_beta(c[f]) for f in ["E", "D", "H", "P", "M", "S"]}
        terms["K"] = var_log_beta(_k(c))      # K treated as one composite gate factor
        tot = sum(terms.values())
        shares = {f: terms[f] / tot for f in terms}
        top = sorted(shares.items(), key=lambda kv: -kv[1])
        out[gname] = {
            "dominant_cell": dom,
            "shares": shares,
            "top_factor": top[0][0],
            "top_two_share": float(top[0][1] + top[1][1]),
        }
    return out


def _tornado(det: dict) -> dict:
    """One-at-a-time swing of each input across its 5-95 Beta interval on the
    rights-model autoimmunity score of the highest-scoring group. Reports the
    fractional swing each input induces, ranked."""
    # pick the group the rights model flags hardest
    g = max(GROUPS, key=lambda x: det["groups"][x]["interest_models"]["rights"]["autoimmunity_per_supporter"])
    group = GROUPS[g]
    cells = group["cells"]
    w = _domain_weights(group, "rights")
    base = det["groups"][g]["interest_models"]["rights"]["autoimmunity_per_supporter"]

    def score(overrides):
        s = 0.0
        for k, c in cells.items():
            cc = {**c, **overrides.get(k, {})}
            R = cc["E"] * cc["D"] * cc["H"] * cc["P"] * cc["M"]
            s += w[k] * max(0.0, R - cc["B"] - TAU)
        return s

    def beta_q(mean, p):
        from scipy.stats import beta as B
        mean = min(max(mean, 1e-4), 1 - 1e-4)
        return float(B.ppf(p, mean * KAPPA, (1 - mean) * KAPPA))

    swings = {}
    for f in ["E", "D", "H", "P", "M"]:
        lo = {k: {f: beta_q(c[f], 0.05)} for k, c in cells.items()}
        hi = {k: {f: beta_q(c[f], 0.95)} for k, c in cells.items()}
        swings[f] = abs(score(hi) - score(lo)) / base
    ranked = sorted(swings.items(), key=lambda kv: -kv[1])
    return {"group": g, "base_score": base,
            "swings": swings, "top_input": ranked[0][0],
            "top_input_swing": ranked[0][1]}


# ---------------------------------------------------------------------------
def run() -> dict:
    det, per_supp = _deterministic()
    det["_priority_order"] = _rank(per_supp)
    ranking = _ranking_analysis(det)
    mc = _monte_carlo(det)
    var = _variance_attribution(det)
    tor = _tornado(det)
    del det["_priority_order"]
    return {
        "deterministic": det,
        "ranking": ranking,
        "monte_carlo": mc,
        "variance_attribution": var,
        "tornado": tor,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2)[:2000])
