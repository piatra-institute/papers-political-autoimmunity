# Audit

Dated log of editorial passes and verification runs. Newest first.
See the workspace docs (run `papers docs`): writing-pipeline.md §7 and refresh-pipeline.md.

## 2026-06-16 — initial full build

Scope: first complete build from the single seed chat (a research-design dump of the "political autoimmunity / rights-dependence voting misalignment" idea). Wrote the simulation, the paper, and all provenance docs; brought the paper to a clean build and `check => PASS`.

Decisions:

- The seed proposed a 12-section paper plus a 17-component playground spec. That structure was discarded. The genius-level move was to extract one sharp, computable, non-moralizing contribution and build the whole paper on it: "voting against your interests" has at least three hidden free parameters (the interest function, the per-voter-vs-per-bloc counting frame, and the awareness gate), and once they are made explicit the verdict for the contested cases is not robust. Seven sections with substantive titles; no ceremonial Conclusion, no bolt-on Objections (limits folded into §7 as argument).
- Synthetic-data discipline enforced throughout: every exposure/dependence/hostility/implementation/magnitude/salience/awareness value is stipulated to display the model's geometry, stated repeatedly as not an estimate. Only the three vote shares anchor to reported figures, flagged by source quality (Pew validated-voter 0.46; CAIR advocacy exit poll 0.21; exit-poll-summary LGBTQ 0.12).

Simulation (`simulation/`, `uv run run_all.py`, seeded SEED=20240, 40000 MC draws):

- Deterministic: per-cell risk R = E·D·H·P·M, foreseeability gate K = λF+(1−λ)a (λ=0.5), priority risk R·K·S; net alignment V·Σ W^m(B−R) and autoimmunity V·Σ W^m·max(0,R−B−τ) (τ=0.02) under seven interest functions (material, rights, subjective, expressive, coalition-entry, protest, institutional).
- Ranking: per-supporter order LGBTQ > Muslim > Latino is stable (2 distinct orderings across 7 models); population-weighted it inverts to Latino > Muslim > LGBTQ (3 distinct orderings); net-alignment sign flips for exactly one of three groups (Latino, +0.267 material to −0.061 rights), holds negative for LGBTQ (−0.273 to −0.285) and Muslim (−0.111 to −0.189).
- Awareness attrition 0.493 / 0.584 / 0.431. Monte Carlo: P(per-supporter order holds) = 0.743; P(LGBTQ most-misaligned under rights) = 0.918; 90% intervals on priority risk overlap.
- Variance attribution: exact Var(log PR) decomposition on each dominant cell; exposure E the largest single driver (0.272 share LGBTQ cell), E+K together 0.512; policy hostility H only 0.07. Tornado: LGBTQ rights score swings 0.873 of its value across exposure's interval.
- Two figures (exposure.png, verdict.png), both embedded with full captions.

Headline numbers (all keys in `simulation/output/results.json`, 154 distinct numerics):

- gross per supporter 0.819 / 0.473 / 0.367; priority per supporter 0.404 / 0.277 / 0.158; population-weighted priority 0.048 / 0.058 / 0.073.
- per-cell gross risks: LGBTQ 0.459 / 0.207 / 0.153; Muslim 0.246 / 0.086 / 0.142; Latino 0.252 / 0.026 / 0.089.
- MC priority medians 0.396 / 0.27 / 0.151, 90% intervals [0.249, 0.585] / [0.162, 0.417] / [0.08, 0.26].

Verification:

- voice: 0 errors, 1 review-candidate (the §2 title "Seven Interests, Not One", a foundational contrast the section develops; kept per voice.md Pattern-2 nuance). Lexical advisory thinned during the pass: exactly 7→4, precisely 3→0, carries 11→4. One numbered-observation-list error ("two things stand between...") rewritten away; four negate-pivot/inline-contrastive warns rewritten to positive declaratives.
- refs: 44 cited / 44 bib / 0 missing / 0 unused.
- claims: 47 prose decimals, 2 without a matching value (−0.189 and −0.061, both genuine net-alignment outputs whose minus sign the gate strips before matching against the signed JSON; not real mismatches).
- build: 14 pages, both figures embedded, 0 missing-character warnings.
- check => PASS.

Notes / deferred:

- Status set to `built`, not `published`: deploying to the web (sync + page.tsx entry + status flip + GitHub repo create/push) is the maintainer's pipeline step.
- The seed's interactive playground is not built; the runnable simulation is the paper's companion artifact and already exposes the interest function, gates, and counting frame as adjustable inputs in code.
- The seven interest functions use two special mechanisms (subjective weights by stated salience S; institutional weights by institutional dependence D) and five type-weightings; this keeps the rank-reversal a transparent consequence of which domain type each model privileges rather than an arbitrary tuning.
