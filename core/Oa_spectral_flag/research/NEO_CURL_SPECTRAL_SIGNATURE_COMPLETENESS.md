# NEO Curl Spectral-Flag Signature: Completeness Stress Test
## Microlocal inverse, Killing kernel, whole-state recovery, and the boundary of the whole-NS claim

**Status.** Research dossier following `research/NEO_CURL_SPECTRAL_OBSTRUCTION_SIGNATURE.md`.

**Purpose.** The preceding signature note established the shifted family
\[
\mathscr O_a(v)
=H_a[\nabla_v,H_a]-[\nabla_{H_av},H_a],
\qquad H_a=\operatorname{sgn}(C-aI),
\]
as a canonical spectral-flag signature of the divergence-free connection relative to curl.  This dossier asks a stronger question:

> Is the full operator-valued signature complete enough to coordinatize the actual homogeneous incompressible Navier--Stokes state and vector field, modulo only the natural geometric symmetries?

The answer is not yet a continuum theorem, but the experiments now support a much sharper structure than a blow-up-specific obstruction picture.

The strongest current candidate is:
\[
\boxed{
\text{full NS geometry}
=
\text{vertical curl-commuting gauge}
+
\text{horizontal spectral-flag signature}
+
\nu C^2.
}
\]
The physical state appears to select the vertical and horizontal pieces simultaneously, and the full shifted signature appears sufficient to recover that physical state modulo Euclidean/Galilean Killing symmetry.

Labels used below:

- **EXACT** -- algebraic identity in the stated finite/smooth setting;
- **AUDIT** -- numerical or symbolic stress test;
- **DEDUCTION** -- consequence of exact identities plus stated regularity assumptions;
- **CANDIDATE PRINCIPLE** -- structural interpretation not yet promoted to theorem;
- **OPEN** -- genuine remaining analytic gap.

---

## 0. Anti-overclaim protocol

The following statements are **not** asserted:

1. that the critical slice \(\mathscr O_0\) alone is a stable continuum coordinate;
2. that the self-contractions \(J_a=\frac14\mathscr O_a(u)u\) determine the Euler vector field;
3. that every curl-commuting connection component vanishes physically;
4. that finite Galerkin injectivity is automatically a continuum injectivity theorem;
5. that the existence of the signature proves regularity or rules out singularities.

The new evidence instead supports a more precise claim: the **full moving spectral flag** is microlocally complete, while lower-rank contractions and the fixed zero cut can be severely blind.

---

## 1. Whole-state coordinate experiment -- AUDIT

On periodic divergence-free Galerkin classes, the map
\[
 u\longmapsto \{\mathscr O_a(u)\}_a
\]
was sampled by random linear measurements of its full operator-valued output.

### Bandwidth \(K=1\)

There are 52 nonconstant real divergence-free degrees of freedom after removing the three Galilean constants.  A random signature sketch had
\[
\boxed{\operatorname{rank}=52/52,\qquad \kappa\approx2.75.}
\]
Inverting the sketch recovered the state coefficients with median relative error
\[
1.8\times10^{-15}.
\]
From the recovered state, the following native NS objects were reconstructed at machine precision:
\[
N(u)=P(u\times Cu),\qquad C^2u,\qquad u_t=N(u)-\nu C^2u.
\]
Typical relative errors were \(2.7\times10^{-15}\) to \(3.4\times10^{-15}\).

### Bandwidth \(K=2\)

There are 248 nonconstant real divergence-free degrees of freedom.  Using the mother map
\[
E_u=[\nabla_u,C],
\]
which is exactly tomographic in the full shifted signature, a random sketch had
\[
\boxed{\operatorname{rank}=248/248,\qquad \kappa\approx22.0.}
\]
State, Euler term, viscous term and full instantaneous NS vector field were recovered with relative errors of order \(10^{-15}\).

**Interpretation.** The signature is not merely a diagnostic of a chosen mechanism.  In the tested finite-dimensional physical realizations it functions as a coordinate chart for the state modulo Galilean translation.

---

## 2. Signature-coordinate evolution -- AUDIT

Let \(c\) denote ordinary Galerkin state coordinates and let
\[
y=Mc
\]
be a full-rank signature sketch.  The state ODE is
\[
\dot c=F_{NS}(c).
\]
On the signature image one may write the conjugated ODE
\[
\boxed{
\dot y=M F_{NS}(M^+y).
}
\]
For a \(K=1\), 52-dimensional truncation, the state ODE and signature ODE were integrated independently over one unit of physical time.  The maximum relative discrepancy was
\[
\boxed{
\|M^+y(t)-c(t)\|/\|c(t)\|
\lesssim2.4\times10^{-15}.
}
\]
The signature trajectories themselves agreed to \(1.8\times10^{-15}\), and the reconstructed vector fields to \(3.4\times10^{-15}\).  Final kinetic energies agreed to all displayed digits.

**CANDIDATE PRINCIPLE.** Once the physical signature map is proved injective with stable inverse on an infinite-dimensional class, NS should be conjugatable to a flow on the signature image.  This is a coordinate reformulation question, not a regularity estimate.

---

## 3. The curl commutant is real dynamics -- FALSIFICATION / RECLASSIFICATION

Abstractly, the full signature determines the connection only modulo the curl commutant:
\[
[D,C]=0.
\]
A tempting but false shortcut would be to assume that the commutant is dynamically zero for physical NS connections.

A helical \(K=2\) Fourier audit instead found that the curl-commuting part of the actual projected advection can be substantial:
\[
\frac{\|\nabla_u^{\parallel}\|}{\|\nabla_u\|}
\approx0.39
\]
in median random tests, and
\[
\frac{\|\nabla_u^{\parallel}u\|}{\|\nabla_u u\|}
\approx0.21
\]
in median, with maxima around \(0.31\).

Thus
\[
\boxed{
\mathscr O\neq\text{the full connection itself}.
}
\]
This is a genuine falsification of the naive strongest claim.

---

## 4. Vertical isospectral gauge -- EXACT / AUDIT

The same commutant sector has a very rigid property.  Since
\[
[\nabla_u^{\parallel},C]=0,
\]
it commutes with every spectral reader \(f(C)\).  Because projected advection is skew-adjoint on divergence-free \(L^2\),
\[
\boxed{
\langle f(C)u,\nabla_u^{\parallel}u\rangle=0
}
\]
for every suitable real spectral reader \(f\).

This was audited for
\[
1,\quad x,\quad x^2,\quad |x|,\quad e^{0.17x},
\quad \sin(0.6x)+0.13x^2,
\quad \sqrt{x^2+0.2},
\]
with residuals of order \(10^{-16}\).

For a frozen skew generator \(D^{\parallel}\) commuting with \(C\),
\[
U(t)=e^{-tD^{\parallel}}
\]
is unitary and commutes with \(C\), hence
\[
\boxed{
\langle U(t)u,f(C)U(t)u\rangle
=
\langle u,f(C)u\rangle.
}
\]
Finite-time numerical flows preserved all tested spectral quadratic functionals to \(10^{-16}\).

**Interpretation.** The curl commutant is not missing physics.  It is vertical, isospectral motion inside exact curl fibers.  The signature records horizontal spectral deformation; the vertical sector is a gauge-like phase/orientation motion invisible to the curl functional calculus.

---

## 5. Horizontal / vertical / heat anatomy -- CANDIDATE NORMAL FORM

The intrinsic NS equation is
\[
u_t+\nabla_u u+\nu C^2u=0.
\]
Write
\[
\nabla_u=\nabla_u^{\parallel}+\nabla_u^{\perp},
\qquad
[\nabla_u^{\parallel},C]=0,
\]
with \(\nabla_u^{\perp}\) the off-spectral component reconstructed from the full shifted flag.  Then
\[
\boxed{
 u_t
=-\nabla_u^{\parallel}u
-\nabla_u^{\perp}u
-\nu C^2u.
}
\]
The three terms have distinct meanings:

- \(\nabla_u^{\parallel}\): vertical unitary/ispectral gauge motion;
- \(\nabla_u^{\perp}\): horizontal spectral deformation, encoded by \(\mathscr O\);
- \(\nu C^2\): physical heat contraction.

The physical realization \(u\mapsto\nabla_u\) ties the vertical and horizontal pieces together.  In the Galerkin classes tested, the horizontal signature was sufficient to identify \(u\), after which the vertical piece is reconstructed automatically.

---

## 6. Native-face recovery from signature -- AUDIT

Starting only from signature-recovered state coordinates, a whole native NS suite was recomputed:
\[
u,\quad \omega=Cu,\quad S=\operatorname{sym}\nabla u,
\quad (\omega\cdot\nabla)u,
\quad N=P(u\times\omega),
\]
\[
p,\quad \nabla p,\quad \operatorname{Hess}p,
\quad u_t.
\]
Median relative errors were approximately
\[
2.1,\ 2.3,\ 2.3,\ 3.3,\ 3.1,\ 3.1,\ 3.1,\ 3.3,\ 3.1
\]
in units of \(10^{-15}\), with maxima below \(4.3\times10^{-15}\).  Quadratic spectral stocks were recovered even more accurately, at \(10^{-16}\) to \(10^{-15}\).

This is strong evidence that the signature does not merely encode one nonlinear balance.  It identifies the physical state from which all ordinary NEO/NS faces follow.

---

## 7. Phase adversary: the signature is not a spectral-measure disguise -- AUDIT

Two divergence-free states were constructed with the same complete signed-curl quadratic spectral measure on 18 roots, differing only by phase/spatial organization.  The spectral measures agreed to
\[
6.1\times10^{-16},
\]
and arbitrary tested quadratic spectral functionals \(\langle u,f(C)u\rangle\) agreed to \(2.8\times10^{-16}\).

Nevertheless the sampled full signatures differed by order one:
\[
\boxed{
\frac{\|\mathscr O(u_1)-\mathscr O(u_2)\|}
{\sqrt{\|\mathscr O(u_1)\|\|\mathscr O(u_2)\|}}
\approx1.44,
}
\]
and their Euler vector fields differed by
\[
\approx1.40.
\]

**Deduction.** The signature carries phase/spatial compatibility information absent from the complete quadratic curl spectral measure.  This is exactly the information needed to determine nonlinear evolution.

---

## 8. Principal symbol of the mother/signature -- EXACT

Let
\[
E_u=[\nabla_u,C].
\]
For a high-frequency divergence-free probe
\[
v(x)=b\,e^{i\xi\cdot x},
\qquad \xi\cdot b=0,
\]
freeze \(G=\nabla u(x)\), write
\[
S=\frac12(G+G^T),
\]
and use the local mother formula
\[
E_uv=-P\sum_j\nabla u_j\times\partial_jv.
\]
The principal symbol is
\[
\boxed{
\sigma_1(E_u)(x,\xi)b
=-i\frac{\xi^TS(x)\xi}{|\xi|^2}\,\xi\times b.
}
\]
Thus the leading microlocal information is the quadratic form
\[
\boxed{
q_x(n)=n^TS(x)n,
\qquad n=\xi/|\xi|.
}
\]

A 5000-sample random algebra audit gave maximum relative residual
\[
7.6\times10^{-16}.
\]

---

## 9. Six-direction local inverse for strain -- EXACT / AUDIT

A symmetric trace-free \(3\times3\) tensor has five degrees of freedom.  The six fixed directions
\[
e_1,e_2,e_3,
\frac{e_1+e_2}{\sqrt2},
\frac{e_1+e_3}{\sqrt2},
\frac{e_2+e_3}{\sqrt2}
\]
produce the measurements
\[
q_j=n_j^TSn_j.
\]
The corresponding linear map has
\[
\boxed{\operatorname{rank}=5,\qquad \kappa\approx2.56.}
\]
Random trace-free strains were reconstructed with maximum relative error
\[
1.2\times10^{-15}.
\]

Hence six directional microlocal readings of the full signature suffice to recover the entire local strain tensor.

---

## 10. Explicit state inverse from strain -- EXACT

For incompressible \(u\),
\[
S_{ij}=\frac12(\partial_i u_j+\partial_j u_i)
\]
and
\[
\partial_jS_{ij}
=\frac12\Delta u_i.
\]
Therefore
\[
\boxed{
\Delta u=2\operatorname{div}S.
}
\]
On a mean-zero torus or for sufficiently decaying whole-space fields,
\[
\boxed{
 u=2\Delta^{-1}\operatorname{div}S.
}
\]
Thus the microlocal inverse is constructive:
\[
\boxed{
\mathscr O
\to E
\to \{n^TSn\}_{n}
\to S
\to u/\mathrm{Kill}.
}
\]

On random periodic fields, exact six-direction reconstruction followed by the Poisson inverse gave median errors
\[
6.2\times10^{-16}\quad\text{for }S,
\qquad
5.2\times10^{-16}\quad\text{for }u.
\]

---

## 11. Killing kernel -- EXACT STRUCTURAL CONSEQUENCE

If the full signature vanishes, then its mother tomography vanishes:
\[
E_u=[\nabla_u,C]=0.
\]
At principal-symbol level this forces
\[
n^TSn=0
\qquad\forall n\in S^2,
\]
hence
\[
\boxed{S=0.}
\]
Therefore
\[
\operatorname{sym}\nabla u=0,
\]
the Euclidean Killing equation.

Exact polynomial rank searches through degree five found only the six standard Euclidean Killing fields:
\[
\boxed{
u(x)=Ax+b,\qquad A^T=-A.}
\]
The nullity was 3 at degree 0 and exactly 6 at every tested degree 1--5, with no hidden nonlinear polynomial kernel.

For a periodic single Fourier mode \(k\ne0\), the Killing equations have full rank; hence the only periodic kernel is the zero Fourier mode.  Therefore on the periodic mean-zero class,
\[
\boxed{
\mathscr O(u)=0\Longrightarrow u=0.
}
\]
On a periodic class without fixing the mean, the kernel is exactly the three Galilean translations.

---

## 12. Microlocal signature metric equals enstrophy mass -- EXACT / AUDIT

For unit \(n\), the principal symbol acts on the two-dimensional plane \(n^\perp\) as a rotation of size \(|n^TSn|\).  Therefore
\[
\|\sigma_1(E_u)(x,n)\|_{HS(n^\perp)}^2
=2(n^TSn)^2.
\]
Spherical averaging for trace-free symmetric \(S\) gives
\[
\left\langle (n^TSn)^2\right\rangle_{S^2}
=\frac{2}{15}|S|^2.
\]
Hence
\[
\boxed{
\left\langle
\|\sigma_1(E_u)(x,n)\|_{HS}^2
\right\rangle_{S^2}
=\frac4{15}|S(x)|^2.
}
\]
For periodic incompressible fields,
\[
\|S\|_2^2=\frac12\|\omega\|_2^2,
\]
so globally
\[
\boxed{
\int\left\langle\|\sigma_1(E_u)\|_{HS}^2\right\rangle_{S^2}
=\frac{2}{15}\|\omega\|_2^2.
}
\]

Random periodic audits produced ratios
\[
0.26653\approx4/15,
\qquad
0.13327\approx2/15.
\]

**Interpretation.** Enstrophy stock is the microlocal quadratic mass of the mother/signature principal symbol, up to a universal constant.  Earlier work showed enstrophy production is a moment of the shifted signature current; both stock and production therefore sit naturally inside the same geometry.

---

## 13. Near-Killing coercivity -- AUDIT

For near-Galilean states
\[
u=b+\varepsilon w,
\]
the signature/strain metric scaled exactly as \(\varepsilon^2\) over four decades:
\[
\varepsilon=1,10^{-1},10^{-2},10^{-3},10^{-4}.
\]
No extra flat direction appeared near the Galilean orbit.  This is consistent with Korn-type coercivity modulo Killing fields.

The continuum quantitative target suggested by the experiments is therefore not a new mysterious inequality but a signature version of Korn/elliptic observability:
\[
\boxed{
\|u-\Pi_{Kill}u\|_X
\lesssim
\|\mathscr O(u)\|_{\mathfrak O}.
}
\]
The exact choice of \(X\) and the canonical operator norm \(\mathfrak O\) remain open.

---

## 14. Actual commutator parametrix -- AUDIT

The previous inverse can be implemented without observing \(S\) directly.  Six high-frequency divergence-free plane waves are inserted into the actual mother commutator, the six scalar quadratic-form responses are extracted, and \(S\) and then \(u\) are reconstructed.

For a smooth periodic state, whole-state velocity errors were
\[
\begin{array}{c|ccccccc}
k&4&8&12&16&20&24&28\\\hline
\mathrm{err}&0.180&0.0602&0.0280&0.0160&0.0103&0.00717&0.00528.
\end{array}
\]
The practical inverse converged close to \(O(k^{-2})\).

A direct operator-symbol comparison separately showed the expected \(O(k^{-1})\) subprincipal error before the scalar polarization/reconstruction cancellation.

---

## 15. Quantitative scale-separation law -- AUDIT

For states with Fourier bandwidth
\[
K_u=1,2,3,4
\]
and probe frequencies \(k=8,12,16,20,24,28\), the reconstruction error obeyed the empirical law
\[
\boxed{
\frac{\|u_{rec}-u\|}{\|u\|}
\approx
C(u)\left(\frac{K_u}{k}\right)^2.
}
\]
For example, at \(K_u=2\) the scaled quantity
\[
\mathrm{err}\,(k/K_u)^2
\]
was
\[
0.867,\ 0.909,\ 0.923,\ 0.929,\ 0.933,\ 0.935.
\]

This is strong evidence for a quantitative microlocal parametrix governed by scale separation rather than a finite-dimensional inversion accident.

---

## 16. Localized whole-space surrogate -- AUDIT

A divergence-free localized field was generated as the curl of a Gaussian vector potential on a large periodic box.  Boundary mass was only
\[
3.3\times10^{-4}
\]
of the total field norm, providing a whole-space surrogate not restricted to a finite spectral band.

Six actual commutator probes gave velocity reconstruction errors
\[
0.129,\ 0.0810,\ 0.0546,\ 0.0390,\ 0.0292,\ 0.0226,\ 0.0180
\]
as probe frequency increased.  The product \(k^2\mathrm{err}\) approached an approximately constant value, and core-region errors matched global errors closely.

**Interpretation.** The parametrix is microlocal and not merely a low-mode torus phenomenon.

---

## 17. NS scaling covariance -- AUDIT

Under the NS scaling
\[
 u_\lambda(x)=\lambda u(\lambda x),
\]
probe frequency was scaled simultaneously by \(\lambda\).  Reconstruction errors were invariant to displayed precision for \(\lambda=1,2,3\).

For example, at one fixed scale ratio the error was
\[
0.0505483473861758
\]
for all three scalings up to roundoff in the last digit.

Thus the constructive signature inverse introduces no extraneous physical scale.  It depends on dimensionless state/probe scale separation, as a genuine NS-compatible microlocal coordinate should.

---

## 18. Self-contraction family is not complete -- STRONG FALSIFICATION

The whole-state information cannot be compressed to the diagonal hard fields
\[
J_a=\frac14\mathscr O_a(u)u.
\]
On a \(K=2\) helical truncation with 21 shifted cuts, even a state-dependent least-squares fit of the full Euler vector field \(N(u)\) from \(\{J_a\}\) had median relative residual
\[
\boxed{0.644.}
\]
The best cases remained around \(0.59\), and universal cut weights failed similarly.

Augmenting the dictionary with
\[
\mathscr O_a(u)C^m u,
\qquad 0\le m\le4,
\]
across all cuts still left residuals around \(0.58\) in state-dependent fits and about \(0.65\) for universal decoders.

**Lesson.** The operator/tensor slot is irreducible at the whole-NS level.  Collapsing \(\mathscr O\) to a finite list of self-generated contractions recreates the same reader-kernel trap that appeared throughout the historical programme.

---

## 19. Critical slice \(\mathscr O_0\) is not the stable whole-state coordinate -- AUDIT

Finite Galerkin sketches of the full operator critical slice \(\mathscr O_0(u)\) were surprisingly injective:
\[
K=1:52/52,\qquad
K=2:248/248,\qquad
K=3:684/684,
\]
with moderate sketch condition numbers.

However microlocal tests reveal that \(\mathscr O_0\) is lower order.  For a low-band state and a pure positive-helicity probe at frequency \(q\),
\[
\boxed{
\|[\nabla_u,H]v_q\|\sim q^{-1}.
}
\]
By contrast, the full mother deformation satisfies
\[
\|[\nabla_u,C]v_q\|\sim q.
\]

Thus finite-dimensional injectivity of \(\mathscr O_0\) should not be confused with uniform microlocal ellipticity.  The zero fold is a distinguished angular/critical reading, not the whole stable signature.

---

## 20. Moving cuts carry the UV principal information -- AUDIT

For the same high-frequency probe, a shifted cut placed near the probe's curl level has a response much larger than the fixed zero cut.  The ratio
\[
\frac{\max_a\|[\nabla_u,H_a]v_q\|}
{\|[\nabla_u,H_0]v_q\|}
\]
was approximately
\[
19.5,\ 36.1,\ 83.6,\ 150.9,\ 324.0
\]
for increasing probe frequencies, growing close to \(q^2\).

This confirms the essential distinction:
\[
\boxed{
\mathscr O_{whole}
=\{\mathscr O_a\}_{a\in\mathbb R},
\qquad
\mathscr O_0=\text{critical slice only}.
}
\]

---

## 21. UV polar anatomy -- EXACT IDENTITY / AUDIT

For a pure positive-helicity high-frequency input, the exact polar split
\[
E=A_0\Lambda+HL
\]
separates the zero-fold angular channel from radial/moving-cut information.

In the UV audit, the angular contribution \(\|A_0\Lambda v_q\|\) stayed nearly constant, around
\[
0.050\to0.046,
\]
while the radial term \(\|HLv_q\|\) grew approximately linearly,
\[
0.138\to0.572.
\]
The angular fraction of the full mother response fell from about
\[
0.345\to0.081,
\]
while the radial fraction rose
\[
0.943\to0.997.
\]
The identity reconstructed \(E\) to \(10^{-15}\).

**Interpretation.** In the ultraviolet, whole-state first-jet information is primarily a moving-cut/radial phenomenon.  The physical zero fold remains a lower-order angular-curvature channel that is special for critical work but not a stable complete state coordinate by itself.

---

## 22. Bandwidth conditioning -- AUDIT / CAUTION

Random whole-output CountSketches of the mother/signature coordinate map were tested at increasing periodic bandwidth with an approximately fixed measurement oversampling ratio of two:
\[
\begin{array}{c|ccc}
K&1&2&3\\\hline
\text{DOF}&52&248&684\\
\text{rank}&52&248&684\\
\kappa&7.6&11.1&22.6.
\end{array}
\]
No near-kernel appeared through 684 nonconstant degrees of freedom, although conditioning worsened with bandwidth.

A previous sparse-coordinate measurement produced fake rank loss.  Replacing sparse pixel sampling by a whole-output CountSketch restored the full rank.  This is a methodological warning: conditioning of a measurement sketch must not be confused with conditioning of the underlying signature map.

---

## 23. Methodological lessons from the completeness campaign

### 23.1 Full tensor before contraction

The signature is an operator-valued one-form.  Readers such as \(W(a)\), \(J_a\), or finitely many Krylov contractions can have large kernels.  Whole-NS completeness must be tested at the tensor level before any contraction.

### 23.2 Fixed cut versus moving flag

A fixed spectral cut, especially \(a=0\), can be physically distinguished and still be microlocally lower order.  Completeness belongs to the entire shifted flag, not automatically to one distinguished slice.

### 23.3 Type errors can masquerade as geometry

During the preceding campaign, a physical/Fourier representation error created an artificial rank-29 map with a fake 26-dimensional kernel.  Correct typing restored rank 52.  Zero-curl spectral blocks also require correct shifted-cut treatment.  Every claimed kernel must survive a representation/type audit.

### 23.4 Measurement geometry can masquerade as operator geometry

Sparse coordinate sampling produced apparent UV rank loss; whole-output random sketches restored full rank.  The signature map and the chosen observation map are different objects and must not be conflated.

### 23.5 A useful falsification should attack the class, not a reader

A vanishing \(W\), \(J\), or \(\mathscr O_0\)-derived scalar does not falsify the full signature.  Strong falsification targets include:

- a non-Killing field with full \(\mathscr O_a(u)=0\) for all cuts;
- failure of mother tomography;
- failure of the microlocal strain symbol;
- an independent physical state pair with identical full operator signature modulo allowed symmetry;
- failure of the inverse under proper continuum domain control.

---

## 24. Current strongest formulation -- CANDIDATE PRINCIPLE

The experiments support the following research statement.

\[
\boxed{
\textbf{Full Spectral-Flag Completeness Principle}
}
\]

For homogeneous incompressible three-dimensional Navier--Stokes, the full operator-valued family
\[
\mathscr O_u(a;v)
=H_a[\nabla_v,H_a]-[\nabla_{H_av},H_a]
\]
appears to be a scale-covariant, microlocally complete signature of the physical state modulo Euclidean Killing symmetry.  The signature determines the mother deformation, whose principal symbol determines the strain; incompressibility then reconstructs the velocity modulo Killing fields.  Once the physical state is recovered, all native NS faces, the vertical isospectral gauge motion, pressure/Hodge geometry, viscosity and the instantaneous NS vector field are reconstructed.

Schematic:
\[
\boxed{
\{\mathscr O_a(u)\}_a
\longrightarrow
[\nabla_u,C]
\longrightarrow
S
\longrightarrow
u/\mathrm{Kill}
\longrightarrow
F_{NS}(u).
}
\]

The full NS geometry is therefore naturally organized as
\[
\boxed{
\text{vertical curl-commuting motion}
\oplus
\text{horizontal spectral-flag deformation}
\oplus
\text{heat }C^2,
}
\]
with the physical state tying the sectors together.

---

## 25. What remains before a continuum whole-NS theorem -- OPEN

The remaining work is now sharply typed.

1. **Continuum injectivity.** Prove that full signature equality implies equality of physical states modulo the appropriate Killing/Galilean symmetry in a natural Sobolev or distributional class.
2. **Stable inverse.** Put the microlocal six-direction inverse into a pseudodifferential/elliptic framework and prove a quantitative estimate with explicit lower-order terms.
3. **Canonical signature norm.** Identify the continuum norm whose principal part is the enstrophy/Korn metric derived above and whose shifted-cut realization is representation independent.
4. **Domain and zero-mode control.** Treat \(H_a\), threshold seams, zero curl, whole-space decay and boundaries without silently importing periodic finite-spectrum simplifications.
5. **Signature-image dynamics.** Characterize the image of the physical map \(u\mapsto\mathscr O(u)\) and write the NS flow intrinsically on this image rather than merely by conjugation through an inverse map.
6. **Gauge geometry.** Formalize the vertical curl commutant as a bundle/gauge sector and determine the exact compatibility tying it to the horizontal signature for physical connections.

These are structural geometry problems.  Blow-up/regularity becomes one possible later application rather than the definition or purpose of the signature.

---

## 26. Compact research record

The decisive experimental facts of this campaign are:

- full signature sketches reconstruct 52/52 and 248/248 physical DOFs at machine precision;
- NS trajectories can be integrated in signature coordinates and agree with state coordinates to \(10^{-15}\);
- curl-commuting physical connection components are nonzero but exactly isospectral;
- identical complete quadratic curl spectra do not imply identical signature or Euler dynamics;
- the mother/signature principal symbol is exactly the quadratic strain form \(n^TSn\);
- six fixed microlocal directions reconstruct all five strain components;
- \(\Delta u=2\operatorname{div}S\) gives an explicit global inverse modulo Killing fields;
- exact polynomial and Fourier kernel searches find only Euclidean/Galilean Killing fields;
- the microlocal signature metric is \(\frac{2}{15}\) of enstrophy after spatial/spherical integration;
- actual six-probe state recovery obeys an approximately quadratic scale-separation law;
- the parametrix survives a localized whole-space surrogate and respects exact NS scaling;
- self-contraction families fail badly to reconstruct the Euler field;
- the zero cut is lower order in the UV, while moving cuts carry the principal whole-state information.

**Working conclusion.** The word *signature* should now be reserved for the full operator-valued spectral flag.  Its scalar/vector shadows are readers.  The evidence no longer supports viewing the object primarily as a blow-up obstruction; it supports treating it as a candidate coordinate geometry for the entire homogeneous incompressible Navier--Stokes system.
