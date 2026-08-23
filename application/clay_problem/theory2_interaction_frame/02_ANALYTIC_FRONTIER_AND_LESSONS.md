# 02 — Analytic frontier: finite density, leading edge, and causal rays

## Status

This note separates already-certified deductions from the two analytic lemmas that now control the finite-density compactness programme.  Nothing here proves global regularity.

## 1. Finite-density versus infinite-density branches — EXACT split

Define the critical shell density

\[
\mu_j(t)=2^j\|P_ju(t)\|_2^2,
\qquad
\mu_{\rm sh}(t)=\sup_j\mu_j(t).
\]

The two branches are

\[
\boxed{
\sup_{t<T_*}\mu_{\rm sh}(t)<\infty
}
\tag{1.1}
\]

and

\[
\boxed{
\mu_{\rm sh}(t_n)\to\infty
\quad\text{for some }t_n\uparrow T_*.
}
\tag{1.2}
\]

The present directory targets (1.1).  The infinite-density branch remains an amplitude/strain concentration problem and is not automatically an affine branch.

If a finite-time singularity occurs while (1.1) holds, then

\[
\|u(t)\|_{\dot H^{1/2}}^2
\simeq\sum_j\mu_j(t)\to\infty
\]

forces a multiplicity explosion: the number/logarithmic width of active critical scales diverges while each shell height stays bounded.

## 2. Finite density gives critical Morrey control — EXACT

For `r ~ 2^{-J}`, finite density gives

\[
\|P_{\le J}u\|_\infty
\lesssim \frac{\sqrt M}{r},
\qquad
\|P_{>J}u\|_2^2\lesssim Mr.
\]

Therefore

\[
\boxed{
\sup_{x,r>0}
\frac1r\int_{B_r(x)}|u|^2
\lesssim M.
}
\tag{2.1}
\]

This is the critical Morrey signature of the formal `1/|x|` scaling.  It does **not** by itself imply global weak-`L^3` on `R^3`; additional global distribution/tightness would be needed.

After normalizing a top shell to frequency one, remote IR obeys for every `m>=0`

\[
\boxed{
\|\nabla^mP_{\le2^{-L}}U\|_\infty
\lesssim_M2^{-(m+1)L}.
}
\tag{2.2}
\]

Thus old finite-density wake is locally smooth and weak at the current front scale.

## 3. Three-scale locality — certified geometry

For one ordered Fourier interaction `p+q=k`, the critical commutator coefficient contains

\[
\big||k|-|q|\big|\,|\widehat u_p\cdot q|.
\]

Incompressibility yields

\[
|\widehat u_p\cdot q|
\le\min(|q|,|k|)|\widehat u_p|.
\]

After critical shell normalization the deep high--high--low regime has the aggregate loss

\[
\boxed{(L/H)^2.}
\tag{3.1}
\]

Hence sufficiently deep scale jumps contribute an arbitrarily small fraction of the critical drive under bounded shell density.  This is an aggregate locality theorem, not a unique genealogy theorem.

## 4. Leading-edge shell inequality — OPEN prove-now lemma

Put

\[
a_j=2^{j/2}\|P_ju\|_2,
\qquad
s_j=2^{2j}t.
\]

The target shell inequality has the form

\[
\boxed{
\partial_{s_j}a_j+c\nu a_j
\lesssim
\left(\max_{|k-j|\le L}a_k\right)^2
+a_j\sum_{p\le j-L}2^{-2(j-p)}a_p
+\sum_{k\ge j+L}2^{-(k-j)}a_k^2.
}
\tag{4.1}
\]

The three terms represent comparable-scale quadratic forcing, deep-IR shear of an already existing high mode, and high--high production of a lower output.

The important point is historical: a static bound `a_j<epsilon` does not forbid a remote `0.99 epsilon` bump.  The UV tail must be propagated from the smooth initial data by a spacetime first-exit argument.

Let `J(t)` be the highest `epsilon`-active shell and

\[
b_m(t)=\sup_{j\ge J(t)+mL}a_j(t).
\]

At the first exit from a barrier `theta_m`, (4.1) should give

\[
\partial_{s_j}a_j
\le
-\frac{c\nu}{2}\theta_m
+C\theta_{m-1}^2
+C\theta_m^2.
\tag{4.2}
\]

Choosing

\[
\boxed{\theta_m=A\nu^{-1}\theta_{m-1}^2}
\tag{4.3}
\]

with `theta_0=epsilon<<nu` yields a negative first-exit derivative.  The desired conclusion is

\[
\boxed{
b_m(t)\lesssim\theta_m,
\qquad\theta_m\downarrow0\text{ super-geometrically}.}
\tag{4.4}
\]

The moving base `J(t)` and reindexing at record jumps are the main technical bookkeeping issue.

## 5. Consequences of the historical barrier — DEDUCTION if (4.4) holds

After normalizing the current front to `J=0`, the super-geometric UV tail implies uniform bounds

\[
\boxed{
\|U\|_{\dot H^s}\le C_{s,M,\nu}
\qquad\text{for every fixed }s>\frac12
}
\tag{5.1}
\]

if the quadratic barrier persists at all depths.  The IR half is summable because

\[
\sum_{j<0}2^{(2s-1)j}\mu_j
\le M\sum_{j<0}2^{(2s-1)j}.
\]

These supercritical norms are auxiliary compactness controls, not state variables.

They supply one-sided UV tightness, continuity of the complete Mother/flag maps on fixed windows, and the uniform integrability later needed for Abel endpoint limits.

## 6. Active-time estimate — OPEN flux lemma, then DEDUCTION

For `lambda<<1`, finite density gives

\[
E_{\ge\lambda}:=\|P_{\ge\lambda}u\|_2^2
\lesssim\frac M\lambda,
\tag{6.1}
\]

and

\[
\|\nabla P_{\le\lambda}u\|_\infty
\lesssim\sqrt M\lambda^2.
\tag{6.2}
\]

The clean target is a high-pass kinetic-energy flux estimate

\[
\boxed{|\Pi_\lambda(u)|\lesssim M^{3/2}\lambda.}
\tag{6.3}
\]

It would imply

\[
\nu\int_0^S D_{\ge\lambda}^{\rm kin}(s)\,ds
\lesssim
\frac M\lambda+M^{3/2}\lambda S.
\tag{6.4}
\]

With `lambda=S^{-1/2}` and

\[
\mathcal A_S=\{s\in[0,S]:\mu_0(s)\ge m_0\},
\]

one obtains

\[
\boxed{
|\mathcal A_S|
\lesssim_{M,\nu,m_0}\sqrt S.
}
\tag{6.5}
\]

Hence a fixed normalized scale cannot remain active with positive asymptotic time density.  This excludes a large class of zero-scale recurrent enemies without using helicity or branch counting.

## 7. Record-time critical production — EXACT

Let

\[
Q(t)=\|u(t)\|_{\dot H^{1/2}}^2,
\qquad
D(t)=\|u(t)\|_{\dot H^{3/2}}^2.
\]

At first hitting times `t_n` of record levels `Q(t_n)->infinity`,

\[
Q'(t_n)\ge0
\]

and therefore

\[
\boxed{\mathcal T(t_n)\ge\nu D(t_n).}
\tag{7.1}
\]

Interpolation with finite kinetic energy gives

\[
\boxed{
D(t_n)\gtrsim\frac{Q(t_n)^3}{\|u_0\|_2^4}\to\infty.
}
\tag{7.2}
\]

After a whole-triad bounded-ratio decomposition and removal of deep interactions, one should extract arbitrarily high windows with a fixed heterochiral production/dissipation ratio.  That localization is an `OPEN` macroblock lemma; one must localize closed-triad production, not merely shell influx.

## 8. Coherence and co-located helicities — DEDUCTION after record-block extraction

On a fixed normalized window, finite density bounds the `L^2` mass.  A fixed production ratio gives a lower bound on physical coherence

\[
\chi_B
=\frac{\|Q_BU\|_\infty}{\|Q_BU\|_2}
\ge\chi_0>0,
\tag{8.1}
\]

and fixed lower masses in both helical sectors.  Translation-profile decoupling then implies that some productive profile contains the `+` and `-` components in the same spatial translation profile; separated opposite helicities cannot carry a fixed heterochiral trilinear current.

The inverse-Bernstein Riesz atom locates one coherent component, but a single radial evaluation atom has zero critical production by parity.  Therefore an efficient motor has a fixed-size internal phase/polarization component beyond that atom.

## 9. Causal record ramps and Type-I-like ray — OPEN/DEDUCTION split

Choose record activations separated by a fixed number `B` of dyadic shells.  If the leading-edge barrier keeps shell `j+B` below a small fraction of threshold until it is born, a normalized shell-speed bound gives

\[
t_{j+B}-t_j\gtrsim2^{-2(j+B)}.
\tag{9.1}
\]

Summing ordered future record gaps yields

\[
\boxed{T_*-t_j\gtrsim2^{-2j}.}
\tag{9.2}
\]

The reverse bound requires the `OPEN` complete causal profile-inheritance theorem: a coherent child event carrying fixed Duhamel/radial-flag current over one parabolic time must have a coherent lower/comparable parent in a bounded spatial and log-scale neighborhood.

For a record graph, coarse-grain by a fixed number of dyadic record shells so that

\[
K_{n+1}\ge R_0K_n,
\qquad R_0>1.
\]

Finite branching then gives an infinite ray

\[
(t_n,x_n,K_n,\Sigma_n)
\]

with

\[
K_{n+1}\ge R_0K_n,
\qquad
t_{n+1}-t_n\lesssim K_n^{-2},
\qquad
|x_{n+1}-x_n|\lesssim K_n^{-1}.
\tag{9.3}
\]

Geometric summation gives

\[
T_*-t_n\lesssim K_n^{-2},
\qquad
|x_n-x_*|\lesssim K_n^{-1}.
\tag{9.4}
\]

Combining with (9.2),

\[
\boxed{
K_n^2(T_*-t_n)\asymp1,
\qquad
|x_n-x_*|\lesssim\sqrt{T_*-t_n}.
}
\tag{9.5}
\]

Thus Type-I-like causal centering is a consequence of two explicit analytic lemmas, not an assumption.

## 10. Current compactness frontier

The finite-density compactness programme is now reduced to proving:

1. the historical leading-edge barrier (4.4), including the moving-record induction;
2. high-pass/active-time control such as (6.3)--(6.5);
3. dynamic translation-cocompactness and causal profile inheritance over bounded normalized times;
4. minimality strong enough to remove spatial satellites while retaining a nontrivial complete record ray.

Once these close, `04` passes to backward similarity variables and treats the old staircase as an outgoing IR boundary rather than as a returning reservoir.