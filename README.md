# political-autoimmunity

**Political Autoimmunity: Adverse-Interest Voting and the Functions That Decide It.** When a commentator says a group "voted against its interests," the claim runs a calculation and hides its inputs. This paper turns the accusation into a measurement model: adverse policy risk factors as exposure × dependence × hostility × implementation × magnitude, gated by foreseeability and salience, and net alignment under a chosen interest function is the candidate's weighted protective benefit minus the weighted risk. Run on three synthetic but anchored 2024 cases (LGBTQ, Muslim, and Latino support for Trump), solved exactly and propagated through 40000 seeded Monte-Carlo draws, the verdict turns out to be governed by three buried analyst choices, the interest function, the per-voter-vs-per-bloc counting frame, and the awareness gate, and for the contested cases it is not robust. The model prices the verdict's dependence on each assumption; it does not issue the verdict. Ships a runnable simulation (`simulation/`) whose `output/results.json` carries every modelled number.

## Build

```bash
uv run build.py          # -> paper/PAPER.pdf  (vendored canonical recipe)
```

Requires `pandoc` and `xelatex` on PATH. From the workspace you can also run
`papers build political-autoimmunity`.

Part of [piatra-papers](https://github.com/piatra-institute). See the workspace
docs for the research and writing pipelines.
