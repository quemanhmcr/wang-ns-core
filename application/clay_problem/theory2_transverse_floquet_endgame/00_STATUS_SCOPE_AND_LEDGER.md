# 00 — Status, scope, and theorem ledger

## 1. Exact claim of this dossier

Theory-2 đã đạt một mức structural closure mạnh:

\[
O_a(u)\ \forall a
\iff
E_u=[\nabla_u,C]
\iff
S(u)
\iff
u,
\]

và Poisson Formation mother

\[
K_u=[C,J_u]
\iff
S(Cu)
\iff
u.
\]

Actual-state vector cocycles đã đủ mạnh để classify zero set:

\[
\Pi_y(u)u=0\ \forall y>0
\Longrightarrow
N(u)=0,
\]

và thêm heat family thì exact NS trajectory là pure heat.

Nhưng **structural completeness không bằng analytic regularity**. Remaining problem là finite-step sign / passivity / recurrence exclusion.

---

## 2. Current strongest exact reductions

### 2.1 Complete state and critical work

\[
\Lambda=|C|=HC,
\qquad
W_\Lambda=2\langle\Lambda u,N(u)\rangle
=\langle u,[\Lambda,J_u]u\rangle
=2\langle Hu,K_uu\rangle.
\]

### 2.2 Constrained-gradient split

\[
N=\gamma G+T,
\]

\[
G=\Lambda(\Lambda-a-bC)u,
\qquad
\gamma=\frac{W_\Lambda}{2d^2},
\]

và

\[
\langle T,u\rangle
=\langle T,Cu\rangle
=\langle T,\Lambda u\rangle=0.
\]

`T` là unique transverse steering component.

### 2.3 Actual-state semigroup Formation cocycles

\[
\Pi_y(u)=P_yJ_u-J_{P_yu}P_y,
\]

\[
\mathcal C_\tau(u)
=e^{-\tau C^2}J_u-J_{e^{-\tau C^2}u}e^{-\tau C^2}.
\]

Finite mixed square uses no new ontology: it is the ordered interleaving of these two existing covariances.

### 2.4 Bounded spectral module passivity

For

\[
Q=1_{[\rho,R\rho]}(\Lambda),
\]

internal projected Formation is skew. Therefore its homogeneous propagator obeys

\[
\boxed{
\|V(t,s)\|_{M\to M}
\le
\sqrt R\,e^{-\nu\rho^2(t-s)}.
}
\]

Arbitrary angular multiplicity and time-dependent internal holonomy inside a fixed finite-ratio spectral module are therefore harmless after a finite viscous horizon.

### 2.5 Finite-viscosity normalized recurrence

On `R^3`, normalize

\[
E=M=1.
\]

Then

\[
\boxed{
v_\theta
=N(v)-\kappa C^2v+\kappa D_2v-\beta\mathcal Lv,
}
\]

\[
\beta=W_\Lambda-2\kappa(D_3-D_2).
\]

Any critically neutral cycle satisfies

\[
\boxed{
\Delta\log r
=2\int\kappa D_2\,d\theta>0.
}
\]

Thus a finite-Reynolds neutral cycle necessarily has positive physical scale exponent.

### 2.6 Complete transverse Floquet reduction

After factoring the commuting nontransverse part,

\[
\boxed{
\frac d{d\theta}
\left[e^{-\Phi(\theta,C)}e^{B(\theta)\mathcal L}v\right]
=e^{-\Phi(\theta,C)}e^{B(\theta)\mathcal L}T.
}
\]

So only `T` survives as an unresolved dynamical source.

### 2.7 Stationary all-depth ray law

For a nondegenerate stationary finite-`κ` profile,

\[
\beta=2\kappa D_2,
\qquad
H_3=0,
\qquad
|b|<1.
\]

At canonical heat depth

\[
\tau_*=\frac1{4D_2},
\]

define

\[
\mathcal V_\sigma(y,\omega)
=\int_0^\infty
\rho^2e^{-\tau_*\rho^2-y\rho}
f_\sigma(\rho,\omega)\,d\rho.
\]

Then for every `y≥0`,

\[
\boxed{
\mathcal N_\sigma(y,\omega)
=-2\kappa D_2y\,\mathcal V_\sigma(y,\omega).
}
\]

In physical-convolution form,

\[
\boxed{
P_\omega\mathsf S_y(\omega)\omega
=-2i\kappa D_2y\,\mathcal V(y,\omega).
}
\]

Thus the old Gaussian-ray cancellation is only the `y=0` member of an entire positive-depth family.

### 2.8 First-order depth equation and exact `T` passivity

Using `N=γG+T`,

\[
\boxed{
\gamma(1-\sigma b)\partial_y\mathcal V_\sigma
+(\gamma a-2\kappa D_2y)\mathcal V_\sigma
=\mathcal T_\sigma.
}
\]

Because `|b|<1`,

\[
\gamma(1-\sigma b)>0
\]

on both helicity sheets.

With the explicit integrating factor

\[
I_\sigma(y)
=\exp\left[
\frac{a}{1-\sigma b}y
-\frac{D_2d^2}{D_3(1-\sigma b)}y^2
\right],
\]

one has the exact forcing-debt identity

\[
\boxed{
\gamma(1-\sigma b)I_\sigma(y_0)\mathcal V_\sigma(y_0)
=-\int_{y_0}^\infty I_\sigma(y)\mathcal T_\sigma(y)\,dy
}
\]

and signed passivity

\[
\boxed{
\int_{y_0}^\infty
I_\sigma^2
\operatorname{Re}\langle\mathcal V_\sigma,\mathcal T_\sigma\rangle\,dy
=-\frac{\gamma(1-\sigma b)}2
I_\sigma(y_0)^2\|\mathcal V_\sigma(y_0)\|_2^2.
}
\]

Hence compact stationary finite-Reynolds strata satisfy a mode-count-independent transverse lower bound

\[
\boxed{\|T\|_{H^{-1/2}}\ge c_{\mathcal K}\kappa.}
\]

### 2.9 Raywise heat-depth radial-spread debt

At `\tau_*=1/(4D_2)`, heat-smoothed Formation is, on every active ray and helicity sheet,

\[
\boxed{\text{energy-inward}}
\qquad\text{and}\qquad
\boxed{\text{critical-neutral}}.
\]

This gives the raywise variance inequality

\[
\boxed{
\sqrt{\mathsf V_{\omega\sigma}}\,
\|F_{\omega\sigma}\|_{L^2(\rho^2d\rho)}
\ge
\kappa D_2M_{\omega\sigma}.
}
\]

On compact stationary finite-Reynolds strata this yields a positive uniform radial-spread gap.

---

## 3. Nonclaims / anti-loop guards

The following moves are forbidden:

- structural completeness `≠` Navier–Stokes regularity;
- operator-pair positivity `≠` actual-state scalar return sign;
- symbol positivity `≠` nonlinear PDE coercivity;
- vector observability `≠` orientation of critical work;
- near-neutral critical balance `≠` small `T`;
- arbitrary Galerkin triads are not trustworthy because physical companion leakage is deleted;
- no infinite scalar moment hierarchy recovers the symmetric complete Formation channel;
- there is no universal dissipation frequency;
- a terminal defect need not contain one positive-mass bubble;
- torus dilation identities must not be used as exact internal identities without passing to a rescaled-domain / `R^3` limit;
- global critical spectral gap for the finite-Reynolds Floquet monodromy is false because of its infrared translation characteristic;
- Laplace injectivity of the all-depth ray family `≠` a global finite-reader critical gap;
- abstract tensor tomography `≠` physical common-state rigidity, because `v\otimes v` cannot be replaced by an arbitrary tensor field.

---

## 4. Current exact/open ledger

### EXACT

1. Theory-2 flag / commutator / strain equivalences.
2. Poisson Formation Hamiltonian structure and complete mother `K_u`.
3. Constrained-gradient decomposition `N=γG+T`.
4. Strict neutral-cell super-viscous creation identity.
5. Mixed-helicity necessity and polarized Curl–Killing.
6. Actual-state Poisson visibility: all-depth zero implies `N=0`.
7. True-heat / Poisson finite covariance formulas and parity.
8. Physical real sum–difference companion leakage.
9. Paired mixed Poisson–heat curvature positivity.
10. Rank-one cross-completion of actual angular cancellation.
11. Bounded spectral module finite-step contraction.
12. Finite-viscosity doubly normalized flow.
13. Positive scale drift for neutral finite-viscosity cells.
14. Nonexistence of `T=0` stationary / periodic finite-Reynolds normalized profiles.
15. Complete transverse Floquet normal form.
16. Critical log-frequency monodromy and infrared characteristic.
17. Stationary regression rigidity: `β=2κD_2`, `H_3=0`, explicit `a,b`, and `|b|<1`.
18. Entire positive-Poisson-depth Gaussian-ray anti-alignment family.
19. Common ray-stress eigenrelation for the physical stress `v\otimes v`.
20. Exclusion of nonzero centered spatially-even stationary finite-`κ` profiles.
21. First-order Poisson-depth equation for `T` on each helicity sheet.
22. `κ`-independent homogeneous depth normal form and canonical depth `y_c`.
23. Exact negative signed transverse depth work identity.
24. Explicit ray-transform `H^{-1/2}` lower bound for `T`.
25. Canonical heat depth is raywise energy-inward and critical-neutral.
26. Every active ray pays a radial-variance debt.
27. Generic leading infrared ancestry is entirely transverse.

### DEDUCTION

1. Compact nonexceptional strata admit finite vector observation gaps.
2. Closed three-shell/high-valence internal recycling is not the terminal obstruction.
3. Persistent finite-Reynolds regeneration requires repeated cross-module / transverse replenishment.
4. Exact compact periodic finite-`κ` recurrence would imply parabolic physical concentration.
5. Compact periodic finite-`κ` recurrence carries a positive transverse-action debt.
6. Compact nondegenerate stationary finite-`κ` strata satisfy `\|T\|_{H^{-1/2}}\gtrsim_{\mathcal K}\kappa`.
7. Compact stationary finite-Reynolds strata have a positive raywise radial-spread gap.

### AUDIT

Arbitrary rotating skew+heat models can show transient critical gain; this demonstrates why NS-specific convolution / rank-one / Curl–Killing restrictions are essential. Such models are not NS conclusions.

The all-depth Laplace transform family is injective but not globally coercive on the entire critical space; radial phase/scale radiation can make finite reader families small.

### OPEN

Two closely related final analytic theorems remain:

1. **Stationary common-ray Formation rigidity:** classify common-state solutions of the all-positive-depth ray-stress eigenrelation under reality, rank-one companion completion, polarized Curl–Killing, `d>0`, `|b|<1`, and normalized moment constraints.
2. **Periodic transverse Floquet rigidity:** exclude a time-ordered self-consistent transverse source solving the weighted-shift recurrence on a compact finite-Reynolds recurrent component.

---

## 5. Current final statement

For the stationary branch, the remaining question is now

\[
\boxed{
\begin{aligned}
&\text{Can one actual state }v\text{ satisfy the common quadratic ray-stress}\
&\text{eigenrelation at every positive Poisson depth while its transverse}\
&\text{component obeys the exact coercive depth ODE on both helicity sheets,}\
&\text{without collapsing into null/collinear/thin-shell geometry or losing}\
&\text{compactness through radial/phase radiation?}
\end{aligned}
}
\]

The decisive unresolved structure is no longer arbitrary mode count or arbitrary tensor tomography. It is

\[
\boxed{
\text{rank-one/common-state self-consistency of }\mathsf R=v\otimes v.
}
\]

For periodic recurrence the corresponding unresolved object is the propagated transverse source in the exact Floquet weighted shift.

**Status: OPEN.**
