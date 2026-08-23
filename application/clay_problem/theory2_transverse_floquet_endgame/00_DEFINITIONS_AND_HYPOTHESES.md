# 00 — Definitions and hypotheses

## 0. Scope

This dossier treats only the **normalized stationary finite-viscosity branch** of Theory-2 on finite-energy divergence-free fields. It does not claim Navier–Stokes global regularity and does not close the Euler or periodic/Floquet branches.

Every statement is labelled as one of:

- **EXACT** — follows from the displayed Theory-2 identities;
- **DEDUCTION** — exact identities plus the explicit compactness/nondegeneracy hypotheses below;
- **NO-GO** — proves that a proposed implication does not follow from the present hypotheses;
- **OPEN** — additional physical structure not yet derived from the Theory-2 axioms.

---

## 1. Basic Theory-2 objects

Let

\[
C=\operatorname{curl},\qquad \Lambda=|C|,\qquad H=\operatorname{sgn}C,
\]

and let \(P\) be the Leray projector. Define

\[
J_u b=P(b\times Cu),\qquad N(u)=J_u u.
\]

Then

\[
J_u^*=-J_u,\qquad J_u(Cu)=0.
\]

The Poisson mother is

\[
K_u=[C,J_u],\qquad K_u b=-2P(S(Cu)b),\qquad K_u^*=K_u,
\]

and

\[
CN(u)=K_u u.
\]

The polarized Curl–Killing identity is

\[
J_a(Cb)+J_b(Ca)=0.
\]

For helical atoms \(Ca=xa\), \(Cb=yb\),

\[
\boxed{2B(a_x,b_y)=(x-y)P(b_y\times a_x).}
\]

---

## 2. Critical stocks and constrained-gradient split

Set

\[
M=\langle u,\Lambda u\rangle,\qquad
D_2=\|\Lambda u\|_2^2,\qquad
D_3=\|\Lambda^{3/2}u\|_2^2,
\]

and

\[
W=2\langle \Lambda u,N(u)\rangle.
\]

Choose \(a,b\in\mathbb R\) so that

\[
G=\Lambda(\Lambda-a-bC)u
\]

satisfies

\[
\langle u,G\rangle=\langle Cu,G\rangle=0.
\]

Define

\[
d^2:=\|G\|_{H^{-1/2}}^2.
\]

For \(d>0\), set

\[
\gamma=\frac{W}{2d^2}.
\]

Then define \(T\) by the exact orthogonal decomposition

\[
\boxed{N=\gamma G+T,}
\]

with

\[
\langle T,u\rangle=\langle T,Cu\rangle=\langle T,\Lambda u\rangle=0.
\]

---

## 3. Normalized stationary finite-\(\kappa\) class

We work on a class \(K\) of nonzero normalized states \(v\) satisfying

\[
E(v)=\|v\|_2^2=1,\qquad M(v)=\langle v,\Lambda v\rangle=1,
\]

with

\[
0<\kappa_0\le \kappa(v)\le \kappa_1<\infty.
\]

For stationary normalized candidates,

\[
W=2\kappa D_3,
\]

and the normalized stationary equation is encoded by the finite-viscosity vector

\[
Y:=\Lambda^2v-D_2v+2D_2\mathcal Lv,
\]

where in Fourier variables

\[
\widehat{\mathcal L f}=-(3/2+\xi\cdot\nabla_\xi)\hat f.
\]

Write

\[
r:=\frac{D_3}{d^2},\qquad
R_{\rm fv}:=Y-rG.
\]

The stationary transverse saturation equation is

\[
\boxed{T=\kappa R_{\rm fv}.}
\]

---

## 4. Quantitative nondegeneracy hypotheses

Whenever compactness is invoked, assume explicitly:

\[
\frac{d^2}{D_3}\ge \delta_0>0,
\]

and bounded normalized coefficients on \(K\). On each helicity sheet \(\sigma=\pm1\), write

\[
\widehat{R_{\rm fv}}_\sigma
=
-2D_2\rho\partial_\rho f_\sigma
+
\Big([1-r(1-\sigma b)]\rho^2+ra\rho-4D_2\Big)f_\sigma.
\]

Define

\[
\chi_\sigma:=r(1-\sigma b)-1.
\]

On the nonexceptional stationary class we assume the established lower bound

\[
\chi_\sigma\ge \chi_K>0.
\]

---

## 5. Rank-one incidence data

For a finite physical incidence family, the actual-state quadratic coefficients factor as

\[
\boxed{Z_{ij}=A_iB_j.}
\]

A physical companion forcing is written schematically as

\[
F_e=Z_e\Phi_e,
\]

where \(\Phi_e\) contains the Curl-root difference, Leray projection, polarization, helicity branch and output geometry.

Reality completion is retained throughout. Arbitrary isolated Galerkin triads are not admissible substitutes for a physical incidence network.

---

## 6. Compactness hypothesis

Whenever a uniform constant is deduced, \(K\) is assumed compact in a topology strong enough that

\[
v\mapsto T(v),\quad v\mapsto R_{\rm fv}(v),\quad v\mapsto \kappa(v)
\]

are continuous into \(H^{-1/2}\) (and that any finite witness holonomy used later is continuous on its domain).

Compactness is used only **after** a pointwise exact theorem has been proved. It is never used to manufacture finite-dimensionality, finite Fourier support, or exact recurrence.

---

## 7. Explicit non-hypotheses

The following are **not** assumed:

1. finite Fourier or triad complexity;
2. finite-reader injectivity on the natural packet space;
3. a nontrivial holonomy produced by rank one plus radial absorption;
4. projective channel closure;
5. finite-witness extraction from an infinite state;
6. a uniform angle gap;
7. Navier–Stokes regularity.

Items 4–5 are the present OPEN physical frontier and are stated only in `04_OPEN_FRONTIER.md` and the conditional closure theorem.