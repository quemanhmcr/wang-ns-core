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

## Start here: theorem-first doctrine

Every new idea in this directory must start from the **proved Theory-2 maps**, not from a late observer, a scalar obstruction, or a convenient renamed descendant. The safe spine is

\[
\boxed{
\Sigma(u)\longleftrightarrow E_u\longleftrightarrow u,
}
\]

followed only by exact coordinate changes whose inverse or gauge is retained. This order is not stylistic. It is the main protection against recreating the historical loop.

The historical endgame became difficult partly because complete state information was contracted too early into stock/work/traffic readers. Those readers were correct at their own level, but they had nontrivial kernels; later differentiation then made the discarded phase, polarization, geometry or higher-state information reappear under new names. That produced the pattern

\[
\text{complete state}
\to\text{lossy reader}
\to\text{blindness}
\to\text{new defect}
\to\text{reconstruction of discarded information}.
\]

The rule here is therefore strict:

1. **Compile backward first.** Before using a new object, identify the exact Mother/Flag theorem, renderer formula, contraction map, or higher-jet chain rule that produces it.
2. **Never promote a contraction to the state.** A scalar/tensor reader may prove an estimate; if it becomes blind, return to \(u/E/\Sigma\) rather than differentiating it into a new ontology.
3. **Keep invertibility explicit.** Any moving frame, normalization, localization or quotient must retain its inverse, its gauge, or a proved reconstruction theorem.
4. **Separate information from control.** Theory 2 supplies complete state information; regularity progress begins only when a step adds a genuine coercive estimate, compactness/rigidity theorem, or contradiction.
5. **Treat a new name as suspicious until it reduces analytic freedom.** If an object is only another renderer of the same complete state, it is bookkeeping, not progress.

A contributor should be able to draw an exact dependency arrow from every proposed mechanism back to the Theory-2 spine. If that arrow is missing, the proposal is not ready to enter the proof architecture.

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
