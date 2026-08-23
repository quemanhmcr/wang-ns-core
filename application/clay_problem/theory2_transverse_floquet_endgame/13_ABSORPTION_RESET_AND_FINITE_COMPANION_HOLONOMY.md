# 13 — Absorption reset and finite companion holonomy

## Status

This chapter records the current stationary finite-`κ` frontier after the failure of the additive companion-mass program.

The threshold is still

\[
\boxed{\mathbf{NO}}.
\]

We do **not** have a mode-count-independent angle gap

\[
\angle(T,R_{\rm fv})\ge \eta_{\mathcal K}>0
\]

or the equivalent stationary saturation gap.

The decisive sharpening is structural:

\[
\boxed{
\text{quadratic Formation export}
\longrightarrow
\text{linear finite-viscosity absorption}
\longrightarrow
\text{smaller quadratic descendant}.
}
\]

This quadratic-to-linear reset can extinguish an infinite companion ancestry at finite `D_3` cost. Therefore additive mass propagation, occupation packing, or finite-reader coercivity cannot by themselves be the final mechanism.

> **Nonclaim.** No actual smooth stationary Navier–Stokes profile realizing the extinction cascade is constructed here. The dyadic ancestry is an AUDIT consistency model for the current ledger.

---

# 1. EXACT — the stationary transverse operator is high-frequency stable on both helicity sheets

Set

\[
r:=\frac{D_3}{d^2}.
\]

For a stationary normalized finite-`κ` candidate and helicity sheet `σ=±1`, with

\[
\widehat v_\sigma(\rho,\omega)=f_\sigma(\rho,\omega),
\]

the explicit transverse finite-viscosity field is

\[
\widehat{R_{\rm fv}}_\sigma
=
-2D_2\rho\partial_\rho f_\sigma
+
\left(
[1-r(1-\sigma b)]\rho^2+ra\rho-4D_2
\right)f_\sigma.
\]

The stationary regression identities give

\[
D_3-d^2=aD_2,
\qquad
b=-\frac{D_2Q}{D_3-Q^2},
\]

and

\[
1-|b|-\frac{d^2}{D_3}
=
\frac{D_2(D_2-|Q|)}{D_3-Q^2}.
\]

For a nonzero stationary state, `H_3=0` forces both helicity sheets to be active, hence

\[
|Q|<D_2.
\]

Therefore

\[
1-|b|>\frac1r,
\]

so for both helicities

\[
\chi_\sigma:=r(1-\sigma b)-1>0.
\]

Thus

\[
\boxed{
\widehat{R_{\rm fv}}_\sigma
=
-2D_2\rho\partial_\rho f_\sigma
+
(-\chi_\sigma\rho^2+ra\rho-4D_2)f_\sigma,
\qquad
\chi_\sigma>0.
}
\]

On compact nonexceptional stationary strata,

\[
\chi_\sigma\ge \chi_{\mathcal K}>0.
\]

This is **EXACT**.

---

# 2. AUDIT / exact frozen-coefficient consequence — local companion forcing is absorbable

Freeze the scalar coefficients `(D_2,r,a,b)` of a putative profile and define raywise

\[
\mathscr R_\sigma f
:=
-2D_2\rho f'
+
(-\chi_\sigma\rho^2+ra\rho-4D_2)f.
\]

For any smooth forcing `F_σ` supported on a compact annulus

\[
0<\rho_0<\rho<\rho_1,
\]

the equation

\[
\mathscr R_\sigma f=F_\sigma
\]

is a first-order radial ODE. Its homogeneous solution is

\[
f_h(\rho)
=C(\omega)\rho^{-2}
\exp\left(
-\frac{\chi_\sigma}{4D_2}\rho^2
+\frac{ra}{2D_2}\rho
\right).
\]

Finite energy kills the `\rho^{-2}` branch below the forcing annulus, while `\chi_\sigma>0` gives Gaussian decay above it. Hence every smooth compact-annulus forcing is absorbable by the frozen ray operator in the finite-energy class.

This is not the nonlinear stationary theorem. It is an exact frozen-coefficient audit showing that there is no universal one-generation range obstruction of the form

\[
\text{“physical companion output has the wrong local shape for }R_{\rm fv}\text{.”}
\]

The absorber must be constrained through **same-state self-consistency**, not through local radial range alone.

---

# 3. DEDUCTION — high-frequency absorption becomes more efficient

With the `H^{-1/2}` radial measure `\rho\,d\rho\,d\omega`, integration by parts gives

\[
\operatorname{Re}\langle f,\mathscr R_\sigma f\rangle_{-1/2}
=
\int
\rho
(-\chi_\sigma\rho^2+ra\rho-2D_2)
|f|^2\,d\rho.
\]

Therefore above a `\mathcal K`-dependent frequency,

\[
-\operatorname{Re}\langle f,\mathscr R_\sigma f\rangle_{-1/2}
\gtrsim_{\mathcal K}
\|\Lambda^2f\|_{H^{-1/2}}^2.
\]

On a fixed-ratio high-frequency annulus,

\[
\boxed{
\|f\|_{H^{-1/2}}
\lesssim_{\mathcal K}
\rho^{-2}
\|\mathscr R_\sigma f\|_{H^{-1/2}}.
}
\]

Thus a high-frequency companion forcing can be absorbed by a state packet smaller by `O(\rho^{-2})` in the critical transverse metric.

---

# 4. AUDIT — quadratic-to-linear reset and geometric extinction

Formation is quadratic:

\[
N(\varepsilon v)=\varepsilon^2N(v),
\]

whereas the frozen finite-viscosity response is linear in the absorber.

If a companion generation creates forcing of size `F_n` at frequency `\rho_{n+1}`, the radial estimate permits an occupied packet of schematic size

\[
a_{n+1}
\sim
\frac{F_n}{\kappa\rho_{n+1}^2}.
\]

For two comparable parent tail packets,

\[
F_n\sim \rho_n a_n^2,
\]

and bounded shell ratio yields

\[
\boxed{
a_{n+1}
\lesssim_{\mathcal K}
\frac{a_n^2}{\kappa\rho_n}.}
\]

Once `a_n` is small, this is superlinear contraction.

For the dyadic audit

\[
\rho_n=2^n\rho_0,
\]

the recursion is compatible with faster-than-exponential decay and

\[
\sum_n\rho_n^3a_n^2<\infty.
\]

Hence every finite completed network may have a nonzero terminal defect while the infinite limit has terminal defect tending to zero at finite `D_3` cost.

This defeats the inference

\[
\text{finite-network nonclosure at every depth}
\Longrightarrow
\text{uniform infinite-depth saturation gap}.
\]

---

# 5. SUPERSEDED FINAL ROUTES — why additive mass arguments are no longer sufficient

The following statements remain useful locally but are no longer credible as the final closure mechanism:

1. raw rank-one companion mass propagation;
2. companion mass `\to` occupied state mass;
3. bounded occupation packing / Carleson charging;
4. a reproduction inequality with factor `c<1`;
5. finite-jet or finite-reader detection without amplitude-independent projective rigidity.

The reason is the absorption reset:

\[
\boxed{
\text{companion export}
\to
\kappa R_{\rm fv}\text{-absorption}
}
\]

terminates the requirement for another nonlinear canceller. Rank-one propagation applies only while the mechanism stays inside nonlinear Formation cancellation.

Even

\[
m_{n+1}\ge c\,m_n,
\qquad 0<c<1,
\]

permits geometric extinction. A counting proof would effectively need reproduction number at least one after all absorption losses and multiplicities, which is incompatible with the small-amplitude quadratic/linear scaling audit.

Therefore

\[
\boxed{
\text{pure additive mass propagation is structurally insufficient as the final stationary theorem.}
}
\]

---

# 6. The continuum phase singular-sequence obstruction remains secondary

On a localized continuum incidence chart, fixing one rank-one factor makes each finite physical companion branch a smooth integral operator in the other factor. Under ordinary compact-chart regularity it is Hilbert--Schmidt, hence compact.

Thus finite physical output families, even with finitely many positive heat/Poisson weights, admit weakly-null normalized phase singular sequences on unrestricted infinite-dimensional hidden spaces.

This remains an important no-go:

\[
\text{finite smooth readers alone cannot be uniformly bounded below.}
\]

However, even granting hereditary/projective compactness of normalized descendants so that this local issue disappears, the quadratic-to-linear absorption reset survives. Therefore the reset is the more fundamental current obstruction.

---

# 7. Pivot — the invariant should be multiplicative, not additive

Actual-state rank one gives the multiplicative rectangle identity

\[
\boxed{Z_{ii}Z_{jj}=Z_{ij}Z_{ji}.}
\]

Suppose partner-swapped outputs `ij` and `ji` are absorbed through finite-viscosity radial transfer operators:

\[
w_{ij}=\kappa^{-1}\mathscr R_{ij}^{-1}Z_{ij},
\qquad
w_{ji}=\kappa^{-1}\mathscr R_{ji}^{-1}Z_{ji}.
\]

Then their product carries

\[
(\mathscr R_{ij}\mathscr R_{ji})^{-1}Z_{ij}Z_{ji}
=
(\mathscr R_{ij}\mathscr R_{ji})^{-1}Z_{ii}Z_{jj}.
\]

This suggests that the amplitude-independent object is a finite loop gain / holonomy rather than an additive companion mass.

For a completed physical loop `Γ`, schematically define

\[
\boxed{
\mathfrak G(\Gamma)
=
\prod_{e\in\Gamma}
\frac{\text{nonlinear companion transfer on }e}
{\text{finite-viscosity radial transfer on }e}.
}
\]

Exact saturation around a closed loop should impose a consistency relation of the form

\[
\mathfrak G(\Gamma)=1
\]

including phase and gain.

---

# 8. OPEN — Finite Companion Holonomy Problem

The sharpest current finite theorem target is:

\[
\boxed{
\textbf{Finite Companion Loop Defect (FCL):}
\qquad
|\mathfrak G(\Gamma)-1|
\ge c_{\mathcal K}>0
}
\]

for some bounded-depth reality-complete physical loop forced by every nonexceptional hidden cancellation.

A successful theorem must tie together:

- rank-one multiplicative completion;
- reality / reverse companion edges;
- Curl--Killing polarization;
- finite-viscosity radial transfer;
- the same global coefficients `D_2,a,b,D_3/d^2`;
- and, if useful, the already established mixed Poisson--heat reverse-pair curvature.

Why this target is qualitatively better:

- it is finite;
- it is amplitude-independent;
- it survives `a_n\to0`;
- it does not rely on continuum Laplace inversion;
- it does not require mass accumulation through an infinite ancestry;
- it is falsifiable on the smallest completed rectangle.

At present the exact transfer composition and a loop defect theorem are **OPEN**.

---

# 9. Why mixed curvature may belong at the loop level

The previously proved reverse-pair mixed Poisson--heat conductance is strictly positive, and complete mixed-helicity triads inherit the same sign. Additive global summation can still cancel unrelated triads.

A completed rank-one rectangle, however, links reverse pairs multiplicatively.

The natural finite program is therefore to test whether every nonexceptional hidden cancellation forces a bounded-depth loop on which:

1. rank-one amplitude products close exactly;
2. finite-viscosity radial transfer preserves the relevant orientation;
3. mixed curvature produces a strict cycle defect.

If the defect attaches to an individual closed physical cycle, unrelated global triad cancellation cannot remove it.

---

# 10. Anti-repacking guard

Global raywise inversion of

\[
T=\kappa R_{\rm fv}
\]

would reconstruct the stationary transverse equation and return to the repackaging problem.

The accepted next theorem must therefore be a **finite cycle invariant** extracted before global radial reconstruction.

The following do **not** count as closure:

- solving the full raywise first-order equation on all rays and then classifying its nonlinear self-consistency;
- adding an infinite scalar moment hierarchy;
- relying on finite-support constants that degenerate with complexity;
- assuming hereditary compactness strong enough to encode the desired saturation gap itself.

A genuine FCL theorem would pass the anti-repacking test because it concerns finitely many incidences and finitely many transfer factors, with a mode-count-independent projective defect.

---

# 11. Current ledger

### EXACT

1. Stationary transverse saturation remains `T=κR_{\rm fv}`.
2. `H_3=0` plus the regression algebra imply `|Q|<D_2` for nonzero stationary states.
3. Both helicity sheets satisfy `χ_σ=r(1-σb)-1>0`.
4. The frozen transverse radial operator has Gaussian-decaying high-frequency homogeneous flow.
5. Rank one supplies multiplicative rectangle closure `Z_{ii}Z_{jj}=Z_{ij}Z_{ji}`.

### DEDUCTION

1. On high-frequency fixed-ratio annuli,
   \[
   \|f\|_{-1/2}\lesssim_{\mathcal K}\rho^{-2}\|\mathscr R_\sigma f\|_{-1/2}.
   \]
2. Quadratic forcing may be absorbed by much smaller state packets.

### AUDIT

1. Dyadic companion ancestry can decay superlinearly with finite `D_3`.
2. Perfect one-generation companion coercivity does not prevent extinction.
3. Local shape/gain mismatch cannot be universal because the frozen radial operator is right-invertible on compact annuli.
4. Additive mass propagation / occupation packing is not a sufficient final mechanism.

### OPEN

1. Exact finite-viscosity transfer factors on a completed physical loop.
2. Existence of a bounded-depth loop forced by every nonexceptional hidden cancellation.
3. A uniform finite companion holonomy defect `FCL`.
4. Periodic/Floquet analogue remains separately open.

---

## Final statement

The smallest current stationary obstruction is no longer an infinite companion laminate or an interaction-to-occupation gap.

It is

\[
\boxed{
\text{quadratic companion export}
\to
\text{linear finite-viscosity absorption}
\to
\text{subcritical quadratic regeneration}.
}
\]

The most promising finite anti-repacking response is a multiplicative, amplitude-independent companion-loop holonomy defect.

**Status: OPEN.**
