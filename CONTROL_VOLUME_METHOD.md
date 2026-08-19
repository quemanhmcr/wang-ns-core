# Control-Volume Method: Let Navier–Stokes Do the Accounting

This file records a proof discipline, not a new theorem, source, budget or ontology.  The observer may choose an unusually clever family of control volumes; the observer may not alter what Navier–Stokes is allowed to do.

## 1. The predecessor identity

For every fixed physical Fourier/helicity mode set `A`, exact modal energy continuity is

`E_A(t1) + D_A[t0,t1] + Phi_out,A[t0,t1] = E_A(t0) + Phi_in,A[t0,t1]`,

with `D_A=2nu int_(t0)^(t1)||Lambda P_Au||_2^2 dt`.

This one identity already types the kinetic-energy accounting.  Existing stock and actual boundary inflow are the only suppliers.  Final stock, genuine viscosity and actual boundary outflow are the only destinations.  Internal circulation cancels.  A label that does not appear in this continuity law does not acquire a kinetic-energy wallet merely because a proof would like one.

The important lesson is methodological: **do not first invent a mechanism and then ask Navier–Stokes to fund it.  First choose a physical control volume and ask the exact equation what crosses its boundary.**

## 2. One control volume is useful; a family can reveal the law

Choose a nested family `A_theta` of actual mode sets.  For each member define its true nonlinear boundary work

`F(theta,t)=2 Re <P_theta u,P_theta N>`, `N=-P(u.grad u)=u_t+nu Lambda^2u`.

Then every member obeys

`dE_(A_theta)/dt + 2nu||Lambda P_theta u||_2^2 = F(theta,t)`.

`theta` is an observer coordinate, never a physical clock.  The power comes from choosing the family so that differentiation, integration or folding in `theta` exposes identities already forced by NS.  The family does not create physics; it makes hidden accounting visible.

## 3. Signed curl is the model example

Put `x=s|k|` and choose `Omega_a={x>a}`.  Let `dW(x,t)` be the pushforward of the one actual signed modal-work law and

`F(a,t)=int_(x>a)dW = 2 Re <P_a u,P_a N>`.

Define the hinge potential

`Psi(a,t)=int (x-a)_+ dW(x,t)=int_a^infinity F(b,t) db`.

Energy and helicity conservation are exactly `int dW=0` and `int x dW=0`.  They become boundary conditions on the same profile.  Critical production, radial flux and vortex stretching are no longer separate stories; they are different readings of this one family.

With `C=curl`, the mother law gives the quadratic full-state action profile

`A(a)=|| |C-a|^(1/2)Lambda^(-1)N||_2^2-|| |C-a|^(1/2)Lambda^(-1)u_t||_2^2+nu^2|| |C-a|^(1/2)Lambda u||_2^2 = 2nu Psi(a)`.

Hence, distributionally,

`F(a)=-(2nu)^(-1) A'(a)`, `dW=(2nu)^(-1)A''`, `A(0)=nu P_(1/2)^NL`, and `int A(a) da=2nu Q`.

Height, slope, curvature and area of one full-state profile recover critical work, actual cut flux, modal work and vortex stretching.  Apparent mechanisms collapse back to one exact NS object viewed through different control volumes.

## 4. What a sufficiently sharp family can force

On smooth finite-energy `R^3`, positive critical production forces a single-helicity tail `P` with zero nonlinear kinetic work but positive critical work `H=2<Lambda Pu,PN> >0` (equivalently, helicity transfer with the sign of that helicity sector).  If `U=Pu`,

`mu=<Lambda U,U>/||U||_2^2`, `V=(Lambda-mu)U`, `S=||V||_2^2`,

then the true nonlinear acceleration splits exactly as

`PN=[H/(2S)]V + N_perp`, with `<U,N_perp>=<Lambda U,N_perp>=0`.

Thus all first-moment radial hardening is carried by one forced direction; phase, polarization and same-heat complexity are isolated in a moment-orthogonal remainder.  This separation was not assumed.  It was extracted by asking the right family of exact control-volume questions.

## 5. Reduce every apparent mechanism to state / flux / source / sink

- **State:** actual `u`, `omega`, modal stock and occupied control-volume stock.
- **Flux:** actual nonlinear boundary work across a named physical mode set.
- **Source/curvature field:** the genuine NS acceleration `N`, and when time curvature is needed, `F_N` or `G=curl N`; none is a second global kinetic-energy supplier.
- **Sink:** true viscosity.  Cancellation deficits, geometric variance and observer motion are not dissipation.

If a proposed object cannot be placed in one of these roles by an exact NS identity, keep it a reader.  Do not promote it to an owner, event, currency or causal road.

## 6. Working protocol

1. Start from the true state and PDE, not from a norm, graph or recurrence language.
2. Choose a physical control volume before estimating anything.
3. Write its exact continuity identity before naming branches or mechanisms.
4. Replace an isolated cut by a family adapted to a true invariant or generator: radius, signed curl, helicity, heat rate, or another exact NS coordinate.
5. Push forward the actual work once; never manufacture a second Hahn law after coarse-graining.
6. Use family derivatives, moments, folds and level sets only as readers of the same work.
7. When instantaneous traffic no longer determines dynamics, return to the full fields `u,N,F_N,G`; do not invent a repair mechanism.
8. Stress-test every claimed rigidity against exact triads, full-polarization pairs, finite-Fourier states and continuum cancellation.
9. Use estimates only after the physical object and exact road are already identified.

## 7. The standard failure modes

Do not count internal circulation as fresh supply.  Do not turn a cutoff into a clock, a first contact into a cause, a moving-boundary term into physical dissipation, a cancellation deficit into a budget, a pair atom into a full-mode statement before summing polarizations, or a divergent norm into a mechanism.  Do not ask NS to obey a genealogy created by the proof.

The preferred contradiction is always internal: **the same actual NS state, flux or source is forced by exact laws into two incompatible states.**  Before proving a human-made intermediate claim, ask whether a sufficiently cunning family of control volumes makes that claim unnecessary.

## 8. The reusable principle

> **Respect Navier–Stokes completely; be ruthless only with the observer.  Choose the control-volume family so cleverly that Navier–Stokes itself reduces the apparent chaos to exact accounting.**

For the current implementation of this method see `PHYSICAL_CORE.md` and the mother-law reconstruction in `BSVO_FULL_STATE_FRONTIER.md`.
