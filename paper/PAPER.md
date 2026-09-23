---
title: |
  Autobiography Without a Self:\
  Self-Historical Memory as Holonomy of the\
  Minimal Realization
author: PIATRA . INSTITUTE
date: July 2026
---

## Abstract

A driven deterministic system $(Z, U, F)$ can be read as carrying a memory of its own history: fibre the state space over an observable self $x = \pi(z)$, quotient each fibre by future behaviour, and let the input words that return the observable to $x$ act on the quotient as a monoid of closed self-histories. A recent proposal builds nine invariants on this picture and interprets them as autobiographical structure. The construction is classical. The autobiographical fibre $A_x$ is the output-$x$ fibre of the Nerode minimal realization, the self-history monoid is the fibre-restricted transition monoid, which is the Krohn-Rhodes holonomy tile, and the nine invariants reduce term by term to automata, semigroup, and Koopman quantities. The proposed curvature $\Omega = dA + A \wedge A$ is ill-posed, because connection holonomy is invertible while the self-history monoid contains erasures, and because fibre size varies with the observable value. The self-versus-environment defect $\Delta_{\mathrm{ext}}$ measures observability of hidden inputs: a system that copies its last input scores as maximally self-remembering, and the value depends on a hand-chosen observable. The remaining question is whether a canonical self can be discovered from the dynamics. Self-predictable observables are closed under common refinement (proved, and confirmed without exception across 150,964 finite systems) but not under coarsening, which fails in 54,300 of the 65,536 systems with four states and two inputs ($82.9\%$) and in $99.8\%$ of sampled six-state systems; a minimal four-state counterexample is given. The self-predictable observables form a closure system without a canonical coarsest nontrivial member, the same structure as informational closure.

## 1. Introduction

A small chemical or gene-regulatory network, simulated as a system of ordinary differential equations, can be put through a Pavlovian conditioning protocol and pass it: after a neutral input is paired with an effective one, the neutral input alone drives the response. @fernando2009 built explicit molecular circuits that learn associatively; @biswas2021 find associative memory across published transcriptional-network models; the bistable multisite-phosphorylation cascade of @markevich2004 supplies the hysteresis that stores the acquired state. @levin2022 interprets such results as memory and minimal agency in substrates without neurons. The equations do not change during training. A state variable crosses a separatrix and remains on the other side, so the same present input meets a different internal configuration and produces a different output. The system's past is recorded in its current position in state space.

A further construction has been proposed on this basis. The system is fibred over its own observable present, $x = \pi(z)$, the "present self". Over each value $x$ lies the set of hidden states that present as $x$; quotienting it by future behaviour gives an autobiographical fibre $A_x$; a self-history that departs from $x$ and returns acts on $A_x$, and such histories generate a monoid of closed self-histories. Nine invariants are defined on this structure and offered as a coordinate-free account of which distinctions among a system's past selves remain causally effective, what they represent, and how experiences transform them, in the vocabulary of memory, identity, autobiography, and self-model.

In the finite deterministic setting that the construction specifies, the apparatus relabels existing theory. The fibre $A_x$ is the output-$x$ slice of the minimal realization; the self-history monoid is the transition monoid of that realization restricted to the slice, which the Krohn-Rhodes holonomy decomposition already studies; the nine invariants are automata, semigroup, and Koopman quantities under new names. One of the nine is ill-posed. The self-versus-world invariant measures a system's failure to observe its own inputs, which differs from what its name suggests. One question lies outside these reductions: the self-observable $\pi$ is supplied to the construction from outside, whereas the object of interest would be a self that the system determines on its own. Section 6 states that question precisely and settles its lattice-theoretic core by exhaustive computation. The answer is partly negative and identifies where new content could still arise.

## 2. The construction

A **driven system** is a triple $(Z, U, F)$ with $Z$ a finite set of states, $U$ a finite input alphabet, and $F : Z \times U \to Z$ a transition map. Write $\Phi_w(z)$ for the state reached from $z$ by the input word $w \in U^{*}$, with $\Phi_{\varepsilon}(z) = z$ and $\Phi_{wu}(z) = F(\Phi_w(z), u)$. A **self-observable** is a surjection $\pi : Z \to X$; its value $x = \pi(z)$ is the present self, and $F_x = \pi^{-1}(x)$ is the fibre over $x$.

Two hidden states in the same fibre are distinguished only if some future intervention exposes a difference in the observable.

\begin{definition}[Autobiographical fibre]
For $z, z' \in F_x$, write $z \sim_x z'$ when $\pi(\Phi_w(z)) = \pi(\Phi_w(z'))$ for every $w \in U^{*}$. The autobiographical fibre is the quotient $A_x = F_x / {\sim_x}$.
\end{definition}

A word $\gamma$ with $\pi(\Phi_{\gamma}(z)) = x$ for the relevant states returns the observable to its starting value. Such a closed self-history acts on $A_x$ by $T_{\gamma}([z]) = [\Phi_{\gamma}(z)]$, and the closed self-histories generate a monoid $H_x$ acting on $A_x$. The monoid is generally not a group: a self-history can merge two classes that no later history separates again, so erasure is possible and the action is non-invertible.

The proposal attaches nine invariants to $(A_x, H_x)$, all taken up to conjugacy of the action: the multiplicity $\mu(x) = \lvert A_x \rvert$; the isomorphism class of $H_x \curvearrowright A_x$; a rank spectrum; a reversibility and consolidation profile; an autobiographical curvature $\Omega = dA + A \wedge A$; a retrieval-depth spectrum; a self-history factorization defect $\Delta_{\mathrm{ext}}$; a historical representation lattice; and a persistence spectrum. Sections 3 to 5 treat them in turn.

## 3. Identification with the minimal realization

### 3.1 The autobiographical fibre

The Moore machine $(Z, U, F, \pi)$ has a future-observation map $\beta_z : U^{*} \to X$, $w \mapsto \pi(\Phi_w(z))$. Nerode equivalence identifies $z$ and $z'$ when $\beta_z = \beta_{z'}$; the quotient is the minimal realization $M$, with an induced output map $\bar\pi : M \to X$ and transition action $\bar\delta_w$ [@nerode1958; @rutten2000]. Write $Q_x = \bar\pi^{-1}(x)$ for its fibre over $x$.

\begin{proposition}
The relation $\sim_x$ is Nerode equivalence restricted to $F_x$, and $A_x$ is canonically the fibre $Q_x$ of the minimal realization.
\end{proposition}

\begin{proof}
For $z, z' \in F_x$ the defining condition of $\sim_x$, equality of $\pi(\Phi_w(z))$ and $\pi(\Phi_w(z'))$ for all $w$, is equality of $\beta_z$ and $\beta_{z'}$, which is Nerode equivalence. Because $\beta_z(\varepsilon) = \pi(z)$, Nerode equivalence refines the $\pi$-fibre partition, so $\bar\pi$ is well defined and no Nerode class straddles two values of $\pi$. The quotient map $Z \to M$ therefore maps $F_x$ onto the Nerode classes with output $x$, which are the elements of $Q_x$, and it identifies exactly the $\sim_x$-equivalent states. Hence $A_x \cong Q_x$.
\end{proof}

The autobiographical fibre therefore holds no information beyond the minimal realization. It is the deterministic predictive state of the system at the observable $x$, the state defined by which future observations the past permits, in the sense of the predictive-state representations of @littman2002 and the causal states of @crutchfield1989; its minimal predictive formulation is that of @{shalizi2001}.

### 3.2 The self-history monoid as holonomy tile

Give $M(\text{min})$ its transition monoid, the set of maps $\bar\delta_w$ for $w \in U^{*}$ under composition. For the fibre $Q_x$, collect the restrictions of the fibre-preserving words,
$$M_{Q_x} = \{\, \bar\delta_w \restriction Q_x \;:\; w \in U^{*},\ \bar\delta_w(Q_x) \subseteq Q_x \,\}.$$

\begin{proposition}
The self-history action $H_x \curvearrowright A_x$ equals the restricted transition action $M_{Q_x} \curvearrowright Q_x$. The group of units of $H_x$ is the Krohn-Rhodes holonomy group of the tile $Q_x$.
\end{proposition}

`\begin{proof}`{=latex} A closed self-history at $x$ is a word $w$ whose transition returns the whole fibre, $\bar\delta_w(Q_x) \subseteq Q_x$, which is the condition for $T_w$ to be a total self-map of $A_x$; under the identification of Proposition 1, $T_w = \bar\delta_w \restriction Q_x$. Fibre-preserving words contain the empty word and are closed under concatenation, and every element of $M_{Q_x}$ is $\bar\delta_w \restriction Q_x$ for such a $w$, so the two monoids of transformations of $Q_x$ coincide. The invertible elements are the permutations of $Q_x$ induced by return words, which are the holonomy group of the tile in the Eilenberg holonomy decomposition of the transition monoid [@krohn1965; @eilenberg1976]. `\end{proof}`{=latex}

The construction slices the minimal automaton by the observable and reads off the return-word monoid on each slice. The choice of a monoid, motivated by the fact that learning includes forgetting, is already built into the holonomy decomposition, where the transformation semigroup acting on a tile need not be a group and non-invertible elements are part of the structure.

### 3.3 The nine invariants

With Propositions 1 and 2, each remaining invariant is computed inside $(M(\text{min}), \bar\pi, U)$, given the choice of fibre and, for the last, a baseline input.

| invariant | classical object |
|---|---|
| multiplicity $\mu(x) = \lvert A_x \rvert$ | number of minimal-realization states with output $x$ |
| monoid action $H_x \curvearrowright A_x$ | fibre-restricted transition monoid, the Krohn-Rhodes holonomy tile |
| rank spectrum | image sizes of monoid elements, graded by word length |
| reversibility profile | Green's relations, resets, nilpotency index of $H_x$ |
| autobiographical curvature | ill-posed; residue is non-commutativity of $H_x$ (Section 4) |
| retrieval depth | shortest distinguishing-word length, the Moore-Hopcroft levels |
| self/environment defect $\Delta_{\mathrm{ext}}$ | output-observability with unknown inputs (Section 5) |
| representation lattice | partition lattice $\Pi_{\mu(x)}$, or the congruence lattice of $H_x$ |
| persistence spectrum | index and period of a baseline map, its Koopman spectrum |

The retrieval-depth spectrum is the ladder of $k$-equivalence levels in Moore and Hopcroft minimization, the shortest word separating two inequivalent states [@hopcroft1971]. The representation lattice, read literally as the decodable functions of the past, is the partition lattice $\Pi_{\mu(x)}$ of an $\mu(x)$-element set, a function of the multiplicity alone; read as the features compatible with the dynamics, it is the congruence lattice of $H_x$, recoverable from the second invariant. The persistence spectrum is the cycle and transient structure of one baseline transformation of a finite set, whose Koopman eigenvalues are roots of unity on the cycles and zero off them. @barnett2015 supply the input-output version of the underlying machinery, the epsilon-transducer, which reappears in Section 5.

The proposed Canonicality Theorem, that a behaviour-preserving isomorphism takes $A_x$ and $H_x$ to conjugate copies, is the universal property of the minimal realization, the finality of the final coalgebra of the Moore functor [@rutten2000]. It holds because $A_x$ and $H_x$ are built functorially from behaviour. The three characterization results attached to the proposal are the condition for trivial fibres ($\mu(x) = 1$ for all $x$, meaning the observable is already the behavioural state), the condition for a non-trivial tile action, and the non-commutativity of a transition monoid.

## 4. The autobiographical curvature is ill-posed

The fifth invariant requires a connection whose parallel transport around a closed self-history is the holonomy $T_{\gamma}$, and interprets its curvature $\Omega = dA + A \wedge A$ as an infinitesimal record of order-dependence. No such connection exists in general.

\begin{proposition}
No principal or linear connection has the self-history action as its holonomy, in general. Where a connection exists, its curvature is ordinary curvature and is not determined by the holonomy.
\end{proposition}

`\begin{proof}`{=latex} Parallel transport of any Ehresmann, principal, or linear connection is invertible, with the transport along the reversed path as inverse [@kobayashi1963]. A transformation monoid containing a non-invertible element is therefore not a transport family, and $H_x$ contains non-invertible elements whenever some closed self-history merges two classes of $A_x$, which is the erasure the construction is built to represent. Independently, a fibre bundle over a connected base has homeomorphic fibres, while $\mu(x) = \lvert A_x \rvert$ is allowed to vary with $x$, so $\{A_x\}$ is not a bundle and admits no connection form. When the fibres are constant and every self-history is invertible, so that $H_x$ is a group, a connection exists, and its curvature is that of the connection, which the holonomy fixes only up to the usual holonomy-curvature gap. `\end{proof}`{=latex}

The well-defined residue is a discrete order test: for closed self-histories $a, b$, whether $T_a T_b = T_b T_a$. Non-commutativity of the self-history monoid records that the order of two episodes changes the resulting state, and the second invariant already contains this information. The differential-geometric formulation adds nothing beyond the finite monoid.

The proposal's own example shows the problem. Let the state run over $\{0, +, -\}$ with a memory register in $\mathbb{Z}_3$, a positive excursion acting on the register by $m \mapsto m + 1 \bmod 3$ and a negative excursion by $m \mapsto 0$. As specified, with the register never read out, the three register values are behaviourally identical, since nothing downstream depends on $m$; the fibre over $0$ collapses to a single class, $\mu(0) = 1$, and the entire $\mathbb{Z}_3$ vanishes under $\sim_0$. The three past states survive only once a readout is added, a flag reporting whether $m = 0$. With the readout the object is an ordinary Moore machine whose self-history monoid at $0$ is generated by a three-cycle and a constant map, and the Krohn-Rhodes decomposition of that monoid is a two-state reset extended by $\mathbb{Z}_3$. The stored history becomes visible only through an output channel, and the resulting system is a finite automaton.

## 5. The self-versus-environment defect

The seventh invariant is intended to separate memory a system holds of its own past from memory it holds of its environment. Formalized, it measures observability.

Let the system be driven by inputs from an environment, and fix a self-observable $\pi$. The factorization defect $\Delta_{\mathrm{ext}}(\pi)$ vanishes when the observed self-trajectory determines the future self-behaviour: any two input words producing the same $\pi$-output trajectory leave the system in $\sim$-equivalent states.

\begin{proposition}
$\Delta_{\mathrm{ext}}(\pi) = 0$ if and only if the minimal $\pi$-transducer is observable from its output under unknown inputs, equivalently has zero structural crypticity, equivalently synchronizes to its output.
\end{proposition}

`\begin{proof}`{=latex} $\Delta_{\mathrm{ext}}(\pi) = 0$ says the output history is a sufficient statistic for the future-relevant state: the map from output trajectories to $\sim$-classes is single-valued. Equivalently, the current behavioural state is a function of the past output, which is observability of the transducer from its output when the inputs are not seen, and it is the vanishing of the crypticity of the epsilon-transducer, the residual state information the observed sequence omits [@barnett2015]. A machine whose output history determines its state synchronizes to its output. `\end{proof}`{=latex}

The defect does not measure aboutness. A machine whose internal register holds a copy of the last input has $\Delta_{\mathrm{ext}} = 0$ whenever that input is visible in the output, so a device that only logs its environment scores as maximally self-remembering. The defect counts hidden inputs, and memory of the self and memory of the world register alike. The defect also depends on choices external to the system. $\Delta_{\mathrm{ext}}$ is a function of the observable $\pi$ and the alphabet $U$, both supplied from outside; the same machine returns a positive defect under one observable and zero under a coarser one, so the value describes the partition an analyst has drawn across the system. Directed information and transfer entropy [@massey1990; @schreiber2000] are the stochastic analogues of the same quantity, and they too are conditioned on a chosen partition of the variables into internal and external.

## 6. Discovering the self from the dynamics

Every reduction so far takes $\pi$ as given. The construction gains content if $\pi$ is treated as the unknown: given a bare driven system with no distinguished observable, does it determine a self of its own? A candidate self should be self-predictable, its own observed history fixing its future observable behaviour, and it should be a genuine coarse-graining distinct from the full microstate. Both conditions can be stated without an external partition.

### 6.1 Autobiographical closure

Let $\mathrm{Proj}(Z)$ be the partitions of $Z$ ordered by refinement, $\rho \preceq \sigma$ meaning $\rho$ is finer. A partition $\rho$ is a candidate observable; its induced future equivalence $\sim^{\rho}$ identifies states with equal $\rho$-output on every input word.

\begin{definition}[Autobiographical closure]
A partition $\rho$ is autobiographically closed when, for any two input words from a common start with identical $\rho$-output trajectories, the words leave the system in $\sim^{\rho}$-equivalent states. Write $\mathrm{Cl}(Z)$ for the set of closed partitions.
\end{definition}

Closure is the condition $\Delta_{\mathrm{ext}}(\rho) = 0$ read as a property of $\rho$: the observable predicts its own future from its own past. The discrete partition, where the observable is the whole state, is closed, and so is the one-block partition, where the observable is constant. The questions are which partitions between these two are closed, and whether closed observables combine into a canonical one.

### 6.2 Closure under common refinement

Two observables can be combined in two ways. Their common refinement $\rho \wedge \sigma$ observes both, its blocks the nonempty intersections of a $\rho$-block and a $\sigma$-block. Their coarser union $\rho \vee \sigma$ merges their blocks, its equivalence relation the transitive closure of the union. Common refinement preserves closure.

\begin{proposition}
If $\rho, \sigma \in \mathrm{Cl}(Z)$ then $\rho \wedge \sigma \in \mathrm{Cl}(Z)$.
\end{proposition}

\begin{proof}
Write $\tau = \rho \wedge \sigma$, whose output at a state is the pair $(\rho\text{-output}, \sigma\text{-output})$. Then $\sim^{\tau} = {\sim^{\rho}} \cap {\sim^{\sigma}}$, since equal $\tau$-output on every future word is equal $\rho$-output and equal $\sigma$-output on every future word. Take two input words from a common start with identical $\tau$-output trajectories. Projecting each trajectory to its first and second coordinates gives identical $\rho$-output trajectories and identical $\sigma$-output trajectories. Closure of $\rho$ makes the endpoints $\sim^{\rho}$-equivalent, closure of $\sigma$ makes them $\sim^{\sigma}$-equivalent, so they are $\sim^{\tau}$-equivalent. Hence $\tau$ is closed.
\end{proof}

The computation confirms Proposition 5 without exception: across the 150,964 systems in the sweep, comprising every system with at most four states and a fixed-seed sample at five and six states, the common refinement of two closed observables was closed in every case, with zero violations.

### 6.3 Failure of closure under coarsening

The coarser union of two self-predictable observables is frequently not self-predictable.

The search is exhaustive over all driven systems with at most four states and, for each system, over all partitions, testing every pair of closed partitions for closure of both combinations; five- and six-state systems, and four-state systems with three inputs, are sampled under a fixed seed. Closure under common refinement holds throughout. Closure under coarsening fails in most systems with two inputs, and the failure rate rises with the number of states.

| states | inputs | mode | systems | coarsening fails |
|---:|---:|:---|---:|---:|
| 2 | 2 | exhaustive | 16 | 0 |
| 3 | 2 | exhaustive | 729 | 0 |
| 3 | 3 | exhaustive | 19,683 | 0 |
| 4 | 2 | exhaustive | 65,536 | 54,300 |
| 5 | 2 | sample | 25,000 | 24,443 |
| 4 | 3 | sample | 25,000 | 12,244 |
| 6 | 2 | sample | 15,000 | 14,975 |

At four states and two inputs the closed observables fail to be closed under coarsening in 54,300 of 65,536 systems, $82.9\%$. With the input alphabet held at two, the rate rises to $97.8\%$ at five states and $99.8\%$ at six; with three inputs at four states it is $49.0\%$. Three states are too few for the failure to appear, since the only partitions between the discrete and the one-block partition are single merges, and the coarser union of two distinct single merges is the one-block partition, which is closed.

The smallest failing system has four states and two inputs. State $3$ moves to state $1$ under input $u_0$ and stays at $3$ under $u_1$; states $0$, $1$, $2$ all move to $0$ under either input.

| state $z$ | $F(z, u_0)$ | $F(z, u_1)$ |
|:---:|:---:|:---:|
| 0 | 0 | 0 |
| 1 | 0 | 0 |
| 2 | 0 | 0 |
| 3 | 1 | 3 |

The observable $\rho$ with blocks $\{0\}, \{1, 2\}, \{3\}$ is closed, and so is $\sigma$ with blocks $\{0\}, \{1\}, \{2, 3\}$. Their coarser union has blocks $\{0\}, \{1, 2, 3\}$ and is not closed. Start at state $3$. Input $u_0$ sends it to state $1$ and input $u_1$ keeps it at state $3$; under the union the start and both endpoints lie in the block $\{1, 2, 3\}$, so the two one-letter words produce the same observed trajectory. The endpoints have different futures: a further $u_0$ sends state $1$ to state $0$, in block $\{0\}$, and state $3$ to state $1$, in block $\{1, 2, 3\}$. The two histories are identical under the union and lead to different futures, so the self-prediction that $\rho$ and $\sigma$ each supported is lost when their blocks are merged.

### 6.4 Absence of a canonical coarsest self

$\mathrm{Cl}(Z)$ contains the one-block partition and is closed under common refinement, so it is a Moore family, a closure system on the lattice of partitions. Its closure operator sends any observable to its least closed coarsening, the finest self-predictable observable that coarsens it. This structure is canonical.

The coarsening failure rules out more. Because two closed observables need not have a closed union, there is in general no greatest closed observable below a given resolution and no unique coarsest nontrivial self. The maximal nontrivial self-predictable coarse-grainings form an antichain, and selecting one among them requires a criterion that the closure structure does not provide. A canonical self, defined from the dynamics alone as the coarsest nontrivial observable that predicts itself, does not exist in general.

The closure operator on self-predictable observables is the deterministic form of a known construction. Informational closure, the property that a coarse-graining's future is conditionally independent of the fine detail given its own past, generates the same Moore-family structure and the same closure operator [@bertschinger2008; @pfante2014]. The tractable part of the self-discovery problem is therefore deterministic informational closure, and the part that would have been new, a canonical coarse self, is excluded by the computation.

## 7. Open problem: discovered selves and Markov blankets

One question remains open. A discovered self, however it is selected from the antichain of maximal self-predictable coarse-grainings, can be compared with the partitions that other theories draw for the same purpose: the internal states of a Markov blanket [@friston2013; @kirchhoff2018], the components that an individuality measure assigns to a system as opposed to its environment [@krakauer2020], and the informationally closed coarse-graining. If these always agree, self-history holonomy adds nothing to them. If a finite system exists in which a discovered self and a Markov blanket disagree about which states are internal memory, and in which the self-history monoid on the discovered self's fibres separates systems that the blanket cannot, that disagreement would be the first content specific to the construction. The coincidence of the closure operator with informational closure (Section 6) makes agreement the more likely outcome. The critiques of blanket-based individuation [@biehl2021] identify where to search, since they already exhibit systems in which the blanket partition is non-unique or misleading.

## 8. Limitations

The analysis is deterministic and finite. The stochastic reduction of $\Delta_{\mathrm{ext}}$ to conditioned directed information is stated but not proved at the generality of the deterministic result in Section 5, and the identification of the discovered-self closure operator with informational closure rests on structural correspondence, without an explicit isomorphism of constructions. Both reductions should be completed before the disagreement search of Section 7 is run.

## 9. Conclusion

The autobiographical reading of a driven system, comprising the fibre of past selves, the holonomy of remembered episodes, and the curvature of experience, reduces to the minimal realization, its transition monoid, and the Krohn-Rhodes holonomy of a tile; one invariant is ill-posed and one measures input observability. Fibring a system over its own output and reading return-word holonomy as memory remains a legitimate way to organize what a finite machine records of its history, applied to classical objects. The self enters the construction as a primitive through the observable $\pi$. It is either supplied from outside or, when it must be found from the dynamics alone, lacks a unique coarsest form, because self-predictable observables are closed under common refinement while closure under coarsening fails in $82.9\%$ of four-state two-input systems. The construction describes how a system records its history without identifying a canonical self.

## References
