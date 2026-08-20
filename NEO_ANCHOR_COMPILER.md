# NEO Core Compiler
Companion synthesis: [NS Polar Compatibility Architecture](history/NS_POLAR_COMPATIBILITY_ARCHITECTURE.md).
This file is the canonical NEO manual for the Wang--Navier--Stokes programme. Its purpose is not to add a second geometry to Navier--Stokes. Its purpose is to reconstruct the genuine 3D incompressible Navier--Stokes equation, its standard geometric faces, and its finite derived jets from the smallest fixed structural language presently known.
**Strategic scope.** NEO is strongest as a reconstruction and normalization compiler: it exposes exact parentage, canonical gauges, and rigid zero sets of genuine NS structures. It is **not necessary**, and is not presently justified, to make NEO control every metamorphosis of an arbitrary full trajectory. Reconstruction completeness is not control completeness.
**Regularity use.** For the blow-up problem, prefer a terminal use of the compiler: first extract a scale-normalized hypothetical singular tangent/ancient object by the appropriate analytic compactness machinery, then run NEO on that object as a **singularity normalizer and rigidity compiler**. Approximate defects along the raw trajectory should be prolonged only when a proof needs them; otherwise the goal is to pass to a limit where NEO's exact zero-set classifications become decisive.
**Anti-loop rule.** A new descendant is progress only if it eliminates an admissible singular normal form, lowers a genuine analytic gap, produces coercivity with an owned finite budget, or yields a direct contradiction. Merely moving the remaining freedom to the next compiled jet is description, not closure.
The typed anchor interface is
\[
\boxed{u(t),\qquad P,\qquad C=\operatorname{curl},\qquad C^2=(-\Delta)P,\qquad t.}
\]
Fixed Euclidean products and contractions already present in the equation are allowed. Everything else must first pass the compiler question
\[
\boxed{\text{Can this object be generated from }(u,P,C,C^2,t)\text{ by the NEO grammar?}}
\]
If yes, it is a **costume**, not a new primitive.
The standing labels are **EXACT**, **DEDUCTION**, **INTERPRETATION**, **CANDIDATE PRINCIPLE**, **OPEN**, and **AUDIT**. Numerical or finite-Fourier tests are always **AUDIT** only. Nonsmooth functional calculus, zero curl spectrum, unbounded operators and critical spaces require explicit localization/domain care.
The central shift of the present compiler is this:
\[
\boxed{
\text{curl is not merely one observable of NS; its matrix, spectrum, commutators and square generate the working language.}
}
\]
The matrix of \(C\) contains spatial differential structure, the spectrum of \(C\) contains Hodge/helicity/radial structure, commutators with multiplication generate local nonlinear deformation, and \(C^2\) is the physical heat generator. The compiler should therefore become smaller as it becomes stronger.
## 1. Typed anchors and domain discipline — EXACT
Work first on smooth finite-energy vector fields on \(\mathbb R^3\), with the usual Helmholtz decomposition. On the ambient vector-field Hilbert space,
\[
\boxed{P^2=P,\qquad PC=CP=C,\qquad C^2=(-\Delta)P.}
\]
On the actual incompressible state,
\[
Pu=u,
\qquad
C^2u=-\Delta u.
\]
On \(L^2(\mathbb R^3;\mathbb R^3)\), the nonzero spectral support of curl is the divergence-free block, so spectrally
\[
P=\mathbf 1_{\mathbb R\setminus\{0\}}(C)
\]
up to the harmless Fourier seam at \(k=0\). This spectral redundancy does **not** mean that \(P\) should be deleted from the typed interface. On domains with harmonic sectors, for example the torus, nonzero divergence-free harmonic fields can lie in \(\ker C\). The compiler therefore keeps \(P\) and \(C^2\) as typed anchors even when they are spectrally reconstructible on the Clay \(\mathbb R^3\) setting.
**Protocol.** Never identify zero curl eigenvalue with zero Fourier frequency. For each nonzero \(k\), the longitudinal direction is a zero eigenvector of \(C(k)\).
**Protocol.** Never infer a new mechanism from a change of tensor type, gauge, observer, projection or differentiation order. Parentage is the ontology test.
## 2. One curl has two complete faces: matrix and spectrum — EXACT
For Fourier covector \(k\),
\[
C(k)=i\,k\times,
\]
with matrix entries
\[
C_{ab}(k)=i\varepsilon_{ajb}k_j.
\]
Contracting the Levi--Civita symbols gives
\[
\boxed{i k_m=\frac12\sum_{a,b}\varepsilon_{amb}C_{ab}(k).}
\]
Hence in physical space, in any fixed Euclidean frame,
\[
\boxed{\partial_m=\frac12\sum_{a,b}\varepsilon_{amb}C_{ab}.}
\]
Thus the matrix entries of curl generate the full constant-coefficient first-order differential calculus. Repeated compositions generate every constant-coefficient spatial derivative.
The spectral face of the same operator is
\[
\operatorname{spec}C(k)=\{-|k|,0,+|k|\}.
\]
Define, with zero extension on \(\ker C\),
\[
H:=\operatorname{sgn}C,
\qquad
\Lambda:=|C|.
\]
Then
\[
\boxed{H^2=P,\qquad C=H\Lambda=\Lambda H,\qquad \Lambda^2=C^2=(-\Delta)P.}
\]
The helicity projections are
\[
\Pi_\pm=\frac12(P\pm H),
\qquad
Q:=I-P.
\]
At scalar spectral value \(x\), the complete static anchor algebra is
\[
p=1_{x\ne0},
\qquad
h=\operatorname{sgn}x,
\qquad
\lambda=|x|,
\]
\[
\boxed{p^2=p,\qquad h^2=p,\qquad x=h\lambda,\qquad \lambda^2=x^2.}
\]
**DEDUCTION.** The same \(C\) has two complementary readings:
\[
\boxed{
\text{matrix of }C\Rightarrow\text{spatial differential geometry},
\qquad
\text{spectrum of }C\Rightarrow\text{Hodge/helicity/radius/heat}.
}
\]
This dual completeness is the structural reason NEO can reconstruct both local and spectral faces without multiplying primitives.
## 3. Curl commutators are the local differential grammar — EXACT
Let \(M_\phi\) denote multiplication by a scalar \(\phi\), and let
\[
X_a v:=a\times v
\]
be pointwise cross multiplication. Direct vector calculus gives
\[
\boxed{[C,M_\phi]=X_{\nabla\phi}.}
\]
The map \(a\mapsto X_a\) is injective, so \(\nabla\phi\) is recovered uniquely from this commutator. Thus gradient is a compiled operation rather than an independent NEO primitive.
The commutator derivation
\[
\mathfrak d_C(A):=[C,A]
\]
obeys
\[
\boxed{\mathfrak d_C(AB)=\mathfrak d_C(A)B+A\mathfrak d_C(B).}
\]
Since \([C,M_\phi]\) is again a multiplication operator,
\[
\boxed{[[C,M_\phi],M_\psi]=0.}
\]
This is the algebraic first-order locality of curl.
The square anchor satisfies
\[
\boxed{[C^2,M_\phi]=\{C,[C,M_\phi]\}.}
\]
A second scalar commutator gives
\[
\boxed{
[[C^2,M_\phi],M_\psi]
=X_{\nabla\psi}X_{\nabla\phi}+X_{\nabla\phi}X_{\nabla\psi},
}
\]
and therefore
\[
\boxed{[[[C^2,M_\phi],M_\psi],M_\chi]=0.}
\]
This is the algebraic second-order locality of the heat generator.
**DEDUCTION.** Local completeness: Every finite Euclidean differential polynomial built from
\[
u,\nabla u,\ldots,\nabla^m u
\]
by fixed dot, cross, tensor product, contraction and constant tensors is generated from \(u\), \(C\) and multiplication. Strain, rotation, Hessians, local stress tensors and local Riccati expressions are therefore one already-collapsed wardrobe class.
**INTERPRETATION.** Differential order can be read internally by scalar-commutator depth. Local polynomial functions of \(C\) have terminating commutator towers; genuine nonlocal spectral functions such as \(H\) and \(\Lambda\) instead generate divided-difference towers.
## 4. Canonical isotropic nonlocal readers and tensors have curl normal forms — EXACT
Let \(T\) be translation invariant on divergence-free vectors and rotationally covariant: \(T(Rk)=RT(k)R^{-1}\). For \(k\ne0\), the \(SO(2)\) stabilizer of \(k\) has commutant generated on \(k^\perp\) by the identity and \(i\widehat k\times\). Hence
\[
\boxed{T(k)=a(|k|)P(k)+b(|k|)H(k)=f(C(k))}
\]
with \(f(\pm r)=a(r)\pm b(r)\). Thus \(H,\Lambda^s,\Pi_\pm,C^\dagger=H\Lambda^{-1}\) and the heat semigroup are one-slot curl readers whenever their domains are meaningful. In particular \([f(C),H]=0\): a fixed isotropic reader cannot itself flip helicity.
The same reconstruction extends to finite-rank isotropic tensor symbols. Put
\[
\mathcal R_j:=\partial_j(-\Delta)^{-1/2},\qquad \sigma(\mathcal R_j)=i\,\widehat k_j.
\]
The derivative \(\partial_j\) is already a matrix entry of \(C\), while \(( -\Delta)^{1/2}\) is square-anchor functional calculus; on physical vectors it equals \(\Lambda\). The isotropic tensor representation theorem for one direction says that every smooth finite-rank \(SO(3)\)-equivariant symbol on \(k\ne0\) is a finite sum
\[
\boxed{a_\alpha(|D|)\operatorname{Contr}_\alpha(\delta,\varepsilon,\mathcal R),}
\]
subject only to the input/output tensor symmetries. Hence canonical Riesz, Leray and pressure-tidal tensor readers belong to a **tensor envelope**, not a new ontology. For example
\[
\boxed{P_{ij}=\delta_{ij}+\mathcal R_i\mathcal R_j,\qquad
(H_0)_{ij}=\Big(\frac13\delta_{ij}+\mathcal R_i\mathcal R_j\Big)g,\quad g=-\Delta p.}
\]
For symmetric rank-two output there is also a canonical fiber normal form. With \(Q=I-P=n\otimes n\),
\[
\boxed{T=QTQ+\frac12\operatorname{tr}(PTP)P+(QTP+PTQ)
+\Big(PTP-\frac12\operatorname{tr}(PTP)P\Big).}
\]
These are the two spin-zero sectors, the spin-one mixed sector and the spin-two transverse sector of the \(SO(2)\) stabilizer. All four projectors are compiled from \(P,Q\) and contractions. In particular incompressible strain is pure spin one,
\[
S(k)=\frac{i|k|}{2}(n\otimes\widehat u+\widehat u\otimes n),
\]
while \(H_0(k)=(I/3-Q)\widehat g\) is spin zero; hence \(\langle S,H_0\rangle_{L^2}=0\) is a tensor-type selection rule rather than an independent pressure cancellation.
For any symmetric stress \(\Sigma\), put \(\sigma_Q=n\cdot\Sigma n\) and \(v=P\Sigma n\). The same decomposition gives
\[
\boxed{P\operatorname{div}\Sigma=i|k|v,\qquad Q\operatorname{div}\Sigma=i|k|\sigma_Qn.}
\]
Thus for the convective stress \(\Sigma=u\otimes u\), \(N=-i|k|v\) and \(p=-\sigma_Q\): Euler acceleration is the mixed spin-one stress output, pressure is the longitudinal spin-zero output, and the transverse-trace/spin-two sectors are divergence-dark at that child.
**OPEN.** This classifies translation-invariant isotropic finite-rank symbols away from the zero seam; anisotropic, variable-coefficient, boundary and harmonic sectors require separate typing.
## 5. The genetic Navier--Stokes equation: commutator plus square — EXACT
Define \(X_u v=u\times v\). Since \(X_uu=0\),
\[
[X_u,C]u=u\times Cu.
\]
The rotational form of incompressible Navier--Stokes is therefore
\[
\boxed{
\partial_tu=P[X_u,C]u-\nu C^2u.
}
\]
This is the **NEO genetic equation**.
The two terms use the same structural operator in different ways:
\[
\boxed{
\text{Euler nonlinearity}=\text{projected curl--multiplication noncommutation},
}
\]
\[
\boxed{
\text{viscosity}=\text{curl square}.
}
\]
Let
\[
L_{\rm raw}:=[X_u,C]u=u\times Cu.
\]
Its Hodge split is
\[
\boxed{PL_{\rm raw}=N:=P(u\times Cu),}
\]
\[
\boxed{QL_{\rm raw}=\nabla B,\qquad B=p+\frac12|u|^2.}
\]
Hence projected Euler acceleration and Bernoulli/pressure correction are tangent and normal faces of one genetic commutator defect.
The standard conservation cancellations are immediate:
\[
\boxed{\langle u,N\rangle=0,\qquad \langle Cu,N\rangle=0.}
\]
Thus energy and helicity are the affine spectral skeleton \(1,C\) on which the Euler commutator is invisible.
**INTERPRETATION.** Nonlinear multiplier visibility begins only when the spectral reader bends away from the affine span of \(1\) and \(C\). The critical fold \(\Lambda=|C|\) is the canonical example.
## 6. Material transport, Lie bracket and intrinsic connection are curl macros — EXACT
For smooth divergence-free \(a,b\),
\[
C(a\times b)=D_ba-D_ab,
\qquad D_a:=a\cdot\nabla.
\]
Hence
\[
\boxed{[a,b]_{\rm Lie}=D_ab-D_ba=-C(a\times b).}
\]
The standard gradient identity gives
\[
\nabla(a\cdot b)=D_ab+D_ba+a\times Cb+b\times Ca.
\]
Solving for transport,
\[
\boxed{
D_ab=\frac12\Big[
\nabla(a\cdot b)-a\times Cb-b\times Ca-C(a\times b)
\Big].
}
\]
Since gradient is already generated by Section 3, \(D_a\) is a NEO macro.
Define the symmetric Euler polarization
\[
\boxed{B(a,b):=\frac12P(a\times Cb+b\times Ca).}
\]
It also has the pure commutator form
\[
\boxed{
B(a,b)=\frac12P\big([X_a,C]b+[X_b,C]a\big).
}
\]
Then \(N=B(u,u)\).
The projected divergence-free connection is
\[
\mathcal D_ab:=PD_ab,
\]
and therefore
\[
\boxed{
\mathcal D_ab=-B(a,b)-\frac12C(a\times b)
=-B(a,b)+\frac12[a,b]_{\rm Lie}.
}
\]
Consequently its symmetric and antisymmetric faces are not independent geometries: both are generated by the same curl algebra.
Pressure, projected connection, Lie geometry and Euler polarization are thus reconstructible before introducing any torsion, curvature or Codazzi costume.
**DEDUCTION — native NS faces reconstruct from one law.** Put \(\omega=Cu\), \(A=\nabla u=S+\Omega\), and \(g=-\Delta p\). The genetic equation, its Hodge split and the transport macro give simultaneously
\[
\boxed{u_t+D_uu=-\nabla p+\nu\Delta u,\qquad
u_t=u\times\omega-\nabla\Big(p+\frac12|u|^2\Big)+\nu\Delta u,}
\]
\[
\boxed{\omega_t+D_u\omega=D_\omega u+\nu\Delta\omega,\qquad
A_t+D_uA+A^2=-\operatorname{Hess}p+\nu\Delta A,}
\]
\[
\boxed{S_t+D_uS+S^2+\Omega^2=-\operatorname{Hess}p+\nu\Delta S,\qquad
g=\operatorname{tr}(A^2)=|S|^2-\frac12|\omega|^2.}
\]
The same genetic law also gives \(S_t=\operatorname{sym}\nabla N+\nu\Delta S\), hence
\[
\boxed{\operatorname{sym}\nabla N=-D_uS-S^2-\Omega^2-\operatorname{Hess}p.}
\]
Thus velocity-pressure, rotational, vorticity-stretching and strain-Riccati formulations are compiler-equivalent faces, not separate dynamics.
## 7. The mother curl jet is a compiled normal form — EXACT
The first spectral deformation is
\[
\boxed{E_a:=[D_a,C].}
\]
Although \(E_a\) remains the most useful **mother jet** for first-order spectral costumes, it is not a primitive compiler verb because \(D_a\) is already reconstructed by Section 6.
Let \(G_a:=\nabla a\) act by matrix multiplication. For divergence-free input \(v\),
\[
D_av=G_av-CX_av.
\]
Therefore
\[
\boxed{E_a=[G_a,C]-C[X_a,C]}
\]
on the physical input block. Both terms are nested curl--multiplication expressions.
The raw local formula is
\[
\boxed{E_av=-\sum_j\nabla a_j\times\partial_jv.}
\]
For the self-contraction,
\[
\boxed{E_uu=(Cu\cdot\nabla)u=S\omega,\qquad \omega=Cu.}
\]
Thus vortex stretching is a contraction of the mother curl deformation, not a new primitive.
Let
\[
K_a:=[D_a,P],
\qquad
A_a:=[D_a,H],
\qquad
L_a:=[D_a,\Lambda].
\]
Differentiating the anchor identities gives
\[
\boxed{PK_a+K_aP=K_a,}
\]
\[
\boxed{HA_a+A_aH=K_a,}
\]
\[
\boxed{E_a=A_a\Lambda+HL_a,}
\]
\[
\boxed{\Lambda L_a+L_a\Lambda=CE_a+E_aC.}
\]
Also
\[
PK_aP=0,
\qquad
QK_aQ=0.
\]
For the actual state,
\[
\boxed{K_uu=QD_uu=-\nabla p.}
\]
Pressure is therefore also the Hodge-normal contraction of the mother deformation.
## 8. Every first spectral costume is a divided-difference filter of the mother jet — EXACT
On a finite nonzero curl-spectral localization, for admissible \(f\),
\[
\boxed{
[D_u,f(C)]_{xy}=f^{[1]}(x,y)E_{u,xy},
\qquad
f^{[1]}(x,y)=\frac{f(y)-f(x)}{y-x}.
}
\]
The diagonal is the corresponding derivative when defined. Nonsmooth readers \(H\), \(\Lambda\) and shifted hinges require the usual seam/domain care.
Hence
\[
C,\quad P,\quad H,\quad \Lambda,\quad |C-a|
\]
do not possess independent first-order deformations. They are filters of one mother jet.
The dynamic costume equation follows directly from the genetic NS equation. For any real admissible spectral reader \(F=f(C)\),
\[
\boxed{
(\partial_t+D_u+\nu C^2)(f(C)u)
=-f(0)\nabla p+[D_u,f(C)]u.
}
\]
If \(f(0)=0\),
\[
\boxed{
(\partial_t+D_u+\nu C^2)(f(C)u)=Df_C[E_u]u.
}
\]
Vorticity, helicity phase and radial modulus are the choices
\[
f(x)=x,\qquad \operatorname{sgn}x,\qquad |x|.
\]
The universal quadratic wardrobe law is
\[
\boxed{
\frac d{dt}\langle f(C)u,g(C)u\rangle
+2\nu\langle Cf(C)u,Cg(C)u\rangle
=\langle u,[D_u,(fg)(C)]u\rangle.
}
\]
Energy, helicity and critical \(\dot H^{1/2}\) balance are therefore three readings of one compiler law.
## 9. Hodge, radial and angular motion form the first NEO prism — EXACT
For physical input, the mother deformation has the orthogonal Hilbert--Schmidt support split
\[
\boxed{
\|E_uP\|_{HS}^2
=\|PE_uP\|_{HS}^2+\|QE_uP\|_{HS}^2.
}
\]
Using
\[
QE_uP=K_uC
\]
and the polar tangent identity yields
\[
\boxed{
\|E_uP\|_{HS}^2
=\|K_uC\|_{HS}^2
+\|PL_uP\|_{HS}^2
+\|\Lambda^{1/2}PA_uP\Lambda^{1/2}\|_{HS}^2.
}
\]
These are the Hodge/support, radial/modulus and angular/phase readings of the same first mother deformation.
**Protocol.** This is an operator/Hilbert--Schmidt Pythagoras. It must never be promoted to a vector \(L^2\) Pythagoras after applying the operators to a spectrally mixed state.
On spectral values \(x,y\), the radial Sylvester relation is
\[
\boxed{(|x|+|y|)L_{xy}=(x+y)E_{xy}.}
\]
Except at the zero-zero block, the denominator is positive.
The phase/support relation is
\[
\boxed{(h(x)+h(y))A_{xy}=K_{xy}.}
\]
Thus \(0\leftrightarrow\pm\) is controlled by Hodge motion, same-helicity intrinsic blocks vanish, while \(+\leftrightarrow-\) is the kernel of the phase Sylvester map. Invertibility migrates to the full-curl relation. If \(x=a>0\), \(y=-b<0\),
\[
\boxed{A_{xy}=\frac{2}{a+b}E_{xy},}
\]
\[
\boxed{L_{xy}=\frac{a-b}{a+b}E_{xy},}
\]
\[
\boxed{|E_{xy}|^2=|L_{xy}|^2+ab|A_{xy}|^2.}
\]
This is the exact localized tangent polar identity.
## 10. Cross-helicity selection is support geometry, not a separate mechanism — EXACT
Let output frequency be \(k\), input frequency \(\ell\), and \(q=k-\ell\). Then
\[
\boxed{
\widehat{[D_u,H]f}(k)
=i\int(\widehat u(q)\cdot\ell)
[H(\ell)-H(k)]\widehat f(\ell)\,d\ell.
}
\]
For helicity input \(h\),
\[
\boxed{\Pi_h(k)[H(\ell)-H(k)]\Pi_h(\ell)=0,}
\]
\[
\boxed{Q(k)[H(\ell)-H(k)]\Pi_h(\ell)=hQ(k)\Pi_h(\ell),}
\]
\[
\boxed{\Pi_{-h}(k)[H(\ell)-H(k)]\Pi_h(\ell)=2h\Pi_{-h}(k)\Pi_h(\ell).}
\]
If \(\theta\) is the angle between \(k\) and \(\ell\),
\[
\boxed{\|\Pi_h(k)\Pi_h(\ell)\|_{HS}=\frac{1+\cos\theta}{2},}
\]
\[
\boxed{\|Q(k)\Pi_h(\ell)\|_{HS}=\frac{|\sin\theta|}{\sqrt2},}
\]
\[
\boxed{\|\Pi_{-h}(k)\Pi_h(\ell)\|_{HS}=\frac{1-\cos\theta}{2}.}
\]
Hence near alignment, support leakage is first order while direct opposite-helicity overlap is second order.
For unit directions \(n,m\), \(n\ne-m\), define the midpoint direction
\[
b=\frac{n+m}{|n+m|}.
\]
Then the opposite-helicity overlap factorizes exactly through the midpoint Hodge sector:
\[
\boxed{
\Pi_{-h}(n)\Pi_h(m)
=2\Pi_{-h}(n)Q_b\Pi_h(m),
}
\]
and more strongly
\[
\boxed{
\Pi_{-h}(n)\Pi_h(m)
=2\Pi_{-h}(n)(P_b-P_n)(P_b-P_m)\Pi_h(m).
}
\]
Thus finite helicity reversal contains two exact support differences. At the antipodal seam the midpoint is noncanonical; this is a geometric seam, not permission to invent a new primitive.
## 11. Principal local transport has no direct opposite-helicity highway — EXACT
The claims in this section are exact at the stated frozen principal-symbol level; they are not full-operator identities unless separately displayed.
Freeze \(A=\nabla u(x)\), write \(\xi=\rho n\), and set
\[
r=A^Tn=\alpha n+\beta,
\qquad \beta\perp n.
\]
The principal symbol of the mother jet is
\[
\boxed{e_u(x,\xi)=-i\rho\,r\times.}
\]
Material covectors obey
\[
\dot\rho=-\rho\alpha,
\qquad
\dot n=-\beta.
\]
On the physical plane,
\[
\boxed{P_ne_uP_n=-\alpha C(\xi),}
\]
\[
\boxed{\Pi_{-h}(n)e_u\Pi_h(n)=0.}
\]
Thus principal local transport produces radial scaling and support steering but no direct intrinsic helicity flip.
The tensorial ambient second curl jet is
\[
B_C^{amb}(u,v)f:=[D_u,E_v]f-E_{D_uv}f,
\]
with exact local formula
\[
\boxed{
B_C^{amb}(u,v)f
=\sum_j((\nabla u)^T\nabla v_j)\times\partial_jf
+\sum_j\nabla v_j\times((\partial_ju)\cdot\nabla f).
}
\]
For \(u=v\), its frozen principal symbol is
\[
\boxed{
\sigma_{pr}(B_C^{amb}(u,u))(x,\xi)
=2i((A^T)^2\xi)\times.
}
\]
More generally, the frozen affine longitudinal covariant curl-jet tower has principal symbols
\[
\boxed{
e^{(n)}(x,\xi)=(-1)^nn!\,i((A^T)^n\xi)\times.
}
\]
Therefore
\[
\boxed{\Pi_{-h}(n)e^{(n)}\Pi_h(n)=0}
\]
for every finite local principal jet in this tower.
**INTERPRETATION.** No finite local ambient mother jet opens a principal helicity highway. Opposite-helicity creation appears through finite support displacement, subprincipal structure, Hodge covariantization or lower-jet products.
## 12. Order-two spectral normal form: one second mother or two first mothers — EXACT / OPEN
Let \(\mathcal E_a=[\mathcal D_a,C]\) and define the tensorial curl Hessian
\[
B_C(a,b):=[\mathcal D_a,\mathcal E_b]-\mathcal E_{\mathcal D_ab}.
\]
For \(F=f(C)\), define \(A_f(a)=[\mathcal D_a,F]\) and \(B_f(a,b)=[\mathcal D_a,A_f(b)]-A_f(\mathcal D_ab)\). After finite nonzero spectral localization, the exact second chain rule is
\[
\boxed{B_f(a,b)=Df_C[B_C(a,b)]+D^2f_C[\mathcal E_a,\mathcal E_b].}
\]
On spectral slots \(x\to y\to z\), with Hermite divided-difference values on repeated slots,
\[
\boxed{
(B_f)_{xz}=f^{[1]}(x,z)(B_C)_{xz}
+\sum_y f^{[2]}(x,y,z)
\big(\mathcal E_{a,xy}\mathcal E_{b,yz}+\mathcal E_{b,xy}\mathcal E_{a,yz}\big).}
\]
Thus every intrinsic second spectral costume has exactly two parent types: one second mother, or a product of two intrinsic first mothers. The raw ambient formula is identical after replacing \(\mathcal D,\mathcal E\) by \(D,E\). For \(f(x)=x^2\),
\[
\boxed{B_{C^2}(a,b)=\{C,B_C(a,b)\}+\mathcal E_a\mathcal E_b+\mathcal E_b\mathcal E_a,}
\]
so the Gauss/carré-du-champ square is the universal \(D^2f\) part of square-anchor differentiation.
Write \(K_C=(B_C(a,b)+B_C(b,a))/2\). Since \(D^2f_C\) is symmetric and the Ricci identity gives \(B_C(a,b)-B_C(b,a)=[R(a,b),C]\), functional calculus yields the universal split
\[
\boxed{\operatorname{Sym}B_f=Df_C[K_C]+D^2f_C[\mathcal E_a,\mathcal E_b],\qquad
\operatorname{Alt}B_f=\frac12[R(a,b),f(C)].}
\]
Equivalently, the order-zero through order-two spectral normalizer is
\[
\boxed{\mathfrak N_0(f)=f(C),\quad
\mathfrak N_1(f;a)=Df_C[\mathcal E_a],}
\]
\[
\boxed{\mathfrak N_{2,sym}(f;a,b)=Df_C[K_C(a,b)]+D^2f_C[\mathcal E_a,\mathcal E_b],\quad
\mathfrak N_{2,alt}(f;a,b)=\frac12[R(a,b),f(C)].}
\]
Thus antisymmetric second spectral geometry is inherited curvature; the only symmetric second-mother information is \(K_C\), plus the universal first-jet square. The known \(H\)-Codazzi and \(\Lambda\)-Hessian formulas are renderings of this normal form. Positive Sylvester inversion, e.g. \(\mathcal S_\Lambda^{-1}=(|C_L|+|C_R|)^{-1}\), is a two-slot renderer on nonzero blocks.
**CANDIDATE PRINCIPLE.** At higher order, spectral complexity should grow by slot arity and partitions of tensorial mother jets, not by primitive species. Multiple-operator-integral/domain closure remains **OPEN** at critical unbounded regularity.
## 13. The quadratic hard crossing is a compiled mother/Sylvester contraction — EXACT
Define the helicity torsion costume
\[
T_H(a,b)
:=B(Ha,Hb)-HB(Ha,b)-HB(a,Hb)+B(a,b),
\]
and the polarized hard crossing
\[
\boxed{\mathscr J(a,b):=\frac14T_H(a,b).}
\]
Helicity resolution gives
\[
\boxed{
\mathscr J(a,b)=\sum_{h=\pm1}P_{-h}B(a_h,b_h).
}
\]
In particular
\[
\boxed{J_{\rm flip}=\mathscr J(u,u).}
\]
Equivalently, since \(B(v,v)=-P\operatorname{div}(v\otimes v)\),
\[
\boxed{J_{\rm flip}=-\sum_hP_{-h}P\operatorname{div}(u_h\otimes u_h).}
\]
Thus hard crossing is the opposite-helicity filter of the same mixed spin-one stress sector that generates the Euler field.
The same object is a material commutator costume:
\[
\boxed{
\mathscr J(a,b)
=-\frac14\sum_hhP_{-h}
\Big([D_{a_h},H]b_h+[D_{b_h},H]a_h\Big).
}
\]
For
\[
E_{a,h}^{\times}:=P_{-h}E_aP_h,
\]
the opposite-helicity Sylvester law gives
\[
\boxed{
P_{-h}[D_a,H]P_h
=2\mathcal S_\Lambda^{-1}(E_{a,h}^{\times}).
}
\]
Therefore
\[
\boxed{
\mathscr J(a,b)
=-\frac12\sum_hh\Big[
\mathcal S_\Lambda^{-1}(E_{a_h,h}^{\times})b_h
+\mathcal S_\Lambda^{-1}(E_{b_h,h}^{\times})a_h
\Big].
}
\]
Hard crossing is thus a contraction of first mother jets through a positive spectral renderer.
Critical work is
\[
\boxed{W_\Lambda=4\langle\Lambda u,J_{\rm flip}\rangle.}
\]
The familiar same-helicity hard numerator
\[
|P-M|PM\sin\delta(1-\cos\delta)
\]
therefore decomposes into three generated gates:
\[
\boxed{
\text{radial antisymmetry}\times
\text{incompressible area}\times
\text{opposite-phase overlap}.
}
\]
It is not a fourth source mechanism.
## 14. Regeneration closes under the same genetic compiler — EXACT
Because \(J(u)=\mathscr J(u,u)\) is quadratic and the genetic Euler field is \(N=P[X_u,C]u\), the native heat law is
\[
\boxed{(\partial_t+\nu\Lambda^2)J_{\rm flip}=S_J,}
\]
with
\[
\boxed{
S_J=2\mathscr J(u,N)-2\nu\sum_j\mathscr J(\partial_ju,\partial_ju).
}
\]
After localized Sylvester resolution,
\[
\boxed{
\begin{aligned}
S_J=-\sum_hh\Big[&
\mathcal S_\Lambda^{-1}(E_{u_h,h}^{\times})N_h
+\mathcal S_\Lambda^{-1}(E_{N_h,h}^{\times})u_h\\
&-2\nu\sum_j\mathcal S_\Lambda^{-1}(E_{\partial_ju_h,h}^{\times})\partial_ju_h
\Big].
\end{aligned}
}
\]
The first line is the same crossing map polarized along the actual NS direction; the second is the heat carré-du-champ forced by the square anchor. Regeneration therefore introduces no new dynamic species.
Set
\[
z:=\Lambda^{-1}J,
\qquad
f:=\Lambda^{-1}S_J.
\]
Then
\[
\boxed{z_t+\nu\Lambda^2z=f.}
\]
When \(z\ne0\), write
\[
z=\rho e,
\qquad \rho=\|z\|_2,
\qquad \|e\|_2=1,
\]
and let
\[
P_e^\perp:=I-|e\rangle\langle e|.
\]
The source has the exact orthogonal split
\[
\boxed{
f=(\rho'+\nu\rho\|\Lambda e\|_2^2)e
+\rho(e_t+\nu P_e^\perp\Lambda^2e),
}
\]
so
\[
\boxed{
\|\Lambda^{-1}S_J\|_2^2
=(\rho'+\nu\rho\|\Lambda e\|_2^2)^2
+\rho^2\|e_t+\nu P_e^\perp\Lambda^2e\|_2^2.
}
\]
This is a legitimate Hilbert-space Pythagoras for one derived source. It is not a Fourier near/far vector Pythagoras.
**INTERPRETATION.** Dynamic maintenance of a compiled crossing can occur through amplitude repair or state-direction relocation. Repair need not occur at the same Fourier child.
## 15. Variational prolongation is a marked-slot compiler algorithm — EXACT
Let \(F(u)\) be a finite NEO expression. Its Fréchet derivative \(DF[u]v\) is obtained algebraically by marking one occurrence of \(u\) at a time, replacing it by \(v\), and summing. Higher derivatives mark multiple state leaves. This is an expression-tree algorithm, not a new physical primitive.
For the quadratic crossing map,
\[
K_u:=DJ[u],
\qquad
\boxed{K_uu=2J.}
\]
The coherence functional
\[
\Phi(u)=\frac12\|J(u)\|_2^2
\]
has gradient
\[
\boxed{\nabla\Phi(u)=K_u^*J.}
\]
Euler homogeneity gives
\[
\boxed{\langle u,K_u^*J\rangle=2\|J\|_2^2.}
\]
Similarly, the critical variational identity has the form
\[
\boxed{R_\Lambda=2\Lambda J+2K_u^*\Lambda u.}
\]
Adjoints remain in the same formal language because
\[
P^*=P,
\qquad C^*=C,
\qquad X_a^*=-X_a,
\qquad M_\phi^*=M_{\bar\phi},
\qquad (AB)^*=B^*A^*.
\]
**DEDUCTION.** Variational and adjoint fields such as \(DJ[u]^*J\) are compiled renderings. They must not be promoted to incidence, coherence or response primitives merely because their tensor type is new.
## 16. Universal parabolic coproduct and formal dynamic closure — EXACT / OPEN
Use the componentwise heat-covariant operator \(\mathscr H_\nu:=\partial_t+\nu(-\Delta)\); on the physical vector state \((-\Delta)u=C^2u\), so the genetic equation is
\[
\boxed{\mathscr H_\nu u=N=P[X_u,C]u.}
\]
Let \(\mathcal M\) be any fixed translation-invariant \(d\)-linear renderer. Fourier polarization of
\(|\sum_a k_a|^2-\sum_a|k_a|^2=2\sum_{a<b}k_a\cdot k_b\) gives the universal compiler law
\[
\boxed{\begin{aligned}
\mathscr H_\nu\mathcal M(F_1,\ldots,F_d)
={}&\sum_a\mathcal M(\ldots,\mathscr H_\nu F_a,\ldots)\\
&-2\nu\sum_{a<b}\sum_j
\mathcal M(\ldots,\partial_jF_a,\ldots,\partial_jF_b,\ldots).
\end{aligned}}
\]
For \(d=1\) fixed Fourier readers commute with heat; for \(d=2\) the second line is exactly the heat carré-du-champ. This one rule generates stress-rate, pressure-source-rate and the \(S_J\) law rather than treating them as separate dynamics.
For example, if \(g=-\Delta p=\partial_i u_j\partial_j u_i\) and \(H_0=(I/3+\mathcal R\otimes\mathcal R)g\), then
\[
\boxed{\mathscr H_\nu g=2\partial_iN_j\partial_j u_i
-2\nu\partial_m\partial_i u_j\partial_m\partial_j u_i,\qquad
\mathscr H_\nu H_0=(I/3+\mathcal R\otimes\mathcal R)\mathscr H_\nu g.}
\]
Thus pressure-tidal evolution is compiled from \(u,N\), the tensor envelope and the square anchor without taking pressure geometry as an input.
**DEDUCTION.** Physical time and spectral-jet order are different compiler axes. Covariant differentiation of \(f(C)\) raises divided-difference arity; the parabolic coproduct of a fixed multilinear renderer preserves that renderer and only replaces state leaves by their evolved leaves or joins two leaves by a heat-gradient edge. This is why regeneration of a compiled crossing need not introduce a higher mother jet.
Let \(\mathfrak A_C\) be the finite expression algebra generated by \(u,P,C,C^2\), Euclidean contractions, curl commutators and admissible fixed spectral/tensor renderers. The coproduct plus \(\mathscr H_\nu u=N\in\mathfrak A_C\) gives
\[
\boxed{\mathscr H_\nu\mathfrak A_C\subseteq\mathfrak A_C}
\]
for every finite multilinear compiled expression, and ordinary time jets follow by subtracting the compiled heat term.
For a local homogeneous monomial let \(d\) be state degree and \(s\) spatial/curl order. Euler insertion sends \((d,s)\mapsto(d+1,s+1)\), heat insertion sends \((d,s)\mapsto(d,s+2)\); both raise \(w=d+s\) by two. Hence after \(n\) time derivatives, \(d'+s'=d+s+2n\), reproducing \(u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t)\).
**DEDUCTION.** The parabolic coproduct is a dynamic normalizer and native type checker, not a new source. **OPEN.** Finite formal closure gives no convergence or infinite-jet analytic control.
## 17. Codazzi and the cubic near-phase null are H-normalizer outputs — EXACT / DEDUCTION
All Sylvester inversions below use the nonzero localization of Section 12. Specialize the universal normalizer to \(f=H\). With
\[
A_a=[\mathcal D_a,H]=D(\operatorname{sgn})_C[\mathcal E_a],\qquad
C_H(a,b):=\operatorname{Sym}B_H(a,b)+\frac12H\{A_a,A_b\},
\]
Codazzi is the symmetric off-diagonal remainder after the universal Gauss square; the antisymmetric remainder is already \(\frac12[R(a,b),H]\). The \(H\)-normal form implies
\[
\boxed{\{\Lambda,C_H(a,b)\}=2K_C(a,b)^\perp
-\{H\mathcal E_a^\parallel,A_b\}-\{H\mathcal E_b^\parallel,A_a\}.}
\]
Since \(A_a=2\mathcal S_\Lambda^{-1}(\mathcal E_a^\perp)\), this is an explicit second-mother/first-mother/Sylvester renderer. In the repeated slot \(a=b=u\),
\[
\boxed{C_H=2\mathcal S_\Lambda^{-1}(K_C^\perp)
-4\mathcal S_\Lambda^{-1}\{H\mathcal E^\parallel,
\mathcal S_\Lambda^{-1}(\mathcal E^\perp)\}.}
\]
Thus Codazzi is not an independent second-order geometry in NEO; it is the \(H\)-specific normal form of Section 12.
The ambient helicity Hessian also has the exact double-increment representation
\[
B_H^{amb}(u,v)f(x)
=PV\int\nabla^2K_H(x-y):
(\delta u\otimes\delta v)f(y)\,dy.
\]
If the two coefficient increments carry frequencies \(q,p\) and the carrier frequency is \(\ell\), then same-to-opposite helicity projection vanishes when \(q=0\), \(p=0\), or \(q+p=0\). In a deep near regime,
\[
\boxed{
\|\Pi_{-h}(k)B_H^{amb}(u,u)\Pi_h(\ell)\|
\lesssim
\frac{|q||p||q+p|}{|\ell|}.
}
\]
This is a cubic phase null: two transport increments plus one opposite-helicity output-direction increment.
**CANDIDATE PRINCIPLE.** Higher tensorial spectral jets may carry an increment count dictated by their compiler arity and the same principal phase blindness. This remains open beyond the established levels.
## 18. Near/far is a renderer split, not ontology — EXACT
Exactness here is after the stated ordered spectral localization; no unordered-triad orthogonality is implied.
For
\[
T_h^u:=\Pi_{-h}[D_u,H]\Pi_h,
\]
the cross block satisfies
\[
\boxed{T_h=2\mathcal S_\Lambda^{-1}(E_h).}
\]
The midpoint support factorization yields the exact mother bound
\[
\boxed{
\|E_h(k,\ell)\|
\le\frac{|\ell|}{|k|+|\ell|}|q|^2|\widehat u(q)|
\le |q|^2|\widehat u(q)|.
}
\]
After ordered spectral localization this can be written exactly as
\[
\boxed{T_{near}=\Lambda^{-1}B_{near}(\nabla^2u,\cdot),}
\]
\[
\boxed{T_{far}=C_{far}(\Lambda u,\cdot).}
\]
No third residual channel appears.
**INTERPRETATION.** Near-diagonal opposite-helicity motion is a geometric smoothing consequence of forbidden principal phase transfer; far displacement loses that local smoothing but exposes a square-anchor scale. Near/far is a renderer choice inside one mother channel, not two mechanisms.
**Protocol.** This ordered split must not be confused with unordered triad genealogy, and its two vector outputs need not be orthogonal after summation.
## 19. Reconstruction crucible on genuine NS time jets — AUDIT
A team compiler must survive states that are not Beltrami, not one-helicity and not closed toy triads. The current crucible used periodic finite-Fourier initial data with multiple radii, both helicities and complex phases; convolution outputs were **not truncated** when computing \(N,u_t,u_{tt},u_{ttt}\), so these are genuine NS jets at \(t=0\).
The following independent reconstructions agreed to machine precision:
1. \(-P(D_uu)=P(u\times Cu)=P[X_u,C]u\).
2. The raw Lamb Hodge split into \(N\) and \(\nabla(p+|u|^2/2)\), including the pressure Poisson equation.
3. Direct material transport versus the curl macro of Section 6, and \(E_uu\) versus vortex stretching.
4. The dynamic costume equation for \(C,H,\Lambda,C^2,|C-1.3|\) and \(e^{-0.07C^2}+0.15C\), including nonzero \(f(0)\nabla p\) terms.
5. \(J_{flip}=\frac14T_H(u,u)\) and \(W_\Lambda=4\langle\Lambda u,J_{flip}\rangle\) on an active heterochiral state with nonzero critical work.
6. \(S_J\) versus the polarized/carré-du-champ chain rule and the exact \(H^{-1}\) dynamic polar split.
7. Classical versus genetic \(u_{tt}\) and \(u_{ttt}\); a representative support growth was \(10\to46\to198\to584\).
8. A pure-helicity boundary state gave \(W_\Lambda=0\) and \(\dot W_\Lambda=4\|\Lambda^{1/2}J_{flip}\|_2^2\).
9. Scalar commutator depth terminated at one level for \(C\) and two for \(C^2\).
10. Exact NS dilation gave \(u,u_t,u_{tt},u_{ttt}\sim\lambda^1,\lambda^3,\lambda^5,\lambda^7\).
11. The order-two normal form passed polynomial matrix audits through degree six and mixed-sign \(H,\Lambda\) second-anchor audits at residuals below \(8\times10^{-15}\), using Hermite values on repeated slots.
12. The universal parabolic coproduct matched full-convolution NS stress, pressure source and pressure Hessian below \(10^{-16}\), and a genuinely nonlocal trilinear renderer at \(2.1\times10^{-16}\).
13. Genetic reconstruction of vorticity, gradient/strain Riccati, \(\operatorname{sym}\nabla N\) and \(g=\operatorname{tr}A^2=|S|^2-|\omega|^2/2\) agreed below \(2.2\times10^{-16}\).
**AUDIT.** These tests validate signs, factors, typing and implementation logic only. They do not prove analytic completeness or regularity.
## 20. NEO compiler protocol for the team — DEDUCTION
For every proposed NS object, use this order.
1. **Type it:** carrier type, state degree, differential order, spectral arity and—when tensorial—the stabilizer spin sector.
2. **Return to** \(u,P,C,C^2,t\); never start from pressure, stress, torsion, Codazzi, incidence or coherence.
3. **Try local curl generation:** replace gradients and finite local derivatives by matrix entries or multiplication commutators of \(C\).
4. **Try isotropic generation:** normalize physical readers to \(f(C)\), tensor readers to the \(\delta,\varepsilon,\mathcal R\) envelope, and higher spectral jets to the order-two divided-difference normalizer before inventing a tensor mechanism.
5. **Compile transport:** use Section 6 rather than importing \(D_u\) when parentage matters.
6. **Use the mother normal form:** route first spectral motion through \(E=[D_u,C]\), then render \(K,A,L\).
7. **Use the square before inequalities:** expose \(C^2\) or positive Sylvester structure before estimating.
8. **Differentiate by compiler law:** use the parabolic coproduct for time evolution and marked-slot differentiation for variational evolution; neither creates a source species.
9. **Audit the type weight** \((d,s)\) and \(w=d+s\).
10. **Separate labels:** exact identity, principal symbol, numerical audit and global estimate are different claims.
11. **Attack seams:** zero-curl/zero-frequency, Beltrami, pure helicity, collinear/radial, near transverse, antipodal/far, harmonic sectors and vector interference.
12. **Stop ontology growth:** once exact parentage is found, record its normal form and demote the name to a costume.
## 21. Core NEO architecture after reconstruction — DEDUCTION / CANDIDATE PRINCIPLE
The current instruction set is
\[
\boxed{\begin{array}{ll}
\text{typed state:}&u(t),P,C,C^2,\\
\text{local algebra:}&M_\phi,X_a,\cdot,\times,\otimes,\text{ contractions},\\
\text{local differential:}&\operatorname{ad}_C=[C,\cdot],\\
\text{nonlocal reader:}&f(C),\ \operatorname{Contr}(\delta,\varepsilon,\mathcal R),\text{ divided differences},\\
\text{composition:}&\text{operator products, projections, contractions},\\
\text{physical evolution:}&u_t=P[X_u,C]u-\nu C^2u.
\end{array}}
\]
Transport and mother jets are macros; order-two spectral normalization, the parabolic coproduct and marked-slot variation are compiler algorithms built from this smaller language.
**CANDIDATE PRINCIPLE.** NEO Genetic Closure: Every finite local NS differential costume, every canonical isotropic linear physical reader, and every finite formal time/variational descendant discovered so far is generated by curl matrix structure, curl spectral calculus, state-dependent multiplication commutators, the typed Hodge interface and the curl square.
Equivalently,
\[
\boxed{\text{geometry}=C\text{-matrix},\qquad\text{spectral wardrobe}=f(C),\qquad
\text{nonlinearity}=\operatorname{ad}_C\text{ against the state},\qquad\text{dissipation}=C^2.}
\]
Pressure, stretching, torsion, stress, Ricci/Codazzi, hard crossing, regeneration, coherence and incidence remain important costumes; exact parentage means their diversity is generated rather than primitive.
**DEDUCTION — order-two closure checkpoint.** On nonzero spectral localizations, within the translation-invariant isotropic finite-rank class, no additional linear/tensor or first/second spectral species is needed: one-frequency tensors reduce to the \(\delta,\varepsilon,\mathcal R\) envelope; spectral jets reduce to \(\mathfrak N_0,\mathfrak N_1,\mathfrak N_{2,sym},\mathfrak N_{2,alt}\); physical time reduces by the parabolic coproduct. The remaining frontier is analytic, anisotropic/variable-coefficient, harmonic/boundary, or normal-form uniqueness.
**DEDUCTION — canonical parentage, not yet canonical syntax.** The anchor reader \(f(x)=x\) isolates the first/second curl mothers and curvature in the spectral normalizer, while the spin projectors isolate tensor sectors. Parentage is therefore canonical at order two; uniqueness of whole expression strings modulo anchor identities, incompressibility, Euclidean vector identities and integration by parts remains open.
## 22. What remains open — OPEN
The reconstruction programme is not a regularity theorem. The structural frontier is:
- analytic local/nonlocal closure in the unbounded critical spaces, including the zero-curl seam;
- analytic mapping bounds for the isotropic tensor envelope, plus genuinely anisotropic or variable-coefficient tensor readers;
- multiple-operator-integral closure for higher divided differences and NEO jets;
- correct boundary/harmonic typing away from finite-energy \(\mathbb R^3\);
- canonical whole-expression syntax modulo anchor/Hodge identities, incompressibility, Euclidean rewrites and integration by parts;
- analytic control of the infinite dynamic tower. Formal finite-jet closure gives no convergence theorem;
- global regularity, which is **not** proved by any reconstruction identity or audit here.
The core research question is
\[
\boxed{\text{How far can genuine NS be normalized inside this curl-genetic language before any new primitive is logically unavoidable?}}
\]
