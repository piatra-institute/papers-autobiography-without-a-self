# Audit

Dated log of editorial passes and verification runs. Newest first.

## 2026-07-11 — draft, simulation, and build

Scope: initial construction of the paper from a multi-agent adversarial audit of
the source "autobiographical causal holonomy" proposal (origin thread in
`chats/chat.md`).

Changes:
  - simulation/ written: `closure.py` (rho-future equivalence, the Delta_ext = 0
    test by product reachability, the two partition combinations, witness
    extractor), `run_all.py` (exhaustive |Z|<=4 plus fixed-seed samples at |Z| in
    {5,6}, |U|=3), output committed to `output/results.json`.
  - paper/PAPER.md drafted: reduction of the nine invariants to the minimal
    realization and the Krohn-Rhodes holonomy tile (Propositions 1-2, table),
    ill-posedness of the curvature invariant (Proposition 3, three obstructions,
    the Z_3 collapse), the self/environment defect as observability (Proposition
    4), autobiographical closure with the common-refinement closure theorem
    (Proposition 5) and the coarsening-failure computation.
  - metadata, brief, sources, research, README filled.

Verification:
  - simulation: 150,964 systems; 0 common-refinement violations (empirical
    support for Proposition 5); coarsening fails in 54,300 / 65,536 (82.9%) at
    |Z|=4,|U|=2, rising to 97.8% (|Z|=5) and 99.8% (|Z|=6); minimal counterexample
    at |Z|=4,|U|=2 recorded with witness. Fixed seed 20260711, deterministic.
  - voice: 0 errors, 0 review-candidates after a pass removing three inline
    contrastives and reducing the "carry/carries" count. Advisories remain
    (tricolon count 8; one 23-sentence run without a short sentence).
  - refs: 23 in-text keys, 23 bib entries, 0 missing, 0 unused.
  - claims: 3 decimal claims in prose, 0 without a matching key in results.json.
  - build: PAPER.pdf, 12 pages, letter; no missing-character warnings; math
    (curvature form, holonomy action, restriction maps, theorem environments)
    renders under Palatino.
  - check => PASS.

Open (deliberately not done): create the GitHub repo and push; `papers sync` /
`web-entry` to publish. Status left at `built`.

Prior-audit failure log (for honesty): during the multi-agent audit, one agent's
transition-monoid order was miscounted from a word-length truncation and
corrected; the source proposal's flagship Z_3 example collapses as literally
written (no readout), reported in the paper's Section 4.

---

## 2026-07-11 — stand-alone fixes + publish

Editorial pass to remove two standalone-rule violations the automated gates do not catch, plus a light rhythm touch, then full publish.

- paper/PAPER.md §7 + References: removed the cross-reference to the sibling PIATRA paper "Owned Causality" (in-text clause and bibliography entry); rewrote §7's close to stand alone. refs rebalanced 23 -> 22 in-text/bib, 0 missing/0 unused.
- paper/PAPER.md abstract: replaced the repo-internal pointer "Every numeric claim traces to a key in `simulation/output/results.json`" with a self-contained sentence ("...reproduced by an accompanying exhaustive computation"); a standalone PDF should not cite a file the reader lacks.
- brief.md, sources.md: dropped the Owned Causality companion lines to match.
- paper/PAPER.md §3.1, §3.2: added two short sentences ("This adds nothing." / "Forgetting is not incidental.") to ease the voice rhythm advisory; no content, numbers, proofs, or citations changed.
- Pipeline: rebuilt PDF; voice 0 errors; refs 22/22; claims 3/3 matched; check => PASS. status -> published; synced PDF to the web app; added the ownPapers entry to piatra-institute-web/app/papers/page.tsx (topics: mathematics/computer-science/philosophy; kinds: formal/simulation), left uncommitted per the never-commit-web rule.
- Git: first commit `setup: initial commit` (SSH-signed); created public repo piatra-institute/papers-autobiography-without-a-self; pushed.
