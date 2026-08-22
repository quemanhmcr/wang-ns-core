# Theory-2 interaction frame

**Status:** canonical blow-up architecture built from the exact Theory-2 mother/flag theorems. **Not a 3D Navier--Stokes regularity theorem.**

This directory restarts the blow-up application from the complete state coordinate

\[
\Sigma(u)=\{\mathscr O_a(u)\}_{a\in\mathbb R}
\longleftrightarrow
E_u=[\nabla_u,C]
\longleftrightarrow u,
\]

and then moves to an anchored material interaction frame in which the state obeys heat while Euler appears exactly as motion of the curl/heat geometry:

\[
\boxed{
 v_t=-\nu(C^\sharp)^2v,
 \qquad
 C^\sharp_t=U^*E_uU,
 \qquad
 (H_a^\sharp)_t=U^*[\nabla_u,H_a]U.
}
\]

The point is architectural: **do the control-volume accounting in a frame where the PDE is heat, but never replace the complete Theory-2 state by a lossy scalar reader.**

## Files

1. [`00_THEOREM_SPINE.md`](00_THEOREM_SPINE.md) — derivation from Mother/Flag Completeness to the moving-heat system and spectral-measure law.
2. [`01_COMPLETENESS_AND_GAUGE.md`](01_COMPLETENESS_AND_GAUGE.md) — proof that the anchored frame preserves Theory-2 information, plus the gauge warning for the pair \((v,C^\sharp)\).
3. [`02_ANALYTIC_FRONTIER_AND_LESSONS.md`](02_ANALYTIC_FRONTIER_AND_LESSONS.md) — exact owners, the half-derivative seam, the monodromy target, no-go statements, and research lessons.
4. [`audits/interaction_frame_algebra.py`](audits/interaction_frame_algebra.py) — finite-dimensional sign/algebra audit for the interaction-frame identities.

## Mandatory discipline

- **Primitive state:** \(u\), equivalently \(E_u\) or the full shifted flag \(\Sigma(u)\).
- **Frame:** \(U_t=-\nabla_uU\), \(U(t_0)=I\). It is an anchored coordinate change, not a new physical source.
- **Readers:** spectral stocks, work, traffic, moments, packets and hinge quantities may prove inequalities but may not replace the primitive state without an explicit inverse theorem.
- **Progress:** a new step must prove coercivity, compactness/rigidity, eliminate a genuine kernel, or contradict a singular-endpoint requirement. A new renderer is not progress.

## Core dependencies

- [`core/spectral_signature/MOTHER_COMPLETENESS_THEOREM.md`](../../../core/spectral_signature/MOTHER_COMPLETENESS_THEOREM.md)
- [`core/spectral_signature/SPECTRAL_FLAG_SIGNATURE.md`](../../../core/spectral_signature/SPECTRAL_FLAG_SIGNATURE.md)
- [`core/spectral_signature/HALF_DERIVATIVE_POLAR_KORN_BRIDGE.md`](../../../core/spectral_signature/HALF_DERIVATIVE_POLAR_KORN_BRIDGE.md)

The interaction frame is therefore a **Theory-2-preserving application layer**, not a replacement for Theory 2.
