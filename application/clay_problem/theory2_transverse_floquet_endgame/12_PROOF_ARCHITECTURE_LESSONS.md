# 12 — Proof architecture lessons and anti-repacking criteria

## Purpose

This file records the methodological lessons learned while reducing the Theory-2 stationary / Floquet frontier. It is intentionally not a theorem chapter. Its role is to prevent future work from looping back into equivalent reformulations, nonuniform finite-mode arguments, or scalar hierarchies that do not control the complete Formation state.

---

# 1. Re-expression is not reduction

A transformed identity is only a genuine reduction if it produces at least one of:

- a new sign;
- a quantitative gap;
- a finite-dimensional obstruction;
- a mode-count-independent coercive estimate;
- an exclusion of a previously viable geometry;
- or a finite theorem whose failure forces loss of compactness.

The all-positive-depth common-ray family is a canonical warning. As a continuum Laplace family it is injective and reconstructs the stationary radial equation. Therefore

\[
\boxed{
\text{continuum observability alone}\neq\text{analytic reduction}.
}
\]

Its useful role is to generate finite coercive consequences, not to become the final theorem itself.

---

# 2. The correct stationary object is the saturation residual

The stationary branch is best encoded by

\[
\boxed{T-\kappa R_{\rm fv}.}
\]

The exact Pythagorean decomposition separates the obstruction into two independent parts:

\[
\text{angle defect}
\qquad\text{and}\qquad
\text{gain defect}.
\]

Therefore do not insist on an angle theorem if physical geometry naturally yields a gain mismatch. The mathematically minimal closure is any uniform lower bound for

\[
\frac{\|T-\kappa R_{\rm fv}\|}
{\|T\|+\kappa\|R_{\rm fv}\|}.
\]

This is sharper and less assumption-heavy than targeting a prescribed angle from the outset.

---

# 3. Compactness supplies constants only after exact saturation is excluded

On a compact class, once exact positive parallelism

\[
T=\lambda R_{\rm fv},\qquad \lambda>0,
\]

is excluded, a uniform angle gap follows by continuity.

Thus the hard theorem is a classification theorem, not an optimization theorem.

Do not spend effort estimating the best `\eta_{\mathcal K}` before proving that the saturation set is empty.

---

# 4. Finite physical geometry is already coercive

For a finite completed nonexceptional physical interaction network, rank-one companion completion and unequal-shell rigidity already rule out exact hidden positive saturation.

This is important evidence that the structural mechanism is real.

But:

\[
\boxed{
\text{finite-complexity coercivity}\not\Rightarrow\text{uniform continuum coercivity}.
}
\]

The hostile angular laminate shows that output displacement can shrink like `O(h^2)` while the base geometry remains noncollinear and non-skinny.

Therefore no proof may rely on a uniform one-generation outward jump unless that gap has been proved independently.

---

# 5. Rank-one completion propagates interaction mass, not automatically state mass

The exact estimate

\[
\sum_{i\ne j}|A_iB_j|^2
\ge
\sum_i|A_iB_i|^2
\]

shows that coherent cancellation cannot destroy raw rank-one companion mass.

But this does **not** yet imply a comparable amount of critical state occupation.

This distinction is central:

\[
\boxed{
\text{interaction mass}\neq\text{occupied state mass}.
}
\]

A small smooth infrared tail or a fine angular laminate may carry little state norm while remaining catalytically relevant.

The missing bridge must therefore be interaction-to-occupation, not another interaction-to-interaction estimate.

---

# 6. Functional compactness does not bound mode count

A singleton containing a smooth state with infinitely many Fourier interactions is compact.

Hence compactness must never be interpreted as finite Fourier complexity.

What compactness can exclude is a **nonvanishing amount of norm or defect** surviving through finer and finer unresolved structure.

The correct continuum question is:

\[
\boxed{
\text{Does companion completion propagate a nonvanishing amount of physical defect through every generation?}
}
\]

If yes, infinite lamination contradicts compactness/tightness. If the defect can decay summably, compactness alone does not close the argument.

---

# 7. Finite semigroup depths are valuable only when they control a physical quantity

Because the positive-depth readers are injective on compact strata, finitely many depths observe the state.

That by itself is not enough.

The desired use is a finite-depth estimate of the form

\[
\sum_j\|\mathcal V(y_j)\|^2
\gtrsim
\mathfrak M_{\rm comp}(v),
\]

where `\mathfrak M_{\rm comp}` is a physical completed companion-mass functional.

This would convert finite semigroup observation into a true interaction-to-occupation mechanism.

Rule:

> A finite reader family counts as analytic progress only when it controls the physical defect which must be propagated or dissipated.

---

# 8. Keep the actual-state rank-one structure until the final estimate

Do not replace

\[
\mathsf R=v\otimes v
\]

by an arbitrary tensor field.

Abstract tensor tomography has large kernels and does not encode physical companion completion.

Likewise, do not isolate arbitrary Galerkin triads: reality companions and cross incidences are part of the actual state and may carry the very leakage needed for coercivity.

The proof must preserve:

- same-state rank one;
- reality;
- polarized Curl–Killing;
- signed helicity data;
- companion completion;
- and actual semigroup covariance.

Only contract to a scalar at a genuinely coercive terminal estimate.

---

# 9. The finite-`κ` and Euler branches must remain separated

At fixed finite critical Reynolds, the stationary branch is quantitatively separated from

\[
d=0,
\qquad
|b|=1,
\]

through the established lower bounds involving `κ`.

Therefore pure-helicity / constrained-gradient degeneration is not an admissible finite-`κ` escape route.

If a sequence approaches those strata, it must simultaneously move toward

\[
\kappa\to0,
\]

the Euler terminal branch.

Do not mix finite-viscosity coercivity with Euler recurrence arguments.

---

# 10. The current decisive milestone

The present anti-repacking test is extremely concrete.

A genuine next theorem should prove, with finitely many physical semigroup depths and mode-count-independent constants,

\[
\boxed{
\text{completed companion interaction mass}
\Longrightarrow
\text{finite-depth occupied mass or a transverse saturation defect}.
}
\]

Equivalent acceptable outcomes include:

- companion nonconcentration;
- a finite-depth interaction-to-occupation inequality;
- a mode-count-independent angle gap;
- or a mode-count-independent gain gap.

What would **not** count as closure:

- inverting the full continuum Poisson-depth family;
- introducing another infinite scalar moment hierarchy;
- proving only a finite-mode outward-support theorem with a constant that degenerates as angular spacing tends to zero;
- or replacing actual convolution by an arbitrary tensor model.

---

# 11. Current proof-engineering doctrine

The recommended theorem-building loop is:

\[
\boxed{
\begin{aligned}
&\text{preserve complete Theory-2 state}\\
&\to\text{ derive exact physical completion}\\
&\to\text{ identify a finite saturation/return defect}\\
&\to\text{ prove mode-count-independent coercivity}\\
&\to\text{ classify every degeneration of the coercive constant}\\
&\to\text{ send those degenerations to explicit terminal branches.}
\end{aligned}
}
\]

A proposed theorem should be rejected as likely repackaging if its proof requires reconstructing the entire stationary PDE before any new finite coercive estimate appears.

The current frontier passes this test up to one remaining step: **interaction-to-occupation for an infinite completed companion laminate**.
