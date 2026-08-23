# 10 — Common-ray Poisson depth and transverse `T` coercivity

## Status

This chapter records the latest stationary finite-`κ` frontier.  It strengthens the earlier Gaussian-ray condition into an **all-positive-Poisson-depth family**, derives a first-order depth equation for the transverse component `T`, and obtains a mode-count-independent coercive lower bound for `T` on compact stationary strata.

> **Nonclaim.** None of the statements below proves 3D Navier–Stokes regularity or excludes the full finite-`κ` stationary/Floquet branch.  The remaining theorem is a rank-one/common-state convolution rigidity problem.

All `EXACT` statements are understood on the smooth finite-energy stationary normalized class with the boundary decay needed for the displayed radial integrations by parts.

---

# 1. EXACT — stationary regression rigidity

Assume a nonzero stationary normalized finite-viscosity profile

\[
0=N(v)-\kappa C^2v+\kappa D_2v-\beta\mathcal Lv,
\qquad E=M=1,
\qquad \kappa>0.
\]

Stationarity of `κ` gives

\[
W_\Lambda=2\kappa D_3,
\]

hence

\[
\boxed{\beta=2\kappa D_2.}
\]

Stationarity of normalized helicity gives

\[
\boxed{H_3:=\langle v,C\Lambda^2v\rangle=0.}
\]

Introduce the signed `D_2` moment

\[
Q:=\langle v,C\Lambda v\rangle.
\]

The two projection equations defining `a,b` are

\[
D_2=a+bQ,
\]

\[
H_3=aQ+bD_3.
\]

Since `H_3=0`,

\[
\boxed{
a=\frac{D_2D_3}{D_3-Q^2},
\qquad
b=-\frac{D_2Q}{D_3-Q^2}.
}
\]

The regression residual satisfies

\[
d^2=D_3-aD_2-bH_3,
\]

so on the stationary branch

\[
\boxed{d^2=D_3-aD_2,}
\qquad
\boxed{D_3-d^2=aD_2.}
\]

The existing heat-gap inequality

\[
D_3-d^2\ge D_2^2
\]

therefore yields

\[
\boxed{a\ge D_2.}
\]

Moreover

\[
d^2
=\frac{D_3\bigl(D_3-D_2^2-Q^2\bigr)}{D_3-Q^2}.
\]

Thus `d>0` implies

\[
\boxed{D_3>D_2^2+Q^2.}
\]

Consequently

\[
|b|
=\frac{D_2|Q|}{D_3-Q^2}
<\frac{|Q|}{D_2}
\le1,
\]

and therefore

\[
\boxed{|b|<1.}
\]

So neither helicity sheet lies on the regression-saturation boundary for a nondegenerate stationary finite-`κ` profile.

---

# 2. EXACT — the Gaussian-ray condition extends to every positive Poisson depth

On helicity sheet `σ=±1`, write the stationary radial Fourier amplitude as `f_σ(ρ,ω)`.  The exact stationary radial equation is

\[
\boxed{
\rho\partial_\rho f_\sigma
+\left(2-\frac{\rho^2}{2D_2}\right)f_\sigma
=-\frac{\widehat N_\sigma(\rho,\omega)}{2\kappa D_2}.
}
\]

Put

\[
\tau_*:=\frac1{4D_2}.
\]

Then

\[
\boxed{
\frac d{d\rho}
\left[\rho^2e^{-\tau_*\rho^2}f_\sigma\right]
=-\frac{\rho e^{-\tau_*\rho^2}}{2\kappa D_2}
\widehat N_\sigma.
}
\]

Multiply by `e^{-yρ}`, with `y≥0`, and integrate on the ray.  The boundary terms vanish and integration by parts gives

\[
\boxed{
\int_0^\infty
\rho e^{-\tau_*\rho^2-y\rho}
\widehat N_\sigma(\rho,\omega)\,d\rho
=-2\kappa D_2y
\int_0^\infty
\rho^2e^{-\tau_*\rho^2-y\rho}
f_\sigma(\rho,\omega)\,d\rho.
}
\]

Define the ray-state reader

\[
\boxed{
\mathcal V_\sigma(y,\omega)
:=\int_0^\infty
\rho^2e^{-\tau_*\rho^2-y\rho}
f_\sigma(\rho,\omega)\,d\rho
}
\]

and ray-Formation reader

\[
\boxed{
\mathcal N_\sigma(y,\omega)
:=\int_0^\infty
\rho e^{-\tau_*\rho^2-y\rho}
\widehat N_\sigma(\rho,\omega)\,d\rho.
}
\]

Then the complete stationary ray law is

\[
\boxed{
\mathcal N_\sigma(y,\omega)
=-2\kappa D_2y\,\mathcal V_\sigma(y,\omega)
\qquad(y\ge0).
}
\]

At `y=0` this recovers Gaussian-ray cancellation.  For every `y>0` it is an exact anti-alignment law.

---

# 3. EXACT — common ray-stress eigenrelation

Let

\[
\mathsf R(x):=v(x)\otimes v(x).
\]

The exact output-frequency null form gives, up to the fixed Fourier sign convention,

\[
\widehat N(\rho\omega)
=-i\rho P_\omega\widehat{\mathsf R}(\rho\omega)\omega.
\]

Define

\[
\boxed{
\mathsf S_y(\omega)
:=\int_0^\infty
\rho^2e^{-\tau_*\rho^2-y\rho}
\widehat{\mathsf R}(\rho\omega)\,d\rho.
}
\]

Then

\[
\mathcal N(y,\omega)
=-iP_\omega\mathsf S_y(\omega)\omega,
\]

and the stationary equation is equivalent to

\[
\boxed{
P_\omega\mathsf S_y(\omega)\omega
=-2i\kappa D_2y\,\mathcal V(y,\omega)
\qquad\forall y>0.
}
\]

At `y=0`,

\[
\boxed{P_\omega\mathsf S_0(\omega)\omega=0,}
\]

so the Gaussian ray stress is shear-free.

This is an all-depth common-state convolution constraint, not a one-moment identity.

---

# 4. EXACT — spatial-even stationary profiles are excluded

Suppose the centered stationary profile is spatially even,

\[
v(x)=v(-x).
\]

Then `\widehat v` is real.  Also `v\otimes v` is even, so `\widehat{\mathsf R}` and therefore

\[
P_\omega\mathsf S_y(\omega)\omega
\]

are real.  But

\[
-2i\kappa D_2y\,\mathcal V(y,\omega)
\]

is purely imaginary because `\mathcal V` is real.  Hence both sides vanish for every positive depth.  Laplace uniqueness implies `v=0`.

Therefore

\[
\boxed{
\text{there is no nonzero centered spatially-even stationary finite-}\kappa\text{ profile.}
}
\]

Odd parity is not excluded by this argument.

---

# 5. EXACT — `T` satisfies a first-order Poisson-depth equation

Use

\[
N=\gamma G+T.
\]

On helicity sheet `σ`,

\[
G_\sigma
=\rho\bigl[(1-\sigma b)\rho-a\bigr]f_\sigma.
\]

Define the ray transform of `T`,

\[
\boxed{
\mathcal T_\sigma(y,\omega)
:=\int_0^\infty
\rho e^{-\tau_*\rho^2-y\rho}
\widehat T_\sigma(\rho,\omega)\,d\rho.
}
\]

Since

\[
-\partial_y\mathcal V_\sigma
=\int_0^\infty
\rho^3e^{-\tau_*\rho^2-y\rho}f_\sigma\,d\rho,
\]

we obtain

\[
\mathcal R_y(G_\sigma)
=-(1-\sigma b)\partial_y\mathcal V_\sigma-a\mathcal V_\sigma.
\]

Using

\[
\mathcal N_\sigma
=\gamma\mathcal R_y(G_\sigma)+\mathcal T_\sigma
=-2\kappa D_2y\mathcal V_\sigma,
\]

we get the exact depth ODE

\[
\boxed{
\gamma(1-\sigma b)\partial_y\mathcal V_\sigma
+\bigl(\gamma a-2\kappa D_2y\bigr)\mathcal V_\sigma
=\mathcal T_\sigma.
}
\]

By stationary nondegeneracy,

\[
\boxed{c_\sigma:=\gamma(1-\sigma b)>0}
\]

on both helicity sheets.  Thus this depth equation has no hidden helicity characteristic.

---

# 6. EXACT — the homogeneous depth dynamics is independent of `κ`

Stationarity gives

\[
\gamma=\kappa\frac{D_3}{d^2}.
\]

Divide the depth ODE by `c_σ`.  An integrating factor is

\[
\boxed{
I_\sigma(y)
:=\exp\left[
\frac{a}{1-\sigma b}y
-\frac{D_2d^2}{D_3(1-\sigma b)}y^2
\right].
}
\]

The viscosity cancels from this dimensionless homogeneous depth dynamics.  Exactly,

\[
\boxed{
\frac d{dy}\left(I_\sigma\mathcal V_\sigma\right)
=\frac{I_\sigma}{c_\sigma}\mathcal T_\sigma.
}
\]

The zero of the zeroth-order coefficient occurs at the canonical positive depth

\[
\boxed{
y_c
=\frac{\gamma a}{2\kappa D_2}
=\frac{aD_3}{2D_2d^2}.
}
\]

It is the same for both helicity sheets.  At `y=y_c`,

\[
\boxed{
\mathcal T_\sigma(y_c,\omega)
=\gamma(1-\sigma b)\partial_y\mathcal V_\sigma(y_c,\omega).
}
\]

Thus at one canonical positive Poisson depth the transverse source is purely the depth derivative of the ray-state reader.

---

# 7. EXACT — transverse Poisson-depth passivity

Because `I_σ(y)` decays Gaussianly as `y→∞` and `\mathcal V_σ(y)→0`, integrating from any `y_0≥0` yields

\[
\boxed{
c_\sigma I_\sigma(y_0)\mathcal V_\sigma(y_0,\omega)
=-\int_{y_0}^\infty
I_\sigma(y)\mathcal T_\sigma(y,\omega)\,dy.
}
\]

This is an exact transverse forcing-debt identity.

There is also a signed version.  From the depth ODE,

\[
\frac d{dy}
\left[I_\sigma(y)^2|\mathcal V_\sigma(y)|^2\right]
=\frac{2I_\sigma(y)^2}{c_\sigma}
\operatorname{Re}
\bigl(\overline{\mathcal V_\sigma}\,\mathcal T_\sigma\bigr).
\]

Integrating gives

\[
\boxed{
\int_{y_0}^\infty
I_\sigma(y)^2
\operatorname{Re}
\bigl(\overline{\mathcal V_\sigma}\,\mathcal T_\sigma\bigr)
\,dy
=-\frac{c_\sigma}{2}
I_\sigma(y_0)^2
|\mathcal V_\sigma(y_0)|^2.
}
\]

After integration over `ω`,

\[
\boxed{
\int_{y_0}^\infty
I_\sigma^2
\operatorname{Re}
\langle\mathcal V_\sigma(y),\mathcal T_\sigma(y)\rangle_{L^2(S^2)}
\,dy<0
}
\]

whenever `\mathcal V_σ(y_0)\neq0`.

This is a genuine exact passivity theorem for **`T` itself in Poisson-depth space**.  Although `T` does no critical work on the original state, its canonical Gaussian-Poisson ray action is strictly negative.

---

# 8. EXACT — an `H^{-1/2}` lower bound for `T`

For

\[
\mathcal T_\sigma(y,\omega)
=\int_0^\infty
\rho e^{-\tau_*\rho^2-y\rho}T_\sigma(\rho,\omega)\,d\rho,
\]

Cauchy–Schwarz gives

\[
\boxed{
\|\mathcal T_\sigma(y)\|_{L^2(S^2)}
\le
A_{\tau_*}(y)\,
\|T_\sigma\|_{H^{-1/2}},
}
\]

where

\[
A_{\tau_*}(y)^2
:=\int_0^\infty
\rho e^{-2\tau_*\rho^2-2y\rho}\,d\rho.
\]

Combine this with the forcing-debt identity:

\[
c_\sigma I_\sigma(y_0)
\|\mathcal V_\sigma(y_0)\|_{L^2(S^2)}
\le
\|T_\sigma\|_{H^{-1/2}}
\int_{y_0}^\infty
I_\sigma(y)A_{\tau_*}(y)\,dy.
\]

Therefore

\[
\boxed{
\|T_\sigma\|_{H^{-1/2}}
\ge
\frac{
c_\sigma I_\sigma(y_0)
}{
\displaystyle\int_{y_0}^\infty
I_\sigma(y)A_{\tau_*}(y)\,dy
}
\|\mathcal V_\sigma(y_0)\|_{L^2(S^2)}.
}
\]

The coefficient scales like `κ`; the remaining factor depends only on normalized Theory-2 geometry.

---

# 9. DEDUCTION — finite positive depths yield a uniform stationary `T` gap on compact strata

The family

\[
v\longmapsto
\{\mathcal V_\sigma(y):y>0,\ \sigma=\pm\}
\]

is injective by Laplace uniqueness.  Hence on a compact normalized stationary stratum `\mathcal K`, finitely many positive depths `y_1,\ldots,y_m` give

\[
\boxed{
\sum_{\sigma,j}
\|\mathcal V_\sigma(y_j)\|_{L^2(S^2)}^2
\ge c_{\mathcal K}>0.
}
\]

If the stratum is separated from

\[
d=0,
\qquad
\kappa=0,
\]

and from loss of spectral compactness, then `|b|<1` plus compactness gives

\[
1-|b|\ge\delta_{\mathcal K}>0.
\]

The exact depth estimate therefore yields

\[
\boxed{
\|T\|_{H^{-1/2}}
\ge c'_{\mathcal K}\,\kappa.
}
\]

This is a **mode-count-independent stationary transverse coercivity theorem**.

It is stronger than the earlier conclusion that `T=0` has no stationary solution: on a compact finite-Reynolds stationary branch, `T` has a definite scale-critical size.

---

# 10. EXACT — canonical heat depth is raywise energy-inward and critical-neutral

Fix a ray `(σ,ω)` and put

\[
w_\sigma(\rho,\omega)
:=e^{-\tau_*\rho^2}f_\sigma(\rho,\omega),
\]

\[
F_\sigma(\rho,\omega)
:=e^{-\tau_*\rho^2}\widehat N_\sigma(\rho,\omega).
\]

At `\tau_*=1/(4D_2)`, the radial equation becomes

\[
F_\sigma=-2\kappa D_2(\rho\partial_\rho w_\sigma+2w_\sigma).
\]

With radial `L^2` measure `\rho^2d\rho`, direct integration by parts gives, **ray by ray and helicity sheet by helicity sheet**,

\[
\boxed{
\operatorname{Re}\int_0^\infty
\rho^2\overline{w_\sigma}F_\sigma\,d\rho
=-\kappa D_2
\int_0^\infty\rho^2|w_\sigma|^2\,d\rho,
}
\]

and

\[
\boxed{
\operatorname{Re}\int_0^\infty
\rho^3\overline{w_\sigma}F_\sigma\,d\rho
=0.
}
\]

Thus at the canonical heat depth the smoothed original Formation is simultaneously

\[
\boxed{\text{strictly energy-inward}}
\]

and

\[
\boxed{\text{critical-neutral}}
\]

on every active ray.

---

# 11. EXACT — every active ray pays a radial-variance debt

For one ray/sheet define

\[
E_{\omega\sigma}
:=\int\rho^2|w|^2d\rho,
\]

\[
M_{\omega\sigma}
:=\int\rho^3|w|^2d\rho,
\]

\[
D_{\omega\sigma}
:=\int\rho^4|w|^2d\rho.
\]

Let

\[
\bar\rho_{\omega\sigma}:=\frac{M_{\omega\sigma}}{E_{\omega\sigma}},
\]

and conditional radial variance

\[
\mathsf V_{\omega\sigma}
:=D_{\omega\sigma}-\frac{M_{\omega\sigma}^2}{E_{\omega\sigma}}.
\]

Using the two canonical-depth identities,

\[
\kappa D_2M_{\omega\sigma}
=
\left|
\operatorname{Re}
\langle(\Lambda-\bar\rho_{\omega\sigma})w,F\rangle
\right|.
\]

Hence Cauchy–Schwarz gives

\[
\boxed{
\sqrt{\mathsf V_{\omega\sigma}}\,
\|F_{\omega\sigma}\|_{L^2(\rho^2d\rho)}
\ge
\kappa D_2M_{\omega\sigma}.
}
\]

A stationary finite-`κ` profile therefore cannot be radially mono-spectral even ray by ray.

---

# 12. DEDUCTION — compact stationary profiles have a uniform raywise radial-spread gap

Sum the preceding estimate over directions and helicity sheets.  With

\[
M_{\tau_*}:=\|\Lambda^{1/2}e^{-\tau_*\Lambda^2}v\|_2^2,
\]

and total conditional radial variance `\mathsf V_{\rm ray}`, one obtains

\[
\kappa D_2M_{\tau_*}
\le
\sqrt{\mathsf V_{\rm ray}}\,
\|e^{-\tau_*\Lambda^2}N(v)\|_2.
\]

The output-frequency null form gives

\[
|\widehat N(k)|\lesssim |k|\,\|v\|_2^2,
\]

and therefore

\[
\|e^{-\tau_*\Lambda^2}N(v)\|_2
\lesssim \tau_*^{-5/4}
\sim D_2^{5/4}
\]

under `E(v)=1`.

Hence

\[
\boxed{
\mathsf V_{\rm ray}
\gtrsim
\kappa^2D_2^{-1/2}M_{\tau_*}^2.
}
\]

On a compact stationary family with

\[
\kappa\ge\kappa_0>0,
\qquad
D_2\le D_*,
\]

one also has a positive lower bound for `M_{\tau_*}` from `E=M=1`; for example a fixed fraction of the critical measure lies below a multiple of its `D_2` mean.  Thus

\[
\boxed{
\mathsf V_{\rm ray}
\ge c(\kappa_0,D_*)>0.
}
\]

So a compact stationary finite-Reynolds counterexample must retain a definite amount of raywise radial spread; it cannot converge to a thin-shell state while remaining in that compact stratum.

---

# 13. EXACT — the generic infrared tail is entirely transverse

Let

\[
\mathsf R_0:=\int_{\mathbb R^3}v(x)\otimes v(x)\,dx.
\]

Since `v\in L^2`, `v\otimes v\in L^1`, so its Fourier transform is continuous at zero.  Therefore

\[
\widehat N(\rho\omega)
=-i\rho P_\omega\mathsf R_0\omega+o(\rho).
\]

The exact stationary Green/radial equation then gives

\[
\boxed{
\widehat v(\rho\omega)
=\frac{i\rho}{6\kappa D_2}
P_\omega\mathsf R_0\omega
+o(\rho).
}
\]

For this tail,

\[
G=O(\rho^2),
\]

whereas

\[
N=-i\rho P_\omega\mathsf R_0\omega+o(\rho).
\]

Hence

\[
\boxed{
\widehat T(\rho\omega)
=-i\rho P_\omega\mathsf R_0\omega+o(\rho).
}
\]

Unless

\[
\mathsf R_0\propto I,
\]

the leading normalized infrared ancestry is explicitly and entirely transverse.  The isotropic-stress case suppresses this first-order tail and forms a separate residual sub-branch.

---

# 14. The remaining stationary theorem — common-ray Formation rigidity

A stationary nondegenerate finite-`κ` profile must satisfy simultaneously

\[
\boxed{
P_\omega
\left[
\int_0^\infty
\rho^2e^{-\rho^2/(4D_2)-y\rho}
\widehat{v\otimes v}(\rho\omega)\,d\rho
\right]\omega
=-2i\kappa D_2y
\int_0^\infty
\rho^2e^{-\rho^2/(4D_2)-y\rho}
\widehat v(\rho\omega)\,d\rho
}
\]

for every

\[
y>0,
\qquad
\omega\in S^2,
\]

together with

\[
E=M=1,
\qquad
H_3=0,
\qquad
d>0,
\qquad
|b|<1,
\]

reality, polarized Curl–Killing, and physical rank-one companion completion.

The corresponding transverse depth equation is

\[
\boxed{
\gamma(1-\sigma b)\partial_y\mathcal V_\sigma
+(\gamma a-2\kappa D_2y)\mathcal V_\sigma
=\mathcal T_\sigma,
}
\]

with exact signed passivity

\[
\boxed{
\int I_\sigma^2
\operatorname{Re}\langle\mathcal V_\sigma,\mathcal T_\sigma\rangle\,dy<0
}
\]

for every active sheet/reader.

The residual stationary mechanism is therefore:

\[
\boxed{
\begin{aligned}
&\textbf{a common quadratic ray-stress eigenstate across every positive}\
&\textbf{Poisson depth, whose transverse component simultaneously solves}\
&\textbf{a coercive first-order depth equation on both helicity sheets.}
\end{aligned}
}
\]

---

# 15. Hostile checks and exact scope

## 15.1 Laplace injectivity is not a global coercive gap

The map

\[
f(\rho)\mapsto
\int_0^\infty
\rho^2e^{-\tau_*\rho^2-y\rho}f(\rho)\,d\rho
\]

is injective in the full positive-depth family, but finitely many depths have no global lower bound on the critical space.  Rapid radial phase/scale radiation can make a fixed finite reader set small.

Therefore the finite-depth `T` gap is an **interior compactness theorem**; its constant may degenerate at a terminal radial/phase loss of compactness.

## 15.2 Tensor tomography alone is insufficient

The abstract map

\[
\mathsf R\mapsto P_\omega\mathsf S_y(\omega)\omega
\]

has a large kernel; e.g. isotropic tensors satisfy `P_\omega(I\omega)=0`.  The proof cannot replace the physical tensor by an arbitrary tensor field.

The decisive remaining structure is that

\[
\mathsf R=v\otimes v
\]

comes from the same actual state, with reality companions, rank-one convolution completion, and Curl–Killing constraints.

---

# 16. Updated theorem ledger

## EXACT

1. Stationary regression gives `β=2κD_2`, `H_3=0`, explicit `a,b`, and `|b|<1`.
2. Gaussian-ray cancellation extends to the entire positive Poisson-depth family.
3. Physical convolution yields the common ray-stress eigenrelation.
4. Nonzero centered spatially-even stationary finite-`κ` profiles are excluded.
5. `T` satisfies a first-order Poisson-depth ODE with positive derivative coefficient on both helicity sheets.
6. The homogeneous depth equation is `κ`-independent after normalization.
7. The transverse depth action has an exact negative signed work identity.
8. The ray transform yields an explicit `H^{-1/2}` lower bound for `T`.
9. Canonical heat depth is raywise energy-inward and critical-neutral.
10. Every active ray obeys a radial-variance debt.
11. The generic first infrared tail is entirely transverse.

## DEDUCTION

1. Compact nondegenerate stationary strata have a mode-count-independent lower bound `\|T\|_{H^{-1/2}}\gtrsim_{\mathcal K}\kappa`.
2. Compact finite-Reynolds stationary strata have a positive raywise radial-spread gap.

## AUDIT / GUARD

- All-positive-depth Laplace injectivity does not by itself yield a global critical spectral gap.
- Abstract tensor tomography is too weak; one must exploit the physical rank-one/common-state origin `v\otimes v`.

## OPEN

### Common-ray Formation rigidity

Classify the common-state solutions of the all-depth ray-stress eigenrelation under the simultaneous Theory-2 constraints.  If compact solutions reduce only to the already-classified null/collinear/thin-shell limits, the stationary finite-Reynolds branch is excluded.

For periodic Floquet recurrence, the corresponding open theorem is the time-ordered version in which the right-hand side is the propagated transverse source of the weighted shift.

---

# 17. Repackaging assessment

This update adds genuine coercive content:

\[
\boxed{\text{bounded-module finite-step passivity}},
\]

\[
\boxed{\text{actual-state covariance visibility/passivity}},
\]

\[
\boxed{\text{stationary transverse }T\text{-coercivity}},
\]

and

\[
\boxed{\text{raywise helicity-resolved radial-spread coercivity}}.
\]

The remaining place where full endpoint difficulty may survive is much narrower:

\[
\boxed{
\text{rank-one self-consistency of the common ray-stress eigenrelation.}
}
\]

A finite, mode-count-independent companion estimate for this common-ray relation would constitute a genuine analytic closure step rather than a change of language.  No such final estimate is proved here.
