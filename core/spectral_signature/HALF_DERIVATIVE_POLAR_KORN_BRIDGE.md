# From the Missing Half Derivative to the Polar--Korn Target

## Status

This note records a Theory-2 reconstruction of the late regularity frontier.  It is intentionally split into **EXACT**, **CERTIFIED**, **AUDIT**, and **OPEN** statements.

It does **not** claim a proof of global Navier--Stokes regularity.  Its purpose is narrower and more useful: identify which pieces of the old endpoint obstruction have now been closed, explain why the subsequent Codazzi/time-packing detour did not close the theorem, and state the remaining key in the smallest form exposed by the complete spectral signature.

The central lesson is:

\[
\boxed{
\text{the missing half derivative is geometric, A+B closes the static reciprocal seam,}
}
\]
\[
\boxed{
\text{and the final unresolved step is not another Codazzi norm but a hypocoercive Polar--Korn coupling.}
}
\]

---

## 1. The old forced-source barrier really misses one half heat derivative -- EXACT

On one hard same-helicity edge let
\[
p+m=q,
\qquad
P=|p|,
\quad M=|m|,
\quad Q=|q|,
\]
and let
\[
\kappa_e=P^2+M^2.
\]
For parent helicity \(h\in\{\pm1\}\) and opposite child helicity \(-h\), the signed curl roots are
\[
x=hP,
\qquad
y=hM,
\qquad z=-hQ.
\]
The shifted involution selector for the hard flip is
\[
\chi_a(e)
=\frac14\bigl(1-H_a(z)H_a(x)\bigr)
        \bigl(1-H_a(z)H_a(y)\bigr).
\]
It is the indicator of one interval.  For \(h=+1\),
\[
\chi_a(e)=1
\quad\Longleftrightarrow\quad
-Q<a<\min(P,M),
\]
and the \(h=-1\) interval is its reflection.  Therefore
\[
\boxed{
\int_{\mathbb R}\chi_a(e)\,da
=d_e:=Q+\min(P,M).
}
\]
Triangle closure implies
\[
\boxed{
\frac1{\sqrt2}\sqrt{\kappa_e}
\le d_e
\le \frac3{\sqrt2}\sqrt{\kappa_e}.
}
\]
Hence, for any pre-contraction hard-edge forcing amplitudes \(g_e\),
\[
\boxed{
\frac1{\sqrt2}G_{-1/2}
\le
\int_{\mathbb R}G_{-1}^{\rm flag}(a)\,da
\le
\frac3{\sqrt2}G_{-1/2},
}
\]
where
\[
G_{-1}^{\rm flag}(a)
=\sum_e\chi_a(e)\kappa_e^{-1}|g_e|^2,
\qquad
G_{-1/2}=\sum_e\kappa_e^{-1/2}|g_e|^2.
\]
Thus one integration dimension of the complete moving spectral flag supplies exactly the half heat derivative that the abstract heat-fiber estimate of `BSVO_FULL_STATE_FRONTIER.md` Section 20.29 cannot supply.

This is a geometric coarea fact before contraction.  It does not by itself prove that \(G_{-1/2}\) has finite spacetime action.

---

## 2. Where the half derivative lives -- EXACT / INTERPRETATION

The support length splits as
\[
\boxed{
d_e=Q+\min(P,M).
}
\]
The \(Q\) piece is the child-side sweep through the zero fold.  The \(\min(P,M)\) piece is the parent-side sweep across shifted cuts.

For deep high--high \(\to\) low interactions,
\[
P\sim M\sim K\gg Q,
\]
so
\[
\frac{Q}{\sqrt\kappa}\to0,
\qquad
\frac{\min(P,M)}{\sqrt\kappa}\to\frac1{\sqrt2}.
\]
Therefore the part invisible to a child-only reader is not absent: it sits on the parent side of the complete shifted flag.

For an ordinary operator \(T\) written in the curl spectral basis,
\[
[T,H_a]_{xy}=(H_a(y)-H_a(x))T_{xy},
\]
so layer-cake integration gives
\[
\boxed{
\frac14\int_{\mathbb R}\|[T,H_a]\|_{\rm edge}^2\,da
=\sum_{x,y}|x-y|\,|T_{xy}|^2
=\bigl\||\operatorname{ad}_C|^{1/2}T\bigr\|_{\rm edge}^2.
}
\]
The missing half derivative is therefore the square root of the curl-commutator Laplacian on operator space.  This is the Theory-2 interpretation of the old heat-fiber gap.

---

## 3. Lemma A: reciprocal leakage has a sharp uniform lower bound -- CERTIFIED THEOREM

Consider a nondegenerate reciprocal-\(\beta\), orthogonal-plane quartet.  Let \((p,m)\) be the canonical same-helicity orbit, \((p',m')\) the mixed-helicity orbit, and \(Q=|q|\) the common child radius.  Define the two companion partition ratios
\[
A=\frac{G_{pp'}G_{mm'}}{G_{pm}G_{p'm'}},
\qquad
B=\frac{G_{pm'}G_{mp'}}{G_{pm}G_{p'm'}},
\]
so that
\[
\chi_{\rm geom}^2=\max(A,B).
\]
Let
\[
R=|p-m|=|p'-m'|.
\]
After normalizing \(Q=1\), using the reciprocal variables
\[
S=P+M>1,
\qquad
d=P-M\in(0,1),
\qquad
T^2=S^2+d^2-S^{-2},
\]
the exact geometric coefficients reduce the target to the quadratic inequality
\[
\boxed{
A^2+B^2\ge\frac3{32}R^2.
}
\]
For the canonical unordered labeling \(P\ge M\), orthogonality of the two triad planes gives
\[
|p-p'|\le\frac R{\sqrt2}.
\]
Therefore
\[
\boxed{
\frac{Q\,\chi_{\rm geom}^2}{|p-p'|}
\ge\frac{\sqrt6}{8}.
}
\]
The constant is sharp in the compactified deep-fiber / near-Beltrami limit.

`audits/reciprocal_lemma_a_certificate.py` verifies the reduction with exact SymPy arithmetic and proves the remaining bivariate polynomial positivity by two exact rational Bernstein certificates.  No floating-point optimization enters the certificate.

---

## 4. Lemma B: reciprocal incidence is finite-to-one -- EXACT SYMBOLIC THEOREM

Fix one nonzero off-diagonal companion role \((p,p')\).  Put
\[
a=|p|,
\qquad b=|p'|,
\qquad c=p\cdot p',
\qquad S=P+M,
\qquad w=Q^2.
\]
Reciprocality and equal heat give one polynomial \(F(S,w)=0\); orthogonality of the two original triad planes gives another polynomial \(G(S,w)=0\).  Exact elimination yields
\[
\boxed{
\operatorname{Res}_w(F,G)
=4S^6L(S)H(S),
}
\]
with
\[
L(S)=S^2-2aS+2a^2-2b^2
\]
and
\[
\boxed{
H(S)=D(S-a)^2-E^2,
}
\]
where
\[
D=(a+b)^2-4c,
\qquad
E=b(a+b)-2c.
\]
The \(L\)-branch is nonphysical: it forces either \(Q=0\) or \(P'+M'=0\).  On the nondegenerate off-diagonal physical branch \(D>0\), and \(S=a+M>a\), hence exactly one radial root survives:
\[
\boxed{
M=\frac{|E|}{\sqrt D}.
}
\]
The child radius is then unique.  The remaining equations
\[
q\cdot p=\frac{Q^2+a^2-M^2}{2},
\qquad
q\cdot p'=\frac{Q^2+b^2-M'^2}{2},
\qquad
|q|^2=Q^2
\]
intersect one line with one sphere, so there are at most two mirror children.

Thus
\[
\boxed{
\#\{\text{nondegenerate reciprocal preimages of one canonical companion role}\}\le2.
}
\]
The angular reconstruction Jacobian is
\[
\boxed{
|\det D\Phi(q)|=2|q\cdot(p\times p')|.
}
\]
Under reciprocal plane orthogonality,
\[
\boxed{
|q\cdot(p\times p')|
=\frac{|q\times p|\,|q\times p'|}{Q},
}
\]
so the only angular Jacobian degeneracies are the collinear source-null faces already present in the original source coefficients.

`audits/reciprocal_lemma_b_certificate.py` checks the resultant factorization, the nonphysical branch, the unique physical radial root, and the Jacobian identities exactly.

---

## 5. What A+B close, and what they do not -- EXACT INTERPRETATION

Lemma A supplies the local reciprocal conductance.  Lemma B prevents the same companion edge from being charged with unbounded reciprocal multiplicity.  Together with the exact diamond coarea
\[
 d\Xi=\frac{dp\,dp'\,d\mathcal H^2(y)}{16|p-p'|},
\]
A+B leave exactly the endpoint child weight
\[
\boxed{Q^{-1}}.
\]
Reflection alignment is separately controlled by the radial mismatch gate
\[
G_{\rm flip}\le\frac{|P-M|}{\sqrt2}
\]
and the kinetic-owned radial variance.

Therefore the old static reciprocal-incidence seam is closed at the aligned level.  This does **not** imply that the longitudinal Codazzi rate has a finite \(L_t^2H_x^{-1}\) budget.  Treating that rate as an independent norm led to the later time-packing detour and to a temporal-integrability mismatch.

The important correction is conceptual: after A+B, the next question should not be "which new Codazzi budget exists?" but "what is the kernel and coercive complement of the complete parabolic compatibility operator?"

---

## 6. Equal-heat diamonds expose the fifth collision invariant -- EXACT INCLUSION / FINITE-LATTICE AUDIT

For one modal logarithmic nonlinear rate
\[
\eta_k=\frac{N_k}{a_k}
\]
on active coefficients, the equal-heat diamond second difference is
\[
\delta_\Diamond\eta
=\eta_p+\eta_m-\eta_{p'}-\eta_{m'}
\]
whenever
\[
p+m=p'+m',
\qquad
|p|^2+|m|^2=|p'|^2+|m'|^2.
\]
Every function
\[
\boxed{
\eta_k=\alpha+\beta\cdot k+\gamma|k|^2
}
\]
lies in this kernel.  Thus the equal-heat collision invariants are at least
\[
\boxed{
1,\ k_x,\ k_y,\ k_z,\ |k|^2.
}
\]
The first four are amplitude/translation directions.  The fifth is exactly the heat coordinate.

`audits/equal_heat_collision_gap.py` builds the complete equal-heat diamond relation matrix on the lattice boxes \(|k_i|\le K\), quotients by pair-group redundancy, and finds
\[
\dim\ker D_K=5
\]
for \(K=1,2,3\), with no additional soft mode in these tests.  The first positive eigenvalues in the audit are approximately
\[
1.9572,\quad5.9228,\quad14.1859.
\]
This is an **AUDIT**, not a continuum spectral-gap theorem.  Its significance is negative as well as positive: the endpoint logarithm is not reproduced by a growing finite-box equal-heat soft mode in these tests.

---

## 7. The fifth invariant identifies the missing normal direction -- EXACT

The physical modal logarithmic rate is
\[
\boxed{
r_k=\frac{\dot a_k}{a_k}=\eta_k-\nu|k|^2.
}
\]
For arbitrary same-output pairs define the parabolic diamond defect
\[
\boxed{
\Delta_\Diamond^\nu\eta
:=
\eta_p+\eta_m-\eta_{p'}-\eta_{m'}
-\nu\bigl(\kappa-\kappa'\bigr),
}
\]
where
\[
\kappa=|p|^2+|m|^2,
\qquad
\kappa'=|p'|^2+|m'|^2.
\]
Then identically
\[
\boxed{
\Delta_\Diamond^\nu\eta
=r_p+r_m-r_{p'}-r_{m'}.
}
\]
Equal-heat geometry sees only tangent motion along \(\kappa=\text{const}\) and therefore necessarily leaves the quadratic invariant \(|k|^2\).  The physical generator \(-\nu C^2\) is the distinguished normal direction that calibrates this fifth mode.

This gives the correct late-stage split:
\[
\boxed{
\text{A+B / projective geometry: tangent control ingredients on heat fibers},
}
\]
\[
\boxed{
\nu C^2: normal heat calibration}.
}
\]
The two pieces must be coupled; neither should be promoted to an independent new budget.

---

## 8. Why Codazzi appeared, and why estimating it alone loops -- EXACT INTERPRETATION

At the physical fold the historical source is the longitudinal covariant rate of
\[
4J_{\rm flip}=\mathscr O_0(u)u.
\]
Its free symmetric off-diagonal second jet is the Codazzi block \(C_H\).  In Fourier diamond coordinates the same non-affine sector appears as a second difference of modal rates.  Thus Codazzi is a derivative coordinate of the complete signature, not a new source species.

Trying to close the endpoint by a stand-alone estimate
\[
\int\|\Lambda^{-1}C_H\|_2^2dt<\infty
\]
throws away the tangent/normal coupling.  The NEO cubic near-phase null recovers the missing half derivative spatially, but two viscous \(L_t^2\) factors still lose time integrability.  The repeated appearance of time-packing, refuge migration, and Codazzi-rate concentration is therefore a symptom of using a non-hypocoercive energy.

---

## 9. The complete signature already supplies first-jet Korn observability -- EXACT

The mother
\[
E_v=[\nabla_v,C]
\]
recovers the strain of any tangent vector \(v\).  On the periodic divergence-free class,
\[
\boxed{
2\|S(v)\|_{\dot H^s}^2=\|v\|_{\dot H^{s+1}}^2
}
\]
and the principal-symbol sphere average gives the exact isometry
\[
\boxed{
\|v\|_{\dot H^{s+1}}^2
=\frac{15}{2}
\int\fint_{S^2}
\|\Lambda_x^s\sigma_1(E_v)(x,n)\|_{HS(n^\perp)}^2\,dn\,dx.
}
\]
Six fixed microlocal directions already form a uniform frame.  Hence Theory 2 does not need a new observability principle at the last step: the complete signature already has a bandwidth-independent Korn theorem for tangent vectors.

The remaining task is to show that the physical A+B/heat measurements form a coercive **parabolic frame** for the non-symmetry part of the actual NS tangent.

---

## 10. The real final key: a hypocoercive Polar--Korn lemma -- OPEN

The radial--Jordan--Codazzi acceleration identity is exact:
\[
\boxed{
EQ'-\frac E2\ddot{\mathcal R}_0-W_\Lambda^2
=\mathcal U\bigl(\langle\Lambda u,Z_{\rm Cod}\rangle+\mathcal C_{\rm compat}\bigr).
}
\]
The representation-free visibility speed is
\[
\boxed{
\mathfrak v=\frac{W_\Lambda^2}{\mathcal U}.
}
\]
A finite singular endpoint forces
\[
\boxed{
\int^{T_*}\mathfrak v(t)\,dt=\infty.
}
\]
The crucial observation is that the acceleration identity already produces the negative square \(-W_\Lambda^2\).  A successful final estimate should therefore not square the Codazzi coupling separately.  It should add a cross term between the angular/equal-heat coordinate and the radial/heat coordinate so that differentiation exposes this square and absorbs the compatibility terms through A+B, radial variance, Curl--Killing, and the genuine viscous generator.

The target is a modified energy \(\mathscr E_{\rm T2}\) satisfying schematically
\[
\boxed{
\frac d{dt}\mathscr E_{\rm T2}
+c\,\frac{W_\Lambda^2}{\mathcal U}
\le
\text{terms already owned by genuine viscosity},
}
\]
with \(c>0\) universal on the typed physical class.

Equivalently, one seeks a **hypocoercive Polar--Korn inequality** coupling

1. A+B reciprocal conductance/finite incidence plus projective/reflection tangent control;
2. the \(\nu C^2\) normal heat direction;
3. exact mother/signature Korn observability;
4. Curl--Killing and radial--Jordan compatibility;
5. the built-in \(-W_\Lambda^2\) square of the acceleration law.

If such an estimate is proved, then
\[
\int^{T_*}\mathfrak v<\infty
\]
contradicts the exact singular-endpoint visibility theorem.  That would close the historical \(Y\Rightarrow\bot\) implication.

No such modified-energy inequality is proved in this PR.  The point of the reconstruction is that the target is now typed much more narrowly than "control Codazzi": the missing key is the cross term that converts the certified local tangent controls and distinguished heat-normal calibration into a hypocoercive visibility estimate.

---

## 11. Proof-status ledger

| Item | Status after this update |
|---|---|
| Abstract forced heat barrier misses one half derivative | **EXACT** |
| Moving spectral flag supplies exactly that half derivative before contraction | **EXACT** |
| Reflection corridor controlled by radial variance | **EXACT / DEDUCTION** |
| Reciprocal sharp lower bound \(Q\chi_{\rm geom}^2/|p-p'|\ge\sqrt6/8\) | **CERTIFIED THEOREM** |
| Reciprocal canonical multiplicity \(\le2\) + Jacobian null classification | **EXACT SYMBOLIC THEOREM** |
| Equal-heat collision invariants contain \(1,k,|k|^2\) | **EXACT** |
| No extra kernel on lattice boxes \(K\le3\) | **AUDIT** |
| Complete mother/signature Korn observability | **EXACT THEOREM** |
| Global hypocoercive Polar--Korn modified-energy estimate | **OPEN** |
| Global 3D NS regularity | **OPEN** |

The intended research discipline is therefore:

\[
\boxed{
\text{do not introduce a new observer until the Polar--Korn coupling itself has been tested.}
}
\]
