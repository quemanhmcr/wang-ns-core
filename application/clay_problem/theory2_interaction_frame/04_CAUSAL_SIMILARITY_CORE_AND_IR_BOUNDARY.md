# 04 — Causal similarity core and the outgoing IR boundary

## Status

This note is the compactness/renormalization bridge for the finite-density branch.  Kinematic similarity identities are `EXACT`; the historical leading-edge barrier, causal profile inheritance, one-way IR decoupling, and Abel-boundary construction are `OPEN` unless stated otherwise.

## 1. From a causal record ray to backward similarity coordinates

Assume the finite-density programme has produced a complete causal record ray

\[
(t_n,x_n,K_n,\Sigma_n)
\]

with

\[
K_{n+1}\ge R_0K_n,
\qquad R_0>1,
\]

\[
t_{n+1}-t_n\lesssim K_n^{-2},
\qquad
|x_{n+1}-x_n|\lesssim K_n^{-1},
\]

and the historical leading-edge barrier supplies the reverse timing bound.  Then

\[
\boxed{
K_n^2(T_*-t_n)\asymp1,
\qquad
|x_n-x_*|\lesssim\sqrt{T_*-t_n}.
}
\tag{1.1}
\]

Introduce backward similarity variables

\[
y=\frac{x-x_*}{\sqrt{T_*-t}},
\qquad
s=-\log(T_*-t),
\qquad
V(y,s)=\sqrt{T_*-t}\,u(x,t).
\tag{1.2}
\]

Along the causal ray, the active front remains at

\[
|\xi|\sim1,
\qquad
|y|\lesssim1.
\tag{1.3}
\]

This is a derived Type-I-like centering of the selected causal front, not an assumed global Type-I bound.

## 2. Similarity drift of old physical scales — EXACT

A Fourier packet that remains at a fixed physical frequency `K_phys` has relative similarity frequency

\[
\boxed{
\kappa_{\rm rel}(s)
=K_{\rm phys}\sqrt{T_*-t}
=K_{\rm phys}e^{-s/2}.
}
\tag{2.1}
\]

Hence

\[
\boxed{
\frac d{ds}\log\kappa_{\rm rel}=-\frac12.
}
\tag{2.2}
\]

So fixed old generations move monotonically toward relative IR.  Dilation does not bring them back to the core.

This is a kinematic statement about a fixed physical packet.  It does **not** by itself rule out nonlinear generation of a higher-frequency descendant from IR material.

## 3. One-way IR causal decoupling — OPEN central lemma

Finite density gives, after normalizing the front to scale one,

\[
\boxed{
\|\nabla^mP_{\le2^{-L}}V\|_\infty
\lesssim_M2^{-(m+1)L}.
}
\tag{3.1}
\]

At relative frequency

\[
\kappa=2^{-L}\ll1,
\]

local nonlinear/parabolic response occurs on the slow normalized rate `O(kappa^2)`, whereas similarity dilation sweeps log-frequency toward the IR at order one.

The target theorem is therefore:

\[
\boxed{
\begin{minipage}{0.86\linewidth}
For every compact finite-density front class and bounded similarity-time
interval, the contribution to an `O(1)` complete core event from state
components initially below relative scale `2^{-L}` tends to zero as
`L -> infinity`, uniformly over the class.
\end{minipage}}
\tag{3.2}
\]

This is stronger than local `C^infinity` smallness at one instant.  It is the theorem that makes the IR wake a genuinely one-way outgoing complete defect and makes a fixed finite-log front+wake germ approximately Markovian.

## 4. Projective local complete state — DEFINITION

Global critical compactness is impossible for an infinite finite-density staircase.  The correct local complete topology is

\[
\boxed{
\mathcal X_{\rm loc}^{T2}
=
\varprojlim_{L\to\infty}
\left\{
Q_{[-L,L]}V,
QEQ,
QA_aQ,
Q\mathscr O_aQ
\right\}.
}
\tag{4.1}
\]

Strong convergence is required on every bounded relative log-frequency window.  Spatial translations are the genuine noncompact physical symmetry; rotations are compact and may be extracted by subsequence.

The historical leading-edge barrier should remove UV scale defects.  Minimality plus dynamic profile inheritance should remove independent spatial satellites.  The persistent noncompact direction is the old staircase moving to `j=-infinity`.

## 5. The projective topology has an IR boundary hole

Equation (4.1) sees every fixed finite negative shell, but two sequences that differ only by a defect translated to

\[
j\to-\infty
\]

look identical in every finite window.  Therefore the true limiting state cannot be only `X_loc^{T2}`.

The correct extended object is

\[
\boxed{
\Sigma_{\rm ext}
=(\Sigma_{\rm loc}^{T2},\mathfrak W_{\rm IR}),
}
\tag{5.1}
\]

where `W_IR` is a complete boundary state at logarithmic scale `-infinity`.  The scalar anomaly below is only one pairing of this boundary object.

## 6. Slightly supercritical balance in similarity variables — EXACT

For `epsilon>0`, define

\[
Q_\epsilon(V)
=\|V\|_{\dot H^{1/2+\epsilon}}^2,
\qquad
D_\epsilon(V)
=\|V\|_{\dot H^{3/2+\epsilon}}^2,
\]

and

\[
\mathcal T_\epsilon(V)
=\langle N(V),\Lambda^{1+2\epsilon}V\rangle.
\]

The exact homogeneity coefficient in backward similarity variables gives

\[
\boxed{
\frac12\frac d{ds}Q_\epsilon
+\frac\epsilon2Q_\epsilon
+\nu D_\epsilon
=\mathcal T_\epsilon.
}
\tag{6.1}
\]

At the critical endpoint `epsilon=0`, the dilation term vanishes.  For an invariant measure, or a recurrent orbit for which `Q_epsilon` is bounded and time averages exist,

\[
\boxed{
\frac\epsilon2\overline{Q_\epsilon}
+\nu\overline{D_\epsilon}
=\overline{\mathcal T_\epsilon}.
}
\tag{6.2}
\]

## 7. Scalar IR Abel anomaly — DEFINITION/DEDUCTION

Finite density gives a uniform bound on

\[
\epsilon\overline{Q_\epsilon},
\]

but not automatic convergence as `epsilon -> 0`.  Accordingly define `Phi_IR` either when the Abel limit exists or along a common subsequence `epsilon_n -> 0`:

\[
\boxed{
\Phi_{\rm IR}
:=\lim_{n\to\infty}
\frac{\epsilon_n}{2}\overline{Q_{\epsilon_n}}
\ge0.
}
\tag{7.1}
\]

If the historical UV barrier gives uniform supercritical regularity strong enough that

\[
D_{\epsilon_n}\to D,
\qquad
\mathcal T_{\epsilon_n}\to\mathcal T
\]

in the averaged identities, then

\[
\boxed{
\overline{\mathcal T}
=\nu\overline D+\Phi_{\rm IR}.
}
\tag{7.2}
\]

`Phi_IR` is the missing critical boundary flux carried by the staircase end that escapes every fixed relative window.

For an asymptotically constant negative-shell density `m_-`,

\[
Q_\epsilon
\sim
m_-\sum_{j<0}2^{2\epsilon j}
\sim
\frac{m_-}{2\epsilon\log2},
\]

so `Phi_IR` is proportional to `m_-`.

## 8. Positive-density and zero-density wakes

Critical divergence does not imply a positive Abel anomaly.  A toy wake with shell masses

\[
\mu_{-n}\sim\frac1n
\]

has

\[
\sum_n\mu_{-n}=\infty
\]

but

\[
\epsilon\sum_n\frac1n e^{-c\epsilon n}\to0.
\]

Therefore the compact endgame contains two distinct possibilities:

\[
\boxed{\Phi_{\rm IR}>0}
\]

for positive Abel-density radiation, and

\[
\boxed{\Phi_{\rm IR}=0,\qquad Q=\infty}
\]

for a zero-density but nonsummable wake.

A theorem forcing fixed critical emission every bounded number of log-scales would imply the first branch, but that is an action-gap theorem and is not currently proved.

## 9. Helical IR anomaly — conditional endpoint identity

At the critical endpoint, the two helical critical norms satisfy equal Euler loading.  For `epsilon>0` the two supercritical nonlinear loadings need not be exactly equal, so the helical anomaly must be obtained by taking the endpoint under the same uniform-integrability assumptions used in Section 7.

If that passage is justified, define `Phi_IR^+` and `Phi_IR^-` by the helical Abel boundary masses.  Then

\[
\boxed{
\frac12\overline{\mathcal T}
=\nu\overline{D_+}+\Phi_{\rm IR}^+,
\qquad
\frac12\overline{\mathcal T}
=\nu\overline{D_-}+\Phi_{\rm IR}^-.
}
\tag{9.1}
\]

Consequently

\[
\boxed{
\Phi_{\rm IR}=\Phi_{\rm IR}^++\Phi_{\rm IR}^-,
}
\tag{9.2}
\]

and

\[
\boxed{
\nu\overline{(D_+-D_-)}
=-(\Phi_{\rm IR}^+-\Phi_{\rm IR}^-).
}
\tag{9.3}
\]

Thus an averaged chiral imbalance of viscous critical dissipation is exported into the helicity composition of the IR boundary.

## 10. Operator-valued IR boundary — OPEN construction

The scalar quantity `Phi_IR` cannot retain phase, polarization, or channel geometry.  The Theory-2 completion should use Mellin/Abel averages of complete relative-scale blocks, schematically

\[
\boxed{
\mathfrak W_{\rm IR}
=\operatorname*{w-lim}_{\epsilon_n\downarrow0}
\epsilon_n\int_0^1
r^{2\epsilon_n}\,\Sigma(r)\,\frac{dr}{r}.
}
\tag{10.1}
\]

A rigorous definition must specify:

1. the dilation action on `u`, `E`, `A_a`, and `O_a`;
2. the corresponding rescaling of the signed-curl flag parameter `a`;
3. a weak operator topology with subsequential compactness;
4. compatibility with the one-way IR decoupling theorem.

The scalar endpoint balance (7.2) should arise as one positive pairing of this complete boundary object.

## 11. Open recurrent core rather than a closed reproducer

After one normalized generation, a state may decompose as

\[
\mathcal R_R\Phi_\tau(\Sigma_n)
=
\Sigma_{n+1}
+\sum_\ell W_n^\ell
+r_n,
\tag{11.1}
\]

where the retained core belongs to a fixed relative window and `W_n^ell` are complete radiation profiles moving toward relative IR and/or spatial infinity.

Thus side leakage is not itself a contradiction.  A finite-density cascade may be an **open recurrent core with radiation**.  The Markov state must retain a sufficiently large finite-log wake germ; only defects outside that window may be discarded after proving one-way causal decoupling.

## 12. Compact dynamics target — OPEN

Assume the historical barrier, dynamic profile inheritance, minimality, and one-way IR decoupling.  Then the extended state space `(local complete core, IR boundary)` should contain a compact invariant set for the backward-similar flow.

One may then take an invariant probability measure on a minimal recurrent subset.  This automatically includes fixed points, cycles, quasiperiodic dynamics, and aperiodic recurrence; no artificial DSS hypothesis is required.

The remaining task is not compactness bookkeeping.  It is to exclude the self-generated recurrent mixer described in `05`.