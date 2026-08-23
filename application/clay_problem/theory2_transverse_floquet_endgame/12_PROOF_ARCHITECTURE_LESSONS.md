# 12 — Proof architecture lessons and anti-repacking criteria

## Purpose

This file records methodological lessons learned while reducing the Theory-2 stationary / Floquet frontier. It is not a theorem chapter. Its purpose is to prevent future work from returning to equivalent reformulations, nonuniform finite-mode arguments, additive coercivity mechanisms already defeated by audits, or compactness assumptions stronger than they appear.

The current stationary frontier is Chapter 13:

[`13_ABSORPTION_RESET_AND_FINITE_COMPANION_HOLONOMY.md`](13_ABSORPTION_RESET_AND_FINITE_COMPANION_HOLONOMY.md).

---

# 1. Re-expression is not reduction

A transformed identity counts as a genuine reduction only if it produces at least one of:

- a new sign;
- a quantitative gap;
- a finite-dimensional obstruction;
- a mode-count-independent coercive estimate;
- an exclusion of a previously viable geometry;
- or a finite invariant whose failure forces an explicit terminal branch.

The all-positive-depth common-ray family is the canonical warning. Taken as a continuum Laplace family it reconstructs the stationary radial equation.

\[
\boxed{
\text{continuum observability alone}\neq\text{analytic reduction}.
}
\]

---

# 2. The correct stationary object is still the saturation residual

The stationary branch is encoded by

\[
\boxed{T-\kappa R_{\rm fv}.}
\]

The exact residual identity is

\[
\boxed{
\|N-\kappa Y\|_{-1/2}^2
=
\|T-\kappa R_{\rm fv}\|_{-1/2}^2
+
\frac{(W/2-\kappa D_3)^2}{d^2}.
}
\]

On the scalar stationary stratum `W=2κD_3`, exact stationarity is exactly

\[
T=\kappa R_{\rm fv}.
\]

The quantitative constant `η_K` is secondary. Once exact saturation is excluded on a compact graph-topology class, continuity supplies the uniform gap.

Do not optimize `η_K` before proving pointwise exclusion.

---

# 3. Finite-complexity rigidity is real but does not compactify automatically

Finite completed nonexceptional physical networks cannot realize positive transverse saturation.

That theorem remains useful evidence.

But

\[
\boxed{
\text{finite-network nonclosure at every depth}
\not\Rightarrow
\text{uniform infinite-depth gap}.
}
\]

A terminal defect may shrink to zero with depth. Any continuum theorem must control the limit mechanism, not merely prove that each finite truncation has some nonzero boundary output.

---

# 4. Rank-one mass propagation has a precise domain of validity

The exact estimate

\[
\sum_{i\ne j}|A_iB_j|^2
\ge
\sum_i|A_iB_i|^2
\]

shows that hidden nonlinear cancellation exports comparable **raw interaction mass**.

But this propagation law only applies while the mechanism stays inside nonlinear Formation cancellation.

Once a genuine companion output is absorbed into the aligned linear field

\[
\kappa R_{\rm fv},
\]

there is no theorem forcing another nonlinear canceller of comparable size.

Rule:

\[
\boxed{
\text{rank-one propagation stops at linear absorption.}
}
\]

This is the absorption reset.

---

# 5. Interaction mass, occupied mass, and regenerated nonlinear mass are three different currencies

Do not identify:

\[
\text{raw companion mass},
\qquad
\text{state occupation},
\qquad
\text{fresh nonlinear ancestry}.
\]

A companion output can be represented by a much smaller high-frequency state packet because the finite-viscosity response carries two derivatives.

The schematic scaling

\[
a_{n+1}
\lesssim
\frac{a_n^2}{\kappa\rho_n}
\]

shows that occupation may regenerate dramatically less nonlinear mass than the parent interaction supplied.

Therefore

\[
\boxed{
\text{interaction}\Rightarrow\text{occupation}
}

is not a final coercive theorem.

Nor is

\[
\boxed{
\text{occupation}\Rightarrow c\times\text{fresh interaction}
}

with `0<c<1`: geometric extinction remains possible.

---

# 6. Bounded occupation packing is not non-extinction

A model

\[
m_{n+1}=q m_n,
\qquad
0<q<1,
\]

has

\[
\sum_n(m_n-m_{n+1})=m_0<\infty
\]

while `m_n→0`.

Thus a Carleson/packing estimate for occupation may be true and still fail to contradict an infinite ancestry.

This retires the earlier idea that a finite-tree occupation packing inequality alone would close stationary saturation.

Any future additive argument must prove a genuinely amplitude-independent defect, not just finite total charging.

---

# 7. Finite readers and finite jets cannot overcome compact-operator singular sequences by themselves

On a bounded nonexceptional continuum incidence chart, after fixing one rank-one factor, a finite physical companion branch is a smooth integral operator in the other factor. Under ordinary chart regularity it is Hilbert--Schmidt and therefore compact.

Adding finitely many reality branches or finitely many positive heat/Poisson multipliers preserves compactness.

Hence on an unrestricted infinite-dimensional hidden-cancellation sphere there are normalized weakly-null sequences whose full finite output family tends to zero.

Therefore

\[
\boxed{
\text{finite smooth readers alone cannot be bounded below on the continuum hidden sphere.}
}
\]

Finite depths are useful only after independent physical rigidity or hereditary/projective compactness has reduced the admissible descendant family.

---

# 8. Ordinary state compactness is not hereditary descendant compactness

A compact state may contain an infinite summably small decomposition

\[
v=v_0+\sum_n\varepsilon_n w_n,
\qquad
\varepsilon_n\to0,
\]

with normalized descendants `w_n` having no compact subsequence.

Thus

\[
\boxed{
\text{compactness of the original state class}
\neq
\text{compactness of normalized microscopic companion descendants}.
}
\]

If a proof needs a uniform translation-continuity / Kolmogorov--Riesz modulus for every normalized descendant, state that as a separate hereditary/projective hypothesis. Do not smuggle it into the word “compact”.

And remember: even hereditary projective compactness only addresses phase singular sequences; it does not prevent amplitude extinction.

---

# 9. The finite-viscosity transverse operator is locally flexible, not locally obstructive

For stationary candidates,

\[
R_{{\rm fv},\sigma}
=
-2D_2\rho\partial_\rho
-\chi_\sigma\rho^2
+O(\rho),
\qquad
\chi_\sigma>0.
\]

The frozen first-order radial operator has a finite-energy right inverse for smooth compact-annulus forcing.

Therefore no universal theorem can close the problem merely by asserting that a companion output has the “wrong local shape”, “wrong local phase”, or “wrong local gain” for `R_{\rm fv}`.

The contradiction, if one exists, must exploit **same-state self-consistency across more than one absorption edge**.

---

# 10. High-frequency stability favors absorption reset

On high-frequency fixed-ratio annuli,

\[
\|f\|_{H^{-1/2}}
\lesssim_{\mathcal K}
\rho^{-2}
\|R_{\rm fv}f\|_{H^{-1/2}}.
\]

Thus high-frequency forcing can be absorbed by a very small state packet.

This is a structural reason not to expect a reproduction-number theorem `≥1` from additive mass accounting.

The current stationary proof should treat quadratic-to-linear homogeneity as a central mechanism, not a technical error term.

---

# 11. The final invariant should survive amplitude extinction

Any proposed terminal coercive quantity should remain meaningful when descendant amplitudes tend to zero superexponentially.

Additive mass does not have this property.

A projective phase/gain or multiplicative cycle invariant can.

This motivates the current target:

\[
\boxed{
\mathfrak G(\Gamma)
=
\prod_{e\in\Gamma}
\frac{\text{nonlinear companion transfer}}
{\text{finite-viscosity radial transfer}}.
}
\]

A finite loop defect

\[
|\mathfrak G(\Gamma)-1|\ge c_{\mathcal K}>0
\]

would survive arbitrarily small amplitudes and directly obstruct simultaneous self-consistent absorption around a completed rank-one loop.

---

# 12. Mixed curvature should be tested at the cycle level, not by global additive summation

The mixed Poisson--heat reverse-pair conductance is positive, but global sums of unrelated triads can cancel.

A rank-one completed rectangle links reverse pairs multiplicatively.

Therefore the right question is whether mixed curvature supplies a **closed-loop phase/gain defect**, not whether it gives a globally signed additive scalar.

This is a new use of an old exact identity and should be audited first on the smallest reality-complete rectangle.

---

# 13. Anti-repacking criterion for the holonomy route

A valid finite companion holonomy theorem must be obtained **before** globally solving the raywise stationary equation.

Accepted:

- finitely many physical incidences;
- finitely many radial transfer factors;
- rank-one multiplicative identities;
- reality/reverse edges;
- Curl--Killing/helicity/Leray geometry;
- a finite cycle defect with mode-count-independent constant.

Rejected as likely repackaging:

- integrate `T=κR_{\rm fv}` over all rays and classify the resulting global self-consistent solution;
- use the full continuum Poisson family as an inverse transform;
- introduce an infinite scalar hierarchy;
- assume a hereditary compactness statement equivalent in strength to the desired saturation gap.

---

# 14. Current stationary milestone

The previous stationary milestone

\[
\text{interaction-to-occupation / companion nonconcentration}
\]

has been superseded as the final target.

The current milestone is

\[
\boxed{
\textbf{Finite Companion Holonomy Problem:}
\quad
\text{a bounded-depth completed physical loop cannot be absorbed with unit phase/gain holonomy.}
}
\]

The desired finite theorem is schematically

\[
\boxed{|\mathfrak G(\Gamma)-1|\ge c_{\mathcal K}>0.}
\]

If proved for a loop forced by every nonexceptional hidden cancellation, exact saturation `T=κR_{\rm fv}` is impossible and compactness supplies the stationary gap.

---

# 15. Distinct recurrent/Floquet route

The nonstationary causal recycling programme remains distinct. Its finite-step source/catalyst or Floquet theorem must not be silently identified with the stationary companion holonomy target.

The two routes may eventually share cycle/monodromy ideas, but their current exact equations and hypotheses differ.

---

# 16. Current proof-engineering doctrine

The recommended loop is now:

\[
\boxed{
\begin{aligned}
&\text{preserve complete Theory-2 state}\\
&\to\text{identify the exact finite physical completion}\\
&\to\text{audit every additive coercive inference against absorption reset}\\
&\to\text{seek an amplitude-independent projective/cycle invariant}\\
&\to\text{prove a bounded-depth mode-independent defect}\\
&\to\text{only then use compactness to extract the global stationary gap.}
\end{aligned}}
\]

A theorem should be rejected as likely repackaging if the entire stationary PDE must be reconstructed before the first genuinely new finite defect appears.
