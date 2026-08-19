# `B/S/V/O` Full-State Frontier — Mother-Law Form

This is the canonical remaining proof block after the representation/owner frontier has been exhausted.  It is organized from true Navier--Stokes state laws outward, not from a cancellation taxonomy inward.  It does **not** claim `Y=>bot` or global regularity.

In this file `B` means `B_crit`, the already-canonical minority-helicity positive-critical nonlinear-work branch; it is not the endpoint complement `B_bad` and is not a fourth sidecar fate.  The exact sidecar theorem remains `Y => S vee V vee O`.  The missing theorem remains

> **No infinite critical full-state recycling**, equivalently `Y=>bot` under the already-proved endpoint grammar.

## 1. Ontology and proof discipline

Primitive true fields/state:
`u`, `omega=curl u`, `S=sym grad u`, `p`,
`N=-P(u.grad u)=P(u x omega)`,
`G=curl N`,
`F_N=N_t-nu Delta N`.

Primitive kinetic objects:
actual modal stock, actual signed nonlinear work `2 Re(conj(uhat) Nhat)`, actual fixed-set boundary work, viscosity, and the initial surface.

Readers only:
helical coordinates, signed curl `x=s|k|`, radial/signed-curl cuts, `F(a)`, `Psi(a)`, the action profile `A(a)`, triad tents, heat fibers, projective source lines, rate variables, neutral radii and moving-front coordinates.  A reader may locate or compress true NS physics; it is not an owner, token, clock, genealogy, dissipation or new force.

The current rule is: first derive from true NS identities; only then use a reader to expose what the identity already forces.

## 2. Mother law: one true force triangle — EXACT

The velocity equation is
`N=u_t+nu Lambda^2 u`, `Lambda=(-Delta)^(1/2)`.

At every nonzero Fourier/helical mode `m=(k,s)`, `rho=|k|`, with actual nonlinear work
`T_m=2 Re(conj(u_m) N_m)`, exact squaring gives

`nu T_m = rho^-2 (|N_m|^2-|u_(t,m)|^2) + nu^2 rho^2 |u_m|^2`.

Thus recipient/donor work is exactly the law-of-cosines defect of the three true vectors `N_m`, `u_(t,m)` and `nu rho^2 u_m`; it is not a sign assigned by a proof taxonomy.

For every fixed Fourier/helicity projector `P`, define
`W_P:=2<Pu,PN>=phi_(in,P)-phi_(out,P)`.
Because `P` commutes with `Lambda`, `Delta` and `partial_t`,

`nu W_P = ||Lambda^-1 PN||_2^2 - ||Lambda^-1 Pu_t||_2^2 + nu^2||Lambda Pu||_2^2`.    (2.1)

The same fixed set obeys Kirchhoff continuity

`d||Pu||_2^2/dt + 2nu||Lambda Pu||_2^2 = W_P`.    (2.2)

Hence

`nu d||Pu||_2^2/dt = [action defect]_P - 2nu^2||Lambda Pu||_2^2`.    (2.3)

At `W_P=0`, `Pu_t` is the hypotenuse:

`||Lambda^-1 Pu_t||^2=||Lambda^-1 PN||^2+nu^2||Lambda Pu||^2`.    (2.4)

At a stock turning point `d||Pu||^2/dt=0`, `PN` is the hypotenuse:

`||Lambda^-1 PN||^2=||Lambda^-1 Pu_t||^2+nu^2||Lambda Pu||^2`.    (2.5)

For the full space `W_I=2<u,N>=0`, so (2.4) is the global exact force triangle.

The older critical-action identity is only a layer-cake reading of (2.1), not a separate mechanism:

`||N||_Hdot^-1/2^2 = ||u_t||_Hdot^-1/2^2 + nu^2||u||_Hdot^3/2^2 + nu d||u||_Hdot^1/2^2/dt`.

## 3. Signed-curl Kirchhoff potential — EXACT

Write the helical signed-curl coordinate `x=s|k|` and push the actual modal work to the signed measure `dW_t(x)`.  Nonlinear energy and helicity conservation are exactly

`int dW=0`,
`int x dW=0`.    (3.1)

For the actual signed-curl tail `Omega_a={x>a}`, define

`F(a,t):=int_(x>a) dW_t(x)=2<P_a u,P_a N>`.

Every such actual control volume obeys

`dE_(Omega_a)/dt + 2nu||Lambda P_a u||_2^2 = F(a,t)`.    (3.2)

Define the hinge-work potential

`Psi(a,t):=int (x-a)_+ dW_t(x)=int_a^infinity F(b,t) db`.    (3.3)

Because of (3.1), also

`Psi(a,t)=(1/2) int |x-a| dW_t(x)`,
`Psi'(a)=-F(a)`,
`Psi''=dW` distributionally.    (3.4)

Thus one actual profile contains the complete signed-curl work traffic: height is a hinge-work source, slope is boundary work, curvature is actual modal work density.

For any suitable scalar weight `f`,

`int f(x)dW(x)=int f''(a) Psi(a) da`    (3.5)

with the distributional interpretation when `f` has kinks.  Affine weights vanish because of energy/helicity conservation.

Special readings:

`P_(1/2)^NL := int |x|dW = 2 Psi(0)`,    (3.6)

`Q:=int omega.S omega = int Psi(a) da`,    (3.7)

and for the full radial high-tail flux `J(R)=2<H_Ru,H_RN>`,

`J(R)=F(R)-F(-R)`,
`P_(1/2)^NL=int_0^infinity J(R)dR`,
`Q=int_0^infinity R J(R)dR`.    (3.8)

All Sobolev nonlinear source laws are Mellin readings of this same actual radial boundary work; they are not independent ledgers.

## 4. Full-state action profile — EXACT

Let `C=curl` on divergence-free fields and set the positive spectral multiplier
`M_a:=|C-a|`.
Define the quadratic full-state reader

`A(a,t):=||M_a^(1/2)Lambda^-1 N||_2^2 - ||M_a^(1/2)Lambda^-1 u_t||_2^2 + nu^2||M_a^(1/2)Lambda u||_2^2`.    (4.1)

The mother law gives

`A(a,t)=2nu<M_a u,N>=2nu Psi(a,t)`.    (4.2)

Therefore

`F(a,t)=-(1/(2nu)) partial_a A(a,t)`,
`dW_t(a)=(1/(2nu)) partial_a^2 A(a,t)` distributionally.    (4.3)

Energy/helicity give the clamped signed-curl boundary conditions `A,A_a ->0` at both ends whenever the corresponding moments exist.

Critical production is one height:

`A(0,t)=nu P_(1/2)^NL(t)`.    (4.4)

Vortex stretching is one area:

`int A(a,t) da = 2nu Q(t)`.    (4.5)

Hence the cubic traffic quotient and the quadratic full-state action geometry are two exact readings of the same actual work measure.  This does **not** make the traffic profile a dynamically closed state; its time evolution uses `F_N`, as below.

## 5. Triad tents and divided differences — EXACT

For a closed triad with distinct signed roots `alpha<beta<gamma`, let

`T_alpha=Z/[(beta-alpha)(gamma-alpha)]`,
`T_beta=-Z/[(beta-alpha)(gamma-beta)]`,
`T_gamma=Z/[(gamma-alpha)(gamma-beta)]`.

Define the positive triangular Green tent

`M_(alpha,beta,gamma)(a)=(a-alpha)/[(beta-alpha)(gamma-alpha)]` for `alpha<a<beta`,

`M_(alpha,beta,gamma)(a)=(gamma-a)/[(gamma-beta)(gamma-alpha)]` for `beta<a<gamma`, and `0` otherwise.

Then the triad contribution to the hinge/action profile is

`Psi_tau(a)=Z_tau M_(alpha,beta,gamma)(a)`,
`A_tau(a)=2nu Z_tau M_(alpha,beta,gamma)(a)`.    (5.1)

For every scalar reader `f`,

`sum_i f(x_i)T_i = Z_tau f[alpha,beta,gamma] = Z_tau int f''(a)M_tau(a)da`.    (5.2)

Thus energy `f=1` and helicity `f=x` vanish because affine functions have zero curvature; enstrophy `f=x^2` reads the constant curvature; criticality `f=|x|` reads the kink at `x=0`.  Homochiral critical production vanishes because its tent does not cross the fold.

This is the atomic signed-curl picture.  The frontier below is formulated after full convolution summation.

## 6. Positive criticality forces a neutral single-helicity tail — EXACT on smooth finite-energy `R^3`

Assume at one smooth time
`P_(1/2)^NL>0`, hence `Psi(0)>0`.
On smooth finite-energy `R^3`, the signed-radius work pushforward has a continuous cumulative profile under the regularity/integrability used here.  Let `a_*` be a maximum of the positive component of `Psi` containing `0`, and put

`H:=Psi(a_*)>0`.

Then

`F(a_*)=0`,
`H>=Psi(0)=P_(1/2)^NL/2`.    (6.1)

If `a_*>0`, choose the positive-helicity tail
`P=P_(+,R_*)`, `R_*=a_*`.
If `a_*<0`, choose the negative-helicity tail
`P=P_(-,R_*)`, `R_*=-a_*`.
If `a_*=0`, either helicity half may be used with the corresponding one-sided statement.

For this actual single-helicity tail, with `U=Pu`,

`W_P=2<U,PN>=0`,    (6.2)

but its critical/helicity-magnitude nonlinear source is

`H=2<Lambda U,PN> >= P_(1/2)^NL/2 >0`.    (6.3)

Equivalently, since `P omega=sigma Lambda U`,

`2<P omega,PN>=sigma H`,
`2<U,PG>=sigma H`.    (6.4)

Thus positive global critical creation forces a true tail with **zero nonlinear kinetic-energy source but nonzero helicity transfer**.  The nonlinearity hardens the tail without funding its total kinetic energy.

Discrete/torus caveat: signed radii may jump, so an exact finite neutral cut need not exist.  There one retains the superlevel sign-reversal/equal-moment statements rather than asserting a continuous zero.

## 7. Flux reversal around a nondegenerate neutral tail — EXACT

Suppose the maximum in Section 6 is nondegenerate, so the signed-curl work density satisfies
`w(a_*)=Psi''(a_*)<0`.
Let `J_sigma(R)` be actual net nonlinear work into the same-helicity radial tail `P_(sigma,R)`.  Then

`J_sigma(R_*)=0`,
`partial_R J_sigma(R_*)=-w(a_*)>0`.    (7.1)

Hence for small `eps>0`,

`J_sigma(R_*-eps)<0<J_sigma(R_*+eps)`.    (7.2)

So a shallower same-helicity tail is a net donor while a deeper same-helicity tail is a net recipient.  The intervening actual annulus has negative net work.  This is the full-convolution continuum version of median-to-extremes radial sorting; it is a same-time mode-set statement, not pair ancestry.

The neutral tail also has exact outward first moment

`int_(rho>R_*) (rho-R_*) dW_sigma(rho)=H>0`.    (7.3)

Since its zeroth work moment is zero, the same canonical Hahn restriction has equal positive/negative masses but the positive-work barycenter lies farther UV than the negative-work barycenter.  No second Hahn split is introduced.

## 8. Forced radial sorter inside the neutral tail — EXACT

Freeze the actual neutral tail `P` at the selected time and write

`E:=||U||_2^2`,
`mu:=<Lambda U,U>/E`,
`V:=(Lambda-mu)U`,
`S:=||V||_2^2=<Lambda^2U,U>-mu^2E`.    (8.1)

By construction `V perp U`.  From `W_P=0` and (6.3),

`<V,PN>=H/2`.    (8.2)

Positive `H` forces `S>0`; otherwise `Lambda U=mu U` and the critical source would vanish.

Orthogonal projection therefore gives the exact decomposition

`PN = [H/(2S)] V + N_perp`,
`N_perp perp U`, `N_perp perp V`.    (8.3)

Since `Lambda U=mu U+V`, also
`<Lambda U,N_perp>=0`.

Thus the entire kinetic-neutral / critical-positive hardening is carried by the unique forced component

`N_sort := [H/(2S)](Lambda-mu)U`.    (8.4)

The remainder `N_perp` contains every still-available phase, polarization, same-heat and higher-shape degree of freedom, but contributes zero to the first two radial work moments of this tail.

Modewise, the forced component has the universal work profile

`T_sort(k)=[H/S](rho-mu)|U_k|^2`.    (8.5)

It is donor below the energy mean radius and recipient above it, with

`int T_sort=0`,
`int rho T_sort=H`.    (8.6)

Pythagoras gives

`||PN||_2^2 = H^2/(4S) + ||N_perp||_2^2`.    (8.7)

This is an exact state decomposition, not a new acceleration source or finite budget.

## 9. Viscosity acts on the same radial-shape direction — EXACT

Write radial energy moments on the frozen tail
`D_j:=<U,Lambda^j U>=int rho^j de(rho)`, so `D_0=E`, `D_1=mu E`.

Decompose the true viscous vector in the same orthogonal frame:

`Lambda^2U = (D_2/E)U + beta V + Z`,
`Z perp U,V`,
`beta=(D_3-mu D_2)/S`.    (9.1)

The coefficient has the exact pair representation

`beta = [double_int (rho-eta)^2(rho+eta) de(rho)de(eta)] / [double_int (rho-eta)^2 de(rho)de(eta)]`.    (9.2)

For a non-monochromatic tail supported on `rho>R`, `beta>2R`.

Substituting (8.3) and (9.1) into `U_t=PN-nu Lambda^2U` gives

`U_t = -nu(D_2/E)U + [H/(2S)-nu beta]V + [N_perp-nu Z]`.    (9.3)

This is the current exact radial-shape split:

- along `U`, kinetic amplitude decays purely by viscosity because the tail is work-neutral;
- along `V`, nonlinearity pushes outward with coefficient `H/(2S)` and viscosity pushes inward with coefficient `nu beta`;
- the orthogonal remainder carries higher-shape/phase/polarization motion invisible to the first two radial moments.

The mean radius therefore obeys at the neutral instant

`dot mu = H/E - 2nu(D_3-mu D_2)/E`.    (9.4)

Moreover

`E D_3-D_1D_2 = (1/2) double_int (rho-eta)^2(rho+eta) de(rho)de(eta) >=0`.    (9.5)

Hence the nonlinear term hardens the tail and viscosity softens its mean radius, exactly.  If `dot mu>=0`, then the forced outward coefficient must beat the own-tail viscous coefficient; no heuristic cascade velocity is introduced.

## 10. Moving neutral front and excess-radius stock — EXACT on a smooth branch

Assume a nondegenerate neutral radius admits a smooth branch `R_*(t)` with the same helicity sign and
`J_sigma(R_*(t),t)=0`.

Define the actual excess-radius stock behind the moving neutral front

`K_*(t):=int_(rho>R_*(t)) (rho-R_*(t)) de(rho,t)`.    (10.1)

The weight vanishes at the moving boundary, so differentiation creates no boundary-stock atom.  Exact NS continuity gives

`dot K_* + R_*' E_* + 2nu(D_3-R_*D_2) = H_*`.    (10.2)

Integrated on a smooth branch,

`K_*(t1) + int R_*'E_* dt + 2nu int(D_3-R_*D_2)dt = K_*(t0)+int H_*dt`.    (10.3)

`R_*'E_*` is a kinematic moving-reader term, not physical dissipation or a kinetic owner.  The actual physical terms remain stock, nonlinear hinge work and viscosity.

For a nondegenerate root,

`R_*' = [partial_t J_sigma(R_*,t)]/w(a_*,t)`.    (10.4)

Because `w(a_*)<0`, UV motion `R_*'>0` requires the old fixed tail to begin moving to the donor side: `partial_t J_sigma(R_*,t)<0`.

## 11. Work curvature is governed by true `F_N` — EXACT

For every fixed mode,

`(partial_t+2nu|k|^2) T_k = 2|N_k|^2 + 2 Re(conj(u_k)(F_N)_k)`.    (11.1)

Push this identity to signed curl.  If `w(x,t)` is actual work density, `n_2(x,t)` the pushforward of `|N_k|^2`, and `f_N(x,t)` the pushforward of `Re(conj(u_k)(F_N)_k)`, then

`partial_t w + 2nu x^2 w = 2n_2 + 2f_N`.    (11.2)

At a donor curvature slice `w<0`, both the direct viscous term when moved to the RHS and `n_2>=0` push the donor curvature toward zero.  If the negative curvature is not allowed to relax, `partial_t w<=0`, true NS therefore forces

`f_N <= nu x^2 w - n_2 < -n_2`.    (11.3)

This is the exact job of `F_N`; there is no unnamed repair mechanism.

For every fixed projector `P`, the same curvature law is

`dot W_P + 4nu<Lambda Pu,Lambda PN> = 2||PN||^2 + 2<Pu,PF_N>`,    (11.4)

or equivalently

`dot W_P = 2||Pu_t||^2 + 2<Pu,PF_N> - 2nu^2||Lambda^2Pu||^2`.    (11.5)

At a neutral tail, UV drift therefore requires

`<Pu,PF_N> < nu^2||Lambda^2Pu||^2 - ||Pu_t||^2`.    (11.6)

The complementary fixed set has exactly the opposite work-curvature residual because the global nonlinear kinetic work is identically zero.

## 12. The action hump itself evolves by `N/F_N` — EXACT

For fixed `a`, differentiation of `Psi(a)=<M_a u,N>` gives

`partial_t Psi(a) + 2nu<M_a Lambda u,Lambda N> = ||M_a^(1/2)N||^2 + <M_a u,F_N>`.    (12.1)

At a smooth moving maximum `a_*(t)`, `Psi_a(a_*)=0`, so the envelope derivative has no artificial `a_*'` term:

`dot H + 2nu<M_(a_*) Lambda u,Lambda N> = ||M_(a_*)^(1/2)N||^2 + <M_(a_*)u,F_N>`.    (12.2)

Thus a UV-moving, non-decaying positive action hump must satisfy simultaneously the neutral-tail drift condition, the local work-curvature condition and the weighted hump-height condition, all through the same true `F_N`.

The quartic relative-translation anti-correspondence remains essential: instantaneous stocks/work/`Q` do not determine `dot Q`; `F_N` carries full-state phase information discarded by the cubic traffic quotient.

## 13. `G` is the same nonlinear acceleration viewed through curl — EXACT

Define
`G:=curl N=omega_t-nu Delta omega=S omega-(u.grad)omega=[omega,u]`.

Its exact PDE is

`G_t-nu Delta G=[G,u]+[omega,N]-2nu sum_j[partial_j omega,partial_j u]`.    (13.1)

There is no independent pressure source here.

On the neutral single-helicity tail of Section 6,

`H=2<Lambda U,PN>=2sigma<P omega,PN>=2sigma<U,PG>`.    (13.2)

Global orthogonality `<u,G>=<omega,N>=0` forces the complementary projector to carry the exact opposite pairing.  This is a same-time full-state companion law, not an ancestry relation.

The physical second acceleration may be written rotationally as

`F_N=P(N x omega + u x G - 2nu sum_j partial_j u x partial_j omega)`.    (13.3)

For every fixed Fourier projector `H` commuting with derivatives and Leray, put `L=I-H`.  Exact scalar-triple-product cancellation gives
`C_H:=||HN||_2^2+<Hu,HF_N>`
`=<HN,Lu x omega>+<Hu,LN x omega>+<Hu,Lu x G>-2nu sum_j<Hu,partial_j u x partial_j omega>`.    (13.4)
Indeed `||HN||^2=<HN,Hu x omega>+<HN,Lu x omega>` while `<Hu,HN x omega>=-<HN,Hu x omega>` and `<Hu,u x G>=<Hu,Lu x G>`.  Thus the nonlinear **internal `H-H` curvature source cancels exactly**.  Applying the same formula to `L` reverses all three cross terms, so
`C_H+2nu sum_j<Hu,partial_j u x partial_j omega>=-[C_L+2nu sum_j<Lu,partial_j u x partial_j omega>]`,
`C_H+C_L=||N||^2+<u,F_N>=2nu Q`.    (13.5)
Hence cross-volume nonlinear curvature is an exact antisymmetric transfer, not a source; only the genuine viscous commutator has nonzero global sum, already owned by the `H^1` law `0.5 d||grad u||^2/dt+nu||Delta u||^2=Q`.  Put `Q_H:=<Lambda Hu,Lambda HN>`.  Combining (13.4) with the fixed-set work-curvature identity gives
`(1/2)dot W_H=<HN,Lu x omega>+<Hu,LN x omega>+<Hu,Lu x G>-2nu[sum_j<Hu,partial_j u x partial_j omega>+Q_H]`.    (13.6)
Every term on the right changes sign under `H<->L`; actual work-rate is therefore pure complementary transfer, with no second-order global supplier.  In fact the underlying boundary work already has the exact cross-volume form
`W_H=2<Hu,HN>=2<Hu,Lu x omega>=-W_L`.    (13.7)
Differentiating this same true triple by NS reproduces (13.6), so curvature transfer is the time jet of the existing boundary-work object, not a new currency.  Every non-affine reshaping belongs to true `N/G/F_N` transfer plus known viscosity, not to an internal UV mechanism.

## 14. Pressure remains Hodge completion, not a second road — EXACT

Let `A=grad u=S+Omega`, `g=-Delta p=|S|^2-|omega|^2/2`, `M=S^2+Omega^2`, and `R=M+Hess p=-(D_tS-nu Delta S)`.
For nonzero output `q`, `e=q/|q|`, Piola gives the Householder reflection

`Rhat(q)=Mhat(q)-2<Mhat(q),e tensor e>_F e tensor e`,
`|Rhat(q)|_F=|Mhat(q)|_F`.    (14.1)

Equivalently,

`2||D_tS-nu Delta S||_2^2=||S omega||_2^2+||Delta p||_2^2`.    (14.2)

Pressure redistributes the geometry of the same state; it does not mint kinetic-energy supply or a second acceleration magnitude.

## 15. Dangerous `B/O` atomic geometry survives inside the new full-state spine — EXACT

For a true far-UV low-donor triad with opposite-helicity high roots, the low root is the signed middle root, both high roots are recipients, `Z_tau>0`, every radial-cut flux of that triad is nonnegative, and the critical production is positive minority-helicity `B_crit` work.

If the high pair has the same helicity, the radial profile is a loop with a farther high donor and critical production zero or negative.  Therefore a true `O` atom whose recipient is radially outermost in its triad lies on the opposite-high positive-critical `B_crit` arch.

The triad picture explains microscopic incidence.  Sections 6--12 are stronger for the final frontier because they survive full convolution summation.

## 16. Full geometric pair and reality-companion leak — EXACT / EXACT ALGEBRAIC

A selected helical atom is not the full pair.  For divergence-free full coefficients `U=uhat(p)`, `V=uhat(q)`, `K=p+q`, the pair-plane calculation gives

`|N_K^(p,q)|^2=|p x q|^2[|BC+DA|^2+((|q|^2-|p|^2)^2/|K|^2)|BD|^2]`.    (16.1)

For unequal parent radii, pair silence is exactly common-normal shear.  Equal radii have the wider exact phase-null manifold `BC+DA=0`; therefore helical-atom nonzero/silent statements do not automatically lift to the full mixed-polarization pair.

For a nondegenerate closed geometric triad with all three coefficients active, any nonzero internal full pair acceleration forces, by reality, a nonzero companion pair at some difference output `k_i-k_j` with radius strictly larger than every triad root.  There is no uniform multiplicative jump.

A real one-triad finite-Fourier state can close only by becoming nonlinear-silent.  The terminal class includes common-normal planar shear and monochromatic `2D3C` states, with Beltrami only a subfamily.  Under viscosity these are regular heat-decaying terminal physics.

## 17. Heat fibers and pair-source repair locate the remaining microscopic freedom — EXACT / EXACT ANALYTIC

For a fixed child `K`, a parent pair `p+q=K` has physical heat rate
`kappa=|p|^2+|q|^2`.
Along the frozen true heat orbit, the child source is the vector Laplace transform

`N_K[e^(nu tau Delta)u]=int exp(-nu kappa tau)dmu_K(kappa)`.    (17.1)

Under finite-variation integrability, interval vanishing implies by Laplace uniqueness that every heat-fiber resultant vanishes separately.  Thus passive cancellation across distinct heat rates cannot persist; actual parent dynamics must repair it.

For a helical pair source `F_e=C_e a_p a_q`, on active parents
`r_k=dot a_k/a_k`, exact differentiation gives

`dot F_e=(r_p+r_q)F_e`.    (17.2)

Minimal persistent cancellation synchronizes the relevant pair-rate sums.  Unequal-heat synchronization requires genuine nonlinear radial parent work to compensate the viscous heat mismatch; only same-heat cancellation can remain purely phase/polarization-driven.

With `eta_k=n_k/a_k`, `h_k=(F_N)_k`,

`dot eta_k=h_k/a_k-eta_k^2`.    (17.3)

So all non-affine repair returns to the genuine `F_N/G` dynamics.  In the mother-law organization, this microscopic freedom belongs to the exact remainder `N_perp` and to the higher work curvature controlled by `F_N`; it is not a parallel source road.

## 18. Affine synchronization is regular terminal physics — EXACT CONDITIONAL RIGIDITY

Under the explicit additional hypothesis that overlapping cancellation circuits force one affine logarithmic law on a connected active set,

`r_(k,s)=sigma(t)+i v(t).k`,

the true field has fixed Fourier shape up to amplitude and translation.  Viscous NS then forces all active modes to one radius and all nonlinear modal works to vanish.  On a torus this is a smooth monochromatic translating/decaying relative equilibrium; in finite-energy `R^3`, exact nonzero `L^2` support on one sphere is impossible, so the synchronized state is trivial.

This theorem does **not** assert that a general continuum same-heat cancellation web synchronizes affinely.

## 19. What the new organization has actually removed

The frontier no longer treats the following as independent mechanisms:

- critical action versus kinetic boundary work: they are layer-cake/action readings of the mother law;
- critical production versus vortex stretching: they are height/area readings of the same signed-curl action profile;
- radial traffic versus signed-curl traffic: the former is the exact fold of the latter;
- `G` versus nonlinear velocity acceleration: `G=curl N`;
- viscous preparation versus its product commutator: two readings of the same viscosity/state interaction;
- pair-cancellation repair versus a new source: all repair is realized by actual `N/G/F_N`;
- a generic “critical donor network” after full convolution: positive criticality already forces a kinetic-neutral, helicity-hardening single-helicity tail on smooth `R^3`.

The phase/polarization loophole has not disappeared.  It has been isolated into the moment-orthogonal remainder `N_perp`, the higher-shape component `Z`, and the true `F_N` evolution needed to regenerate the forced radial sorter.

## 20. Exact surviving frontier — OPEN
The endpoint block is now organized by one fixed radial control-volume family.  No new owner, clock, genealogy, Hahn split, or estimate-defined mechanism is introduced below.  Every set is frozen at the physical time where its identity is read.
### 20.1 Folded radial state/action family — EXACT
Push modal energy and the one actual signed modal-work law under `rho=|k|` to `dE_rho` and `dW_rho`.  Define
`J(R,t):=int_(rho>R)dW_rho = F(R,t)-F(-R,t)`,
`K_rad(R,t):=int (rho-R)_+ dE_rho`,
`Psi_rad(R,t):=int (rho-R)_+ dW_rho=int_R^infinity J(b,t)db=Psi(R,t)+Psi(-R,t)`.    (20.1)
The last equality uses only the exact affine invariants `int dW=0` and `int x dW=0`; the fold does not discard helicity arbitrarily.  Distributionally,
`partial_R K_rad=-E_(>R)`, `partial_R^2K_rad=dE_rho`,
`partial_R Psi_rad=-J`, `partial_R^2Psi_rad=dW_rho`.    (20.2)
Integrating the exact tail Kirchhoff law over the nested family gives
`partial_t K_rad + 2nu L_rad = Psi_rad`,
`L_rad(R,t):=int rho^2(rho-R)_+dE_rho >=0`.    (20.3)
The genuine viscous term is itself an exact Volterra reading of the state hinge,
`L_rad=R^2K_rad+4R int_R^infinity K_rad(b)db+6 int_R^infinity(b-R)K_rad(b)db`.    (20.4)
The folded mother-law action is
`A_rad(R,t):=A(R,t)+A(-R,t)=2nu Psi_rad`
`=2nu partial_tK_rad+4nu^2L_rad`.    (20.5)
At the origin,
`K_rad(0)=||u||_Hdot^(1/2)^2`, `Psi_rad(0)=P_(1/2)^NL`, `int_0^infinity Psi_rad(R)dR=Q`.    (20.6)
Thus `B_crit`, radial `O`, sidecar stock and viscosity are not independent mechanisms here: they are height/slope/state/viscous readings of one exact family.
### 20.2 Endpoint hard states force one fixed unbounded hinge front — EXACT
If a hard shell satisfies `M E_M(t)>=c`, then at `R=M/4`,
`K_rad(R,t)>= (M/4)E_M(t)>=c/4`.    (20.7)
Fix once and for all any observer level `0<kappa<c/4`.  Whenever `K_rad(0,t)>kappa`, strict monotonicity at the positive level,
`partial_RK_rad(R,t)=-E_(>R)(t)<0`,
defines a unique reader front `R_kappa(t)` by
`K_rad(R_kappa(t),t)=kappa`.    (20.8)
The endpoint hard-shell sequence therefore forces
`limsup_(t->T_*) R_kappa(t)=infinity`.    (20.9)
Differentiating the level identity gives the exact moving-reader law
`R_kappa' E_(>R_kappa)=partial_tK_rad(R_kappa)`
`=Psi_rad(R_kappa)-2nu L_rad(R_kappa)`
`=int_(R_kappa)^infinity g_tail(b,t)db`,    (20.10)
where
`g_tail(R,t):=partial_tE_(>R)=J(R,t)-2nu D_(2,>R)(t)`,
`D_(2,>R):=int_(rho>R)rho^2dE_rho`.    (20.11)
The front is an observer, not an event.  Since it has unbounded UV excursions on a finite interval, there are arbitrarily late, arbitrarily large outward states `R_kappa'>0`.  At every such actual state,
`Psi_rad(R_kappa)>2nu L_rad(R_kappa)>=2nu R_kappa^2 kappa`.    (20.12)
No Sard selection or first-contact clock is needed in the canonical endpoint spine.
### 20.3 The fixed hinge carries a genuine finite viscous resource — EXACT
At `K_rad(R_kappa)=kappa`, the elementary identity
`rho^2=4R_kappa(rho-R_kappa)+(rho-2R_kappa)^2`
gives
`D_(2,>R_kappa)=4R_kappa kappa+int_(rho>R_kappa)(rho-2R_kappa)^2dE_rho`.    (20.13)
Put `E_*:=E_(>R_kappa)`, `D_(1,>R_kappa):=int_(rho>R_kappa)rho dE_rho`,
`mu_*:=D_(1,>R_kappa)/E_*=R_kappa+kappa/E_*`,
`S_*:=int_(rho>R_kappa)(rho-mu_*)^2dE_rho`.
Then
`int_(rho>R_kappa)(rho-2R_kappa)^2dE_rho`
`=S_*+(kappa-R_kappa E_*)^2/E_*`.    (20.14)
Hence the global kinetic-energy law yields, on every interval where the front is defined,
`8nu kappa int R_kappa(t)dt`
`+2nu int int_(rho>R_kappa(t))(rho-2R_kappa(t))^2dE_rho dt <= E_total(t_0)-E_total(t_1) <= E_total(0)`.    (20.15)
This is a true viscosity budget in physical units.  The excess is actual radial variance plus actual tail-energy mismatch; it is not a concentration wallet.  It does not by itself rule out unbounded `limsup R_kappa`, because UV excursions may be `L^1_t`-thin.
### 20.4 Flux-level cells absorb radial `O` — EXACT
For any `lambda>=0`, let
`C^J_lambda:={R>0:J(R)>lambda}`
and let `P^J_lambda` be the corresponding actual radial Fourier set.  Each connected component has equal flux on its two faces, so Stieltjes accounting gives
`W^J_lambda:=2<P^J_lambda u,P^J_lambda N>=0`,    (20.16)
while
`H^J_lambda:=2<Lambda P^J_lambda u,P^J_lambda N>`
`=int_0^infinity (J(R)-lambda)_+dR>0` whenever the set is nonempty.    (20.17)
More generally, if `I=(a,b)` is a component of `{J>0}`, then for every absolutely continuous radial reader `f`,
`int_I f(rho)dW_rho=int_a^b f'(R)J(R)dR`.    (20.18)
Thus every increasing radial observable is nonlinearly hardened on the work-neutral cell.  Every true positive radial `O` through an internal cut is therefore internal circulation of a larger equal-flux neutral control volume.  `O` remains real boundary work through the smaller cut, but it is no longer an independent dynamical road once the full family is observed.
### 20.5 Growth-level cells absorb stock/viscosity/outflow after full NS — EXACT
At any fixed smooth time and any `lambda>0`, put
`C^g_lambda:={R>0:g_tail(R)>lambda}`
and let `P^g_lambda` be the corresponding actual radial mode set.  Since every component has equal `g_tail=lambda` on its two faces,
`d/dt ||P^g_lambda u||_2^2=0`.    (20.19)
For every absolutely continuous radial reader `f`,
`d/dt int_(C^g_lambda) f(rho)dE_rho`
`=int_0^infinity f'(R)(g_tail(R)-lambda)_+dR`.    (20.20)
Thus every positive tail-stock-growth region lies inside an actual stationary-stock control volume that hardens every increasing radial observable under the **full** Navier--Stokes evolution.  The selection-free multiplier form is
`int q^g_lambda dE_t=0`,
`int rho q^g_lambda dE_t=(1/2)int (q^g_lambda(R))^2dR>0`,
`q^g_lambda:=(g_tail-lambda)_+`,    (20.21)
where `dE_t` is the actual radial state-change measure.  This is a reader of one signed state-change law, not a second Hahn split.
At every outward UV front state from (20.10), `g_tail>0` somewhere above `R=R_kappa`.  Let `I=(a,b)` be a component of `{g_tail>lambda}` containing such a point and define
`Gamma_I(r):=g_tail(r)-lambda>0`, `a<r<b`, `Gamma_I(a)=Gamma_I(b)=0`.
Then
`d/dt E_I=0`,
`d/dt <Lambda P_Iu,P_Iu>=int_a^b Gamma_I(r)dr>0`.    (20.22)
For every frozen upper suffix `I_r=(r,b)`,
`d/dt E_(I_r)=Gamma_I(r)>0`,
`W_(I_r)=2nu D_(2,I_r)+Gamma_I(r)`,    (20.23)
whereas on the whole cell `W_I=2nu D_(2,I)`.  Nonlinear work exceeds each suffix's own viscosity by exactly its actual stock growth.
The level topology gives a sharper alternative at the same outward radius `R`.  Either some positive-growth superlevel component lies wholly in `(R,infinity)`, producing a genuinely UV stationary-stock hardening cell, or no such component exists.  In the latter case any rise of `g_tail` above `R` would itself create such a component; therefore on the positive corridor up to its first zero `b_R`,
`g_tail` is nonincreasing, hence `dE_t=-dg_tail>=0`,
`dW_rho=dE_t+2nu rho^2dE_rho >=2nu rho^2dE_rho`.    (20.24)
So the no-cell alternative is a one-sided UV state-growth corridor in which every radial subannulus gains actual stock under full NS.  No temporal ancestry is asserted.
### 20.6 The growth family reconstructs the radial state velocity — EXACT
Freeze one growth cell `I` and put `U=P_Iu`.  Define
`dE_I(B):=||1_B(Lambda)U||_2^2`,
`dE_(t,I)(B):=2 Re<1_B(Lambda)U,1_B(Lambda)U_t>`.
Then `dE_(t,I)<<dE_I`, so there is a unique real `h_t in L^2(dE_I)` with
`dE_(t,I)=h_t dE_I`,
`2 Re<f(Lambda)U,U_t>=int f h_t dE_I`.    (20.25)
The nested suffix family gives
`Gamma_I(r)=int_(r<rho<b) h_t(rho)dE_I(rho)`.    (20.26)
Hence
`(U_t)_rad=(1/2)h_t(Lambda)U`,
`(U_t)_fib:=U_t-(U_t)_rad`,
`Re<f(Lambda)U,(U_t)_fib>=0` for every real radial `f`.    (20.27)
Because `P_IN=P_Iu_t+nu Lambda^2U`, the radial nonlinear-work density is exactly
`h_N(rho)=h_t(rho)+2nu rho^2`,
and `(P_IN)_fib=(U_t)_fib`.    (20.28)
Thus no hidden radial regeneration freedom remains at that instant: radial state motion is `h_t`, viscosity is the explicit `2nu rho^2` shift, and the only unseen instantaneous freedom is fiber-tangent state motion.
### 20.7 Quadratic state-growth profile and the Sobolev sign pivot — EXACT
Let
`Theta_I(r):=int_r^b Gamma_I(s)ds=d/dt int_I(rho-r)_+dE_rho`
and `q_(I,r):=1_I(Lambda)(Lambda-r)_+`.  The mother law gives
`B_I(r):=||q_(I,r)^(1/2)Lambda^-1P_IN||^2`
`-||q_(I,r)^(1/2)Lambda^-1P_Iu_t||^2`
`-nu^2||q_(I,r)^(1/2)Lambda U||^2=nu Theta_I(r)`.    (20.29)
Distributionally,
`partial_r B_I=-nu Gamma_I<0`, `partial_r^2B_I=nu dE_(t,I)`.    (20.30)
The negative viscous sign is correct because this profile reads **state growth after viscosity**, whereas `A=2nu Psi` reads nonlinear work before viscosity.  Height/slope/curvature now recover hinge-stock growth / suffix-stock growth / actual radial state change.
For every nonnegative absolutely continuous radial weight `f`,
`||f(Lambda)^(1/2)P_IN||^2-||f(Lambda)^(1/2)P_Iu_t||^2`
`-nu^2||f(Lambda)^(1/2)Lambda^2U||^2`
`=nu int_a^b (rho^2f(rho))' Gamma_I(rho)d rho`.    (20.31)
Since `0<a<b<infinity`, all Sobolev weights are admissible on the frozen cell.  For every real `sigma`,
`||Lambda^sigma P_IN||^2-||Lambda^sigma P_Iu_t||^2-nu^2||Lambda^(sigma+2)U||^2`
`=2nu(sigma+1)int_a^b r^(2sigma+1)Gamma_I(r)dr`.    (20.32)
Thus the complete Sobolev force-triangle family changes sign **exactly** at `sigma=-1`: positive for `sigma>-1`, zero at `-1`, negative for `sigma<-1`.  These are Mellin readings of one state-growth profile, not separate norm mechanisms.
### 20.8 Maximal work/state decomposition and exact tangent cancellation — EXACT
The older two-moment remainder can be refined by the whole radial family.  For any frozen actual set `P`, with `U=Pu`, `n=PN`, define radial state/work measures
`dE_U(B)=||1_B(Lambda)U||^2`,
`dW_U(B)=2 Re<1_B(Lambda)U,1_B(Lambda)n>`.
Then `dW_U<<dE_U`, so `dW_U=h_U dE_U` and
`N_rad=(1/2)h_U(Lambda)U`, `N_fib=n-N_rad`,
`Re<f(Lambda)U,N_fib>=0` for all real radial `f`.    (20.33)
On a work-neutral first-moment-positive cell, the old sorter is the affine projection of `h_U`; the remaining radial work shape is still determined by `dW_U`, while only `N_fib` is radial-work invisible.  Since viscosity belongs to the radial cyclic subspace,
`N_fib=(U_t)_fib`.    (20.34)
Taking the observer all the way to physical Fourier/helicity mode space, let `dE(m)=|u_m|^2dm`, `dW(m)=T_mdm`.  On occupied modes,
`N_work,m=(1/2)(dW/dE)(m)u_m`,
`N_tan:=N-N_work`, `Re(conj(u_m)N_tan,m)=0`,
`(N_tan)_m=(u_t)_tan,m`.    (20.35)
Thus the maximal observer removes every possible **instantaneous hidden kinetic-work mechanism**: the work-aligned acceleration is reconstructed by the one actual work law; the remainder is true state rotation/zero-stock acceleration.
Its next-jet role is also exact.  On an occupied scalar helical mode write
`eta_m:=N_m/u_m=alpha_m+i gamma_m`.
Because `F_N=(partial_t+nu Lambda^2)N` and `N=(partial_t+nu Lambda^2)u`,
`(F_N)_m/u_m=dot eta_m+eta_m^2`.    (20.36)
Therefore
`|N_m|^2/|u_m|^2=alpha_m^2+gamma_m^2`,
`Re(conj(u_m)(F_N)_m)/|u_m|^2=dot alpha_m+alpha_m^2-gamma_m^2`,
so
`|N_m|^2+Re(conj(u_m)(F_N)_m)=|u_m|^2(dot alpha_m+2alpha_m^2)`.    (20.37)
The tangent square cancels exactly.  Equivalently, with `e_m=|u_m|^2`,
`T_m=(partial_t+2nu rho^2)e_m`,
`(partial_t+2nu rho^2)^2e_m=2|N_m|^2+2Re(conj(u_m)(F_N)_m)`.    (20.38)
Thus neither `N_tan` nor the matching `F_N` term is a separate phase-repair cost.  Relative phase still matters because the present stock/work quotient does not determine the next amplitude jet; once the true next jet is retained, there is no parallel tangent mechanism.
### 20.9 True radial-flux curvature remains a full-state law — EXACT
Let
`N2_>(R):=int_(rho>R)|Nhat|^2`,
`R_N,>(R):=int_(rho>R)Re(conj(uhat)(F_N)hat)`.
Folding the fixed-mode work-curvature law gives
`partial_tJ(R)+2nu R^2J(R)+4nu int_R^infinity rJ(r)dr`
`=2N2_>(R)+2R_N,>(R)`.    (20.39)
At `R=0`,
`<u,F_N>=2nu Q-||N||_2^2`.    (20.40)
When the indicated integrals are finite, or after compact radial localization and passage to the limit,
`(1/2)d/dt int_0^infinity R J(R)^2dR`
`+2nu int_0^infinity R^3J(R)^2dR+2nu Q^2`
`=2int_0^infinity R J(R)[N2_>(R)+R_N,>(R)]dR`.    (20.41)
The `2nu Q^2` term is genuine viscosity in this reader.  Equation (20.41) is not a new finite budget: the RHS contains the true full-state curvature and may diverge at a singular endpoint.
### 20.10 Observer-neutralization stops here; the mother law gives a dual growth action — EXACT
There is a useful methodological stopping theorem.  Let `dmu` be any finite signed radial measure and `G(R):=dmu((R,infinity))`.  If `I=(a,b)` is a component of `{G>lambda}` with equal endpoint value `lambda`, then
`dmu(I)=0`,
`int_I f(rho)dmu=int_a^b f'(R)(G(R)-lambda)dR`    (20.42)
for every absolutely continuous reader `f`.  Thus the superlevel-neutral-cell construction is **observer calculus**, not a new Navier--Stokes mechanism.  It applies equally to `dW`, `dE_t`, `dE_tt`, and higher signed jets.  In particular, merely replacing `g_tail` by `partial_t g_tail` and repeating Section 20.5 would add no physics.
The genuine NS content is the mother law.  For every frozen nonnegative radial weight `w`, define its force-triangle defect
`Delta[w]:=||w(Lambda)^(1/2)N||_2^2-||w(Lambda)^(1/2)u_t||_2^2-nu^2||w(Lambda)^(1/2)Lambda^2u||_2^2`.
Then directly from `N=u_t+nu Lambda^2u`,
`Delta[w]=nu int_0^infinity rho^2 w(rho)dE_t(rho)`.    (20.43)
This is one identity; all state-growth force triangles are readers of it.
Write `g:=g_tail`, `Xi(R,t):=partial_tK_rad(R,t)=int_R^infinity g(b,t)db`, so `Xi'=-g` and `dE_t=partial_R^2Xi=-dg`.  Since `g(0)=-2nu||Lambda u||_2^2<0` and `g(infinity)=0`, for every `p>1` and every radial exponent `beta` for which the boundary terms vanish,
`Delta[rho^beta g_+^(p-1)]`
`=nu(beta+2)/p int_0^infinity rho^(beta+1)g_+(rho)^p d rho`.    (20.44)
The sign pivot `beta=-2` is the same mother-law homogeneity already seen at Sobolev `sigma=-1`, not a new criterion.  In particular,
`Delta[rho g_+]=(3nu/2)int_0^infinity rho^2g_+(rho)^2d rho >=0`.    (20.45)
The one-hinge-higher reader has the opposite exact sign.  Taking the frozen weight `w=Xi_+/rho^2` in (20.43) and integrating the Stieltjes derivative once gives
`Delta[Xi_+/rho^2]`
`=nu Xi_+(0)g(0)-nu int_{Xi>0}g(R)^2dR <=0`.    (20.46)
If `Xi(0)<=0`, the RHS is exactly `-nu int_{Xi>0}g^2`.  Thus positive tail-stock growth and positive hinge-stock growth are not two mechanisms: the same mother triangle reads the former as a positive growth action and the latter as a negative square.  The weights are observers; `g`, `Xi`, `dE_t`, and the force fields are the true state objects.
### 20.11 Thin UV excursions force scale-amplified true growth; zero stock is a crossing, not a birth mechanism — EXACT
Extend the reader front by `R_kappa(t)=0` when `K_rad(0,t)<=kappa` and put `Omega_kappa:={(R,t):K_rad(R,t)>kappa}`.  Exact layer cake and the physical energy law give
`|Omega_kappa|=int R_kappa(t)dt <= E_total(0)/(8nu kappa)`.    (20.47)
At a positive front radius put `E:=E_(>R_kappa)`, `D_j:=D_(j,>R_kappa)` and `S_*:=int_(rho>R_kappa)(rho-D_1/E)^2dE_rho`.  Since `D_1=R_kappa E+kappa`,
`E D_2=(R_kappa E+kappa)^2+E S_*`.    (20.48)
At every outward state `Xi(R_kappa)=R_kappa'E`, hence
`Xi(R_kappa)D_2=R_kappa'[(R_kappa E+kappa)^2+ES_*] >= kappa^2R_kappa'`.    (20.49)
Because `2nu int D_2dt<=E_total(0)`, every absolutely continuous increasing unbounded reader `Phi` with `Phi'>=0` satisfies
`limsup_(outward,t->T_*) Phi'(R_kappa(t)) Xi(R_kappa(t),t)=infinity`.    (20.50)
Otherwise the positive variation of the unbounded function `Phi(R_kappa)` would be bounded by `kappa^-2 sup(Phi'Xi) int D_2dt`.  Thus not only `Xi` but, e.g., `Xi/(1+R_kappa)` is cofinally unbounded (`Phi=log(1+R)`).
For every `beta>0`, Cauchy on `Xi(R)<=int_R^infinity g_+` and (20.44) give the scale-sharp family
`Delta[rho^beta g_+] >= [nu beta(beta+2)/2] R^beta Xi(R)^2` whenever `Xi(R)>0`.    (20.51)
Hence finite-area escape forces arbitrarily large true mother-law growth action at arbitrarily large scale; thinness is only observer geometry.
On maximal Fourier/helicity mode space let `e_m=|u_m|^2`, `T_m=2Re(conj(u_m)N_m)`, `O={e_m>0}`, `Z={e_m=0}`, `h_t=dot e/e` and `h_N=T/e=h_t+2nu rho^2` on `O`.  Define the positive **zero-stock curvature measure**
`dZ_0(m):=2 1_Z(m)|N_m|^2dm`.
Then
`dE_tt=(dot h_t+h_t^2)dE+dZ_0`,
`[2|N|^2+2Re(conj(u)F_N)]dm=(dot h_N+h_N^2)dE+dZ_0`.    (20.52)
The tangent variable is absent.  The true work-rate measure
`d dot W:=dE_tt+2nu rho^2dE_t`
obeys `int d dot W=0`, `int x d dot W=0`, and `d dot W=dZ_0` on `Z`.    (20.53)
For a fixed modal control volume with `Pu(t_0)=0`,
`E_P'(t_0)=0`, `E_P''(t_0)=2||PN(t_0)||_2^2`, `E_P(t_0+h)=h^2||PN(t_0)||_2^2+o(h^2)`.    (20.54)
If `t_0` is an interior time and `PN(t_0)!=0`, this is a two-sided strict quadratic minimum: an actual zero crossing/reappearance, **not** one-sided creation from nothing.  Its curvature is owned by existing `N` stock and is compensated by occupied work-rate through (20.53).
### 20.12 One Volterra heat-square family collapses the remaining second-stock mechanisms — EXACT
The instantaneous tail law itself already has core-style accounting.  Since `g=J-2nu D_(2,>R)`,
`int_0^infinity R^2g_+(R)J(R)dR=int R^2g_+^2dR+2nu int R^2g_+(R)D_(2,>R)dR`.    (20.55)
The left side is actual nonlinear boundary work read by the positive-growth family; the two right terms are the positive stock-growth square and the genuine viscous tail payment.  No second source has appeared.
More generally define the exact heat-tail operator and first-moment tail
`(L_tail h)(R):=R^2h(R)+2int_R^infinity r h(r)dr`, `M_h(R):=int_R^infinity r h(r)dr`.
For every decaying signed tail `h` and every `alpha>1` (or after compact radial localization), integration by parts gives the positive Green identity
`int R^alpha h L_tail h = int R^(alpha+2)h^2 +(alpha-1)int R^(alpha-2)M_h^2`.    (20.56)
At `alpha=1` the last term is replaced by the boundary square `M_h(0)^2`.  Thus if the **true** tail object satisfies `h_t+2nu L_tail h=S`, then
`(1/2)d/dt int R^alpha h^2 +2nu int R^(alpha+2)h^2+2nu(alpha-1)int R^(alpha-2)M_h^2=int R^alpha hS`    (20.57)
for `alpha>1`, with the stated `alpha=1` boundary replacement.  This is an observer-square identity generated exactly by physical viscosity, not a new kinetic energy.
The two true tails already present obey the same operator law:
`g_t+2nu L_tail g=J_t`,
`J_t+2nu L_tail J=2C`, `C(R):=N2_>(R)+R_N,>(R)`.    (20.58)
At the decisive `alpha=2`, therefore,
`(1/2)d/dt int R^2g^2+2nu int R^4g^2+2nu int M_g^2=int R^2g J_t`,
`(1/2)d/dt int R^2J^2+2nu int R^4J^2+2nu int M_J^2=2int R^2J C`.    (20.59)
The `alpha=1` member of the second line is exactly (20.41), because `M_J(0)=Q`; (20.41) was one member of this family, not an isolated mechanism.
Put `G_2=(1/2)int R^2g^2`, `J_2=(1/2)int R^2J^2`.  Since `A_g=(3nu/2)int R^2g_+^2` and `J>=g>0` wherever `g>0`,
`G_2>=A_g/(3nu)`, `J_2>=A_g/(3nu)`.    (20.60)
More generally, matching `alpha=beta+1` in (20.57) to the mother reader (20.44), for every `beta>0`
`G_(beta+1),J_(beta+1) >= Delta[rho^beta g_+]/[nu(beta+2)] >= (beta/2)R^beta Xi(R)^2`,
where `G_alpha=(1/2)int R^alpha g^2`, `J_alpha=(1/2)int R^alpha J^2`.  Thus every member is one Mellin reading of the same state/work family, not a new criterion.  In particular fixed-front escape forces `limsup G_2=limsup J_2=infinity`; (20.50) with `Phi=log(1+R)` gives `limsup_(outward) G_2/R_kappa^3=limsup_(outward) J_2/R_kappa^3=infinity`.
Integrating the matched balances from any fixed smooth `s<T_*` gives, for every `beta>0`, the necessary endpoint divergence
`sup_(t<T_*) int_s^t int R^(beta+1)g J_t dRdt=infinity`,
`sup_(t<T_*) 2int_s^t int R^(beta+1)J(R)C(R)dRdt=infinity`.    (20.61)
Thus the old “occupied curvature versus zero-stock birth” dichotomy is not a dynamical fork.  All second-stock behavior first collapses into actual work-rate `J_t`, then into the single true `N/F_N` curvature tail `C`; by (13.4)--(13.5) its nonlinear internal-tail part cancels and the surviving cross-volume part is antisymmetric curvature transfer; only the known viscous commutator has nonzero global sum.
The observer families themselves contain no extra state.  If `R_kappa(t)` denotes the inverse hinge level for `0<kappa<K_rad(0,t)`, then for every `p>=0`
`int_0^(K_rad(0,t)) R_kappa(t)^p d kappa = [1/(p+1)]int rho^(p+1)dE_rho`; in particular `int R_kappa d kappa=D_2/2`.    (20.62)
Likewise, because `int dW_rho=0`, for every `alpha>-1` with the indicated moment finite,
`J_alpha=-(1/[4(alpha+1)]) int int |rho^(alpha+1)-sigma^(alpha+1)| dW_rho dW_sigma`.    (20.63)
The exact integrated `J`-balance, for `alpha>1`, is therefore
`J_alpha(t)+2nu int_s^t[int R^(alpha+2)J^2 +(alpha-1)int R^(alpha-2)M_J^2]dtau = J_alpha(s)+2int_s^t int R^alpha J C dRdtau`.    (20.64)
This is the precise second-level analogue of control-volume bookkeeping: `J_alpha` is a quadratic reader of the one actual boundary-work law, the positive left terms are heat-generated reader payments, and the right side is the true `N/F_N` curvature input.  The moving-front family is likewise only inverse coordinates for actual stock moments by (20.62).  None of these readers is a new kinetic owner or resource.
### 20.13 Summing the entire physical cut family gives one multiplier commutator — EXACT
Let `H_R=1_(Lambda>R)`, `L_R=I-H_R` and `Q_R:=<Lambda H_Ru,Lambda H_RN>`.  Comparing fixed-set work curvature with (20.58) gives the exact owner of the Volterra heat term,
`L_tail J(R)=2Q_R`.    (20.65)
For every real absolutely continuous radial multiplier `phi` with `phi(0)=0` (first compactly localized if needed), layer cake gives
`W_phi:=int phi'(R)J(R)dR=2<phi(Lambda)u,N>`,
`Q_phi:=int phi'(R)Q_RdR=<phi(Lambda)Lambda u,Lambda N>`,
`C_phi:=int phi'(R)C(R)dR=<phi(Lambda)N,N>+<phi(Lambda)u,F_N>`.    (20.66)
Let `T_R` denote the three nonlinear cross-volume terms in (13.4) and `V_R:=sum_j<H_Ru,partial_j u x partial_j omega>`.  Then
`C_phi=T_phi-2nu V_phi`, `0.5 dot W_phi=T_phi-2nu(V_phi+Q_phi)`,    (20.67)
for time-independent `phi`, where `T_phi=int phi'T_R`, `V_phi=int phi'V_R`.  Thus summing cuts creates no source.
Define the slot commutator
`D_phi(a,b;c):=<phi(Lambda)a,b x c>-<a,phi(Lambda)b x c>`.
Exact complement cancellation yields
`T_phi=D_phi(N,u;omega)+(1/2)D_phi(u,u;G)`.    (20.68)
If `phi(Lambda)` has an even kernel `K_phi`, then
`D_phi(a,b;c)=int int K_phi(x-y)a(x).[b(y)x(c(y)-c(x))]dxdy`.    (20.69)
So the summed nonlinear curvature is a full-field increment commutator, not a traffic token or internal UV engine.
For `alpha>1` define the adaptive **reader** `phi_(alpha,J)(rho):=2int_0^rho R^alpha J(R)dR`.  At each frozen time,
`W_(phi_(alpha,J))=4J_alpha`,
`Q_(phi_(alpha,J))=int R^alpha J L_tail J=int R^(alpha+2)J^2+(alpha-1)int R^(alpha-2)M_J^2>=0`,
`dot J_alpha=T_(phi_(alpha,J))-2nu[V_(phi_(alpha,J))+Q_(phi_(alpha,J))]`.    (20.70)
The last line is simply the family sum of the antisymmetric `0.5 dot W_(H_R)` law with weight `2R^alpha J`; even the adaptive observer contributes no extra mechanism.  The inviscid part has no universal sign (finite-Fourier states realize both signs).
### 20.14 The whole hinge-front family forces a critical forcing burden, and also shows the observer barrier — EXACT / EXACT ANALYTIC
Fix `0<kappa_0<kappa_1<c/4`.  Every `R_kappa`, `kappa in[kappa_0,kappa_1]`, has unbounded endpoint limsup.  If `w>=0` has unbounded primitive `Phi(R)=int_0^R w`, Tonelli plus the exact change of variables `d kappa=-E_(>R)dR` and `R_kappa'E_(>R_kappa)=Xi(R_kappa)` gives
`int_(kappa_0)^(kappa_1) int w(R_kappa)(R_kappa')_+ dt d kappa`
`=int int_(R_(kappa_1)(t))^(R_(kappa_0)(t)) w(R)Xi_+(R,t)dRdt=infinity`.    (20.71)
This is family coarea for observer motion; the middle integrand is the actual hinge-stock rate.
With `q_R=(Lambda-R)_+`, mother law gives
`Xi=2<q_Ru,N>-2nu||q_R^(1/2)Lambda u||^2 <= B_R/(2nu)`,
`B_R:=||q_R^(1/2)Lambda^-1N||^2`.    (20.72)
Hence for every `0<=epsilon<1`,
`int_0^infinity R^(-epsilon)B_RdR=||Lambda^(-epsilon/2)N||^2/[(1-epsilon)(2-epsilon)]`,
so finite-endpoint recycling forces
`int_0^(T_*)||Lambda^(-epsilon/2)N||_2^2dt=infinity`.    (20.73)
At the endpoint reader `w(R)=(1+R)^-1`, the forced multiplier is explicitly
`m_log(rho)=[(rho+1)log(1+rho)-rho]/rho^2 ~ log(rho)/rho`,
and `int_0^(T_*)||m_log(Lambda)^(1/2)N||_2^2dt=infinity`.    (20.74)
More generally the forcing multiplier produced by `w` is
`m_w(rho):=rho^-2 int_0^rho w(R)(rho-R)dR >= Phi(rho/2)/(2rho)`.    (20.75)
Thus any observer weight capable of seeing an unbounded front necessarily demands at least an `H^-1/2`-scale forcing action with an unbounded slowly varying strengthening.  By contrast the standard energy-class estimate is only
`||N||_Hdot^-1 <= C||u||_2^(1/2)||grad u||_2^(3/2)`, hence `int_0^(T_*)||N||_Hdot^-1^(4/3)dt <= C E_*^(1/3)int||grad u||_2^2dt<infinity`.    (20.76)
So no unbounded observer primitive can weaken (20.71)--(20.75) to the spatial `H^-1` / time-`L^(4/3)` level already funded by kinetic energy.  The remaining closure must use the actual convolution/full-field structure in (20.68), not another front or norm mechanism.
### 20.15 Exact remaining theorem — OPEN
The surviving theorem is still:
> **No infinite critical full-state recycling.** A smooth true 3D incompressible Navier--Stokes trajectory on a finite interval cannot have one fixed positive hinge level `K_rad(R_kappa,t)=kappa` make unbounded UV excursions while the same true fields satisfy the mother force triangle, folded radial state/action law, genuine viscous front budget, growth family, tangent cancellation, the scale-amplified front law (20.47)--(20.54), the Volterra heat-square family (20.55)--(20.61), the observer-exhaustion/integrated accounting identities (20.62)--(20.64), the summed-family/full-field identities (20.65)--(20.76), and all full-pair/heat-fiber identities.
Equivalently: `Y=>bot`.
The sharpened chain is
`fixed unbounded K_rad=kappa front`
`=>` cofinal scale-amplified true `Xi` and mother growth action
`=>` blow-up of both tail-growth square `G_2` and actual boundary-work square `J_2`
`=>` infinite cumulative actual work-rate input and `N/F_N` curvature input
`=>` the whole `kappa` family simultaneously forces critical-plus `N` forcing action divergence
`=>` by (20.68) and (13.4)--(13.7), no internal UV nonlinear curvature owner remains: the required evolution is one full-field slot commutator / complementary work-rate transfer plus known viscosity.
What is **not** proved is exactly that this final full-field commutator/work-rate transfer is incompatible with finite smooth lifespan.  No finite physical budget for the weighted curvature-transfer/viscous input on the right side of (20.61) has yet been proved; large `Q`, Lamb/source-square diagnostics, or selected pair/triad arguments do not supply one automatically.  Any closure must therefore control this true `N/G/F_N` input without inventing a clock, genealogy, Hahn law, transfer wallet, internal-UV curvature mechanism, or higher observer jet.
## 21. QED hook
Once Section 20 is proved, the existing composition is unchanged:
`T_*<infinity => X vee Y`,
`X=>bot`,
`Y=>bot`,
therefore `T_*<infinity=>bot` and `T_*=infinity`.
See `SOLUTION_MAP.md` for the short proof graph, `PHYSICAL_CORE.md` for the primitive identity/endpoint basis, and `MIXED_FRONTIER.md` for exhausted false-owner routes and the closed Clay-to-`S/V/O` upstream spine.
