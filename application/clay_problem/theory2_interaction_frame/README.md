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

## A note on how to work from here

The most useful lesson from the earlier endgame is not a new rule, but a change of habit: when developing an idea, it is usually safer to return first to the original Theory-2 theorems and ask what the complete state is already telling us.  The natural spine is

\[
\boxed{
\Sigma(u)\longleftrightarrow E_u\longleftrightarrow u.
}
\]

The historical stock/work/traffic constructions were often exact and useful, but they lived after contractions of this complete state.  Once such a reader was asked to carry the whole dynamics, information hidden in its kernel could reappear one derivative later as phase, polarization, geometry, or another apparently new defect.  Much of the old loop can be understood as repeatedly recovering information that had been compressed away too early.

That experience suggests a simple working perspective for this directory.  New coordinates, control volumes, normalizations and observables are most trustworthy when their relation to the Mother/Flag theorems remains visible.  A contraction can be extremely useful for an estimate without having to become the state of the proof; when it stops seeing something, the complete coordinate \(u/E/\Sigma\) is still available in the background.  Likewise, an interaction frame is valuable because it reorganizes the same information, not because it creates a smaller hidden model of the PDE.

This also keeps two different questions separate.  Theory 2 addresses **what information describes the physical state**.  The blow-up problem still asks **what analytic estimate, compactness or rigidity prevents that state from concentrating**.  Keeping that distinction visible has so far been the most reliable way to tell genuine progress from another change of notation.

## Files

1. [`00_THEOREM_SPINE.md`](00_THEOREM_SPINE.md) — derivation from Mother/Flag Completeness to the moving-heat system and spectral-measure law.
2. [`01_COMPLETENESS_AND_GAUGE.md`](01_COMPLETENESS_AND_GAUGE.md) — proof that the anchored frame preserves Theory-2 information, plus the gauge warning for the pair \((v,C^\sharp)\).
3. [`02_ANALYTIC_FRONTIER_AND_LESSONS.md`](02_ANALYTIC_FRONTIER_AND_LESSONS.md) — exact owners, the half-derivative seam, the monodromy target, no-go statements, and research lessons.
4. [`audits/interaction_frame_algebra.py`](audits/interaction_frame_algebra.py) — finite-dimensional sign/algebra audit for the interaction-frame identities.

## Working perspective

Throughout the notes, \(u\), equivalently \(E_u\) or the full shifted flag \(\Sigma(u)\), remains the complete physical state.  The anchored frame \(U_t=-\nabla_uU\), \(U(t_0)=I\), is used to expose the moving heat geometry while retaining its inverse/gauge.  Spectral stocks, work, traffic, moments and packets are then read from that state when they sharpen an estimate.  The intended direction of travel is toward coercivity, compactness or rigidity; merely finding another renderer of the same complete information is useful bookkeeping, but not by itself a new endpoint mechanism.

## Core dependencies

- [`core/spectral_signature/MOTHER_COMPLETENESS_THEOREM.md`](../../../core/spectral_signature/MOTHER_COMPLETENESS_THEOREM.md)
- [`core/spectral_signature/SPECTRAL_FLAG_SIGNATURE.md`](../../../core/spectral_signature/SPECTRAL_FLAG_SIGNATURE.md)
- [`core/spectral_signature/HALF_DERIVATIVE_POLAR_KORN_BRIDGE.md`](../../../core/spectral_signature/HALF_DERIVATIVE_POLAR_KORN_BRIDGE.md)

The interaction frame is therefore a **Theory-2-preserving application layer**, not a replacement for Theory 2.
