# 11 — Transverse saturation: exact core and superseded additive frontier

## Status

This chapter now serves two purposes:

1. preserve the exact stationary saturation reduction;
2. record which earlier additive companion strategies have been **superseded** by the absorption-reset analysis in `13_ABSORPTION_RESET_AND_FINITE_COMPANION_HOLONOMY.md`.

The current frontier is **not** companion nonconcentration / interaction-to-occupation by itself. The deeper obstruction is quadratic companion export followed by linear finite-viscosity absorption and subcritical nonlinear regeneration.

> **Nonclaim.** Stationary finite-`κ` saturation rigidity remains OPEN.

---

# 1. EXACT — stationary residual and saturation

Write

\[
Y_v=\Lambda^2v-D_2v+2D_2\mathcal Lv,
\qquad
R_{\rm fv}=Y_v-\frac{D_3}{d^2}G_v.
\]

On the stationary scalar stratum

\[
W=2\kappa D_3,
\qquad
\gamma=\kappa\frac{D_3}{d^2},
\]

one has

\[
\boxed{N-\kappa Y=T-\kappa R_{\rm fv}.}
\]

More generally,

\[
\boxed{
\|N-\mu Y\|_{H^{-1/2}}^2
=
\|T-\mu R_{\rm fv}\|_{H^{-1/2}}^2
+
\frac{(W/2-\mu D_3)^2}{d^2}.
}
\]

Therefore stationarity is exactly

\[
\boxed{T=\kappa R_{\rm fv}.}
\]

The transverse residual itself has the Pythagorean decomposition

\[
\boxed{
\begin{aligned}
\|T-\kappa R\|_{-1/2}^{2}
={}&
(\|T\|_{-1/2}-\kappa\|R\|_{-1/2})^2\\
&+2\kappa\|T\|_{-1/2}\|R\|_{-1/2}(1-\cos\vartheta).
\end{aligned}}
\]

Thus either an angle defect or a gain defect is sufficient.

---

# 2. EXACT — `R_{\rm fv}` has no nonzero finite-energy kernel

On helicity sheet `σ=±1`, with `r=D_3/d^2`,

\[
\widehat{R_{\rm fv}}_\sigma
=
-2D_2\rho\partial_\rho f_\sigma
+
\left(
[1-r(1-\sigma b)]\rho^2+ra\rho-4D_2
\right)f_\sigma.
\]

If `R_{\rm fv}(v)=0`, the raywise homogeneous solution behaves as

\[
f_\sigma(\rho,\omega)\sim C_\sigma(\omega)\rho^{-2}
\qquad(\rho\downarrow0),
\]

which is not finite energy unless `C_\sigma=0`. First-order uniqueness then gives

\[
\boxed{R_{\rm fv}(v)=0,\ v\in L^2\Longrightarrow v=0.}
\]

On compact graph-topology normalized classes where `R_{\rm fv}` is continuous,

\[
\inf_{\mathcal K}\|R_{\rm fv}\|_{H^{-1/2}}>0.
\]

Hence denominator degeneration is not the hard issue.

---

# 3. EXACT — saturation implies Fourier-support closure

Because `G`, `Y`, and `R_{\rm fv}` are Fourier-local multiplier/radial-differential expressions,

\[
\operatorname{supp}G,
\operatorname{supp}Y,
\operatorname{supp}R_{\rm fv}
\subseteq
\operatorname{supp}v.
\]

Therefore exact saturation gives

\[
N=\gamma G+\kappa R_{\rm fv}
\]

and hence

\[
\boxed{\operatorname{supp}N(v)\subseteq\operatorname{supp}v.}
\]

Finite completed spectral networks cannot realize this nonexceptionally. Continuum states can evade support export through already occupied tails, so support closure alone is not a PDE contradiction.

---

# 4. EXACT — finite completed networks remain rigid

For a finite completed nonexceptional physical network, reality companions, unequal-shell rigidity, and actual-state rank-one completion rule out

\[
T=\lambda R_{\rm fv},
\qquad
\lambda>0.
\]

This finite theorem remains valid and important.

What has changed is the inference to the continuum: finite-network nonclosure at every depth does **not** imply a uniform infinite-depth gap, because terminal defects may shrink to zero under finite-viscosity absorption.

---

# 5. EXACT — rank-one propagation applies only inside nonlinear cancellation

If same-output diagonal incidences cancel,

\[
Z_{ij}=A_iB_j
\]

and

\[
\boxed{
\sum_{i\ne j}|A_iB_j|^2
\ge
\sum_i|A_iB_i|^2.
}
\]

Thus raw companion mass cannot disappear while the mechanism stays inside nonlinear Formation cancellation.

The crucial limitation is now explicit:

\[
\boxed{
\text{rank-one mass propagation stops when a companion output is absorbed into }\kappa R_{\rm fv}.
}
\]

After linear absorption there is no theorem forcing another nonlinear canceller of comparable size.

---

# 6. SUPERSEDED — continuum laminate as the unique final obstruction

Earlier versions of this chapter treated

\[
\text{increasingly fine angular/radial companion laminate}
\]

as the unique stationary obstruction.

That diagnosis is incomplete.

The continuum phase/compact-operator singular-sequence issue is real, but even if one grants a perfect mode-independent one-generation companion-output theorem, an ancestry can still extinguish through

\[
\boxed{
\text{nonlinear export}
\to
\text{linear finite-viscosity absorption}
\to
\text{smaller nonlinear regeneration}.
}
\]

Therefore the angular laminate is no longer the deepest obstruction.

---

# 7. SUPERSEDED — interaction-to-occupation as a sufficient final theorem

Earlier target:

\[
\text{completed companion interaction mass}
\Longrightarrow
\text{finite-depth occupied mass or angle/gain defect}
\]

is **not sufficient by itself**.

Even if each generation pays occupation mass, one may have

\[
m_{n+1}=q m_n,
\qquad
0<q<1,
\]

so

\[
\sum_n(m_n-m_{n+1})<\infty
\]

while `m_n→0`.

Thus bounded occupation packing does not exclude geometric extinction.

The same warning applies to any companion functional `\mathfrak M_{\rm comp}` that only converts interaction into additive occupation cost.

---

# 8. SUPERSEDED — finite-jet / finite-reader coercivity as a stand-alone route

On localized continuum incidence fibers, finite physical companion maps with finitely many smooth Poisson/heat weights are compact in the dangerous oscillatory factor variable.

Therefore finite readers cannot be bounded below on unrestricted infinite-dimensional hidden-cancellation spheres.

Finite jets/readers become useful only after a separate hereditary/projective compactness or finite-dimensional physical rigidity has been proved. They cannot supply that rigidity themselves.

---

# 9. Current stationary target

The current frontier is recorded in Chapter 13.

The additive question

\[
\text{how much mass survives each generation?}
\]

has been replaced by the amplitude-independent projective question

\[
\boxed{
\text{can a finite completed rank-one loop be absorbed with exactly consistent phase and gain?}
}
\]

The proposed finite object is a companion loop holonomy

\[
\mathfrak G(\Gamma)
=
\prod_{e\in\Gamma}
\frac{\text{nonlinear companion transfer}}
{\text{finite-viscosity radial transfer}},
\]

with the desired theorem

\[
\boxed{|\mathfrak G(\Gamma)-1|\ge c_{\mathcal K}>0.}
\]

This is OPEN.

---

# 10. Current verdict

The exact transverse saturation reduction remains the correct stationary object:

\[
\boxed{T=\kappa R_{\rm fv}.}
\]

What has been retired is the claim that companion nonconcentration / interaction-to-occupation is the unique final coercive bridge.

The strongest current obstruction is the **absorption reset**. The most promising finite anti-repacking target is a **multiplicative companion-loop holonomy defect**.
