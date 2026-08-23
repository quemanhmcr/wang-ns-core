# 02 — Critical geometry, constrained-gradient decomposition, helicity sheets

## 1. Energy–helicity leaf and constrained critical gradient

Let

\[
G_u=\Lambda(\Lambda-a-bC)u,
\]

where `a,b` are chosen as the metric projection coefficients making `G_u` tangent to the joint energy–helicity leaf:

\[
\boxed{
\langle u,G_u\rangle=0,
\qquad
\langle Cu,G_u\rangle=0.
}
\]

Define

\[
\boxed{
d_u^2
=\|G_u\|_{H^{-1/2}}^2
=\|\Lambda^{1/2}(\Lambda-a-bC)u\|_2^2.
}
\]

For `d_u>0`, set

\[
\boxed{
\gamma_u=\frac{W_\Lambda}{2d_u^2}.
}
\]

Then the exact orthogonal projection of Formation onto the constrained critical-gradient direction is

\[
\boxed{
N(u)=\gamma_uG_u+T_u.
}
\]

The transverse component satisfies

\[
\boxed{
\langle T_u,u\rangle
=\langle T_u,Cu\rangle
=\langle T_u,\Lambda u\rangle=0.
}
\]

In the natural `H^{-1/2}` metric,

\[
\boxed{
T_u
=\operatorname{orthogonal\ remainder\ of\ }N(u)
\text{ from }
\operatorname{span}\{C^2u,C\Lambda u,\Lambda u\}.
}
\]

Thus `T` is the unique critical-null steering component.

---

## 2. Regression facts

The projection coefficients obey

\[
\boxed{|b|\le1,\qquad a\ge0.}
\]

On finite-energy `R^3`,

\[
d=0,\quad u\ne0
\]

forces pure helicity. Mixed-helicity affine kernels restricted to an exact radial sphere cannot support a nonzero `L^2` field.

If exact Cauchy saturation holds,

\[
T=0,
\]

then

\[
\boxed{
N=\gamma\Lambda(\Lambda-a-bC)u.
}
\]

If additionally

\[
a=0,
\]

then

\[
|b|=1
\]

and the state is pure helicity, so

\[
\boxed{N=0.}
\]

This removes the most dangerous exact saturation branch.

---

## 3. Navier–Stokes modulation normal form

From

\[
N=\gamma G+T
\]

and

\[
G=C^2u-bC\Lambda u-a\Lambda u,
\]

Navier–Stokes becomes

\[
\boxed{
u_t=P_u(C)u+T_u,
}
\]

where

\[
\boxed{
P_u(C)
=(\gamma-\nu)C^2
-\gamma b\,C\Lambda
-\gamma a\,\Lambda.
}
\]

Since `P_u(C)` is always a scalar function of the fixed curl operator,

\[
\boxed{
u(t)
=M(t,s)u(s)
+\int_s^tM(t,r)T_u(r)\,dr,
}
\]

with

\[
M(t,s)
=\exp\left(\int_s^tP_u(r,C)\,dr\right).
\]

Interpretation:

- low finite-step `T` means proximity to a commuting spectral-multiplier module;
- high `T` is genuine non-normal / hypocoercive Formation steering.

---

## 4. Exact heat decomposition in the same metric

Let

\[
R_u^{\rm heat}=a\Lambda u+bC\Lambda u.
\]

Then

\[
\Lambda^2u=G_u+R_u^{\rm heat}.
\]

In the `H^{-1/2}` metric, the projection conditions give

\[
(G,R^{\rm heat})_{-1/2}=0.
\]

The defining properties of `T` also imply

\[
(T,G)_{-1/2}=0,
\qquad
(T,R^{\rm heat})_{-1/2}=0.
\]

Hence

\[
\boxed{
G,\ T,\ R^{\rm heat}
\text{ are pairwise orthogonal in }H^{-1/2}.
}
\]

Because

\[
\|\Lambda^2u\|_{H^{-1/2}}^2=D_3,
\]

we obtain

\[
\boxed{
D_3=d^2+\|R^{\rm heat}\|_{H^{-1/2}}^2.
}
\]

Thus

\[
\boxed{
D_3-d^2
=\|a\Lambda u+bC\Lambda u\|_{H^{-1/2}}^2.
}
\]

This gives a direct geometric meaning to the strict residual-heat gap.

---

## 5. Exact orthogonal splitting of the full viscous velocity

Using

\[
u_t=N-\nu\Lambda^2u,
\]

we get

\[
\boxed{
u_t
=(\gamma-\nu)G+T-\nu R^{\rm heat}.
}
\]

By the orthogonality above,

\[
\boxed{
\|u_t\|_{H^{-1/2}}^2
=(\gamma-\nu)^2d^2
+\|T\|_{H^{-1/2}}^2
+\nu^2(D_3-d^2).
}
\]

So `T` cannot pointwise cancel either the super-viscous constrained-gradient component or the residual heat component in the natural metric. Its role is geometric steering, not direct scalar cancellation.

---

## 6. Critical stock and neutral-cell identity

Let

\[
M=\langle u,\Lambda u\rangle,
\qquad
D_2=\|\Lambda u\|_2^2,
\qquad
D_3=\|\Lambda^{3/2}u\|_2^2.
\]

Since

\[
W_\Lambda=2\gamma d^2,
\]

Navier–Stokes gives

\[
\boxed{
M'=2\gamma d^2-2\nu D_3.
}
\]

The exact inequality

\[
\boxed{
D_3-d^2
\ge
\frac{D_2^2}{M}>0
}
\]

holds on every nonzero nondegenerate state.

Therefore instantaneous critical neutrality

\[
M'=0
\]

occurs at

\[
\boxed{
\gamma=\nu\frac{D_3}{d^2}>\nu.
}
\]

Not at `γ=ν`.

For a finite critically neutral cell,

\[
M(t_1)=M(t_0),
\]

integration gives

\[
\boxed{
\int(\gamma-\nu)d^2
=\nu\int(D_3-d^2)
\ge
\nu\int\frac{D_2^2}{M}>0.
}
\]

Hence every nonzero neutral cell requires strictly super-viscous constrained-gradient creation.

`T` performs no direct critical work and can only act catalytically.

---

## 7. Instantaneous neutral heat angle

Define

\[
\cos^2\vartheta=\frac{d^2}{D_3}.
\]

At exact instantaneous neutrality,

\[
\boxed{
\gamma=\nu\sec^2\vartheta,
\qquad
\gamma-\nu=\nu\tan^2\vartheta.
}
\]

Then

\[
\boxed{
\|u_t\|_{H^{-1/2}}^2
=\|T\|_{H^{-1/2}}^2
+\nu^2D_3\tan^2\vartheta.
}
\]

So critical neutrality does not imply stationarity, even if `T=0`.

---

## 8. Helicity sheets

Write

\[
u=u_++u_-,
\]

and define

\[
C_\pm=\|\Lambda^{1/2}u_\pm\|_2^2,
\qquad
D_\pm=\|\Lambda^{3/2}u_\pm\|_2^2.
\]

Then exactly

\[
\boxed{
\dot C_++2\nu D_+=W_\Lambda/2,
}
\]

\[
\boxed{
\dot C_-+2\nu D_-=W_\Lambda/2.
}
\]

So positive critical creation is injected equally into both helicity sheets.

Also

\[
\boxed{
\langle\Lambda u_+,T_+\rangle
=\langle\Lambda u_-,T_-\rangle=0.
}
\]

Pure helicity is therefore not a persistent positive-growth refuge.

---

## 9. Mixed-helicity triadic necessity

For signed curl roots `x,y,z`, a complete physical triad contributes

\[
W_{\rm tri}=\tau\Theta(x,y,z),
\]

with

\[
\boxed{
\Theta
=\det
\begin{pmatrix}
1&1&1\\
x&y&z\\
|x|&|y|&|z|
\end{pmatrix}.
}
\]

If all three roots have the same sign,

\[
\boxed{\Theta=0.}
\]

Therefore all genuine critical creation has mixed-helicity ancestry somewhere in the physical interaction network.

---

## 10. Status

### EXACT

Everything in Sections 1–9.

### Consequence

A finite-viscosity neutral cell is a nonstationary, strictly super-viscous constrained-gradient process in which `T` must continually steer geometry without doing direct critical work.

### OPEN

The fact that `T` is only catalytic does not yet imply it cannot sustain recurrent regenerative geometry over finite time. That is addressed only after the full semigroup / companion / Floquet reductions.
