# Curl Spectral-Flag Signature
## The spectral-flag differential of the NS connection relative to curl

**Purpose.** Record the structural object exposed jointly by the historical curl-polar programme, the NEO anchor compiler, and the terminal/provenance worktrees.  The central point is not regularity or blow-up.  Those are applications.  The primary claim of this note is structural: the family below is a differential signature of how the physical divergence-free connection fails to preserve the spectral flag of curl.  It simultaneously normalizes the mother deformation, the full first curl functional calculus, and the historical torsion/stress/curvature costumes.  The object should therefore be treated as part of the geometry of Navier--Stokes itself, not as another candidate positive quantity.

The proposed universal signature is the shifted curl-spectral family
\[
\boxed{
\mathscr O_a(v)
:=R_{H_a}(v)
:=H_aA^{(a)}_v-A^{(a)}_{H_av},
\qquad
H_a:=\operatorname{sgn}(C-aI),
}
\]
where on the divergence-free state space
\[
\boxed{
A^{(a)}_v:=[\nabla_v,H_a],
\qquad
\nabla_vw:=P[(v\cdot\nabla)w].
}
\]
The physical critical slice is
\[
\boxed{
\mathscr O_0=R_H,
\qquad H=\operatorname{sgn}C.
}
\]

The evidence and exact identities below show that:

1. \(\mathscr O_a\) is equivalent to the failure of the physical connection to preserve the spectral cut \(H_a\);
2. the entire family \(a\mapsto\mathscr O_a\) reconstructs the mother deformation \([\nabla,C]\) by exact spectral tomography;
3. more strongly, every first spectral deformation \([\nabla,f(C)]\) is a weighted moment of the same shifted signature, so the full first curl functional calculus contains no additional deformation species;
4. on finite spectral localizations, the kernel of the full signature is exactly the curl commutant: two metric connections have the same signature iff their difference commutes with \(C\);
5. historical objects such as hard flip, Euler torsion, Nijenhuis defect, helical stress divergence, helicity curvature and longitudinal Codazzi rate are contractions, polarizations, physical-space renderers or covariant jets of the same signature rather than new source species;
6. finite local velocity jets do not determine the global spectral signature, explaining a structural seam between the local terminal compiler and the historical global spectral programme.

This note deliberately separates exact algebra from numerical audits and from all later applications, including regularity.  A nonzero signature is ordinary NS geometry and occurs even in smooth steady/shear/Beltrami examples; singularity questions concern exceptional concentration or rate of the signature, not its mere existence.

Labels: **EXACT**, **AUDIT**, **DEDUCTION**, **PROPOSED CANONICAL SYNTAX**, **OPEN**.

---

## 0. Typing and scope

All intrinsic operator identities are stated on the divergence-free Hilbert space where
\[
P^2=P=P^*,
\qquad
C=\operatorname{curl}=C^*,
\qquad
H_a=H_a^*=H_a^{-1}
\]
on a finite spectral localization avoiding the threshold seam.  Whole-space/unbounded formulations require the usual domain and zero-frequency care.

The terminal ancient-profile programme does **not** automatically license global \(L^2\) spectral readers.  Therefore this note does not silently insert \(H_a\) into a bounded ancient limit.  The transfer of the signature through a singular microscope is an open typing problem stated explicitly below.

---

## 1. The signature is the non-parallelness of a curl spectral cut -- EXACT

For divergence-free \(v\), define
\[
A^{(a)}_v=[\nabla_v,H_a].
\]
Because \(\nabla_v^*=-\nabla_v\) and \(H_a^*=H_a\),
\[
\boxed{A^{(a)*}_v=A^{(a)}_v.}
\]
Differentiating \(H_a^2=I\) gives
\[
\boxed{H_aA^{(a)}_v+A^{(a)}_vH_a=0.}
\]
Thus \(A^{(a)}_v\) is self-adjoint and off-diagonal with respect to the cut \(H_a\).

Define
\[
\boxed{
\mathscr O_a(v):=H_aA^{(a)}_v-A^{(a)}_{H_av}.
}
\]
The two terms have different adjoint parity:
\[
(H_aA^{(a)}_v)^*=-H_aA^{(a)}_v,
\qquad
A^{(a)*}_{H_av}=A^{(a)}_{H_av}.
\]
Therefore
\[
\boxed{
\operatorname{skew}\mathscr O_a(v)=H_aA^{(a)}_v,
\qquad
\operatorname{sym}\mathscr O_a(v)=-A^{(a)}_{H_av}.
}
\]
In particular there is an exact reverse compiler
\[
\boxed{
A^{(a)}_v
=H_a\operatorname{skew}\mathscr O_a(v).
}
\]
Hence
\[
\boxed{
\mathscr O_a\equiv0
\Longleftrightarrow
A^{(a)}\equiv0
\Longleftrightarrow
\nabla H_a\equiv0.
}
\]
The signature vanishes exactly when the physical divergence-free connection preserves that spectral splitting.

---

## 2. Norm identity: the signature detects the whole cut connection -- EXACT

Let \(\{e_i\}\) be an orthonormal basis of a finite physical state space.  Since skew and symmetric Hilbert--Schmidt sectors are orthogonal,
\[
\|\mathscr O_a(e_i)\|_{HS}^2
=
\|A^{(a)}_{e_i}\|_{HS}^2
+
\|A^{(a)}_{H_ae_i}\|_{HS}^2.
\]
Because \(H_a\) is orthogonal and permutes an orthonormal basis,
\[
\boxed{
\sum_i\|\mathscr O_a(e_i)\|_{HS}^2
=2\sum_i\|[\nabla_{e_i},H_a]\|_{HS}^2.
}
\]
`audits/spectral_flag_signature.py` stress-tests this identity on random metric connections.

**DEDUCTION.** \(\mathscr O_a\) is not merely one scalar critical reader.  Its operator norm is equivalent, at finite dimension, to the complete non-parallelness of the cut.

---

## 3. Relation to the mother deformation -- EXACT

The intrinsic curl mother is
\[
\boxed{
E_v:=[\nabla_v,C].
}
\]
For the physical cut \(a=0\), its opposite-helicity part is
\[
E_v^\perp
=P_+E_vP_-+P_-E_vP_+.
\]
Differentiating \(C=H\Lambda\) gives the Sylvester relation
\[
\boxed{
\{\Lambda,A_v\}=2E_v^\perp.
}
\]
On nonzero spectrum,
\[
\boxed{
A_v=2\mathcal S_\Lambda^{-1}(E_v^\perp),
\qquad
\mathcal S_\Lambda(X)=\Lambda X+X\Lambda.
}
\]
Together with Section 1,
\[
\boxed{
E_v^\perp
\longleftrightarrow
A_v
\longleftrightarrow
\mathscr O_0(v)
}
\]
is an exact reversible chain on the localized physical block.

This is the first-order quotient that the anchor compiler's phrase **canonical parentage, not yet canonical syntax** was missing: same-helicity/radial deformation may change arbitrarily while the cross-helicity obstruction class remains fixed.

---

## 4. Shifted-cut tomography reconstructs the entire mother -- EXACT

The deeper object is not only the physical slice \(\mathscr O_0\).  Consider all thresholds
\[
H_a=\operatorname{sgn}(C-aI).
\]
On a spectral matrix element from curl root \(x\) to root \(y\),
\[
[\nabla_v,H_a]_{xy}
=
\big(\operatorname{sgn}(y-a)-\operatorname{sgn}(x-a)\big)(\nabla_v)_{xy}.
\]
The coefficient is zero unless \(a\) lies between \(x\) and \(y\), where it equals \(2\operatorname{sgn}(y-x)\).  Integrating over \(a\) therefore gives
\[
\boxed{
[\nabla_v,C]
=\frac12\int_{\mathbb R}[\nabla_v,H_a]\,da.
}
\]
Using the reverse compiler of Section 1,
\[
\boxed{
E_v
=\frac12\int_{\mathbb R}
H_a\operatorname{skew}\mathscr O_a(v)\,da.
}
\]
On a finite spectrum this is an ordinary finite sum over intervals between signed curl roots.  In continuum settings it should be interpreted with the appropriate spectral-measure/domain formulation.

**DEDUCTION.** The family
\[
\boxed{a\mapsto\mathscr O_a}
\]
is a spectral tomography of the mother deformation.  the mother-jet compiler language and the historical hinge language are two coordinate systems for the same first-order differential information.

---

## 5. The critical slice and the universal signature -- EXACT / INTERPRETATION

The physical critical norm uses
\[
\Lambda=|C|=|C-0I|,
\]
so it selects the threshold \(a=0\).  Thus
\[
\boxed{
\mathscr O_0=R_H
}
\]
is the **critical zero-fold slice** of the universal signature.

A state can be nearly invisible at \(a=0\) while being active at another shifted cut.  The audit campaign found finite Fourier states with
\[
|W(0)|\approx3.0\times10^{-4},
\qquad
\max_a|W(a)|\approx5.05\times10^{-2},
\]
a ratio about \(1.67\times10^2\).  This is numerical evidence, not a theorem, that \(\mathscr O_0\) should not be confused with the entire mother deformation.

---

## 6. Torsion and Nijenhuis are the two polarizations of one signature -- EXACT

Let
\[
B(a,b)=-\frac12(\nabla_ab+\nabla_ba),
\qquad
[a,b]=\nabla_ab-\nabla_ba.
\]
For any involutive cut \(H_a\), define the symmetric Euler torsion
\[
T_{H_a}(p,q)
=B(H_ap,H_aq)-H_aB(H_ap,q)-H_aB(p,H_aq)+B(p,q),
\]
and the Nijenhuis-type Lie defect
\[
N_{H_a}(p,q)
=[H_ap,H_aq]-H_a[H_ap,q]-H_a[p,H_aq]+[p,q].
\]
Direct expansion gives
\[
\boxed{
T_{H_a}(p,q)
=\frac12\big(\mathscr O_a(p)q+\mathscr O_a(q)p\big),
}
\]
\[
\boxed{
N_{H_a}(p,q)
=\mathscr O_a(q)p-\mathscr O_a(p)q.
}
\]
Hence
\[
\boxed{
\mathscr O_a(p)q
=T_{H_a}(p,q)-\frac12N_{H_a}(p,q).
}
\]
Torsion and Lie non-integrability are not separate source species.  They are the symmetric and antisymmetric polarizations of the same tensor.

---

## 7. Self-contraction and scalar readers lose information -- EXACT / AUDIT

Define the shifted hard field
\[
\boxed{
J_a:=\frac14T_{H_a}(u,u)
=\frac14\mathscr O_a(u)u.
}
\]
The shifted hinge work is
\[
\boxed{
W(a)
:=2\langle |C-a|u,N(u)\rangle
=4\langle |C-a|u,J_a\rangle.
}
\]
Therefore there is a strict information hierarchy
\[
\boxed{
\mathscr O_a
\longrightarrow
J_a
\longrightarrow
W(a),
}
\]
where each arrow is a contraction and may have a nontrivial kernel.

Two exact/adversarial examples are decisive.

### 7.1 Pure-helicity blindness

At a pure \(h\)-helicity state, first-order critical work vanishes,
\[
W(0)=0,
\]
while the opposite-sheet hard field \(J_0\) may be nonzero.  Its first visible critical response is the positive second-order square
\[
\boxed{
\dot W(0)=4\|\Lambda^{1/2}J_0\|_2^2
}
\]
at the pure-sheet boundary.

### 7.2 Self-contraction blindness

A Beltrami state \(Cu=\lambda u\) has
\[
u\times Cu=0,
\qquad
J_0=0,
\]
but the operator-valued one-form \(\mathscr O_0(u)\) can act nontrivially on independent divergence-free directions.  A finite Fourier audit found \(J_0=0\) exactly while \(\|\mathscr O_0(u)v\|\) was nonzero for every random probe direction tested.

**DEDUCTION.** A vanishing scalar reader or diagonal self-contraction does not imply that the signature disappeared.  It may only mean that the chosen renderer entered its kernel.  This explains why independent-direction Nijenhuis/Ricci/Codazzi geometry reappears after diagonal hard-flip descriptions become blind.

---

## 8. Historical costume collapse -- EXACT

For the physical cut \(a=0\),
\[
\boxed{
4J_{\rm flip}=\mathscr O_0(u)u.
}
\]
The same field also has the exact helical-stress form
\[
\boxed{
J_{\rm flip}
=-\sum_{h=\pm1}P_{-h}P\,\operatorname{div}(u_h\otimes u_h).
}
\]
Thus
\[
\text{Fourier hard flip}
\to
\text{Euler torsion}
\to
\text{helical stress divergence}
\to
\text{intrinsic helicity curvature}
\]
is an ontology collapse, not a sequence of new mechanisms.

The genetic cross-product language gives another exact renderer.  With \(X_vw=P(v\times w)\),
\[
\boxed{
W_\Lambda
=\langle\omega,[H,X_u]\omega\rangle,
}
\]
and the hard field can likewise be written by sheetwise commutators \([H,X_{u_h}]\omega_h\).  Actual finite-Fourier audits reproduced the stress, torsion, curvature and cross-product renderers at residuals of order \(10^{-16}\).

---

## 9. The final historical Codazzi obstruction is a covariant jet of the same signature -- EXACT

Let
\[
C_J^\sigma
:=(\partial_t+\nu\Lambda^2+\nabla_u)J_{\rm flip}
\]
on the true projected state space.  Since \(4J_{\rm flip}=\mathscr O_0(u)u\) and \(\Lambda^2\) commutes with fixed curl spectral readers, the product commutator yields
\[
\boxed{
4C_J^\sigma
=
\big([\nabla_u,\mathscr O_0(u)]-\mathscr O_0(\nabla_uu)\big)u
-2\nu\sum_j\mathscr O_0(\partial_ju)\partial_ju.
}
\]
The first term is the longitudinal covariant derivative of the signature.  The second is the genuine viscous carré-du-champ of the same signature evaluated on spatial leaves.

The Gauss--Codazzi--Ricci decomposition then resolves the first term into the symmetric Codazzi block, intrinsic pressure/Ricci curvature and lower connection-curvature couplings.  The positive Gauss square cancels from the true longitudinal curvature rate exactly; it is a frame/centripetal term rather than a new positive owner.

**DEDUCTION.** The historical endpoint did not leave the signature.  It moved from \(\mathscr O_0\) to its parabolic/covariant jet.

Actual Galerkin audits performed during the discovery campaign gave relative residuals between approximately \(5\times10^{-17}\) and \(2\times10^{-16}\) for \(\nu=0,0.03,0.2\).

---

## 10. Shifted dynamic closure -- EXACT FORM / AUDIT

The same calculation applies to every fixed threshold \(a\), because \(H_a\) and \(|C-a|\) are fixed functions of \(C\) and commute with the physical heat operator.  Thus each shifted signature has the same typed evolution architecture:
\[
\boxed{
\text{NS derivative of }\mathscr O_a(u)u
=
\text{covariant derivative of }\mathscr O_a
+
\text{viscous carré of }\mathscr O_a.
}
\]
A finite Fourier audit tested thresholds
\[
a=-2.37,-1.37,-0.37,0,0.63,1.37,2.37
\]
and viscosities \(\nu=0,0.05,0.2\), with relative residuals of order \(10^{-16}\).

**INTERPRETATION.** Threshold differentiation does not create a new source species.  The whole spectral signature remains inside one covariant/parabolic architecture.

---

## 11. Scalar hinge tomography of nonlinear spectral work -- EXACT MODULO AFFINE READERS

For a sufficiently regular scalar spectral reader \(f\), modulo its affine part,
\[
f(x)
=\frac12\int_{\mathbb R}f''(a)|x-a|\,da.
\]
The Euler nonlinearity is invisible to affine readers \(1\) and \(C\):
\[
\langle u,N\rangle=0,
\qquad
\langle Cu,N\rangle=0.
\]
Therefore
\[
\boxed{
W_f
:=2\langle f(C)u,N\rangle
=rac12\int_{\mathbb R}f''(a)W(a)\,da.
}
\]
The critical reader \(f(x)=|x|\) has distributional curvature \(f''=2\delta_0\), so it selects the physical zero-fold slice.

Finite Fourier audits reconstructed the \(f(x)=x^2\) and \(f(x)=x^3\) nonlinear works from the hinge profile with residuals below \(5\times10^{-15}\).

---

## 12. NS symmetry audit -- AUDIT / STRUCTURAL CHECK

The self-induced critical signature passed the following finite Fourier checks:

- Galilean addition by a constant velocity changed \(\mathscr O_0(u)u\) only at relative roundoff, because constant advection commutes with translation-invariant curl spectral readers;
- spatial translation produced the expected covariance at relative roundoff;
- under integer NS scaling \(u_s(x)=s u(sx)\) on a periodic replication, the \(L^2\) norm of \(\mathscr O_0(u_s)u_s\) scaled by \(s^3\), while \(W_\Lambda\) scaled by \(s^5\), as dictated by the quadratic Euler/curl orders.

These tests do not prove a continuum theorem, but they are useful falsification checks against a coordinate artifact.

---

## 13. Finite local jets do not determine the spectral signature -- EXACT CONSTRUCTION + AUDIT

This is the key seam with the terminal worktree.

For any integer \(q\ge1\), the periodic analytic vector potential
\[
\mathcal A_q(x)
=(1-\cos x_j)^q\sin x_\ell\,e_r
\]
produces the divergence-free perturbation
\[
\boxed{w_q=\operatorname{curl}\mathcal A_q.}
\]
Because
\[
(1-\cos x_j)^q\sin x_\ell
=O(|x|^{2q+1}),
\]
one has
\[
\boxed{
\partial^\alpha w_q(0)=0
\qquad
\text{for all }|\alpha|\le2q-1.
}
\]
Thus one may modify the global spectral completion of a field while preserving any prescribed finite local jet order by choosing \(q\) sufficiently large.

In the adversarial audit campaign, exact G3 contact data were held fixed while such analytic flat perturbations preserved local jets through orders
\[
1,3,5,7,9.
\]
The global critical work \(W_\Lambda\), a scalar contraction of \(\mathscr O_0\), still moved through both signs at every tested order.  For example, with the jet fixed through order seven,
\[
W_\Lambda\in[-1.17\times10^{-4},\,2.53\times10^{-4}].
\]

A separate nullspace experiment fixed all velocity derivatives at the contact through orders \(1,2,3,4,5\) and again found opposite signs of \(W_\Lambda\) among global completions.

**DEDUCTION.** Local contact variables such as
\[
b=P_{n^\perp}Sn,
\qquad
\delta=6a^2-g,
\qquad
\omega\times A\omega,
\qquad
r^2-g^3/6
\]
may classify local terminal geometry, but no fixed finite local jet tower can reconstruct the global curl-spectral signature.  This is a structural reason not to respond to terminal ambiguity by indefinitely differentiating local defects.

---

## 14. Relation to the current terminal/provenance worktrees -- DEDUCTION / TYPE WARNING

The historical programme retained the global spectral objects \(H,\Lambda\) and eventually isolated \(R_H\) and its longitudinal covariant derivative.  Its weakness was terminal extraction/compactness.

The endpoint-first programme deliberately imposes
\[
\boxed{
\text{Local compiler first; global spectral calculus only when licensed},
}
\]
because a bounded ancient singular profile need not belong to global \(L^2\) or \(\dot H^{1/2}\).  Its strength is terminal extraction and local normal-form rigidity, but this typing rule removes direct access to \(\mathscr O_0\).

The two programmes therefore meet at a precise seam:
\[
\boxed{
\begin{array}{c}
\text{history: spectral signature visible, terminal transfer unproved},\\
\text{terminal worktree: terminal object visible, spectral signature unlicensed}.
\end{array}}
\]
This is a more precise explanation of the repeated impression that each programme was “missing one thing.”

---

## 15. What the signature is not -- ANTI-OVERCLAIM

The following statements are **not** established:

1. \(\mathscr O_0\neq0\) implies singularity;
2. smooth solutions have \(\mathscr O_0=0\);
3. a bounded ancient terminal profile automatically admits \(H_a\), \(J_a\), or the global tomography integral in the required spaces;
4. the family \(\mathscr O_a\) supplies a finite coercive norm by itself;
5. the discovery resolves the Clay problem.

Generic smooth three-dimensional states have nonzero signature.  The historical singularity ledger points instead to a stronger phenomenon: a hypothetical finite singular endpoint forces an uncontrolled **rate/concentration** of the critical slice, e.g. the divergence of an energy-dual norm of the parabolic/covariant derivative of \(J_{\rm flip}\).

Thus the present discovery is an ontology/normal-form statement, not yet a regularity estimate.

---

## 16. Proposed canonical interpretation -- CANDIDATE PRINCIPLE

The repeated historical “metamorphosis” can now be separated into two phenomena.

### Genuine change of state geometry

The signature itself changes:
\[
\mathscr O_a(t_1)\ne\mathscr O_a(t_2).
\]
This is true dynamics and must be handled by the covariant/parabolic evolution law.

### Renderer change or blindness

One passes among
\[
\mathscr O_a,
\quad
A^{(a)},
\quad
E,
\quad
T_{H_a},
\quad
N_{H_a},
\quad
J_a,
\quad
W(a),
\quad
\text{stress divergence},
\quad
\text{Codazzi jets}.
\]
An individual renderer may vanish or become inconvenient while the underlying signature remains nonzero.

This motivates the formulation
\[
\boxed{
\textbf{Conservation of detectability:}
\quad
\text{exact NS representation changes can move visibility between renderers,}
\quad
\text{but they remain constrained by one curl-spectral compatibility signature.}
}
\]
This is a structural principle suggested by exact identities and audits, not a conservation law for a scalar norm.

---

## 17. The one open bridge that this note exposes -- OPEN

The immediate high-value theorem is no longer another local descendant.  It is a typed transfer problem:
\[
\boxed{
\text{Can a compactness-stable/localized renderer of the critical signature}
\quad\mathscr O_0
\quad\text{survive singular rescaling without assuming global }L^2?
}
\]
The Poisson/Sylvester formula
\[
A_v
=2\int_0^\infty e^{-s\Lambda}E_v^\perp e^{-s\Lambda}\,ds
\]
and the subordination of \(e^{-s\Lambda}\) to the heat semigroup suggest a possible bridge between the global spectral signature and parabolic local compactness, but no such transfer theorem is asserted here.

**STOP RULE.** Do not introduce another terminal defect merely because \(\mathscr O_0\) is not directly licensed on the current ancient class.  Any new renderer must either:

- reconstruct a nontrivial piece of \(\mathscr O_0\) under the extraction topology;
- prove that the relevant critical signature action vanishes in the limit;
- or provide a genuine counterexample showing that the signature thesis is incomplete.

Otherwise it risks recreating the historical metamorphosis loop in local coordinates.

---

## 18. Audit ledger

The discovery campaign preceding this note established the following finite-dimensional / finite-Fourier checks.

| Audit | Result |
|---|---:|
| Actual Fourier \(R_H=T_H-\frac12N_H\) | residual \(\sim10^{-16}\) |
| Actual Fourier \(R_H(u)u=4J_{\rm flip}\) | residual \(\sim10^{-16}\) |
| \(W_\Lambda=\langle\Lambda u,R_H(u)u\rangle\) | residual \(\sim10^{-16}\) |
| helical-stress divergence renderer | residual \(\sim10^{-16}\) |
| cross-product commutator renderer | residual \(\sim10^{-16}\) |
| connection norm identity | residual \(<2.3\times10^{-16}\) |
| reverse compiler \(\mathscr O\to A\to E^\perp\) | residual \(\lesssim10^{-14}\) |
| shifted tomography \(\{\mathscr O_a\}\to E\), finite matrix | residual \(<2.5\times10^{-16}\) |
| shifted tomography, actual Fourier | residual \(<2.9\times10^{-16}\) |
| historical final source = covariant \(\mathscr O_0\) jet + carré | residual \(\lesssim2\times10^{-16}\) |
| shifted dynamic closure across seven cuts / three viscosities | residual \(\lesssim2\times10^{-16}\) |
| pure-helicity first-reader blindness | \(W(0)=0\), \(J_0\ne0\) generically |
| Beltrami self-contraction blindness | \(J_0=0\), operator \(\mathscr O_0(u)\ne0\) on probes |
| fixed G3 / fixed local jets | opposite signs of global \(W_\Lambda\) survive |
| universal \(f(C)\) reader reconstruction | residual \(\lesssim10^{-15}\) |
| commutant-kernel rank tests | nullities \(0,2,4,7\) exactly as predicted |
| layer-cake crossing metric | residual \(\lesssim7\times10^{-16}\) |
| spectral-flag tomography through commutator order 4 | residual \(\lesssim1.2\times10^{-15}\) |
| vortex-stretching tomography from shifted cuts | residual \(\sim10^{-15}\) |
| corrected periodic state-signature rank, \(|k_i|\le1\) | rank \(52\), nullity \(3\) Galilean directions |

`audits/spectral_flag_signature.py` records the algebraically portable core of these checks.  The larger pseudo-spectral experiments were discovery audits and should be promoted into separate reproducible files if this programme becomes canonical.

---

## 19. Compact statement

The current structural candidate is
\[
\boxed{
\mathscr O_a(v)
=H_a[\nabla_v,H_a]-[\nabla_{H_av},H_a].
}
\]
Its key exact properties are
\[
\boxed{
\mathscr O_a=0
\iff
\nabla H_a=0,
}
\]
\[
\boxed{
[\nabla_v,C]
=\frac12\int H_a\operatorname{skew}\mathscr O_a(v)\,da,
}
\]
\[
\boxed{
\mathscr O_a(p)q
=T_{H_a}(p,q)-\frac12N_{H_a}(p,q),
}
\]
\[
\boxed{
4J_a=\mathscr O_a(u)u,
\qquad
W(a)=4\langle|C-a|u,J_a\rangle.
}
\]
At the physical fold \(a=0\), the historical final Codazzi/heat-rate obstruction is a covariant/parabolic jet of this same object.

**Working interpretation.** the mother deformation and history's succession of torsion/stress/curvature/Codazzi costumes are not separate ontologies.  They are different resolutions and derivative levels of one curl spectral-compatibility signature.  Regularity is one later application; the more basic problem is to understand this quotient geometry and the dynamics it induces on spectral flags.

---

## 20. Structural reclassification: the signature belongs to the NS state-space geometry -- EXACT INTERPRETATION

The connection
\[
\nabla_vw=P[(v\cdot\nabla)w]
\]
and every fixed spectral cut
\[
H_a=\operatorname{sgn}(C-aI)
\]
are defined before a particular NS trajectory is chosen.  Consequently
\[
\boxed{
(v,w)\longmapsto \mathscr O_a(v)w
}
\]
is an operator-valued tensor of the divergence-free state-space geometry.  A solution \(u(t)\) does not create this tensor.  It samples it through evaluations such as
\[
\mathscr O_a(u)u,
\qquad
\mathscr O_a(\partial_j u)\partial_j u,
\qquad
\mathscr O_a(u)N(u).
\]
This distinction is essential.  The self-induced source may vanish while the latent tensor is nonzero.  Therefore
\[
\boxed{
\mathscr O\neq\text{Euler forcing},
\qquad
\mathscr O\neq\text{blow-up quantity}.
}
\]
It is the spectral-compatibility tensor from which those trajectory-dependent readings are obtained.

The natural hierarchy is
\[
\boxed{
\text{state-space tensor }\mathscr O_a
\longrightarrow
J_a=\frac14\mathscr O_a(u)u
\longrightarrow
W(a)=4\langle |C-a|u,J_a\rangle.
}
\]
Each contraction may have a large kernel.  One must not infer disappearance of the tensor from disappearance of a lower-rank reader.

---

## 21. Universal spectral-reader reconstruction -- EXACT ON FINITE SPECTRAL LOCALIZATIONS

The shifted tomography formula is not special to the anchor reader \(f(x)=x\).  Let \(f\) be differentiable on an interval containing the finite spectrum under consideration.  For scalar spectral values \(x,y\),
\[
f(y)-f(x)
=\frac12\int_{\mathbb R}f'(a)
\big(\operatorname{sgn}(y-a)-\operatorname{sgn}(x-a)\big)\,da,
\]
where the integrand vanishes outside the interval between \(x\) and \(y\).  Therefore
\[
\boxed{
[\nabla_v,f(C)]
=\frac12\int_{\mathbb R}f'(a)[\nabla_v,H_a]\,da.
}
\]
Using the reverse compiler
\[
[\nabla_v,H_a]
=H_a\operatorname{skew}\mathscr O_a(v),
\]
one obtains
\[
\boxed{
[\nabla_v,f(C)]
=\frac12\int_{\mathbb R}f'(a)
H_a\operatorname{skew}\mathscr O_a(v)\,da.
}
\]

Thus the full first curl-spectral wardrobe is a family of moments of one shifted spectral-flag signature.  In particular:
\[
f(x)=x
\quad\Rightarrow\quad
[\nabla_v,C],
\]
\[
f(x)=|x|
\quad\Rightarrow\quad
[\nabla_v,\Lambda],
\]
The discontinuous reader \(f(x)=\operatorname{sgn}x\) is recovered in the spectral-gap/distributional limit, yielding \([\nabla_v,H]\).  These are not distinct deformation species.

**AUDIT.** Random finite spectral geometries were tested with polynomial, exponential, trigonometric and smooth-hinge readers.  The portable audit stayed below \(10^{-15}\).  The same reconstruction was checked on actual Fourier/Galerkin NS operators with residuals of order \(10^{-15}\).

**INTERPRETATION.** divided-difference calculus and history's shifted-hinge geometry are two bases for the same differential information.  The scalar identity above is the layer-cake representation of the divided difference.

---

## 22. The exact quotient: the full signature is the connection modulo the curl commutant -- EXACT IN FINITE SPECTRAL GEOMETRY

Let \(\nabla^{(1)}\) and \(\nabla^{(2)}\) be two metric connection one-forms on a finite spectral localization, and write
\[
K_v:=\nabla^{(1)}_v-\nabla^{(2)}_v.
\]
Because the signature reconstructs \([\nabla_v,H_a]\) pointwise in \(a\), and the shifted cuts reconstruct \([\nabla_v,C]\),
\[
\boxed{
\mathscr O_a^{(1)}(v)=\mathscr O_a^{(2)}(v)
\ \forall(a,v)
\iff
[K_v,C]=0
\ \forall v.
}
\]
Equivalently, in each input slot the full signature is the metric connection modulo the skew commutant of curl:
\[
\boxed{
\{\mathscr O_a\}_{a\in\mathbb R}
\cong
\frac{\text{metric connection one-forms}}
{\text{curl-commuting one-forms}}.
}
\]
This is the precise quotient interpretation that the historical metamorphosis suggested.  A deformation may change its coordinate representation, but motion entirely inside exact curl eigenspaces lies in the quotient kernel because every curl spectral reader is blind to it.

**AUDIT.** For spectra with different degeneracies, the measured nullity of the signature map agreed exactly with the dimension of the skew commutant of \(C\):
\[
0,\quad2,\quad4,\quad7
\]
in four adversarial test spectra.  Adding an arbitrary commuting block left both the signature and \([D,C]\) unchanged to machine zero; adding an off-spectral block changed both immediately.

---

## 23. A natural layer-cake metric on spectral crossing -- EXACT IN FINITE SPECTRAL GEOMETRY

On spectral matrix elements \(x\to y\),
\[
[D,H_a]_{xy}
=\big(\operatorname{sgn}(y-a)-\operatorname{sgn}(x-a)\big)D_{xy}.
\]
Squaring and integrating over the cut location yields
\[
\boxed{
\int_{\mathbb R}\|[D,H_a]\|_{HS}^2\,da
=4\sum_{x,y}|x-y|\,|D_{xy}|^2.
}
\]
For the full operator-valued one-form, let \(\{e_i\}\) be an orthonormal basis of the input slot.  The adjoint-parity split gives the traced identity
\[
\boxed{
\sum_i\|\mathscr O_a(e_i)\|_{HS}^2
=2\sum_i\|[\nabla_{e_i},H_a]\|_{HS}^2.
}
\]
This factor \(2\) is a **one-form Hilbert--Schmidt identity after summing the input slot**; it must not be asserted pointwise for a single \(v\).  Consequently,
\[
\boxed{
\int_{\mathbb R}\sum_i\|\mathscr O_a(e_i)\|_{HS}^2\,da
=8\sum_i\sum_{x,y}|x-y|\,|(\nabla_{e_i})_{xy}|^2.
}
\]
Thus the signature carries a canonical crossing metric: a matrix element is weighted by the spectral distance through which it moves.  This is not a new NS energy.  It is the intrinsic quadratic metric of the quotient geometry.

**AUDIT.** The layer-cake metric identity was checked on random finite spectra with relative residual at machine precision; separate degenerate-spectrum tests audited the commutant kernel.

---

## 24. All-order spectral-flag tomography -- EXACT FORMAL / FINITE SPECTRAL

The layer-cake representation is linear before any commutator is taken.  Hence for fixed operators \(D_1,\ldots,D_n\),
\[
\boxed{
\operatorname{ad}_{D_1}\cdots\operatorname{ad}_{D_n} f(C)
=\frac12\int_{\mathbb R}f'(a)
\operatorname{ad}_{D_1}\cdots\operatorname{ad}_{D_n}H_a\,da.
}
\]
This does **not** say that the first tensor \(\mathscr O_a\) alone numerically determines every higher covariant jet without the higher connection data.  It says something cleaner: every higher spectral jet is still tomography of the **same spectral flag**.  Higher order increases jet order and slot arity, not spectral species.

**AUDIT.** Orders \(1,2,3,4\) were tested for exponential, trigonometric/polynomial and smooth-absolute-value readers.  Worst residual across the campaign was \(1.2\times10^{-15}\).

This supplies a direct bridge between the shifted-signature language and the the order-two/higher divided-difference normalizer.

---

## 25. Local stretching is a moment of the same signature -- EXACT / FOURIER AUDIT

The mother self-contraction is
\[
E_u u=[\nabla_u,C]u=P[(\omega\cdot\nabla)u].
\]
Tomography gives
\[
\boxed{
E_u u
=\frac12\int_{\mathbb R}[\nabla_u,H_a]u\,da
=\frac12\int_{\mathbb R}H_a\operatorname{skew}\mathscr O_a(u)u\,da.
}
\]
Thus the apparently local vortex-stretching field and the global shifted-helicity geometry are two resolutions of one mother/signature.

Pairing with \(\omega=Cu\) shows that enstrophy production is likewise a moment of the signature.  Actual Fourier audits gave residual \(\sim7\times10^{-16}\) for the mother tomography and \(\sim10^{-15}\) for its identification with projected vortex stretching.

**INTERPRETATION.** There is no ontological wall between “local vortex stretching” and “global helicity curvature.”  The former is a moment of the spectral-flag differential that the latter resolves by cuts.

---

## 26. Spectral work laws are moments of one shifted current -- EXACT MODULO AFFINE READERS

Let
\[
W(a):=2\langle |C-a|u,N(u)\rangle.
\]
For a scalar reader \(f\) whose second derivative is represented by a finite measure on the relevant spectral interval, the hinge representation modulo an affine function is
\[
f(x)=\alpha+\beta x+\frac12\int f''(a)|x-a|\,da.
\]
Energy and helicity annihilate the affine part under Euler evolution.  Therefore
\[
\boxed{
2\langle f(C)u,N(u)\rangle
=\frac12\int f''(a)W(a)\,da.
}
\]
Important cases are
\[
f(x)=x^2
\quad\Rightarrow\quad
\boxed{2\langle C^2u,N\rangle=\int W(a)\,da,}
\]
while
\[
f(x)=|x|
\quad\Rightarrow\quad
\boxed{2\langle\Lambda u,N\rangle=W(0).}
\]
Thus helicity, enstrophy and critical production are not separate nonlinear mechanisms; they are different moments or evaluations of one shifted work profile induced by the signature.

**AUDIT.** Random finite spectral tests gave median residual \(2\times10^{-16}\).  Actual Fourier tests reconstructed enstrophy production from \(\int W(a)da\) to approximately \(10^{-14}\) or better.

---

## 27. The signature is latent geometry, not self-induced forcing -- AUDIT / ANTI-CONFLATION

A flow may sit in a kernel of its own self-contraction while the operator-valued signature remains nonzero.  A Fourier atlas gave the following qualitative pattern:

| flow class | self Euler forcing | \(J_0,W(0)\) | operator signature on independent probes |
|---|---:|---:|---:|
| constant | zero | zero | zero |
| shear | zero | zero | nonzero |
| 2D steady Taylor--Green | zero | zero | nonzero |
| ABC Beltrami | zero | zero | nonzero |
| generic mixed 3D | nonzero | typically nonzero | nonzero |

For the ABC Beltrami audit, \(Cu=u\) held to \(10^{-15}\), hence the diagonal hard field was machine-zero, while the median independent-probe norm of \(\mathscr O_0(u)\) was about \(6.7\times10^{-2}\).

**DEDUCTION.** The tensor exists independently of whether the current state activates it diagonally.  This is why the self-torsion reader can disappear while Nijenhuis/Ricci/Codazzi faces remain available on independent directions.

---

## 28. Principal-symbol zero geometry: infinitesimal Killing motion -- AUDIT / STRUCTURAL INTERPRETATION

For a trace-free local velocity gradient \(G\), the intrinsic mother/signature principal symbol separates the eight-dimensional gradient space into
\[
8=5_{\rm strain}+3_{\rm rotation}.
\]
A direct symbol-rank audit gave
\[
\boxed{\operatorname{rank}=5,\qquad\operatorname{nullity}=3,}
\]
with the three null directions exactly the skew gradients generating rigid Euclidean rotations.  Every symmetric trace-free strain direction was visible at order one.

This suggests the local geometric statement:
\[
\boxed{
\text{signature-principal-symbol zero}
\Longleftrightarrow
\text{infinitesimal Killing motion of curl geometry}.
}
\]
On a periodic class, nonconstant rigid rotations are excluded by the global geometry, leaving Galilean translations as the obvious global symmetry kernel.

---

## 29. State-coordinate evidence modulo Galilean symmetry -- AUDIT, NOT A CONTINUUM THEOREM

After correcting the Fourier/physical typing and the zero-curl block, a periodic Galerkin audit at bandwidth \(|k_i|\le1\) used 55 real divergence-free velocity directions: 52 nonconstant directions plus three constants.  The correctly typed full shifted-signature measurement map had
\[
\boxed{
\operatorname{rank}=52,
\qquad
\operatorname{nullity}=3.
}
\]
The three numerical null vectors were exactly the Galilean constants to machine precision, and the next nonzero singular value remained separated from zero by an order-one gap.

This is evidence for, but not proof of, the stronger possibility
\[
\boxed{
 u\pmod{\text{Galilean translations}}
\longmapsto
\{\mathscr O_a(u)\}_{a\in\mathbb R}
}
\]
being a faithful coordinate map on suitable periodic classes.

No continuum injectivity theorem is asserted here.  In particular, domain, zero mode, boundaries and noncompact geometry must be treated explicitly before such a statement can be promoted.

---

## 30. Dynamic closure reinforces the fixed-signature interpretation -- EXACT FORM / AUDIT

For
\[
J_a(u)=\frac14T_{H_a}(u,u)=\frac14\mathscr O_a(u)u,
\]
the true NS evolution has the heat-covariant form
\[
\boxed{
(\partial_t+\nu C^2)J_a(u)
=\frac12T_{H_a}(u,N(u))
-2\nu\sum_jJ_a(\partial_j u).
}
\]
The Euler contribution feeds the same bilinear signature with the new leaf \(N(u)\); viscosity contributes the carré of the same signature on spatial derivative leaves.  No new operator/source species is created by moving in physical time.

**AUDIT.** Seven shifted cuts and viscosities \(\nu=0,0.03,0.2\) were tested on actual Fourier/Galerkin NS.  Euler residual was machine-zero and viscous residuals were approximately \(10^{-15}\) to \(10^{-14}\).

This should be read together with Section 24: physical time raises state/derivative complexity while the spectral flag remains the same organizing object.

---

## 31. Methodological lessons from the signature campaign -- RESEARCH DISCIPLINE

### 31.1 A renderer kernel is not disappearance of the signature

The exact hierarchy
\[
\mathscr O_a\to J_a\to W(a)
\]
contains nontrivial kernels at each contraction.  Pure-helicity and Beltrami examples demonstrate both levels of blindness.  Therefore a vanishing scalar or self-contraction must never be promoted to an ontology statement without testing the operator-valued tensor.

### 31.2 Check representation types before interpreting a numerical kernel

One exploratory rank test appeared to produce a 26-dimensional physical kernel.  The apparent geometry was false.  The advecting field had already been transformed to physical space and was accidentally inverse-transformed a second time before entering \(D_u\).  After the Fourier/physical type error was corrected, the rank returned from \(29\) to \(52\), leaving only the three Galilean directions.

**Lesson:**
\[
\boxed{
\text{type error can masquerade as new NS geometry.}
}
\]
Every rank/nullity claim must therefore be audited with explicit representation types at each operator boundary.

### 31.3 The zero-curl block is part of the shifted spectral flag

For \(a\ne0\), the zero eigenvalue of \(C\) belongs to one side of the cut according to
\[
\operatorname{sgn}(0-a)=\operatorname{sgn}(-a).
\]
Dropping the zero block from \(H_a\) by habit breaks shifted tomography.  The zero mode is Galilean for the physical state, but it is not algebraically absent from the shifted functional calculus.

**Lesson:** zero-frequency quotienting and shifted spectral calculus are different operations and must not be conflated.

### 31.4 Do not compress the tensor too early

Repeatedly measuring only \(W(a)\), or only \(J_a\), reproduces the old history trap because contractions manufacture large artificial kernels.  The canonical object is the operator-valued one-form \(\mathscr O_a(v)\).  Compression is legitimate only after the information loss has been typed explicitly.

### 31.5 Falsification must target the quotient, not one costume

A valid counterexample to the signature thesis must break one of the invariant statements -- tomography, reverse recovery, quotient kernel, or dynamic closure -- rather than merely find a state on which one contraction vanishes.  Otherwise it only finds a kernel of a reader.


### 31.6 Keep the one-form input slot visible in norm identities

The identity
\[
\sum_i\|\mathscr O_a(e_i)\|_{HS}^2
=2\sum_i\|[\nabla_{e_i},H_a]\|_{HS}^2
\]
is traced over an orthonormal basis of advecting directions.  The corresponding factor \(2\) is not generally true for a single fixed input \(v\).  Forgetting the input slot would silently turn a tensor identity into a false pointwise norm law.

**Lesson:** operator Hilbert--Schmidt type and one-form Hilbert--Schmidt type must be kept distinct throughout the signature calculus.

---

## 32. Revised compact interpretation

The strongest currently justified structural statement is:
\[
\boxed{
\mathscr O_a(v)
=H_a[\nabla_v,H_a]-[\nabla_{H_av},H_a]
}
\]
is the **curl spectral-flag differential signature of the physical divergence-free connection**.

On finite spectral localizations it has four canonical properties:
\[
\boxed{
\mathscr O_a\longleftrightarrow[\nabla,H_a],
}
\]
\[
\boxed{
\{\mathscr O_a\}_a\longleftrightarrow[\nabla,C],
}
\]
\[
\boxed{
[\nabla,f(C)]
=\frac12\int f'(a)H_a\operatorname{skew}\mathscr O_a\,da,
}
\]
\[
\boxed{
\ker\{\mathscr O_a\}_a
=\operatorname{Comm}(C).
}
\]
Hence the mother deformation, the deformation of every curl spectral reader, the shifted hinge family, vortex stretching, helicity torsion, stress divergence and helicity curvature are not independent species.  They are coordinates, contractions, moments or jets of one spectral-compatibility geometry.

Regularity is only one possible application.  The more basic open programme is to determine whether Navier--Stokes admits a useful autonomous formulation on this quotient geometry, and whether the state can be reconstructed from the signature modulo its genuine symmetries in the continuum settings of interest.
