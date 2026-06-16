# Research

Findings, tiered by source proximity. See the workspace docs (`papers docs`): research-pipeline.md §2.
T1 primary · T2 authoritative secondary · T3 reference · T4 general web (leads only).
A claim that reaches the paper rests on a T1 or T2 source. The modelled numbers are produced by `simulation/` and reconcile against `output/results.json` via `papers claims`; they are facts about the model, not empirical findings, and are tagged [SIM] below.

## The conceptual problem

- [T2] The phrase "voting against your interests" assumes a single objective interest; the popular version (Frank, 2004) was empirically contested by the income-vote gradient (Gelman, 2008; Bartels, 2008) — richer voters, not poorer ones, vote Republican more, so the crude thesis inverts the within-group pattern. — motivates the paper's refusal to fix one interest (§1).
- [T2] Self-interest is a weak predictor of policy attitudes across decades of survey work (Sears & Funk, 1991). — the empirical ground for treating interest as plural rather than assuming a material default (§2).
- [T1] Sen (1977) separates interest, preference, and commitment: a person can act against their own welfare ranking out of commitment without irrationality. — the conceptual spine of "seven interests, not one" (§2, §3).
- [T2] False consciousness (Elster, 1985, on the Marxian construct) and cognitive dissonance (Festinger, 1957) are distinct from measured misalignment: the first presumes deception about real position, the second is a psychological state, while the construct here is a relation among exposure, policy risk, awareness, and vote. — fixes what the paper is not (§1).

## The interest functions (literature behind the seven weightings)

- [T1] Expressive voting: the vote carries symbolic/identity utility because its instrumental weight is negligible (Downs, 1957; Riker & Ordeshook, 1968, the D term; Brennan & Lomasky, 1993). — the strongest challenge to any external interest model; built in as the expressive/protest weightings (§2).
- [T1] Party identification as a standing social identity, not a policy tally (Campbell et al., 1960; Green, Palmquist & Schickler, 2002; Mason, 2018; Iyengar et al., 2012, 2019). — partisanship and affective polarization as utility-bearing; the subjective and expressive models (§2).
- [T1] System justification (Jost & Banaji, 1994; Jost et al., 2004) and social dominance (Sidanius & Pratto, 1999): the disadvantaged may defend the hierarchy that disadvantages them. — the coalition-entry weighting (§2).
- [T2] Status threat (Mutz, 2018), resentment (Cramer, 2016; Hochschild, 2016): status restoration as a motive distinct from material gain. — the expressive/status model (§2). Note the Mutz claim is contested; cited as the model's anchor, not as settled.
- [T1] Moral foundations (Graham, Haidt & Nosek, 2009) and authoritarian disposition (Stenner, 2005): order, authority, sanctity as genuine preference structure. — religious/cultural content of the subjective model; guards against pathologizing (§2).
- [T1] Linked fate and group consciousness (Dawson, 1994; Miller et al., 1981): group exposure becomes a voter priority only under group consciousness. — why the salience gate S is necessary; group-level exposure does not imply voter-level priority (§4).
- [T1] Cross-pressure (Lazarsfeld, Berelson & Gaudet, 1944) and intersectionality (Crenshaw, 1991): conflicting memberships are the normal condition; "group interest" is unstable. — the voter-vs-group distinction and the heterogeneity caveat (§7).

## The awareness gate

- [T1] Information shortcuts (Lupia & McCubbins, 1998), non-attitudes and thin constraint (Converse, 1964), elite cues and the receive-accept-sample model (Zaller, 1992): foreseeability has a supply side. — the public foreseeability term F (§4).
- [T1] Confident misinformation is distinct from ignorance (Kuklinski et al., 2000); framing constructs salience (Tversky & Kahneman, 1981). — the separation of F (public foreseeability) from a (voter self-reported awareness), and the typology of informed-tradeoff vs uninformed vs protest voting (§4).
- [T2] "Voters are not fools": retrospective rationality (Key, 1966; Fiorina, 1981) and realist skepticism about it (Achen & Bartels, 2016; Caplan, 2007). — both halves: the gate must allow informed tradeoff and must not assume it (§4, §6).

## The model and its method

- [SIM] Risk decomposes as R = E·D·H·P·M; net alignment under interest model m is V·Σ W^m(B−R); gross and net differ by exactly the weighted protective-benefit term Σ W^m B. — the decomposition proposition (§3); arithmetic, stated and proven in-text.
- [SIM] On the three synthetic cases: per-supporter priority risk LGBTQ 0.404, Muslim 0.277, Latino 0.158; population-weighted 0.048 / 0.058 / 0.073 — the counting frame inverts the most-misaligned group from LGBTQ to Latino (§5, §6).
- [SIM] Net-alignment sign flips for exactly one of three groups across the seven interest functions: Latino ranges +0.267 (material) to −0.061 (rights); LGBTQ stays −0.273 to −0.285; Muslim −0.111 to −0.189 (§6).
- [SIM] The awareness gate removes 43–58% of gross risk (attrition 0.49 / 0.58 / 0.43) (§5).
- [SIM] Monte Carlo (40000 seeded draws, Beta concentration 12): P(per-supporter order holds) = 0.743; P(LGBTQ most-misaligned under rights model) = 0.918 (§6).
- [SIM] Variance attribution (exact log-variance on each dominant cell): exposure E is the largest driver (~0.27 share for the LGBTQ dominant cell), with the gate K and salience S next; policy hostility H contributes ~0.07; the rights-model score swings 0.87 of its value when exposure moves across its interval (§6).
- [T1] The Shapley value (Shapley, 1953) is used reflexively to attribute the model's own output among input factors; global sensitivity analysis (Saltelli et al., 2008) frames the variance decomposition and tornado (§6).

## Data anchors (vote shares only; flagged by quality)

- [T2] Pew Research Center (2025) validated-voter study: Trump roughly even with Harris among Hispanic voters in 2024 — anchors the Latino vote-share input 0.46 (validated-voter quality) (§5).
- [T3] Council on American-Islamic Relations (2024) exit poll: large Muslim shift toward third-party and Trump — anchors the Muslim input 0.21, flagged explicitly as advocacy-survey, not validated-voter, quality (§5).
- [T3] Exit-poll summaries place LGBTQ Trump support around an eighth — anchors the LGBTQ input 0.12, lowest-quality anchor, used only for order of magnitude (§5).

All exposure, dependence, hostility, implementation, magnitude, salience, and awareness values are stipulated to exhibit the model's geometry. They are not estimates and are not traceable to any T1/T2 source by design; the paper states this repeatedly.
