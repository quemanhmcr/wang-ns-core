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

## 9.5. Realtime anti-loop reduction: the parabolic synchronization kernel -- EXACT / AUDIT / OPEN TRANSFER

The dynamic scalar triangle already gives
\[
EQ-\frac E2\dot{\mathcal R}_0=\mathcal U W_\Lambda.
\]
Differentiating this identity is exactly the radial--Jordan--Codazzi acceleration identity before the Codazzi rendering is substituted.  Therefore a modified energy built only by algebraically recombining
\[
\mathcal U,\qquad \mathcal R_0,\qquad Q,\qquad W_\Lambda
\]
cannot create new coercivity by itself: at scalar level one only rewrites the same polar triangle.  A genuine Polar--Korn closure must use the information that was lost by scalar contraction, namely the physical pair-source/projective tangent geometry together with the heat-normal direction.

That coupling has a canonical rate variable.  On an active Fourier/helical coefficient put
\[
\eta_k=\frac{N_k}{a_k},
\qquad
\boxed{r_k=\frac{\dot a_k}{a_k}=\eta_k-\nu|k|^2.}
\]
For two parent pairs with the same output, define the physical parabolic synchronization defect
\[
\boxed{
\delta_\Diamond r
:=r_p+r_m-r_{p'}-r_{m'}
=\Delta_\Diamond^\nu\eta.
}
\]
This is not a new observer.  If
\[
f_e=C_ea_pa_m
\]
is one existing helical pair source, then exactly
\[
\dot f_e=(r_p+r_m)f_e.
\]
Thus \(\delta_\Diamond r\) is the relative logarithmic rate by which two already-existing same-output source atoms lose synchronization.

### Exact continuum kernel lemma

There are two nested functional equations.

First, if a \(C^2\) function \(\eta\) satisfies
\[
\eta(p)+\eta(m)=\eta(p')+\eta(m')
\]
for all local elastic diamonds
\[
p+m=p'+m',
\qquad
|p|^2+|m|^2=|p'|^2+|m'|^2,
\]
then
\[
\boxed{
\eta(k)=\alpha+\beta\cdot k+\gamma|k|^2.
}
\]
Indeed, writing
\[
p=c+z,\qquad m=c-z,
\]
the sum \(\eta(c+z)+\eta(c-z)\) is radial in \(z\).  Its quadratic Taylor term therefore forces
\[
\operatorname{Hess}\eta(c)=\lambda(c)I.
\]
In dimension at least two, equality of the diagonal second derivatives and vanishing of the mixed derivatives force \(\lambda\) to be constant, giving the displayed quadratic-affine form.  This is the continuum version of the five collision invariants.

Second, after the physical heat calibration, suppose a \(C^1\) rate \(r\) satisfies
\[
\boxed{
\delta_\Diamond r=0
}
\]
for all local same-output parallelograms.  Taking
\[
p=x+h,\qquad m=y,\qquad p'=x,\qquad m'=y+h
\]
gives
\[
r(x+h)-r(x)=r(y+h)-r(y).
\]
Hence every sufficiently small increment depends only on \(h\), not on the base point.  Differentiating in \(h\) at zero gives a base-point-independent gradient, so
\[
\boxed{
r(k)=\sigma+b\cdot k.}
\]
The heat mode has disappeared.  The kernel has collapsed from
\[
1,k_x,k_y,k_z,|k|^2
\]
to exactly
\[
\boxed{1,k_x,k_y,k_z.}
\]
These are precisely the amplitude/translation symmetry directions appearing in the historical affine-synchronization terminal theorem.

The same conclusion upgrades to the actual two-helicity full-vector source grammar on a connected open nonzero-frequency region.  Let \(r_+(k),r_-(k)\) be \(C^1\) physical logarithmic rates, and assume that all nonzero full-vector source atoms with one common output synchronize their parent-rate sums.  On a generic noncollinear parent pair with unequal radii, the exact source zero set (20.85) removes none of the four parent-helicity choices.  Comparing the \((+,+)\) and \((+,-)\) atoms with the same geometric parents gives
\[
r_+(m)=r_-(m),
\]
and comparing \((+,+)\) with \((-,+)\) gives the same equality at \(p\).  Hence the two sheet rates agree on the generic set, and continuity extends the equality across the codimension-one source-null seams.  The remaining same-output synchronization equation is therefore the scalar parallelogram equation above, so
\[
\boxed{
r_+(k)=r_-(k)=\sigma+b\cdot k.
}
\]
Thus **full physical parabolic source synchronization has no hidden helicity mode**.  Its continuum kernel is exactly affine.

### Physical finite-helical audit

`audits/parabolic_synchronization_kernel.py` tests the same statement without replacing the NS pair grammar by a complete abstract graph.

For the kinematic same-output relation matrix on lattice boxes \(|k_i|\le K\), the observed kernel is exactly four-dimensional for
\[
K=1,2,3,4,
\]
with first positive eigenvalues approximately
\[
2.2176,\qquad2.7836,\qquad2.9827,\qquad3.0790.
\]

More importantly, the audit then keeps only parent pairs whose full Leray vector source is nonzero according to the exact zero set (20.85): collinear shear and the same-helicity equal-radius Beltrami equator are removed, and no other nondegenerate pair is removed.  The resulting synchronization incidence matrix has integer entries, so its rank is certified exactly modulo the prime \(1000003\).  The results are
\[
\begin{array}{c|c|c|c}
R^2&\text{helical nodes}&\text{rank}&\text{nullity}\\\hline
2&36&30&6\\
3&52&48&4\\
5&112&108&4\\
6&160&156&4.
\end{array}
\]
The deliberately poor \(R^2=2\) window is a negative control: its interaction category is not rich enough and two extra directions survive.  As soon as the next physical shell is present, the kernel collapses exactly to the four affine directions, and stays there on the larger tested windows.

This is the correct anti-loop signal.  The remaining theorem should not ask for the next derivative of Codazzi.  It should prove a **quantitative stability/coercivity version of this parabolic synchronization functional equation on the actual physical source category**, with the A+B/reflection geometry supplying tangent conductance and \(-\nu C^2\) supplying the missing heat-normal calibration.

The clean terminal chain would then be
\[
\boxed{
\begin{gathered}
\text{finite singular endpoint}
\Longrightarrow
\text{mandatory macroscopic source coherence},\\
\text{A+B + reflection + physical heat}
\Longrightarrow
\text{vanishing/controlled parabolic synchronization defect},\\
\delta_\Diamond r\to0
\Longrightarrow
r(k)=\sigma+i\,v\cdot k
\quad\text{modulo the physical reality symmetry},\\
\text{affine synchronization}
\Longrightarrow
\text{monochromatic translating/decaying terminal physics or the zero }L^2(\mathbb R^3)\text{ state},\\
\Longrightarrow\bot.
\end{gathered}}
\]

The kernel classification is no longer the missing item.  The **OPEN transfer** is the single quantitative arrow from endpoint coherence, through the already-certified A+B/reflection/heat geometry, to coercive control of the parabolic synchronization defect.  If an attempted proof of that arrow produces a new uncontrolled jet or wallet, it has re-entered the historical loop and must be stopped rather than prolonged.



---

## 9.55. Endpoint raw UV amplification is **not yet coherence** -- EXACT DEDUCTION / SCALING CORRECTION

Let \(J_{>L}\) denote the all-three-roots high-frequency hard-flip resultant from the exact excision theorem, and let \(S_{2,>L}\) be the corresponding restriction of the microscopic edge-source square.  The established endpoint facts give, for every fixed finite \(L\),
\[
\int_0^{T_*}\|J_{>L}(t)\|_2^2\,dt=\infty,
\qquad
\int_0^{T_*}S_{2,>L}(t)\,dt<\infty.
\]
Hence for every \(M<\infty\) there are times arbitrarily close to the endpoint at which
\[
\boxed{
\|J_{>L}(t)\|_2^2\ge M\,S_{2,>L}(t).
}
\]
One may therefore choose \(L_n\to\infty\), \(M_n\to\infty\), \(t_n\uparrow T_*\) with
\[
\boxed{
\frac{\|J_{>L_n}(t_n)\|_2^2}{S_{2,>L_n}(t_n)}\to\infty.
}
\]
Every edge in the selected high-frequency restriction has
\[
\kappa_e=|p|^2+|m|^2\ge2L_n^2.
\]

The realtime Theory-2 typing correction is that this quotient is **not scale invariant**, so it must not be called projective coherence.  On the whole-space parabolic scaling relevant to a singular microscope,
\[
u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),
\qquad
\widehat u_\lambda(k,t)=\lambda^{-2}\widehat u(k/\lambda,\lambda^2t).
\]
A quadratic one-derivative edge-source density scales as
\[
 f_\lambda(p,m,t)
 =\lambda^{-3}f(p/\lambda,m/\lambda,\lambda^2t).
\]
Since the edge measure has six Fourier dimensions,
\[
\boxed{S_{2,\mathrm{edge}}[u_\lambda](t)=S_{2,\mathrm{edge}}[u](\lambda^2t),}
\]
whereas convolution over one three-dimensional parent fiber gives
\[
\widehat J_\lambda(q,t)=\widehat J(q/\lambda,\lambda^2t),
\qquad
\boxed{
\|J[u_\lambda](t)\|_2^2
=\lambda^3\|J[u](\lambda^2t)\|_2^2.
}
\]
Consequently
\[
\frac{\|J[u_\lambda]\|_2^2}{S_{2,\mathrm{edge}}[u_\lambda]}
=\lambda^3
\frac{\|J[u]\|_2^2}{S_{2,\mathrm{edge}}[u]},
\]
and at spacetime level
\[
\int S_{2,\mathrm{edge}}[u_\lambda]dt
=\lambda^{-2}\int S_{2,\mathrm{edge}}[u]dt,
\qquad
\int\|J[u_\lambda]\|_2^2dt
=\lambda\int\|J[u]\|_2^2dt.
\]
Thus raw resultant amplification can be produced by ordinary concentration scaling even when the scale-normalized source geometry does not become more coherent.

If a packet has one characteristic physical frequency \(K\), the dimensionless static amplification is instead of the form
\[
\boxed{
\mathfrak A_K
:=\frac{\|J_K\|_2^2}{K^3 S_{2,K}}.
}
\]
The endpoint facts above do **not** presently imply \(\mathfrak A_{K_n}\to\infty\).  Therefore Section 9.55 supplies an all-UV concentration sequence, but not yet a projectively aligned source packet.  Any later compactness argument must preserve a scale-normalized quantity, or use the canonical moving-front scale, before invoking A+B/projective rigidity.

This correction is an anti-loop gain: it removes a false interpretation rather than manufacturing a stronger descendant to support it.

---

## 9.6. Source-projective Fisher identity: the microscopic Polar--Korn law -- EXACT / OPEN OWNER

The synchronization defect has an intrinsic metric meaning on the already-existing physical edge-source field; no new rate tensor is required.  Fix a child/source sector and write
\[
\dot f_e=\lambda_e f_e,
\qquad
\lambda_e=r_p+r_m.
\]
Let
\[
M=\int |f_e|^2\,de,
\qquad
d\mu(e)=\frac{|f_e|^2}{M}\,de.
\]
Then the complex projective/Fubini--Study speed of the source ray is exactly
\[
\boxed{
\frac{M\|\dot f\|_2^2-|\langle f,\dot f\rangle|^2}{M^2}
=
\operatorname{Var}_\mu(\lambda)
=
\frac12\iint |\lambda_e-\lambda_{e'}|^2\,d\mu(e)d\mu(e').
}
\]
For two same-output atoms the difference \(\lambda_e-\lambda_{e'}\) is precisely \(\delta_\Diamond r\).  Thus the parabolic synchronization Dirichlet form is not an invented Codazzi norm: it is the projective Fisher speed of the true quadratic source field.

Writing
\[
\lambda_e=\eta_e-\nu\kappa_e,
\qquad
\eta_e:=\eta_p+\eta_m,
\qquad
\kappa_e:=|p|^2+|m|^2,
\]
gives an exact tangent/normal variance decomposition
\[
\boxed{
\operatorname{Var}_\mu(\lambda)
=
\operatorname{Var}_\mu(\eta)
+\nu^2\operatorname{Var}_\mu(\kappa)
-2\nu\operatorname{Re}\operatorname{Cov}_\mu(\eta,\kappa).
}
\]
There is also a canonical heat-normal cross identity.  With
\[
\bar\kappa=\int\kappa\,d\mu,
\]
the normalized source weights obey
\[
\dot\mu_e=2\bigl(\operatorname{Re}\lambda_e-\operatorname{Re}\bar\lambda\bigr)\mu_e,
\]
and therefore
\[
\boxed{
\dot{\bar\kappa}
+2\nu\operatorname{Var}_\mu(\kappa)
=
2\operatorname{Re}\operatorname{Cov}_\mu(\kappa,\eta).
}
\]
This is the microscopic Polar--Korn structure sought in Sections 7--10: physical heat contributes the normal variance with a favorable sign, while nonlinear source-rate variation supplies the tangent forcing.  The five-to-four kernel collapse of Section 9.5 is the zero-set statement of the same geometry.

`audits/source_projective_fisher.py` verifies the projective numerator identity, the pairwise variance formula, the heat-normal identity and the tangent/normal split to machine precision on random complex source fields.

The realtime anti-loop consequence is equally important.  The identity does **not** by itself make the Fisher action finite.  Bounding \(\|\dot f\|\) as a new source-rate norm would merely recreate the Codazzi/time-packing loop.  A valid final argument must therefore do one of exactly two things:

1. show that the projective Fisher action is paid by the already-owned A+B/reflection/heat geometry on an interaction-rich stratum; or
2. pass to a normalized terminal sequence on which this action degenerates, so the exact affine synchronization kernel and terminal rigidity apply.

No third rate/jet owner is licensed.


There is also a source-space visibility-speed consequence.  Since
\[
\dot{\bar\kappa}
=2\operatorname{Re}\operatorname{Cov}_\mu(\kappa,\lambda),
\qquad
\lambda=r_p+r_m,
\]
Cauchy gives
\[
\boxed{
\frac{\dot{\bar\kappa}^{\,2}}{4\bar\kappa}
\le
\frac{\operatorname{Var}_\mu(\kappa)}{\bar\kappa}
\operatorname{Var}_\mu(\lambda).
}
\]
Hence any finite-time normalized source packet with \(\bar\kappa(t_n)\to\infty\) must satisfy
\[
\boxed{
\int^{T_*}
\frac{\operatorname{Var}_\mu(\kappa)}{\bar\kappa}
\operatorname{Var}_\mu(\lambda)\,dt
=\infty.
}
\]
Indeed this is the same Cauchy argument as for \((\sqrt{\mathcal U})'\): finite action would keep \(\sqrt{\bar\kappa}\) bounded on a finite interval.  The two factors have the desired typing: \(\operatorname{Var}_\mu(\kappa)\) is the heat-normal spread and \(\operatorname{Var}_\mu(\lambda)\) is exactly the parabolic synchronization/projective-Fisher defect.

This conditional identity should not be silently upgraded to the full endpoint theorem.  The all-three-roots UV result proves that singular torsion escapes every fixed frequency scale, but a publish-grade closure must still construct a canonical normalized physical source packet (or an equivalent projective-limit object) whose mean heat escapes and for which the A+B/flag conductance passes to the limit.  That extraction/transfer is now the precise remaining analytic seam.

---

## 10. The real final key: a parabolic Source--Korn / hypocoercive Polar--Korn transfer -- OPEN

Section 9.5 sharpens what a successful modified energy is allowed to do.  A scalar recombination of the dynamic polar triangle is tautological, while a naive state-weighted source Korn gap can degenerate near sparse/source-null states.  Therefore the target must be **stratified**: interaction-rich states are controlled through parabolic source-synchronization coercivity, while degeneration of that coercivity must converge to an already-classified harmless/source-null terminal geometry rather than create another jet.

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
with \(c>0\) uniform on each quantitatively interaction-rich stratum; degeneration of that richness belongs to the terminal-rigidity branch, not to a claim of one global source-weighted gap.

Equivalently, one seeks a **parabolic Source--Korn / hypocoercive Polar--Korn dichotomy** coupling

1. A+B reciprocal conductance/finite incidence plus projective/reflection tangent control;
2. the \(\nu C^2\) normal heat direction;
3. exact mother/signature Korn observability;
4. Curl--Killing and radial--Jordan compatibility;
5. the built-in \(-W_\Lambda^2\) square of the acceleration law.

On the interaction-rich stratum this may be realized by a modified-energy estimate of the displayed type.  On a degenerating stratum the required conclusion is instead terminal rigidity: the state must approach the Beltrami/shear/monochromatic or affine-synchronized null geometries already known to be harmless.  No new descendant is permitted in that branch.

If this stratified transfer is proved, then
\[
\int^{T_*}\mathfrak v<\infty
\]
contradicts the exact singular-endpoint visibility theorem.  That would close the historical \(Y\Rightarrow\bot\) implication.

No such stratified transfer theorem is proved in this PR.  The point of the reconstruction is that the target is now typed much more narrowly than "control Codazzi": the missing key is a coercivity-or-rigidity mechanism that converts the certified local tangent controls and distinguished heat-normal calibration into a finite visibility action without creating another descendant.

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
| No extra equal-heat kernel on lattice boxes \(K\le3\) | **AUDIT** |
| Full physical parabolic source-synchronization kernel on a connected local continuum domain | **EXACT AFFINE-RIGIDITY THEOREM** |
| Physical full-vector synchronization kernel is exactly four-dimensional on tested interaction-rich windows | **EXACT ACTIVE-SET CLASSIFICATION / EXACT MODULAR RANK** |
| Source-projective Fisher / heat-normal microscopic Polar--Korn identities | **EXACT** |
| Endpoint coherence \(\Rightarrow\) coercive/vanishing parabolic synchronization defect | **OPEN TRANSFER** |
| Complete mother/signature Korn observability | **EXACT THEOREM** |
| Global stratified Source--Korn / hypocoercive Polar--Korn transfer | **OPEN** |
| Global 3D NS regularity | **OPEN** |

The intended research discipline is therefore:

\[
\boxed{
\text{do not introduce a new observer until the Polar--Korn coupling itself has been tested.}
}
\]
