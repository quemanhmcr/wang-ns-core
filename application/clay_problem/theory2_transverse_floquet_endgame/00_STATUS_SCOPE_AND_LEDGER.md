# 00 — Status, scope, and theorem ledger

## 1. Exact claim of this dossier

Theory-2 has achieved strong structural closure:

\[
O_a(u)\ \forall a
\iff
E_u=[\nabla_u,C]
\iff
S(u)
\iff
u,
\]

and the Poisson Formation mother

\[
K_u=[C,J_u]
\iff
S(Cu)
\iff
u.
\]

Actual-state vector cocycles classify the relevant zero sets, while finite-viscosity geometry supplies genuine coercive statements. However,

\[
\boxed{
\text{structural completeness}\neq\text{Navier–Stokes regularity}.
}
\]

The current stationary finite-`κ` problem has now been reduced beyond the all-depth common-ray formulation to a **finite transverse saturation problem plus one continuum companion-nonconcentration step**.

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
\qquad
G=\Lambda(\Lambda-a-bC)u,
\qquad
\gamma=\frac{W_\Lambda}{2d^2},
\]

with `T` the unique transverse steering component.

### 2.3 Actual-state semigroup Formation cocycles

\[
\Pi_y(u)=P_yJ_u-J_{P_yu}P_y,
\]

\[
\mathcal C_\tau(u)
=e^{-\tau C^2}J_u-J_{e^{-\tau C^2}u}e^{-\tau C^2}.
\]

### 2.4 Bounded spectral module passivity

For

\[
Q=1_{[\rho,R\rho]}(\Lambda),
\]

internal projected Formation is skew and

\[
\boxed{
\|V(t,s)\|_{M\to M}
\le
\sqrt R\,e^{-\nu\rho^2(t-s)}.
}
\]

Thus arbitrary internal high-valence/time-dependent recycling inside a fixed finite-ratio spectral module is passive after a finite viscous horizon.

### 2.5 Finite-viscosity normalized recurrence

On `R^3`, normalize `E=M=1`. Then

\[
\boxed{
v_\theta=N(v)-\kappa C^2v+\kappa D_2v-\beta\mathcal Lv,
}
\]

\[
\beta=W_\Lambda-2\kappa(D_3-D_2).
\]

Every critically neutral cycle satisfies

\[
\boxed{
\Delta\log r=2\int\kappa D_2\,d\theta>0.
}
\]

### 2.6 Complete transverse Floquet reduction

After factoring all commuting nontransverse dynamics,

\[
\boxed{
\frac d{d\theta}
\left[e^{-\Phi(\theta,C)}e^{B(\theta)\mathcal L}v\right]
=e^{-\Phi(\theta,C)}e^{B(\theta)\mathcal L}T.
}
\]

Only `T` remains as unresolved dynamical source.

### 2.7 Stationary positive-depth `T` coercivity

For nondegenerate stationary finite-`κ` profiles,

\[
\beta=2\kappa D_2,
\qquad
H_3=0,
\qquad
|b|<1,
\]

and the positive-depth transverse equation is

\[
\boxed{
\gamma(1-\sigma b)\partial_y\mathcal V_\sigma
+(\gamma a-2\kappa D_2y)\mathcal V_\sigma
=\mathcal T_\sigma.
}
\]

The derivative coefficient is positive on both helicity sheets and, on the stationary branch, obeys the stronger finite-viscosity bound

\[
\boxed{
\gamma(1-\sigma b)\ge\kappa.
}
\]

Compact stationary finite-Reynolds strata therefore satisfy a mode-count-independent transverse load

\[
\boxed{
\|T\|_{H^{-1/2}}\gtrsim_{\mathcal K}\kappa.
}
\]

### 2.8 Stationary transverse saturation

Define

\[
Y_v=\Lambda^2v-D_2v+2D_2\mathcal Lv,
\]

\[
R_{\rm fv}
=Y_v-\frac{D_3}{d^2}G_v.
\]

Then stationarity is exactly

\[
\boxed{T=\kappa R_{\rm fv}.}
\]

Moreover `R_{\rm fv}` is the `H^{-1/2}` transverse projection of `Y_v`.

The stationary residual has the exact Pythagorean decomposition

\[
\boxed{
\begin{aligned}
\|T-\kappa R\|_{-1/2}^{2}
={}&
(\|T\|_{-1/2}-\kappa\|R\|_{-1/2})^2\\
&+2\kappa\|T\|_{-1/2}\|R\|_{-1/2}(1-\cos\vartheta).
\end{aligned}}
\]

Thus a stationary profile must saturate both an angle defect and a gain defect.

The minimal coercive closure is

\[
\boxed{
\|T-\kappa R_{\rm fv}\|_{-1/2}
\ge
\eta_{\mathcal K}
\bigl(
\|T\|_{-1/2}+\kappa\|R_{\rm fv}\|_{-1/2}
\bigr).
}
\]

### 2.9 Finite completed-network rigidity

For a finite completed nonexceptional physical interaction network, actual-state rank-one completion plus reality companions and unequal-shell rigidity rule out

\[
\boxed{T=\lambda R_{\rm fv},\qquad\lambda>0.}
\]

Therefore compact finite-complexity completed network families possess a positive transverse angle gap.

### 2.10 Rank-one mass propagation

If diagonal same-output products cancel, actual-state rank one gives

\[
\boxed{
\sum_{i\ne j}|A_iB_j|^2
\ge
\sum_i|A_iB_i|^2.
}
\]

Hence coherent hiding cannot destroy raw completed companion interaction mass.

---

## 3. Nonclaims / anti-loop guards

The following moves are forbidden:

- structural completeness `≠` Navier–Stokes regularity;
- operator-pair positivity `≠` actual-state return sign;
- symbol positivity `≠` nonlinear PDE coercivity;
- vector observability `≠` critical-work orientation;
- near-neutrality `≠` small `T`;
- arbitrary Galerkin triads are not physical substitutes because companion leakage is deleted;
- no infinite scalar moment hierarchy recovers complete Formation;
- there is no universal dissipation frequency;
- a terminal defect need not contain one positive-mass bubble;
- torus dilation is not an exact internal continuous symmetry;
- global critical Floquet spectral gap is false because of the infrared translation characteristic;
- the whole positive-depth Laplace family is not a smaller theorem: inverting it reconstructs the stationary radial equation;
- compactness does not imply finite Fourier/triad complexity;
- finite completed-network coercivity does not imply a uniform continuum constant;
- raw rank-one interaction mass does not automatically equal occupied critical state mass;
- abstract tensor tomography cannot replace the actual same-state rank-one object `v\otimes v`.

---

## 4. Current theorem ledger

### EXACT

1. Theory-2 flag / commutator / strain equivalences.
2. Poisson Formation Hamiltonian structure and complete mother `K_u`.
3. Constrained-gradient decomposition `N=γG+T`.
4. Strict neutral-cell super-viscous creation identity.
5. Mixed-helicity necessity and polarized Curl–Killing.
6. Actual-state Poisson zero-set visibility.
7. True-heat / Poisson finite covariance formulas and parity.
8. Physical sum–difference companion leakage.
9. Paired mixed Poisson–heat curvature positivity.
10. Rank-one cross-completion of angular cancellation.
11. Bounded spectral module finite-step contraction.
12. Finite-viscosity doubly normalized flow and positive neutral scale drift.
13. Nonexistence of `T=0` stationary / periodic finite-Reynolds normalized profiles.
14. Complete transverse Floquet normal form.
15. Critical log-frequency monodromy and infrared characteristic.
16. Stationary regression algebra and `|b|<1`.
17. Positive-Poisson-depth ray anti-alignment family.
18. First-order depth equation and signed `T` passivity.
19. Canonical heat-depth radial derivative / raywise energy-inward critical-neutral geometry.
20. Exact stationary vector saturation `T=κR_{\rm fv}`.
21. `R_{\rm fv}` is the transverse projection of the finite-viscosity radial/dilation defect.
22. Exact Pythagorean angle/gain decomposition of the stationary residual.
23. Rank-one companion cancellation propagates comparable raw interaction mass.
24. Finite completed nonexceptional interaction networks cannot realize positive transverse saturation.

### DEDUCTION

1. Compact nonexceptional strata admit finite vector observation gaps.
2. Closed three-shell/high-valence internal recycling is not the terminal obstruction.
3. Persistent finite-Reynolds regeneration requires cross-module / transverse replenishment.
4. Compact periodic finite-`κ` recurrence would imply parabolic physical concentration.
5. Compact stationary finite-`κ` strata satisfy a scale-critical `T` gap.
6. Finite `κ` quantitatively separates stationary profiles from `d=0`, `|b|=1`, and the pure-helicity regression boundary, assuming the stated critical bilinear estimate.
7. Once exact positive parallelism is excluded on a compact class, a quantitative angle gap follows by continuity.

### AUDIT

1. Arbitrary rotating skew+heat models permit transient critical gain; NS-specific physical restrictions are essential.
2. The all-depth Laplace family is injective but not a global finite-reader coercive theorem.
3. The hostile angular laminate has exact local cancellation while cross-output displacement can be only `O(h^2)`; there is no uniform one-step outward gap.
4. Functional compactness does not bound physical triad count.

### OPEN

1. **Companion nonconcentration:** completed rank-one Formation mass cannot survive through arbitrarily many increasingly fine angular/radial generations with nonvanishing size unless the state approaches an exceptional stratum.
2. **Finite-depth interaction-to-occupation:** construct a mode-count-independent physical functional `\mathfrak M_{\rm comp}` such that finitely many positive-depth state readers control completed companion interaction mass and that functional controls orthogonal leakage/export.
3. **Finite-Reynolds transverse saturation rigidity:** deduce a uniform angle defect or gain defect and thereby exclude `T=κR_{\rm fv}` on compact stationary nonexceptional components.
4. **Periodic transverse Floquet rigidity:** time-ordered analogue for recurrent finite-`κ` normalized trajectories.
5. Euler-dominated recurrence / scale-radiation terminal classification remains separate.

---

## 5. Current final frontier

The finite-complexity physical problem is closed. The remaining stationary obstruction is uniquely localized to the continuum limit:

\[
\boxed{
\text{completed rank-one interaction mass migrating through an increasingly fine angular/radial companion laminate.}
}
\]

The missing implication is

\[
\boxed{
\text{completed companion interaction mass}
\Longrightarrow
\text{finite-depth occupied mass or a transverse angle/gain defect}.
}
\]

A desirable finite formulation is

\[
\boxed{
\sum_{j=1}^{m}\|\mathcal V(y_j)\|_2^2
\ge
c_{\mathcal K}\,\mathfrak M_{\rm comp}(v),
}
\]

with

\[
\boxed{
\mathfrak M_{\rm comp}(v)
\gtrsim
\|T_{\perp R}(v)\|_{-1/2}^2
+
\text{exported hidden mass}.
}
\]

If this bridge is proved using finitely many existing semigroup depths and actual rank-one companion geometry, without inverting the continuum ray family, the compact stationary finite-`κ` branch will have been reduced to a genuinely smaller coercive theorem rather than a rewritten stationary Navier–Stokes equation.

**Status: OPEN.**
