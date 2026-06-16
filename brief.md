# Brief

Written before research begins. See the workspace docs (run `papers docs`): research-pipeline.md §1.

## Question

When a commentator says a group "voted against its interests," what would have to be true for the claim to be measurable rather than a moral accusation? The phrase presupposes a single objective interest, treats an identity category as a monolith, and folds together at least three distinct judgments: that the candidate's policies harm the group, that the harm was knowable, and that the harm outweighs everything else the voter wanted. Can the accusation be turned into a construct that separates those judgments, prices the free parameters, and reports honestly how much of any verdict is forced by the data versus chosen by the analyst?

## Claim

"Political autoimmunity" — a group supporting a coalition whose likely policies weaken the protections that group disproportionately depends on — can be operationalized as a decomposition, and once it is, the verdict is not robust for the contested cases. Adverse policy risk factors as `R = E·D·H·P·M` (exposure, institutional dependence, candidate hostility, implementation probability, magnitude); a foreseeability gate `K` and a salience gate `S` separate knowable, group-relevant risk from raw exposure; and net alignment under interest model `m` is `Σ W^m (B − R)`, where `B` is the candidate's protective benefit and `W^m` the domain weights a given definition of interest assigns. Gross risk and net alignment are different objects whose difference is exactly the weighted protective-benefit term; "voting against your interests" reports the first and asserts the second.

On a synthetic but anchored three-case dataset (LGBTQ, Muslim, Latino support for Trump in 2024), solved exactly and propagated through 40000 seeded Monte-Carlo draws, three hidden parameters govern the verdict. (1) The interest function: the same Latino vote reads as aligned (net `+0.267`) under a material-interest model and misaligned (`−0.061`) under a rights-dependence model; the net-alignment sign flips for one of the three groups across the seven interest functions, while it stays negative for the other two. (2) The counting frame: per supporter the most-misaligned group is LGBTQ; population-weighted, the politically operative count, it inverts to Latino. (3) The awareness gate, which removes 43–58% of gross risk and is dominated, with exposure and salience, by the quantities the analyst measures worst — exposure alone drives roughly half the multiplicative uncertainty, against seven percent for the well-documented policy-hostility term. Only the extreme case (LGBTQ rights dependence, per voter) is robust, and it breaks in about a quarter of the draws. The construct's contribution is to make those parameters explicit and quantify the verdict's dependence on each, not to issue the verdict.

## Kind

formal-model (ships a simulation). `has_simulation: true`, `claims_target: results.json`. The synthetic-data discipline is central: numbers are facts about the model's geometry, never empirical frequencies, and the paper is scrupulous about the difference. Substantial literature engagement across rational-choice, expressive-voting, social-identity, system-justification, and the folk-theory-of-democracy critiques.

## Cornerstone literature

- Downs (1957), Riker & Ordeshook (1968) — the calculus of voting and why a single vote's instrumental weight is tiny, which opens room for non-policy motives.
- Brennan & Lomasky (1993) — expressive voting; the strongest challenge to any external interest model, since it counts symbolic utility as real.
- Sen (1977) — interest versus preference versus commitment; the conceptual spine of "seven interests, not one."
- Achen & Bartels (2016), Caplan (2007), Converse (1964) — the folk theory of democracy and its critics; retrospective and low-information voting.
- Fiorina (1981), Key (1966) — retrospective voting; protest as rational punishment of incumbents.
- Tajfel & Turner (1979), Green, Palmquist & Schickler (2002), Mason (2018), Iyengar et al. (2019) — social and partisan identity, affective polarization.
- Jost & Banaji (1994), Jost et al. (2004), Sidanius & Pratto (1999) — system justification and social dominance; out-group favoritism among the disadvantaged.
- Mutz (2018), Cramer (2016), Hochschild (2016) — status threat and the expressive economy of resentment.
- Graham, Haidt & Nosek (2009), Stenner (2005) — moral foundations and authoritarian disposition as genuine (not pathological) preference structures.
- Crenshaw (1991), Dawson (1994), Hajnal & Lee (2011) — intersectionality, linked fate, and minority coalition politics; why "group interest" is unstable.
- Sears & Funk (1991), Lupia & McCubbins (1998), Kuklinski et al. (2000) — the weakness of self-interest as a vote predictor; information shortcuts and misinformation.
- Shapley (1953), Saltelli et al. (2008) — the value (used reflexively on the model's own factors) and global sensitivity analysis.
- Data anchors: Pew Research Center 2024 validated-voter study; AP VoteCast; ANES 2024; CES; CAIR 2024 Muslim-voter exit poll (advocacy survey, flagged).

## Risks to manage

Stigmatizing voters; treating groups as monoliths; smuggling partisan assumptions into the coding; calling voters irrational. The paper's defense is structural: the construct is descriptive, the interest function is exposed as a knob rather than fixed, every number carries an uncertainty interval, and the model's job is to show which assumption drives a result, not to certify the result. Neutral vocabulary throughout: misalignment, exposure, dependence, tradeoff, policy-risk acceptance.
