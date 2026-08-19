# `B/S/V/O` Full-State Frontier — Mother-Law Form

This is the canonical remaining proof block after the representation/owner frontier has been exhausted.  It is organized from true Navier--Stokes state laws outward, not from a cancellation taxonomy inward.  It does **not** claim `Y=>bot` or global regularity.

`B` means the already-canonical minority-helicity positive-critical nonlinear-work branch; it is not a fourth sidecar fate.  The exact sidecar theorem remains `Y => S vee V vee O`.  The missing theorem remains

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

Hence every non-affine repair/reshaping in Sections 11--12 belongs to true `N/G/F_N` dynamics.

## 14. Pressure remains Hodge completion, not a second road — EXACT

Let `A=grad u=S+Omega`, `g=-Delta p=|S|^2-|omega|^2/2`, `M=S^2+Omega^2`, and `R=M+Hess p=-(D_tS-nu Delta S)`.
For nonzero output `q`, `e=q/|q|`, Piola gives the Householder reflection

`Rhat(q)=Mhat(q)-2<Mhat(q),e tensor e>_F e tensor e`,
`|Rhat(q)|_F=|Mhat(q)|_F`.    (14.1)

Equivalently,

`2||D_tS-nu Delta S||_2^2=||S omega||_2^2+||Delta p||_2^2`.    (14.2)

Pressure redistributes the geometry of the same state; it does not mint kinetic-energy supply or a second acceleration magnitude.

## 15. Dangerous `B/O` atomic geometry survives inside the new full-state spine — EXACT

For a true far-UV low-donor triad with opposite-helicity high roots, the low root is the signed middle root, both high roots are recipients, `Z_tau>0`, every radial-cut flux of that triad is nonnegative, and the critical production is positive minority-helicity `B` work.

If the high pair has the same helicity, the radial profile is a loop with a farther high donor and critical production zero or negative.  Therefore a true `O` atom whose recipient is radially outermost in its triad lies on the opposite-high positive-critical `B` arch.

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

The remaining theorem may now be stated more sharply:

> **No infinite critical full-state recycling.**  A smooth true 3D incompressible NS trajectory on a finite interval cannot repeatedly realize unbounded-scale positive-critical regeneration while the same true fields `u,N,F_N/G` satisfy the mother force triangle, the signed-curl action-profile identities, the neutral-helicity-tail hardening law, the forced sorter decomposition, the opposite viscous radial-shape projection, and all full-pair/heat-fiber convolution identities.

Equivalently, under the already-proved endpoint grammar: `Y=>bot`.

The especially sharp unresolved subproblem is:

`late UV hard B-regeneration`
`=>` `late UV neutral-helicity flux-reversal tail`
`=>` repeated regeneration of `[H/(2S)](Lambda-mu)U` by the moment-orthogonal `N_perp/F_N` dynamics at `R->infinity`,

and then prove that this true-state process cannot continue to a finite endpoint.

What is **not** yet proved:

- that neutral radii from Section 6 must track the hard-shell sequence to unbounded UV;
- that `N_perp` must synchronize affinely;
- that action-hump height is monotone or a finite resource;
- that large `Q`, Lamb action or source-square diagnostics alone contradict smoothness;
- that a selected pair/triad survives full-convolution cancellation.

Any closure must be an incompatibility among true NS state laws, not a new token, budget, observer clock, genealogy or estimate-defined mechanism.

## 21. QED hook

Once Section 20 is proved, the remaining composition is already assembled:

`T_*<infinity => X vee Y`,
`X=>bot`,
`Y=>bot`,
therefore `T_*<infinity=>bot` and `T_*=infinity`.

See `SOLUTION_MAP.md` for the short proof graph, `PHYSICAL_CORE.md` for the primitive identity basis, `MIXED_FRONTIER.md` for the exhausted false-owner routes, and `FOURTH_DOCUMENT_FINAL_EXHAUSTION.tex` for the conditional endpoint composition.
