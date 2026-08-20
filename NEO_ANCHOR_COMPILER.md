# NEO Anchor Compiler

Companion synthesis: [NS Polar Compatibility Architecture](NS_POLAR_COMPATIBILITY_ARCHITECTURE.md).

This document is the dedicated NEO research surface for the Wang--Navier--Stokes programme. It is not a second ontology and it does not introduce a new physical source. Its purpose is to force every proposed mechanism, tensor, observer, gauge or rate back through the smallest fixed anchor set before it is allowed to enter the architecture.

The immutable inputs are
\[
\boxed{u(t),\qquad P,\qquad C=\operatorname{curl},\qquad C^2=(-\Delta)P,\qquad t.}
\]
On the divergence-free state space, \(Pu=u\) and \(C^2=-\Delta\). Fixed Euclidean bilinear operations already present in the Navier--Stokes equation are allowed; pressure, helicity torsion, Codazzi, stress, Jordan measures and other derived faces are outputs, not inputs.

The standing labels are **EXACT**, **DEDUCTION**, **INTERPRETATION**, **CANDIDATE PRINCIPLE**, **AUDIT**, and **OPEN**. A finite Fourier or matrix computation may audit algebra but never upgrades an analytic claim. Zero curl spectrum, unbounded functional calculus and critical norms require localization/domain care whenever used.

The governing research rule is:
\[
\boxed{\text{generate from anchors first; render into a costume only afterwards.}}
\]
If a quantity is an exact projection, contraction, functional-calculus filter, gauge transform or covariant prolongation of the anchor algebra, it is a costume and must not be promoted to a new primitive.

---

## 1. Immutable anchors beneath the metamorphosis — EXACT / INTERPRETATION
The repeated ontology collapses suggest a stricter distinction between a derived face and an object that remains fixed while the face changes. The smallest presently visible set of physical anchors is
\[
\boxed{u(t),\qquad P,\qquad C=\operatorname{curl},\qquad C^2=-\Delta,\qquad t.}
\]
Here \(u\) is the actual divergence-free trajectory, \(P\) is the incompressibility/Hodge constraint, \(C\) is curl, \(C^2=-\Delta\) is the physical heat scale, and \(t\) is physical time. None is created by changing observer, gauge, multiplier, measure, or helicity frame.

The two canonical affine quadratic readings are
\[
\boxed{E=\langle u,u\rangle,\qquad \mathcal H=\langle u,Cu\rangle,}
\]
with exact nonlinear annihilation
\[
\boxed{\langle u,N\rangle=0,\qquad \langle Cu,N\rangle=0.}
\]
Equivalently, in signed-curl work coordinates,
\[
\boxed{\int dW=0,\qquad \int x\,dW=0.}
\]
Thus nonlinear multiplier visibility begins beyond the affine spectral skeleton \(1,C\). The hinge family \(|C-a|\) is a canonical second-difference coordinate of that quotient, not another primitive.

The polar objects are intrinsic but derived:
\[
\boxed{H=\operatorname{sgn}C,\qquad \Lambda=|C|,\qquad C=H\Lambda.}
\]
Pressure/Hodge curvature, helicity torsion, Codazzi, Jordan variation and the Poisson Gram tensor are likewise derived representations of compatibility failures among the anchors; changing tensor type does not create a new physical source.

The persistent relation underneath these changes is non-intertwining. For any admissible \(f(C)\), transport before or after applying \(f(C)\) differs by
\[
\boxed{[\nabla,f(C)]u.}
\]
Angular deformation \([\nabla,H]\), radial deformation \([\nabla,\Lambda]\), full curl deformation \([\nabla,C]\), Hodge leakage from failure of raw transport to remain in \(\operatorname{Ran}P\), and radial heat compatibility through \([\nabla,C^2]\) are typed readings of this same noncommutation principle.

**INTERPRETATION.** The anchors remain fixed; what metamorphoses is the incompatibility of transporting them simultaneously. Apparent disappearance from one reader must first be tested for migration into a complementary projection, gauge connection, higher jet, or scalar contraction.

A useful ontology stopping rule is
\[
\boxed{X\ \text{is not a new primitive if it is an exact projection, gauge transform, functional-calculus reading, contraction, or covariant prolongation of }(u,P,C,C^2,t).}
\]
The regularity frontier can therefore be stated without adding another species: can the actual finite-energy trajectory sustain nonintegrable critical visibility speed in finite physical time while these fixed anchors and all exact compatibility relations among them remain simultaneously satisfied?

---

## 2. NEO anchor algebra: one curl spectrum, three structural readings — EXACT
Work first on the ambient vector-field Hilbert space and let \(P\) be the Helmholtz projector and \(C=\operatorname{curl}\). Away from the measure-zero Fourier seam \(k=0\),
\[
\boxed{P^2=P,\qquad PC=CP=C,\qquad C^2=(-\Delta)P.}
\]
Thus \(P\) is the support projection of curl. If \(H=\operatorname{sgn}C\) and \(\Lambda=|C|\) are extended by zero on \(\ker C\), then spectral calculus gives
\[
\boxed{H^2=P,\qquad C=H\Lambda=\Lambda H,\qquad \Lambda^2=C^2=(-\Delta)P.}
\]
On a nonzero Fourier fiber \(k\), the spectrum of \(C(k)=i\,k\times\) is
\[
\boxed{-|k|,\qquad0,\qquad+|k|.}
\]
The zero eigenspace is the longitudinal/Hodge-normal direction and the two nonzero eigenspaces are the two helicity directions. Hence Hodge support, helicity phase, radial modulus and physical heat are not independent static geometries: they are canonical readings of the same curl spectrum.

At scalar spectral value \(x\), the anchor algebra is
\[
p(x)=1_{x\ne0},\qquad h(x)=\operatorname{sgn}x,\qquad \lambda(x)=|x|,
\]
\[
\boxed{p^2=p,\qquad h^2=p,\qquad x=h\lambda,\qquad \lambda^2=x^2.}
\]
The non-affine seams of \(p,h,\lambda\) all occur at the curl spectral value \(x=0\). This is a zero-curl eigenvalue seam, not the same thing as zero Fourier frequency: the longitudinal zero-curl sector exists on every nonzero Fourier fiber.

**DEDUCTION.** The static NEO content can be generated from one curl operator and its support/square. The apparent multiplicity \(P,H,\Lambda,-\Delta\) is a spectral decomposition of that one anchor algebra, not a multiplicity of physical sources.

## 3. The NEO dynamic compiler is one derivation — EXACT
Let the raw material transport be \(D_u=u\cdot\nabla\) and define
\[
\boxed{\delta_uX:=[D_u,X].}
\]
It is an associative derivation:
\[
\boxed{\delta_u(XY)=(\delta_uX)Y+X(\delta_uY).}
\]
Introduce only shorthand outputs, not new primitives,
\[
K:=\delta_uP,\qquad A:=\delta_uH,\qquad L:=\delta_u\Lambda,\qquad E:=\delta_uC.
\]
Differentiating the anchor identities gives, without any extra mechanism,
\[
\boxed{PK+KP=K,}
\]
\[
\boxed{HA+AH=K,}
\]
\[
\boxed{E=A\Lambda+HL,}
\]
\[
\boxed{\Lambda L+L\Lambda=CE+EC.}
\]
From \(PK+KP=K\),
\[
\boxed{PKP=0,\qquad (I-P)K(I-P)=0,}
\]
so first support motion is forced to be tangent-normal off-diagonal. Acting on the actual state \(u=Pu\), the projected NS equation yields
\[
\boxed{Ku=(I-P)D_uu=-\nabla p.}
\]
Thus pressure is the state contraction of differentiated Hodge support; it is not an additional NEO input.

Likewise, \(HA+AH=K\) says before intrinsic Leray reduction that helicity-phase deformation and Hodge leakage are two readings of the differentiated identity \(H^2=P\). On the divergence-free block \(PKP=0\), this reduces to the familiar anti-commutation \(HA+AH=0\).

**INTERPRETATION.** The anchors remain fixed. The wardrobe is generated by failure of the self-generated transport to intertwine with their spectral calculus. Projection can move a defect between tangent and normal readings, but does not create another defect species.

## 4. The opposite-helicity channel is an exact Sylvester resonance — EXACT / DEDUCTION
On curl spectral values \(x,y\), the differentiated support/phase identity reads
\[
\boxed{(h(x)+h(y))A_{xy}=K_{xy}.}
\]
This gives a complete routing rule:

- on \(0\leftrightarrow+\), \(A=K\);
- on \(0\leftrightarrow-\), \(A=-K\);
- on \(+\leftrightarrow+\) and \(-\leftrightarrow-\), \(K=0\) forces \(A=0\);
- on \(+\leftrightarrow-\), \(h(x)+h(y)=0\) and \(K_{xy}=0\), so the equation reduces to \(0=0\).

Therefore
\[
\boxed{+\leftrightarrow-\ \text{is precisely the kernel of the Sylvester map }X\mapsto HX+XH.}
\]
This is a structural resonance of the differentiated anchor identity \(H^2=P\). Hodge/pressure support motion controls the \(0\leftrightarrow\pm\) edges but cannot directly determine the intrinsic opposite-helicity block.

The radial square identity behaves differently. On the same spectral pair,
\[
\boxed{(|x|+|y|)L_{xy}=(x+y)E_{xy}.}
\]
Except for the trivial \(x=y=0\) block,
\[
\boxed{L_{xy}=\frac{x+y}{|x|+|y|}E_{xy}.}
\]
The denominator is positive, so the radial leg is Sylvester-resolved rather than resonant.

For \(x=a>0\), \(y=-b<0\),
\[
A_{xy}=\frac{2}{a+b}E_{xy},\qquad L_{xy}=\frac{a-b}{a+b}E_{xy},
\]
and the scalar identity \((a+b)^2=(a-b)^2+4ab\) lifts to
\[
\boxed{|E_{xy}|^2=|L_{xy}|^2+ab\,|A_{xy}|^2.}
\]
This is the localized tangent polar Pythagoras. Its origin is the anchor algebra, not a separate positive wallet.

**DEDUCTION.** Radial deformation is positively resolved by the square \(C^2\), while the critical angular channel is a phase resonance left open by \(H^2=P\). The remaining anchor identities, full-curl Killing compatibility and the physical heat clock must therefore constrain that resonant block indirectly. This gives a precise algebraic reason pressure cannot be the direct first-order owner of the intrinsic critical endpoint.

## 5. One mother curl deformation wears every first-order spectral costume — EXACT after spectral localization
Let \(f\) be an admissible scalar function and work first on a finite curl-spectral localization. For distinct spectral values \(x,y\),
\[
\boxed{[D_u,f(C)]_{xy}=f^{[1]}(x,y)E_{xy},\qquad f^{[1]}(x,y):=\frac{f(y)-f(x)}{y-x}.}
\]
The diagonal value is the corresponding derivative when defined. In operator language this is the standard divided-difference/double-operator-integral derivative of functional calculus. Nonsmooth readers such as \(\operatorname{sgn}\) and \(|\cdot|\) require the same spectral-localization and zero-seam care already used elsewhere in the note.

Hence the first-order multiplier wardrobe is not a family of independent deformations:
\[
\boxed{\text{costume}_f=f^{[1]}(C_L,C_R)\,E.}
\]
Choosing \(f=x\), \(|x|\), \(\operatorname{sgn}x\), \(1_{x\ne0}\), or \(|x-a|\) gives respectively the full-curl, radial, angular, support/Hodge and shifted-hinge readings of the same mother deformation.

Euler work further quotients the wardrobe by the affine spectral skeleton. Since
\[
\langle u,N\rangle=0,\qquad \langle Cu,N\rangle=0,
\]
for \(W_f:=2\langle f(C)u,N\rangle\),
\[
\boxed{W_{f+\alpha+\beta x}=W_f.}
\]
Thus nonlinear spectral work sees \(f\) only modulo \(\operatorname{span}\{1,x\}\). Hinges are canonical second-difference coordinates of this quotient rather than new mechanisms.

The positive root \(\Lambda=|C|\) is singled out internally by the anchors: it is the unique nonnegative square root of \(C^2\). It is affine on each helicity half-line but globally non-affine across the sign seam. Critical \(\dot H^{1/2}\) visibility can therefore be read as the cost of transporting the positive square root of physical heat while the signed square root \(C\) simultaneously obeys Euler's helicity/Killing compatibility.

## 6. Higher wardrobes are Leibniz prolongations, not new ontology — EXACT algebraically / CANDIDATE analytically
Repeated application of the same derivation generates the jet tower. For any product,
\[
\boxed{\delta_u^n(XY)=\sum_{k=0}^n\binom nk(\delta_u^kX)(\delta_u^{n-k}Y)}
\]
when the repeated derivation is understood on a fixed algebraic trajectory. In particular, the second anchor prolongations are
\[
\boxed{P\,\delta_u^2P+(\delta_u^2P)P-\delta_u^2P=-2(\delta_uP)^2,}
\]
\[
\boxed{H\,\delta_u^2H+(\delta_u^2H)H=\delta_u^2P-2(\delta_uH)^2,}
\]
\[
\boxed{\delta_u^2C=(\delta_u^2H)\Lambda+2(\delta_uH)(\delta_u\Lambda)+H\delta_u^2\Lambda,}
\]
\[
\boxed{\{C,\delta_u^2C\}+2(\delta_uC)^2=\{\Lambda,\delta_u^2\Lambda\}+2(\delta_u\Lambda)^2.}
\]
Thus Gauss squares, Coriolis-type cross terms and quadratic polar corrections are forced chain-rule terms of differentiated anchor constraints. They must not be promoted to independent sources.

On finite spectral models, higher derivatives of \(f(C)\) organize by higher divided differences \(f^{[j]}\) and partitions of lower curl jets: a noncommutative Faà di Bruno structure. **CANDIDATE PRINCIPLE.** The full tensor/parabolic wardrobe may be the analytic realization of this finite anchor differential algebra, with Ricci/Bianchi, Curl-Killing and heat carré-du-champ supplying the geometric typing and compatibility needed to pass from formal operator jets to the PDE.

This candidate does not assert global operator differentiability for every nonsmooth \(f\), nor any regularity theorem. Zero frequency, unbounded operators and critical norms must continue to be localized and justified separately.

## 7. NEO laboratory protocol for the team — RESEARCH RULE
The NEO experiment should now be run before inventing any new object.

1. **Inputs are fixed:** \(u(t),P,C,C^2,t\), together with the fixed Euclidean bilinear operations already present in NS.
2. **Generate a reader only through the anchors:** functional calculus \(f(C)\), support/square identities, or the actual projected NS vector field
\[
\boxed{\partial_tu=P(u\times Cu)-\nu C^2u.}
\]
3. **Generate motion only through transport:** apply \(\delta_u=[D_u,\cdot]\) or its parabolic-covariant completion; do not insert pressure, torsion, Codazzi, stress or Jordan variables as independent inputs.
4. **Render only after generation:** project by \(P\) or \(I-P\), contract with \(u\), pair with another anchor reader, change gauge, or integrate in physical time.
5. **Audit the parentage:** if a proposed quantity is an exact projection, contraction, functional-calculus filter, gauge transform or covariant prolongation of an anchor relation, it is a costume, not a new primitive.
6. **Locate kernels before estimating:** the opposite-helicity kernel of \(X\mapsto HX+XH\) is the prototype. A loss of algebraic invertibility is more informative than naming the residual tensor.
7. **Use the square before inequalities:** radial quantities should first be resolved through \(C^2=(-\Delta)P\); only then ask for norms.
8. **Keep physical time and heat visible:** every successful static disguise must still be regenerated against the same \(\nu C^2\) clock.
9. **Finite models are audits only:** exact matrix/Fourier tests may verify algebra and expose kernels, but never replace the whole-space PDE identities.
10. **No theorem inflation:** keep EXACT, DEDUCTION, INTERPRETATION, CANDIDATE and OPEN labels separate.

**Working NEO thesis.** The apparently unbounded wardrobe of 3D NS may be generated by a very small fixed curl algebra acted on by one self-generated noncommuting transport and one physical heat clock. The difficult sector is not an extra source but a resonant compatibility channel where one differentiated anchor relation loses invertibility and the remaining anchor relations must close the gap. The first adversarial test below adds an important asymmetry: the phase relation can resonate, but the positive square anchor does not become blind to nonzero spectral scale.

## 8. NEO adversarial unit test: phase locking drives nonzero companions into square-anchor heat — EXACT ON THE AFFINE BRANCH / AUDIT
Use \(\Pi\) for the local Riccati rank-one projector, reserving \(P\) for the Helmholtz anchor. Restrict to the exact **phase-locked affine Riccati subbranch** of `NS_POLAR_COMPATIBILITY_ARCHITECTURE.md`, Section 70:
\[
\nabla u=A=\lambda(I-3\Pi),\qquad \Pi=n\otimes m,\quad m\cdot n=1,
\qquad \dot\lambda=\lambda^2,\quad D_t\Pi=0.
\]
A Fourier/material covector obeys \(\dot k=-A^Tk\). Writing \(k=\alpha m+r\), \(n\cdot r=0\), gives exactly
\[
\boxed{\dot\alpha=2\lambda\alpha,\qquad \dot r=-\lambda r.}
\]
For \(\lambda=(T-t)^{-1}\),
\[
\boxed{\alpha(t)=\alpha(s)\Big(\frac{T-s}{T-t}\Big)^2,\qquad r(t)=r(s)\frac{T-t}{T-s}.}
\]
Thus \(\alpha(s)\ne0\) gives projective line collapse \(\|r\|/|\alpha|=O((T-t)^3)\) and \(|k|\asymp(T-t)^{-2}\); \(\alpha(s)=0\) moves toward the IR instead of the UV.

The exact `NS_POLAR_COMPATIBILITY_ARCHITECTURE.md`, Section 71 family makes the heat consequence explicit. For
\[
u=(ax+F(t,z),ay,-2az),\quad a=(T-t)^{-1},\qquad F_t+aF-2azF_z=\nu F_{zz},
\]
Fourier transform in \(z\) gives
\[
\boxed{\partial_t\widehat F+2ak\partial_k\widehat F=-(3a+\nu k^2)\widehat F.}
\]
Along the characteristic from \((s,k_s)\),
\[
\boxed{k(t)=k_s\Big(\frac{T-s}{T-t}\Big)^2,\qquad
\int_s^t k(\tau)^2d\tau=\frac{k_s^2(T-s)^4}{3}\big[(T-t)^{-3}-(T-s)^{-3}\big],}
\]
\[
\boxed{\widehat F(t,k(t))=\widehat F(s,k_s)\Big(\frac{T-t}{T-s}\Big)^3
\exp\!\Big[-\nu\int_s^t k(\tau)^2d\tau\Big].}
\]
Every \(k_s\ne0\) companion is therefore pushed to UV while receiving a heat exponent diverging like \((T-t)^{-3}\). The Riccati blow-up itself survives on the harmonic affine backbone, a generalized zero-Fourier-mode geometry outside finite-energy \(L^2(\mathbb R^3)\).

**AUDIT / SCOPE.** These statements are exact only for the affine phase-locked branch and the exact architecture Section 71 family. They do **not** imply that a general finite-energy NS trajectory is affine, self-similar or Riccati locked. They are an adversarial NEO unit test: the strongest exact coherent amplifier presently known cannot carry a nonzero finite-frequency companion through its own blow-up clock without \(C^2\) seeing rapidly increasing heat.

## 9. NEO reading: the phase resonance has no square-anchor escape — EXACT ALGEBRA / DEDUCTION
Section 4 gives a genuine first-order phase resonance: on the intrinsic \(+\leftrightarrow-\) block, \((h(x)+h(y))A_{xy}=0\) becomes \(0=0\). The square anchor does not share that degeneracy:
\[
\boxed{(|x|+|y|)L_{xy}=(x+y)E_{xy},\qquad \nu C^2=\nu\Lambda^2\ \text{ on }\operatorname{Ran}P.}
\]
Except at the double-zero block, \(|x|+|y|>0\). Hence
\[
\boxed{\text{phase freedom in the }+\leftrightarrow-\text{ Sylvester kernel}\ \neq\ \text{freedom from the }C^2\text{ heat clock}.}
\]
This resolves the `NS_POLAR_COMPATIBILITY_ARCHITECTURE.md`, Section 85 paradox structurally. The exact affine amplifier evades heat only on its generalized Fourier-zero backbone. Finite energy forbids that backbone, while the control-volume spine already gives \(X\Rightarrow\bot\); any finite endpoint must therefore use \(Y\), actual regeneration of nonzero UV state. Algebraic freedom of the resonant angular block is not enough: regeneration at nonzero scale is produced by the same true transport that also deforms the radial/square anchor.

The affine unit test adds an adversarial geometric clue. Under one locked Riccati block, UV-producing covectors collapse toward a projective line; collinear shear is an exact Leray-source null and the hard-flip symbol contains the associated cross-product null factor. This is not a general PDE theorem, but it shows how prolonged locking can simultaneously weaken hard-flip regeneration and strengthen heat.

## 10. Candidate contradiction target: finite-energy \(Y\) must both lock and unlock — CANDIDATE PRINCIPLE / OPEN
The exact upstream facts are
\[
\boxed{T_*<\infty\Rightarrow Y,\qquad \int_s^{T_*}\mathfrak v(t)dt=\infty\quad(s<T_*).}
\]
A coherent amplifier wants its local Riccati involution nearly locked. The affine NEO test says that if a finite-frequency packet remains locked too long, \(C^2\) sees rapid UV heat and the packet tends toward line collapse. To avoid that fate, the true state must steer, rotate, rebuild angular spread or regenerate new nonzero spectral content. NEO forbids inserting that escape as a new mechanism: it must compile from
\[
\boxed{u(t),\ P,\ C,\ C^2,\ t}
\]
through \(\delta_u=[D_u,\cdot]\) and its parabolic completion, hence reappear in existing \(K,A,L,E\) jets and their compatible prolongations.

This suggests the unproved NEO-native dichotomy
\[
\boxed{\text{late UV critical regeneration}\ \Longrightarrow\
\text{square-anchor heat dominates}\ \vee\ \text{compiler steering breaks phase locking}.}
\]
The second branch must not become a new steering wallet. The task is to identify its exact contraction with an already compulsory carrier
\[
\|\Lambda^{-1/2}L_u u\|_2^2,\qquad \|\Lambda^{1/2}J_{\rm flip}\|_2^2,\qquad \int\operatorname{tr}(S^2G)dx,
\]
or with the existing longitudinal Codazzi/NEO prolongation, and then obtain time integrability from genuine viscosity or an exact compensated identity.

**Candidate contradiction.** A finite-energy singularity appears to need to be coherent enough to amplify and incoherent enough to regenerate. Staying locked exposes it to square-anchor heat/directional collapse; repeatedly unlocking to keep \(Y\) alive forces compatibility motion through the same NEO derivation. Since \(X\) is already excluded and control volume admits no third kinetic supplier, the missing theorem is to derive this lock--regenerate dichotomy directly from true NS, without an affine/Riccati hypothesis. A suitable projective/spectral theorem would say: persistent directional collapse forces hard-flip/source nullness plus square-anchor heat, while persistent angular spread forces a quantified compiler/Codazzi rate. Closing either branch against nonintegrable visibility would break the recycling loop without a new observer, source, genealogy or wallet.

---

## 11. Mother-jet normal form and dynamic costume equation — EXACT / DEDUCTION
Let
\[
E_u:=[D_u,C],\qquad D_u=u\cdot\nabla,\qquad Q:=I-P.
\]
The first-order NEO wardrobe has one mother parent. Differentiating \(PC=CP=C\) gives
\[
Q E_u P=(\delta_uP)C,\qquad P E_u Q=C(\delta_uP).
\]
On a nonzero spectral localization, with \(C^\dagger\) the inverse of \(C\) on \(\operatorname{Ran}P\),
\[
\boxed{\delta_uP=Q E_u C^\dagger+C^\dagger E_uQ.}
\]
Thus, for the actual state \(u=Pu\),
\[
\boxed{-\nabla p=(\delta_uP)u=Q E_u C^\dagger u.}
\]
Pressure is therefore a Hodge-normal filtered contraction of the same mother curl deformation.

For divergence-free \(u,v\), the mother jet is local:
\[
\boxed{E_uv=-\sum_j\nabla u_j\times\partial_jv.}
\]
Its self-contraction is vortex stretching,
\[
\boxed{E_uu=(Cu\cdot\nabla)u=S\omega,\qquad \omega=Cu.}
\]
Hence the local Riccati-alignment condition \(S\omega\approx\lambda\omega\) can be read at NEO level as \(E_uu\approx\lambda Cu\): one contraction of the mother operator, not a new primitive.

Let
\[
\mathcal T:=\partial_t+D_u+\nu C^2.
\]
For any real admissible spectral costume \(F=f(C)\), smooth solutions satisfy
\[
\boxed{\mathcal T(f(C)u)=-f(0)\nabla p+[D_u,f(C)]u.}
\]
When \(f(0)=0\),
\[
\boxed{\mathcal T(f(C)u)=Df_C[E_u]u,}
\]
after the same spectral-localization care used for divided differences. Vorticity, phase and modulus equations are the choices \(f(x)=x\), \(\operatorname{sgn}x\), and \(|x|\).

For two real costumes \(F=f(C)\), \(G=g(C)\), integration by parts gives the universal bilinear wardrobe law
\[
\boxed{\frac d{dt}\langle Fu,Gu\rangle+2\nu\langle CFu,CGu\rangle=\langle u,[D_u,(fg)(C)]u\rangle.}
\]
Energy, helicity and the critical \(\dot H^{1/2}\) balance are therefore three choices of the same NEO equation. The lifted signed-curl measure is likewise the positive spectral representation of this universal costume functional; it is a rendered history, not another input.

## 12. Exact NEO prism: Hodge, radial and angular readings — EXACT after localization
For input in the physical support, the mother jet has the orthogonal Hodge split
\[
\boxed{\|E_uP\|_{HS}^2=\|PE_uP\|_{HS}^2+\|Q E_uP\|_{HS}^2.}
\]
Using \(Q E_uP=(\delta_uP)C\) and the tangent polar Pythagoras,
\[
\boxed{\|E_uP\|_{HS}^2=\|(\delta_uP)C\|_{HS}^2+\|PL_uP\|_{HS}^2+\|\Lambda^{1/2}PA_uP\Lambda^{1/2}\|_{HS}^2.}
\]
Thus the first-order mother deformation has exactly three operator readings: Hodge/support, radial/modulus and angular/phase. This is an operator/HS statement. It must not be promoted to a vector-level Pythagoras after applying the operators to a spectrally mixed state; different input channels can interfere in one output channel.

For the Poisson-resolved state \(u_s=e^{-s\Lambda}u\), the resolvent mother carrier can be written
\[
\boxed{\mathfrak M_E=2\int_0^\infty\|P E_u u_s\|_2^2\,ds.}
\]
The raw local version is
\[
\boxed{\mathfrak M_E^{raw}=2\int_0^\infty\|E_u u_s\|_2^2\,ds,}
\]
and the Hodge part is exactly
\[
\boxed{\mathfrak M_E^{Hodge}=2\int_0^\infty\|Q E_u u_s\|_2^2\,ds=2\int_0^\infty\|K C u_s\|_2^2\,ds.}
\]
These are compiled diagnostics, not wallets. They are useful because the mother operator is local while the nonlocality is isolated in the anchor renderers \(P\) and \(e^{-s\Lambda}\).

## 13. Exact cross-helicity selection rule — EXACT
Let \(k\) be output frequency, \(\ell\) input frequency and \(q=k-\ell\). Fourier convolution gives
\[
\boxed{\widehat{[D_u,H]f}(k)=i\int(\widehat u(q)\cdot\ell)\,[H(\ell)-H(k)]\widehat f(\ell)\,d\ell.}
\]
If the input is on helicity sheet \(h\), then
\[
\boxed{\Pi_h(k)[H(\ell)-H(k)]\Pi_h(\ell)=0,}
\]
\[
\boxed{Q(k)[H(\ell)-H(k)]\Pi_h(\ell)=h\,Q(k)\Pi_h(\ell),}
\]
\[
\boxed{\Pi_{-h}(k)[H(\ell)-H(k)]\Pi_h(\ell)=2h\,\Pi_{-h}(k)\Pi_h(\ell).}
\]
Therefore angular transport from one helicity sheet has only a Hodge-normal output and an opposite-helicity output; the same-helicity output vanishes identically.

If \(\theta\) is the angle between \(k\) and \(\ell\), exact projector overlaps are
\[
\boxed{\|\Pi_h(k)\Pi_h(\ell)\|_{HS}=\frac{1+\cos\theta}{2},}
\]
\[
\boxed{\|Q(k)\Pi_h(\ell)\|_{HS}=\frac{|\sin\theta|}{\sqrt2},}
\]
\[
\boxed{\|\Pi_{-h}(k)\Pi_h(\ell)\|_{HS}=\frac{1-\cos\theta}{2}.}
\]
Thus Hodge leakage is \(O(\theta)\) while direct opposite-helicity overlap is \(O(\theta^2)\) near alignment. Along a smooth direction path \(n(t)\),
\[
\boxed{\Pi_{-h}\dot\Pi_h=0,\qquad \Pi_{-h}\ddot\Pi_h=-\dot\Pi_{-h}\dot\Pi_h.}
\]
The infinitesimal route is therefore \(h\to0\to-h\): first support/Hodge steering, then second-order intrinsic phase change. This is spectral fiber geometry, not a claim that pressure dynamically causes helicity flip.

## 14. Principal-symbol selection and the one-derivative gain — EXACT PRINCIPAL SYMBOL / DEDUCTION
Freeze \(A=\nabla u(x)\), write \(\xi=\rho n\), and set
\[
r=A^Tn=\alpha n+\beta,\qquad \beta\perp n.
\]
The mother principal symbol is
\[
\boxed{e_u(x,\xi)=-i\rho\,r\times.}
\]
Material covectors obey \(\dot\xi=-A^T\xi\), hence
\[
\boxed{\dot\rho=-\rho\alpha,\qquad \dot n=-\beta.}
\]
On the physical plane,
\[
\boxed{P_ne_uP_n=-\alpha C(\xi),\qquad \Pi_{-h}(n)e_u\Pi_h(n)=0.}
\]
Thus principal local transport produces radial scaling and Hodge/support steering but no direct intrinsic helicity flip. The latter is subprincipal or finite-displacement information.

In the near-diagonal regime \(|q|\ll|\ell|=\rho\), with \(q_\perp\) transverse to \(\ell\),
\[
1-\cos\theta=\frac{|q_\perp|^2}{2\rho^2}+O(|q|^3/\rho^3).
\]
Since \(\widehat u(q)\cdot\ell=O(\rho|\widehat u(q)|)\), the first nonzero cross-helicity kernel scales as
\[
\boxed{O(|q|^2/\rho).}
\]
This is the NEO origin of the \(\Lambda^{-1}\nabla^2u\)-type gain: the order-zero principal phase symbol is forbidden by the selection rule. The gain is local/near-diagonal; it cannot be extended blindly to far off-diagonal or antipodal interactions.

## 15. Hard-flip numerator as three NEO gates — EXACT FACTORIZATION / INTERPRETATION
For same-helicity parents, the self-interaction identity
\[
\widehat{u_h\times Cu_h}(k)=\frac h2\int_{q+\ell=k}(|\ell|-|q|)\widehat u_h(q)\times\widehat u_h(\ell)
\]
shows the exact radial gate: equal parent radii cancel. Incompressibility supplies the area gate through \(q\cdot\widehat u(q)=0\), and the cross-helicity selection rule supplies the phase-overlap gate. Consequently the known hard-flip numerator
\[
|P-M|PM\sin\delta(1-\cos\delta)
\]
can be read as
\[
\boxed{\underbrace{|P-M|}_{\text{radial antisymmetry}}\;\underbrace{PM\sin\delta}_{\text{incompressible transport area}}\;\underbrace{(1-\cos\delta)}_{\text{opposite-phase overlap}}.}
\]
Near parallel, the last two gates give \(O(\delta)O(\delta^2)=O(\delta^3)\). Near antipodal, the phase gate is open while the area gate remains linear; a nonzero radial mismatch is still required. The static symbol is therefore a rendered product of NEO selection rules, not a separate microscopic source.

## 16. NEO local-gain / far-heat research split — CANDIDATE PRINCIPLE / OPEN
The selection rule suggests a two-regime attack on the true operator \(P_{-h}[D_u,H]P_h\):
\[
\boxed{\text{near spectral diagonal}\Longrightarrow\text{one-derivative gain from the forbidden principal phase symbol},}
\]
\[
\boxed{\text{far spectral diagonal}\Longrightarrow\text{no local gain, but the responsible nonzero states remain visible to the square anchor }C^2.}
\]
This is not yet a regularity theorem. The next task is to implement an exact/paradifferential partition before norm inequalities, identify the near piece as \(\Lambda^{-1}\) times a second-order local transport term, and rewrite the far piece so the parent heat scale is explicit. If successful, critical angular regeneration would split into a local derivative-gain branch and a nonlocal heat-visible branch without adding an observer, wallet or mechanism.

**NEO frontier.** The current experiments support a stronger working thesis: the wardrobe is one mother curl-jet spine with functional-calculus renderers, and the renderers obey selection rules. The difficult critical channel is not free; its principal local symbol is forbidden, its near-diagonal part is one order smoother, and its far-off-diagonal escape remains exposed to the same square anchor that generates viscosity.

---

## 17. Parabolic regeneration closes inside the same mother/Sylvester compiler — EXACT after localization
Let
\[
\mathscr J(a,b):=\frac14T_H(a,b),
\qquad
J_{\rm flip}=\mathscr J(u,u),
\]
where \(T_H\) is the symmetric helicity-involution torsion already compiled from the Euler bilinear map and \(H=\operatorname{sgn}C\).  Resolving the same-helicity inputs gives
\[
\boxed{
\mathscr J(a,b)
=-\frac14\sum_{h=\pm1}h\,P_{-h}
\Big([D_{a_h},H]b_h+[D_{b_h},H]a_h\Big).
}
\]
For a divergence-free direction field \(a\), write
\[
E_a:=[D_a,C],
\qquad
E_{a,h}^{\times}:=P_{-h}E_aP_h,
\qquad
\mathcal S_\Lambda X:=\Lambda X+X\Lambda.
\]
On a fixed nonzero spectral localization the opposite-sheet block obeys the positive Sylvester equation
\[
P_{-h}[D_a,H]P_h=2\mathcal S_\Lambda^{-1}(E_{a,h}^{\times}),
\qquad
\mathcal S_\Lambda^{-1}(Y)=\int_0^\infty e^{-s\Lambda}Ye^{-s\Lambda}\,ds.
\]
Hence the full polarized hard-crossing map has the mother normal form
\[
\boxed{
\mathscr J(a,b)
=-\frac12\sum_h h\Big[
\mathcal S_\Lambda^{-1}(E_{a_h,h}^{\times})b_h
+\mathcal S_\Lambda^{-1}(E_{b_h,h}^{\times})a_h
\Big].
}
\]
In particular
\[
\boxed{
J_{\rm flip}
=-\sum_h h\,\mathcal S_\Lambda^{-1}(E_{u_h,h}^{\times})u_h.
}
\]
Thus hard helicity crossing is not an additional bilinear primitive: it is a self-contraction of the same mother curl deformation after positive Sylvester resolution.

The native NS law
\[
(\partial_t+\nu\Lambda^2)J_{\rm flip}=S_J
\]
closes under the same compiler.  Since \(J(u)=\mathscr J(u,u)\) is quadratic and \(N=P(u\times Cu)\),
\[
\boxed{
S_J
=2\mathscr J(u,N)-2\nu\sum_j\mathscr J(\partial_j u,\partial_j u).
}
\]
Equivalently,
\[
\boxed{
\begin{aligned}
S_J=-\sum_hh\Big[&
\mathcal S_\Lambda^{-1}(E_{u_h,h}^{\times})N_h
+\mathcal S_\Lambda^{-1}(E_{N_h,h}^{\times})u_h\\
&-2\nu\sum_j\mathcal S_\Lambda^{-1}(E_{\partial_j u_h,h}^{\times})\partial_j u_h
\Big].
\end{aligned}
}
\]
The first line is the actual NS directional derivative of the same crossing map in the direction \(N\); the second is the exact heat carré-du-champ generated when the square anchor \(C^2=\Lambda^2\) passes through a quadratic derived field.  No regeneration source outside \((u,P,C,C^2,t)\) has appeared.

**NEO upgrade.**  The compiler chain is now
\[
\boxed{
(u,P,C,C^2,t)
\longrightarrow E_u
\longrightarrow \mathscr J
\longrightarrow J_{\rm flip}
\longrightarrow S_J,
}
\]
with every arrow an anchor functional-calculus, contraction, NS substitution, or parabolic Leibniz prolongation.  Regeneration is therefore a higher motion of an already compiled costume, not ontology growth.

## 18. The derived crossing field has its own exact dynamic polar law — EXACT
Because \(\Lambda\) is time-independent and commutes with the heat semigroup, put
\[
z:=\Lambda^{-1}J_{\rm flip},
\qquad
f:=\Lambda^{-1}S_J.
\]
On the nonzero spectral support,
\[
\boxed{z_t+\nu\Lambda^2z=f.}
\]
Whenever \(z\neq0\), write the Hilbert-space polar decomposition
\[
z=\rho e,
\qquad
\rho=\|z\|_2,
\qquad
\|e\|_2=1,
\]
and let
\[
\mathbb P_e^\perp:=I-|e\rangle\langle e|
\]
be the orthogonal projector in the state Hilbert space.  This \(\mathbb P_e^\perp\) is a derived kinematic reader; it is not the Fourier Hodge projector \(P\) or \(Q=I-P\).  Since \(\langle e,e_t\rangle=0\) and \(\langle e,\Lambda^2e\rangle=\|\Lambda e\|_2^2\), the source splits exactly as
\[
\boxed{
f=
\Big(\rho'+\nu\rho\|\Lambda e\|_2^2\Big)e
+\rho\Big(e_t+\nu\mathbb P_e^\perp\Lambda^2e\Big).
}
\]
The two terms are orthogonal, so
\[
\boxed{
\|\Lambda^{-1}S_J\|_2^2
=
\Big(\rho'+\nu\rho\|\Lambda e\|_2^2\Big)^2
+\rho^2\Big\|e_t+\nu\mathbb P_e^\perp\Lambda^2e\Big\|_2^2.
}
\]
This is a genuine Hilbert-space Pythagoras for the one derived source \(\Lambda^{-1}S_J\).  It must not be confused with a vector-level Pythagoras between NEO near/far Fourier channels, where interference is allowed.

**DEDUCTION.**  Dynamic maintenance of hard crossing has exactly two kinematic readings:
\[
\boxed{\text{amplitude/radial repair}}
\qquad\text{or}\qquad
\boxed{\text{coherence-direction relocation}}.
\]
A cancellation need not be repaired at the same Fourier child.  The normalized profile \(e\) may rotate toward companion outputs while \(\rho\) remains small or vice versa.  Unequal-output heat is visible through \(\mathbb P_e^\perp\Lambda^2e\); parent-relative heat mismatch remains inside the already compiled carré-du-champ in \(S_J\).  Neither effect is a new mechanism.

## 19. Hardy ownership locks macroscopic crossing coherence to the UV — ABSOLUTE ANALYTIC DEDUCTION
The div--curl Hardy estimate for the hard field gives
\[
\|J_{\rm flip}\|_{\mathcal H^1}
\lesssim
\|u\|_2\|\nabla u\|_2,
\]
so the original kinetic budget owns
\[
\mathcal M_J(T):=\int_0^T\|J_{\rm flip}\|_{\mathcal H^1}^2dt<\infty
\]
on every finite interval before a putative endpoint.  The three-dimensional Nash inequality, using \(\mathcal H^1\hookrightarrow L^1\), gives pointwise
\[
\boxed{
\|J\|_2^2
\lesssim
\|J\|_{\mathcal H^1}^{4/5}\|\Lambda J\|_2^{6/5}.
}
\]
Hence, with
\[
\mathcal A_J(T):=\int_0^T\|J\|_2^2dt,
\qquad
\mathcal Z_J(T):=\int_0^T\|\Lambda J\|_2^2dt,
\]
Hölder yields
\[
\boxed{
\mathcal A_J\lesssim \mathcal M_J^{2/5}\mathcal Z_J^{3/5}.
}
\]
The exact heat law for \(J\), paired as
\[
\langle J,S_J\rangle
=\langle\Lambda J,\Lambda^{-1}S_J\rangle,
\]
gives
\[
\mathcal Z_J
\le
\frac{\|J(0)\|_2^2}{\nu}
+\frac1{\nu^2}
\mathcal R_J,
\qquad
\mathcal R_J(T):=\int_0^T\|\Lambda^{-1}S_J\|_2^2dt.
\]
Therefore
\[
\boxed{
\mathcal A_J
\lesssim
\mathcal M_J^{2/5}
\left(
\frac{\|J(0)\|_2^2}{\nu}
+\frac{\mathcal R_J}{\nu^2}
\right)^{3/5}.
}
\]
Equivalently, up to universal constants,
\[
\boxed{
\mathcal R_J
\gtrsim
\nu^2\frac{\mathcal A_J^{5/3}}{\mathcal M_J^{2/3}}
-\nu\|J(0)\|_2^2.
}
\]
Thus finite microscopic Hardy action converts large macroscopic \(L^2\) coherence into a superlinear dynamic repair bill.  This is not a new wallet: \(\mathcal M_J\) is kinetically owned and \(\mathcal R_J\) is exactly the already forced endpoint source action.

There is also a pointwise scale lock.  Define the RMS output frequency when \(J\neq0\) by
\[
\kappa_J:=\frac{\|\Lambda J\|_2}{\|J\|_2}.
\]
Nash implies
\[
\boxed{
\kappa_J
\gtrsim
\left(\frac{\|J\|_2}{\|J\|_{\mathcal H^1}}\right)^{2/3}.
}
\]
Consequently, on a finite singular interval, the combination
\[
\int\|J\|_{\mathcal H^1}^2dt<\infty,
\qquad
\int\|J\|_2^2dt=\infty
\]
forces
\[
\boxed{\sup_{t<T_*}\kappa_J(t)=\infty.}
\]
Macroscopic hard-crossing coherence cannot remain confined to a bounded output scale while its microscopic Hardy mass stays finite.

## 20. Variational prolongation is a compiler operation, not a new primitive — EXACT for the quadratic crossing map / RESEARCH RULE
Once a nonlinear NS costume has been compiled from the anchors, its linearization and adjoint linearization are canonical prolongations of that same map.  For
\[
J(u):=J_{\rm flip}(u),
\qquad
K_u:=DJ[u],
\]
quadratic homogeneity gives
\[
\boxed{K_uu=2J.}
\]
The existing variational Gauss--Weingarten identity is
\[
\boxed{
R_\Lambda=2\Lambda J+2K_u^*\Lambda u.
}
\]
Therefore the adjoint companion response of the same crossing map obeys
\[
\langle u,K_u^*\Lambda u\rangle
=2\langle\Lambda u,J\rangle
=\frac12W_\Lambda,
\]
and hence
\[
\boxed{
\|K_u^*\Lambda u\|_2^2
\ge
\frac{W_\Lambda^2}{4\|u\|_2^2}.
}
\]
A large \(J\) need not feed critical stock if it is nearly orthogonal to \(\Lambda u\); once it does feed criticality, however, the same quadratic map necessarily has a nontrivial adjoint companion response.  This is a full-convolution variational statement, not a quartet genealogy.

The coherence functional
\[
\Phi(u):=\frac12\|J(u)\|_2^2
\]
has the exact gradient
\[
\boxed{\nabla\Phi(u)=K_u^*J.}
\]
Euler homogeneity gives
\[
\boxed{
\langle u,K_u^*J\rangle=2\|J\|_2^2,
\qquad
\|K_u^*J\|_2\ge\frac{2\|J\|_2^2}{\|u\|_2}.
}
\]
Hence, on a finite interval with the kinetic mass bounded, the endpoint condition \(\int\|J\|_2^2dt=\infty\) forces
\[
\boxed{
\int_0^{T_*}\|DJ[u]^*J\|_2^2dt=\infty.
}
\]
This cubic field is a variational prolongation of the already compiled quadratic map; it must not be promoted to an incidence wallet or new source species.

Static variational response and dynamic regeneration are linked by one exact derivative:
\[
\boxed{
\frac12\frac d{dt}\|J\|_2^2
=\langle u_t,K_u^*J\rangle
=\langle J,S_J\rangle-\nu\|\Lambda J\|_2^2.
}
\]
Thus companion/incidence language and heat-covariant repair language are two renderings of the same derived-field motion.

**RESEARCH RULE.**  The NEO grammar now admits three kinds of operations without ontology growth:
\[
\boxed{
\text{spectral functional calculus }f(C),
\qquad
\text{transport/parabolic prolongation},
\qquad
\text{variational prolongation }DF[u],DF[u]^*.
}
\]
The last operation is permitted only after \(F\) itself has been compiled from \((u,P,C,C^2,t)\); it does not license arbitrary auxiliary functionals.

## 21. Upgraded NEO closure principle — CANDIDATE PRINCIPLE / OPEN
The current compiler has moved beyond a static polar dictionary.  It now has a closed hierarchy of generated motion:
\[
\boxed{
\begin{array}{ccccc}
(u,P,C,C^2,t)
&\longrightarrow&E_u=[D_u,C]
&\longrightarrow&\text{spectral costumes}\\
&&\downarrow&&\\[-1mm]
&&J_{\rm flip}&&\\
&&\downarrow&&\\[-1mm]
&&S_J&&\\
&&\downarrow&&\\[-1mm]
&&\Lambda^{-1}S_J
&\longrightarrow&\text{amplitude/direction polar motion}.
\end{array}
}
\]
In parallel, every already compiled nonlinear map has its canonical variational branch
\[
\boxed{F(u)\longrightarrow DF[u]\longrightarrow DF[u]^*.}
\]
The resulting working principle is:

\[
\boxed{
\begin{gathered}
\textbf{NEO closure principle.}\\
\text{Every dynamically relevant NS defect found so far is generated by}\\
\text{anchor functional calculus, transport/parabolic prolongation, or}\\
\text{variational prolongation of an already compiled map.}
\end{gathered}
}
\]
Pressure, stress, torsion, Codazzi, coherence, leakage and incidence remain costumes whenever they pass this parentage test.  Changing tensor type, observer, or differentiation order is not evidence for a new primitive.

The new dynamic content is equally restrictive.  If hard-crossing coherence becomes macroscopically large while its kinetic Hardy owner remains finite, then it must move to the UV.  Maintaining that UV coherence requires the already compiled \(\Lambda^{-1}S_J\), whose exact polar law splits only into amplitude repair and coherence-direction relocation.  If the coherence aligns so as to feed the critical stock, the adjoint prolongation of the same quadratic map is forced as well.  Thus NEO now tracks not only where a derived quantity comes from, but the kinematically allowed ways in which that compiled quantity can move under the true NS flow.

**OPEN.**  None of these identities proves that the endpoint repair action is finite, nor do they prove global regularity.  The strengthened research target is instead structural: push the no-new-primitive statement to higher NEO jets, derive normal forms for their near/far renderings, and determine whether every apparent higher defect continues to reduce to the same anchor spine before any norm inequality is applied.
