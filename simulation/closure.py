"""Core routines for autobiographical closure in finite driven systems.

A driven deterministic system is a triple (Z, U, F) with F: Z x U -> Z, and no
distinguished output. A partition rho of Z is a candidate self-observable. Two
input words from a common start that produce the same rho-output trajectory are
rho-indistinguishable to the system's own observation; rho is autobiographically
closed when any two such words land in rho-future-equivalent states, so that the
observed self-history determines the future observable behaviour (Delta_ext = 0).

This module computes, for a given system:
  - future_equiv : the rho-future (Nerode) equivalence, by partition refinement;
  - is_closed    : whether Delta_ext(rho) = 0, by product-automaton reachability;
  - common_refinement / coarser_union : the two ways to combine two observables;
  - analyze_system : which combinations of closed observables stay closed.

No printing, no randomness. Partitions are canonical restricted-growth strings.
"""
from __future__ import annotations

from collections import deque, defaultdict
from typing import Optional

State = int
Word = tuple  # tuple[int, ...] of input letters
Partition = tuple  # tuple[int, ...], block id per state (restricted-growth string)
System = list  # F[z][u] -> next state


# --------------------------------------------------------------------------- #
# partitions of {0, ..., n-1} as canonical restricted-growth strings
# --------------------------------------------------------------------------- #
def all_partitions(n: int) -> list[Partition]:
    res: list[Partition] = []
    a = [0] * n

    def gen(i: int) -> None:
        if i == n:
            res.append(tuple(a))
            return
        top = (max(a[:i]) + 1) if i else 0
        for v in range(top + 1):
            a[i] = v
            gen(i + 1)

    gen(0)
    return res


def canon(labels) -> Partition:
    order: dict = {}
    out = []
    for x in labels:
        if x not in order:
            order[x] = len(order)
        out.append(order[x])
    return tuple(out)


def common_refinement(rho: Partition, sigma: Partition) -> Partition:
    """Blocks are the nonempty intersections of a rho-block and a sigma-block:
    the greatest lower bound (finer than both) in the refinement order."""
    return canon([(rho[z], sigma[z]) for z in range(len(rho))])


def coarser_union(rho: Partition, sigma: Partition) -> Partition:
    """Transitive closure of the union of the two equivalence relations:
    the least upper bound (coarser than both) in the refinement order."""
    n = len(rho)
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x: int, y: int) -> None:
        parent[find(x)] = find(y)

    for grp in (rho, sigma):
        members = defaultdict(list)
        for z in range(n):
            members[grp[z]].append(z)
        for zs in members.values():
            for z in zs[1:]:
                union(zs[0], z)
    return canon([find(z) for z in range(n)])


def is_nontrivial(rho: Partition) -> bool:
    k = len(set(rho))
    return 1 < k < len(rho)


# --------------------------------------------------------------------------- #
# rho-future equivalence and autobiographical closure
# --------------------------------------------------------------------------- #
def future_equiv(nZ: int, nU: int, F: System, rho: Partition) -> list[int]:
    """rho-future (Nerode) equivalence: a ~ b iff rho(Phi_v(a)) = rho(Phi_v(b))
    for every input word v. Returned as canonical class ids per state."""
    cls = list(rho)
    while True:
        order: dict = {}
        new = [0] * nZ
        for z in range(nZ):
            sig = (cls[z], tuple(cls[F[z][u]] for u in range(nU)))
            if sig not in order:
                order[sig] = len(order)
            new[z] = order[sig]
        if new == cls:
            return cls
        cls = new


def is_closed(nZ: int, nU: int, F: System, rho: Partition) -> bool:
    """Delta_ext(rho) = 0: every pair of states reachable from a common start by
    two words with identical rho-output trajectory is rho-future-equivalent."""
    cls = future_equiv(nZ, nU, F, rho)
    visited = {(z, z) for z in range(nZ)}
    frontier = deque(visited)
    while frontier:
        a, b = frontier.popleft()
        for u in range(nU):
            a2 = F[a][u]
            for v in range(nU):
                b2 = F[b][v]
                if rho[a2] == rho[b2] and (a2, b2) not in visited:
                    visited.add((a2, b2))
                    frontier.append((a2, b2))
    return all(cls[a] == cls[b] for a, b in visited)


def closure_witness(nZ: int, nU: int, F: System, rho: Partition) -> Optional[dict]:
    """For a non-closed rho, return an explicit certificate: a common start, two
    input words with identical rho-output trajectory reaching rho-future-
    inequivalent states, and a suffix that separates them. None if rho is closed."""
    cls = future_equiv(nZ, nU, F, rho)
    visited = {(z, z) for z in range(nZ)}
    parent: dict = {}
    frontier = deque(visited)
    bad = None
    while frontier:
        a, b = frontier.popleft()
        if cls[a] != cls[b]:
            bad = (a, b)
            break
        for u in range(nU):
            a2 = F[a][u]
            for v in range(nU):
                b2 = F[b][v]
                if rho[a2] == rho[b2] and (a2, b2) not in visited:
                    visited.add((a2, b2))
                    parent[(a2, b2)] = ((a, b), (u, v))
                    frontier.append((a2, b2))
    if bad is None:
        return None
    # reconstruct the two words back to a diagonal seed
    wu: list[int] = []
    wv: list[int] = []
    cur = bad
    while cur in parent:
        (prev, (u, v)) = parent[cur]
        wu.append(u)
        wv.append(v)
        cur = prev
    wu.reverse()
    wv.reverse()
    start = cur[0]
    return {
        "start": start,
        "word_w": wu,
        "word_w_prime": wv,
        "reached": list(bad),
        "distinguishing_suffix": _distinguishing_suffix(nZ, nU, F, rho, bad[0], bad[1]),
    }


def _distinguishing_suffix(nZ, nU, F, rho, a, b) -> Optional[list[int]]:
    seen = {(a, b)}
    frontier = deque([((a, b), [])])
    while frontier:
        (p, q), word = frontier.popleft()
        if rho[p] != rho[q]:
            return word
        for u in range(nU):
            nxt = (F[p][u], F[q][u])
            if nxt not in seen:
                seen.add(nxt)
                frontier.append((nxt, word + [u]))
    return None


# --------------------------------------------------------------------------- #
# closure of Cl(Z) under the two combinations
# --------------------------------------------------------------------------- #
def analyze_system(nZ: int, nU: int, F: System, parts: list[Partition]):
    """Return (closed_partitions, cr_violation, cu_violation).

    A violation is a triple (rho, sigma, combined) of closed rho, sigma whose
    combination `combined` is not closed, or None if the family is closed under
    that combination. `parts` is all_partitions(nZ), precomputed once per size.
    """
    closed = {p: is_closed(nZ, nU, F, p) for p in parts}
    cl = [p for p in parts if closed[p]]
    cr_violation = None
    cu_violation = None
    for i in range(len(cl)):
        for j in range(i, len(cl)):
            p, q = cl[i], cl[j]
            if cr_violation is None:
                cr = common_refinement(p, q)
                if not closed[cr]:
                    cr_violation = (p, q, cr)
            if cu_violation is None:
                cu = coarser_union(p, q)
                if not closed[cu]:
                    cu_violation = (p, q, cu)
        if cr_violation and cu_violation:
            break
    return cl, cr_violation, cu_violation
