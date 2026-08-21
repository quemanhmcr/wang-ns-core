# Application 1 — Blow-up via Theory 1: Full-Core Critical Rigidity

## 1. Purpose

This folder is **Application 1 of Theory 1**.  Here **Theory 1** is the canonical Metric–Lie/Hodge Formation Core, applied to the finite-time blow-up problem for smooth homogeneous incompressible three-dimensional Navier–Stokes.

The guiding rule is deliberately strict:

> **Do not replace the full state by a lower-information observer.**

Pressure, vortex stretching, Riccati variables, helicity torsion, spectral hinges, local alignment tensors, and individual triad mechanisms are useful renderers, but none is taken here as the primitive state.  The application starts from the same full core that forms the equation:

\[
\boxed{
\mathcal C_{NS}
=
\bigl(\mathfrak g_\sigma,[\cdot,\cdot],\langle\cdot,\cdot\rangle_{L^2},C\bigr),
\qquad C=\operatorname{curl}.
}
\]

Equivalently, the nonlinear datum is the metric Lie tensor

\[
\boxed{T(a,b,c)=\langle a,[b,c]\rangle.}
\]

The canonical formation form is

\[
\boxed{
\ell_{\nu,u}(a,b)
=-\langle u,[a,b]\rangle
-\nu\langle Ca,Cb\rangle,
}
\]

with Riesz operator

\[
\boxed{
\mathcal L_{\nu,u}=\mathcal J_u-\nu C^2,
\qquad
u_t=\mathcal L_{\nu,u}u.
}
\]

The application question is therefore not "which mechanism causes blow-up?" but:

\[
\boxed{
\text{Can a trajectory of this complete core lose critical compactness in finite physical time?}
}
\]

## 2. Main reduction

Let

\[
\Lambda=|C|,
\qquad
K(u)=\|\Lambda^{1/2}u\|_2^2,
\qquad
E(u)=\|u\|_2^2.
\]

At the critical level,

\[
\boxed{
\frac12\frac d{dt}K(u)
=
\langle\Lambda u,\mathcal J_u u\rangle
-\nu\|\Lambda^{3/2}u\|_2^2.
}
\]

The nonlinear term is the full-state critical work

\[
\boxed{W_c(u)=\langle\Lambda u,\mathcal J_u u\rangle.}
\]

No independent pressure or stretching variable is needed: \(W_c\) is a contraction of the complete formation law.

For the blow-up normalization step, work on \(\mathbb R^3\) (or in the corresponding rescaled local blow-up chart).  Continuous Navier–Stokes dilation is not an internal continuous symmetry of a fixed torus.  In that typed setting, the current strongest reduction removes both critical amplitude and dilation.  Set

\[
A=\sqrt{K(u)},
\qquad
\rho=\frac{K(u)}{E(u)},
\]

and write

\[
\boxed{u=A\,S_\rho v,\qquad (S_\rho f)(x)=\rho f(\rho x).}
\]

Then \(v\) is normalized by

\[
\boxed{
\|v\|_2^2=1,
\qquad
\|\Lambda^{1/2}v\|_2^2=1.
}
\]

With nonlinear time

\[
\boxed{\frac{d\tau}{dt}=A\rho^2,}
\]

the exact normalized equation is

\[
\boxed{
v_\tau
=
B(v,v)
-\frac{\nu}{A}C^2v
-\alpha v
-\beta Gv,
\qquad
Gv=v+x\cdot\nabla v,
}
\]

where

\[
\boxed{
\alpha=W(v)-\frac{\nu}{A}M_3(v),
}
\]

\[
\boxed{
\beta=2W(v)-\frac{2\nu}{A}\bigl(M_3(v)-M_2(v)\bigr),
}
\]

and

\[
W(v)=\langle\Lambda v,B(v,v)\rangle,
\qquad
M_2(v)=\|\Lambda v\|_2^2,
\qquad
M_3(v)=\|\Lambda^{3/2}v\|_2^2.
\]

If a hypothetical critical blow-up sequence has \(A\to\infty\), then \(\nu/A\to0\).  The limiting full-core quotient flow is therefore

\[
\boxed{
 v_\tau
 =
 B(v,v)
 -2W(v)\mathcal Sv,
 \qquad
 \mathcal S=x\cdot\nabla+\frac32.
}
\]

This is the **Core END Flow** used in this application.

## 3. Reconstruction of the removed variables

The removed amplitude and scale are not discarded; they are reconstructed from the same full state:

\[
\boxed{
\frac{d\log A}{d\tau}=W(v)
\quad\text{in the inviscid normalized limit},
}
\]

\[
\boxed{
\frac{d\log\rho}{d\tau}=2W(v).
}
\]

Hence

\[
\boxed{
A(\tau)
=A(0)\exp\!\left(\int_0^\tau W(v(s))\,ds\right),
\qquad
\rho\propto A^2.
}
\]

A critical-amplitude blow-up therefore requires

\[
\boxed{
\int_0^\tau W(v(s))\,ds\to+\infty.
}
\]

This is not an observer criterion: \(W(v)\) is computed from the complete normalized state through the same core tensor \(T\).

## 4. Exact structural constraints on a dangerous orbit

### 4.1 Helicity

Let

\[
h(v)=\langle v,Cv\rangle.
\]

Physical helicity is \(\mathcal H(u)=A^2h(v)\) under the above normalization.  In the inviscid quotient flow,

\[
\boxed{h_\tau=-2W(v)h.}
\]

Thus any complete recurrent normalized orbit with positive mean critical drift must satisfy

\[
\boxed{h\equiv0.}
\]

In particular, one-helicity and nonzero-helicity recurrent locks cannot be the final blow-up object.

### 4.2 Finite closure

Any trajectory confined to a fixed finite-dimensional \((T,C)\)-closed Galerkin subspace obeys the finite-dimensional energy law

\[
\frac12\frac d{dt}\|u_N\|_2^2=-\nu\|Cu_N\|_2^2
\]

and is a bounded smooth polynomial ODE.  Hence it exists globally.  A genuine singular orbit must therefore escape every fixed finite \((T,C)\)-closed subsystem.

### 4.3 Exact dilation-locked profile

A fixed point of the Core END Flow satisfies

\[
\boxed{
B(v,v)=b\left(x\cdot\nabla+\frac32\right)v,
\qquad b=2W(v)>0.
}
\]

Pairing with energy and helicity gives the exact restrictions

\[
\boxed{\langle v,Cv\rangle=0}
\]

for every amplifying fixed point.  Thus an exact self-similar enemy, if one exists, must be a genuinely three-dimensional, zero-helicity, infinite-closure solution of this single core equation.

## 5. Critical curvature and chiral form

The full-state critical work also admits the self-adjoint curvature representation

\[
\boxed{
\mathscr R_u
=\frac12\Lambda^{-3/2}[\Lambda,\mathcal J_u]\Lambda^{-3/2},
\qquad
z=\Lambda^{3/2}u,
}
\]

so

\[
\boxed{
\frac12\frac d{dt}\|\Lambda^{1/2}u\|_2^2
=
\langle z,(\mathscr R_u-\nu I)z\rangle.
}
\]

Because helicity is a Casimir, \(\mathcal J_u(Cu)=0\).  With \(H=\operatorname{sgn}C\), \(P_\pm=(I\pm H)/2\), and

\[
A_u=P_+\mathcal J_uP_-,
\]

one obtains the exact critical identity

\[
\boxed{
W_c(u)
=2\operatorname{Re}\langle u_+,[\Lambda,A_u]u_-\rangle.
}
\]

Thus critical nonlinear growth requires both helicity-sign mixing and radial noncommutation.  It cannot be created inside a single signed-curl sheet or by interactions that commute with \(\Lambda\).

This is a structural characterization, not a regularity proof: exact smooth finite-dimensional states can exhibit strong positive instantaneous critical curvature.

## 6. Spectral stress representation

For a typed scalar reader \(q(C)\), define

\[
\mathcal T_u(q)=\langle q(C)u,\mathcal J_uu\rangle.
\]

Energy and helicity imply

\[
\mathcal T_u(1)=\mathcal T_u(x)=0.
\]

Define the hinge stress

\[
\boxed{
\Sigma_u(r)=\mathcal T_u\bigl((x-r)_+\bigr).
}
\]

Then, for readers with a suitable second-derivative representation,

\[
\boxed{
\mathcal T_u(q)=\int q''(r)\Sigma_u(r)\,dr.
}
\]

In particular,

\[
\boxed{W_c(u)=2\Sigma_u(0).}
\]

If \(\mu_u\) is the signed-curl spectral energy measure defined by

\[
\int q(x)\,d\mu_u(x)=\frac12\langle u,q(C)u\rangle,
\]

then the scalar spectral balance is

\[
\boxed{
\partial_t\mu
=
\partial_x^2\Sigma
-2\nu x^2\mu
}
\]

in the distributional sense.  This is a renderer of the full state, not a closed replacement for it: \(\Sigma_u\) is always reconstructed from \(u\) through the same formation core.

For the critical excess beyond radius \(R\),

\[
X_R(t)=\int (|x|-R)_+\,d\mu_t(x),
\]

one has

\[
\boxed{
\dot X_R
=
\Sigma_u(R)+\Sigma_u(-R)
-2\nu\int x^2(|x|-R)_+\,d\mu_t(x),
}
\]

hence

\[
\boxed{
\dot X_R+2\nu R^2X_R
\le
\Sigma_u(R)+\Sigma_u(-R).
}
\]

This makes precise that any singular scenario must continuously recreate high-frequency critical excess on the local parabolic time scale; an isolated finite lock is insufficient.

## 7. Current theorem target

The reduction above does **not** prove global regularity.  The remaining problem is a full-state infinite-dimensional rigidity question.

A sufficient endpoint target is:

> **Full-Core Critical Rigidity.** After quotienting the exact amplitude, dilation, and Euclidean gauge freedoms, no complete normalized orbit of the Core END Flow can satisfy
> \[
> \int_0^T W(v(\tau))\,d\tau\to+\infty
> \]
> while remaining a genuine three-dimensional finite-energy core state.

Equivalently, any dynamically relevant normalized sequence with persistent nonnegative critical drift must compactify strongly enough that the full cubic core pairing \(W(v)\) has no positive defect at infinity.

The exact fixed-point subproblem is:

\[
\boxed{
B(v,v)=b\left(x\cdot\nabla+\frac32\right)v,
\qquad
b>0,
\qquad
\langle v,Cv\rangle=0.
}
\]

Proving that no nonzero finite-energy genuinely three-dimensional full-core solution exists would exclude exact dilation-locked blow-up profiles, but a complete regularity proof must also exclude recurrent/noncompact normalized orbits.

## 8. Claim discipline

### Exact in the stated typed setting

- formation law \(u_t=(\mathcal J_u-\nu C^2)u\);
- critical \(\dot H^{1/2}\) identity;
- self-adjoint critical curvature representation;
- helicity-flip/radial-mismatch identity;
- spectral stress representation;
- amplitude/dilation normalization and modulation equations on \(\mathbb R^3\) or an equivalent rescaled blow-up chart;
- the inviscid Core END Flow as the \(A\to\infty\) normalized limit;
- zero-helicity restriction for recurrent amplifying normalized orbits;
- global regularity of every fixed finite-dimensional closed Galerkin subsystem.

### Open

- exclusion of infinite migrating/recurrent critical locking;
- compactness of all dynamically relevant normalized full-core sequences;
- nonexistence of every zero-helicity dilation-relative full-core profile;
- global regularity of 3D Navier–Stokes.

This folder should therefore be read as a sharp application reduction and theorem target, not as a completed Clay proof.

## 9. Reading order

1. [`CORE_REDUCTION.md`](CORE_REDUCTION.md) — derivation of the normalized full-state flow and exact constraints.
2. [`FORMULA_CHAIN.md`](FORMULA_CHAIN.md) — compact equation-by-equation chain from core datum to the final rigidity target.
3. [`RIGIDITY_TARGET.md`](RIGIDITY_TARGET.md) — theorem statement, anti-models, falsified shortcuts, and the remaining proof gap.
4. Canonical formation theory: [`../../core/metric_lie_hodge/README.md`](../../core/metric_lie_hodge/README.md).
5. Whole-state completeness: [`../../core/spectral_signature/README.md`](../../core/spectral_signature/README.md).
