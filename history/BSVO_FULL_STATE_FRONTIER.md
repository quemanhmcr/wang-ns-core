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
`W_phi:=int phi'(R)J(R)dR=2<phi(Lambda)u,N>`, `Q_phi:=int phi'(R)Q_RdR=<phi(Lambda)Lambda u,Lambda N>`, `C_phi:=int phi'(R)C(R)dR=<phi(Lambda)N,N>+<phi(Lambda)u,F_N>`.    (20.66)
Let `T_R` denote the three nonlinear cross-volume terms in (13.4) and `V_R:=sum_j<H_Ru,partial_j u x partial_j omega>`.  Then
`C_phi=T_phi-2nu V_phi`, `0.5 dot W_phi=T_phi-2nu(V_phi+Q_phi)`,    (20.67)
for time-independent `phi`, where `T_phi=int phi'T_R`, `V_phi=int phi'V_R`.  Thus summing cuts creates no source.
Define the slot commutator
`D_phi(a,b;c):=<phi(Lambda)a,b x c>-<a,phi(Lambda)b x c>`.
Exact complement cancellation yields
`T_phi=D_phi(N,u;omega)+(1/2)D_phi(u,u;G)`.    (20.68)
Already at first order `W_phi=D_phi(u,u;omega)=<u,[u.grad,phi(Lambda)]u>`; (20.68) is the full-field time jet of this same boundary-work commutator, not a new mechanism.
If `phi(Lambda)` has an even kernel `K_phi`, then
`D_phi(a,b;c)=int int K_phi(x-y)a(x).[b(y)x(c(y)-c(x))]dxdy`.    (20.69)
So the summed nonlinear curvature is a full-field increment commutator, not a traffic token or internal UV engine.
For `alpha>1` define the adaptive **reader** `phi_(alpha,J)(rho):=2int_0^rho R^alpha J(R)dR`.  At each frozen time,
`W_(phi_(alpha,J))=4J_alpha`, `Q_(phi_(alpha,J))=int R^alpha J L_tail J=int R^(alpha+2)J^2+(alpha-1)int R^(alpha-2)M_J^2>=0`, `dot J_alpha=T_(phi_(alpha,J))-2nu[V_(phi_(alpha,J))+Q_(phi_(alpha,J))]`.    (20.70)
The last line is simply the family sum of the antisymmetric `0.5 dot W_(H_R)` law with weight `2R^alpha J`; even the adaptive observer contributes no extra mechanism.  The inviscid part has no universal sign (finite-Fourier states realize both signs).
### 20.14 The whole hinge-front family forces a critical forcing burden, and also shows the observer barrier — EXACT / EXACT ANALYTIC
Fix `0<kappa_0<kappa_1<c/4`.  Every `R_kappa`, `kappa in[kappa_0,kappa_1]`, has unbounded endpoint limsup.  If `w>=0` has unbounded primitive `Phi(R)=int_0^R w`, Tonelli plus the exact change of variables `d kappa=-E_(>R)dR` and `R_kappa'E_(>R_kappa)=Xi(R_kappa)` gives
`int_(kappa_0)^(kappa_1) int w(R_kappa)(R_kappa')_+ dt d kappa=int int_(R_(kappa_1)(t))^(R_(kappa_0)(t)) w(R)Xi_+(R,t)dRdt=infinity`.    (20.71)
This is family coarea for observer motion; the middle integrand is the actual hinge-stock rate.
With `q_R=(Lambda-R)_+`, mother law gives
`Xi=2<q_Ru,N>-2nu||q_R^(1/2)Lambda u||^2 <= B_R/(2nu)`,
`B_R:=||q_R^(1/2)Lambda^-1N||^2`.    (20.72)
Hence for every `0<=epsilon<1`,
`int_0^infinity R^(-epsilon)B_RdR=||Lambda^(-epsilon/2)N||^2/[(1-epsilon)(2-epsilon)]`, so finite-endpoint recycling forces `int_0^(T_*)||Lambda^(-epsilon/2)N||_2^2dt=infinity`.    (20.73)
At the endpoint reader `w(R)=(1+R)^-1`, the forced multiplier is explicitly
`m_log(rho)=[(rho+1)log(1+rho)-rho]/rho^2 ~ log(rho)/rho`,
and `int_0^(T_*)||m_log(Lambda)^(1/2)N||_2^2dt=infinity`.    (20.74)
More generally the forcing multiplier produced by `w` is
`m_w(rho):=rho^-2 int_0^rho w(R)(rho-R)dR >= Phi(rho/2)/(2rho)`.    (20.75)
Thus any observer weight capable of seeing an unbounded front necessarily demands at least an `H^-1/2`-scale forcing action with an unbounded slowly varying strengthening.  By contrast the standard energy-class estimate is only
`||N||_Hdot^-1 <= C||u||_2^(1/2)||grad u||_2^(3/2)`, hence `int_0^(T_*)||N||_Hdot^-1^(4/3)dt <= C E_*^(1/3)int||grad u||_2^2dt<infinity`.    (20.76)
So no unbounded observer primitive can weaken (20.71)--(20.75) to the spatial `H^-1` / time-`L^(4/3)` level already funded by kinetic energy.  The remaining closure must use the actual convolution/full-field structure in (20.68), not another front or norm mechanism.
### 20.15 Full-convolution secant-defect theorem — EXACT
Put `B(a,b):=-(1/2)P[(a.grad)b+(b.grad)a]`, so `N=B(u,u)`.  Polarized Euler energy/helicity conservation are the three-slot identities `<a,B(b,c)>+<b,B(c,a)>+<c,B(a,b)>=0` and `<Ca,B(b,c)>+<Cb,B(c,a)>+<Cc,B(a,b)>=0`.    (20.77)
For child helical mode `m=(q,s)`, `y=s|q|`, write the actual unordered parent-helicity source law `N_m=sum_(e->m)f_(m,e)` and let the two parent signed curls of `e` be `x,z`.  For a scalar curl multiplier `phi`, let `ell_(x,z)phi(y)` be its secant value at `y` (Hermite tangent when `x=z`) and `d_phi(y;x,z):=phi(y)-ell_(x,z)phi(y)=(y-x)(y-z)phi[x,z,y]`.    (20.78)
Define the defect resultant `R_(phi,m):=sum_(e->m)d_phi(y;x_e,z_e)f_(m,e)`.  Then the inviscid second work jet collapses exactly to
`(1/2)dot W_(phi(C))^E=<phi(C)N,N>+2<phi(C)u,B(u,N)>=sum_m Re(conj(N_m)R_(phi,m))`.    (20.79)
Equivalently, polarizing into one complete quartet of curl eigenmodes `Ca_i=x_i a_i`, its three physical diagonals obey `Q_phi[a_1,a_2,a_3,a_4]=(1/6)sum_(ij|kl)sum_y[d_phi(y;x_i,x_j)+d_phi(y;x_k,x_l)]S_(ij|kl)^y`, where `S_(ij|kl)^y` is the pairing of the two actual helical pair-source components on that diagonal.    (20.80)
Thus affine `phi=alpha+beta x` is annihilated by the complete convolution, recovering energy/helicity without channel selection.  For the critical kink `phi(x)=|x|`, same-sign parents give `d=0` for a same-sign child and `d=2|q|` for the opposite-helicity child; for parents `(-P,+R)` and child radius `Q`, `d(+Q)=2P(Q-R)/(P+R)`, `d(-Q)=2R(Q-P)/(P+R)`.    (20.81)
Let `D_h:=<u,(Lambda-hC)u>=2||Lambda^(1/2)P_(-h)u||_2^2`.  Full NS gives `dot D_h+4nu||Lambda^(3/2)P_(-h)u||_2^2=W_Lambda`; hence at any actual pure-helicity state `u=u_h`, heat is tangent to the same sheet and `dot W_Lambda=4||Lambda^(1/2)P_(-h)N||_2^2=||Lambda^(-1/2)(G-h Lambda N)||_2^2>=0`.    (20.82)
Hence if `K=max(P,R)`, `L=min(P,R)` and the child keeps the helicity of the `K`-parent, triangle geometry gives the exact locality inequality `|d_|x||<=2L^2/(K+L)<=2L^2/K`; every unsuppressed critical defect is therefore a minority-helicity child relative to the largest parent.  Quartic complexity has collapsed to one true source resultant paired with the secant curvature of the observer multiplier; no quartet genealogy or hidden positive curvature law is introduced.
### 20.16 Heat-fiber secant Gram: only constant-defect sectors are degenerate — EXACT
Fix one child helical mode `m=(q,s)`, one physical heat `kappa`, and one parent-helicity sector on its canonical finite base fiber `(Omega,dmu)`.  Let `f(e)` be the actual child-source amplitude and `d(e)=d_phi(y;x_e,z_e)`.  Put `n_k=int f dmu`, `r_k=int d f dmu`, `v_k=(n_k,r_k)^T` and
`Gamma_k:=int_Omega (1,d)^T(1,d)dmu`.  Orthogonal projection in the **actual edge-source Hilbert space** gives
`int|f|^2dmu = v_k^* Gamma_k^dagger v_k + int|f-(c_0+c_1d)|^2dmu`, `(c_0,c_1)^T=Gamma_k^dagger v_k`.    (20.83)
Here `dagger` is the Moore--Penrose inverse, so the formula includes rank-one fibers without a case split.  Moreover
`det Gamma_k = mu(Omega)^2 Var_mu(d)`.    (20.84)
For the critical kink, same-helicity parents have the constant defects `0` and `2Q` in the majority/minority child coordinates, hence rank one.  For mixed parents `(-P,+M)` at fixed `P^2+M^2=kappa`, `d_+=2P(Q-M)/(P+M)`, `d_-=2M(Q-P)/(P+M)`; at the equator `P=M=A`, differentiation along the heat circle gives `partial_P d_+=Q/A`, `partial_P d_-=-Q/A`.  Thus every nondegenerate mixed heat fiber has `det Gamma_k>0`.  The secant moments resolve all mixed sectors exactly; the only critical Gram degeneracy is the same-helicity sector already singled out by (20.81)--(20.82).
### 20.17 Complete projective-line classification for all parent helicities — EXACT
Let `q=p+m`, `Q=|q|`, `P=|p|`, `M=|m|`, `r=p-m`, and parent helicities `a,b in {+-1}`.  On a noncollinear triad let `n` be its normal and `t_q` the in-plane unit vector orthogonal to `q`.  The full Leray **vector** source atom has projective line and geometric magnitude
`ell_(ab)=[t_q+i beta_(ab)n]`, `beta_(ab)=Q/(aP+bM)`,
`G_(ab)=|bM-aP||q x r| sqrt((aP+bM)^2+Q^2)/(4PMQ)`,    (20.85)
with `beta=infinity` interpreted projectively; the physical source magnitude is `G_(ab)|a_p a_m|`.  Hence the complete nondegenerate vector-source zero set is exactly collinear shear `q x r=0`, together with the same-helicity equal-radius Beltrami equator `a=b, P=M`.
For two source lines with parameters `(beta,n)` and `(beta',n')` and dihedral angle `psi`,
`D_proj=[(beta-beta')^2 cos^2psi +(1-beta beta')^2 sin^2psi]/[(1+beta^2)(1+beta'^2)]`.    (20.86)
Thus away from the null boundary `D_proj=0` iff either `(i) beta=beta'` and `psi=0 mod pi`, or `(ii) beta beta'=1` and `psi=pi/2 mod pi`.  On one equal-heat fiber `P^2+M^2=kappa`, same-helicity atoms obey `|beta|=Q/(P+M)<Q/sqrt(kappa)`, while mixed-helicity atoms obey `|beta|=Q/|P-M|>Q/sqrt(kappa)`.  Therefore a **distinct** aligned equal-heat pair is only
- the old same-helicity equatorial reflection doublet from case (i), or
- one same-helicity / mixed-helicity **reciprocal-beta orthogonal-plane pair** from case (ii).    (20.87)
A mixed-helicity aligned atom is otherwise unique: heat fixes `P^2+M^2`, `beta` fixes the signed difference `P-M`, and the projective line fixes the triad plane.  Consequently a generic equal-heat projective-line fiber contains at most three actual parent orbits: one same-helicity reflection doublet and one reciprocal mixed-helicity singlet.  The apparent continuum of same-line cancellation has collapsed to a finite physical fiber.
### 20.18 Reciprocal-orthogonal cancellation has unavoidable companion source — EXACT
Take a nonzero reciprocal pair from (20.87): `p+m=q` has helicities `(h,h)` and `p'+m'=q` has `(h,-h)` after the harmless unordered relabeling.  Their triad planes are orthogonal.  The four cross pairs split into the two physical companion partitions `A={(p,p'),(m,m')}` and `B={(p,m'),(m,p')}`.  Every mixed-helicity cross pair is noncollinear and therefore nonzero by (20.85).  If both companion products vanished, the same-helicity pair in `A` and the same-helicity pair in `B` would both have to be Beltrami-null, forcing `|p|=|p'|=|m|` and hence `|p|=|m|`, which would make the original `(p,m)` source zero.  Thus at least one complete companion partition has two nonzero source atoms.    (20.88)
More quantitatively, let `G_ij` denote the geometric coefficient (20.85) for the indicated pair and let `S_ij=G_ij|a_i a_j|`.  The amplitude factors cancel **exactly** in each four-mode partition:
`S_(pp')S_(mm')/[S_(pm)S_(p'm')] = G_(pp')G_(mm')/[G_(pm)G_(p'm')]`,
`S_(pm')S_(mp')/[S_(pm)S_(p'm')] = G_(pm')G_(mp')/[G_(pm)G_(p'm')]`.    (20.89)
Hence if the two aligned original atoms cancel at `q`, so `S_(pm)=S_(p'm')=:S_0`, then
`max_companion S >= chi_geom S_0`, `chi_geom:=max{sqrt(G_(pp')G_(mm')/(G_(pm)G_(p'm'))),sqrt(G_(pm')G_(mp')/(G_(pm)G_(p'm')))}>0`.    (20.90)
The constant is the **actual quartet geometry**, not a proof threshold; (20.88) proves it is strictly positive for each nondegenerate reciprocal quartet, but no uniform lower bound is claimed here.  Together with the existing reflection-diamond law, (20.87)--(20.90) classify every generic two-orbit equal-heat line-aligned cancellation: it either is source-null or emits an actual companion source.  No projectively coherent equal-heat line is a closed nonlinear subsystem.
The projective fold itself has no hidden singular mass.  On a fixed heat sphere write `r=U e+Z qhat`, `U^2+Z^2=2kappa-Q^2`.  For either same- or mixed-helicity sectors, differentiation of `beta=Q/(aP+bM)` and the exact coefficient (20.85) give the **same** Jacobian cancellation
`G_(ab)/|partial_Z beta_(ab)| = Q U sqrt(1+beta_(ab)^2)/|beta_(ab)|^3`.    (20.91)
Thus the Beltrami source zero at the reflection fold cancels the vanishing projective Jacobian exactly, while the collinear pole is killed by `U=0`.  In source-line coordinates there is no extra continuum multiplicity hidden at either null face.  Combining (20.87) and (20.91), every non-null equal-heat conditional measure in the projective disintegration is supported on at most three physical parent orbits (reflection doublet plus reciprocal singlet); within-line cancellation is therefore finite-dimensional actual-source algebra.    (20.92)
There is an exact physical-space mirror of the same full-convolution locality.  If `phi(Lambda)` has even kernel `K_phi`, put `delta_h a=a(x+h)-a(x)` and `bar a_h=[a(x+h)+a(x)]/2`.  Symmetrizing (20.69) under `x<->x+h` gives
`D_phi(a,b;c)=(1/2)int int K_phi(h) delta_h c.[bar a_h x delta_h b-delta_h a x bar b_h] dx dh`.    (20.93)
Therefore
`W_phi=int int K_phi(h) delta_h omega.[bar u_h x delta_h u]dx dh`,
`T_phi=(1/2)int int K_phi(h){delta_h omega.[bar N_h x delta_h u-delta_h N x bar u_h]+delta_h G.[bar u_h x delta_h u]}dx dh`.    (20.94)
Every surviving nonlinear work/curvature term contains two actual field increments before any estimate.  The `L^2/K` Fourier suppression in (20.81) is the secant-coordinate shadow of this exact double-increment structure, not a separately assumed locality mechanism.
### 20.19 The secant resultant is one true full-field Leibniz defect — EXACT
Let `L(a,b):=P_Leray(a x b)`, so `N=L(u,Cu)`.  The edgewise secant numerator in (20.78) resums over the **entire** convolution before any absolute value: for every scalar curl multiplier `phi`,
`R_phi:=sum_m R_(phi,m)=phi(C)N-L(phi(C)u,Cu)-C L(u,phi(C)u)`.    (20.95)
Indeed on one parent pair with signed curls `(x,z)` and child signed curl `y`, the three terms carry the coefficient `phi(y)(z-x)-[z phi(x)-x phi(z)]-y[phi(z)-phi(x)]=(z-x)d_phi(y;x,z)`.  Thus (20.79) is equivalently the full-field identity
`(1/2)dot W_(phi(C))^E=<N,R_phi>`.    (20.96)
Affine multipliers vanish **as fields**, not merely after integration: `R_(alpha+beta x)=0`.  For the critical kink `phi(x)=|x|`, `phi(C)=Lambda` and
`R_Lambda=Lambda N-P_Leray(Lambda u x omega)-curl(u x Lambda u)`.    (20.97)
Hence the remaining critical quartic input is already one pairing of the two actual full fields `N` and `R_Lambda`; the companion-output incidence of (20.88)--(20.92) is a Fourier disintegration of this one field, not an additional dynamical network or owner.
There is also an exact Hodge completion.  Put the raw Lamb field `L_0:=u x omega=N+grad B`, `B=p+|u|^2/2`, and
`Rtilde_Lambda:=Lambda L_0-Lambda u x omega-curl(u x Lambda u)`.
Then `R_Lambda=P_Leray Rtilde_Lambda` and, writing `(I-P_Leray)Rtilde_Lambda=grad Pi_Lambda`,
`<N,R_Lambda>=<L_0,Rtilde_Lambda>-<grad B,grad Pi_Lambda>`, `grad Pi_Lambda=Lambda grad B-(I-P_Leray)(Lambda u x omega)`.    (20.98)
Thus any sign lost by Leray projection is exactly an actual Bernoulli/pressure-gradient correlation.  Raw Lamb, projected acceleration and pressure complement are three Hodge readings of the same critical Leibniz defect; none is a new source.  No sign is asserted for either term on the right of (20.98).
### 20.20 Closed-triad equalization of the Leibniz defect — EXACT
On one actual closed helical triad with distinct signed roots `x_0,x_1,x_2`, let `T_i` be its three modal works and `Z_tri` the canonical signed-curl second moment from §12.  Exact energy/helicity algebra gives
`T_i=Z_tri/prod_(j!=i)(x_i-x_j)`.  For the same triad the `R_phi` root contribution is `R_(phi,i)=d_phi(x_i;x_j,x_k)N_i`; hence
`2 Re(conj(u_i)R_(phi,i))=d_phi(x_i;x_j,x_k)T_i=Z_tri phi[x_0,x_1,x_2]` for **each** `i=0,1,2`.    (20.99)
Thus the secant defect removes the cyclic denominators exactly: every root of one closed triad receives the same signed curvature-work quantum.  Equivalently, if `P_(phi,tri):=sum_i phi(x_i)T_i=Z_tri phi[x_0,x_1,x_2]`, then for every scalar reader `psi`,
`2<psi(C)u,R_phi>_tri = P_(phi,tri) sum_i psi(x_i)`.    (20.100)
After summing all closed triads this gives, in particular,
`<u,R_phi>=3<phi(C)u,N>`.    (20.101)
For `phi(x)=|x|`, homochiral triads vanish because the divided difference is zero; every heterochiral triad has one common `R_Lambda` work quantum equal to its own critical nonlinear production.  Hence `<Lambda u,R_Lambda>` and `<Cu,R_Lambda>` are exactly the radius-sum and signed-curl-sum moments of the same critical triad production, not independent sources.  This is an instantaneous full-convolution moment identity; no selected triad is assumed to persist in time.
### 20.21 Energy-dual endpoint criterion for the true defect field — EXACT DEDUCTION
For the critical kink, (20.101) and the exact critical stock law give
`int_0^t <u,R_Lambda>dtau=(3/2)int_0^t W_Lambda dtau=(3/2)[C_(1/2)(t)-C_(1/2)(0)+2nu int_0^t||Lambda^(3/2)u||^2dtau]`.    (20.102)
Since `<u,R_Lambda>=<Lambda u,Lambda^-1 R_Lambda>` and physical kinetic energy gives `2nu int_0^(T_*)||Lambda u||^2dt<=E_total(0)`, Cauchy yields the absolute continuation criterion
`Lambda^-1 R_Lambda in L_t^2(0,T;L_x^2)  =>  sup_(t<T) C_(1/2)(t)<infinity`.    (20.103)
Consequently a finite singular endpoint necessarily satisfies
`int_0^(T_*)||Lambda^-1 R_Lambda||_2^2dt=infinity`.    (20.104)
This is not a new norm mechanism: `R_Lambda` is the explicit NS bilinear field (20.97), and the finite factor in the dual pairing is exactly the original kinetic viscous budget.  Equations (20.102)--(20.104) say that all remaining full-convolution recycling must manifest as failure of one concrete energy-dual Leibniz-defect action.  No estimate proving that action finite is currently available.
### 20.22 Multiplier-covariant NS and the universal hinge basis — EXACT
Rearranging (20.95) gives, for every admissible real scalar curl multiplier `phi`, the exact covariant differentiated equation
`(partial_t+nu Lambda^2)phi(C)u = P_Leray(phi(C)u x omega)+C P_Leray(u x phi(C)u)+R_phi`.    (20.105)
Thus `phi=1` is exactly the velocity equation and `phi=x` exactly the vorticity equation; both are affine and have `R_phi=0`.  Every non-affine multiplier fails to intertwine these two native NS laws by the **single** true field `R_phi`, not by a hierarchy of repair mechanisms.
Because `R_phi` is linear in `phi` and annihilates affine functions, the Peano/hinge representation is exact: whenever `phi''` is a finite signed measure after the usual compact spectral localization,
`R_phi=(1/2)int R_(|C-a|) d(phi''(a))`.    (20.106)
Hence the signed-curl hinge family is a universal basis for full-field multiplier covariance defects.  The control-volume reader did not create a special mechanism; it discovered the canonical second-difference coordinates of the nonlinear PDE itself.
For the critical kink `phi=|x|`,
`(partial_t+nu Lambda^2)Lambda u=P_Leray(Lambda u x omega)+curl(u x Lambda u)+R_Lambda`.  Pairing with `Lambda u` gives the exact `H^1` source decomposition
`Q=<Lambda omega,u x Lambda u>+<Lambda u,R_Lambda>`.    (20.107)
The first term is the covariant velocity/vorticity transport already present in (20.105); the second is the unique critical kink defect.  Their sum is the native vortex-stretching source `Q`, so neither is an additional enstrophy supplier.
### 20.23 Lie-bracket intertwining defect and Jacobi/Bianchi reduction — EXACT
On divergence-free fields define the helicity involution and Biot--Savart inverse-curl operators
`H:=C Lambda^-1`, `K:=C^-1=H Lambda^-1`; hence `H^2=I`, `HK=KH`, `u=K omega`, `Lambda u=H omega`.  With the divergence-free Lie bracket `[a,b]=(a.grad)b-(b.grad)a`, the critical defect (20.97) is exactly
`R_Lambda=[K omega,H omega]-K[omega,H omega]-H[K omega,omega]`.    (20.108)
Thus `R_Lambda` is the mixed Lie-bracket **intertwining defect** of the two native NS operators `K,H`; this line is the definition meant here, not an appeal to an external torsion formalism.
For any linear operator `A` put `S_A(X,Y):=[AX,Y]-[X,AY]`.  Jacobi applied to `X=omega`, `U=KX`, `V=HX` and (20.108) gives the exact Bianchi-type identity
`[X,R_Lambda]=S_K(X,[X,HX])+S_H(X,[KX,X])`.    (20.109)
No third term remains.  On helical curl eigenmodes `CX_x=xX_x`, `CY_z=zY_z`,
`S_H(X_x,Y_z)=[sgn(x)-sgn(z)][X_x,Y_z]`,
`S_K(X_x,Y_z)=[x^-1-z^-1][X_x,Y_z]`.    (20.110)
Hence the Jacobi evolution of the critical defect is driven only by two actual mismatches: cross-helicity mismatch and inverse-curl/radial mismatch.  The first vanishes inside one helicity sheet; the second vanishes on an equal signed-curl sheet.  These are algebraic properties of the full fields, not observer branches.
At a pure-helicity state `H omega=h omega`, (20.108) collapses further to
`R_Lambda=(H-hI)G=Lambda N-hG=-h(G-h Lambda N)`.    (20.111)
Thus the positive square in (20.82) is exactly the squared normal component of this same Lie-intertwining defect; no separate pure-helicity curvature mechanism exists.
### 20.24 Shifted-hinge normal square and global helicity-sheet Pythagoras — EXACT
For any signed-curl hinge `a`, put `A_a=C-aI`, `Lambda_a=|A_a|`, `H_a=sgn(A_a)` and `P_(a,h)=1_(hA_a>0)`.  If at one actual time `u=P_(a,h)u` for `h in {+-1}`, then every occupied parent lies on the same affine branch of `|x-a|`, and the full defect field collapses to
`R_(|C-a|)=2 Lambda_a P_(a,-h)N`.    (20.112)
Equivalently the squared distance `D_(a,h):=<u,[Lambda_a-hA_a]u>=2||Lambda_a^(1/2)P_(a,-h)u||^2` has `D_(a,h)=dot D_(a,h)=0` there, while viscosity is tangent to the same spectral side.  Hence full NS gives the exact normal-curvature law
`dot W_(|C-a|)=4||Lambda_a^(1/2)P_(a,-h)N||^2=2<N,R_(|C-a|)> >=0`.    (20.113)
Thus (20.82) is only the `a=0` member: every signed-curl half-space has the same exact tangent/normal Pythagoras.  A hinge is still an observer coordinate; the crossing acceleration is the true event.
For the global critical hinge `a=0`, write `omega_+-=P_+- omega`, `P_+-=(I+-H)/2`, and put
`A_-:=P_-[u,omega_+]`, `B_+:=P_+[u,omega_-]`, `D:=K[omega_+,omega_-]`.  Expanding (20.108) gives
`R_Lambda=2[A_-+P_-D]+2[P_+D-B_+]`.    (20.114)
The two brackets lie in orthogonal helicity sheets and commute with every radial power of `Lambda`; therefore
`||Lambda^-1 R_Lambda||^2=4||Lambda^-1(A_-+P_-D)||^2+4||Lambda^-1(P_+D-B_+)||^2`.    (20.115)
Consequently the endpoint divergence (20.104) is exactly divergence of at least one of these two actual helicity-sheet mismatch actions.  No sign is asserted for the internal cross terms of either square; they are not separately budgets or mechanisms.
### 20.25 Full-NS curvature law in defect coordinates — EXACT
For every admissible real curl multiplier `phi`, put
`Q_phi:=<phi(C)Lambda u,Lambda N>`, `V_phi:=sum_j<phi(C)u,partial_j u x partial_j omega>`.
Differentiating `W_phi=2<phi(C)u,N>`, using `u_t=N-nu Lambda^2u`, `N_t=F_N-nu Lambda^2N`, and the exact rotational identity (13.3), while (20.96) collects the inviscid terms, gives
`(1/2)dot W_phi=<N,R_phi>-2nu[Q_phi+V_phi]`.    (20.116)
Thus full work curvature has exactly three typed pieces: the nonlinear multiplier-covariance defect `R_phi`, the heat/state coupling `Q_phi`, and the genuine viscous product commutator `V_phi`.  No `F_N` remainder, phase repair, or observer source remains.  On a one-sided hinge state from (20.112), the two viscous readings cancel in the derivative of the tangent distance and (20.116) reduces to the normal square (20.113).
### 20.26 Affine viscous cancellation and universal curvature hinges — EXACT
For every affine curl multiplier `phi(x)=alpha+beta x`, energy/helicity give `W_phi=0` identically while (20.95) gives `R_phi=0`.  Hence (20.116) forces
`Q_phi+V_phi=0`.    (20.117)
In particular `<Lambda u,Lambda N>+sum_j<u,partial_j u x partial_j omega>=0`; the two terms are not independent enstrophy sources.  Since `Q_phi+V_phi` is linear in `phi` and annihilates affine functions, it has the same Peano basis as the nonlinear defect:
`Q_phi+V_phi=(1/2)int [Q_(|C-a|)+V_(|C-a|)] d(phi''(a))`.    (20.118)
Combining (20.106), (20.116) and (20.118), the **entire** full-NS multiplier-curvature law is a superposition of signed-curl hinge laws.  Nonlinearity and viscosity share the same second-difference coordinates; there is no further multiplier hierarchy hidden beyond the control-volume hinges.
### 20.27 Critical production is exactly the same-helicity-to-opposite resultant — EXACT
Write `u=u_++u_-`, `omega_h=h Lambda u_h`, and let `N^(hh):=P_Leray(u_h x omega_h)` be the actual self-helicity nonlinear acceleration.  Define the true helicity-flip resultant
`J_flip:=P_-N^(++)+P_+N^(--)`.  For every heterochiral closed triad, exactly one root is the minority-helicity child with same-helicity parents, while the other two roots have mixed-helicity parents; by the equalization law (20.99) the three `R_Lambda` root works are equal.  Therefore, after full convolution summation,
`<u,R_Lambda^(same parents)>=(1/3)<u,R_Lambda>=<Lambda u,N>`, `R_Lambda^(same parents)=2 Lambda J_flip`, and hence
`W_Lambda=4<Lambda u,J_flip>`.    (20.119)
Thus mixed-parent roots are two companion readings of the same triad critical quantum; the critical nonlinear production itself is completely owned by the actual same-parent helicity-flip resultant.
Combining (20.119) with the exact critical stock law gives
`C_(1/2)(t)-C_(1/2)(0)+2nu int_0^t||Lambda^(3/2)u||^2dtau=4int_0^t<Lambda u,J_flip>dtau`.    (20.120)
Since the kinetic energy law supplies `int_0^(T_*)||Lambda u||^2dt<infinity`, Cauchy gives the absolute continuation criterion `J_flip in L_t^2L_x^2 => sup C_(1/2)<infinity`; consequently every finite singular endpoint must satisfy
`int_0^(T_*)||J_flip||_2^2dt=infinity`.    (20.121)
This is a resultant statement after the entire same-helicity parent convolution has already been summed.  It does **not** follow from, nor imply, an atomwise persistent minority lineage.
### 20.28 Initial source coherence is heat-funded; endpoint flip divergence must be forced — EXACT / EXACT ANALYTIC
On the same pre-Hahn same-helicity edge space that defines `J_flip`, each actual child-source atom has the exact heat equation
`(partial_t+nu kappa_e)f_e=g_e`, `g_e=C_e(n_p a_m+a_p n_m)`, `kappa_e=|p|^2+|m|^2`, and hence
`f_e(t)=e^(-nu kappa_e t)f_e(0)+int_0^t e^[-nu kappa_e(t-s)]g_e(s)ds`.    (20.122)
Fix a child helical mode and write the heat-fiber aggregate of the homogeneous part as `a(kappa)=int_(Omega_kappa)f_e(0)dmu_kappa`.  The exact parent coarea gives `mu_kappa(Omega_kappa)=pi R`, `R=sqrt(2kappa-Q^2)<=sqrt(2kappa)`.  Therefore fiber Cauchy and the Carleman kernel identity give
`int_0^infinity |int e^(-nu kappa t)a(kappa)dkappa|^2dt <= (pi/nu)int|a(kappa)|^2dkappa <= (pi^2 sqrt(2)/nu)int kappa^(1/2)int_(Omega_kappa)|f_e(0)|^2dmu_kappa dkappa`.    (20.123)
The first constant is elementary: Schur with weight `kappa^-1/2` uses `int_0^infinity lambda^-1/2/(kappa+lambda)dlambda=pi kappa^-1/2`.  Clay rapid decay makes the final half-heat-weighted initial edge square finite; summing children/helicities therefore puts the entire inherited homogeneous contribution `J_flip^hom` in `L_t^2L_x^2`.
Consequently (20.121) forces the **Duhamel-forced** resultant to diverge:
`int_0^(T_*)||J_flip^forc||_2^2dt=infinity`, `J_flip^forc:=J_flip-J_flip^hom`.    (20.124)
Thus infinite critical recycling cannot be inherited from an initially coherent same-helicity source cloud.  It must be continually rebuilt by the true parent-acceleration forcing `g_e`; the Duhamel split is exact heat accounting, not a temporal ancestry or new source law.
### 20.29 Forced-source heat barrier: the remaining gap is one half derivative — EXACT ANALYTIC / ANTI-SHORTCUT
Let `G_alpha^flip:=int kappa_e^alpha|g_e|^2dLambda_flip` on the forced same-helicity flip edge space.  Restrict to `kappa>=kappa_0>0`.  Temporal Fourier transform of (20.122), fiber Cauchy, and `mu_kappa=pi R<=pi sqrt(2kappa)` give for every `alpha>-1/2`
`||J_flip^forc||_(L_t^2L_x^2;kappa>=kappa_0)^2 <= [pi sqrt(2)/(nu^2(alpha+1/2))] kappa_0^(-alpha-1/2) int G_alpha^flip(t)dt`.    (20.125)
Indeed the dual fiber integral is bounded by `pi sqrt(2) int_(kappa_0)^infinity kappa^(1/2-alpha)/(tau^2+nu^2kappa^2)dkappa <= [pi sqrt(2)/(nu^2(alpha+1/2))]kappa_0^(-alpha-1/2)`.  At the endpoint `alpha=-1/2` the abstract heat/coarea operator has logarithmic UV divergence, so no uniform bound exists on the unrestricted edge Hilbert space from heat geometry alone.  The known exact estimate `G_(-1,edge)<=4C_F^2 E||N||^2` therefore lies a half heat derivative below this direct resultant threshold.  Any closure must exploit further NS structure of `g_e`, not another heat-fiber/Cauchy reader.

#### Theory-2 update: the half derivative is present in the complete moving flag — EXACT
The later spectral-signature reconstruction identifies the missing half derivative before contraction.  For one hard edge with parent radii `P,M`, opposite-helicity child radius `Q`, and `kappa=P^2+M^2`, the shifted hard selector is supported on an interval of length
`d_e=Q+min(P,M)`, with
`(1/sqrt(2))sqrt(kappa)<=d_e<=(3/sqrt(2))sqrt(kappa)`.
Consequently, for the pre-contraction forcing square,
`(1/sqrt(2))G_(-1/2)<=int_R G_(-1)^flag(a)da<=(3/sqrt(2))G_(-1/2)`.    (20.125a)
Thus the old half-heat deficit is not a missing spectral species: it is the one-dimensional coarea length of the complete moving curl flag.  In deep high--high to low geometry the child-side piece `Q/sqrt(kappa)` vanishes while the parent-side sweep tends to `1/sqrt(2)`.  A zero-cut/child-only reader had discarded the relevant part of the flag.

This exact structural correction does **not** by itself give `int G_(-1/2)dt<infinity`.  The late reciprocal analysis shows how the same missing weight reappears in true full-convolution geometry: the certified reciprocal inequality
`Q chi_geom^2/|p-p'|>=sqrt(6)/8` combined with diamond coarea leaves exactly the endpoint child weight `Q^-1`, and exact symbolic elimination gives at most two reciprocal preimages per canonical companion role.  See `core/spectral_signature/HALF_DERIVATIVE_POLAR_KORN_BRIDGE.md` and the three companion audits there.
### 20.30 The hard flip coefficient is controlled by the child scale — EXACT ALGEBRAIC
For same-helicity parents of radii `P,M` and the opposite-helicity child radius `Q`, projecting the line (20.85) onto the minority child line gives
`G_flip=|P-M||q x r|(P+M-Q)/(4sqrt(2)PMQ) <= Q/(2sqrt(2))`.    (20.126)
Indeed with `S=P+M`, `delta=|P-M|`, `s=S/Q`, `d=delta/Q`, one has `sin^2theta=4(s^2-1)(1-d^2)/(s^2-d^2)^2`, so `(2sqrt(2)G_flip/Q)^2=4d^2(1-d^2)(s-1)^3(s+1)/(s^2-d^2)^2<=4d^2(1-d^2)<=1`.  Thus the hard flip source carries at most one derivative of the **child** scale, independently of parent heat.  Away from collinearity its zero set is exactly the Beltrami equator `P=M`; after applying `Lambda^-1`, the pair symbol is order zero.  This is an exact helical null structure, not a generic bilinear estimate.
### 20.31 The forced flip resultant is a state/acceleration commutator — EXACT
Let `N_h=P_hN`, `G_h=P_hG=h Lambda N_h`.  Summing the true edge forcing `g_e` over all same-helicity parent pairs **before** any estimate gives
`Y_flip:=sum_h P_(-h)P_Leray(N_h x omega_h+u_h x G_h)=sum_h h P_(-h)P_Leray(u_h x Lambda N_h-Lambda u_h x N_h)`.    (20.127)
Thus the nonlinear forcing that rebuilds `J_flip^forc` is one `Lambda`-placement commutator of the actual fields `u_h,N_h`.  On every Fourier parent pair its scalar radial factor is `|m|-|p|`, hence `|||m|-|p|||<=|q|`: regeneration itself carries a child-scale null factor.  The generic `G_(-1,edge)` estimate does not use this cancellation; any final closure should preserve (20.127) before applying a norm inequality.
### 20.32 Edge Duhamel resums to one full-field heat commutator — EXACT
Let `E_tau=e^(-nu tau Lambda^2)`.  Because the parent heat factor splits exactly, (20.122) resums before any estimate to
`J_flip^hom(t)=sum_h h P_(-h)P_Leray(E_tu_(0,h) x Lambda E_tu_(0,h))`,
`J_flip^forc(t)=sum_h h int_0^t P_(-h)P_Leray[E_(t-s)u_h(s) x Lambda E_(t-s)N_h(s)-Lambda E_(t-s)u_h(s) x E_(t-s)N_h(s)]ds`.    (20.128)
Thus even the final source-space Duhamel accounting contains no edge ancestry: inherited coherence is the flip source of the linear heat state, while regeneration is one bilinear heat-flow `Lambda`-placement commutator of the true fields `u_h,N_h`.
### 20.33 Helicity-involution torsion: the hard flip field is one full-field algebraic defect — EXACT
Let `B(a,b):=(1/2)P_Leray(a x Cb+b x Ca)`, so `N=B(u,u)`, and let `H=C Lambda^-1`, `P_+-=(I+-H)/2`.  Define the symmetric helicity-involution torsion
`T_H(a,b):=B(Ha,Hb)-H B(Ha,b)-H B(a,Hb)+B(a,b)`.
On one input/output helicity triple `(h,k;s)` its scalar coefficient is `hk-hs-ks+1=(1-hs)(1-ks)`, hence identically
`T_H(a,b)=4[P_-B(a_+,b_+)+P_+B(a_-,b_-)]`.    (20.129)
Therefore the hard critical resultant and its genuine nonlinear regeneration are simply
`J_flip=(1/4)T_H(u,u)`, `Y_flip=(1/2)T_H(u,N)`.    (20.130)
Thus the hard sector is not an edge mechanism: it is exactly the failure of the two helicity eigenspaces of the actual involution `H` to be invariant under the Euler bilinear product.  In particular `||J_flip||^2=||P_-B(u_+,u_+)||^2+||P_+B(u_-,u_-)||^2`; the two true output sheets are orthogonal before any estimate.
### 20.34 Smooth-background excision and the all-three-roots UV theorem — EXACT ALGEBRAIC / ABSOLUTE ANALYTIC
For any decomposition `u=w+z`, bilinearity of (20.129) gives
`J_flip(u)=J_flip(w)+(1/2)T_H(w,z)+J_flip(z)`.    (20.131)
If `w` is a divergence-free background with bounded `W^(1,infinity)` on a finite interval, Leray/Riesz `L^2` boundedness gives
`||T_H(w,z)||_2 <= C[||w||_infinity+||Hw||_infinity]||Lambda z||_2 + C[||Lambda w||_infinity+||Lambda Hw||_infinity]||z||_2`; hence the cross term is `L_t^2L_x^2` whenever `z` has the kinetic energy class.  Taking the arbitrary **fixed** Fourier cutoff `w=P_(<=L)u`, `z=P_(>L)u`, Bernstein and the physical energy law make every term containing `w` finite.  Thus (20.121) forces, for every finite `L`,
`int_0^(T_*)||J_flip(P_(>L)u)||_2^2dt=infinity`.    (20.132)
The exact hard-flip coefficient has in fact the low-root bound
`G_flip <= (1/sqrt(2)) min{P,M,Q}`.    (20.133)
For `Q` minimal this is (20.126); if `P<=M,Q`, use `|M-P|<=Q` and `P+M-Q<=2P` in the exact formula of (20.126), and similarly for `M`.  Consequently, for `z=P_(>L)u`,
`|hat[J_flip(z)](q)| <= C_F |q| ||z||_2^2` on `|q|<=L`, hence `||P_(<=L)J_flip(z)||_2 <= C L^(5/2)E_*` and its finite-time `L_t^2L_x^2` action is finite.  Combining this with (20.120)--(20.132) removes every bounded input or output scale:
`sup_(t<T_*) int_0^t <Lambda P_(>L)u, P_(>L)J_flip(P_(>L)u)>dtau=+infinity`, and in particular `int_0^(T_*)||P_(>L)J_flip(P_(>L)u)||_2^2dt=infinity`, for every fixed `L<infinity`.    (20.134)
Thus the final divergent work is genuinely **all-three-roots UV**.  The fixed cutoff is only a test background; because (20.134) holds for every `L`, no bounded-scale state, low-high paraproduct or high-high-to-bounded-output channel can own the endpoint.
### 20.35 Free-heat excision: the singular torsion belongs to the zero-initial nonlinear remainder — EXACT / ABSOLUTE ANALYTIC
Let `U_0(t)=E_tu_0` and `v(t)=u(t)-U_0(t)=int_0^t E_(t-s)N(s)ds`; then `v(0)=0` and `v` is still in the kinetic energy class.  Applying (20.131) with this smooth background gives the exact identity
`J_flip^forc=(1/2)T_H(U_0,v)+(1/4)T_H(v,v)`.    (20.135)
Because the smooth heat orbit `U_0` has bounded `W^(1,infinity)` on every finite interval, the first term belongs to `L_t^2L_x^2`.  Hence (20.124) implies
`int_0^(T_*)||T_H(v,v)||_2^2dt=infinity`.    (20.136)
So even continual regeneration cannot be attributed to interaction with the inherited smooth state: after exact heat subtraction, the remaining obstruction is the self-torsion of the true zero-initial nonlinear correction.
### 20.36 The hard flip resultant itself obeys a native heat-covariant NS law — EXACT
Because `T_H` is translation invariant and `H` commutes with `Lambda^2` and spatial derivatives, the ordinary Laplacian product rule polarizes exactly to
`Lambda^2 T_H(a,b)=T_H(Lambda^2a,b)+T_H(a,Lambda^2b)-2sum_j T_H(partial_j a,partial_j b)`.    (20.137)
Using `J_flip=(1/4)T_H(u,u)`, `u_t=N-nu Lambda^2u` and `Y_flip=(1/2)T_H(u,N)` therefore gives the full-field PDE
`(partial_t+nu Lambda^2)J_flip = S_J`, `S_J:=Y_flip-2nu sum_j J_flip(partial_j u)`.    (20.138)
Here `J_flip(partial_j u):=(1/4)T_H(partial_j u,partial_j u)`.  Thus the parent-relative heat hidden in (20.122)--(20.128) is not another mechanism: after exact resummation it is ordinary child viscosity plus the genuine viscous gradient-torsion commutator in (20.138).  Equivalently,
`J_flip(t)=E_tJ_flip(0)+int_0^t E_(t-s)S_J(s)ds`.    (20.139)
For every fixed Fourier set/projector `P` commuting with `Lambda`, this yields the exact derived-field accounting
`0.5||PJ_flip(t)||^2+nu int_s^t||Lambda PJ_flip||^2 =0.5||PJ_flip(s)||^2+int_s^t<PJ_flip,PS_J>dtau`.    (20.140)
This is a heat balance of the true derived field, not a new kinetic wallet; the source `S_J` is already the two actual terms displayed in (20.138).
### 20.37 The endpoint pushes one derivative down to the true flip source — ABSOLUTE ANALYTIC DEDUCTION
Fix `L>0` and apply (20.140) to `P_(>L)`.  Since `<PJ,PS_J>=<Lambda PJ,Lambda^-1PS_J>`, Young plus `||PJ||<=L^-1||Lambda PJ||` gives
`sup_(t<T)||P_(>L)J_flip(t)||^2 + nu int_0^T||Lambda P_(>L)J_flip||^2 <= ||P_(>L)J_flip(0)||^2 + nu^-1 int_0^T||Lambda^-1P_(>L)S_J||^2`.    (20.141)
Consequently the all-UV divergence (20.134) forces, for every finite `L`,
`int_0^(T_*)||Lambda^-1 P_(>L)[Y_flip-2nu sum_jJ_flip(partial_j u)]||_2^2dt=infinity`.    (20.142)
So the remaining obstruction is not arbitrary edge coherence: even after one full child derivative is removed, the **single heat-covariant torsion source** of (20.138) must have infinite UV `L_t^2L_x^2` action.  Neither term in the bracket is separately declared a mechanism or budget.
### 20.38 The Leibniz defect is the variational gradient of the cubic work — EXACT
For the cubic full-state functional `W_phi(u):=2<phi(C)u,B(u,u)>`, any divergence-free variation `v` satisfies
`delta W_phi[u;v]=2<phi(C)v,N>+4<phi(C)u,B(u,v)>=2<v,R_phi(u)>`.    (20.143)
The last equality is scalar-triple-product algebra and the explicit field (20.95); hence
`R_phi=(1/2) grad_(L^2) W_phi`.    (20.144)
Thus (20.101) is simply cubic Euler homogeneity `2<u,R_phi>=3W_phi`.  Moreover the linearization is a genuine Hessian and therefore obeys the exact reciprocity
`<v,D R_phi[u]w>=<w,D R_phi[u]v>` for all divergence-free `v,w`.    (20.145)
So complete-quartet/cross-child reciprocity is already the Hessian symmetry of one actual cubic state functional.  `R_phi` is not an extra source field attached to a genealogy; it is the state gradient of the same multiplier work whose endpoint growth is being accounted.
### 20.39 Variational Gauss--Weingarten collapse: `R_Lambda` and `J_flip` are one geometry — EXACT
Since (20.119) is the full-field identity `W_Lambda(u)=4<Lambda u,J_flip(u)>` and (20.144) gives `R_Lambda=(1/2)grad W_Lambda`, variation in an arbitrary divergence-free direction yields
`R_Lambda=2 Lambda J_flip+2[D J_flip[u]]^* Lambda u`, `D J_flip[u]v=(1/2)T_H(u,v)`.    (20.146)
Thus the same-parent term `2Lambda J_flip` and the mixed-parent/companion term are not two curvature mechanisms: the latter is exactly the `L^2` adjoint response of the **same** quadratic helicity-torsion map.  Since `D J_flip[u]u=2J_flip`, pairing (20.146) with `u` gives the exact `1:2` split
`<u,2Lambda J_flip>=(1/3)<u,R_Lambda>`, `<u,2[D J_flip[u]]^*Lambda u>=(2/3)<u,R_Lambda>`.    (20.147)
This is the full-field origin of the closed-triad equalization in (20.99)--(20.101); no persistent triad or companion genealogy is needed.
### 20.40 The two unsigned-helicity critical ledgers have one common nonlinear input — EXACT
Put `C_+-:=||Lambda^(1/2)u_+-||^2`, `D_+-:=||Lambda^(3/2)u_+-||^2`.  Helicity-resolved NS gives `dot C_h+2nu D_h=2<Lambda u_h,N_h>`, while nonlinear helicity conservation gives `<Lambda u_+,N_+>=<Lambda u_-,N_->`.  Using (20.119),
`dot C_+ +2nu D_+ = dot C_- +2nu D_- = 2<Lambda u,J_flip> = W_Lambda/2`.    (20.148)
Thus critical production is a common-mode loading of the two positive helicity stocks, not transfer from one helicity stock to the other; their difference is the signed-helicity ledger and has zero nonlinear input exactly.
### 20.41 The hard symbol has no hidden parent-heat decay — EXACT / SHARP ANTI-SHORTCUT
If `theta` is the angle between the two same-helicity parents, the exact coefficient (20.126) factors further as
`G_flip=|P-M|PM sin(theta)[1-cos(theta)]/[sqrt(2)Q(P+M+Q)]`.    (20.149)
Thus the parallel face has a cubic angular null.  However, for fixed nonzero child `q`, write `r=R e` and let `R->infinity`, with `gamma=angle(q,e)`.  Direct expansion of `P=|q+r|/2`, `M=|q-r|/2` gives the sharp deep-fiber limit
`G_flip -> [Q/(2sqrt(2))]|sin(2gamma)|`.    (20.150)
Hence the child bound in (20.126) is asymptotically saturated and there is **no** additional decay in parent heat on the deep high-high fiber.  The half-heat barrier (20.125) cannot be repaired by a stronger static coefficient estimate; any closure must use the actual `u_h/N_h` dynamics in `S_J`, not another geometric symbol bound.
### 20.42 Every signed-curl hinge has the same normal-torsion geometry — EXACT
For an arbitrary hinge `a`, put `H_a=sgn(C-aI)`, `Lambda_a=|C-aI|` and define `J_a:=(1/4)T_(H_a)(u,u)`, with the torsion formula (20.129) using `H_a`.  On a closed triad lying entirely on one side of `a`, `|x-a|` is affine and its nonlinear work vanishes by energy/helicity; on a crossing triad the unique minority-side root is exactly the normal output selected by `J_a`.  Summing the full convolution therefore gives
`W_(|C-a|)=4<Lambda_a u,J_a>`.    (20.151)
Combining (20.151) with the variational-gradient theorem (20.144) yields the shifted Gauss--Weingarten identity
`R_(|C-a|)=2Lambda_a J_a+2[D J_a[u]]^*Lambda_a u`.    (20.152)
Because every `H_a` is a fixed spectral involution commuting with heat and derivatives, the same chain rule as (20.137)--(20.138) gives
`(partial_t+nu Lambda^2)J_a=D J_a[u]N-2nu sum_jJ_a(partial_j u)`.    (20.153)
Thus the signed-curl hinge family is simultaneously the universal second-difference basis of multiplier work **and** the family of actual normal-torsion fields of the PDE.  The critical field `J_flip` is simply `J_0`; moving the observer hinge does not create a new dynamical species.
### 20.43 Full multiplier reconstruction from the hinge-torsion family — EXACT
For every multiplier covered by the Peano representation in (20.106), linearity together with (20.151)--(20.152) gives
`W_phi=2 int <Lambda_a u,J_a> d(phi''(a))`.    (20.154)
`R_phi=int [Lambda_aJ_a+[D J_a[u]]^*Lambda_a u] d(phi''(a))`.    (20.155)
Thus every nonlinear multiplier work and every full-convolution variational curvature field are superpositions of the actual hinge-normal torsions and the adjoint responses of those **same** torsions.  There is no additional multiplier-level mechanism left beyond the family `J_a`; the observer coordinate `a` only resolves the universal second-difference content of the PDE.
### 20.44 The critical work and torsion source are one self-adjoint helicity commutator — EXACT
For divergence-free fields put `A_v w:=P_Leray(v x w)` and `C_v:=[H,A_v]`.  Since `A_v^*=-A_v` and `H^*=H`, `C_v` is self-adjoint.  Scalar-triple-product algebra and the helical split give
`W_Lambda=<omega,C_u omega>=2<u,omega x Homega>=-4<u,omega_+ x omega_->`, `J_flip=-(1/2)sum_(h=+-1)h C_(u_h)omega_h`.    (20.156)
Differentiating the second identity with the true `u_h/N_h` and `omega_h/G_h` equations, or equivalently using (20.137), yields
`S_J=-(1/2)sum_h h[C_(N_h)omega_h+C_(u_h)G_h-2nu sum_j C_(partial_j u_h)partial_j omega_h]`.    (20.157)
Thus nonlinear regeneration and the viscous correction are covariant derivatives of the **same** self-adjoint helicity commutator.  If `K_H` is the kernel of `H`, then `C_v w=P_Leray PV int K_H(x-y)[v(y)-v(x)] x w(y)dy`; every term in (20.157) contains an actual field increment.  No new operator/source species appears at the final derivative.
### 20.45 The final source is the heat-rate divergence of one same-helicity quadratic stress — EXACT
Because `B(u_h,u_h)=-P_Leray div(u_h tensor u_h)`,
`J_flip=-sum_h P_(-h)P_Leray div(u_h tensor u_h)`.    (20.158)
The product rule and `(partial_t+nu Lambda^2)u_h=N_h` give the exact tensor law
`(partial_t+nu Lambda^2)(u_h tensor u_h)=u_h tensor N_h+N_h tensor u_h-2nu sum_j partial_j u_h tensor partial_j u_h=:Sigma_h`.    (20.159)
Consequently
`S_J=-sum_h P_(-h)P_Leray div Sigma_h`, `Lambda^-1S_J=-sum_h P_(-h)P_Leray (div/Lambda)Sigma_h`.    (20.160)
So the UV `H^-1` obstruction in (20.142) is exactly an order-zero Riesz reading of the heat-covariant rate of the **same actual quadratic helical stress** whose divergence is `J_flip`; `Sigma_h` is a derived state tensor, not a wallet or independent source.  In particular the child-scale factor in (20.126)--(20.127) is the Fourier image of the true divergence in (20.160), while the remaining difficulty is precisely lack of a finite `L_t^2L_x^2` control for this projected stress rate.
### 20.46 Pressure quotient of the torsion stress and cross-helicity stretching — EXACT
Let `M_h^0:=u_h tensor u_h-(|u_h|^2/3)I` and `Sigma_h^0:=Sigma_h-(tr Sigma_h/3)I`.  Since Leray annihilates the divergence of every scalar multiple of `I`,
`J_flip=-sum_h P_(-h)P_Leray div M_h^0`, `S_J=-sum_h P_(-h)P_Leray div Sigma_h^0`.    (20.161)
Moreover integration by parts in (20.119) gives the physical-space identity
`W_Lambda=4sum_h int u_h . S(Lambda u_(-h)) u_h dx`, `S(v):=[grad v+(grad v)^T]/2`.    (20.162)
Thus isotropic same-helicity stress belongs only to the pressure quotient; critical production is exactly stretching of each helical velocity by the strain of the opposite-helicity `Lambda u` field.  This is another reading of the same torsion work, not a new supplier.
### 20.47 The deviatoric helical stress has an exact kinetic-energy mass owner — EXACT
For `M_h^0=u_h tensor u_h-(|u_h|^2/3)I`, the Frobenius eigenvalues are `(2,-1,-1)|u_h|^2/3`, so pointwise and after integration
`|M_h^0|_F=sqrt(2/3)|u_h|^2`, `sum_h||M_h^0(t)||_(L^1)=sqrt(2/3)||u(t)||_2^2`.    (20.163)
Hence the primitive kinetic energy law is equivalently the finite stress-mass ledger
`sum_h||M_h^0(t)||_1+2nu sqrt(2/3) int_s^t||Lambda u||_2^2dtau=sum_h||M_h^0(s)||_1`.    (20.164)
This does **not** promote `M_h^0` to a new energy: its total mass is exactly the old kinetic owner in another algebraic coordinate.  Thus the endpoint cannot be attributed to growth of stress mass itself; only concentration/rotation/rate of a bounded-mass stress remains possible.
The tensor heat equation in (20.159) also has the exact matrix Kato identity (with the quotient defined by continuity at `u_h=0`)
`(partial_t+nu Lambda^2)|M_h^0|_F = Mhat_h^0:Sigma_h^0-nu O_h`,
`O_h:=[|grad M_h^0|_F^2-|grad |M_h^0|_F|^2]/|M_h^0|_F=sqrt(6)sum_j|P_(u_h^perp)partial_j u_h|^2 <=sqrt(6)|grad u_h|^2`.    (20.165)
Therefore `nu int_0^(T_*)sum_h int O_h dxdt<infinity` is a genuine **subpayment of the original viscous energy budget**: spatial rotation of the stress direction has finite normalized action.  The uncontrolled quantity in (20.160) is the full heat-rate stress, not this spatial orientation payment.
### 20.48 Material-covariant helical stress law — EXACT
Put `D_u:=u.grad` and let `P_h=(P_Leray+hH)/2`.  Since `N_h=-P_h D_u u`, the true helical velocity satisfies
`(partial_t+nu Lambda^2+D_u)u_h=K_h`, `K_h:=[D_u,P_h]u`.    (20.166)
Moreover `K_++K_-=[D_u,P_Leray]u=-grad p` and `K_+-K_-=[D_u,H]u`.  Thus in the material frame the only non-gradient sheet-changing object is the **helicity/advection commutator**; the common mode is exactly the pressure correction required by incompressibility.
Taking the trace-free quadratic product gives
`(partial_t+nu Lambda^2+D_u)M_h^0=Theta_h^0`,
`Theta_h: = u_h tensor K_h+K_h tensor u_h-2nu sum_j partial_j u_h tensor partial_j u_h`.    (20.167)
Let `Q_h:=P_(-h)P_Leray div`, so `J_flip=-sum_h Q_h M_h^0`.  Because `Q_h` is fixed in time and commutes with heat but not with material advection,
`(partial_t+nu Lambda^2+D_u)J_flip=C_J`,
`C_J:=sum_h([Q_h,D_u]M_h^0-Q_h Theta_h^0)=S_J+D_u J_flip`.    (20.168)
This is the material/Codazzi form of the same source, not a new source species.  Every inviscid term is now either a projector--advection commutator or the common pressure correction; viscosity appears only through the true gradient stress already present in (20.167).
Since `div u=0`, material advection is `L^2`-skew and therefore
`0.5||J_flip(t)||_2^2+nu int_s^t||Lambda J_flip||_2^2=0.5||J_flip(s)||_2^2+int_s^t<J_flip,C_J>dtau`.    (20.169)
Consequently `Lambda^-1 C_J in L_t^2L_x^2` on a finite interval would bound `sup_t||J_flip(t)||_2`; together with (20.121) this yields the necessary endpoint condition
`int_0^(T_*)||Lambda^-1 C_J||_2^2dt=infinity`.    (20.170)
Thus the final divergence survives even in the physical material frame: a stress with exactly finite kinetic mass (20.164) and finite normalized spatial-orientation payment (20.165) would have to undergo infinite energy-dual **material Codazzi rate**.  No estimate proving (20.170) impossible is asserted here.
### 20.49 The hard flip is the self-induced material helicity commutator — EXACT
For any divergence-free `v`, the identity `P_(-h)P_Leray D_v v=(1/(2h))P_Leray[D_v,H]v` holds when `Hv=hv`.  Hence the full hard field has the equivalent material form
`J_flip=-(1/2)sum_(h=+-1) h P_Leray[D_(u_h),H]u_h`.    (20.171)
If `K_H` denotes the distribution kernel of `H`, integration by parts using `div v=0` gives the exact Calderon commutator formula
`[D_v,H]w(x)=PV int grad K_H(x-y).[v(x)-v(y)] w(y)dy`.    (20.172)
Thus the hard source contains a true velocity increment before any norm estimate.  At an actual pure-`h` state the empty-sheet material acceleration is `K_(-h)=N_(-h)=J_(-h)`, recovering the normal-crossing event of (20.113) without an edge interpretation.
The finite stress owner also controls its ordinary spatial variation.  Pointwise
`|grad M_h^0|_F <=sqrt(8/3)|u_h||grad u_h|`, hence for every finite `T<T_*`,
`int_0^T sum_h||grad M_h^0||_(L^1)dt <=sqrt(8/3) T^(1/2) sup_t||u||_2 [int_0^T||grad u||_2^2dt]^(1/2)<infinity`.    (20.173)
Consequently, by `W^(1,1)(R^3)->L^(3/2)` and Riesz boundedness,
`Lambda^-1 J_flip in L_t^1(0,T;L_x^(3/2))`.    (20.174)
This is a genuine finite weak/spatial-variation consequence of kinetic energy, but it is far below the `L_t^2L_x^2` action whose divergence is forced by (20.121).  Thus neither stress mass nor ordinary spatial BV can by themselves close the endpoint; the unresolved concentration is specifically in the heat/material **rate** of that stress.
### 20.50 Leray-covariant helicity connection and its off-diagonal curvature — EXACT
The involution geometry must be taken on the true divergence-free state manifold.  Put `Dcal_v w:=P_Leray[(v.grad)w]` for divergence-free `v,w`; then `Dcal_v^*=-Dcal_v` on `L^2_sigma`, while `H^2=I` and `H^*=H` there.  Define the intrinsic helicity connection
`A_v:=[Dcal_v,H]`.  Then exactly
`A_v^*=A_v`, `H A_v+A_v H=0`.    (20.175)
(The raw material commutator in (20.171) is `P_Leray[D_v,H]` on the state; without the Leray covariance one has instead `H[D_v,H]+[D_v,H]H=[D_v,P_Leray]`, whose missing normal component is pressure/Hodge geometry.)
Define `Curv_H(v):=H A_v-A_(Hv)`.  Since the Euler bilinear map is `B(a,b)=-(1/2)[Dcal_a b+Dcal_b a]`, expansion of the torsion (20.129) gives
`4J_flip=Curv_H(u)u`, `W_Lambda=<Lambda u,Curv_H(u)u>`.    (20.176)
Moreover `H Curv_H(v)+Curv_H(v)H=0`.    (20.177)
Thus the hard critical field is intrinsically off-diagonal on the actual divergence-free state space.  The old statement “same-helicity parents create an opposite-helicity child” is only the Fourier-coordinate form of (20.177).  Raw material transport and this intrinsic connection differ precisely by the gradient second-fundamental-form/pressure direction, so they must not be conflated.
### 20.51 Kinetic dissipation is exactly stress Fisher information — EXACT
Write `r_h:=|M_h^0|_F=sqrt(2/3)|u_h|^2`.  The rank-one differential algebra behind (20.165) gives pointwise
`2sqrt(2/3)|grad u_h|^2=(1/2)|grad r_h|^2/r_h+(2/3)O_h`.    (20.178)
Substituting this identity into the kinetic ledger (20.164) yields the exact stress-coordinate form of the **same** physical energy law:
`sum_h||M_h^0(t)||_1 +(nu/2)int_s^t sum_h int |grad r_h|^2/r_h dxdtau +(2nu/3)int_s^t sum_h int O_h dxdtau =sum_h||M_h^0(s)||_1`.    (20.179)
Since `|grad M_h^0|^2/r_h=|grad r_h|^2/r_h+O_h`, Cauchy and (20.179) imply the absolute stress class
`M_h^0 in L_t^infinity L_x^1 intersect L_t^2 W_x^(1,1)`, and hence `Lambda^-1 J_flip in L_t^2 L_x^(3/2)`.    (20.180)
Thus kinetic viscosity already owns both magnitude Fisher information and spatial orientation Fisher information of the finite-mass stress.  The unresolved endpoint is strictly stronger: it asks the **heat/material rate** of this stress, after opposite-helicity divergence, to leave the energy-dual `L_t^2H_x^-1` class.  No extra stress energy or Fisher wallet remains to be discovered at first spatial order.
### 20.52 Connection transfer versus curvature loading — EXACT TWO-LEDGER ACCOUNTING
Let `A_u=[D_u,H]` as in (20.175) and put `T_E:=<u_+,A_u u_->`.  The material sector law (20.166), pressure orthogonality, self-adjointness of `A_u` and its anti-commutation with `H` give
`dot E_+ +2nu||Lambda u_+||^2=T_E`, `dot E_- +2nu||Lambda u_-||^2=-T_E`, `E_h:=||u_h||_2^2`.    (20.181)
Thus `T_E` is an exact antisymmetric kinetic transfer and its signed cumulative integral is finite on every finite interval by the original energy budget.
In contrast, with `C_h=||Lambda^(1/2)u_h||^2`, (20.148) and (20.176) read
`dot C_+ +2nu||Lambda^(3/2)u_+||^2 = dot C_- +2nu||Lambda^(3/2)u_-||^2 = (1/2)W_Lambda=(1/2)<Lambda u,Curv_H(u)u>`.    (20.182)
Hence the endpoint is not sustained by repeated helicity-energy ping-pong: the **connection** `A_u` only redistributes the finite kinetic owner antisymmetrically, whereas the **curvature** `Curv_H` loads the two positive critical stocks in common mode.  A finite singular endpoint requires infinite cumulative common-mode curvature loading even though the signed connection-transfer ledger remains finite.
### 20.53 Instantaneous involution forbids a hidden even torsion Lyapunov stock — EXACT ANTI-SHORTCUT
The Euler acceleration is quadratic, so under the instantaneous algebraic involution `u->-u`, `N(-u)=N(u)`.  For every differentiable **even** state functional `F(-u)=F(u)`, its Euler production therefore obeys
`P_F(u):=D F(u)[N(u)]`, `P_F(-u)=-P_F(u)`.    (20.183)
Hence an even positive stock can have a sign-definite nonlinear production only if that production vanishes identically, i.e. the stock is an exact Euler invariant.  In particular changing the Sobolev weight in a quadratic torsion norm `||Lambda^sigma J_flip||^2`, or using a quadratic stress norm, cannot manufacture a one-sided nonlinear payment: `J_flip(-u)=J_flip(u)` makes every such stock even.  This is an instantaneous algebraic statement, not the claim that `u->-u` is an NS trajectory symmetry.
Thus the final closure cannot be a hidden positive “torsion energy” obtained by choosing a clever even norm.  It must use the signed covariant/material structure already exposed in (20.166)--(20.182), while the only genuine positive payments remain those owned by viscosity/kinetic energy.
### 20.54 Hinge-work Kirchhoff profile: critical height, connection slope, enstrophy area — EXACT
For `Lambda_a=|C-a|`, `H_a=sgn(C-a)` put `W_a:=2<Lambda_a u,N>` and its cumulative profile `A(a,t):=int_0^t W_a(tau)dtau`.  Since `partial_a Lambda_a=-H_a`,
`partial_a A(a,t)=-int_0^t2<H_a u,N>dtau= -[S_a(t)-S_a(0)]-2nu int_0^t<H_a u,Lambda^2u>dtau`, `S_a:=<u,H_a u>`.    (20.184)
Because `|S_a|<=||u||_2^2` and `|<H_a u,Lambda^2u>|<=||Lambda u||_2^2`, the original kinetic law gives the uniform connection-slope bound
`sup_(a in R,t<T_*) |partial_a A(a,t)| <= 3||u_0||_2^2`.    (20.185)
At the critical hinge, `A(0,t)=C_(1/2)(t)-C_(1/2)(0)+2nu int_0^t||Lambda^(3/2)u||_2^2dtau`.  On the other hand, writing the instantaneous signed modal-work measure as `dW_x`, energy/helicity give `int dW_x=int x dW_x=0` and `W_a=int|x-a|dW_x`; two integrations by parts in `a` therefore give
`int_R A(a,t)da = int_0^t int x^2 dW_x dtau =2int_0^t Q(tau)dtau`.    (20.186)
Thus critical growth, helicity-sheet connection transfer and enstrophy stretching are respectively the **height, slope and area of one true hinge-work profile**.  The slope has a finite kinetic owner, while the area is exactly the already-known `H^1` stretching input and may diverge at a singular endpoint.  Hence this identity does not manufacture a new finite area wallet; it precisely explains why bounded connection transfer alone cannot kill common-mode critical curvature.
### 20.55 State plus viscous history is one positive signed-curl measure — EXACT CORE ACCOUNTING
Let `dE_x(t)` be the positive kinetic-energy measure resolved by signed curl `x=s|k|`, and define the positive accumulated measure
`dM_t(x):=dE_x(t)+2nu int_0^t |x|^2 dE_x(tau)dtau`.    (20.187)
The exact energy and helicity laws give, for every `t<T_*`,
`int dM_t=E(0)`, `int x dM_t=H(0)`.    (20.188)
Thus `M_t` has fixed total mass and fixed signed-curl barycenter.  For every hinge `a`, the multiplier stock law integrates to
`int |x-a|dM_t(x)=int|x-a|dE_x(0)+A(a,t)`, `A(a,t)=int_0^t W_(|C-a|)(tau)dtau`.    (20.189)
So the whole hinge family is only the absolute-deviation potential of **one positive physical measure** consisting of present kinetic stock plus genuinely dissipated kinetic history.  The observer coordinate `a` does not create a resource.
Writing `m_0=H(0)/E(0)`, its signed-curl variance is
`Var(M_t):=int(x-m_0)^2dM_t=||Lambda u(t)||_2^2+2nu int_0^t||Lambda^2u||_2^2dtau-H(0)^2/E(0)=Var(M_0)+2int_0^t Q(tau)dtau`.    (20.190)
Hence vortex stretching is exactly half the variance-growth rate of this fixed-mass/fixed-barycenter positive measure.  Critical blow-up is loss of first-absolute-moment tightness; it necessarily drives variance to infinity but this is already the known `H^1` frontier, not a new contradiction.  The measure can in principle spread simultaneously toward `x=+-infinity` while keeping (20.188), so positivity alone does not close `Y=>bot`.
### 20.56 The hard torsion has a finite kinetic Hardy owner — ABSOLUTE DIV--CURL
For each helicity sheet, `J_(-h)=-P_(-h)P_Leray (u_h.grad)u_h`.  Componentwise, `u_h` is divergence-free while `grad(u_h)_i` is curl-free.  The div--curl Hardy theorem, followed by boundedness of Riesz/Leray/helicity projectors on the real Hardy space `H^1`, gives
`||J_(-h)||_(H^1) <= C ||u_h||_2||grad u_h||_2`.    (20.191)
Therefore the original kinetic budget implies
`int_0^(T_*)||J_flip||_(H^1)^2dt <= C E_* int_0^(T_*)||grad u||_2^2dt <= C E_*^2/nu <infinity`.    (20.192)
The same estimate holds for the material helicity-connection field `P_Leray[D_u,H]u`.  Thus the hard source already has finite `L_t^2` **Hardy mass**, while (20.121) forces its `L_t^2L_x^2` action to diverge.  The remaining endpoint is therefore a genuine Hardy-to-`L^2` UV concentration, not growth of total nonlinear-source mass.  This estimate supplies no `L^2` wallet: the Hardy/BMO dual would require `Lambda u` in BMO, i.e. one additional spatial derivative beyond the critical viscous stock.
### 20.57 Even and natural odd torsion potentials both fail as hidden nonlinear wallets — EXACT ANTI-SHORTCUT
The parity obstruction (20.183) kills every even quadratic torsion/stress Lyapunov candidate.  The most natural odd cubic escape also fails **exactly**.  Let the real Fourier state have only the reality pairs generated by `k=(1,0,0)` with helicity `+` and `p=(2,1,0)` with helicity `-`, each of unit helical amplitude, e.g.
`u_k=(0,1,i)/sqrt(2)`, `u_p=(-i/sqrt(10),2i/sqrt(10),1/sqrt(2))`, and `u_(-q)=conj(u_q)`.  For the cubic `F_0(u):=<u,J_flip(u)>`, direct **untruncated** Euler convolution gives
`D F_0(u)[N(u)]=<N,J_flip>+<u,DJ_flip[u]N>=(-27-5sqrt(5)+5sqrt(10)+15sqrt(2))/25<0`.    (20.193)
Indeed `<N,J_flip>=0` on this state, and the displayed numerator is negative because `(27+5sqrt(5))^2-(5sqrt(10)+15sqrt(2))^2=154-30sqrt(5)>0`.  Hence the apparent Chern--Simons-type cubic potential is not positive either.  Together with (20.183), this forbids both the even-norm and the canonical odd-cubic shortcuts; a closure must use the actual signed material/covariant accounting, not a hidden state-space Lyapunov functional of these natural forms.
### 20.58 The entire native `u/H/B` cubic-potential space has no positive Euler production — EXACT CLASSIFICATION / ANTI-SHORTCUT
Let `T(a,b,c):=<a,B(b,c)>`.  Symmetry of `B` and the polarized energy identity `T(a,b,c)+T(b,c,a)+T(c,a,b)=0` reduce every placement `<H^alpha u,B(H^beta u,H^gamma u)>`, `alpha,beta,gamma in {0,1}`, to two independent nonzero cubics:
`F_1:=<Hu,N>` and `F_2:=<u,B(Hu,Hu)>=2<u,J_flip>`; the zero-`H` and three-`H` sectors vanish, while the three placements in each one-/two-`H` sector occur in the ratio `1:-1/2:-1/2`.    (20.194)
No nontrivial linear combination of these two native cubics has sign-definite Euler production.  Four exact two-reality-pair states suffice.  Their production vectors `(D F_1[N],D F_2[N])` are
`(a,a), (-a,a), (-b,-c), (b,-c)` with
`a=(23+sqrt(5)-sqrt(10)-15sqrt(2))/10>0`,
`b=-(3/130)[-13sqrt(5)-13sqrt(2)-10-sqrt(65)-sqrt(26)+14sqrt(10)]>0`,
`c=[-13sqrt(65)-13sqrt(26)-13sqrt(5)-13sqrt(2)+26sqrt(10)+154]/130>0`.    (20.195)
The first pair is produced by modes `(1,0,0),(1,1,0)` with equal unit amplitudes and helicities `--` / `++`; the second by `(1,1,0),(2,1,0)` with helicities `+-` / `-+`.  Positivity follows for example from `sqrt(5)>2`, `sqrt(10)<16/5`, `sqrt(2)<10/7` for `a,b`, and `sqrt(65)<81/10`, `sqrt(26)<51/10`, `sqrt(5)<9/4`, `sqrt(2)<3/2`, `sqrt(10)>79/25` for `c`.  If `alpha D F_1+beta D F_2>=0` on all four states, the first pair forces `beta>=|alpha|`, while the second forces `-beta>=(b/c)|alpha|`; hence `alpha=beta=0`.
Thus within the full native cubic placement algebra generated solely by `u,H,B`, **no** odd cubic hidden wallet exists.  Any final signed accounting must come from the already exposed material/hinge dynamics rather than another placement of the same operators.
### 20.59 Nonlinear homochiral-background excision — EXACT REDUCTION
For each `h=+-1`, let `v_h` solve the helicity-decimated equation
`partial_t v_h+nu Lambda^2v_h=P_h B(v_h,v_h)`, `v_h(0)=u_(0,h)`.    (20.196)
Energy polarization gives `0.5d||v_h||_2^2/dt+nu||Lambda v_h||_2^2=0`; because `Cv_h=hLambda v_h`, helicity conservation simultaneously gives `0.5d||Lambda^(1/2)v_h||_2^2/dt+nu||Lambda^(3/2)v_h||_2^2=0`.  Thus the positive critical norm stays bounded, and the usual critical local theory makes each smooth-data decimated orbit global and smooth.
Put `V=v_++v_-` and `w=u-V`, so `w(0)=0`.  On every finite interval `V` is a smooth divergence-free background; applying the exact bilinear expansion (20.131) and the smooth-background estimate gives
`int_0^(T_*)||J_flip(w)||_2^2dt=infinity`.    (20.197)
Hence neither homochiral tangent subsystem, even after its full nonlinear evolution, can own the singular torsion.  After excising both globally regular sheet flows the obstruction remains in the self-torsion of one zero-initial remainder.  This is a comparison reduction, not a restart clock or a claim that `V` itself solves the full NS equation.
### 20.60 Rank-one stress-cone Gauss decomposition — EXACT
At every point with `u_h!=0`, put `n_h=u_h/|u_h|`, `r_h=|M_h^0|_F=sqrt(2/3)|u_h|^2`, and `q_h:=(partial_t+D_u)u_h=K_h-nu Lambda^2u_h`.  The rank-one deviatoric cone has tangent space `T_h={u_h tensor q+q tensor u_h-(2/3)(u_h.q)I}` and normal space `N_h={S=S^T:tr S=0, S u_h=0}`.  Therefore the true material rate is tangent identically and its amplitude/orientation split is
`[(|(partial_t+D_u)M_h^0|_F^2-|((partial_t+D_u)r_h)|^2)/r_h]=sqrt(6)|P_(n_h^perp)q_h|^2`.    (20.198)
Thus material rotation of the distinguished stress eigenline is exactly the squared normal material acceleration of the actual helical velocity, not an arbitrary tensor rate.
For the heat-covariant rate (20.167), the inviscid term `(u_h tensor K_h+K_h tensor u_h)^0` is still tangent to this cone.  Hence its **entire normal component is viscous**.  Writing `b_j=P_(n_h^perp)partial_j u_h`, orthogonal projection onto `N_h` gives
`Pi_(N_h)Theta_h^0=-2nu[sum_j b_j tensor b_j-(1/2)(sum_j|b_j|^2)(I-n_h tensor n_h)]`.    (20.199)
Since a positive `2x2` covariance matrix with trace `T` has trace-free Frobenius norm at most `T/sqrt(2)`, (20.165) yields
`|Pi_(N_h)Theta_h^0| <= (nu/sqrt(3)) O_h`, hence `int_0^(T_*)sum_h||Pi_(N_h)Theta_h^0||_(L^1)dt<infinity`.    (20.200)
So biaxial/normal escape from the rank-one stress cone is already owned by genuine viscosity.  Any unresolved material-Codazzi concentration must live in the **tangent** cone motion: amplitude and eigenline rotation of the actual helical stress.  This does not yet give an `L_t^2H^-1` bound for that tangent rate.
### 20.61 Leray-covariant Riccati/Gauss identity of the intrinsic helicity connection — EXACT
For operators on `L^2_sigma`, let `Lcal_u X:=partial_t X+[Dcal_u,X]`.  Since `Lcal_u H=[Dcal_u,H]=A_u`, applying this derivation to the exact involution `H^2=I` once and twice gives
`H A_u+A_u H=0`, `H Lcal_u A_u+(Lcal_u A_u)H=-2A_u^2`.    (20.201) Hence on each helicity sheet
`P_h(Lcal_u A_u)P_h=-h P_hA_u^2P_h`.    (20.202) Equivalently the intrinsic projector has first covariant derivative `(h/2)A_u` off-diagonal and forced diagonal second derivative `P_h Lcal_u^2(P_h)P_h=-(1/2)P_hA_u^2P_h`.  This is a genuine Gauss/Riccati square of the actual Leray-covariant connection.  The involution alone leaves the off-diagonal/Codazzi block of `Lcal_u A_u` free; any closure must therefore obtain that block from additional NS compatibility rather than silently promoting raw material advection to an involutive connection.
### 20.62 Intrinsic/extrinsic Gauss split of helical transport — EXACT
The projected advection `Dcal_u=P_Leray D_u` is not an observer device: the true NS state equation is exactly `partial_tu+nu Lambda^2u+Dcal_u u=0`.  Its Hodge-normal complement is the second-fundamental-form field `II_u(v):=(I-P_Leray)D_u v`, with `II_u(u)=-grad p`.  For `P_h=(I+hH)/2` and the intrinsic connection (20.175),
`(partial_t+nu Lambda^2+Dcal_u)u_h=(h/2)A_u u`, and equivalently `partial_tu_h+nu Lambda^2u_h+P_hDcal_u u_h=(h/2)A_u u_(-h)`.    (20.203)
Thus the left side is the homochiral tangent evolution in the fixed helicity sheet and the **only** intrinsic sheet-changing input is the connection acting on the opposite sheet.  Comparing with the raw material law (20.166) gives the exact Gauss split
`K_h=II_u(u_h)+(h/2)A_u u`, `sum_h II_u(u_h)=II_u(u)=-grad p`.    (20.204) The first term is gradient/Hodge-normal and the second is divergence-free/state-tangent, hence they are globally `L^2`-orthogonal whenever the displayed norms are finite.  Pressure is therefore the extrinsic normal geometry of physical material transport, not part of the intrinsic helicity connection; conversely the connection is the unique pressure-free cross-sheet coupling of the true projected NS dynamics.
### 20.63 Gauss--Codazzi block decomposition of projected advection — EXACT
Relative to `P_+ direct-sum P_-`, decompose `Dcal_u=Dcal_u^parallel+Dcal_u^perp` into its block-diagonal and off-diagonal parts.  Since `A_u=[Dcal_u,H]` and `H A_u=-A_u H`,
`Dcal_u^perp=-(1/2)H A_u`, `Dcal_u^parallel=Dcal_u+(1/2)H A_u`.    (20.205)
Therefore the intrinsic material derivative in (20.201) splits identically as
`Lcal_u A_u = Cod_H(u)-H A_u^2`, `Cod_H(u):=partial_t A_u+[Dcal_u^parallel,A_u]`.    (20.206)
Here `Cod_H(u)` is purely off-diagonal, while `-H A_u^2` is purely diagonal.  Thus (20.202) is exactly the Gauss block, and the **entire** still-free block is the Codazzi derivative of the cross-sheet connection under the homochiral/tangent projected connection.  No norm estimate enters this split. The true projected NS equation itself becomes
`partial_tu+nu Lambda^2u+Dcal_u^parallel u=(1/2)H A_u u`.    (20.207)
Hence the same connection which measures sheet exchange is the only correction to homochiral tangent evolution, while its diagonal material acceleration is already the square in (20.202).  Any further closure must use the NS evolution to constrain `Cod_H(u)`; the involution/Grassmannian geometry has now given all of its algebraic content.
### 20.64 Pressure is the Gauss curvature of the divergence-free state manifold — EXACT
For the intrinsic connection `nabla_u v:=Dcal_u v` and `II(u,v):=(I-P_Leray)D_u v`, the gradient part is symmetric because `D_u v-D_v u=[u,v]` is divergence-free.  Let `R(u,v)w:=nabla_u nabla_v w-nabla_v nabla_u w-nabla_[u,v]w`.  Ambient advection is flat before projection, so one integration by parts gives the exact Gauss equation
`<R(u,v)w,z>=<II(v,w),II(u,z)>-<II(u,w),II(v,z)>`.    (20.208) In particular `<R(u,v)v,u>=<II(v,v),II(u,u)>-||II(u,v)||^2`; the intrinsic curvature is sign-indefinite and is owned entirely by the actual Hodge/pressure second fundamental form, not by a new source. For the helicity connection `A_v=[nabla_v,H]`, the standard Ricci identity is an elementary commutator consequence:
`[nabla_u,A_v]-A_(nabla_u v)-[nabla_v,A_u]+A_(nabla_v u)=[R(u,v),H]`.    (20.209)
Thus the antisymmetric/Codazzi second derivative of the helicity splitting is completely fixed by pressure/Hodge curvature.  This does **not** determine the symmetric longitudinal derivative `Cod_H(u)` in (20.206): the latter is precisely the remaining dynamical information along the NS trajectory.  Hence pressure geometry supplies an exact compatibility law but no unproved finite rate budget is inferred from it.
### 20.65 The stress eigenline obeys a forced weighted harmonic-map heat law — EXACT
At points with `u_h!=0`, write `u_h=rho_h n_h`, `|n_h|=1`, and let `D_t:=partial_t+D_u`.  Splitting the raw material equation `D_tu_h-nu Delta u_h=K_h` into the `n_h` and `n_h^perp` directions gives
`D_t rho_h-nu[Delta rho_h-rho_h|grad n_h|^2]=n_h.K_h`.    (20.210)
`rho_h{D_t n_h-nu[Delta n_h+2 grad(log rho_h).grad n_h+|grad n_h|^2 n_h]}=P_(n_h^perp)[II_u(u_h)+(h/2)A_u u]`.    (20.211)
Here (20.204) was used in the second line.  Thus the distinguished eigenline of the rank-one stress is a weighted harmonic-map heat flow forced by exactly the two true geometries already identified: the Hodge/pressure second fundamental form and the intrinsic helicity connection.  The viscosity terms are precisely the orientation Fisher/tension behind (20.165), (20.178)--(20.180).  No additional tensor-rate species remains; a final eigenline-based closure would have to control the right side of (20.211) from the coupled NS evolution itself.
### 20.66 Pressure cannot own the final rate: intrinsic Codazzi obstruction — EXACT REDUCTION
Project the material law (20.168) back to the true divergence-free state space and put
`C_J^sigma:=(partial_t+nu Lambda^2+Dcal_u)J_flip=S_J+Dcal_u J_flip=P_Leray C_J`.    (20.212) Since `Dcal_u^*=-Dcal_u` on `L^2_sigma`, the same exact energy accounting is
`0.5||J_flip(t)||_2^2+nu int_s^t||Lambda J_flip||_2^2=0.5||J_flip(s)||_2^2+int_s^t<J_flip,C_J^sigma>dtau`.    (20.213)
Therefore `Lambda^-1 C_J^sigma in L_t^2L_x^2` on a finite interval would bound `sup_t||J_flip(t)||_2`, and (20.121) forces the sharper necessary endpoint condition
`int_0^(T_*)||Lambda^-1 C_J^sigma||_2^2dt=infinity`.    (20.214)
Thus the Hodge-normal/pressure part of raw material transport cannot own the last divergence: it survives after exact Leray projection.  The remaining rate is intrinsically divergence-free and belongs to the same state manifold on which the connection/Riccati/Codazzi identities (20.201)--(20.209) live.
### 20.67 The intrinsic endpoint source is the longitudinal covariant derivative of helicity curvature — EXACT
Write `R_H(v):=Curv_H(v)=H A_v-A_(Hv)`, so `4J_flip=R_H(u)u`.  Because `Lambda^2` commutes with `P_Leray,H` and derivatives, the Laplacian product commutator is
`[Lambda^2,R_H(v)]=R_H(Lambda^2v)-2sum_j R_H(partial_jv)partial_j`.    (20.215) Apply `partial_t+nu Lambda^2+Dcal_u` to `R_H(u)u` and use the true projected NS equation `partial_tu+nu Lambda^2u+Dcal_u u=0`.  The state/heat terms cancel identically, leaving
`4 C_J^sigma=([Dcal_u,R_H(u)]-R_H(Dcal_u u))u-2nu sum_j R_H(partial_j u)partial_j u`.    (20.216)
Thus the pressure-free obstruction (20.214) is exactly the **longitudinal covariant derivative** of the intrinsic helicity-curvature tensor along the actual projected NS trajectory, plus the genuine viscous carre-du-champ of that same tensor.  Ricci/Codazzi (20.209) fixes antisymmetric second derivatives through pressure curvature, but it does not determine this longitudinal component.  No additional forcing species remains to be named.
### 20.68 The helicity Hessian has one canonical free Codazzi block — EXACT
Define the intrinsic covariant Hessian `B_H(u,v):=[nabla_u,A_v]-A_(nabla_u v)`.  Differentiating `HA_v+A_vH=0` covariantly gives
`H B_H(u,v)+B_H(u,v)H=-{A_u,A_v}`.    (20.217)
Together with the Ricci identity (20.209), this yields the unique Gauss--Codazzi--Ricci split
`B_H(u,v)=C_H(u,v)-(1/2)H{A_u,A_v}+(1/2)[R(u,v),H]`, where `C_H(u,v)=C_H(v,u)`, `C_H(u,v)^*=C_H(u,v)` and `H C_H+C_H H=0`.    (20.218) Thus all diagonal Hessian blocks are fixed by the connection square, all antisymmetric second derivatives are fixed by pressure/Hodge curvature, and the only structurally free second derivative is the symmetric self-adjoint off-diagonal Codazzi tensor `C_H`. The projected NS equation and `[Lambda^2,A_u]=A_(Lambda^2u)-2sum_j A_(partial_j u)partial_j` give the exact connection law
`(partial_t+ad_(nabla_u)+nu ad_(Lambda^2))A_u=C_H(u,u)-H A_u^2-2nu sum_j A_(partial_j u)partial_j`.    (20.219) This identity was audited on full finite Fourier convolution; the residual was machine zero.  It is a connection equation, not a new energy law.
### 20.69 The ambient longitudinal Hessian is a true double-increment object — EXACT
Before Leray covariantization, put `B_H^amb(u,v):=[D_u,[D_v,H]]-[D_(D_u v),H]`.  If `K_H` is the kernel of `H`, incompressibility and one integration by parts give
`B_H^amb(u,v)f(x)=PV int nabla^2 K_H(x-y):(delta u tensor delta v) f(y)dy`.    (20.220)
Thus the ambient Hessian is symmetric in `(u,v)` and contains two actual velocity increments; Leray covariantization adds exactly the Hodge/Gauss geometry already typed in (20.203)--(20.209).  This is a physical-space origin for the second-order cancellation, not an extra locality estimate or source.
### 20.70 The Gauss square cancels from the longitudinal curvature rate — EXACT ANTI-SHORTCUT
For `R_H(v):=H A_v-A_(Hv)`, direct covariant differentiation gives `L_u R_H(u):=[nabla_u,R_H(u)]-R_H(nabla_u u)=A_u^2+H B_H(u,u)-B_H(u,Hu)-A_(A_u u)`.  Substituting (20.218) and `A_(Hu)=H A_u-R_H(u)` cancels the full `A_u^2` Gauss block and yields
`L_u R_H(u)=H C_H(u,u)-C_H(u,Hu)-(1/2)H{A_u,R_H(u)}-(1/2)[R(u,Hu),H]-A_(A_u u)`.    (20.221)
Hence the positive Riccati square in (20.201)--(20.202) is genuine but cannot own the final curvature rate: it disappears identically when the actual longitudinal derivative of `R_H` is formed.  The surviving terms are precisely the symmetric Codazzi tensor, intrinsic pressure/Ricci curvature and lower connection--curvature couplings.  No positive wallet is inferred from the Gauss square.
### 20.71 Sheet crossing is exactly curl/radial transport mismatch — EXACT
On one helical sheet `C u_h=h Lambda u_h`.  Since heat commutes with both `C` and `Lambda`, applying `partial_t+D_u-nu Delta` and projecting to the opposite sheet gives
`P_(-h)K_h=(1/2)Lambda^-1 P_(-h)[h[D_u,C]-[D_u,Lambda]]u_h`, and hence, by (20.204),
`P_(-h)A_u u=Lambda^-1 P_(-h)([D_u,C]-h[D_u,Lambda])u_h`.    (20.222) The curl defect is local and exact:
`[D_u,C]v=-sum_j grad(u_j) x partial_j v` for divergence-free `u,v`.    (20.223) Thus intrinsic helicity crossing is precisely the mismatch between material transport of curl and of radial frequency, after one true `Lambda^-1`; it is not an independent sheet-change source.  The radial commutator remains nonlocal, so no finite `L^2` rate budget is inferred from this identity.
### 20.72 Curl is a Killing endomorphism and locks helicity Codazzi to the radial Hessian — EXACT
Put `A_u^C:=[nabla_u,C]` and `B_C(x,u):=[nabla_x,A_u^C]-A_(nabla_xu)^C`.  Polarized Euler helicity conservation is exactly the Killing identity
`<A_u^C v,w>+<A_v^C w,u>+<A_w^C u,v>=0`.    (20.224)
Taking one covariant derivative gives the second Killing compatibility `sum_cyc <B_C(x,u)v,w>=0` for every divergence-free `x,u,v,w`.    (20.225)
Since `C=H Lambda`, with `L_x:=[nabla_x,Lambda]` and `B_Lambda(x,u):=[nabla_x,L_u]-L_(nabla_xu)`, the Hessians obey the exact product rule
`B_C(x,u)=B_H(x,u)Lambda+A_u L_x+A_x L_u+H B_Lambda(x,u)`.    (20.226)
Thus the symmetric off-diagonal Codazzi block of `H` cannot vary independently of radial transport: it must combine with the true `Lambda` connection/Hessian so that curl remains Killing.  The first curl connection is local, `A_u^C v=-P_Leray sum_j grad(u_j) x partial_jv`; in particular `A_u^C u=P_Leray[(omega.grad)u]` and `<omega,A_u^C u>=Q`.    (20.227)
So vortex stretching is one scalar reading of the same Killing connection whose factorization `C=H Lambda` constrains the final helicity Codazzi field.  The local curl-Hessian part does not vanish in the final combination, so (20.224)--(20.227) are compatibility identities, not a hidden positive budget.
### 20.73 Radial transport is the Poisson-resolved local viscous commutator — EXACT
For `L_u=[nabla_u,Lambda]`, the identity `Lambda^2=Lambda Lambda=-Delta` gives the Sylvester equation `{Lambda,L_u}=[nabla_u,Lambda^2]`, with `[nabla_u,Lambda^2]v=P_Leray[(Delta u.grad)v+2sum_j(partial_j u.grad)partial_jv]`.    (20.228)
On the nonzero Fourier spectrum the positive Sylvester operator is inverted exactly by `L_u=int_0^infinity e^(-sLambda)[nabla_u,Lambda^2]e^(-sLambda)ds`.    (20.229)
Differentiating once more gives `{Lambda,B_Lambda(x,u)}=B_(Lambda^2)(x,u)-{L_x,L_u}` and hence the same Poisson resolution of the radial Hessian.    (20.230)
In particular `W_Lambda=<u,L_u u>`.  Since `<f,[nabla_u,Lambda^2]f>=-2int S(u):(grad f grad f^T)dx`, putting `U_s=e^(-sLambda)u` and `G(u):=2int_0^infinity grad U_s grad U_s^T ds` yields
`G(u)>=0`, `int tr G(u)dx=||Lambda^(1/2)u||_2^2`, `W_Lambda=-int S(u):G(u)dx`.    (20.231)
Thus the nonlocal radial connection/Hessian entering the curl-Killing bridge (20.226) is an exact Poisson resolution of local commutators of the genuine viscous generator.  The PSD tensor `G` is only the critical stock in another representation; because its mass may diverge, (20.228)--(20.231) do not create a finite stress wallet.
### 20.74 Two-sided Poisson smoothing and sheetwise rigidity of the free Codazzi block — EXACT
Taking the adjoint of (20.226) and adding gives `{Lambda,B_H(x,u)}=2B_C(x,u)-{A_u,L_x}-{A_x,L_u}-{H,B_Lambda(x,u)}`; hence `B_H=int_0^infinity e^(-sLambda)Y_(x,u)e^(-sLambda)ds` with `Y_(x,u)` equal to that right side.    (20.232)
For `Z_Cod:=H C_H(u,u)u-C_H(u,Hu)u`, symmetry in the two arguments and `H C_H+C_H H=0` give `P_(-h)Z_Cod=-2h C_H(u_h,u)u_h`.    (20.233)
Since `Lambda` preserves the two sheets, `||Lambda^-1Z_Cod||_2^2=4sum_(h=+-1)||Lambda^-1 C_H(u_h,u)u_h||_2^2`.    (20.234)
Thus the genuinely free Codazzi contribution has exact two-sided Poisson smoothing but **no cancellation between its two output helicity sheets**; any divergence of this block must occur in at least one true sheet component.
### 20.75 Exact remaining theorem — OPEN
The surviving theorem is still:
> **No infinite critical full-state recycling.** A smooth true 3D incompressible Navier--Stokes trajectory on a finite interval cannot have one fixed positive hinge level `K_rad(R_kappa,t)=kappa` make unbounded UV excursions while the same true fields satisfy the mother force triangle, folded radial state/action law, genuine viscous front budget, growth family, tangent cancellation, the scale-amplified front law (20.47)--(20.54), the Volterra heat-square family (20.55)--(20.61), the observer-exhaustion/integrated accounting identities (20.62)--(20.64), the summed-family/full-field, secant-defect, heat-Gram, complete line-fiber and Leibniz-defect identities (20.65)--(20.234), and all full-pair/heat-fiber identities.
Equivalently: `Y=>bot`.
The sharpened chain is `fixed unbounded K_rad=kappa front`
`=>` cofinal scale-amplified true `Xi` and mother growth action
`=>` blow-up of both tail-growth square `G_2` and actual boundary-work square `J_2`
`=>` infinite cumulative actual work-rate input and `N/F_N` curvature input
`=>` the whole `kappa` family simultaneously forces critical-plus `N` forcing action divergence
`=>` (20.95)--(20.118) resum all quartet/companion curvature into the single true multiplier-gradient field `R_Lambda`, while (20.119)--(20.150) identify the actual critical supplier as the helicity-involution torsion `J_flip=(1/4)T_H(u,u)`, excise every fixed smooth/low-frequency background, and push the obstruction to all-three-roots UV;
`=>` the same torsion obeys the native child-heat law `(partial_t+nu Lambda^2)J_flip=S_J`, so finite singularity forces infinite UV `L_t^2 H_x^-1` action of the one true source `S_J=(1/2)T_H(u,N)-2nu sum_jJ_flip(partial_j u)`.
What is **not** proved is still `Y=>bot`, but the late Theory-2 reconstruction changes the correct formulation of the missing step.  Static full-convolution geometry is now more sharply exhausted: the moving flag supplies the old half derivative before contraction; the reciprocal lower bound `Q chi_geom^2/|p-p'|>=sqrt(6)/8` has an exact rational certificate; and reciprocal companion incidence has exact finite multiplicity (at most two preimages per canonical role) with Jacobian degeneration confined to the already-known source-null faces.  The old `global companion-incidence multiplicity` seam is therefore closed at the aligned static level.

The remaining obstruction should not be phrased as a request for an independent finite Codazzi wallet.  Equal-heat diamond geometry has the collision invariants `1,k_x,k_y,k_z,|k|^2`; the fifth invariant is exactly heat.  The physical logarithmic rate is `r_k=N_k/a_k-nu|k|^2`, so A+B controls the tangent/equal-heat geometry while the distinguished generator `-nu C^2` supplies the normal heat calibration.  Together with the exact mother/signature Korn observability and the acceleration identity `E Q'-(E/2)ddot R_0-W_Lambda^2=U(<Lambda u,Z_Cod>+C_compat)`, this retypes the final key as a **hypocoercive Polar--Korn coupling**: construct a modified energy whose cross term uses A+B, radial/heat compatibility and Curl--Killing to expose and retain the built-in negative square `-W_Lambda^2`, rather than estimating `Z_Cod` by a stand-alone `L_t^2H^-1` norm.

No such modified-energy inequality is proved here.  Thus global 3D regularity remains open, but the frontier has moved: the missing item is no longer an unidentified half derivative, reciprocal multiplicity, or new source species; it is the specific cross-term/coercivity mechanism needed to make one compulsory visibility-speed carrier time-integrable.
## 21. QED hook
Once Section 20 is proved, the existing composition is unchanged:
`T_*<infinity => X vee Y`,
`X=>bot`,
`Y=>bot`,
therefore `T_*<infinity=>bot` and `T_*=infinity`.
See `SOLUTION_MAP.md` for the short proof graph, `PHYSICAL_CORE.md` for the primitive identity/endpoint basis, and `MIXED_FRONTIER.md` for exhausted false-owner routes and the closed Clay-to-`S/V/O` upstream spine.
