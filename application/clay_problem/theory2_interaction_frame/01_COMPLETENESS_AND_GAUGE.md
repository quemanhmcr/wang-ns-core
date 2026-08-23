# 01 — Completeness, gauge, profile topology, and boundary bookkeeping

## Status

Structural statements are `EXACT`; compactness assertions are labelled `OPEN` or `DEDUCTION`.  The purpose of this note is to prevent the finite-density programme from reintroducing information loss while changing coordinates.

## 1. Safe physical ontology — EXACT

Theory 2 gives

\[
\boxed{
\Sigma(u)\longleftrightarrow E_u\longleftrightarrow u.
}
\tag{1.1}
\]

No scalar shell stock, current, spectral occupation, affine defect, or coherent packet is complete.  These may be used as locators or coercive quantities, but a reader kernel is never promoted to a physical-state kernel.

## 2. Anchored interaction frame preserves information — EXACT

For a true smooth trajectory,

\[
U_t=-\Gamma_uU,
\qquad U(t_0)=I,
\qquad v=U^*u.
\]

Hence

\[
\boxed{u=Uv.}
\tag{2.1}
\]

The pair `(U,v)` obeys the closed equivalent system

\[
\boxed{
\begin{cases}
U_t=-\Gamma_{Uv}U,\\
v_t=-\nu(U^*CU)^2v,
\end{cases}}
\tag{2.2}
\]

with the anchor retained.  The interaction frame is therefore a coordinate transform, not a quotient.

## 3. Gauge warning for `(v,C^sharp)` — EXACT

The identity

\[
C^\sharp=U^*CU
\]

does not uniquely reconstruct `U`.  Curl-commuting unitary transformations give the familiar vertical gauge.  Therefore

\[
\boxed{
(v,C^\sharp)\text{ is an exact pathwise renderer but is not, by itself,
a proved complete autonomous state.}
}
\tag{3.1}
\]

Whenever a standalone interaction-frame argument is used, the anchored `U` or an equivalent gauge reconstruction must remain available.

## 4. Signed-flag tangent algebra — EXACT

The shifted flag

\[
H_a=\operatorname{sgn}(C-aI)
\]

is an involution, not a projection.  Away from threshold kernel,

\[
H_a^2=I,
\qquad
\{H_a,A_a\}=0.
\tag{4.1}
\]

With

\[
P_a^\pm=\frac12(I\pm H_a),
\]

one has

\[
P_a^+A_aP_a^+=P_a^-A_aP_a^-=0.
\tag{4.2}
\]

Thus `A_a` moves information across the signed-curl split and remembers matrix channels that may cancel only after the operator acts on the physical state.

For a finite collection of channel vectors `B_i` with signed input radii

\[
\lambda_1<\cdots<\lambda_m,
\qquad
\sum_iB_i=0,
\]

the sign-flag resolved cancellation satisfies the exact partial-sum identity

\[
\boxed{
\int_{\mathbb R}
\left|
\sum_i\operatorname{sgn}(\lambda_i-a)B_i
\right|^2da
=
4\sum_{j=1}^{m-1}
(\lambda_{j+1}-\lambda_j)
\left|\sum_{i>j}B_i\right|^2.
}
\tag{4.3}
\]

Hence source cancellation across separated signed-curl radii leaves a quantitative complete-flag footprint unless cancellation occurs level by level.

## 5. Translation profile decomposition lifts to the complete state — EXACT on fixed windows

Let `Q_L` be a fixed relative-frequency window.  Suppose

\[
Q_Lu_n
=
\sum_{\ell=1}^J T_{x_n^\ell}\phi^\ell+r_n^J,
\qquad
|x_n^\ell-x_n^k|\to\infty.
\tag{5.1}
\]

Because `u -> E_u`, `u -> A_a(u)`, and `u -> O_a(u)` are linear and translation-covariant,

\[
E_{Q_Lu_n}
=
\sum_\ell
T_{x_n^\ell}E_{\phi^\ell}T_{-x_n^\ell}
+E_{r_n^J},
\tag{5.2}
\]

and likewise for `A_a` and `O_a`.

Thus a fixed-window profile decomposition is a **complete Theory-2 decomposition**, not merely an amplitude decomposition.  When matrix blocks of the full `E_u` are needed, enlarge the velocity window by a fixed amount because an entry `(k,q)` uses the coefficient `u_{k-q}`.

## 6. Dynamic cocompactness — OPEN

The desired theorem is:

\[
\boxed{
\text{finite-band translation-cocompactness propagates over bounded
normalized time in a uniformly compact complete background.}
}
\tag{6.1}
\]

The clean route is an adjoint Duhamel argument.  A terminal bandlimited packet detecting a child profile is propagated backward through the adjoint linearized parabolic equation around the coherent background.  Spatially escaping profiles have vanishing pairings; quadratic cocompact remainders are then treated perturbatively.

A simple statement that the heat semigroup has a bounded inverse on a fixed annulus is not enough, because the linearized NS flow mixes frequencies.

If (6.1) is proved, a coherent child event must inherit a coherent ancestor or receive a fixed local Duhamel forcing from a coherent profile.  This is the key spacetime inheritance theorem used by the causal-ray construction.

## 7. Projective finite-window topology — DEFINITION

Global strong `H^{1/2}` compactness is false for a finite-density staircase: old generations may carry an unbounded total critical norm while moving to relative IR.

The natural local topology is the projective family

\[
\boxed{
\mathcal X_{\rm loc}^{T2}
=
\varprojlim_{L\to\infty}
\left(
Q_{[-L,L]}u,
QEQ,
QA_aQ,
Q\mathscr O_aQ
\right).
}
\tag{7.1}
\]

Convergence means strong complete-state convergence on every bounded relative log-frequency window, modulo physical translation and compact rotation extraction.

This topology retains every fixed finite negative shell, but it does **not** by itself remember mass that escapes to the endpoint `j=-infinity`.

## 8. The IR boundary is an additional complete defect — DEFINITION/OPEN

Because the projective topology cannot distinguish defects moving to relative `-infinity`, the honest limiting object is

\[
\boxed{
\Sigma_{\rm ext}
=(\Sigma_{\rm loc}^{T2},\mathfrak W_{\rm IR}).
}
\tag{8.1}
\]

Here `W_IR` is an operator-valued logarithmic boundary state constructed, if possible, by Mellin/Abel averaging of rescaled complete blocks of

\[
E,\qquad A_a,\qquad \mathscr O_a.
\]

The scalar IR anomaly developed in `04` is only one pairing of this boundary state.  A rigorous construction must rescale the flag parameter together with physical scale and specify a weak operator topology.

## 9. One-way IR bookkeeping — target theorem

In backward similarity variables a physical frequency that is no longer regenerated at larger physical scale satisfies

\[
\kappa_{\rm rel}(s)=K_{\rm phys}e^{-s/2}.
\]

Thus fixed old packets move monotonically toward relative IR.  This kinematic fact is exact, but the stronger statement

\[
\boxed{
\text{a sufficiently far-IR complete defect cannot regenerate an }O(1)
\text{core contribution before being swept farther IR}
}
\tag{9.1}
\]

is an analytic theorem.  Finite density suggests the mechanism: at relative scale `kappa<<1`, nonlinear/parabolic response is `O(kappa^2)` while similarity dilation sweeps log-frequency at order one.  `04` records the required one-way decoupling estimate.

## 10. Anti-loop discipline

The following moves are forbidden:

- calling `(v,C^sharp)` complete without retaining/reconstructing gauge;
- treating `H_a` as a projection;
- replacing the complete state by the spectral measure `rho`;
- treating projective local convergence as global critical compactness;
- discarding the IR boundary because it disappears from every finite relative window;
- converting a shell/profile reader into a state variable simply because it is convenient for an estimate.

The point of the new compactness programme is to arrive at one honest complete broadband enemy, not to make noncompact information disappear by notation.