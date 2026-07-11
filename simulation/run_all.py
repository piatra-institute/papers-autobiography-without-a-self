"""Sweep driven systems (Z, U, F) and test whether the autobiographically closed
observables Cl(Z) are closed under the two ways of combining two observables:
common refinement (observe both) and coarser union (lump their blocks).

Exhaustive for |Z| <= 4; a fixed-seed random sample for |Z| in {5, 6} and
|U| = 3, to show the coarsening failure is generic and worsens with size. The
smallest coarser-union counterexample encountered (in size order) is recorded in
full, with a witness: a common start, two input words with identical output
trajectory reaching future-inequivalent states, and a separating suffix.

Entry point:  uv run run_all.py    (writes output/results.json, prints a summary)
Deterministic: the only randomness is the sample, seeded below.
"""
from __future__ import annotations

import itertools
import json
import pathlib
import random
import time

import closure as C

SEED = 20260711
EXHAUSTIVE = [(2, 2), (3, 2), (3, 3), (4, 2)]
SAMPLED = [(5, 2, 25000), (4, 3, 25000), (6, 2, 15000)]

OUT = pathlib.Path(__file__).resolve().parent / "output"


def blocks(rho) -> list[list[int]]:
    groups: dict[int, list[int]] = {}
    for z, b in enumerate(rho):
        groups.setdefault(b, []).append(z)
    return sorted(sorted(v) for v in groups.values())


def _record_counterexample(nZ, nU, F, viol) -> dict:
    rho, sigma, comb = viol
    return {
        "nZ": nZ,
        "nU": nU,
        "F": [list(F[z]) for z in range(nZ)],
        "rho_blocks": blocks(rho),
        "sigma_blocks": blocks(sigma),
        "combined_blocks": blocks(comb),
        "witness": C.closure_witness(nZ, nU, F, comb),
    }


def run_config(nZ, nU, sample_k=None, rng=None):
    parts = C.all_partitions(nZ)
    n_sys = cr_bad = cu_bad = 0
    first_cu = None

    def systems():
        if sample_k is None:
            for flat in itertools.product(range(nZ), repeat=nZ * nU):
                yield [list(flat[z * nU:(z + 1) * nU]) for z in range(nZ)]
        else:
            for _ in range(sample_k):
                yield [[rng.randrange(nZ) for _ in range(nU)] for _ in range(nZ)]

    for F in systems():
        n_sys += 1
        _, cr, cu = C.analyze_system(nZ, nU, F, parts)
        if cr:
            cr_bad += 1
        if cu:
            cu_bad += 1
            if first_cu is None:
                first_cu = _record_counterexample(nZ, nU, F, cu)

    row = {
        "nZ": nZ,
        "nU": nU,
        "mode": "exhaustive" if sample_k is None else f"sample({sample_k})",
        "systems": n_sys,
        "common_refinement_not_closed": cr_bad,
        "coarser_union_not_closed": cu_bad,
        "coarser_union_not_closed_rate": round(cu_bad / n_sys, 4),
        "coarser_union_not_closed_percent": round(100 * cu_bad / n_sys, 1),
    }
    return row, first_cu


def main() -> int:
    t0 = time.time()
    rng = random.Random(SEED)
    sweep = []
    min_counterexample = None

    for nZ, nU in EXHAUSTIVE:
        row, cu = run_config(nZ, nU)
        sweep.append(row)
        if min_counterexample is None and cu is not None:
            min_counterexample = cu

    for nZ, nU, k in SAMPLED:
        row, cu = run_config(nZ, nU, sample_k=k, rng=rng)
        sweep.append(row)
        if min_counterexample is None and cu is not None:
            min_counterexample = cu

    cr_total = sum(r["common_refinement_not_closed"] for r in sweep)
    results = {
        "meta": {
            "seed": SEED,
            "sizes_exhaustive": [list(x) for x in EXHAUSTIVE],
            "sizes_sampled": [list(x) for x in SAMPLED],
            "runtime_seconds": round(time.time() - t0, 1),
        },
        "systems_total": sum(r["systems"] for r in sweep),
        "common_refinement_violations_total": cr_total,
        "sweep": sweep,
        "min_coarser_union_counterexample": min_counterexample,
    }

    OUT.mkdir(exist_ok=True)
    (OUT / "results.json").write_text(json.dumps(results, indent=2))

    print(f"systems tested: {results['systems_total']}")
    print(f"common-refinement violations (all sizes): {cr_total}")
    for r in sweep:
        print(f"  |Z|={r['nZ']} |U|={r['nU']:<2} {r['mode']:>12}  "
              f"systems={r['systems']:>6}  coarser-union-not-closed="
              f"{r['coarser_union_not_closed']:>6} ({r['coarser_union_not_closed_rate']:.1%})")
    cx = min_counterexample
    print(f"smallest coarser-union counterexample: |Z|={cx['nZ']} |U|={cx['nU']}, "
          f"witness words w={cx['witness']['word_w']} w'={cx['witness']['word_w_prime']}")
    print(f"runtime: {results['meta']['runtime_seconds']}s -> output/results.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
