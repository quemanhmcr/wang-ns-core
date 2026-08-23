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

internal projected Formation is skew.  Therefore its homogeneous propagator obeys

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
- global critical spectral gap for the finite-Reynolds Floquet monodromy is false because of its infrared translation characteristic.

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

### DEDUCTION

1. Compact nonexceptional strata admit finite vector observation gaps.
2. Closed three-shell/high-valence internal recycling is not the terminal obstruction.
3. Persistent finite-Reynolds regeneration requires repeated cross-module / transverse replenishment.
4. Exact compact periodic finite-`κ` recurrence would imply parabolic physical concentration.
5. Compact periodic finite-`κ` recurrence carries a positive transverse-action debt.

### AUDIT

Arbitrary rotating skew+heat models can show transient critical gain; this demonstrates why NS-specific convolution / rank-one / Curl–Killing restrictions are essential. Such models are not NS conclusions.

### OPEN

The final analytic theorem is transverse Floquet rigidity / finite-Reynolds transverse replenishment exclusion.

---

## 5. Current final statement

The exact frontier is no longer “observe Formation” or “prove one edge is dissipative.” Those are closed.

The remaining question is:

\[
\boxed{
\begin{aligned}
&\text{Can the actual transverse source }T(v)\text{ repeatedly rebuild}\
&\text{the critical spectral shape displaced by the explicit finite-Reynolds}\
&\text{Floquet translation strongly enough to support a compact recurrent}\
&\text{component, without entering the known null/thin-shell/collinear}\
&\text{limits or losing compactness in log-scale?}
\end{aligned}
}
\]

**Status: OPEN.**
