# autobiography-without-a-self

Reads the "autobiographical" invariants proposed for a driven system's memory of
its own history and shows they are classical. The autobiographical fibre is the
output-fibre of the Nerode minimal realization; the self-history monoid on it is
the fibre-restricted transition monoid, the Krohn-Rhodes holonomy tile; the nine
invariants reduce term by term to automata, semigroup, and Koopman quantities. One
proposed invariant (an autobiographical curvature) is ill-posed; the self-versus-
environment defect measures observability of hidden inputs, not aboutness. The one
question the fixed-observable reductions cannot reach, whether a canonical self can
be discovered from the dynamics alone, is settled by an exhaustive closure search:
the self-predictable observables form a closure system under common refinement but
generically fail it under coarsening, so no canonical coarsest self exists, and the
structure that does survive coincides with informational closure.

## Simulation

`simulation/` holds the closure search. Every numeric claim in the paper resolves
to a key in `simulation/output/results.json`.

```bash
cd simulation && uv run run_all.py     # -> output/results.json (deterministic)
```

## Build

```bash
uv run build.py          # -> paper/PAPER.pdf  (vendored canonical recipe)
```

Requires `pandoc` and `xelatex` on PATH. From the workspace you can also run
`papers build autobiography-without-a-self`.

Part of [piatra-papers](https://github.com/piatra-institute). See the workspace
docs for the research and writing pipelines.
