# 00 — Definitions and hypotheses

## 0. Status convention

Every assertion in this dossier is one of:

- **EXACT**: identity/theorem proved from the stated Theory-2 definitions and hypotheses;
- **DEDUCTION**: consequence of EXACT statements plus an explicitly stated compactness/regularity hypothesis;
- **AUDIT/NO-GO**: a rigorous obstruction to an inference or proof architecture; not a Navier–Stokes counterexample unless stated;
- **OPEN**: not proved.

No statement in this dossier claims 3D Navier–Stokes global regularity.

---

## 1. Ambient classes

We use two settings, never interchange them silently.

### (P) Periodic structural class

Smooth mean-zero divergence-free vector fields on `T^3`. This is the class used for the complete shifted-curl flag and finite spectral-network statements.

### (R) Finite-energy Euclidean class

Smooth divergence-free vector fields on `R^3` with enough decay/regularity for all displayed Fourier, radial, `H^{-1/2}`, and integration-by-parts identities. This is the class used for continuous dilation, normalized stationary profiles, radial transfer, and the current frontier.

`P` denotes Leray projection. Set

\[
C=\operatorname{curl},\qquad \Lambda=|C|,\qquad H=\operatorname{sgn}C,
\]

so `C=HΛ` on the divergence-free mean-zero subspace.

---

## 2. Curl/Formation state

For the velocity field `u`, define

\[
E_u=[\nabla_u,C].
\]

For every real shift `a`,

\[
H_a=\operatorname{sgn}(C-aI),\qquad
A_a(u)=[\nabla_u,H_a],
\]

\[
O_a(u)=H_aA_a(u)-A_a(H_au).
\]

Define the Poisson/Formation operator

\[
J_ub=P(b\times Cu),\qquad N(u)=J_uu,
\]

and the Formation mother

\[
K_u=[C,J_u].
\]

The Navier–Stokes equation is

\[
u_t=N(u)-\nu C^2u.
\]

---

## 3. Critical stocks and constrained gradient

Define

\[
M=\langle u,\Lambda u\rangle,
\qquad
D_2=\|\Lambda u\|_2^2,
\qquad
D_3=\|\Lambda^{3/2}u\|_2^2,
\]

and critical work

\[
W=2\langle\Lambda u,N(u)\rangle.
\]

Choose real `a,b` so that

\[
G=\Lambda(\Lambda-a-bC)u
\]

satisfies

\[
\langle u,G\rangle=0,
\qquad
\langle Cu,G\rangle=0.
\]

Set

\[
d^2=\|G\|_{H^{-1/2}}^2
=\|\Lambda^{1/2}(\Lambda-a-bC)u\|_2^2.
\]

When `d>0`, define

\[
\gamma=\frac{W}{2d^2}
\]

and the transverse component

\[
\boxed{N=\gamma G+T.}
\]

Then

\[
\langle T,u\rangle=
\langle T,Cu\rangle=
\langle T,\Lambda u\rangle=0.
\]

---

## 4. Semigroup covariances

Poisson depth:

\[
P_y=e^{-y\Lambda},
\qquad
\Pi_y(u)=P_yJ_u-J_{P_yu}P_y.
\]

True heat depth:

\[
H_\tau=e^{-\tau C^2}=e^{-\tau\Lambda^2},
\]

\[
\mathcal C_\tau(u)=H_\tau J_u-J_{H_\tau u}H_\tau.
\]

The actual-state vectors are

\[
\Pi_y(u)u=P_yN(u)-N(P_yu),
\]

and

\[
\mathcal C_\tau(u)u=H_\tau N(u)-N(H_\tau u).
\]

---

## 5. Physical companion interaction

For divergence-free Fourier atoms `a_p,b_q`, with output `k=p+q`, the symmetric physical bilinear Formation is denoted `B(a_p,b_q)` and obeys

\[
2B(a_p,b_q)_k
=-iP_k\big[(a_p\cdot k)b_q+(b_q\cdot k)a_p\big].
\]

For curl eigenatoms

\[
Ca_x=xa_x,\qquad Cb_y=yb_y,
\]

polarized Curl–Killing gives

\[
2B(a_x,b_y)=(x-y)P(b_y\times a_x).
\]

Reality retains the physical sum/difference companions.

For actual-state incidence factors we write

\[
Z_{ij}=A_iB_j.
\]

This rank-one factorization must be preserved; arbitrary tensor or isolated-Galerkin replacements are not allowed.

---

## 6. Normalized finite-viscosity variables

In the Euclidean normalized branch impose

\[
E=\|v\|_2^2=1,
\qquad
M=\langle v,\Lambda v\rangle=1.
\]

Let

\[
\mathcal L=\frac32+x\cdot\nabla,
\qquad
\widehat{\mathcal Lf}
=-(\tfrac32+\xi\cdot\nabla_\xi)\hat f.
\]

The normalized finite-viscosity equation is

\[
\boxed{
v_\theta=N(v)-\kappa C^2v+\kappa D_2v-\beta\mathcal Lv,
}
\]

\[
\beta=W-2\kappa(D_3-D_2),
\qquad \kappa>0.
\]

For stationary normalized candidates, define

\[
Y_v=C^2v-D_2v+2D_2\mathcal Lv,
\]

\[
\boxed{
R_{\rm fv}=Y_v-\frac{D_3}{d^2}G_v.
}
\]

---

## 7. Hypotheses used only for quantitative compactness deductions

When a compact class `K` is invoked, it is assumed explicitly that:

1. `K` lies in a graph topology strong enough for all displayed quantities to be defined;
2. `v\mapsto T(v)` and `v\mapsto R_{\rm fv}(v)` are continuous into `H^{-1/2}`;
3. `E=M=1`, `\kappa` is bounded away from `0` and `∞`, and the class is separated from the stated exceptional/null strata whenever such separation is used;
4. ordinary compactness of `K` is **not** interpreted as finite Fourier complexity or compactness of normalized microscopic descendants.

A uniform angle gap additionally requires `T` and `R_{\rm fv}` to stay nonzero. The normalized saturation-ratio gap does not require `T\neq0`.

---

## 8. Nonclaims

The following are never assumed:

\[
\text{operator positivity}\Rightarrow\text{actual-state sign},
\]

\[
\text{finite readers}\Rightarrow\text{finite-dimensional reconstruction},
\]

\[
\text{finite-network rigidity}\Rightarrow\text{uniform continuum rigidity},
\]

or

\[
\text{radial solvability}\Rightarrow\text{state-incidence closure}.
\]

The final missing structure is stated in `04_OPEN_FRONTIER.md`.