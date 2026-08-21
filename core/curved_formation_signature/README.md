# Core 3 — Curl-Spectral Formation Geometry

Core 3 is the canonical synthesis layer between the repository's two parent structures:

- [Metric–Lie / Hodge formation core](../metric_lie_hodge/README.md): the physical metric-Lie/curl datum generates the Navier--Stokes formation law;
- [Spectral Signature Core](../spectral_signature/README.md): the mother and shifted spectral flag encode the complete smooth periodic state modulo the known Killing/Galilean sector.

The current Core 3 is stronger than the original bridge between those theories.

Its central structural picture is now

\[
\boxed{
\text{formation geometry}
\longrightarrow
\text{curl spectral reduction}
\longrightarrow
\text{differential spectral signature}
\longrightarrow
\text{generic reconstruction of formation geometry}.
}
\]

The last arrow is the newest result.  It is **not yet an infinite-dimensional theorem**.  It is a conditional exact reconstruction mechanism supported by a broad adversarial executable campaign.

---

## 1. Three levels of completeness

Core 3 now distinguishes three logically different claims.

### Level A — state completeness

On the canonical smooth periodic physical core,

\[
\boxed{
E_u=[\nabla_u,C]
\quad\Longleftrightarrow\quad
u=u\ \text{modulo Killing/Galilean symmetry}.
}
\]

This is inherited from the spectral-signature completeness theorem.

It says the mother is a complete **state sensor**.

### Level B — differential spectral geometry

Treat

\[
E=d_\nabla C
\]

as a one-form and differentiate again:

\[
\boxed{
K:=d_\nabla E=d_\nabla^2C=[R,C].
}
\]

The first tower is

\[
\boxed{
C
\xrightarrow{d_\nabla}
E
\xrightarrow{d_\nabla}
K=[R,C]
\xrightarrow{d_\nabla}
R\wedge E
\xrightarrow{d_\nabla}\cdots,
\qquad d_\nabla R=0.
}
\]

This gives the signature a genuine differential-geometric structure rather than only a state encoding.

### Level C — formation-geometry reconstruction

The newest campaign asks whether the differential signature can reconstruct the connection that generated it.

In a curl spectral frame,

\[
\boxed{
\nabla=V+B,
\qquad
[V,C]=0,
\qquad
E=[B,C].
}
\]

Thus \(E\) reconstructs the cross-sheet part \(B\).  The missing part \(V\) acts within curl eigensheets.

The curvature mother supplies the second measurement:

\[
\boxed{
K=K_B+\mathcal A_{C,E}(V),
}
\]

where, in the exact finite metric-Lie setting, \(\mathcal A_{C,E}\) is linear in the hidden stabilizer connection.

Whenever this **Codazzi observability map** is injective modulo genuine stabilizer symmetry,

\[
\boxed{
(g,C,E,K)
\Longrightarrow
\nabla
\Longrightarrow
T,R,\mathcal J.
}
\]

This is the current geometric-completeness mechanism.

Read [GEOMETRIC_COMPLETENESS.md](GEOMETRIC_COMPLETENESS.md) for the complete statement, tribunals, failures and theorem target.

---

## 2. Why curvature can recover information that mother misses

Curl decomposes the metric connection into:

- \(V\): motion inside the same signed curl eigensheet;
- \(B\): mixing between distinct eigensheets.

For spectral blocks \(i,j\),

\[
E_{ij}=(\lambda_j-\lambda_i)B_{ij}.
\]

Therefore

\[
B_{ij}=\frac{E_{ij}}{\lambda_j-\lambda_i}
\qquad(\lambda_i\neq\lambda_j).
\]

But if \(\lambda_i=\lambda_j\), the mother is blind to that connection coefficient.

The physical helical tribunal creates exactly such a same-signed-curl Fourier transition.  The mother sees zero in that channel.  A cross-sheet curvature loop then recovers the hidden coefficient through \(K=[R,C]\).

Across 80 independent resonant triads:

\[
\text{median recovery error}
=
9.56\times10^{-16},
\]

with noise slope

\[
1.0004.
\]

So the new mechanism is not merely metaphorical:

\[
\boxed{
E\text{ sees first-order sheet mixing; }K\text{ can reveal within-sheet connection through holonomy.}
}
\]

---

## 3. Curl-spectral Gauss–Codazzi–Ricci split

The spectral decomposition also organizes curvature:

\[
R=R_\parallel+R_\perp,
\qquad
[R_\parallel,C]=0.
\]

The within-sheet sector has the Gauss/Ricci form

\[
R_\parallel
=
[V,V]+\Pi_\parallel[B,B]
\]

in the constant spectral-frame model.

The cross-sheet sector \(R_\perp\) is Codazzi-like, and

\[
\boxed{
K=[R,C]=[R_\perp,C].
}
\]

Thus \(K\) is the **cross-sheet curvature mother**, not the entire curvature.

This distinction is crucial.  Within-sheet curvature can be invisible at degree two and re-enter through higher Bianchi levels.

See [CURL_SPECTRAL_REDUCTION.md](CURL_SPECTRAL_REDUCTION.md).

---

## 4. Generic completeness has singular spectral strata

The new reconstruction result is intentionally not written as an unconditional theorem.

A phase diagram swept:

- 9 exact six-dimensional Lie-algebra families;
- 9 curl multiplicity patterns;
- 6 randomized metrics per family/pattern.

Among non-scalar family/pattern combinations,

\[
\boxed{68/72}
\]

were full rank for every tested seed.

All persistent failures occurred at the highly degenerate pattern

\[
\boxed{5+1}.
\]

Examples of remaining degree-two nullity were

\[
2,\quad2,\quad11,\quad1.
\]

Higher covariant degrees removed several of those kernels.  In the hardest tested case,

\[
\boxed{11\to9\to6}
\]

through \(K,dK,d^2K\).

Even the maximal exterior tower plus Jacobi/Bianchi retained a five-dimensional **linearized** kernel.  But nonlinear probing showed those directions to be quadratically visible:

\[
\boxed{
\text{sensor residual}\sim t^2
}
\]

with fitted slopes equal to \(2.0000000000\) at numerical precision.

Therefore Core 3 distinguishes:

\[
\boxed{
\text{linearized singularity}
\neq
\text{finite non-uniqueness}.
}
\]

This is now part of the canonical interpretation, not an inconvenient exception hidden in research notes.

---

## 5. Scalar curl is an exact dark control

If

\[
C=\lambda I,
\]

then

\[
E=0,
\qquad
K=0.
\]

The entire commutator-based spectral geometry collapses.

In the six-dimensional negative controls all

\[
90/90
\]

hidden connection coefficients remain invisible.

Thus nontrivial curl spectral separation is essential to the Theory-2 reconstruction mechanism.

---

## 6. The metric is part of the data

The signature image is a linear representation space.  It is not intrinsically curved as an ordinary Euclidean embedding.

The curvature belongs to the transported formation connection.

Correspondingly, the correct geometric inverse data are

\[
\boxed{
(g_\Sigma,C,E,K),
}
\]

not raw matrices \((C,E,K)\) in an arbitrary chart.

Non-orthogonal coordinate tests with condition numbers up to \(10^3\) recover the same connection when the transported metric is carried.  Pretending the signature chart is Euclidean produces order-one reconstruction errors around \(0.20\)–\(0.53\).

See [SIGNATURE_METRIC_DYNAMICS.md](SIGNATURE_METRIC_DYNAMICS.md) and [GEOMETRIC_COMPLETENESS.md](GEOMETRIC_COMPLETENESS.md).

---

## 7. Viscosity is a separate scalar calibration

The differential spectral geometry reconstructs the tested **reversible formation geometry**.

It does not determine viscosity \(\nu\).

Two systems can have identical

\[
(g,C,E,K)
\]

and different

\[
\mathcal L_{\nu,u}=\mathcal J_u-\nu C^2.
\]

Once the geometry is known, a single generic observed time tangent recovers \(\nu\) in the finite tribunal with linear noise stability.

The current architecture is therefore

\[
\boxed{
\text{differential spectral geometry}
+
\nu
=
\text{full formation law}.
}
\]

This separation is conceptually useful: Theory 2 reconstructs geometry; the irreversible strength is one additional physical scalar.

---

## 8. Shifted spectral flags remain tomography of the same geometry

The shifted family

\[
H_a=\operatorname{sgn}(C-aI)
\]

tomographs the mother and curvature action.

In particular,

\[
\boxed{
\frac12\int_{\mathbb R}[R,H_a]\,da=[R,C].
}
\]

The new reconstruction tribunal also fits only \(E\) and \(K\), then correctly predicts held-out readers

\[
[\nabla,f(C)],
\qquad
[R,f(C)],
\]

for polynomial, exponential, trigonometric, absolute-value, hinge and shifted-cut functions, as well as a held-out \(dK\) level.

Errors are at approximately \(10^{-15}\) in the exact finite test.

An \(E\)-only control misses a held-out curvature reader by \(0.931\).

This supports the interpretation that the reconstruction recovers a **generator of the spectral functional calculus**, not just a matrix interpolating the fitted observations.

---

## 9. Exact metric bridge

For the strain signature

\[
q_u(x,n)=n^TS(u)(x)n,
\]

the exact identities remain

\[
\boxed{
\langle u,v\rangle_{L^2}
=
15\langle\Lambda^{-1}q_u,\Lambda^{-1}q_v\rangle,
}
\]

and

\[
\boxed{
\langle Cu,Cv\rangle_{L^2}
=
15\langle q_u,q_v\rangle.
}
\]

Hence

\[
\boxed{
 g^{\Sigma}_{\rm kinetic}=15\dot H^{-1},
\qquad
 g^{\Sigma}_{\rm Dirichlet}=15L^2,
\qquad
(g^{\Sigma}_{\rm kinetic})^{-1}g^{\Sigma}_{\rm Dirichlet}=\Lambda^2.
}
\]

This is why the transported metric is structural rather than cosmetic.

---

## 10. Read Core 3 in this order

1. [GEOMETRIC_COMPLETENESS.md](GEOMETRIC_COMPLETENESS.md) — newest central result: state completeness versus geometric completeness, Codazzi inverse map, adversarial phase diagram, higher-degree completion, nonlinear singular observability, metric covariance and viscosity calibration.
2. [CURL_SPECTRAL_REDUCTION.md](CURL_SPECTRAL_REDUCTION.md) — curl sheets, orbit/stabilizer geometry, \(\nabla=V+B\), Gauss–Codazzi–Ricci split and Bianchi tower.
3. [FORMATION_SIGNATURE_EQUIVALENCE.md](FORMATION_SIGNATURE_EQUIVALENCE.md) — state-level forward/reverse bridge on a fixed physical formation core.
4. [SIGNATURE_METRIC_DYNAMICS.md](SIGNATURE_METRIC_DYNAMICS.md) — exact transported kinetic/Dirichlet metrics and heat as their Riesz ratio.
5. [CURVED_CURL_MODULE.md](CURVED_CURL_MODULE.md) — curvature-corrected mother bracket, holonomy and shifted-cut curvature tomography.
6. [PHYSICAL_RIGIDITY_AND_IDENTIFIABILITY.md](PHYSICAL_RIGIDITY_AND_IDENTIFIABILITY.md) — abstract dark sectors, physical locality, Galerkin warnings, topology and domain typing.
7. [DEEP_GEOMETRY_LESSONS.md](DEEP_GEOMETRY_LESSONS.md) — durable lessons and failed interpretations.
8. [THEOREM_STATUS_AND_SCOPE.md](THEOREM_STATUS_AND_SCOPE.md) — exact identities, inherited theorems, executable evidence, candidate statements and explicit nonclaims.
9. [HISTORY_AND_FALSIFICATION.md](HISTORY_AND_FALSIFICATION.md) — chronological record of how the theory changed when experiments contradicted attractive but false formulations.

---

## 11. Canonical reproduction

Run the original bridge / metric / physical-curvature tribunals:

```bash
python core/curved_formation_signature/audits/metric_lie_spectral_unification.py
python core/curved_formation_signature/audits/signature_to_formation_microlocal.py
python core/curved_formation_signature/audits/signature_core_identifiability.py
python core/curved_formation_signature/audits/physical_axiom_rigidity.py
python core/curved_formation_signature/audits/signature_metric_heat_bridge.py
python core/curved_formation_signature/audits/galerkin_probe_lie_failure.py
python core/curved_formation_signature/audits/curved_curl_dg_physical.py
python core/curved_formation_signature/audits/physical_curvature_flag_tomography.py
```

Run the curl-spectral geometry tribunals:

```bash
python core/curved_formation_signature/audits/curl_solder_cartan_structure.py
python core/curved_formation_signature/audits/curl_orbit_stabilizer.py
python core/curved_formation_signature/audits/spectral_gauss_codazzi_ricci.py
python core/curved_formation_signature/audits/full_physical_gauss_codazzi.py
python core/curved_formation_signature/audits/full_physical_vertical_curvature.py
python core/curved_formation_signature/audits/full_physical_vertical_degree4.py
python core/curved_formation_signature/audits/representation_curvature_not_embedding_curvature.py
python core/curved_formation_signature/audits/harmless_class_curvature.py
python core/curved_formation_signature/audits/harmonic_zero_mode_signature.py
python core/curved_formation_signature/audits/boundary_metric_typing.py
python core/curved_formation_signature/audits/bch_vs_geometric_curvature.py
python core/curved_formation_signature/audits/orientation_double_cover.py
python core/curved_formation_signature/audits/blind_reversible_irreversible_split.py
python core/curved_formation_signature/audits/connection_lift_curvature_recovery.py
```

Run the geometric-completeness campaign:

```bash
python core/curved_formation_signature/audits/ek_exact_lie_reconstruction.py
python core/curved_formation_signature/audits/physical_helical_resonant_recovery.py
python core/curved_formation_signature/audits/ek_rank_phase_diagram.py
python core/curved_formation_signature/audits/ek_higher_degree_completion.py
python core/curved_formation_signature/audits/ek_maximal_tower_stabilizer.py
python core/curved_formation_signature/audits/ek_bianchi_integrability_completion.py
python core/curved_formation_signature/audits/ek_cartan_integrability_closure.py
python core/curved_formation_signature/audits/ek_nonlinear_singular_observability.py
python core/curved_formation_signature/audits/ek_metric_covariant_reconstruction.py
python core/curved_formation_signature/audits/ek_28d_sparse_codazzi_recovery.py
python core/curved_formation_signature/audits/ek_heldout_spectral_prediction.py
python core/curved_formation_signature/audits/ek_minimal_viscosity_calibration.py
```

The suite deliberately includes negative controls and singular cases.  Passing the suite does not mean every test is a full-rank positive reconstruction; it means the code reproduces both the positive mechanism and the failures that delimit its scope.

---

## 12. Strongest current wording

The strongest canonical interpretation is now:

> **Core 3 is a curl-spectral differential observability geometry for the canonical physical Navier--Stokes formation core.**  The mother is complete for state on the smooth periodic class.  The full differential signature carries a spectral reduction of the connection.  In broad exact finite tests and direct physical helical interactions, curvature recovers connection information hidden from degree one.  At generic tested spectral points, \((g,C,E,K)\) reconstructs the formation connection and its reversible descendants.  High spectral degeneracy creates singular strata where higher degrees and nonlinear information matter.

This does **not** claim:

- a completed infinite-dimensional geometric-completeness theorem;
- that one state snapshot reconstructs the entire background geometry;
- that \(E+K\) is full rank at every spectral multiplicity;
- that a Jacobian kernel is automatically gauge;
- that nonzero \(E\), \(K\) or curvature is a blow-up indicator;
- that viscosity is encoded by reversible spectral geometry;
- global regularity of three-dimensional Navier--Stokes.
