# 03 — Spectral flags, Poisson/heat cocycles, actual-state visibility

## 1. Polarized Curl–Killing identity

The exact polarized null structure is

\[
\boxed{
J_a(Cb)+J_b(Ca)=0.
}
\]

If

\[
Ca=xa,
\qquad
Cb=yb,
\]

then

\[
\boxed{
2B(a_x,b_y)
=(x-y)P(b_y\times a_x).
}
\]

Hence same signed-curl-root interactions vanish exactly:

\[
\boxed{x=y\Longrightarrow B(a_x,b_x)=0.}
\]

This is the polarized Curl–Killing mechanism. It must be preserved in every physical truncation or symbolic argument.

---

## 2. Full shifted curl flag representation

Euler Formation has the exact shifted-flag representation

\[
\boxed{
N(u)
=-\frac12\int_{\mathbb R}P(H_au\times u)\,da
=-\int_{\mathbb R}P(u_+^a\times u_-^a)\,da.
}
\]

Thus the complete spectral flag is the Theory-2 replacement for any historical scalar control-volume architecture.

The representation makes mixed signed-root interaction explicit and preserves all angular/vector information until a later scalar reader is genuinely needed.

---

## 3. Finite Poisson Formation covariance

Let

\[
P_y=e^{-y\Lambda}.
\]

Define

\[
\boxed{
\Pi_y(u)=P_yJ_u-J_{P_yu}P_y.
}
\]

At a matrix incidence with probe/input frequency `p`, state frequency `η`, and output

\[
k=p+\eta,
\]

the scalar defect multiplier is

\[
\boxed{
e^{-y|k|}-e^{-y(|p|+|\eta|)}.
}
\]

The cocycle law is

\[
\boxed{
\Pi_{y+s}(u)
=P_s\Pi_y(u)+\Pi_s(P_yu)P_y.
}
\]

Its infinitesimal covariance is

\[
\boxed{
\Gamma_\Lambda(u)
=J_{\Lambda u}-[\Lambda,J_u].
}
\]

Adjoint parity:

\[
\boxed{
\Gamma_\Lambda^{\rm sk}=J_{\Lambda u},
\qquad
\Gamma_\Lambda^{\rm sa}=-[\Lambda,J_u].
}
\]

Critical work sees only the self-adjoint half:

\[
\boxed{
W_\Lambda=-\langle u,\Gamma_\Lambda u\rangle.
}
\]

---

## 4. True-heat Formation covariance

Let

\[
H_\tau=e^{-\tau C^2}=e^{-\tau\Lambda^2}.
\]

Define

\[
\boxed{
\mathcal C_\tau(u)
=H_\tau J_u-J_{H_\tau u}H_\tau.
}
\]

Its matrix defect multiplier is

\[
\boxed{
e^{-\tau|p+\eta|^2}
-e^{-\tau(|p|^2+|\eta|^2)}.
}
\]

The heat resonance surface is

\[
\boxed{p\cdot\eta=0.}
\]

At that surface the forward true-heat covariance of the corresponding incidence vanishes instantaneously. Later reverse/companion analysis shows this is not a dynamically invariant refuge.

---

## 5. Exact finite covariance parity

For either

\[
S=P_y
\quad\text{or}\quad
S=H_\tau,
\]

set

\[
\mathfrak C_S(u)=SJ_u-J_{Su}S.
\]

Then exactly

\[
\boxed{
\mathfrak C_S^{\rm sa}
=\frac12\bigl([S,J_u]+[S,J_{Su}]\bigr),
}
\]

\[
\boxed{
\mathfrak C_S^{\rm sk}
=\frac12\{S,J_{(I-S)u}\}.
}
\]

On the mean-zero periodic or finite-energy `R^3` class,

\[
\boxed{
\mathfrak C_S^{\rm sk}=0
\iff
u=0.
}
\]

The complete finite covariance is therefore structurally state-complete.

However same-state scalar spectral balances erase part of the symmetric paired state-frequency channel. This is an exact reason no scalar moment hierarchy can recover the complete Formation state.

---

## 6. Actual-state Poisson cocycle is qualitatively complete

The actual-state vector is

\[
\boxed{
\Pi_y(u)u=P_yN(u)-N(P_yu).
}
\]

At Fourier output `k`,

\[
\boxed{
N_k
=\lim_{y\to\infty}
e^{y|k|}[\Pi_y(u)u]_k.
}
\]

Reason: after multiplying by `e^{y|k|}`, only incidences satisfying the triangle equality

\[
|k|=|p|+|\eta|
\]

survive. Those are collinear same-direction incidences, and incompressibility / Leray projection kills them.

Therefore

\[
\boxed{
\Pi_y(u)u=0\ \forall y>0
\Longrightarrow
N(u)=0.
}
\]

This is a major actual-state uniqueness theorem. Independent-probe operator flatness is unnecessary for qualitative visibility.

---

## 7. Adding true heat identifies harmless trajectories

If in addition

\[
\mathcal C_\tau(u)u=0
\qquad\forall\tau>0,
\]

then

\[
N(H_\tau u)=0
\qquad\forall\tau>0.
\]

Therefore the exact Navier–Stokes trajectory is

\[
\boxed{
u(t)=e^{-\nu tC^2}u(0).}
\]

So the common zero set of the full actual-state Poisson/heat families is heat-stable and harmless.

### Compactness consequence

On a compact normalized stratum separated from this harmless set, finitely many positive depths give a uniform vector observation gap.

This settles the **visibility** side.

It does not settle passivity/sign.

---

## 8. Poisson Formation covariance is subordinated to true heat

Using the subordination formula

\[
P_y=\int_0^\infty H_t\,d\mu_y(t),
\]

let

\[
v_t=H_tu,
\qquad
\bar v=P_yu.
\]

Then exactly

\[
\boxed{
\Pi_y(u)u
=
\int\mathcal C_t(u)u\,d\mu_y(t)
+
\frac12\iint
B(v_t-v_s,v_t-v_s)
\,d\mu_y(t)d\mu_y(s).
}
\]

Thus Poisson covariance consists entirely of:

1. true-heat Formation covariance;
2. Formation of the heat-spread variance.

No new observable is needed.

---

## 9. Moving heat-depth identity

Let

\[
\tau(t)=\tau_0+\nu(t_1-t),
\qquad
v(t)=H_{\tau(t)}u(t).
\]

Then the explicit heat derivative cancels viscosity and one obtains

\[
\boxed{
v_t=N(v)+\mathcal C_{\tau(t)}(u)u.
}
\]

This is an exact finite-step interpretation of the heat covariance: it is the forcing required to make heat smoothing commute with the actual Navier–Stokes Formation trajectory.

For mixed smoothing

\[
S_{y,\tau}=P_yH_\tau,
\]

the same argument gives

\[
\boxed{
(v_y)_t
=N(v_y)+\mathfrak C_{S_{y,\tau(t)}}(u)u.
}
\]

This dynamic interpretation is central later in the adaptive-depth finite-step argument.

---

## 10. Fractional heat-covariance reader for critical work

The fractional representation

\[
\Lambda
=\frac1{2\sqrt\pi}
\int_0^\infty(I-H_t)t^{-3/2}\,dt
\]

and `⟨u,N(u)⟩=0` give

\[
\boxed{
W_\Lambda(u)
=-\frac1{\sqrt{2\pi}}
\int_0^\infty
\tau^{-3/2}
\langle H_\tau u,\mathcal C_\tau(u)u\rangle
\,d\tau.
}
\]

Hence positive critical creation forces a negative oriented heat-covariance pairing at at least one depth.

Applying Cauchy–Schwarz in `τ` gives the scale-correct square-function lower bound

\[
\boxed{
\int_0^\infty
\tau^{-5/2}
\|\mathcal C_\tau(u)u\|_{H^{-1/2}}^2
\,d\tau
\ge
2\sqrt{2\pi}
\frac{W_\Lambda(u)^2}{\|u\|_2^2}.
}
\]

Under critical scaling both sides have the same homogeneity.

So large critical creation forces quantitatively large all-depth actual-state heat-covariance action.

---

## 11. Status

### EXACT

All finite covariance identities, actual-state zero-set theorem, subordination, moving heat-depth equation, and fractional heat reader.

### DEDUCTION

Finite depth gives uniform vector observability on compact interior strata.

### OPEN

Observability does not imply a dissipative return sign. That requires physical companion completion, reverse pairing and finite-time coercivity developed in the next chapters.
