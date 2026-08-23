# Theory-2 Transverse Floquet Endgame — Formal Proof Dossier

## Status

\[
\boxed{\mathbf{THRESHOLD\;NOT\;CROSSED}.}
\]

This directory is a compact theorem-first record of the current Theory-2 / NEO Navier–Stokes proof chain.

It contains only:

1. definitions and hypotheses;
2. proved identities/theorems with short proofs;
3. rigorous no-go limits;
4. the exact next open theorem.

Historical narrative, superseded proof routes, and duplicated chapter-by-chapter development have been removed from `main`; they remain recoverable from Git history.

No file in this directory claims 3D Navier–Stokes global regularity.

---

## Files

- [`00_DEFINITIONS_AND_HYPOTHESES.md`](00_DEFINITIONS_AND_HYPOTHESES.md)  
  Ambient classes, Theory-2 objects, normalization, compactness hypotheses, forbidden implicit assumptions.

- [`01_EXACT_THEOREMS_AND_PROOFS.md`](01_EXACT_THEOREMS_AND_PROOFS.md)  
  Complete Curl/Formation state, constrained-gradient split, critical debt, cocycle visibility, physical companions, rank-one completion, bounded-module passivity, exact transverse Floquet reduction.

- [`02_STATIONARY_FINITE_VISCOSITY.md`](02_STATIONARY_FINITE_VISCOSITY.md)  
  Stationary identities, regression algebra, exact saturation `T=κR_fv`, ray formula, trivial kernel, high-frequency radial stability, canonical finite-energy radial inverse, direct-product absorption lemma, tautological rank-one holonomy.

- [`03_NO_GO_THEOREMS.md`](03_NO_GO_THEOREMS.md)  
  Rigorous obstructions: finite output/frame coercivity, finite reader injectivity, ordinary compactness, additive packing/non-extinction, quadratic-to-linear absorption reset, local range/gain mismatch, and nontrivial holonomy without state-incidence closure.

- [`04_OPEN_FRONTIER.md`](04_OPEN_FRONTIER.md)  
  The exact missing theorem: **Projective State–Incidence Closure (PSC)**; conditional genuine holonomy; finite witness theorem; conditional saturation exclusion and compact quantitative gap.

---

## Dependency chain

The proved chain is

\[
\boxed{
\begin{aligned}
&\text{complete Theory-2 state}
\Longrightarrow
N=\gamma G+T\\
&\Longrightarrow
\text{normalized finite-viscosity equation}\\
&\Longrightarrow
\text{stationary }N=\kappa Y\\
&\Longrightarrow
\boxed{T=\kappa R_{\rm fv}}\\
&\Longrightarrow
\text{canonical edgewise radial absorption}.
\end{aligned}}
\]

What is **not** proved is the next arrow

\[
\boxed{
\text{absorbed output packet}
\Longrightarrow
\text{subsequent incidence projective variable}.
}
\]

That arrow is the current frontier `(PSC)`.

Without it, the only exact finite holonomy is the tautological rank-one identity

\[
\operatorname{Hol}^{Z}_\Gamma=1,
\]

which carries no radial information and cannot yield a positive saturation defect.

---

## Minimal success criterion

A genuine next advance must prove from the actual Navier–Stokes/Curl–Killing geometry a gauge-covariant closure law

\[
\boxed{
\mathcal S_{\sigma_\gamma}B(\psi_\alpha,\psi_\beta)
=h_e\psi_\gamma,
}
\]

with the output line `L_γ=\mathbb C\psi_γ` belonging to the same actual state.

Only after that is a nontrivial physical holonomy well-defined.

If a finite witness theorem then excludes holonomy one on every nonexceptional positive-alignment candidate, exact stationary saturation is impossible; compactness would then give

\[
\boxed{
\|T-\kappa R_{\rm fv}\|_{H^{-1/2}}
\ge
\eta_K
\big(
\|T\|_{H^{-1/2}}+
\kappa\|R_{\rm fv}\|_{H^{-1/2}}
\big).
}
\]

That implication remains conditional because `(PSC)` and the finite witness theorem are OPEN.