# Rigidity Target, Falsifiers, and Remaining Gap

## 1. The target is a full-state theorem

The current application no longer searches for a singularity mechanism among separate observers.  The complete normalized state is governed by

\[
\boxed{
 v_\tau
 =B(v,v)-2W(v)\mathcal Sv,
 \qquad
 \mathcal S=x\cdot\nabla+\frac32,
 \qquad
 W(v)=\langle\Lambda v,B(v,v)\rangle,
}
\]

on the normalized manifold

\[
\boxed{
\mathcal M
=
\left\{
 v:
 \nabla\cdot v=0,
 \ \|v\|_2=1,
 \ \|\Lambda^{1/2}v\|_2=1
\right\}.
}
\]

A recurrent amplifying candidate is further forced into

\[
\boxed{
\mathcal M_0
=
\{v\in\mathcal M:\langle v,Cv\rangle=0\}.
}
\]

The final application theorem should therefore concern complete trajectories on \(\mathcal M_0\), not a scalar surrogate.

## 2. Proposed Full-Core Critical Rigidity theorem

A sufficiently strong final statement would be:

> **Full-Core Critical Rigidity (open target).** Every complete dynamically admissible trajectory of
> \[
> v_\tau=B(v,v)-2W(v)\mathcal Sv
> \]
> on \(\mathcal M_0\), arising as a normalized limit of smooth finite-energy Navier–Stokes trajectories, satisfies
> \[
> \boxed{
> \sup_{T>0}\int_0^T W(v(\tau))\,d\tau<\infty.
> }
> \]

Because

\[
A(\tau)=A(0)\exp\left(\int_0^\tau W(v(s))\,ds\right),
\]

this would rule out unbounded critical amplification in the normalized limit.

The phrase **dynamically admissible** matters.  A proof cannot classify arbitrary formal solutions of a quotient equation while ignoring whether they arise from the full formation law and its compactness limits.

## 3. Fixed-point subproblem

A first strict subproblem is the zero-helicity dilation equation

\[
\boxed{
B(v,v)=b\left(x\cdot\nabla+\frac32\right)v,
\qquad
b>0,
\qquad
\langle v,Cv\rangle=0.
}
\]

A theorem excluding every nonzero finite-energy genuinely three-dimensional solution would rule out exact self-similar/dilation-locked normalized profiles.

This is not enough by itself: recurrent, almost-periodic, splitting, or noncompact normalized trajectories must also be excluded.

## 4. Why several tempting shortcuts are false

### 4.1 No pointwise positive-spectrum exclusion

Exact smooth finite-dimensional states can align very strongly with positive critical curvature spectrum.  Therefore a theorem of the form

\[
\lambda_{\max}(\mathscr R_u)\le\nu
\]

or "the state cannot occupy the positive eigenspace" is too strong and is false as a universal principle.

### 4.2 No scalar Euler Lyapunov shortcut

The Euler part is reversible.  Finite invariant subsystems can display monotone critical growth over long intervals while remaining globally smooth and bounded.  A sign-definite scalar Euler Lyapunov cannot be assumed.

### 4.3 No finite-cell holonomy shortcut

Finite interaction cells may be phase locked or flat.  Even a fixed fractional phase frustration does not dominate cubic nonlinear growth at arbitrarily large amplitude.  Holonomy is useful structural information but not, by itself, an endpoint regularity proof.

### 4.4 No static high-tail barrier

Quadratic ancestry can seed a new tail from the previous octave.  A target-frequency tail can have zero first derivative and positive second derivative even when initially empty.  The proof must therefore follow the closure genealogy of the complete core state.

### 4.5 No "two derivatives beat one" budget proof

At critical scaling, a packet with critical mass of order \(\nu^2\) can balance one-derivative Euler production against two-derivative viscosity.  Energy and parabolic timescale sums alone do not contradict an infinite cascade.

## 5. What finite-dimensional anti-models actually prove

Every fixed finite \((T,C)\)-closed Galerkin system is global because its energy is bounded and its dynamics is a smooth polynomial ODE.  Such systems can nevertheless realize:

- positive critical curvature;
- strong state/eigenvector locking;
- recurrent lock/release cycles;
- one-step spectral transfer;
- phase-locked triad geometries.

These facts show that none of the listed local phenomena equals blow-up.  A singularity, if it exists, must be an infinite-dimensional migration/noncompactness phenomenon.

## 6. Interaction closure and information completeness

In a Fourier–helical basis, define the core coefficients

\[
T_{\alpha\beta\gamma}
=\langle e_\alpha,[e_\beta,e_\gamma]\rangle.
\]

Active interactions define an incidence map \(A_T\) on modal phases.  The nullspace

\[
\ker A_T
\]

encodes phase transformations invisible to the active interaction complex; with sufficiently connected full interactions this collapses to physical translation gauge.  The dual space

\[
\ker A_T^*
\]

encodes cycle compatibility/holonomy constraints.

This explains the historical hidden-phase phenomenon without discarding information: an observer that disconnects the interaction complex artificially enlarges \(\ker A_T\).  Restoring the complete core restores the missing constraints.

For the regularity problem, however, finite cycle frustration is not the final theorem.  The remaining enemy can continually enter new interaction closure sectors.  The required rigidity statement is therefore an **infinite-closure compactness theorem** for the full core.

## 7. Candidate compactness formulation

After quotienting the exact Euclidean gauges and, on \(\mathbb R^3\) or a rescaled blow-up chart, normalizing amplitude/dilation, suppose

\[
v_n\rightharpoonup v,
\qquad
\|v_n\|_2=\|\Lambda^{1/2}v_n\|_2=1.
\]

The dangerous possibility is a nonzero critical interaction defect at infinity: the cubic core pairing may fail to pass to the weak limit because of concentration, oscillation, or profile splitting.

Schematically, the missing theorem must force

\[
\boxed{
W(v_n)=\langle\Lambda v_n,B(v_n,v_n)\rangle
\longrightarrow
W(v)
}
\]

for every dynamically relevant normalized sequence with persistent nonnegative drift, after extraction of the exact Euclidean/dilation gauges.

This is not a claim that arbitrary bounded sequences in the critical space are compact.  It is a proposed **dynamic compactness** statement using the fact that the sequences are generated by the single Navier–Stokes formation core.

## 8. Endgame logic if the target is proved

The intended implication chain is:

\[
\boxed{
\text{hypothetical finite-time singularity}
}
\]

\[
\Downarrow
\]

\[
\boxed{
A(t)=\|u(t)\|_{\dot H^{1/2}}\to\infty
\text{ along a critical sequence}
}
\]

\[
\Downarrow\quad\text{normalize amplitude and dilation}
\]

\[
\boxed{
\text{complete normalized full-core trajectory on }\mathcal M_0
}
\]

\[
\Downarrow
\]

\[
\boxed{
\int W(v(\tau))\,d\tau\to+\infty
}
\]

\[
\Downarrow\quad\textbf{Full-Core Critical Rigidity}
\]

\[
\boxed{\text{contradiction}.}
\]

The final bold arrow is open.  This folder documents the reduction to that arrow; it does not claim that the arrow has already been proved.

## 9. Recommended next mathematical attacks

Any continuation of this programme should remain at full-core level.  High-value directions are:

1. derive compactness identities directly from the normalized equation, rather than estimating pressure or a projected observer;
2. classify the exact zero-helicity dilation equation and its possible finite-energy solutions;
3. study concentration/profile-splitting compatibility with the complete interaction tensor \(T\) and curl grading \(C\);
4. exploit the exact relation between the normalized drift \(W\), helicity decay in quotient coordinates, and interaction closure;
5. formulate a dynamic defect measure that retains the complete \((T,C)\)-coupling rather than only radial spectral mass.

The programme should be considered successful only when the final rigidity statement is proved without silently replacing the full state by a lower-information shadow.
