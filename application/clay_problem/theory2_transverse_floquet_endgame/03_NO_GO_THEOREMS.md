# 03 — Rigorous no-go theorems and limits

This file records only obstructions that rule out specific proof inferences. It contains no speculative narrative.

---

## No-Go 1 — Operator/vector positivity does not give the critical sign

Actual Formation vectors are even under `u↦-u`, while

\[
W(-u)=-W(u).
\]

Hence no scalar built only from even actual-state vector norms/pairings can determine the sign of `W`.

**Consequence.** Vector observability is not a passivity theorem.

---

## No-Go 2 — Finite physical output maps are not uniformly bounded below on an unrestricted continuum incidence fiber

Fix a compact nonexceptional same-output incidence chart `U`, one smooth nonvanishing rank-one factor `B`, and finitely many physical companion branches. After local coordinates, each branch has the form

\[
(\mathcal C_\ell A)(d)
=\int_U K_\ell(d,s)A(s)B(\Phi_\ell(d,s))\,ds,
\]

with square-integrable kernel on the compact chart. Therefore

\[
\boxed{\mathcal C_\ell:L^2(U)\to L^2(D_\ell)\text{ is Hilbert--Schmidt, hence compact}.}
\]

Any finite direct sum, including finitely many Poisson/heat weights, remains compact.

Same-output cancellation imposes finitely many bounded linear constraints, so the hidden-cancellation subspace is infinite-dimensional. Choose an orthonormal sequence `A_n` there. Then

\[
A_n\rightharpoonup0,
\qquad
\mathcal C A_n\to0,
\]

while the normalized raw product `A_nB` stays nonzero.

Thus no estimate

\[
\boxed{
\|\mathcal Ch\|\ge c\|h\|
}
\]

holds on the unrestricted continuum hidden sphere for any finite family of immediate output readers.

---

## No-Go 3 — Finite Poisson/heat depths are not injective on the natural radial transfer class

Let `I` be a fixed nonexceptional annulus and

\[
X=C_c^\infty(I).
\]

Any finite family of Poisson/heat readers, even enlarged by finitely many readers of `\mathscr Rg`, defines a finite-rank map

\[
L:X\to\mathbb C^N.
\]

Since `X` is infinite-dimensional,

\[
\boxed{\ker L\ne\{0\}.}
\]

Choose `0\ne g\in\ker L` and set

\[
F_g=\kappa\mathscr R_\sigma g.
\]

Then `g` is an exactly absorbable packet and every chosen finite reader vanishes on it.

Therefore

\[
\boxed{
\text{finite semigroup depths do not exactly identify arbitrary radial absorbers.}
}
\]

The Vandermonde determinant only proves that `m+1` distinct depths separate an `m`-jet once finite-jet determinacy has already been assumed.

---

## No-Go 4 — Ordinary compactness does not imply hereditary descendant compactness

A compact state family may contain

\[
v_n=v_0+\varepsilon_nw_n,
\qquad
\varepsilon_n\to0,
\]

with `w_n` orthonormal. Then `v_n→v_0` strongly, but the normalized microscopic descendants `w_n` have no compact subsequence.

Hence

\[
\boxed{
\text{compactness of whole states}
\not\Rightarrow
\text{compactness of normalized companion descendants}.}
\]

Any hereditary/projective compactness condition must be stated as an additional hypothesis or proved from the PDE.

---

## No-Go 5 — Packing/occupation alone does not prevent infinite extinction

Let hidden ancestry mass obey

\[
m_{n+1}=qm_n,
\qquad
0<q<1,
\]

and let the absorbed occupation be

\[
o_n=(1-q)m_n.
\]

Then

\[
m_n=q^nm_0\to0,
\qquad
\sum_no_n=m_0<\infty.
\]

Therefore

\[
\boxed{
\text{finite total occupation}\not\Rightarrow\text{non-extinction of ancestry}.}
\]

A finite-tree packing estimate cannot by itself produce a depth-independent saturation contradiction.

---

## No-Go 6 — Quadratic export followed by linear viscous absorption permits subcritical reset

On a high-frequency annulus, Theorem S7 gives schematically

\[
\|f\|_{H^{-1/2}}
\lesssim_K
\frac1{\kappa\rho^2}
\|F\|_{H^{-1/2}}.
\]

Formation is quadratic. For comparable packets of amplitude `a_n` at scale `ρ_n`, a schematic companion force is

\[
F_n\sim \rho_na_n^2.
\]

For bounded shell ratio this is compatible with

\[
\boxed{
a_{n+1}\lesssim_K\frac{a_n^2}{\kappa\rho_n}.}
\]

Once `a_n` is small, the regenerated nonlinear ancestry may decay superlinearly while

\[
\sum_n\rho_n^3a_n^2<\infty.
\]

This is an **AUDIT consistency mechanism**, not a stationary NS construction.

**Consequence.** Additive mass propagation is structurally insufficient as the final mechanism.

---

## No-Go 7 — Local shape/gain mismatch against `R_fv` is false

By Theorem S7, every smooth annular forcing `F` has a unique finite-energy absorber

\[
f=\mathcal S_\sigma F.
\]

Hence no universal local theorem of the form

\[
\text{“a physical companion output is outside the range/direction/gain of }R_{\rm fv}\text{”}
\]

can follow from frozen radial geometry alone.

The obstruction, if any, must use **same-state self-consistency across incidences**, not one-edge radial solvability.

---

## No-Go 8 — The present axioms do not force a nontrivial radial holonomy

Rank-one algebra acts on incidence coefficients `Z_{ij}`. Radial absorption acts independently on occupied output packets `f_e`:

\[
F_e=\kappa\mathscr R_{\sigma_e}f_e,
\qquad
f_e=\mathcal S_{\sigma_e}F_e.
\]

No established identity identifies an absorbed `f_e` with an `A`- or `B`-factor of a subsequent incidence.

Therefore the only currently forced finite multiplicative invariant is

\[
\boxed{\operatorname{Hol}^Z_\Gamma=1,}
\]

which is the tautological rank-one cycle identity of Theorem S9.

Any nontrivial `R_fv`-dependent holonomy requires an additional state-incidence closure law.

---

## No-Go 9 — Finite completed-network rigidity does not automatically pass to the continuum

Finite completed nonexceptional networks can force companion export, but continuum incidence spacing may collapse and finite output maps are compact in the dangerous fiber variable. Therefore a finite-mode/nonexceptional theorem with a constant depending on mode separation does not imply a mode-count-independent PDE constant.

---

## No-Go 10 — Exact exclusion plus compactness does not automatically give an angle gap if `T` may vanish

It is possible on a compact parameter set that `T(v)` is never a positive multiple of `R(v)` for `T\ne0`, yet

\[
\angle(T(v),R(v))\to0
\]

as `T(v)→0`.

Thus a uniform angle formulation requires nonvanishing of both vectors.

However, if `R_{\rm fv}\ne0` and exact stationary equality is excluded,

\[
T(v)\ne\kappa R_{\rm fv}(v),
\]

then the normalized defect

\[
\Psi(v)
=
\frac{\|T-\kappa R_{\rm fv}\|}
{\|T\|+\kappa\|R_{\rm fv}\|}
\]

is continuous and strictly positive on a compact class. Hence

\[
\boxed{
\min_K\Psi>0.
}
\]

So the **saturation-ratio gap**, not the angle gap, is the minimal quantitative target.

---

# Formal conclusion of the no-go ledger

The following routes are closed as final mechanisms under the current axioms:

\[
\boxed{
\begin{aligned}
&\text{finite output/frame coercivity alone},\\
&\text{finite semigroup reconstruction alone},\\
&\text{occupation packing/non-extinction by mass counting},\\
&\text{one-edge local gain/shape mismatch},\\
&\text{nontrivial holonomy without a state-incidence connection}.
\end{aligned}}
\]

The exact next missing theorem is stated in `04_OPEN_FRONTIER.md`.