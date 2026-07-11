# Brief

## Question

When does a driven system carry a memory of its own history that is more than a
relabelling of its input/output behaviour? Recent work reads small deterministic
systems (gene-regulatory and reaction networks) as Pavlovian-conditionable and
proposes a family of "autobiographical" invariants: fibre a system over its own
observable output, quotient each fibre by future behaviour, and read the
return-word holonomy on each fibre as a record of the system's past selves. Is any
of that apparatus new, and does anything survive once the self-observable is not
handed to the system but has to be discovered?

## Claim

The apparatus reduces to classical theory. For a finite driven system with a
fixed self-observable, the autobiographical fibre is the output-fibre of the
Nerode/bisimulation minimal realization, and its holonomy monoid is the fibre-
restricted transition monoid, which is the Krohn-Rhodes holonomy tile; the nine
proposed invariants each land on a named automata, semigroup, or Koopman quantity.
One proposed differential-geometric invariant is not merely non-novel but ill-
posed. The self-versus-environment defect measures observability, not aboutness,
and is not intrinsic. The one direction that no fixed-observable reduction reaches,
discovering the self-observable, has a definite structure: the autobiographically
self-predictable observables form a closure system under common refinement (proved)
but are generically not closed under coarsening (proved by exhaustive search plus a
minimal counterexample), so a canonical coarsest self does not exist. The tractable
half of that structure coincides with informational closure. The paper delivers the
reduction dictionary, the ill-posedness result, and the closure asymmetry with its
counterexample.

## Kind

formal-model (ships a simulation). `has_simulation: true`,
`claims_target: results.json`. The simulation is an exhaustive/sampled closure
search; every numeric claim traces to `simulation/output/results.json`.

## Cornerstone literature

Krohn and Rhodes (holonomy decomposition); Eilenberg (holonomy method); Nerode and
Rutten (bisimulation, coalgebra); Crutchfield and Young, Shalizi and Crutchfield,
Barnett and Crutchfield (computational mechanics, causal states, epsilon-transducer
crypticity); Littman, Sutton and Singh (predictive-state representations); Massey and
Schreiber (directed information, transfer entropy); Kobayashi and Nomizu (connection
holonomy); Bertschinger, Olbrich, Ay and Jost, and Pfante et al. (informational
closure); Krakauer et al. (individuality); Friston, Kirchhoff et al., Biehl et al.
(Markov blankets and their critique); Fernando et al. and Biswas, Manicka, Hoel and
Levin (associative learning in molecular and gene-regulatory networks, the
motivating claim).
