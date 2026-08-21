# History and Falsification

Core 3 did not emerge from a single successful derivation.  Its current form was forced by a sequence of attractive formulations that failed under stronger tests.

This file records those failures because they are part of the theory.

---

## 1. Starting point: two mature structures that looked separate

The repository first had two strong but apparently different objects.

The formation core started from

\[
(\mathfrak g_\sigma,g,T,C)
\]

and generated the connection and Navier--Stokes operator.

The spectral-signature core started from

\[
E_u=[\nabla_u,C]
\]

and showed that the mother/shifted flag reconstructs the smooth periodic state modulo Killing symmetry.

The first Core-3 question was modest:

> Is the signature merely compatible with the formation core, or is it a complete representation of the same dynamics?

The answer was stronger than expected, but every later strengthening required new falsification.

---

## 2. First unification: state and dynamics commute across the bridge

A blind finite physical algebra was built in which the reconstruction path retained only the metric-Lie tensor and curl.

From those data it rebuilt the connection, mother and shifted flag.  The reverse path recovered state and the state-dependent formation operator.  Independent trajectory integrations in physical and signature coordinates agreed at roundoff.

This established the first durable statement:

\[
\boxed{
\text{on a fixed physical core, the spectral signature carries the full state dynamics.}
}
\]

But the first false simplification appeared immediately.

---

## 3. Falsification 1: complete coordinates are not automatically Euclidean

The first reduced mother coordinates were treated as if their metric were the identity.

Formation identities failed by order one.

Transporting the correct Riesz metric restored them to roundoff.

The exact Sobolev bridge later explained why:

\[
L^2_u
\longleftrightarrow
15\dot H^{-1}_q,
\qquad
\|Cu\|_2^2
\longleftrightarrow
15L^2_q.
\]

Lesson:

\[
\boxed{
\text{coordinate completeness}\neq\text{metric equivalence without transporting }g.
}
\]

This warning later became essential for geometric reconstruction.

---

## 4. Falsification 2: the induced bracket is not the operator commutator

The tempting guess

\[
E_{[u,v]}=[E_u,E_v]
\]

failed at order one.

The correct identity is

\[
\boxed{
E_{[u,v]}
=
[\nabla_u,E_v]-[\nabla_v,E_u]-[R(u,v),C].
}
\]

Curvature was therefore not optional decoration.  It was required for the induced Lie geometry.

An infinitesimal-loop experiment then measured \([R,C]\) as actual curl holonomy.

---

## 5. Falsification 3: a state snapshot does not determine an arbitrary abstract universe

An exact dark-sector collision was constructed inside a degenerate curl eigenspace.

Two abstract metric-Lie cores could have:

- identical mother maps on the observed state;
- identical shifted flags;
- identical diagonal dissipative dynamics;

while their full Poisson operators differed by order one.

This killed

\[
\text{signature snapshot}
\Rightarrow
\text{arbitrary background core}.
\]

The surviving statement became fiberwise over the canonical physical NS category.

This distinction returns in the newest campaign: **state completeness is not geometric completeness**.

---

## 6. Falsification 4: arbitrary Galerkin projection can lie about geometry

Several finite Fourier libraries produced projected mother rank loss and large Jacobi defects.

A first higher-curvature experiment inside such a projected algebra failed badly.  The failure was not evidence against the continuum identity; the projected bracket was not a Lie bracket.

Repeating the experiment on full pseudospectral divergence-free fields restored Jacobi, Bianchi and curved-covariant identities at \(10^{-15}\)–\(10^{-13}\).

Methodological rule:

\[
\boxed{
\text{finite coordinate labs may stress inversion, but physical higher-geometry claims require faithful physical checks.}
}
\]

This is why the newest campaign separates the 28D sparse stress test from the full physical helical tribunal.

---

## 7. Curvature tomography closes the first synthesis

The shifted spectral family already tomographed the mother.  The next test showed

\[
\boxed{
\frac12\int[R,H_a]\,da=[R,C].
}
\]

Thus the same spectral machinery reads both first deformation and curvature action.

At this point Core 3 could be described as a curved formation--signature representation.

That wording was still too loose.

---

## 8. Falsification 5: “curved representation” does not mean a curved embedding

A linear image can be flat as an ordinary constant-metric vector subspace while carrying a nonzero transported formation connection.

An exact \(so(3)\) control showed:

- linear image curvature: zero;
- transported formation curvature: nonzero;
- transported match: roundoff.

The correct sentence became:

\[
\boxed{
\text{the signature is a linear representation carrying curved formation geometry.}
}
\]

The map is not being advertised as an extrinsically curved embedding.

---

## 9. Curl spectral sheets reveal what the mother is actually measuring

The next campaign decomposed the metric connection as

\[
\nabla=V+B,
\qquad
[V,C]=0.
\]

Then

\[
\boxed{
E=[B,C].
}
\]

This was the conceptual turning point.

The mother does not change the eigenvalues of curl.  It measures how the formation connection mixes the curl eigensheets.

The finite physical coordinate lab made the scale disparity vivid:

- skew connection dimension: 378;
- curl stabilizer dimension: 62;
- full isospectral orbit tangent dimension: 316;
- physical state image dimension: 28.

So the physical state distribution is a very special low-dimensional direction field inside a much larger curl orbit.

---

## 10. Gauss--Codazzi--Ricci structure appears

Curvature split as

\[
R=R_\parallel+R_\perp,
\qquad
[R_\parallel,C]=0.
\]

In the spectral frame,

\[
R_\parallel=[V,V]+\Pi_\parallel[B,B]
\]

and \(R_\perp\) is the cross-sheet/Codazzi sector.

Because

\[
K=[R,C]=[R_\perp,C],
\]

it became clear that \(K\) is not “the curvature”; it is the curvature mother that sees only the off-sheet component directly.

Full physical helical experiments confirmed the same split.

---

## 11. Falsification 6: the curl commutant is not the final gauge

At degree one,

\[
[V,C]=0
\]

makes \(V\) invisible to the mother.

It was tempting to call the entire curl commutant gauge.

Curvature destroyed that interpretation: generic within-sheet connection information reappears through cross-sheet loops.

The correct wording became:

\[
\boxed{
\operatorname{comm}(C)
\text{ is a first-order stabilizer, not the final gauge.}
}
\]

True darkness must stabilize the full generated differential-spectral data, not only \(C\).

---

## 12. Falsification 7: higher tower does not always mean new independent connection information

When curvature was treated as an independent unknown tensor, higher Bianchi degrees added rank.

But when curvature was constrained to come from a compatible connection, generic \(E+K\) already reconstructed the hidden connection in finite tests.

Thus the statement

\[
\text{every higher degree adds new physics}
\]

was rejected.

The better interpretation is:

> Higher degrees are additional observability/compatibility channels that matter especially at symmetry-degenerate strata.

---

## 13. Falsification 8: mother and curvature are not danger amplitudes

2D, Beltrami and shear controls have harmless/self-nonlinear structure while ambient \(E\) and \(K\) can be nonzero and even large.

Therefore

\[
E\neq0
\quad\text{or}\quad
K\neq0
\]

is not a singularity or blow-up criterion.

Core 3 is structural geometry first.  Any regularity application must be a separate theorem.

---

## 14. Falsification 9: zero curl is not gauge

A topological harmonic circulation can satisfy

\[
Cu=0
\]

while

\[
E_u\neq0.
\]

A constant Galilean mode can satisfy both

\[
Cu=0,
\qquad E_u=0.
\]

Thus

\[
\boxed{
\ker C\neq\ker(u\mapsto E_u)
}
\]

in general.

Gauge is controlled by interaction with the connection, not merely by curl eigenvalue zero.

---

## 15. Falsification 10: Euler--heat BCH descendants are not geometric curl curvature

The Euler--heat splitting descendants and \([R,C]\) share the same parent core \((T,C)\), but they are different tensors.

Beltrami and shear controls can have zero Euler--heat BCH descendant while the formation curvature mother is nonzero.

Therefore

\[
\boxed{
\text{BCH splitting defect}\neq[R,C].
}
\]

Theories should be unified through their common parent datum, not by renaming distinct descendants as each other.

---

# Campaign III — from state completeness to geometric completeness

## 16. New suspicion: perhaps Theory 2 can reverse-engineer the formation connection

Once

\[
E=[B,C]
\]

was understood, the remaining inverse problem became obvious.

Degree one gives \(B\).  What about the hidden stabilizer connection \(V\)?

The new question was

\[
\boxed{
(g,C,E,K)
\stackrel{?}{\Longrightarrow}
\nabla
\stackrel{?}{\Longrightarrow}
T,R,\mathcal J.
}
\]

This is categorically stronger than state completeness.

The campaign was designed to kill this hypothesis if possible.

---

## 17. First surprise: the hidden inverse is affine-linear in the exact metric-Lie model

In the left-invariant torsion-free metric-Lie tribunal, once \(B\) is fixed by \(E\), the curvature mother satisfies

\[
\boxed{
K=K_B+\mathcal A_{C,E}(V).
}
\]

The map \(\mathcal A_{C,E}\) is linear in the hidden within-sheet connection coefficients.

Why the quadratic part disappears is structural: pure vertical commutators remain in the curl stabilizer and are killed by the final commutator with \(C\).

The superposition residual was \(10^{-16}\).

This turned a potentially nonlinear reverse-engineering problem into a Codazzi observability problem.

---

## 18. Generic exact reconstruction succeeds

Four exact Lie-algebra families under randomized non-bi-invariant metrics produced

\[
\boxed{16/16}
\]

full-rank generic cases.

From only \(g,C,E,K\), the tribunal reconstructed:

\[
\nabla,\quad [\cdot,\cdot],\quad R,\quad\mathcal J,\quad\mathcal L_{\nu,u}
\]

at roundoff scale.

Independent 80-step trajectories agreed within

\[
5.02\times10^{-16}.
\]

Noise response was linear with slope

\[
1.008.
\]

This was the first strong evidence for formation-geometry completeness.

---

## 19. Physical helical tribunal: curvature sees a connection coefficient that mother sees as exactly zero

A full Fourier/helical experiment selected transitions with the same signed curl eigenvalue.

By construction the mother is exactly blind to that vertical coefficient.

A cross-sheet curvature loop recovered it.

Across 80 resonant triads:

\[
\text{median error}=9.56\times10^{-16},
\]

\[
\text{worst error}=3.51\times10^{-14},
\]

with noise slope \(1.0004\).

This was the decisive physical confirmation of the mechanism:

\[
\boxed{
\text{curvature can reveal first-order spectral blindness.}
}
\]

---

## 20. Falsification 11: \(E+K\) is not universally complete

The hypothesis was then attacked across 9 exact Lie-algebra families, 9 spectral multiplicity patterns and 6 random metrics.

The result was mostly positive but not universal:

\[
\boxed{68/72}
\]

non-scalar family/pattern combinations were full rank for every tested seed.

All persistent failures occurred at the highly degenerate multiplicity

\[
5+1.
\]

The hardest case retained 11 degree-two hidden directions.

Therefore the correct theory is **stratified**.

The statement

\[
(C,E,K)\text{ always determines }\nabla
\]

was explicitly rejected.

---

## 21. Higher tower repairs several degenerate failures

At \(5+1\), higher degrees were added exactly where degree two failed.

Several kernels closed completely at degree three.

The hardest case showed

\[
\boxed{11\to9\to6}.
\]

This gave higher Bianchi degrees a clearer role: not universal new mechanisms, but completion data on singular spectral strata.

---

## 22. Falsification 12: Bianchi or Jacobi do not automatically restore uniqueness

A natural hope was that integrability would close the remaining kernel.

It did for several families, but failed in the hardest nilpotent-plus-central case.

There:

\[
K:11,
\qquad
K+D R:11,
\qquad
K+\text{Jacobi}:7.
\]

Even the maximal tower plus Jacobi and Bianchi retained a five-dimensional linearized kernel.

So “Cartan equations automatically imply full-rank inverse” was rejected.

---

## 23. Falsification 13: a linearized kernel is not automatically a true dark family

The remaining five directions looked like possible gauge/non-uniqueness.

They were tested nonlinearly.

Along each random kernel direction,

\[
\boxed{
\text{full sensor residual}\sim t^2.
}
\]

Six independent fitted slopes were equal to \(2.0000000000\) at numerical precision.

Random finite sphere scans found no zero-residual collision.

Thus the linearized inverse is singular, but the nonlinear map still sees those directions at second order.

New lesson:

\[
\boxed{
\text{Jacobian blindness}\neq\text{finite darkness}.
}
\]

A geometric-completeness theorem may therefore need a stratified nonlinear formulation rather than a uniform inverse-function theorem.

---

## 24. Sparse 28D stress test reveals an observability threshold

The canonical 28D coordinate lab leaves 1736 within-sheet connection coefficients hidden after degree one.

Random scalar curvature projections were reduced until the inverse failed.

Recovery errors were roughly

\[
0.67,\ 0.51,\ 0.25
\]

while the system had fewer equations than unknowns.

When 5 projections per pair produced 1890 equations, just above 1736 hidden coefficients, the error collapsed to

\[
4.4\times10^{-10}.
\]

This resembles a genuine observability threshold rather than an accidental identity.

The result remains a coordinate stress test, not a faithful projected-Lie theorem.

---

## 25. Held-out readers show that the inverse reconstructs a generator

Only \(E\) and \(K\) were fitted.

The recovered connection then predicted unseen readers

\[
[\nabla,f(C)],
\qquad
[R,f(C)],
\]

shifted flags and a higher \(dK\) level at \(10^{-15}\).

An \(E\)-only control failed a curvature reader by \(0.931\).

This argues against the interpretation that the inverse simply overfits the supplied matrices.

---

## 26. Metric covariance survives; Euclideanization fails again

The new inverse was pushed through charts with condition numbers up to \(10^3\).

Carrying the transported metric reproduced the same connection up to conditioning error.

Pretending the chart was Euclidean failed by order one.

The first Core-3 lesson therefore survived the entire programme:

\[
\boxed{
\text{the metric is part of the signature geometry.}
}
\]

---

## 27. Final boundary: geometry does not contain viscosity

The reconstructed data determine the reversible formation geometry, not \(\nu\).

Two systems with the same \(g,C,E,K\) and different viscosity have different formation laws.

But after geometry is known, one generic time tangent calibrates \(\nu\) with linear noise stability.

The resulting architecture is

\[
\boxed{
\text{differential spectral geometry}
+
\nu
=
\text{full formation law}.
}
\]

This separation is cleaner than trying to force dissipation into the reversible geometric data.

---

## 28. What the third campaign changed permanently

Before this campaign, the strongest canonical phrase was

> the spectral signature is a complete curved representation of the physical formation core.

That is still true as a broad synthesis, but it is no longer the most informative wording.

The stronger and more precise current picture is:

\[
\boxed{
\textbf{Core 3 is a curl-spectral differential observability geometry.}
}
\]

Its hierarchy is now:

\[
\boxed{
\text{state completeness}
\to
\text{spectral differential geometry}
\to
\text{generic formation-geometry reconstruction}.
}
\]

The word **generic** and the distinction between **snapshot data** and **polarized differential data** are essential.

The hardest remaining theorem problem is no longer “find another mechanism”.  It is to characterize the continuum Codazzi observability operator, its singular spectral strata, nonlinear injectivity and true stabilizer.

---

## 29. Durable research rules learned from Core 3

The following rules should govern future work:

1. Never promote a finite projected bracket to physical Lie geometry without a Jacobi/physical check.
2. Never call a coordinate representation Euclidean unless the transported metric says so.
3. Never identify a commutant or kernel with gauge from one covariant degree alone.
4. Never infer finite non-uniqueness from a Jacobian kernel without nonlinear collision tests.
5. Never call a structural curvature magnitude a danger/blow-up quantity without a separate regularity theorem.
6. Never merge descendants merely because they share the same parent core.
7. When a reconstruction works, test held-out readers and trajectories rather than only fitted tensors.
8. When a generic theorem candidate appears, attack spectral degeneracy and symmetry before polishing the statement.
9. Keep viscosity typed separately from reversible geometry unless the data explicitly contain a dynamical calibration.
10. Preserve negative controls in the canonical suite; they are part of the theorem boundary.
