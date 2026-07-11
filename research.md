# Research

Findings, tiered by source proximity. T1 primary, T2 authoritative secondary.
A claim that reaches the paper rests on a T1 or T2 source, or on the simulation.

## Findings

- [T1] The Nerode/Myhill congruence quotients a machine to its minimal realization; two states merge when their future output maps agree (Nerode, 1958; Rutten, 2000). — supports §3.1, that the autobiographical fibre is the output-fibre of the minimal realization.
- [T1] The Krohn-Rhodes prime decomposition and Eilenberg's holonomy method study the transformation semigroup acting on the subsets ("tiles") of an automaton; the holonomy group of a tile is the group of permutations induced on it (Krohn and Rhodes, 1965; Eilenberg, 1976). — supports §3.2, the master reduction of the self-history monoid to the tile transition monoid.
- [T1] Causal states / predictive-state representations define a state by which futures the past permits (Crutchfield and Young, 1989; Shalizi and Crutchfield, 2001; Littman, Sutton and Singh, 2002). — supports §3.1, the fibre as deterministic predictive state.
- [T1] Automaton minimization proceeds by $k$-equivalence levels; the level at which two states separate is the length of the shortest distinguishing word (Hopcroft, 1971). — supports §3.3, retrieval depth.
- [T1] The epsilon-transducer extends computational mechanics to input-output processes; structural crypticity is the state information not carried by the observed sequence (Barnett and Crutchfield, 2015). — supports §5, the defect equals zero crypticity / output-observability.
- [T1] Parallel transport of a connection is invertible, its inverse the transport along the reversed path (Kobayashi and Nomizu, 1963). — supports §4 obstruction A, incompatibility of connection holonomy with the non-invertible (erasing) elements of the self-history monoid.
- [T1] Informational closure: a coarse-graining whose future is conditionally independent of the fine detail given its own past; the closed coarse-grainings admit a least-closed-refinement operator (Bertschinger, Olbrich, Ay and Jost, 2008; Pfante et al., 2014). — supports §6.4, the closure operator on self-predictable observables coincides with informational closure.
- [T1] Markov-blanket / individuality partitions assign states to a system rather than its environment (Friston, 2013; Kirchhoff et al., 2018; Krakauer et al., 2020), with known non-uniqueness and failure cases (Biehl, Pollock and Kanai, 2021). — supports §7, the disagreement search and its adversary.
- [T1] Associative learning without neurons in molecular and gene-regulatory networks, stored as a persistent dynamical state under fixed equations (Fernando et al., 2009; Biswas, Manicka, Hoel and Levin, 2021; Markevich, Hornberg and Kholodenko, 2004; Levin, 2022). — supports §1, the motivating claim.
- [SIM] Across 150,964 finite driven systems, the autobiographically closed observables are closed under common refinement with zero violations (empirical support for Proposition 5), and fail closure under coarsening in 82.9% of four-state two-input systems, rising to 99.8% at six states; the smallest counterexample has four states and two inputs. — `simulation/output/results.json`; supports §6.2-§6.4.

## Prior audit

The reductions above were first assembled by a multi-agent adversarial audit of the
source construction (an eight-approach portfolio with per-approach verification and a
synthesis), then re-derived and checked here. The audit's failure log: one agent's
transition-monoid order was miscounted (word-length truncation) and corrected; the
source construction's flagship $\mathbb{Z}_3$ example collapses as literally written
(no readout), which the paper reports in §4.
