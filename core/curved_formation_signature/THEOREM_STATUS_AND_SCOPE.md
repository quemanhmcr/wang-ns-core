# Theorem Status and Scope

Core 3 now contains three different kinds of mathematical content and must keep them visibly separated:

1. exact differential/algebraic identities;
2. theorem-level state completeness inherited from the parent spectral-signature core;
3. a new **formation-geometry completeness candidate** supported by exact conditional reconstruction and extensive executable evidence.

The third item is powerful, but it is not yet an infinite-dimensional theorem.

---

## 1. Status legend

Throughout Core 3, claims should be read with the following labels.

### EXACT

An algebraic or differential identity once the operators, domains and connection are typed.

### INHERITED THEOREM

A theorem already established in one of the canonical parent cores and used here without re-proving it.

### CONDITIONAL EXACT

An exact finite/typed reconstruction statement whose conclusion follows if an explicitly defined observability operator is injective modulo stabilizer.

### EXECUTABLE EVIDENCE

A numerical or exact-computational tribunal that supports, falsifies or delimits a candidate statement.

### OPEN

A continuum theorem, boundary extension, quotient theorem, regularity consequence or novelty statement not proved by the present corpus.

---

## 2. EXACT formation identities

On the typed smooth periodic physical formation core,

\[
\mathcal C_{NS}
=(\mathfrak g_\sigma,g,T,C),
\qquad C=\operatorname{curl},
\]

the metric and Lie tensor reconstruct the Levi--Civita connection through Koszul:

\[
2\langle\nabla_ab,c\rangle
=
\langle[a,b],c\rangle
-
\langle[b,c],a\rangle
+
\langle[c,a],b\rangle.
\]

The formation operator is

\[
\mathcal L_{\nu,u}
=
\mathcal J_u-\nu C^2.
\]

The mother is

\[
\boxed{
E=d_\nabla C,
\qquad E_u=[\nabla_u,C].
}
\]

The curvature-corrected mother bracket is

\[
\boxed{
E_{[u,v]}
=
[\nabla_u,E_v]
-
[\nabla_v,E_u]
-
[R(u,v),C].
}
\]

The covariant square is

\[
\boxed{
d_\nabla^2C=[R,C].
}
\]

Writing

\[
K=[R,C],
\]

the next Bianchi relation is

\[
\boxed{
d_\nabla K=R\wedge E.
}
\]

The second Bianchi identity is

\[
\boxed{
d_\nabla R=0.
}
\]

These are standard connection/endomorphism-bundle identities once the NS datum \((g,T,C)\) has selected the distinguished connection and curl object.  Core 3 does not claim novelty for the abstract Bianchi calculus itself.

---

## 3. EXACT spectral reduction formulas

In a typed spectral frame for self-adjoint \(C\), decompose the metric connection into the curl commutant and its off-sheet complement:

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

For spectral blocks with eigenvalues \(\lambda_i,\lambda_j\),

\[
E_{ij}
=(\lambda_j-\lambda_i)B_{ij}.
\]

Hence off the commutant,

\[
\boxed{
B_{ij}
=
\frac{E_{ij}}{\lambda_j-\lambda_i}
\qquad(\lambda_i\neq\lambda_j).
}
\]

Similarly, if

\[
R=R_\parallel+R_\perp,
\qquad
[R_\parallel,C]=0,
\]

then

\[
\boxed{
K=[R,C]=[R_\perp,C].
}
\]

Thus degree one determines cross-sheet connection, and degree two measures cross-sheet curvature.

---

## 4. EXACT shifted-cut curvature tomography

Whenever the spectral layer-cake representation is typed,

\[
H_a=\operatorname{sgn}(C-aI)
\]

satisfies

\[
\boxed{
\frac12\int_{\mathbb R}[R,H_a]\,da=[R,C].
}
\]

This is the curvature analogue of the mother tomography already used by the spectral-signature core.

---

## 5. INHERITED THEOREM — state completeness

Core 3 inherits from the canonical spectral-signature theorem that, on the smooth mean-zero periodic physical class,

\[
\boxed{
E_u\Longrightarrow u
}
\]

modulo the known Killing/Galilean sector, with an explicit reconstruction through the strain signature/principal symbol.

The full shifted flag also reconstructs the mother and hence the state.

This is **state completeness**.

It must not be silently upgraded to background-geometry completeness from a single state snapshot.

---

## 6. EXACT metric bridge inherited by Core 3

For

\[
q_u(x,n)=n^TS(u)(x)n,
\]

polarization of the parent Sobolev identity gives

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

Therefore

\[
\boxed{
 g^{\Sigma}_{\rm kinetic}=15\dot H^{-1},
\qquad
 g^{\Sigma}_{\rm Dirichlet}=15L^2,
\qquad
(g^{\Sigma}_{\rm kinetic})^{-1}g^{\Sigma}_{\rm Dirichlet}=\Lambda^2.
}
\]

This is why geometric reconstruction must carry \(g_\Sigma\).  Raw Euclidean signature coordinates are not canonical.

---

## 7. CONDITIONAL EXACT — Codazzi reconstruction of the hidden connection

The newest exact algebraic statement is a conditional one.

After \(E\) determines the cross-sheet connection \(B\), write

\[
\nabla=B+V,
\qquad
V\in\mathfrak h_C:=\operatorname{comm}(C)\cap\mathfrak{so}.
\]

In the exact finite metric-Lie / left-invariant torsion-free setting used by the canonical reconstruction audit, the curvature mother has the form

\[
\boxed{
K=K_B+\mathcal A_{C,E}(V),
}
\]

where \(\mathcal A_{C,E}\) is linear in the unknown stabilizer-valued connection coefficients.

The pure quadratic vertical curvature term lies in the curl commutant and disappears after applying \([\cdot,C]\); the remaining terms are affine-linear in \(V\).

Therefore:

> **Conditional reconstruction statement.** If \(\mathcal A_{C,E}\) is injective modulo the genuine stabilizer, then \((g,C,E,K)\) determines \(V\), hence the complete connection \(\nabla=B+V\).  The torsion-free bracket, Lie tensor, full curvature and reversible Poisson/formation operator are then reconstructed.

This implication is exact once the hypotheses and category are fixed.

What is **not** yet a theorem is that the corresponding infinite-dimensional physical NS observability operator is generically injective on an optimal function space.

---

## 8. EXECUTABLE EVIDENCE — exact metric-Lie reconstruction

`ek_exact_lie_reconstruction.py` tested four exact Lie-algebra families under randomized non-bi-invariant metrics.

Results:

- full Codazzi rank in \(16/16\) generic tested cases;
- affine-linearity residual \(\sim10^{-16}\);
- worst connection reconstruction error \(3.97\times10^{-15}\);
- bracket, full curvature, Poisson and formation operator reconstructed at roundoff scale;
- independently integrated 80-step trajectories matched within \(5.02\times10^{-16}\);
- noise slope \(1.008\).

This is unusually strong finite exact evidence for the conditional reconstruction mechanism.

---

## 9. EXECUTABLE EVIDENCE — direct physical helical recovery

`physical_helical_resonant_recovery.py` avoids using a projected finite Lie algebra as the main evidence.

It selects a same-signed-curl Fourier transition for which the hidden connection coefficient is exactly invisible to \(E\), then uses a cross-sheet physical curvature loop to reconstruct it from \(K\).

Across 80 independent resonant triads:

\[
\text{median error}=9.56\times10^{-16},
\]

\[
\text{worst error}=3.51\times10^{-14},
\]

with noise slope \(1.0004\).

This is the strongest direct physical evidence that curvature resolves first-order spectral blindness.

---

## 10. EXECUTABLE EVIDENCE — generic rank with singular strata

`ek_rank_phase_diagram.py` sweeps 9 Lie-algebra families, 9 spectral multiplicity patterns and 6 randomized metrics.

Among 72 non-scalar family/pattern combinations,

\[
\boxed{68/72}
\]

were full rank for every tested seed.

All persistent failures were concentrated at the highly degenerate pattern

\[
5+1.
\]

The universal statement

\[
(C,E,K)\Longrightarrow\nabla\quad\text{for every spectral multiplicity}
\]

is therefore **falsified**.

The current claim is generic and stratified.

---

## 11. EXACT NEGATIVE CONTROL — scalar curl

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

The rank campaign correctly leaves the complete hidden connection dark.

In the six-dimensional controls this means

\[
90/90
\]

hidden coefficients remain unobservable.

Any formulation of geometric completeness must therefore assume nontrivial spectral separation and cannot be purely formal in \([\cdot,C]\).

---

## 12. EXECUTABLE EVIDENCE — higher-degree completion

At rank-deficient \(5+1\) points, the tower

\[
K,\quad dK,\quad d^2K,\ldots
\]

was tested as additional observability data.

Three families closed completely at degree three.  In the hardest \(\mathfrak h_3\oplus\mathbb R^3\) case,

\[
\boxed{11\to9\to6}
\]

through degrees two, three and four.

The maximal available exterior tower retained a six-dimensional linearized kernel.

Thus higher degrees can add rank, but they are not asserted to add independent physical mechanisms at generic points.

---

## 13. EXECUTABLE NEGATIVE CONTROL — Bianchi/Jacobi do not automatically close every kernel

Several tempting stronger claims were explicitly falsified.

Second Bianchi and Jacobi close some high-degeneracy kernels, but in the hardest \(\mathfrak h_3\oplus\mathbb R^3\) case:

- \(K\) nullity: \(11\);
- \(K+D R\) nullity: \(11\);
- \(K+\)Jacobi nullity: \(7\).

The maximal tower plus Jacobi and Bianchi still retains a five-dimensional **linearized** kernel.

Therefore neither

\[
\text{Bianchi alone}\Rightarrow\text{uniqueness}
\]

nor

\[
\text{maximal linearized tower}\Rightarrow\text{full rank}
\]

is a canonical claim.

---

## 14. EXECUTABLE EVIDENCE — nonlinear visibility of a linearized kernel

`ek_nonlinear_singular_observability.py` probes the remaining five-dimensional linearized kernel.

Along random kernel directions \(w\), the maximal-tower-plus-Jacobi residual behaves as

\[
\boxed{
\|\mathcal S(V_0+tw)-\mathcal S(V_0)\|\sim c(w)t^2.
}
\]

The fitted slopes across all tested directions equal \(2.0000000000\) at numerical precision.

Random finite sphere scans found no machine-zero collision.

This supports, but does not prove, local nonlinear injectivity at that singular stratum.

The key canonical distinction is

\[
\boxed{
\text{Jacobian kernel}\neq\text{proved finite gauge/non-uniqueness}.
}
\]

---

## 15. EXECUTABLE EVIDENCE — coordinate covariance

`ek_metric_covariant_reconstruction.py` applies non-orthogonal charts with condition numbers up to \(10^3\).

With the transported metric, the same geometric connection is reconstructed, with numerical loss explained by chart conditioning.

If the chart is falsely Euclideanized, errors become order one.

Thus the candidate geometric-completeness data are intrinsically

\[
\boxed{(g_\Sigma,C,E,K)}
\]

rather than coordinate matrices alone.

---

## 16. EXECUTABLE EVIDENCE — 28D sparse information threshold

The canonical 28D coordinate stress lab has curl multiplicities

\[
2,6,6,6,6,2
\]

and

\[
1736
\]

connection coefficients hidden from degree one.

Twelve random scalar curvature projections per state pair reconstruct all hidden coefficients with error \(2.75\times10^{-12}\), and the descendants \(\nabla,T,\mathcal J,\mathcal L\) at roughly \(4\times10^{-13}\).

A measurement-density sweep exhibits a sharp practical transition when the number of scalar curvature measurements first exceeds the number of hidden coefficients.

This is coordinate-lab stress evidence only; it is not promoted to a finite projected Lie theorem because arbitrary projection can violate Jacobi.

---

## 17. EXECUTABLE EVIDENCE — held-out spectral functional calculus

After fitting only \(E\) and \(K\), the reconstructed connection predicts held-out readers

\[
[\nabla,f(C)]
\quad\text{and}\quad
[R,f(C)]
\]

for polynomial, exponential, trigonometric, absolute-value, hinge and shifted-cut functions, plus a held-out \(dK\) level.

Errors are approximately \(10^{-15}\).

An \(E\)-only control misses a curvature reader by \(0.931\).

This supports the interpretation that the reconstructed object is the underlying spectral generator, not merely an overfit to \(E,K\).

---

## 18. Viscosity status

The reversible differential geometry does not determine \(\nu\).

Two systems can have identical

\[
(g,C,E,K)
\]

but different formation operators because

\[
\mathcal L_{\nu,u}=\mathcal J_u-\nu C^2.
\]

`ek_minimal_viscosity_calibration.py` verifies that once the reversible geometry is known, one generic observed time tangent recovers the scalar \(\nu\) with linear noise stability in the finite tribunal.

Thus the candidate full-data architecture is

\[
\boxed{
\text{reversible spectral geometry}+\nu
=\text{formation law}.
}
\]

---

# Campaign IV — presentation bootstrap status

## 19. EXACT in a fixed finite spectral representation — spectral polynomial relation

If the distinguished curl operator in a fixed finite spectral representation has minimal polynomial \(p\), then

\[
\boxed{p(C)=0}
\]

is exact.

In the canonical 28-dimensional base window,

\[
p(x)=(x^2-1)(x^2-2)(x^2-3),
\]

so

\[
C^6-6C^4+11C^2-6I=0.
\]

This is a finite spectral identity, not a claim that continuum curl satisfies this finite polynomial.

---

## 20. EXACT — differentiated spectral relation

Whenever

\[
E=[A,C],
\]

commuting \(p(C)=0\) with \(A\) gives

\[
\boxed{Dp_C(E)=0.}
\]

In the base window this is

\[
\sum_{j=0}^{5}C^jEC^{5-j}
-6\sum_{j=0}^{3}C^jEC^{3-j}
+11(EC+CE)=0.
\]

This identity is exact for the represented operator pair.

---

## 21. EXECUTABLE EVIDENCE — one generic mother generates the full operator algebra

In the 28-dimensional physical coordinate laboratory,

\[
\dim\operatorname{Alg}(C)=6,
\]

while one generic mother produces

\[
\boxed{\dim\operatorname{Alg}(C,E_u)=784=28^2.}
\]

The word-span profile is

\[
1,3,7,15,31,63,125,246,483,784,
\]

reaching the full matrix algebra at the information-theoretic minimum possible depth \(9\) for two generators.

An SVD audit on all \(1023\) words through depth \(9\) confirms rank \(784/784\) across four generic states.

This is finite algebraic irreducibility evidence, not a continuum Burnside theorem.

---

## 22. EXECUTABLE EVIDENCE — a three-law finite-window presentation

In the base physical window, the first non-spectral relation is

\[
\boxed{
Q(C,E)
=(C^2-I)(C^2E+EC^2-5E)(C^2-I)=0.
}
\]

Across four generic states, the two-sided ideal generated by

\[
p(C),\qquad Dp_C(E),\qquad Q(C,E)
\]

has exactly the same dimension as the complete numerical relation space through word degree \(8\):

\[
2=2,
\qquad
9=9,
\qquad
28=28.
\]

At degree \(9\), additional relations appear exactly when the finite \(28\times28\) representation reaches its dimension ceiling.

This supports a finite generator--relations presentation before saturation.

The fixed polynomial \(Q\) is **not** universal across larger helical windows.

---

## 23. EXECUTABLE EVIDENCE — one-snapshot law transfer and rival-law identification

The complete degree-\(8\) relation space learned from one generic physical mother transfers to \(80\) unseen physical states with minimum principal cosine

\[
0.9999999999999991.
\]

After quotienting the common spectral/control relation space, four physical-specific relation directions remain.  They annihilate unseen physical states at approximately \(10^{-16}\) while a same-spectrum generic off-block law leaves a residual of order \(10^{-7}\).

A relation-only classifier distinguishes:

- all three same-spectrum, same-forbidden-count codimension-one rival laws in the physical regime;
- an independent eight-law same-spectrum/same-count stress family with \(32/32\) correct classifications.

Thus the tested relation ideal behaves as a state-independent interaction-law fingerprint.

---

## 24. EXECUTABLE EVIDENCE — exact-helical sparse law holography

The Campaign-IV results are not restricted to the projected 28-dimensional bracket.

In exact helical Fourier action:

- the base-window operators satisfy \(p(C)=0\), \(Dp_C(E)=0\), and \(Q(C,E)=0\) at normalized residuals \(10^{-19}\)--\(10^{-21}\);
- in a \(160\)-node window, a generic state supported on only three Fourier directions reconstructs the complete first physical quotient relation and all \(12\) forbidden root transitions;
- the same fixed three support directions realize the complete root-level interaction category in ten tested windows from \(52\) to \(512\) helical nodes;
- forbidden-channel count grows from \(2\) to \(324\), while the tested support complexity remains three;
- finite-window root-level interaction categories are projectively consistent under every tested refinement from \(R^2=3\) through \(R^2=16\).

These results motivate a sparse law-holography and projective-presentation theorem programme.

They do not prove a continuum inverse-limit theorem.

---

## 25. EXECUTABLE NEGATIVE CONTROL — one snapshot does not determine polarized geometry

Campaign IV explicitly falsifies

\[
(C,E_u)\Longrightarrow\text{full formation geometry}.
\]

Two distinct metric-compatible connection one-forms are constructed with the same training

\[
(C,E_{u_*},\nabla_{u_*})
\]

to approximately \(10^{-15}\), and with the same tested presentation category.

On unseen directions they differ by order-one fractions:

\[
\text{mother median difference}=17.2\%,
\]

\[
\text{connection median difference}=22.4\%.
\]

Therefore the canonical Campaign-IV claim is

\[
\boxed{
\text{snapshot}\rightsquigarrow\text{syntax/category},
\qquad
\text{not full polarized coefficients}.
}
\]

---

## 26. EXECUTABLE EVIDENCE — curvature calibrates hidden geometry beyond the snapshot

The previous ambiguity is refined to a continuous family of metric-compatible connections that share the same training snapshot.

One generic scalar curvature polarization

\[
\langle z,K(u_*,v)w\rangle
\]

recovers the hidden family parameter in \(80/80\) trials, with median error \(9.1\times10^{-15}\), worst error \(4.1\times10^{-13}\), and noise slope \(0.995\).

This supports the hierarchy

\[
\boxed{
\text{snapshot}\Rightarrow\text{syntax},
\qquad
\text{curvature polarization}\Rightarrow\text{geometry calibration}.
}
\]

---

## 27. Strongest current canonical interpretation

The present corpus supports the following layered statement:

> The canonical physical Navier--Stokes formation core admits a curl-spectral differential representation.  The mother is theorem-level complete for state on the smooth periodic class.  The full polarized differential signature generically reconstructs formation geometry in the tested finite categories, with singular spectral strata retained explicitly.  Campaign IV adds a different phenomenon: one generic mother snapshot can generate an irreducible operator language and reveal state-independent interaction relations in finite and exact-helical spectral windows.  The snapshot does not determine the full polarized connection; curvature supplies precisely the missing calibration information in explicit collision tribunals.

The canonical hierarchy is now

\[
\boxed{
\text{state completeness}
\to
\text{differential geometry}
\to
\text{formation-geometry observability}
\to
\text{presentation bootstrap}.
}
\]

The recommended name for Campaign IV is

\[
\boxed{
\textbf{Curl--Mother Presentation Bootstrap}.
}
\]

A compact operational summary is

\[
\boxed{
\text{snapshot}\Rightarrow\text{syntax},
\qquad
\text{polarized }E,K\Rightarrow\text{geometry},
\qquad
\nu\Rightarrow\text{dissipation}.
}
\]

---

## 28. Explicit nonclaims

Core 3 does **not** currently claim:

1. a proved infinite-dimensional theorem that \((g,C,E,K)\) reconstructs \(\nabla\) on the full periodic NS Fréchet/Sobolev category;
2. that one mother snapshot \(E_u\) reconstructs the background connection;
3. that \(E+K\) is full rank at every spectral multiplicity;
4. that every linearized kernel is a physical gauge;
5. that higher tower levels always add new independent physics;
6. that Bianchi or Jacobi alone force uniqueness;
7. that nonzero mother or curvature is a blow-up signal;
8. that \(\ker C\) is a gauge sector;
9. that the signature image is extrinsically curved as a linear embedding;
10. that Euler--heat BCH descendants equal formation curvature;
11. that viscosity is encoded by reversible spectral geometry;
12. a boundary/manifold theorem without a typed Hodge/Stokes replacement;
13. global regularity or exclusion of finite-time singularity;
14. novelty relative to every existing Cartan, holonomy, isospectral-orbit or hydrodynamic-geometric formalism;
15. that one generic snapshot determines the full polarized mother one-form or connection;
16. that the base-window selection polynomial is universal across all spectral scales;
17. that graph connectivity alone implies \(\operatorname{Alg}(C,E)=\operatorname{End}(V)\);
18. that the finite-window presentation already defines a proved continuum inverse/projective limit;
19. that every nongeneric or sparse state reveals the same law category.

---

## 29. Open theorem programme

The next theorem-level programme is no longer vague.

It is to define and analyze, on the actual periodic function space,

\[
\boxed{
\mathcal A_{C,E}:\Omega^1(\mathfrak h_C)\to\Omega^2(\mathfrak m_C),
}
\]

with correct domains and Sobolev orders, and prove a statement of the form

\[
\boxed{
(g_\Sigma,C,E,K,\text{finite higher jets if required})
\Longrightarrow
\nabla
\quad\text{modulo the true differential-spectral stabilizer}.
}
\]

The hard pieces are:

- unbounded curl and connection domains;
- spectral multiplicities and shell degeneracy;
- Fredholm/injectivity properties of the continuum Codazzi map;
- nonlinear resolution of singular Jacobian strata;
- topology/harmonic modes;
- boundary Hodge typing;
- exact characterization of the residual stabilizer/holonomy centralizer;
- a Burnside-type criterion coupling spectral-sheet connectivity with inter-sheet channel rank;
- a generic theorem identifying the state-independent relation ideal carried by \((C,E_u)\);
- a sparse law-holography theorem for exact helical interaction categories;
- compatible restriction maps and a possible continuum projective/inverse limit of finite-window presentations;
- a rigorous syntax-versus-geometry separation theorem.

Until those programmes are completed, geometric completeness and presentation bootstrap remain precisely formulated and strongly tested **candidates**, not closed continuum theorems.
