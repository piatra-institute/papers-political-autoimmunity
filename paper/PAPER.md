---
title: |
  Political Autoimmunity:\
  Adverse-Interest Voting and the Functions That Decide It
author: PIATRA . INSTITUTE
date: June 2026
---

## Abstract

The claim that a group voted against its interests conceals most of its inputs. It assumes a single interest where voters hold several, counts a candidate's likely harm to a group while ignoring what the candidate offers it, treats knowable and unforeseeable harms alike, and does not specify whether it counts voters or votes. We convert the accusation into a measurement model that exposes each input. Adverse policy risk for a group, candidate, and policy domain is the product of exposure, institutional dependence, candidate hostility, implementation probability, and magnitude; foreseeability and salience gates separate the risk a voter could know and weigh from raw exposure; and net alignment under a stated definition of interest is weighted protective benefit minus weighted adverse risk. We apply it to three synthetic but anchored 2024 cases, support for Trump among LGBTQ, Muslim, and Latino voters, solved exactly and propagated through 40,000 seeded Monte Carlo draws. The interest function moves the Latino vote from aligned (net $+0.267$) under a material reading to misaligned ($-0.061$) under a rights reading, while the other two groups remain misaligned under every reading. The counting frame reverses the most-misaligned group from LGBTQ per supporter to Latino per bloc. The gates retain between $0.431$ and $0.584$ of each group's gross risk. Exposure accounts for $0.467$ of the variance in the sharpest cell and policy hostility for $0.016$. The rights-dependence verdict on the LGBTQ case holds in $0.901$ of draws, and the full per-supporter ordering in $0.664$. The model reports how much of a verdict each input drives and issues no verdict itself.

## 1. Introduction

After most elections some group is said to have supported a candidate whose program will remove protections the group relies on, and the support is described as a mistake the group made about itself. The claim has a long history in popular political writing, most influentially in the argument that working-class voters in the American interior trade their economic interests for cultural ones and lose both (Frank, 2004). It has the form of an empirical claim with little empirical content, because the quantity it rests on, the group's interest, is left undefined. The most direct test of the popular version reverses it: among American voters the probability of voting Republican rises with income, so the picture of the poor voting against material interest while the rich vote for it is inconsistent with the income gradient (Gelman, 2008; Bartels, 2008). The accusation survives this test only as a claim about an undisclosed choice made by its author.

That choice is the interest function, the map from a group and a candidate to a number measuring how well the vote served the group. With one interest function fixed, the accusation becomes testable; with a different one, the same vote can receive a different verdict. The folk version assumes a particular interest, usually material self-interest, in a sentence whose grammar implies there is only one, and that assumption gives the claim its apparent obviousness. Survey research undermines even the presumption that material self-interest is the natural default: measured directly, self-interest predicts policy attitudes weakly and inconsistently, while symbolic and group attachments predict them better (Sears and Funk, 1991). Votes seldom track the voter's own balance sheet.

We build the instrument the accusation lacks: a decomposition separating the components the folk claim combines, namely the adverse policy risk a candidate poses to a group, the protection the same candidate offers, whether the risk was foreseeable, whether the affected issue was salient to the group, and which definition of interest is applied. We call the measured pattern political autoimmunity: support from a group for a coalition whose likely policies weaken the legal, administrative, redistributive, and status protections on which the group disproportionately depends. The term refers to the structure, a system's protections turned against the system that maintains them, and carries no verdict about the voters, who may be trading the protection for something they value more, and may be right to do so.

The construct is narrower than several neighbouring concepts, each of which carries a charge the construct is designed to avoid. False consciousness, in its Marxian sense, presumes that the group has a true interest about which it has been deceived, and treats the deception as the explanandum (Elster, 1985); the present model fixes no true interest and treats the choice among interests as the analyst's disclosed assumption. Cognitive dissonance names a psychological state and its reduction (Festinger, 1957), a mechanism inside the voter, whereas political autoimmunity is a relation among exposure, policy risk, awareness, and vote share that can be observed without claims about what voters feel. Intersectional scholarship has shown that a group defined along one axis is cross-cut by others, so the interest of women, of Latino voters, or of the working class is never a single quantity (Crenshaw, 1991). The model adopts that result as a constraint: it computes per subgroup where possible and reports the instability of any group-level number.

## 2. Seven Interest Functions

The premise that a vote serves a single interest is poorly supported, and the alternatives are well-studied utilities. The underlying distinction is Sen's: a person's choices respond to their welfare, to their wider preferences, and to their commitments, which can diverge without any failure of reason, so that acting against one's welfare ranking out of commitment maximizes a different quantity (Sen, 1977). An interest function is a choice of maximand, and the model includes seven, each supported by a literature.

The material reading defines interest as income, employment, benefits, prices, and wealth, and it is the reading the folk accusation usually intends. The rights-dependence reading defines interest as the legal and administrative protections a group relies on (anti-discrimination enforcement, due process, bodily autonomy, immigration security, and the neutrality of agencies), and under it "autoimmunity" is most legible, because a hostile administration can withdraw these protections. The two readings diverge for any group whose material and rights positions move in opposite directions under the same candidate.

The remaining five readings come from the study of why votes track quantities other than the voter's welfare. The instrumental value of a single vote is negligible, because the probability of casting the decisive ballot is extremely small; this is the oldest result in the economic theory of voting (Downs, 1957). Riker and Ordeshook addressed the problem by adding a term to the calculus, a value the voter derives from the act of voting regardless of its effect (Riker and Ordeshook, 1968), and Brennan and Lomasky developed the term into a theory in which the ballot is expressive, a nearly costless occasion to register identity and allegiance (Brennan and Lomasky, 1993). Expressive voting is the strongest challenge to any external interest model, because what an outside analyst records as self-harm the voter records as utility, and a model must allow that reading to prevail where it fits. The subjective reading follows from this: interest is what voters themselves rank as important, measured directly.

Three further readings specify contents the expressive ballot can carry. Party identification is a durable social identity, acquired early and rarely revised, and it predicts the vote more consistently than the issues of any particular election (Campbell et al., 1960; Green, Palmquist and Schickler, 2002); the in-group attachment and out-group antagonism underlying it are the mechanisms described by social identity theory (Tajfel and Turner, 1979). As partisanship has aligned with race, religion, and place, these identities reinforce one another, and affect toward the out-party has become a motive in its own right (Mason, 2018; Iyengar, Sood and Lelkes, 2012; Iyengar et al., 2019). System-justification theory documents that members of disadvantaged groups sometimes defend the arrangements that disadvantage them, which supplies a motive for supporting a dominant coalition from within a group it subordinates (Jost and Banaji, 1994; Jost, Banaji and Nosek, 2004). Social-dominance theory traces the tendency to a measurable preference over group hierarchy (Sidanius and Pratto, 1999), and the weak and shifting attachment of minority voters to either party leaves room to act on it (Hajnal and Lee, 2011). Status, as distinct from money, recurs in the work on recent realignments: perceived threat to a group's relative position moved votes in 2016 on Mutz's contested but careful account (Mutz, 2018), and ethnographies of resentment describe its texture directly (Cramer, 2016; Hochschild, 2016). These literatures supply the expressive-status and coalition-entry readings, in which acceptance and standing are the interests served.

Much of this content is structured commitment, and an external reading that discards it misclassifies votes. Moral intuitions are weighted differently across the political spectrum, with loyalty, authority, and sanctity weighing on the right in ways an interest model built only from care and fairness cannot register (Graham, Haidt and Nosek, 2009); a disposition toward order and conformity, activated by perceived threat, organizes a coherent politics (Stenner, 2005); and ethnocentrism and racial resentment shape policy preferences through channels whose measurement remains contested (Kinder and Kam, 2009; Kinder and Sanders, 1996). Treating any of these as error assumes the conclusion the model is designed to leave open. The seventh reading is protest. A vote can be cast to punish a party instead of to select a government, and retrospective-voting theory treats this as rational: the electorate holds incumbents accountable for outcomes, and punishment is the instrument (Key, 1966; Fiorina, 1981). A protest reading downweights the adverse risk of the punished alternative, because the voter maximizes the signal sent. Whether the protest was well calculated is a separate question that the model can pose and cannot answer from vote choice alone.

None of the seven readings is privileged. Interest is treated as a parameter, and the literatures above supply seven defensible settings, each of which reclassifies some apparent self-harm as religious commitment, expressive identity, status, protest, or a tradeoff the voter would make again. A model that fixed one setting would reproduce the folk accusation in formal terms. The model fixes none and reports how results change across settings.

## 3. Model

Let $g$ index a group or subgroup, $c$ a candidate or coalition, and $j$ a policy domain. The adverse policy risk a candidate poses to a group in a domain is the product of five quantities, each scaled to the unit interval:

$$R_{gcj} = E_{gj}\,D_{gj}\,H_{gcj}\,P_{cj}\,M_{gj}.$$

$E_{gj}$ is the group's exposure to the domain, the share of the group whose circumstances the domain affects. $D_{gj}$ is institutional dependence, the degree to which the group's standing in the domain rests on protections an administration can alter, as opposed to private means the group controls. $H_{gcj}$ is the candidate's hostility, read from platform, record, appointments, and coalition commitments as a signed policy score folded to its adverse part. $P_{cj}$ is the probability that the candidate can and will implement the policy, which depends on unified government, the courts, and administrative capacity. $M_{gj}$ is the magnitude of the harm if implemented. The product form means that a risk is large only when every factor is large: a single small factor, such as an unexposed group or a candidate without the means to act, reduces the domain's contribution regardless of the other factors.

Summed over a group's domains and weighted by the group's support for the candidate, the product gives gross risk, $V_{gc}\sum_j R_{gcj}$, where $V_{gc}$ is the group's vote share for $c$. This is the quantity closest to what the folk accusation refers to, and two corrections separate it from any verdict of self-harm. First, a candidate is rarely hostile to a group in every domain. A platform that withdraws a protection in one domain may extend a benefit in another, and that benefit is part of the vote's return; reading the same signed policy score from its protective side gives $B_{gcj}$, the protection the candidate offers the group in the domain, on the same scale as the harm. Second, domains differ in weight under a given interest. The interest function of Section 2 enters as $W^m_{gj}$, the importance interest model $m$ assigns to the domain, normalized across the group's domains.

Net alignment under interest model $m$ is weighted protection minus weighted risk,

$$\mathrm{NA}_m(g,c) = V_{gc}\sum_j W^m_{gj}\,\bigl(B_{gcj} - R_{gcj}\bigr),$$

and the autoimmunity score retains only the domains in which adverse risk exceeds protection by more than a tolerance $\tau$,

$$A_m(g,c) = V_{gc}\sum_j W^m_{gj}\,\max\!\bigl(0,\; R_{gcj} - B_{gcj} - \tau\bigr).$$

The tolerance, $\tau = 0.02$, prevents domains of negligible net adversity from accumulating into a verdict.

The relation between gross risk and net alignment follows directly. Write the weighted gross risk under model $m$ as $G_m = V_{gc}\sum_j W^m_{gj} R_{gcj}$ and the weighted protective offset as $\Pi_m = V_{gc}\sum_j W^m_{gj} B_{gcj}$. Then $\mathrm{NA}_m = \Pi_m - G_m$, and a group is net-misaligned, $\mathrm{NA}_m < 0$, if and only if $G_m > \Pi_m$. A judgment of self-harm is therefore a claim that weighted risk exceeds weighted protection. The folk accusation observes part of $G_m$, the alarming domain, and concludes that $\mathrm{NA}_m < 0$; the inference is valid only when $\Pi_m$ is small, that is, only when the candidate offers the group nothing it wanted. That condition is sometimes met and usually assumed. Including $\Pi_m$ as an explicit term converts a verdict into a comparison and restores the half of the comparison the accusation omits.

## 4. Foreseeability and Salience Gates

A risk that no one could have foreseen is not evidence about a voter's judgment, and a risk in a domain the voter did not care about is not evidence about the voter's priorities. The model separates both from raw risk with two gates, which divide the charge of irrationality into questions that can be examined one at a time.

Foreseeability has a public and a private component. The public component, $F_{cj}$, is whether the adverse policy was knowable before the vote from the candidate's record, explicit promises, party platform, media coverage, and the warnings of advocacy groups, that is, the supply of available signal. The private component, $a_{gcj}$, is whether voters in the group reported awareness of the issue, the signal actually received. The receive-accept-sample account of opinion makes the supply of elite signal a precondition for mass perception of an issue (Zaller, 1992), and the finding of weak issue constraint in mass publics indicates that supply often goes unreceived (Converse, 1964). Voters who receive the signal reason with it through cues and shortcuts (Lupia and McCubbins, 1998), and received beliefs can be confident and wrong, a failure distinct from the absence of information (Kuklinski et al., 2000). A model that merged these components would confuse a misled voter with an uninformed one and with one the signal never reached. The gate combines them as $K_{gcj} = \lambda F_{cj} + (1-\lambda)\,a_{gcj}$, with $\lambda = 0.5$ giving equal weight, and multiplying risk by $K$ gives foreseeable risk.

Salience is the second gate. Exposure to a domain becomes a voter's priority only when the group perceives the domain as bearing on it, the condition that the literature on group consciousness and linked fate identifies as converting demographic position into political behaviour (Dawson, 1994; Miller et al., 1981). The model includes $S_{gj}$, the salience of the domain to the group, and multiplies again to give priority risk, $R_{gcj} K_{gcj} S_{gj}$. Each gate can only reduce risk, so the model proceeds from what a candidate could do to a group, through what was foreseeable, to what was both foreseeable and salient, and the difference between the first and last quantities is the gap the folk accusation fills with an assumption of negligence.

The gates also yield a typology that replaces the binary of rational and irrational voting. A vote facing high foreseeable and salient risk with low reported awareness is uninformed adverse-interest voting, the information failure the folk claim imagines and the only category in which that account holds. A vote facing the same risk with high awareness and an explicit higher-priority issue is informed tradeoff voting, a knowingly paid price, the case emphasized by the realist argument that the electorate is not foolish (Key, 1966); the model must recognize it in order not to classify every tradeoff as error. Between these lie protest voting, in which the adverse risk is accepted in order to send a signal, and its miscalculated variant, in which the cost of the signal was underestimated; distinguishing these requires a counterfactual the model can specify but not resolve. Framing research shows that salience and awareness depend on how a choice is presented and are not fixed properties of the voter (Tversky and Kahneman, 1981), so the gates measure the information environment as well as the voter. The realist literature questions whether retrospective judgment is as considered as rational-choice accounts suppose (Achen and Bartels, 2016; Caplan, 2007). The model does not take a position on this; it treats awareness as an input whose value changes the verdict and whose measurement is therefore the point of contention.

## 5. Three 2024 Cases

The model is applied to three pairings from the 2024 United States presidential election: support for Trump among LGBTQ, Muslim, and Latino voters. Each was cited in popular commentary as a group voting against itself, and the three differ in the parameters the model isolates. All results are computed from a synthetic dataset whose exposure, dependence, hostility, implementation, magnitude, salience, and awareness values are stipulated to display the model's behaviour and are not estimates. The numbers are properties of a fully specified model, in the way that a worked example in mechanics describes the example. Only the vote shares refer to reported figures, and their sources differ in quality: the Latino share of $0.46$ is anchored to a validated-voter study that found Trump roughly even with Harris among Hispanic voters (Pew Research Center, 2025); the Muslim share of $0.21$ to an advocacy-group exit poll, recorded as such and not as validated-voter evidence (Council on American-Islamic Relations, 2024); and the LGBTQ share of $0.12$ to exit-poll summaries, the weakest anchor, used only for order of magnitude. The cases most discussed in public are thus the hardest to measure.

Each group has three domains. The LGBTQ case covers federal civil-rights protection, transgender health and documentation, and hate-crime and discrimination enforcement, all rights-dependent and all facing a hostile administration; its per-cell gross risks are $0.459$, $0.207$, and $0.153$, the highest single-cell risks in the study, because exposure, dependence, hostility, and implementation are jointly high. The Muslim case covers entry and travel restriction, the Gaza-related foreign-policy grievance that motivated much of the defection, and religious-bias enforcement, with risks of $0.246$, $0.086$, and $0.142$; the protest domain scores low on adverse risk because its hostility is lower and its content is expressive. The Latino case covers immigration enforcement, the economy, and civil-rights enforcement, with risks of $0.252$, $0.026$, and $0.089$; the economy domain is the only cell in the study in which the candidate is read as protective, with a nonzero benefit $B$. Figure 1 shows the nine cells and the effect of the gates.

![Left: per-cell gross risk $R = E\,D\,H\,P\,M$ for the nine group-domain cells. The LGBTQ civil-rights cell ($0.459$) is the largest single risk in the study; the Latino economy cell ($0.026$) is the smallest, because the candidate is read as protective there. Right: gross risk $\sum R$, foreseeable risk $\sum RK$, and priority risk $\sum RKS$ for each group; the percentage is priority over gross, the share of raw risk retained as both foreseeable and salient. The gates retain between 43% and 58% of gross risk, removing between 42% and 57%, and the fraction differs by group.](../simulation/output/figures/exposure.png){width=100%}

Gross risk per supporter is $0.819$ for the LGBTQ case, $0.473$ for the Muslim case, and $0.367$ for the Latino case. The gates reduce these to priority risks of $0.404$, $0.277$, and $0.158$, retaining $0.493$, $0.584$, and $0.431$ of gross risk and removing $0.507$, $0.416$, and $0.569$. The Muslim case retains the largest share because its dominant adverse domain, entry restriction, is among the most foreseeable in the study, having been openly promised and previously enacted; the gate keeps more of a hostility the candidate has made explicit. The LGBTQ case loses about half its gross risk because some of its largest exposure lies in a lower-salience domain. The Latino case loses the most because its dominant domain is somewhat less foreseeable and the economy domain, where the group's attention is concentrated, carries little adverse risk.

## 6. Interest Function, Counting Frame, and Uncertainty

### 6.1 Counting frame

The per-supporter ordering of priority risk, LGBTQ, then Muslim, then Latino, does not depend on the interest function, but it is the wrong unit for the question the accusation poses. A claim about a group voting against itself concerns a bloc, and a bloc's electoral effect scales with its size. Weighting each group's priority risk by its vote share reverses the order: population-weighted priority risk is $0.048$ for the LGBTQ case, $0.058$ for the Muslim case, and $0.073$ for the Latino case. The group with the highest risk per supporter forms the lowest-impact bloc and the group with the lowest risk per supporter the highest-impact bloc, because the LGBTQ vote share is small and the Latino share large. Both numbers are correct and answer different questions. Per supporter, the LGBTQ case is the clearest instance of a vote at odds with a group's rights dependence; per votes moved, the Latino case is where the pattern bears most on an outcome. The folk accusation does not specify which it means, and the two readings identify different groups.

### 6.2 Interest function

The interest function has its largest effect on net alignment, where the protective term of Section 3 operates. Figure 2 plots net alignment for the three groups across the seven interest functions. The LGBTQ line lies between $-0.285$ and $-0.273$, because the case has no protective domain for any interest function to weight: every reading finds the vote misaligned, differing only in degree. The Muslim line remains negative throughout, from $-0.111$ under the protest reading, which downweights the adverse domains in favour of the expressive one, to $-0.189$ under the coalition-entry reading. The Latino line crosses zero. Under the material reading, which weights the economy domain in which the candidate is protective, Latino net alignment is $+0.267$; under the rights-dependence reading, which weights immigration and civil-rights enforcement, it is $-0.061$. The same vote and the same data yield opposite verdicts, and the only change is the analyst's definition of interest. The sign of the verdict depends on that choice for one of the three groups, so sensitivity to the assumption is uneven across cases, and the model identifies which verdicts are robust. The autoimmunity score names LGBTQ the most misaligned group under all seven interest functions, while the order of the other two groups reverses under the expressive and protest readings, giving two distinct per-supporter orderings; per bloc, the most-misaligned group is Latino under six readings and Muslim under the material reading.

![Left: net alignment per supporter for each group across the seven interest functions, with the zero line dividing aligned from misaligned. The LGBTQ case is negative and nearly flat; the Muslim case is negative throughout; the Latino case is aligned under the material, subjective, expressive, coalition-entry, and institutional readings and misaligned under rights dependence and protest. Center: group rank by priority risk per supporter and population-weighted; the order reverses because vote share runs in the opposite direction. Right: share of the variance of log priority risk in each group's dominant cell attributable to each input, exact for the Beta-distributed factors and by the delta method for the composite awareness gate, with each input drawn at its own measurement-quality concentration. Exposure $E$, salience $S$, and awareness $K$, the survey-estimated inputs given wide priors, dominate; policy hostility $H$, given a tight prior, contributes least.](../simulation/output/figures/verdict.png){width=100%}

### 6.3 Sources of uncertainty

The third parameter concerns the measurement of the inputs on which the assumptions act. Priority risk in a single domain is a product of independent factors, so the variance of its logarithm decomposes into a sum of per-factor terms, and each factor's share attributes the uncertainty in the verdict. The attribution is informative because each input has its own measurement-quality concentration. The three survey-estimated inputs, exposure, salience, and reported awareness, are drawn from wide Beta priors (concentrations 5, 5, and 4), and the inputs read from the public record, hostility, implementation probability, magnitude, institutional dependence, and public foreseeability, from tight ones (concentration 30), so the decomposition reflects a stipulated difference in measurement quality in addition to the stipulated means. For the dominant LGBTQ cell, exposure accounts for $0.467$ of the variance, salience for $0.36$, and awareness for $0.107$, while hostility, implementation, magnitude, and dependence account for $0.016$ each. Exposure and awareness together account for $0.574$, and exposure and salience for $0.827$. The pattern holds in all three cases: uncertainty in the verdict is dominated by exposure, salience, and awareness, the quantities estimated from surveys with the widest error, and is least sensitive to candidate hostility, the quantity read from the public record with most confidence. A one-at-a-time analysis agrees. Moving each input of the LGBTQ rights-model score across its 5-95% interval changes the score by $1.269$ of its value for exposure and by $0.21$ to $0.27$ of its value for each policy factor. The accusation places its weight on the input that contributes least to the uncertainty.

Propagating every input as a Beta distribution at its own concentration over 40,000 seeded draws yields intervals for the verdict. Per-supporter priority risks have medians of $0.394$, $0.27$, and $0.148$ for the three cases, with 90% intervals of $0.206$ to $0.636$ (LGBTQ), $0.148$ to $0.429$ (Muslim), and $0.064$ to $0.282$ (Latino), which overlap. The per-supporter ordering holds in $0.664$ of draws, so about one draw in three reorders the groups under input uncertainty alone. The most robust statement in the study, that the LGBTQ case is the most misaligned under the rights-dependence reading per supporter, holds in $0.901$ of draws and fails in about one in ten. The uncertainty is reportable, and a defensible verdict takes the form of an interval with an attached probability. The attribution applies to the model's own output the logic of a value over the factors of a game (Shapley, 1953) and of variance-based global sensitivity analysis (Saltelli et al., 2008): before grading a vote, the model reports which of its assumptions the grade depends on.

## 7. Limitations

Each of the three analyst choices is a point at which calculation ends and commitment begins. The interest function is a normative claim about what a group ought to value, and no measurement settles it; the model prices it, showing that adopting the rights reading over the material one produces the entire misalignment verdict in the Latino case, which moves the argument to the defence of the reading. The counting frame is a choice of question, per voter or per bloc, and the two identify different groups from the same data, so a verdict that does not state its unit is incomplete. The awareness gate depends on what a group knew and weighed, the quantity surveys estimate worst, and the same gate that separates informed tradeoff from uninformed error cannot, from vote choice alone, distinguish a tradeoff from a miscalculated protest, because the two differ in a counterfactual no cross-section observes. Beneath the group score lies within-group variation: exposure, salience, and awareness vary within every group studied, and the cross-pressured voter subject to several memberships at once is the normal case (Lazarsfeld, Berelson and Gaudet, 1944; Crenshaw, 1991). A population-weighted number is an ecological summary, and reading it as a per-voter verdict commits the ecological fallacy.

The input values are stipulated, the vote-share anchors are of unequal quality, and the measurement-quality concentrations are themselves assumptions; the variance attribution follows from them. The model also shares a commitment with the accusation it examines. Calling a vote self-harm claims standing to define a group's interest against the group's expressed choice, and the expressive and subjective readings deny that standing. The model does not resolve the question: it retains the subjective reading, interest as what voters say they value, among the seven, and measures how far each external reading departs from it.

## 8. Conclusion

A decomposition with disclosed inputs converts the accusation that a group voted against its interests into a measurement. For the cases most argued over in public, the verdict is governed by three analyst choices, the interest function, the counting frame, and the awareness gate, and under realistic uncertainty most verdicts are not robust. One configuration holds up, the rights-dependence reading of the LGBTQ case per voter, in $0.901$ of draws. Where an external reading of interest agrees with the subjective one, a verdict is well supported; where they diverge, the verdict is a contest between the analyst's account of a group's interest and the group's own, and the instrument can defend only the size of the divergence, the distance between what a group votes for and what would serve it under a stated theory of its interest. That distance is computable, and whether it justifies an accusation is a judgment outside the arithmetic. A carefully constructed measure of political autoimmunity more often supports withholding the accusation than making it.

## Reproducibility

All model numbers are produced by `simulation/run_all.py` (seed 20240, 40,000 Monte Carlo draws), which writes `simulation/output/results.json` and both figures. The deterministic quantities are exact; the variance attribution is exact for the Beta factors and uses the delta method for the composite awareness gate.

## References

Achen, C. H., and Bartels, L. M. (2016). *Democracy for Realists: Why Elections Do Not Produce Responsive Government*. Princeton University Press.

Bartels, L. M. (2008). *Unequal Democracy: The Political Economy of the New Gilded Age*. Princeton University Press.

Brennan, G., and Lomasky, L. (1993). *Democracy and Decision: The Pure Theory of Electoral Preference*. Cambridge University Press.

Campbell, A., Converse, P. E., Miller, W. E., and Stokes, D. E. (1960). *The American Voter*. Wiley.

Caplan, B. (2007). *The Myth of the Rational Voter: Why Democracies Choose Bad Policies*. Princeton University Press.

Converse, P. E. (1964). The nature of belief systems in mass publics. In D. E. Apter (Ed.), *Ideology and Discontent* (pp. 206–261). Free Press.

Council on American-Islamic Relations. (2024). *CAIR Exit Poll of Muslim Voters: 2024 General Election*. CAIR.

Cramer, K. J. (2016). *The Politics of Resentment: Rural Consciousness in Wisconsin and the Rise of Scott Walker*. University of Chicago Press.

Crenshaw, K. (1991). Mapping the margins: Intersectionality, identity politics, and violence against women of color. *Stanford Law Review*, 43(6), 1241–1299.

Dawson, M. C. (1994). *Behind the Mule: Race and Class in African-American Politics*. Princeton University Press.

Downs, A. (1957). *An Economic Theory of Democracy*. Harper & Row.

Elster, J. (1985). *Making Sense of Marx*. Cambridge University Press.

Festinger, L. (1957). *A Theory of Cognitive Dissonance*. Stanford University Press.

Fiorina, M. P. (1981). *Retrospective Voting in American National Elections*. Yale University Press.

Frank, T. (2004). *What's the Matter with Kansas? How Conservatives Won the Heart of America*. Metropolitan Books.

Gelman, A. (2008). *Red State, Blue State, Rich State, Poor State: Why Americans Vote the Way They Do*. Princeton University Press.

Graham, J., Haidt, J., and Nosek, B. A. (2009). Liberals and conservatives rely on different sets of moral foundations. *Journal of Personality and Social Psychology*, 96(5), 1029–1046.

Green, D. P., Palmquist, B., and Schickler, E. (2002). *Partisan Hearts and Minds: Political Parties and the Social Identities of Voters*. Yale University Press.

Hajnal, Z. L., and Lee, T. (2011). *Why Americans Don't Join the Party: Race, Immigration, and the Failure of Political Parties to Engage the Electorate*. Princeton University Press.

Hochschild, A. R. (2016). *Strangers in Their Own Land: Anger and Mourning on the American Right*. New Press.

Iyengar, S., Lelkes, Y., Levendusky, M., Malhotra, N., and Westwood, S. J. (2019). The origins and consequences of affective polarization in the United States. *Annual Review of Political Science*, 22, 129–146.

Iyengar, S., Sood, G., and Lelkes, Y. (2012). Affect, not ideology: A social identity perspective on polarization. *Public Opinion Quarterly*, 76(3), 405–431.

Jost, J. T., and Banaji, M. R. (1994). The role of stereotyping in system-justification and the production of false consciousness. *British Journal of Social Psychology*, 33(1), 1–27.

Jost, J. T., Banaji, M. R., and Nosek, B. A. (2004). A decade of system justification theory: Accumulated evidence of conscious and unconscious bolstering of the status quo. *Political Psychology*, 25(6), 881–919.

Key, V. O. (1966). *The Responsible Electorate: Rationality in Presidential Voting, 1936–1960*. Harvard University Press.

Kinder, D. R., and Kam, C. D. (2009). *Us Against Them: Ethnocentric Foundations of American Opinion*. University of Chicago Press.

Kinder, D. R., and Sanders, L. M. (1996). *Divided by Color: Racial Politics and Democratic Ideals*. University of Chicago Press.

Kuklinski, J. H., Quirk, P. J., Jerit, J., Schwieder, D., and Rich, R. F. (2000). Misinformation and the currency of democratic citizenship. *Journal of Politics*, 62(3), 790–816.

Lazarsfeld, P. F., Berelson, B., and Gaudet, H. (1944). *The People's Choice: How the Voter Makes Up His Mind in a Presidential Campaign*. Columbia University Press.

Lupia, A., and McCubbins, M. D. (1998). *The Democratic Dilemma: Can Citizens Learn What They Need to Know?* Cambridge University Press.

Mason, L. (2018). *Uncivil Agreement: How Politics Became Our Identity*. University of Chicago Press.

Miller, A. H., Gurin, P., Gurin, G., and Malanchuk, O. (1981). Group consciousness and political participation. *American Journal of Political Science*, 25(3), 494–511.

Mutz, D. C. (2018). Status threat, not economic hardship, explains the 2016 presidential vote. *Proceedings of the National Academy of Sciences*, 115(19), E4330–E4339.

Pew Research Center. (2025). *Behind Trump's 2024 Victory, a More Racially and Ethnically Diverse Voter Coalition*. Pew Research Center.

Riker, W. H., and Ordeshook, P. C. (1968). A theory of the calculus of voting. *American Political Science Review*, 62(1), 25–42.

Saltelli, A., Ratto, M., Andres, T., Campolongo, F., Cariboni, J., Gatelli, D., Saisana, M., and Tarantola, S. (2008). *Global Sensitivity Analysis: The Primer*. Wiley.

Sears, D. O., and Funk, C. L. (1991). The role of self-interest in social and political attitudes. *Advances in Experimental Social Psychology*, 24, 1–91.

Sen, A. (1977). Rational fools: A critique of the behavioral foundations of economic theory. *Philosophy & Public Affairs*, 6(4), 317–344.

Shapley, L. S. (1953). A value for n-person games. In H. W. Kuhn and A. W. Tucker (Eds.), *Contributions to the Theory of Games, Volume II* (pp. 307–317). Princeton University Press.

Sidanius, J., and Pratto, F. (1999). *Social Dominance: An Intergroup Theory of Social Hierarchy and Oppression*. Cambridge University Press.

Stenner, K. (2005). *The Authoritarian Dynamic*. Cambridge University Press.

Tajfel, H., and Turner, J. C. (1979). An integrative theory of intergroup conflict. In W. G. Austin and S. Worchel (Eds.), *The Social Psychology of Intergroup Relations* (pp. 33–47). Brooks/Cole.

Tversky, A., and Kahneman, D. (1981). The framing of decisions and the psychology of choice. *Science*, 211(4481), 453–458.

Zaller, J. R. (1992). *The Nature and Origins of Mass Opinion*. Cambridge University Press.
