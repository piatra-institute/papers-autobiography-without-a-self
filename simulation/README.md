# Simulation: closure of self-predictable observables

Brute-force search behind the central computational claim of the paper. For a
finite driven system `(Z, U, F)` and a partition `rho` of the states (a candidate
self-observable), `rho` is *autobiographically closed* when its own output history
determines its future observable behaviour (`Delta_ext(rho) = 0`). The search asks
whether the closed observables `Cl(Z)` are closed under two ways of combining two
observables:

- **common refinement** (observe both) — the finer combination;
- **coarser union** (lump their blocks) — the coarser combination.

## Run

```bash
uv run run_all.py          # -> output/results.json  (deterministic; fixed seed)
```

Pure standard library, no dependencies. Exhaustive over all systems with
`|Z| <= 4`; a fixed-seed sample for `|Z|` in `{5, 6}` and `|U| = 3`.

## Files

- `closure.py` — partitions, `rho`-future equivalence, the `Delta_ext = 0` test
  (product-automaton reachability), the two combinations, and the witness
  extractor for a non-closed observable.
- `run_all.py` — the sweep; writes `output/results.json`.
- `output/results.json` — committed output. Every numeric claim in the paper
  resolves to a key here.

## What it reports

`results.json` records, per size, the number of systems tested and how many have
`Cl(Z)` not closed under each combination, the total count of common-refinement
violations across the whole sweep, and the smallest coarser-union counterexample
in full: the system `F`, the two closed observables `rho`, `sigma`, their
non-closed union, and a witness (a common start, two input words with identical
output trajectory reaching future-inequivalent states, and a separating suffix).
