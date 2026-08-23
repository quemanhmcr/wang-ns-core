# 09 — Chronological theorem chain: from first Theory-2 deployment to the latest transverse Floquet frontier

This file records the proof evolution in chronological mathematical order rather than by topic.

---

## Stage 1 — Complete Theory-2 state

### T1. Shifted curl-flag completeness — EXACT

\[
O_a(u)\ \forall a
\iff
E_u=[\nabla_u,C]
\iff
S(u)
\iff
u.
\]

The complete shifted-sign flag resolves the deformation of curl strongly enough to recover the smooth mean-zero periodic state.

### T2. Poisson Formation representation — EXACT

\[
J_ub=P(b\times Cu),
\qquad
N(u)=J_uu,
\]

\[
J_u^*=-J_u,
\qquad
J_u(Cu)=0.
\]

This places Euler Formation into a skew Poisson geometry while preserving energy and helicity.

### T3. Complete Poisson mother — EXACT

\[
K_u=[C,J_u],
\]

\[
K_ub=-2P(S(Cu)b),
\]

\[
K_u\iff S(Cu)\iff u,
\]

\[
K_u^*=K_u,
\qquad
CN=K_uu.
\]

### T4. Critical reader — EXACT

\[
W_\Lambda
=2\langle\Lambda u,N\rangle
=\langle u,[\Lambda,J_u]u\rangle
=2\langle Hu,K_uu\rangle.
\]

The complete state is kept vector/operator-valued until this scalar reader is genuinely required.

---

## Stage 2 — Constrained critical geometry

### T5. Energy–helicity constrained-gradient split — EXACT

\[
G=\Lambda(\Lambda-a-bC)u,
\]

\[
d^2=\|G\|_{H^{-1/2}}^2,
\]

\[
\gamma=\frac{W_\Lambda}{2d^2},
\]

\[
\boxed{N=\gamma G+T.}
\]

`T` is orthogonal to `u,Cu,Λu` and is the unique transverse steering component.

### T6. Regression and saturation — EXACT

\[
|b|\le1,
\qquad
a\ge0.
\]

`d=0` on finite-energy `R^3` forces pure helicity. If `a=0`, then `|b|=1` and `N=0`.

### T7. Strict residual heat gap — EXACT

\[
D_3-d^2
\ge
\frac{D_2^2}{M}>0.
\]

### T8. Neutral-cell super-viscous creation — EXACT

\[
M'=2\gamma d^2-2\nu D_3.
\]

For a neutral cell,

\[
\int(\gamma-\nu)d^2
=
\nu\int(D_3-d^2)
>0.
\]

So neutrality requires constrained-gradient creation strictly above viscosity; `T` is purely catalytic in critical work.

---

## Stage 3 — Helicity and complete physical interactions

### T9. Equal sheet creation — EXACT

\[
\dot C_++2\nu D_+=W_\Lambda/2,
\]

\[
\dot C_-+2\nu D_-=W_\Lambda/2.
\]

Positive creation is shared equally by both helicity sheets.

### T10. Mixed-helicity necessity — EXACT

For a complete triad,

\[
W_{\rm tri}=\tau\Theta,
\]

\[
\Theta=
\det
\begin{pmatrix}
1&1&1\\
x&y&z\\
|x|&|y|&|z|
\end{pmatrix}.
\]

Same-sign roots give `Θ=0`.

### T11. Polarized Curl–Killing — EXACT

\[
2B(a_x,b_y)
=(x-y)P(b_y\times a_x).
\]

Same signed-root interactions vanish exactly.

### T12. Full shifted-flag Euler representation — EXACT

\[
N(u)
=-\frac12\int P(H_au\times u)\,da
=-\int P(u_+^a\times u_-^a)\,da.
\]

---

## Stage 4 — Finite semigroup covariances

### T13. Poisson covariance — EXACT

\[
\Pi_y(u)=P_yJ_u-J_{P_yu}P_y.
\]

Its incidence multiplier is

\[
e^{-y|p+\eta|}-e^{-y(|p|+|\eta|)}.
\]

### T14. True-heat covariance — EXACT

\[
\mathcal C_\tau(u)
=H_\tau J_u-J_{H_\tau u}H_\tau.
\]

Multiplier:

\[
e^{-\tau|p+\eta|^2}-e^{-\tau(|p|^2+|\eta|^2)}.
\]

Heat resonance is `p·η=0`.

### T15. Finite covariance parity — EXACT

The self-adjoint/skew decomposition is explicit, and the skew half vanishes only for the zero state.

### T16. Actual-state Poisson zero-set theorem — EXACT

\[
\Pi_y(u)u=0\ \forall y>0
\Longrightarrow
N(u)=0.
\]

This removes the need for independent-probe operator flatness on the qualitative observation side.

### T17. Common Poisson/heat zero set is pure heat — EXACT

If also

\[
\mathcal C_\tau(u)u=0\ \forall\tau>0,
\]

then the exact NS trajectory is

\[
u(t)=e^{-\nu tC^2}u(0).
\]

---

## Stage 5 — Physical companions and curvature

### T18. Real sum–difference companion leakage — EXACT

Every non-null real pair generates

\[
p+m,
\qquad
p-m.
\]

A projected single-triad saturation which deletes one output is artificial.

### T19. Radial companion defect — EXACT

\[
(|p+m|^2-|p|^2)+(|p-m|^2-|p|^2)=2|m|^2.
\]

### T20. Poisson + heat depths resolve radial cancellation classes — EXACT

All-depth cancellation separates by unordered parent radii, and the signed flag further separates signed roots.

### T21. Mixed commuting-square curvature — EXACT

\[
H_\tau\Pi_y(u)-\Pi_y(H_\tau u)H_\tau
=
P_y\mathcal C_\tau(u)-\mathcal C_\tau(P_yu)P_y.
\]

For physical forward/reverse defects,

\[
\boxed{a_+b_++a_-b_->0.}
\]

Infinitesimally,

\[
\delta_+q_++\delta_-q_-
\ge2s^3.
\]

### T22. Pair-potential decomposition — EXACT

\[
\delta_+q_++\delta_-q_-
=2s^3+2(r-c)^2(r+c),
\]

while the antisymmetric part is

\[
\Psi(r,s)-\Psi(c,s),
\qquad
\Psi(a,b)=ab(a+b).
\]

Positive conserved radius-pair circulation cannot hide the positive symmetric core.

---

## Stage 6 — Actual-state overlap classification

### T23. Local angular kernel — EXACT

At fixed equal spectral data,

\[
N_{k;\lambda}=0
\iff
\widehat z(\pm1)=0.
\]

So the local angular kernel is the first-harmonic annihilator, not merely translation gauge.

### T24. Actual-state rank-one completion — EXACT

\[
Z_{ij}=A_iB_j,
\qquad
\operatorname{rank}Z=1.
\]

Every diagonal cancellation forces all physical cross incidences.

### T25. Cross-incidence mass debt — EXACT

\[
\sum_{i\ne j}|A_iB_j|^2
\ge
\sum_i|A_iB_i|^2.
\]

### T26. Outward grading — EXACT

For distinct equal-output decompositions,

\[
|p_i+m_j|^2
=|k|^2+|p_i-p_j|^2>|k|^2.
\]

On the torus this is quantized by the lattice spacing.

### T27. Unequal-shell rigidity — EXACT

On periodic curl eigenshells with unequal radii,

\[
B(a_x,b_y)=0
\]

forces common-line support. The globally completed nonexceptional angular kernel is therefore collinear.

### T28. Binary Möbius radiation — EXACT

Binary angular cancellation obeys

\[
X_{n+1}=2-\frac\Delta{X_n},
\]

and monotonically approaches the collinear characteristic. No compact binary interior cycle exists.

---

## Stage 7 — Sign theorems and no-go results

### T29. Critical commutator reader of mixed curvature — EXACT

\[
\mathcal P_{y,\tau}
=\operatorname{Re}\langle u,[\Lambda,\mathscr R_{y,\tau}(u)]u\rangle.
\]

Edgewise,

\[
(\mathcal P_{y,\tau})_e
=\frac{a_+b_++a_-b_-}{2}W_e.
\]

### T30. Complete mixed-triad sign preservation — EXACT

\[
\mathcal P_{{\rm PH},{\rm tri}}
=\mu_{\rm tri}W_{\rm tri},
\qquad
\mu_{\rm tri}>0.
\]

### T31. Pointwise global sign theorem is false — EXACT counterexample

Two separated complete triads can give

\[
M'=0,
\qquad
W>0,
\qquad
\mathcal P_{\rm PH}<0.
\]

Finite time is therefore essential.

### T32. Skinny complementarity — EXACT

For `a∼b≫c`, relative companion leakage and normalized curvature vanish together while cubic-stock amplification diverges.

This classifies the only companion-strength degeneration.

---

## Stage 8 — Finite-step coercivity

### T33. Isolated reverse block passivity — EXACT

Each radial singular pair evolves under

\[
\begin{pmatrix}
-\nu r^2&-g\\
g&-\nu c^2
\end{pmatrix}.
\]

An underdamped projective Formation return is multiplied by a strict scalar heat contraction. Overdamped blocks do not return.

### T34. Bounded-module contraction — EXACT

For

\[
Q=1_{[\rho,R\rho]}(\Lambda),
\]

arbitrary time-dependent internal skew Formation obeys

\[
\boxed{
\|V(t,s)\|_{M\to M}
\le\sqrt R\,e^{-\nu\rho^2(t-s)}.
}
\]

Thus arbitrary three-shell/high-valence internal recycling is not the terminal obstruction.

### T35. Whole-module external forcing debt — EXACT

If a bounded module fails to lose critical stock after its coercive horizon, the cross-module Formation forcing must satisfy a quantitative Duhamel lower bound.

### T36. `T`-only signed-root recruitment — EXACT

\[
\dot u_x=\ell_xu_x+T_x.
\]

Only `T` creates or rotates projective signed-root directions.

---

## Stage 9 — Terminal normalization

### T37. Critical Reynolds scaling — EXACT

\[
z_\tau=N(z)-\frac\varepsilon\alpha C^2z.
\]

Absolute frequency cancels; `α/ε` is the true local parameter.

### T38. Renormalized Euler flow — EXACT

\[
v_\theta=N(v)-W\mathcal Lv.
\]

Positive recurrent scale growth forces normalized helicity to vanish.

### T39. Euler transverse normal form — EXACT

\[
v_\theta=T-WR^{\rm dil}.
\]

`R^{dil}=0` has no nonzero finite-energy solution.

### T40. Doubly normalized finite-viscosity flow — EXACT

\[
\boxed{
v_\theta=N(v)-\kappa C^2v+\kappa D_2v-\beta\mathcal Lv.
}
\]

### T41. Positive scale drift for neutral finite-viscosity cycles — EXACT

\[
\boxed{
\Delta\log r=2\int\kappa D_2\,d\theta>0.
}
\]

### T42. `T=0` finite-Reynolds recurrence impossible — EXACT / DEDUCTION

The homogeneous normalized infrared profile is `ρ^{-2}` and not finite energy; exact periodic `T=0` recurrence is likewise excluded.

---

## Stage 10 — Latest frontier: complete transverse Floquet reduction

### T43. Integrate all nontransverse dynamics — EXACT

\[
\boxed{
\frac d{d\theta}
\left[e^{-\Phi(\theta,C)}e^{B(\theta)\mathcal L}v\right]
=e^{-\Phi(\theta,C)}e^{B(\theta)\mathcal L}T.
}
\]

### T44. Exact one-cycle transverse fixed point — EXACT

\[
\boxed{(I-\mathcal M_0)v_0=G_T.}
\]

### T45. Critical log-frequency monodromy — EXACT

\[
(\mathbb M_0F)_\sigma(s,\omega)
=w_\sigma(s)F_\sigma(s+B_*,\omega),
\]

\[
\lim_{s\to-\infty}w_\sigma(s)=1.
\]

### T46. No global critical Floquet gap — EXACT

\[
\boxed{
\inf_{\|F\|_M=1}
\|(I-\mathbb M_0)F\|_M=0.
}
\]

The obstruction is an infrared critical translation characteristic.

### T47. Compact actual recurrence is spectrally tight — EXACT inequality

\[
M_{<\rho_0}\le\rho_0,
\]

\[
M_{>R}\le D_2/R.
\]

Hence compact finite-`κ` recurrence cannot place order-one critical mass at the asymptotic characteristic.

### T48. Compact recurrence requires order-one transverse Floquet source — DEDUCTION

Under uniform `κ`, period and `D_2` bounds, one cycle must carry a positive propagated `T`-source debt on the relevant finite log-frequency band.

### T49. Transverse ancestry reaches arbitrarily small normalized radii — EXACT recurrence consequence

If the one-cycle `T` source vanished below a finite scale, finite energy plus the homogeneous recurrence would force the entire profile to vanish.

### T50. Hostile infrared repair by full Formation — conditional exact asymptotic

The stationary equation is

\[
\rho f_\rho+\left(2-\frac{\rho^2}{2D_2}\right)f
=-\frac{\widehat N}{2\kappa D_2}.
\]

Under sufficient decay, physical output-null structure gives `\widehat N=O(ρ)`, so a finite-energy particular solution can behave as `f=O(ρ)` and repair the forbidden homogeneous `ρ^{-2}` branch.

Therefore `T=0` nonexistence does not perturb directly to `T≠0`.

---

# Final frontier

The problem has been reduced to:

\[
\boxed{
F=\mathbb M_0[F]F+\mathbb G_T[F].
}
\]

**OPEN:** prove that the actual Theory-2 transverse source cannot self-consistently sustain a compact finite-Reynolds recurrent solution of this weighted critical-shift fixed-point equation, except through classified exceptional limits or genuine log-scale loss of compactness.

Until that arrow is closed, no Navier–Stokes global regularity claim is justified.
