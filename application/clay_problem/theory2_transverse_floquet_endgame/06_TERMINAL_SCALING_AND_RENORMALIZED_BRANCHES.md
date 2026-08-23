# 06 — Terminal scaling, critical Reynolds, and renormalized branches

## 1. Exact terminal scaling

Write a boundary profile as

\[
u=\alpha\mathcal S_r z,
\qquad
(\mathcal S_rz)(x)=rz(rx).
\]

After the Formation time change

\[
\tau=\alpha r^2\theta,
\]

the profile equation becomes

\[
\boxed{
z_\tau=N(z)-\frac{\varepsilon}{\alpha}C^2z.
}
\]

Thus absolute frequency `r` cancels from the Formation/heat ratio.

The true dimensionless parameter is

\[
\boxed{\alpha/\varepsilon.}
\]

Hence the three regimes are:

\[
\alpha/\varepsilon\gg1
\quad\text{Euler / Formation dominated},
\]

\[
\alpha/\varepsilon\sim1
\quad\text{finite-viscosity critical profile},
\]

\[
\alpha/\varepsilon\ll1
\quad\text{heat dominated}.
\]

There is no universal dissipation frequency.

Low/high `T` is invariant under this rescaling.

---

## 2. Exact scaling of critical work and heat

Under the same scaling,

\[
M(u)=\alpha^2M(z),
\]

\[
D_3(u)=\alpha^2r^2D_3(z),
\]

and

\[
W_\Lambda(u)=\alpha^3r^2W_\Lambda(z).
\]

Therefore

\[
\boxed{
\frac{W_\Lambda(u)}{2\varepsilon D_3(u)}
=
\frac\alpha\varepsilon
\frac{W_\Lambda(z)}{2D_3(z)}.
}
\]

Any terminal theorem must therefore be critical-Reynolds, not frequency-threshold based.

---

## 3. Conditional critical-Reynolds concentration lemma

Suppose a profile decomposition has pieces

\[
u_j=\alpha_j\mathcal S_{r_j}z_j
\]

whose normalized shapes stay in a compact class on which

\[
\frac{W_\Lambda(z_j)_+}{2D_3(z_j)}\le R_*.
\]

Assume the cubic Formation work and `D_3` decouple asymptotically across profiles.

Then

\[
\sum_jW_\Lambda(u_j)
\le
2R_*
\left(\sup_j\frac{\alpha_j}{\varepsilon}\right)
\varepsilon\sum_jD_3(u_j).
\]

So a regenerative neutral defect forces

\[
\boxed{
\limsup_j\frac{\alpha_j}{\varepsilon}
\ge\frac1{R_*}.
}
\]

Therefore heat-dominated dust cannot regenerate if self-profile Formation decouples.

If every extracted profile has

\[
\alpha_j/\varepsilon\to0,
\]

then a nonzero defect requires either loss of compactness of the normalized shapes or leading cross-profile Formation work.

This is a **DEDUCTION**, not a one-bubble theorem.

---

## 4. Renormalized Euler branch

On finite-energy `R^3`, normalize

\[
E(v)=M(v)=1.
\]

Let

\[
\mathcal L=\frac32+x\cdot\nabla
\]

be the energy-preserving dilation generator.

The inviscid normalized flow is

\[
\boxed{
v_\theta=N(v)-W_\Lambda(v)\mathcal Lv.
}
\]

For helicity

\[
h=\langle v,Cv\rangle,
\]

scaling gives

\[
2\langle Cv,\mathcal Lv\rangle=h,
\]

and Euler Formation preserves helicity, hence

\[
\boxed{h'=-W_\Lambda h.}
\]

A recurrent component with positive mean scale exponent therefore has

\[
\boxed{h=0.}
\]

On finite-energy `R^3`, this implies `d>0` for a nonzero normalized state.

A compact positive-exponent recurrent Euler component would correspond to a type-II terminal concentration with

\[
M(t)\sim(T-t)^{-2/5},
\]

\[
\ell(t)\sim(T-t)^{2/5},
\]

\[
|u|_{\rm core}\sim(T-t)^{-3/5},
\]

\[
|\nabla u|_{\rm core}\sim(T-t)^{-1}.
\]

Nothing currently proved excludes this high-`T` Euler recurrence.

---

## 5. Exact Euler `T` normal form

Recall

\[
N=\gamma G+T,
\qquad
\gamma=\frac W{2d^2}.
\]

On

\[
E=M=1,
\qquad
h=0,
\]

scaling identities give

\[
2\langle\Lambda v,\mathcal Lv\rangle=1,
\]

\[
2\langle Cv,\mathcal Lv\rangle=0,
\]

\[
2\langle v,\mathcal Lv\rangle=0.
\]

In `H^{-1/2}`,

\[
(G,\mathcal Lv)_{-1/2}=\frac12.
\]

Define

\[
\boxed{
R_v^{\rm dil}
=\mathcal Lv-\frac{G_v}{2d_v^2}.
}
\]

Then

\[
(G,R^{\rm dil})_{-1/2}=0
\]

and the renormalized Euler equation becomes

\[
\boxed{
v_\theta=T_v-W_\Lambda(v)R_v^{\rm dil}.
}
\]

The tangential dilation field is tangent to energy, helicity and critical normalization.

---

## 6. Exact nonexistence of `R^{dil}=0` finite-energy states

If

\[
R^{\rm dil}=0,
\]

then

\[
\mathcal Lv
=
\frac1{2d^2}\Lambda(\Lambda-a-bC)v.
\]

In helical Fourier variables

\[
C=\sigma\rho,
\qquad\sigma=\pm1,
\]

each amplitude solves

\[
-\left(\frac32+\rho\partial_\rho\right)f_\sigma
=
\left[
\frac{1-b\sigma}{2d^2}\rho^2
-
\frac a{2d^2}\rho
\right]f_\sigma.
\]

Thus

\[
\boxed{
f_\sigma(\rho,\omega)
=A_\sigma(\omega)\rho^{-3/2}
\exp\left[
-\frac{1-b\sigma}{4d^2}\rho^2
+\frac a{2d^2}\rho
\right].
}
\]

Near `ρ=0`, nonzero solutions behave as `ρ^{-3/2}`. The Fourier `L^2` measure produces

\[
|f|^2\rho^2d\rho\sim\frac{d\rho}{\rho},
\]

which diverges.

Hence

\[
\boxed{
R^{\rm dil}=0,\quad v\in L^2
\Longrightarrow v=0.
}
\]

So a compact positive-`W` Euler recurrence cannot be low-`T` saturation; genuine transverse dynamics is required.

---

## 7. Doubly normalized finite-viscosity flow

Now normalize finite-viscosity `R^3` dynamics by

\[
E(v)=M(v)=1.
\]

Write

\[
u(t)=\alpha(t)\mathcal S_{r(t)}v(\theta).
\]

Since

\[
E(u)=\frac{\alpha^2}{r},
\qquad
M(u)=\alpha^2,
\]

we have canonically

\[
\boxed{
\alpha=\sqrt{M(u)},
\qquad
r=\frac{M(u)}{E(u)}.
}
\]

Take

\[
\frac{d\theta}{dt}=\alpha r^2,
\qquad
\kappa=\frac\nu\alpha.
\]

Then exactly

\[
\boxed{
v_\theta
=N(v)-\kappa C^2v+\kappa D_2v-\beta\mathcal Lv,
}
\]

where

\[
\boxed{
\beta=W_\Lambda-2\kappa(D_3-D_2).
}
\]

The scale equations are

\[
\boxed{
(\log\alpha)_\theta
=\frac12(W_\Lambda-2\kappa D_3),
}
\]

\[
\boxed{
(\log r)_\theta
=\beta,
}
\]

and

\[
\boxed{
(\log\kappa)_\theta
=-\frac12(W_\Lambda-2\kappa D_3).
}
\]

This is the exact finite-Reynolds counterpart of the Euler renormalized flow.

---

## 8. Exact positive scale drift of a neutral finite-viscosity cycle

For a critically neutral cell,

\[
M(t_1)=M(t_0),
\]

so `α` and `κ` return to the same endpoint values. Integrating the amplitude equation gives

\[
\int W_\Lambda\,d\theta
=2\int\kappa D_3\,d\theta.
\]

Insert into the scale equation:

\[
\boxed{
\Delta\log r
=2\int\kappa D_2\,d\theta>0.
}
\]

Since `E=M=1`, Cauchy gives

\[
D_2\ge1,
\]

hence

\[
\boxed{
\Delta\log r
\ge2\int\kappa\,d\theta.
}
\]

So every nonzero finite-viscosity neutral cycle advances toward smaller physical scales.

---

## 9. Parabolic finite-Reynolds recurrence branch

If a normalized finite-`κ` orbit is exactly periodic with period `P`, then

\[
B=2\int_0^P\kappa D_2\,d\theta>0
\]

and each normalized cycle multiplies the physical frequency scale by `e^B`.

Physical cycle lengths shrink geometrically, so cycles accumulate at a finite physical time. At equal normalized phases,

\[
\boxed{
r(t)\asymp(T-t)^{-1/2},
}
\]

\[
\boxed{\ell(t)\asymp(T-t)^{1/2},}
\]

\[
\boxed{|u|_{\rm core}\asymp(T-t)^{-1/2},}
\]

\[
\boxed{|\nabla u|_{\rm core}\asymp(T-t)^{-1}.}
\]

This is a distinct finite-viscosity parabolic recurrence branch. It is not excluded by the current theory.

---

## 10. `T=0` cannot support finite-Reynolds normalized recurrence

If `T=0`, the stationary normalized Fourier equation has infrared leading behavior

\[
\rho\partial_\rho f+2f=O(\rho)f,
\]

so the homogeneous solution is

\[
\boxed{f(\rho)\sim\rho^{-2}.}
\]

This is not `L^2` because

\[
|f|^2\rho^2d\rho\sim\rho^{-2}d\rho.
\]

Hence there is no nonzero stationary finite-energy finite-`κ` normalized profile with `T=0`.

The same radial characteristic over an exact period produces

\[
f(q\rho)\sim q^{-2}f(\rho),
\qquad q=e^{-B}<1,
\]

and therefore no finite-energy periodic normalized orbit with `T\equiv0`.

Thus any compact finite-Reynolds recurrence is necessarily genuinely transverse.

---

## 11. Terminal branch ledger

### Branch A — Euler dominated

\[
\kappa\to0
\quad\Leftrightarrow\quad
\alpha/\nu\to\infty.
\]

Compact positive-exponent renormalized Euler recurrence remains **OPEN**.

### Branch B — compact finite-Reynolds recurrence

`κ` stays in a positive compact interval, but normalized shape recurs. Then exact positive scale drift gives parabolic physical concentration and `T` must continually replenish relative spectral shape. Existence/nonexistence is **OPEN**.

### Branch C — normalized loss of compactness

Infrared skinny ancestry (`ρ↓0`) or broadband/log-scale Formation radiation (`R↑∞`). This may be profile-distributed rather than one positive-mass bubble.

---

## 12. Status

The terminal problem is no longer organized by absolute frequency. It is organized by critical Reynolds `α/ν`, normalized recurrence, and whether `T` can continually replenish spectral structure against exact positive scale drift.
