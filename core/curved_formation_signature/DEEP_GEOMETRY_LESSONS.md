# Deep Geometry Lessons and Durable Negative Controls

This note is not a theorem list.  It records the interpretations that survived repeated adversarial testing.

---

## 1. Core 3 now has three different completeness questions

Do not collapse them.

### State completeness

\[
E_u\Longrightarrow u
\]

on the canonical smooth periodic physical core, modulo Killing/Galilean symmetry.

### Differential-geometric completeness

Does

\[
(C,E(\cdot),K(\cdot,\cdot),\ldots)
\]

recover the local formation connection?

### Dynamical completeness

Once the reversible geometry is known, is the full viscous formation law known?

The newest experiments say:

- state completeness is theorem-level in the parent core;
- geometric completeness is strongly supported generically but still a theorem candidate;
- viscosity remains one additional scalar calibration.

---

## 2. The mother is a spectral soldering-type form, not merely an observable

The strongest durable interpretation of

\[
E=d_\nabla C
\]

is that it converts physical directions into infinitesimal motion of the curl spectral frame.

For a direction \(u\),

\[
E_u=[\nabla_u,C].
\]

The map is linear in \(u\), and on the smooth mean-zero periodic class it is state-complete.

It is useful to call \(E\) a **soldering-type form**, but not literally the ordinary Cartan solder form: its codomain is operator-valued and the map is injective rather than an isomorphism onto the full operator space.

---

## 3. Curl spectral sheets are the right reduction

Write

\[
\nabla=V+B,
\qquad [V,C]=0.
\]

Then

\[
E=[B,C].
\]

This one identity explains several previously disconnected facts:

- why the mother is isospectral to first order;
- why spectral gaps control inversion;
- why same-eigenvalue connection channels are degree-one blind;
- why the curl commutant is only a first-order stabilizer;
- why curvature can reveal information that the mother misses.

The reduction is not a visualization trick.  It is the current organizing geometry of Core 3.

---

## 4. Curvature mother is a Codazzi sensor, not the whole curvature

With

\[
R=R_\parallel+R_\perp,
\qquad [R_\parallel,C]=0,
\]

we have

\[
K=[R,C]=[R_\perp,C].
\]

Therefore:

- \(R_\parallel\): within-sheet Gauss/Ricci/stabilizer curvature;
- \(R_\perp\): cross-sheet Codazzi curvature;
- \(K\): gap-weighted sensor of the cross-sheet curvature.

Never write \(K\) as if it were the complete curvature tensor.

---

## 5. The newest structural lesson: degree two measures hidden degree-one geometry

After \(E\) reconstructs \(B\), the remaining connection is \(V\in\operatorname{comm}(C)\).

In the exact finite metric-Lie setting,

\[
\boxed{
K=K_B+\mathcal A_{C,E}(V),
}
\]

with \(\mathcal A_{C,E}\) linear in \(V\).

This is the geometric-completeness mechanism.

Curvature is not merely “another invariant”.  It is a measurement equation for connection coefficients hidden from the mother.

The direct helical experiment confirms this physically: a same-signed-curl transition is exactly invisible to \(E\), while a cross-sheet \(K\)-loop recovers its amplitude at roundoff scale.

---

## 6. Generic does not mean universal

The rank phase diagram falsified universal degree-two completeness.

Broadly split curl spectra were full rank throughout the tested families.  Highly degenerate \(5+1\) spectra produced persistent kernels.

Therefore the correct mental model is a **stratified inverse geometry**:

\[
\boxed{
\text{generic regular strata}
\quad\text{and}\quad
\text{high-symmetry singular strata}.
}
\]

Any continuum theorem should expect this stratification rather than hide it under a global genericity phrase.

---

## 7. Higher covariant degrees are completion channels, not automatically new physics

At generic connection-constrained points, \(E+K\) can already close the inverse.

At degenerate points, however,

\[
K\to dK\to d^2K\to\cdots
\]

can reduce the hidden nullspace.

The hardest tested sequence was

\[
11\to9\to6.
\]

Thus higher degrees have a precise role:

> they refine observability where lower-degree spectral symmetry leaves a kernel.

Do not claim that each degree introduces an independent NS mechanism.

---

## 8. Bianchi and Jacobi are compatibility equations, not automatic uniqueness engines

It was tempting to believe that

\[
d_\nabla R=0
\]

or Jacobi would immediately eliminate every remaining hidden connection direction.

The hardest \(5+1\) nilpotent-plus-central case falsified that.

Second Bianchi left an 11-dimensional degree-two kernel unchanged.  Jacobi reduced it only to 7.  The maximal tower plus both still had a five-dimensional linearized kernel.

Therefore:

\[
\boxed{
\text{integrability constraints help observability but do not guarantee full-rank linearization.}
}
\]

---

## 9. Linearized blindness is not the same as nonlinear darkness

This is one of the most important new lessons.

The final five-dimensional linearized kernel was probed at finite amplitude.  The full sensor residual behaved as

\[
\boxed{
\mathrm{residual}\sim t^2.
}
\]

So those directions are invisible to first derivative but visible to second order.

A Jacobian rank test alone would have misclassified them as “gauge”.

Future work must distinguish:

- exact stabilizer/gauge;
- linearized kernel;
- higher-order visible singular directions;
- true finite collisions.

This distinction is more important than naming another curvature tensor.

---

## 10. Curved representation is not curved embedding

The signature image can be a flat linear subspace in ordinary additive coordinates.

The nonzero curvature belongs to the transported formation connection, not to the extrinsic shape of the image.

Therefore the correct phrase is:

\[
\boxed{
\text{linear signature representation carrying curved formation geometry}.
}
\]

Not:

\[
\text{the signature image is intrinsically curved as a vector subspace}.
\]

---

## 11. The metric is structural

A complete coordinate map does not canonically Euclideanize the formation geometry.

The correct data are

\[
(g_\Sigma,C,E,K,\ldots).
\]

Non-orthogonal reconstruction succeeds when \(g_\Sigma\) is carried and fails by order one when the same chart is treated as Euclidean.

This repeats the very first Core-3 falsification at a much deeper inverse level.

---

## 12. The first curl commutant is not the final gauge

At degree one,

\[
[V,C]=0
\]

makes \(V\) invisible.

But generic curvature data recover \(V\).

Therefore

\[
\operatorname{comm}(C)
\]

is only the initial stabilizer of the distinguished curl object.

True gauge/darkness must stabilize the complete differential-spectral geometry, and even a linearized stabilizer may disappear nonlinearly.

---

## 13. Kernel of curl is not gauge

A harmonic circulation can satisfy

\[
Cu=0
\]

while

\[
E_u\neq0.
\]

A constant Galilean direction can be dark.

Hence

\[
\boxed{
\ker C\neq\text{gauge kernel}.
}
\]

Topology and boundary extensions must therefore be handled by a typed Hodge/connection analysis rather than quotienting all curl-zero modes.

---

## 14. Signed curl is canonical but not the only complete state sensor

Experiments show that commutators with \(|C|\) can also be state-complete microlocally in suitable regimes.

So the right claim is not uniqueness of \(C\) among all possible sensors.

The right claim is:

> signed \(C\) is the canonical degree-one sensor selected by orientation, physical first-order normalization, the Stokes relation \(C^2\), and the existing completeness theorem.

This matters for novelty and for future generalization.

---

## 15. Orientation is a double cover of the same viscous dynamics

Changing

\[
C\mapsto-C
\]

leaves

\[
C^2
\]

and the unoriented formation law unchanged, while the signed mother/curvature tower changes orientation and the shifted flag reflects in threshold.

Thus signed curl geometry is an orientation double cover of the same underlying viscous dynamics.

---

## 16. Reversible geometry and viscosity should remain separate

The new geometric inverse reconstructs the reversible formation structure.

It does not contain \(\nu\).

This is not a defect.  It gives a cleaner architecture:

\[
\boxed{
\text{spectral formation geometry}
+
\text{scalar dissipation strength}
=
\text{full NS law}.
}
\]

A single generic time tangent calibrates \(\nu\) after geometry is known in the finite audit.

---

## 17. BCH descendants and formation curvature remain distinct

Euler--heat BCH objects and \([R,C]\) share the same parent data \((T,C)\), but they measure different structures.

One is a splitting/commutator descendant involving the symmetric \(C^2\) channel; the other is antisymmetric covariant holonomy of signed curl.

Keep both, but do not identify them.

---

## 18. Structural curvature is not a regularity alarm

2D, shear and Beltrami controls can carry nonzero ambient mother/curvature while remaining structurally harmless in the relevant self-interaction sense.

Therefore Core 3 does not interpret

\[
\|E\|,
\quad
\|K\|,
\quad
\|R\|
\]

as danger amplitudes by default.

Any connection to regularity must be established by a separate coercive or a priori theorem.

---

## 19. Boundary extension is a category change

Periodic self-adjoint curl syntax cannot simply be copied to domains with boundary.

The correct extension needs either:

- an \(L^2\)-compatible self-adjoint curl realization with explicit domain;
- or a Hodge/Stokes form formulation in which the metric, adjoint and harmonic sectors are typed.

The geometric-completeness programme inherits this warning fully.

---

## 20. Held-out prediction is a better test than fitted residual

A reconstruction that only reproduces \(E\) and \(K\) could still be an overfit.

The newest campaign therefore asks the recovered connection to predict:

- unseen \([\nabla,f(C)]\) readers;
- unseen \([R,f(C)]\) readers;
- shifted cuts;
- a higher Bianchi level;
- independent trajectories.

These held-out tests pass at roundoff in the exact full-rank models.

This should remain standard methodology for future Core-3 inverse claims.

---

## 21. Sparse information thresholds matter

The 28D stress laboratory leaves 1736 hidden connection coefficients after degree one.

Recovery fails continuously while the number of random curvature measurements remains below that count and collapses to near machine accuracy just after the equation count exceeds the hidden dimension.

This suggests a real observability problem with dimension/rank thresholds.

Future continuum work should therefore study the spectrum and Fredholm properties of the Codazzi observability operator, not merely prove formal identities.

---

## 22. The strongest durable wording

The current Core-3 summary should be:

\[
\boxed{
\textbf{curl-spectral differential observability of formation geometry}
}
\]

rather than merely “curved representation”.

The full hierarchy is

\[
\boxed{
\text{state completeness}
\to
\text{spectral reduction}
\to
\text{curvature observability}
\to
\text{generic formation-geometry reconstruction}.
}
\]

At high symmetry, the inverse becomes stratified and can require higher or nonlinear data.

That is the theory that survived the experiments.
