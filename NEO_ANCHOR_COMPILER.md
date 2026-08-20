# NEO Core Compiler
Companion synthesis: [NS Polar Compatibility Architecture](NS_POLAR_COMPATIBILITY_ARCHITECTURE.md).
This file is the canonical NEO manual for the Wang--Navier--Stokes programme. Its purpose is not to add a second geometry to Navier--Stokes. Its purpose is to reconstruct the genuine 3D incompressible Navier--Stokes equation, its standard geometric faces, and its finite derived jets from the smallest fixed structural language presently known.
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
## 4. Canonical isotropic nonlocal readers are functions of curl — EXACT
Let \(T\) be a translation-invariant linear operator on divergence-free vector fields and assume rotational covariance
\[
T(Rk)=RT(k)R^{-1}
\]
for all \(R\in SO(3)\). Fix \(k\ne0\). The stabilizer of \(k\) acts as \(SO(2)\) on the physical plane \(k^\perp\). Its commutant is generated by the identity on that plane and the quarter-turn \(i\widehat k\times\). Therefore
\[
\boxed{T(k)=a(|k|)P(k)+b(|k|)H(k).}
\]
On the two helicity lines the eigenvalues are \(a(r)\pm b(r)\). Define
\[
f(+r)=a(r)+b(r),
\qquad
f(-r)=a(r)-b(r).
\]
Then
\[
\boxed{T=f(C)\quad\text{on }\operatorname{Ran}P.}
\]
This includes
\[
H,\quad \Lambda^s,\quad \Pi_\pm,\quad C^\dagger=H\Lambda^{-1},\quad e^{-t\Lambda^2},
\]
whenever the corresponding domains are meaningful.
**DEDUCTION.** A fixed isotropic translation-invariant reader cannot by itself flip helicity because
\[
[f(C),H]=0.
\]
Intrinsic helicity metamorphosis must therefore come from state-dependent multiplication/transport noncommutation, not from the fixed reader.
**OPEN.** This is a completeness theorem for the stated physical-block symmetry class, not for arbitrary tensor-valued, anisotropic, boundary-dependent or variable-coefficient nonlocal operators.
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
## 12. Higher spectral jets increase arity, not ontology — EXACT / OPEN
Repeated transport differentiation is a derivation:
\[
\delta_u^n(XY)=\sum_{k=0}^n\binom nk\delta_u^kX\,\delta_u^{n-k}Y.
\]
Differentiating the anchor algebra twice gives
\[
\boxed{P\delta^2P+(\delta^2P)P-\delta^2P=-2(\delta P)^2,}
\]
\[
\boxed{H\delta^2H+(\delta^2H)H=\delta^2P-2(\delta H)^2,}
\]
\[
\boxed{
\delta^2C=(\delta^2H)\Lambda+2(\delta H)(\delta\Lambda)+H\delta^2\Lambda,
}
\]
\[
\boxed{
\{C,\delta^2C\}+2(\delta C)^2
=\{\Lambda,\delta^2\Lambda\}+2(\delta\Lambda)^2.
}
\]
For functional calculus, first derivatives use a two-slot divided difference
\[
f^{[1]}(C_0,C_1),
\]
second derivatives use three-slot functions
\[
f^{[2]}(C_0,C_1,C_2),
\]
and higher derivatives continue similarly. Positive Sylvester resolution is simply a two-slot spectral renderer, for example
\[
\boxed{
\mathcal S_\Lambda^{-1}=(|C_L|+|C_R|)^{-1}
}
\]
on nonzero localized blocks.
**CANDIDATE PRINCIPLE.** Higher nonlocal NEO calculus grows by spectral arity and lower-jet partitions, not by new primitive species. A full analytic theorem requires multiple-operator-integral/domain control at the relevant unbounded critical regularities.
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
## 16. Formal dynamic closure: finite time jets cannot create a primitive — EXACT
Let \(\mathfrak A_C\) be the finite expression algebra generated by
\[
u,\ P,\ C,\ C^2,\]
fixed Euclidean multiplications/contractions, local curl commutators, admissible spectral/multi-slot curl renderers, composition and projection.
The actual NS vector field is
\[
\boxed{
\mathcal X_\nu(u):=P[X_u,C]u-\nu C^2u\in\mathfrak A_C.
}
\]
Define the NS derivation
\[
\boxed{\mathscr D_\nu F:=DF[u]\mathcal X_\nu(u).}
\]
Because the only time-dependent generator is \(u\), and because \(\mathcal X_\nu(u)\in\mathfrak A_C\), Leibniz and chain rules imply
\[
\boxed{\mathscr D_\nu\mathfrak A_C\subseteq\mathfrak A_C.}
\]
Hence every finite formal NS time jet of a compiled expression remains in the same language.
For local homogeneous monomials, assign
\[
d:=\text{number of state leaves},
\qquad
s:=\text{total spatial/curl order}.
\]
Euler insertion has type
\[
\boxed{(d,s)\mapsto(d+1,s+1),}
\]
while heat insertion has type
\[
\boxed{(d,s)\mapsto(d,s+2).}
\]
Both increase
\[
\boxed{w:=d+s}
\]
by exactly two. This reproduces the physical NS scaling
\[
u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t).
\]
After \(n\) time differentiations, descendants of a local term of type \((d,s)\) lie on
\[
\boxed{d'+s'=d+s+2n.}
\]
**DEDUCTION.** The compiler carries a native type checker: one extra state factor plus one curl has the same scaling weight as two curls. This is an exact grammar property, not a degree-of-freedom count.
**OPEN.** Formal finite-jet closure does not imply convergence or analytic control of the infinite time-jet tower.
## 17. Second-jet normal form and the cubic near-phase null — EXACT / DEDUCTION
All Sylvester inversions below are understood on the same nonzero spectral localization used throughout the compiler.
The intrinsic second helicity/Codazzi costume is not a new mother species. Let \(\mathcal E_u=[\mathcal D_u,C]\), and split
\[
\mathcal E^\parallel=\frac12(\mathcal E+H\mathcal EH),
\qquad
\mathcal E^\perp=\frac12(\mathcal E-H\mathcal EH).
\]
Let \(B_C^\perp\) denote the off-diagonal part of the second curl Hessian. Then
\[
\boxed{
\{\Lambda,C_H\}
=2B_C^\perp-2\{H\mathcal E^\parallel,A_u\}.
}
\]
Since
\[
A_u=2\mathcal S_\Lambda^{-1}(\mathcal E_u^\perp),
\]
we obtain
\[
\boxed{
C_H
=2\mathcal S_\Lambda^{-1}(B_C^\perp)
-4\mathcal S_\Lambda^{-1}
\{H\mathcal E^\parallel,
\mathcal S_\Lambda^{-1}(\mathcal E^\perp)\}.
}
\]
Thus Codazzi is a second-mother/Sylvester costume.
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
**AUDIT.** These tests validate signs, factors, typing and implementation logic only. They do not prove analytic completeness or regularity.
## 20. NEO compiler protocol for the team — DEDUCTION
For every proposed NS object, use this order.
1. **Type it:** scalar, ambient/physical vector, operator, multilinear kernel, tensor, functional or time jet.
2. **Return to** \(u,P,C,C^2,t\); never start from pressure, stress, torsion, Codazzi, incidence or coherence.
3. **Try local curl generation:** replace gradients and finite local derivatives by matrix entries or multiplication commutators of \(C\).
4. **Try spectral generation:** normalize fixed isotropic physical readers to \(f(C)\); use multi-slot divided differences for higher spectral derivatives.
5. **Compile transport:** use Section 6 rather than importing \(D_u\) when parentage matters.
6. **Use the mother normal form:** route first spectral motion through \(E=[D_u,C]\), then render \(K,A,L\).
7. **Use the square before inequalities:** expose \(C^2\) or positive Sylvester structure before estimating.
8. **Differentiate the expression tree:** time/variational derivatives are compiler algorithms, not new sources.
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
\text{spectral reader:}&f(C)\text{ and multi-slot divided differences},\\
\text{composition:}&\text{operator products, projections, contractions},\\
\text{physical evolution:}&u_t=P[X_u,C]u-\nu C^2u.
\end{array}}
\]
Transport, mother jets, parabolic prolongation and variational prolongation are macros or expression-tree algorithms built from this smaller language.
**CANDIDATE PRINCIPLE.** NEO Genetic Closure: Every finite local NS differential costume, every canonical isotropic linear physical reader, and every finite formal time/variational descendant discovered so far is generated by curl matrix structure, curl spectral calculus, state-dependent multiplication commutators, the typed Hodge interface and the curl square.
Equivalently,
\[
\boxed{\text{geometry}=C\text{-matrix},\qquad\text{spectral wardrobe}=f(C),\qquad
\text{nonlinearity}=\operatorname{ad}_C\text{ against the state},\qquad\text{dissipation}=C^2.}
\]
Pressure, stretching, torsion, stress, Ricci/Codazzi, hard crossing, regeneration, coherence and incidence remain important costumes; exact parentage means their diversity is generated rather than primitive.
## 22. What remains open — OPEN
The reconstruction programme is not a regularity theorem. The structural frontier is:
- analytic local/nonlocal closure in the unbounded critical spaces, including the zero-curl seam;
- tensor-valued nonlocal completeness beyond the scalar/vector isotropic classification;
- multiple-operator-integral closure for higher divided differences and NEO jets;
- correct boundary/harmonic typing away from finite-energy \(\mathbb R^3\);
- useful normal-form uniqueness modulo anchor identities, Hodge equivalence and integration by parts;
- analytic control of the infinite dynamic tower. Formal finite-jet closure gives no convergence theorem;
- global regularity, which is **not** proved by any reconstruction identity or audit here.
The core research question is
\[
\boxed{\text{How far can genuine NS be normalized inside this curl-genetic language before any new primitive is logically unavoidable?}}
\]
