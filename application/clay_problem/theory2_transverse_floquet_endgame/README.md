# Theory-2 Transverse Floquet Endgame

## Purpose

This dossier records the current theorem-first proof chain of Theory-2 / NEO Navier–Stokes, with explicit separation between **EXACT**, **DEDUCTION**, **AUDIT**, and **OPEN** statements.

The stationary finite-`κ` frontier has moved through several reductions:

1. complete Theory-2 state and constrained-gradient split `N=γG+T`;
2. transverse Floquet / stationary `T`-only reduction;
3. all-positive-depth stationary `T` coercivity;
4. exact stationary saturation `T=κR_{\rm fv}`;
5. finite completed-network rigidity;
6. audits showing that continuum companion mass / occupation packing is not enough;
7. current pivot to a **finite multiplicative companion-loop holonomy obstruction**.

> **No claim of 3D Navier–Stokes global regularity or Clay-problem resolution is made.**
>
> The current finite-holonomy theorem is OPEN.

---

## Governing doctrine

> Keep the complete Theory-2 state until a genuinely coercive terminal estimate is proved.

Do not:

- replace physical companion completion by arbitrary Galerkin triads;
- treat continuum Laplace invertibility as a coercive theorem;
- equate raw rank-one interaction mass with occupied state mass;
- assume ordinary state compactness controls normalized microscopic descendants;
- or hide the stationary PDE inside a “finite” theorem whose proof first reconstructs the full raywise equation.

---

## Ledger convention

- **EXACT** — direct algebraic / Fourier / spectral identity.
- **DEDUCTION** — exact identities plus stated analytic hypotheses.
- **AUDIT** — hostile model or mechanism testing an inference; not an NS counterexample unless explicitly proved as one.
- **OPEN** — analytic arrow not proved.

---

## File map

1. `00_STATUS_SCOPE_AND_LEDGER.md` — current status, exact/open ledger, final frontier.
2. `01_CORE_THEORY2_STATE.md` — Curl flag, commutator state, Poisson Formation mother.
3. `02_CRITICAL_GEOMETRY_AND_CONSTRAINED_GRADIENT.md` — critical stocks, `G`, `γ`, `T`, helicity sheets.
4. `03_FLAGS_COCYCLES_AND_ACTUAL_STATE_VISIBILITY.md` — Poisson/heat cocycles and actual-state visibility.
5. `04_COMPANIONS_TRIADS_AND_MIXED_CURVATURE.md` — Curl–Killing, reality companions, reverse-pair curvature.
6. `05_ANGULAR_CANCELLATION_RANK_ONE_AND_MODULE_COERCIVITY.md` — angular cancellation, rank-one completion, bounded-module coercivity.
7. `06_TERMINAL_SCALING_AND_RENORMALIZED_BRANCHES.md` — terminal scaling and normalized finite-viscosity/Euler branches.
8. `07_TRANSVERSE_FLOQUET_NORMAL_FORM.md` — exact transverse Floquet reduction.
9. `08_NO_GO_COUNTERMECHANISMS_AND_OPEN_THEOREMS.md` — no-go mechanisms and hostile audits.
10. `09_CHRONOLOGICAL_THEOREM_CHAIN.md` — chronological theorem chain.
11. `10_COMMON_RAY_POISSON_DEPTH_AND_T_COERCIVITY.md` — all-depth stationary ray laws and `T` coercivity.
12. `11_TRANSVERSE_SATURATION_AND_COMPANION_NONCONCENTRATION.md` — exact saturation core plus explicit record of additive routes now superseded.
13. `12_PROOF_ARCHITECTURE_LESSONS.md` — anti-repacking and proof-engineering doctrine.
14. `13_ABSORPTION_RESET_AND_FINITE_COMPANION_HOLONOMY.md` — current stationary frontier: absorption reset and finite loop holonomy.

---

## Current strongest stationary exact reduction

Define

\[
Y_v=\Lambda^2v-D_2v+2D_2\mathcal Lv,
\qquad
R_{\rm fv}=Y_v-\frac{D_3}{d^2}G_v.
\]

On the stationary scalar stratum,

\[
W=2\kappa D_3,
\qquad
\gamma=\kappa\frac{D_3}{d^2},
\]

and

\[
\boxed{T(v)=\kappa R_{\rm fv}(v).}
\]

The full residual identity is

\[
\boxed{
\|N-\kappa Y\|_{H^{-1/2}}^2
=
\|T-\kappa R_{\rm fv}\|_{H^{-1/2}}^2
+
\frac{(W/2-\kappa D_3)^2}{d^2}.
}
\]

Thus once exact saturation is excluded on a compact graph-topology class, the quantitative saturation gap follows by continuity.

The hard problem is exact exclusion.

---

## New exact finite-viscosity structure

For helicity sheet `σ=±1`, put `r=D_3/d^2`. The stationary transverse field is

\[
\widehat{R_{\rm fv}}_\sigma
=
-2D_2\rho\partial_\rho f_\sigma
+
\left(
[1-r(1-\sigma b)]\rho^2+ra\rho-4D_2
\right)f_\sigma.
\]

The regression identities and `H_3=0` imply for nonzero stationary states

\[
|Q|<D_2,
\qquad
r(1-\sigma b)>1
\]

on both sheets. Hence

\[
\boxed{
R_{{\rm fv},\sigma}
=
-2D_2\rho\partial_\rho
-\chi_\sigma\rho^2+O(\rho),
\qquad
\chi_\sigma>0.
}
\]

The frozen radial operator is therefore high-frequency stable and admits finite-energy solutions for arbitrary smooth compact-annulus forcing.

This kills the hoped-for universal one-edge theorem

\[
\text{“a physical companion output has the wrong local shape/gain for }R_{\rm fv}\text{.”}
\]

Local absorption is flexible; only same-state multi-edge self-consistency can still obstruct saturation.

---

## Why the additive companion-mass programme is no longer the final route

Rank-one cancellation still gives the exact raw-mass propagation

\[
\sum_{i\ne j}|A_iB_j|^2
\ge
\sum_i|A_iB_i|^2.
\]

But this only propagates mass while cancellation stays nonlinear.

Once a companion output is absorbed into

\[
\kappa R_{\rm fv},
\]

rank-one completion is no longer forced at comparable amplitude.

The finite-viscosity scaling permits schematically

\[
\boxed{
a_{n+1}
\lesssim
\frac{a_n^2}{\kappa\rho_n}.}
\]

Thus an infinite outward ancestry can decay superlinearly while keeping

\[
\sum_n\rho_n^3a_n^2<\infty.
\]

Consequences:

- perfect one-generation companion-output coercivity would still not suffice;
- interaction-to-occupation alone would still not suffice;
- bounded occupation packing alone would still not suffice;
- reproduction with factor `<1` would still not suffice;
- finite readers cannot repair this amplitude reset.

This is the **quadratic-to-linear absorption reset**.

---

## Current final frontier — finite companion holonomy

Actual-state rank one is multiplicative:

\[
\boxed{Z_{ii}Z_{jj}=Z_{ij}Z_{ji}.}
\]

The current proposal is to attach to a bounded-depth completed physical loop `Γ` a projective gain/phase quantity

\[
\boxed{
\mathfrak G(\Gamma)
=
\prod_{e\in\Gamma}
\frac{\text{nonlinear companion transfer on }e}
{\text{finite-viscosity radial transfer on }e}.
}
\]

Exact saturation around a closed loop should require unit consistency,

\[
\mathfrak G(\Gamma)=1,
\]

including phase.

The desired finite theorem is

\[
\boxed{
\textbf{Finite Companion Loop Defect:}
\qquad
|\mathfrak G(\Gamma)-1|
\ge c_{\mathcal K}>0
}
\]

for some bounded-depth reality-complete loop forced by every nonexceptional hidden cancellation.

A successful proof should combine:

- rank-one multiplicative completion;
- reality / reverse pairs;
- Curl–Killing and helicity polarization;
- finite-viscosity radial transfers;
- and possibly the already established mixed Poisson–heat reverse-pair curvature.

This target is attractive because it is finite and amplitude-independent: it can survive descendant amplitudes tending to zero.

**Status: OPEN.**

---

## Anti-repacking test

The holonomy route counts as genuine reduction only if the defect is proved before reconstructing the full stationary ray equation.

A successful theorem must involve finitely many physical incidences and finitely many transfer factors with a mode-count-independent projective defect.

The following do not count as closure:

- global inversion of `T=κR_{\rm fv}` over all rays;
- full positive-depth Laplace inversion;
- an infinite scalar moment hierarchy;
- a finite-support theorem with constants degenerating with complexity;
- or a hereditary compactness hypothesis effectively equivalent to saturation exclusion.

---

## Parallel periodic/Floquet frontier

The periodic finite-`κ` recurrent branch remains separately OPEN through the exact transverse Floquet source equation. The stationary holonomy pivot may eventually suggest a cycle/monodromy analogue, but no such theorem is currently established.

---

## Nonclaim

Theory-2 has not proved 3D Navier–Stokes global regularity. The current stationary finite-`κ` obstruction has been sharpened to a finite multiplicative loop/holonomy problem, but the required loop defect theorem is unproved.
