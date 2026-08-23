# 01 — Exact theorems and proofs

This file contains only statements needed by the present proof chain.

---

## Theorem 1 — Complete Curl/Formation state

On the smooth mean-zero periodic class,

\[
\boxed{
O_a(u)\ \forall a
\iff
E_u=[\nabla_u,C]
\iff
S(u)
\iff
u.
}
\]

Also

\[
\boxed{J_u^*=-J_u,\qquad J_u(Cu)=0.}
\]

For

\[
K_u=[C,J_u],
\]

\[
\boxed{K_ub=-2P(S(Cu)b),\qquad K_u^*=K_u,\qquad CN=K_uu.}
\]

### Proof

The shifted signs `H_a` resolve the spectral flag of the self-adjoint curl operator. Their commutators recover the off-diagonal action of `∇_u`; the second polarized commutator removes the residual gauge. Mean-zero periodicity eliminates the remaining Killing ambiguity. The formulas for `J_u` follow from Leray projection and the vector cross product. Since `C` is self-adjoint and `J_u` is skew-adjoint, `[C,J_u]` is self-adjoint. Finally

\[
K_uu=CJ_uu-J_uCu=CN
\]

because `J_u(Cu)=0`.

---

## Theorem 2 — Critical work identities

With `Λ=|C|=HC`,

\[
\boxed{
W
=2\langle\Lambda u,N\rangle
=\langle u,[\Lambda,J_u]u\rangle
=2\langle Hu,K_uu\rangle.
}
\]

### Proof

Skewness gives

\[
2\langle\Lambda u,J_uu\rangle
=\langle u,(\Lambda J_u-J_u\Lambda)u\rangle.
\]

Using `Λ=HC`, `CN=K_uu`, and self-adjointness of `H,K_u` gives the last identity.

---

## Theorem 3 — Constrained-gradient orthogonal split

For `d>0`,

\[
\boxed{N=\gamma G+T,\qquad \gamma=\frac{W}{2d^2}.}
\]

Moreover

\[
\boxed{
\langle T,u\rangle=
\langle T,Cu\rangle=
\langle T,\Lambda u\rangle=0.
}
\]

The regression coefficients satisfy

\[
\boxed{a\ge0,\qquad |b|\le1.}
\]

Define

\[
R^{\rm heat}=a\Lambda u+bC\Lambda u.
\]

Then in `H^{-1/2}`,

\[
\boxed{\Lambda^2u=G+R^{\rm heat}},
\]

and `G,T,R^{heat}` are pairwise orthogonal. Hence

\[
\boxed{D_3=d^2+\|R^{\rm heat}\|_{H^{-1/2}}^2.}
\]

### Proof

`G` is the metric projection of `Λ^2u` onto the tangent direction of the energy-helicity leaf. The coefficient of the projection of `N` onto `G` is

\[
\frac{(N,G)_{-1/2}}{\|G\|_{-1/2}^2}
=\frac{W/2}{d^2}.
\]

The defining regression equations give the two orthogonality constraints and the standard covariance-matrix bounds `a≥0`, `|b|≤1`. The final identity is Pythagoras.

---

## Theorem 4 — Critical stock and neutral-cell debt

\[
\boxed{M'=2\gamma d^2-2\nu D_3.}
\]

Also

\[
\boxed{D_3-d^2\ge\frac{D_2^2}{M}>0}
\]

for every nonzero nondegenerate state. Therefore instantaneous critical neutrality implies

\[
\boxed{\gamma=\nu\frac{D_3}{d^2}>\nu.}
\]

If `M(t_1)=M(t_0)`, then

\[
\boxed{
\int_{t_0}^{t_1}(\gamma-\nu)d^2dt
=\nu\int_{t_0}^{t_1}(D_3-d^2)dt
\ge
\nu\int_{t_0}^{t_1}\frac{D_2^2}{M}dt>0.
}
\]

### Proof

Differentiate `M`, insert Navier–Stokes and Theorem 3. The lower bound is the exact regression/Pythagorean inequality followed by Cauchy–Schwarz. Integrate the identity for `M'` over a neutral cell.

---

## Theorem 5 — Polarized Curl–Killing and physical companions

For curl eigenatoms

\[
Ca_x=xa_x,\qquad Cb_y=yb_y,
\]

\[
\boxed{2B(a_x,b_y)=(x-y)P(b_y\times a_x).}
\]

Hence same-root interactions vanish. For a real noncollinear unequal-root pair, reality supplies the physical outputs

\[
\boxed{p+m,\qquad p-m.}
\]

and

\[
\boxed{
(|p+m|^2-|p|^2)+(|p-m|^2-|p|^2)=2|m|^2.
}
\]

### Proof

Polarize the exact identity `J_u(Cu)=0`. The radial identity is direct expansion of the two squares.

---

## Theorem 6 — Actual-state Poisson visibility

\[
\boxed{\Pi_y(u)u=P_yN(u)-N(P_yu).}
\]

For each nonzero Fourier output `k`,

\[
\boxed{
N_k=\lim_{y\to\infty}e^{y|k|}[\Pi_y(u)u]_k.
}
\]

Consequently

\[
\boxed{
\Pi_y(u)u=0\ \forall y>0
\Longrightarrow N(u)=0.
}
\]

If also

\[
\mathcal C_\tau(u)u=0\quad\forall\tau>0,
\]

then the exact Navier–Stokes trajectory is pure heat.

### Proof

At an incidence `k=p+η`, the Poisson defect is

\[
e^{-y|k|}-e^{-y(|p|+|\eta|)}.
\]

After multiplying by `e^{y|k|}` and sending `y→∞`, only triangle-equality incidences can survive. Those are collinear same-direction incidences and are killed by incompressibility/Leray projection. Hence the limit equals `N_k`. The heat conclusion follows from the analogous actual-state identity.

---

## Theorem 7 — Poisson/heat cocycles and mixed reverse-pair positivity

The cocycles satisfy

\[
\boxed{
\Pi_{y+s}(u)=P_s\Pi_y(u)+\Pi_s(P_yu)P_y,
}
\]

and

\[
\boxed{
H_\tau\Pi_y(u)-\Pi_y(H_\tau u)H_\tau
=P_y\mathcal C_\tau(u)-\mathcal C_\tau(P_yu)P_y.
}
\]

For `r=|p|`, `s=|η|`, `c=|p+η|`, define

\[
a_+=e^{-yc}-e^{-y(r+s)},\quad
a_-=e^{-yr}-e^{-y(c+s)},
\]

\[
b_+=e^{-\tau c^2}-e^{-\tau(r^2+s^2)},\quad
b_-=e^{-\tau r^2}-e^{-\tau(c^2+s^2)}.
\]

Then for `s,y,τ>0`,

\[
\boxed{a_+b_++a_-b_->0.}
\]

### Proof

The cocycle identities follow by adding and subtracting the intermediate smoothed state. The positivity is a direct scalar calculation after pairing the physical forward/reverse incidences.

---

## Theorem 8 — Rank-one completion

For actual-state incidence factors

\[
Z_{ij}=A_iB_j,
\]

\[
\boxed{Z_{ii}Z_{jj}=Z_{ij}Z_{ji}.}
\]

If the diagonal same-output incidences cancel, then

\[
\boxed{
\sum_{i\ne j}|A_iB_j|^2
\ge
\sum_i|A_iB_i|^2.
}
\]

### Proof

The first identity is immediate from rank one. The second follows by expanding

\[
\Big(\sum_i|A_i|^2\Big)\Big(\sum_j|B_j|^2\Big)
\]

and using cancellation of the diagonal vector sum together with Cauchy–Schwarz. It controls raw interaction mass only; it does not identify occupied state mass.

---

## Theorem 9 — Bounded spectral-module passivity

Let

\[
Q=1_{[\rho,R\rho]}(\Lambda),\qquad x=Qu.
\]

For the homogeneous projected equation

\[
x_t=J_Qx-\nu\Lambda^2x,
\qquad J_Q^*=-J_Q,
\]

the propagator obeys

\[
\boxed{
\|V(t,s)\|_{M\to M}
\le\sqrt R\,e^{-\nu\rho^2(t-s)}.
}
\]

### Proof

In `L^2`, skewness eliminates the internal Formation contribution and heat gives `e^{-νρ^2(t-s)}`. On the band, the critical `M` norm is equivalent to `L^2` with ratio at most `R`, producing the factor `√R`.

---

## Theorem 10 — Exact transverse Floquet reduction

For normalized finite viscosity,

\[
v_\theta=N(v)-\kappa C^2v+\kappa D_2v-\beta\mathcal Lv.
\]

Insert `N=γG+T` and set

\[
B(\theta)=\int_0^\theta\beta(s)ds.
\]

With

\[
\widetilde{\mathcal A}_\theta
=e^{-2B}\big[(\gamma-\kappa)C^2-\gamma bC\Lambda\big]
-e^{-B}\gamma a\Lambda+\kappa D_2I,
\]

and

\[
\Phi(\theta,C)=\int_0^\theta\widetilde{\mathcal A}_s(C)ds,
\]

one has

\[
\boxed{
\frac d{d\theta}
\left[e^{-\Phi(\theta,C)}e^{B(\theta)\mathcal L}v(\theta)\right]
=e^{-\Phi(\theta,C)}e^{B(\theta)\mathcal L}T(\theta).
}
\]

### Proof

Use `[C,\mathcal L]=C` and `[\Lambda,\mathcal L]=\Lambda` to conjugate the dilation. All remaining operators are functions of `C,Λ` and commute, so their propagator integrates exactly. The only unresolved source is `T`.

---

## Corollary — Exact status before the stationary frontier

The Theory-2 state is structurally complete; actual-state semigroup covariances are qualitatively visible; fixed finite-ratio spectral recycling is passive; and after the normalized Floquet conjugation the sole unresolved nonlinear source is `T`.

None of these statements supplies the final finite-viscosity saturation exclusion. That problem is treated in `02_STATIONARY_FINITE_VISCOSITY.md` and `03_NO_GO_THEOREMS.md`.