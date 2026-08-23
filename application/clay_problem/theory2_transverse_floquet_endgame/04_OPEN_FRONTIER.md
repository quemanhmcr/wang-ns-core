# 04 — Open physical frontier

This file contains the only statements not yet derived from the current Theory-2 axioms.

The stationary analytic reduction is complete up to the exact exclusion

\[
T(v)=\kappa(v)R_{\rm fv}(v).
\]

The remaining problem is finite physical state-incidence closure.

---

## OPEN A — Channel-Resolved Projective Closure (CRPC)

Let a physical interaction edge be

\[
e=(p,q\to r).
\]

For a chosen finite witness network, attach one-dimensional complex input lines

\[
L_p=\mathbb C\psi_p,
\qquad
L_q=\mathbb C\psi_q,
\]

and an **edge-resolved output channel line**

\[
L_{r,e}.
\]

Let \(B_e\) be the physical Curl–Killing bilinear interaction for that edge, and let \(\mathcal S_{r,e}\) be the canonical finite-energy radial absorber on its output ray.

The required theorem is:

\[
\boxed{
\mathcal S_{r,e}B_e(L_p,L_q)
\subseteq L_{r,e}
}
\]

nontrivially, together with a specified projective identification

\[
\boxed{
\iota_e:L_{r,e}\longrightarrow L_r
}
\]

where \(L_r\) is the state line used as input by the next incidence of the witness.

The channel must be followed **before** summation with other incoming interactions at \(r\).

### Why CRPC is necessary

Without channel resolution, the physical amplitude at \(r\) obeys

\[
a_r=\sum_{e:r_e=r}h_ea_{p_e}a_{q_e},
\]

so ordinary edgewise multiplicative transport is destroyed by additive mixing.

CRPC is therefore a theorem about persistence of identifiable physical ancestry, not merely about one-dimensionality of the total occupied mode.

---

## Conditional definition — projective edge gain

If CRPC holds, choose representatives \(\psi_v\in L_v\setminus\{0\}\). For each witness edge there is a unique nonzero scalar \(h_e\) such that

\[
\boxed{
\iota_e\mathcal S_{r,e}B_e(\psi_p,\psi_q)
=h_e\psi_r.
}
\]

Under gauge changes

\[
\psi_v\mapsto g_v\psi_v,
\qquad g_v\in\mathbb C^\times,
\]

one has

\[
\boxed{h_e\mapsto g_pg_qg_r^{-1}h_e.}
\]

Thus CRPC would induce a multiplicative connection on the quadratic incidence hypergraph.

---

## Conditional definition — finite incidence holonomy

Associate to each edge

\[
\partial e=[p]+[q]-[r].
\]

For finitely supported integer coefficients \(n=(n_e)\) satisfying

\[
\boxed{
\sum_en_e\partial e=0,
}
\]

define

\[
\boxed{
\operatorname{Hol}_n:=\prod_eh_e^{n_e}.
}
\]

The gauge factors cancel by the incidence-cycle condition, so this is a genuine gauge-invariant finite holonomy **provided CRPC has first been proved**.

---

## OPEN B — Exact channel-amplitude consistency

For a channel-resolved witness loop, one must prove that the actual inherited channel amplitudes satisfy the multiplicative transport law

\[
\boxed{
a_r=h_ea_pa_q}
\]

along the selected ancestry channel before it is mixed with the other incoming channels.

Under this law, every incidence cycle satisfies

\[
\boxed{\operatorname{Hol}_n=1.}
\]

### Proof of the conditional implication

From

\[
h_e=\frac{a_r}{a_pa_q},
\]

multiplying with exponents \(n_e\) gives cancellation of every vertex amplitude because

\[
\sum_en_e([p_e]+[q_e]-[r_e])=0.
\]

Hence \(\operatorname{Hol}_n=1\). ∎

The OPEN content is not this algebra; it is deriving the edgewise channel-amplitude law from the actual PDE ancestry.

---

## OPEN C — Pointwise finite physical nonflatness

Let

\[
P_{\rm stat}:=\{v\in K:T(v)=\kappa(v)R_{\rm fv}(v)\}
\]

be the forbidden stationary saturation set.

The required witness theorem is:

\[
\boxed{
\forall v\in P_{\rm stat},
\quad
\exists\text{ a finite reality-complete, nonexceptional, channel-resolved cycle }\Gamma_v
\quad
\text{with}
\quad
|\operatorname{Hol}_{\Gamma_v}(v)-1|>0.
}
\]

The witness need only be finite **pointwise**. No uniform a priori loop length is required.

If the witness remains defined and its defect is continuous on a neighborhood of \(v\), compactness later supplies a finite family of witnesses and a uniform positive constant.

---

## Equivalent OPEN formulation — Finite Witness Extraction (FWE)

Instead of constructing holonomy explicitly, it is sufficient to prove:

> If a normalized PDE state satisfies the forbidden saturation condition, then it contains a finite reality-complete, nonexceptional, channel-resolved subnetwork whose inherited state data satisfy the same exact saturation compatibility.

Symbolically,

\[
\boxed{
T=\kappa R_{\rm fv}
\Longrightarrow
\text{finite exact saturation witness}.
}
\]

Combined with the established finite-network rigidity theorem, FWE would immediately exclude the global saturated state.

CRPC + pointwise nonflatness and FWE are two formulations of the same missing bridge: **an exact finite physical witness must be extractable from the infinite PDE state without using a Fourier cutoff or deleting companions**.

---

## What is not enough

None of the following proves CRPC/FWE:

\[
2B(a_x,b_y)=(x-y)P(b_y\times a_x),
\]

rank-one factorization,

\[
\chi_\sigma>0,
\]

radial coercivity, finite Poisson/heat depths, ordinary compactness, or finite-network rigidity by itself.

An infinite ancestry may remain open at every finite stage. Approximate recurrence is not exact algebraic completion.

---

## Minimal unresolved theorem package

The physical endgame is therefore exactly:

\[
\boxed{
\text{CRPC / exact channel inheritance}
+
\text{pointwise finite nonflat witness (or FWE)}.
}
\]

Everything after these statements is a finite compactness argument and is proved in `05_CONDITIONAL_CLOSURE.md`.

**Status: OPEN.**