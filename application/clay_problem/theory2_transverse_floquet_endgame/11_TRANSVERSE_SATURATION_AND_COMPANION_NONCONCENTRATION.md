# 11 — Transverse saturation and companion nonconcentration

## Status

This chapter records the next stationary finite-`κ` reduction after the common-ray Poisson-depth analysis. The continuum ray family is **not** used as the final theorem: because it is Laplace-invertible, attacking the entire family head-on would reconstruct the stationary radial equation and risk repackaging the stationary Navier–Stokes profile problem.

The genuinely smaller object is the exact transverse saturation

\[
\boxed{T(v)=\kappa R_{\rm fv}(v)}.
\]

The finite completed-network version is already rigid. The only remaining obstruction is a continuum limit in which completed rank-one companion mass migrates through an increasingly fine angular/radial laminate.

> **Nonclaim.** The continuum-laminate obstruction is still OPEN. Nothing below proves 3D Navier–Stokes regularity or excludes every finite-`κ` stationary profile.

---

# 1. EXACT — stationary residual has a Pythagorean saturation decomposition

Write

\[
R:=R_{\rm fv}(v).
\]

The normalized stationary equation is exactly

\[
\boxed{T(v)=\kappa R(v)}.
\]

In the `H^{-1/2}` Hilbert structure define

\[
\cos\vartheta(v)
=
\frac{\operatorname{Re}(T,R)_{-1/2}}
{\|T\|_{-1/2}\|R\|_{-1/2}}.
\]

Then identically

\[
\boxed{
\begin{aligned}
\|T-\kappa R\|_{-1/2}^{2}
={}&
\bigl(\|T\|_{-1/2}-\kappa\|R\|_{-1/2}\bigr)^2\\
&+2\kappa\|T\|_{-1/2}\|R\|_{-1/2}(1-\cos\vartheta).
\end{aligned}}
\]

Thus exact stationarity requires simultaneous saturation of two independent defects:

\[
\boxed{\vartheta=0}
\]

and

\[
\boxed{\|T\|_{-1/2}=\kappa\|R\|_{-1/2}}.
\]

Hence an angle gap is sufficient but not logically necessary. A uniform gain mismatch would also exclude stationarity.

The minimal coercive target is

\[
\boxed{
\frac{\|T-\kappa R\|_{-1/2}}
{\|T\|_{-1/2}+\kappa\|R\|_{-1/2}}
\ge \eta_{\mathcal K}>0.
}
\]

---

# 2. EXACT / compactness reduction — the real issue is exact positive saturation

On a compact class `\mathcal K` on which

\[
v\mapsto T(v),\qquad v\mapsto R(v)
\]

are continuous into `H^{-1/2}`, and with

\[
\inf_{\mathcal K}\|T\|_{-1/2}>0,
\qquad
\inf_{\mathcal K}\|R\|_{-1/2}>0,
\]

exact exclusion of positive parallelism

\[
T(v)\notin\mathbb R_+R(v)
\qquad\forall v\in\mathcal K
\]

immediately yields a quantitative angle gap by compactness.

Therefore the constant `\eta_{\mathcal K}` is not the conceptual difficulty. The exact classification problem is

\[
\boxed{T(v)=\lambda R_{\rm fv}(v),\qquad \lambda>0.}
\]

For a stationary profile one only needs to exclude the special gain

\[
\lambda=\kappa.
\]

On the scalar stationary constraint surface

\[
W=2\kappa D_3,
\qquad
\gamma=\kappa D_3/d^2,
\]

one has

\[
\boxed{N-\kappa Y=T-\kappa R.}
\]

Thus if `T=\lambda R`, the stationary residual is

\[
\boxed{N-\kappa Y=(\lambda-\kappa)R.}
\]

This is why either an angle defect or a gain defect can close the stationary branch.

---

# 3. EXACT — finite completed physical networks cannot saturate nonexceptionally

Consider a physical interaction network with finitely many completed spectral incidence classes. Assume:

- all reality companions are retained;
- rank-one cross incidences are retained;
- `R_{\rm fv}` is local to the occupied spectral packets;
- active unequal-shell interactions remain away from the already classified collinear, same-root, skinny, and null strata.

If

\[
T=\lambda R_{\rm fv},\qquad \lambda>0,
\]

then every Formation output outside the occupied packet family must vanish because `R_{\rm fv}` has no support there.

But the completed rank-one companion results imply that exact non-null unequal-shell hiding cannot remain inside a finite physical network. Same-output cancellation forces cross incidences; repeated completion either reaches an exceptional geometry or exports to new spectral data.

In the periodic finite-support setting the resulting rigidity is

\[
\boxed{
\text{finite exact unequal-shell hidden completion}
\Longrightarrow
\text{collinear/null exception}.
}
\]

Therefore, for every genuinely finite completed nonexceptional interaction network,

\[
\boxed{T=\lambda R_{\rm fv},\ \lambda>0}
\]

is impossible.

Consequently every compact finite-complexity family has a positive transverse angle gap.

This closes the finite physical version of the desired stationary rigidity theorem.

---

# 4. AUDIT — why the finite theorem does not automatically compactify

The hostile angular annihilator

\[
z_h=\delta_{-h}-2\cos h\,\delta_0+\delta_h
\]

kills the local `\pm1` angular moments exactly, while rank-one cross-completion changes output radius by only

\[
O(h^2).
\]

The base physical triangle may remain uniformly noncollinear and non-skinny as

\[
h\downarrow0.
\]

Therefore a proof based only on "every hidden interaction exports strictly outward" has a coercivity constant that may degenerate to zero in the continuum limit.

There is no uniform one-generation radial jump.

This is not a stationary NS construction. Full rank-one completion continues to produce further interactions. But it proves that the finite-support theorem cannot be promoted to a mode-count-independent theorem by a naive `N\to\infty` limit.

---

# 5. EXACT — rank-one cancellation propagates raw companion mass

Suppose same-output cancellation uses diagonal incidence products

\[
Z_{ii}=A_iB_i.
\]

Actual-state rank one forces

\[
Z_{ij}=A_iB_j.
\]

Whenever the diagonal incidences cancel,

\[
\boxed{
\sum_{i\ne j}|A_iB_j|^2
\ge
\sum_i|A_iB_i|^2.
}
\]

Hence coherent angular hiding cannot destroy raw interaction mass. It exports at least comparable rank-one companion mass.

This estimate is mode-count independent.

Away from physical coupling degeneracies, helical Formation coupling is uniformly comparable to raw rank-one mass. At fixed finite `κ`, the already proved inequalities

\[
\frac{d^2}{D_3}\gtrsim \kappa^2,
\qquad
1-|b|\gtrsim \kappa^2
\]

exclude the pure-helicity / constrained-gradient saturation escape.

Thus the unresolved mechanism is reduced to

\[
\boxed{
\text{completed rank-one interaction mass migrating through an increasingly fine angular/radial companion laminate.}
}
\]

---

# 6. OPEN — companion nonconcentration

Functional compactness does not bound the number of physical triads. A single smooth state may have infinitely many Fourier interactions.

What compactness can exclude is a fixed nonzero amount of norm or defect living indefinitely in progressively finer unresolved structure.

The correct question is therefore:

\[
\boxed{
\text{Does exact positive transverse alignment force a nonvanishing amount of Formation mass to survive at every generation of companion completion?}
}
\]

If yes, an infinite laminate would transport a nonvanishing defect through arbitrarily fine scales and violate compactness/tightness.

If instead the propagated mass can decay summably generation by generation, a smooth compact profile could in principle carry infinite ancestry.

The exact missing theorem is therefore:

\[
\boxed{\textbf{Companion nonconcentration.}}
\]

> On a positively oriented finite-`κ` state satisfying the stationary scalar constraints, a nonzero amount of completed rank-one Formation mass cannot remain trapped through arbitrarily many generations inside an angular/radial neighborhood whose diameter tends to zero, unless the state approaches a previously classified exceptional stratum.

Combined with rank-one mass propagation, this would produce a mode-count-independent transverse angle or saturation gap.

---

# 7. OPEN — interaction mass must be converted into occupied state mass or an orthogonal defect

The remaining quantitative bridge is

\[
\boxed{
\text{nondecaying companion interaction mass}
\Longrightarrow
\text{nondecaying state occupation or an unavoidable orthogonal component}.
}
\]

The difficulty is real: the stationary infrared law allows

\[
\widehat v(\rho\omega)=O(\rho),
\]

with leading ancestry carried by `T`. Therefore an infinite companion chain can in principle terminate in a very small smooth infrared tail without carrying order-one critical stock there.

Likewise increasingly fine angular structures may carry little state mass while remaining catalytically relevant.

The current rank-one inequalities control interaction products more strongly than they control the state occupation required to sustain those products.

---

# 8. Desired finite-depth interaction-to-occupation bridge

Because a compact stationary finite-`κ` class is observed by finitely many positive Poisson depths, choose

\[
y_1,\dots,y_m>0
\]

so that

\[
\sum_{\sigma,j}\|\mathcal V_\sigma(y_j)\|_2^2
\ge c_{\mathcal K}>0.
\]

The desired strengthening is not another observability theorem for `v`. It is a finite-depth bridge from completed interaction mass to actual occupied state mass:

\[
\boxed{
\sum_{j=1}^{m}\|\mathcal V(y_j)\|_2^2
\ge
c_{\mathcal K}\,\mathfrak M_{\rm comp}(v),
}
\]

where `\mathfrak M_{\rm comp}` is a nonnegative completed rank-one companion-mass functional satisfying

\[
\boxed{
\mathfrak M_{\rm comp}(v)
\gtrsim
\|T_{\perp R}(v)\|_{-1/2}^{2}
+
\text{exported hidden mass}.
}
\]

If such a finite functional can be constructed, the loop becomes

\[
\text{alignment}
\Rightarrow
\text{hidden companion mass}
\Rightarrow
\text{rank-one export}
\Rightarrow
\text{finite-depth occupation}
\Rightarrow
\text{new completed interaction},
\]

with no quantitative loss.

A finite compact spectral region cannot support that indefinitely unless a completed circulation closes. Away from the exceptional set, the existing mixed Poisson–heat positivity then obstructs a completely hidden nonnegative circulation.

This would close the compact stationary finite-`κ` branch without inverting the continuum ray family.

---

# 9. Minimal final theorem

The strongest desirable theorem is an angle gap,

\[
\angle(T,R_{\rm fv})\ge\eta_{\mathcal K}>0.
\]

But the mathematically minimal closure is the saturation gap

\[
\boxed{
\|T-\kappa R_{\rm fv}\|_{H^{-1/2}}
\ge
\eta_{\mathcal K}
\left(
\|T\|_{H^{-1/2}}
+
\kappa\|R_{\rm fv}\|_{H^{-1/2}}
\right).
}
\]

Any finite physical theorem that provides either a uniform angle defect or a uniform gain defect rules out the compact stationary finite-`κ` branch immediately.

---

# 10. Current verdict

The repackaging objection is **not fully eliminated**, but it is now localized to one quantitative implication:

\[
\boxed{
\text{completed companion interaction mass}
\Longrightarrow
\text{finite-depth occupied mass or angle/gain defect}.
}
\]

Everything before that is genuinely coercive:

1. bounded-module recycling has a mode-count-independent viscous loss;
2. adaptive actual-state covariance has a signed debt;
3. stationary `T` has finite-depth coercive load;
4. rank-one cancellation exports comparable companion interaction mass;
5. finite completed networks cannot hide nonexceptionally;
6. finite `κ` quantitatively separates the stationary branch from the pure-helicity regression boundary.

If the interaction-to-occupation bridge is proved with finitely many physical semigroup depths and the existing rank-one companion identities, the compact stationary finite-`κ` problem will have been reduced to a genuinely smaller coercive theorem rather than a rewritten stationary Navier–Stokes equation.
