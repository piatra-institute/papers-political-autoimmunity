# Political Autoimmunity

Adverse-Interest Voting and the Functions That Decide It.

The claim that a group voted against its interests conceals most of its inputs. It assumes a single interest where voters hold several, counts a candidate's likely harm to a group while ignoring what the candidate offers it, treats knowable and unforeseeable harms alike, and does not specify whether it counts voters or votes. We convert the accusation into a measurement model that exposes each input. Adverse policy risk for a group, candidate, and policy domain is the product of exposure, institutional dependence, candidate hostility, implementation probability, and magnitude; foreseeability and salience gates separate the risk a voter could know and weigh from raw exposure; and net alignment under a stated definition of interest is weighted protective benefit minus weighted adverse risk. We apply it to three synthetic but anchored 2024 cases, support for Trump among LGBTQ, Muslim, and Latino voters, solved exactly and propagated through 40,000 seeded Monte Carlo draws. The interest function moves the Latino vote from aligned (net $+0.267$) under a material reading to misaligned ($-0.061$) under a rights reading, while the other two groups remain misaligned under every reading. The counting frame reverses the most-misaligned group from LGBTQ per supporter to Latino per bloc. The gates retain between $0.431$ and $0.584$ of each group's gross risk. Exposure accounts for $0.467$ of the variance in the sharpest cell and policy hostility for $0.016$. The rights-dependence verdict on the LGBTQ case holds in $0.901$ of draws, and the full per-supporter ordering in $0.664$. The model reports how much of a verdict each input drives and issues no verdict itself.

## Build

```bash
uv run build.py          # -> paper/PAPER.pdf  (vendored canonical recipe)
```

Requires `pandoc` and `xelatex` on PATH. From the workspace you can also run `papers build political-autoimmunity`.

Part of [piatra-papers](https://github.com/piatra-institute). See the workspace docs for the research and writing pipelines.
