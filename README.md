# Autobiography Without a Self

Self-Historical Memory as Holonomy of the Minimal Realization.

A driven deterministic system $(Z, U, F)$ can be read as carrying a memory of its own history: fibre the state space over an observable self $x = \pi(z)$, quotient each fibre by future behaviour, and let the input words that return the observable to $x$ act on the quotient as a monoid of closed self-histories. A recent proposal builds nine invariants on this picture and interprets them as autobiographical structure. The construction is classical. The autobiographical fibre $A_x$ is the output-$x$ fibre of the Nerode minimal realization, the self-history monoid is the fibre-restricted transition monoid, which is the Krohn-Rhodes holonomy tile, and the nine invariants reduce term by term to automata, semigroup, and Koopman quantities. The proposed curvature $\Omega = dA + A \wedge A$ is ill-posed, because connection holonomy is invertible while the self-history monoid contains erasures, and because fibre size varies with the observable value. The self-versus-environment defect $\Delta_{\mathrm{ext}}$ measures observability of hidden inputs: a system that copies its last input scores as maximally self-remembering, and the value depends on a hand-chosen observable. The remaining question is whether a canonical self can be discovered from the dynamics. Self-predictable observables are closed under common refinement (proved, and confirmed without exception across $150{,}964$ finite systems) but not under coarsening, which fails in $54{,}300$ of the $65{,}536$ systems with four states and two inputs ($82.9\%$) and in $99.8\%$ of sampled six-state systems; a minimal four-state counterexample is given. The self-predictable observables form a closure system without a canonical coarsest nontrivial member, the same structure as informational closure.

## Simulation

`simulation/` holds the closure search. Every numeric claim in the paper resolves to a key in `simulation/output/results.json`.

```bash
cd simulation && uv run run_all.py     # -> output/results.json (deterministic)
```

## Build

```bash
uv run build.py          # -> paper/PAPER.pdf  (vendored canonical recipe)
```

Requires `pandoc` and `xelatex` on PATH. From the workspace you can also run `papers build autobiography-without-a-self`.

Part of [piatra-papers](https://github.com/piatra-institute). See the workspace docs for the research and writing pipelines.
