"""Publication figures for *Political Autoimmunity*. Pure plotters: every value
is read from the results dict produced by analyses.run(). Deterministic."""
from __future__ import annotations

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from analyses import GROUPS, INTEREST_MODELS

INK = "#1a1a1a"
ACCENT = "#b3202c"   # red
COOL = "#2a5b8c"     # blue
MUTE = "#8a8a8a"
PALE = "#cfcfcf"
GOLD = "#c98a1a"

GLABEL = {"lgbtq": "LGBTQ", "muslim": "Muslim", "latino": "Latino"}
MLABEL = {"material": "material", "rights": "rights", "subjective": "subjective",
          "expressive": "expressive", "coalition_entry": "coalition\nentry",
          "protest": "protest", "institutional": "institutional"}
GCOLOR = {"lgbtq": ACCENT, "muslim": COOL, "latino": GOLD}

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.edgecolor": INK,
    "axes.labelcolor": INK,
    "text.color": INK,
    "xtick.color": INK,
    "ytick.color": INK,
    "axes.linewidth": 0.8,
})


# ---------------------------------------------------------------------------
def plot_exposure(results: dict, path: str) -> None:
    """Left: per-cell gross risk heatmap. Right: the awareness gate's attrition
    of gross risk into foreseeable and priority risk, per group."""
    det = results["deterministic"]["groups"]
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(11, 4.2),
                                   gridspec_kw={"width_ratios": [1.25, 1.0]})

    # --- left: heatmap of cell gross risk R --------------------------------
    glist = list(GROUPS)
    maxcols = max(len(GROUPS[g]["cells"]) for g in glist)
    grid = np.full((len(glist), maxcols), np.nan)
    labels = [["" for _ in range(maxcols)] for _ in glist]
    for i, g in enumerate(glist):
        for j, (cname, _) in enumerate(GROUPS[g]["cells"].items()):
            grid[i, j] = det[g]["cells"][cname]["R"]
            labels[i][j] = cname.replace("_", "\n")
    im = axL.imshow(grid, cmap="OrRd", vmin=0, vmax=np.nanmax(grid), aspect="auto")
    axL.set_xticks(range(maxcols))
    axL.set_xticklabels([f"domain {j+1}" for j in range(maxcols)], fontsize=9)
    axL.set_yticks(range(len(glist)))
    axL.set_yticklabels([GLABEL[g] for g in glist])
    for i in range(len(glist)):
        for j in range(maxcols):
            if not np.isnan(grid[i, j]):
                v = grid[i, j]
                axL.text(j, i + 0.18, f"{v:.2f}", ha="center", va="center",
                         fontsize=8.5, color="white" if v > 0.18 else INK)
                axL.text(j, i - 0.22, labels[i][j], ha="center", va="center",
                         fontsize=6.6, color="white" if v > 0.18 else INK)
    axL.set_title("Per-cell gross risk  $R = E\\,D\\,H\\,P\\,M$", fontsize=10)
    fig.colorbar(im, ax=axL, fraction=0.046, pad=0.04)

    # --- right: gross -> foreseeable -> priority, per group ----------------
    x = np.arange(len(glist))
    bw = 0.26
    gross = [det[g]["gross_risk_per_supporter"] for g in glist]
    fore = [det[g]["foreseeable_risk_per_supporter"] for g in glist]
    prio = [det[g]["priority_risk_per_supporter"] for g in glist]
    axR.bar(x - bw, gross, bw, color=PALE, label="gross  $\\Sigma R$")
    axR.bar(x, fore, bw, color=MUTE, label="foreseeable  $\\Sigma RK$")
    axR.bar(x + bw, prio, bw, color=INK, label="priority  $\\Sigma RKS$")
    for i, g in enumerate(glist):
        axR.text(i + bw, prio[i] + 0.01, f"{det[g]['awareness_attrition']*100:.0f}%",
                 ha="center", fontsize=8, color=INK)
    axR.set_xticks(x)
    axR.set_xticklabels([GLABEL[g] for g in glist])
    axR.set_ylabel("risk per supporter")
    axR.set_title("The awareness gate (label: priority / gross)", fontsize=10)
    axR.legend(frameon=False, fontsize=8, loc="upper right")
    axR.spines[["top", "right"]].set_visible(False)

    fig.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
def plot_verdict(results: dict, path: str) -> None:
    """Left: net alignment under each interest model, by group (Latino crosses
    zero). Center: the counting-frame inversion, per-supporter rank vs
    population-weighted rank. Right: log-variance attribution of the dominant
    cell, per group."""
    det = results["deterministic"]["groups"]
    var = results["variance_attribution"]
    glist = list(GROUPS)
    fig, (axL, axC, axR) = plt.subplots(1, 3, figsize=(13.5, 4.3))

    # --- left: net alignment by interest model (sign flips) ----------------
    x = np.arange(len(INTEREST_MODELS))
    for g in glist:
        ys = [det[g]["interest_models"][m]["net_alignment_per_supporter"]
              for m in INTEREST_MODELS]
        axL.plot(x, ys, "o-", color=GCOLOR[g], ms=5, lw=1.8, label=GLABEL[g])
    axL.axhline(0, color=INK, lw=0.9, ls="--")
    axL.text(len(x) - 1, 0.012, "aligned", ha="right", va="bottom", fontsize=7.5, color=MUTE)
    axL.text(len(x) - 1, -0.012, "misaligned", ha="right", va="top", fontsize=7.5, color=MUTE)
    axL.set_xticks(x)
    axL.set_xticklabels([MLABEL[m] for m in INTEREST_MODELS], fontsize=7.5)
    axL.set_ylabel("net alignment per supporter")
    axL.set_title("Verdict by interest function", fontsize=10)
    axL.legend(frameon=False, fontsize=8, loc="lower left")
    axL.spines[["top", "right"]].set_visible(False)

    # --- center: counting-frame inversion (slope/bump chart) ---------------
    ps = {g: det[g]["priority_risk_per_supporter"] for g in glist}
    pw = {g: det[g]["priority_risk_pop_weighted"] for g in glist}
    ps_rank = {g: r + 1 for r, (g, _) in enumerate(sorted(ps.items(), key=lambda kv: -kv[1]))}
    pw_rank = {g: r + 1 for r, (g, _) in enumerate(sorted(pw.items(), key=lambda kv: -kv[1]))}
    for g in glist:
        axC.plot([0, 1], [ps_rank[g], pw_rank[g]], "o-", color=GCOLOR[g], ms=10, lw=2.2)
        axC.text(-0.04, ps_rank[g], GLABEL[g], ha="right", va="center", fontsize=9, color=GCOLOR[g])
        axC.text(1.04, pw_rank[g], GLABEL[g], ha="left", va="center", fontsize=9, color=GCOLOR[g])
    axC.set_xticks([0, 1])
    axC.set_xticklabels(["per supporter\n(voter-level)", "population-weighted\n(bloc-level)"], fontsize=8.5)
    axC.set_yticks([1, 2, 3]); axC.set_yticklabels(["most\nmisaligned", "2nd", "3rd"], fontsize=8)
    axC.set_ylim(3.5, 0.5); axC.set_xlim(-0.45, 1.45)
    axC.set_title("Same data, two counting frames", fontsize=10)
    axC.spines[["top", "right", "bottom"]].set_visible(False)
    axC.tick_params(bottom=False)

    # --- right: variance attribution stacked bars --------------------------
    factors = ["H", "P", "E", "M", "D", "S", "K"]
    fcolor = {"H": ACCENT, "P": COOL, "E": GOLD, "M": "#6a8f3c",
              "D": MUTE, "S": "#7a5ca8", "K": PALE}
    bottoms = np.zeros(len(glist))
    for f in factors:
        vals = [var[g]["shares"][f] for g in glist]
        axR.bar(range(len(glist)), vals, 0.6, bottom=bottoms, color=fcolor[f],
                label=f, edgecolor="white", linewidth=0.5)
        bottoms += np.array(vals)
    axR.set_xticks(range(len(glist)))
    axR.set_xticklabels([f"{GLABEL[g]}\n({var[g]['dominant_cell'].replace('_',' ')})"
                         for g in glist], fontsize=8)
    axR.set_ylabel("share of $\\mathrm{Var}(\\log PR)$")
    axR.set_ylim(0, 1)
    axR.set_title("What drives the uncertainty\n(dominant cell)", fontsize=10)
    axR.legend(frameon=False, fontsize=8, ncol=2, loc="upper center",
               bbox_to_anchor=(0.5, -0.12))
    axR.spines[["top", "right"]].set_visible(False)

    fig.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
