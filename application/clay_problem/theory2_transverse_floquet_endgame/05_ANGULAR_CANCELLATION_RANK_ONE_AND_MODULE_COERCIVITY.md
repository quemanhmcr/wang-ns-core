# 05 — Angular cancellation, rank-one completion, radial compression, bounded-module coercivity

## 1. Local equal-spectral angular kernel

Fix an output

\[
k,
\qquad |k|=c,
\]

parent radii `r,s`, and signed roots

\[
x=\sigma r,
\qquad
y=\rho s.
\]

The decompositions

\[
p+m=k,
\qquad |p|=r,
\qquad |m|=s
\]

form a circle around the `k`-axis.

Let `ψ` parametrize that circle. The projected helical interaction vector has exact form

\[
\boxed{
U(\psi)
=u_+e^{-i\psi}h_+(k)
+u_-e^{i\psi}h_-(k).
}
\]

For a nondegenerate strict triangle, `u_±≠0`.

If `z(ψ)` is the scalar incidence density, the class contribution is

\[
N_{k;\lambda}
=(x-y)
\left[
 u_+Z_{-1}h_+
+u_-Z_{+1}h_-
\right],
\]

where

\[
Z_{\pm1}=\int z(\psi)e^{\pm i\psi}\,d\psi.
\]

Hence

\[
\boxed{
N_{k;\lambda}=0
\iff
Z_{+1}=Z_{-1}=0.
}
\]

So the local equal-spectral angular kernel is exactly the vanishing of the two azimuthal first harmonics.

Equivalently,

\[
\boxed{
\widehat z(\pm1)=0
\iff
z=(\partial_\psi^2+1)g
}
\]

for a periodic distribution `g`, modulo the first-harmonic kernel.

This local kernel is much larger than translation/Killing gauge.

---

## 2. Actual-state incidences are rank-one completed

The local coefficients are not independent in an actual state.

Suppose the decompositions are indexed by `i` with helical amplitudes

\[
A_i\quad\text{at }p_i,
\qquad
B_i\quad\text{at }m_i.
\]

The diagonal incidence coefficient is

\[
z_i=A_iB_i.
\]

But because all modes coexist in the same actual state, every cross pair

\[
(p_i,m_j)
\]

is also physical, with coefficient

\[
\boxed{Z_{ij}=A_iB_j.}
\]

Thus

\[
\boxed{\operatorname{rank}(Z)=1}
\]

and every `2×2` minor vanishes:

\[
\boxed{Z_{ii}Z_{jj}=Z_{ij}Z_{ji}.}
\]

This is the missing actual-state compatibility constraint on the local angular kernel.

---

## 3. Exact cancellation exports at least comparable cross-incidence mass

If the diagonal class cancels exactly,

\[
\sum_iA_iB_iU_i=0,
\]

all `U_i` have equal norm. Let

\[
a_i=|A_iB_i|.
\]

Triangle inequality gives

\[
\max_i a_i\le\frac12\sum_ia_i.
\]

Hence

\[
\left(\sum_i a_i\right)^2
\ge2\sum_i a_i^2.
\]

Cauchy gives

\[
\left(\sum_i|A_iB_i|\right)^2
\le
\left(\sum_i|A_i|^2\right)
\left(\sum_j|B_j|^2\right)
=
\sum_{i,j}|A_iB_j|^2.
\]

Subtracting the diagonal part,

\[
\boxed{
\sum_{i\ne j}|A_iB_j|^2
\ge
\sum_i|A_iB_i|^2.
}
\]

Thus exact angular cancellation cannot remove raw mixed-shell incidence mass. It exports at least comparable squared amplitude into rank-one cross incidences.

---

## 4. Cross completion moves outward

Write the decomposition circle as

\[
p_i=\alpha k+\varrho e_i,
\]

\[
m_i=(1-\alpha)k-\varrho e_i,
\]

with `e_i⊥k` and `|e_i|=1`.

Then for an off-diagonal cross incidence,

\[
\boxed{
|p_i+m_j|^2
=|k|^2+2\varrho^2(1-e_i\cdot e_j).
}
\]

Hence for `i≠j`,

\[
\boxed{|p_i+m_j|>|k|.}
\]

On the standard periodic lattice,

\[
p_i-p_j\in\mathbb Z^3\setminus\{0\},
\]

and therefore

\[
\boxed{
|p_i+m_j|^2\ge|k|^2+1.
}
\]

For unequal radii `r≠s`, these off-diagonal cross pairs cannot be collinear. Hence they are non-null by polarized Curl–Killing.

So unequal-shell angular cancellation necessarily exports non-null Formation to a strictly larger sum-radius.

---

## 5. Polarized unequal-shell rigidity

Let

\[
Ca=xa,
\qquad
Cb=yb,
\qquad
|x|\ne|y|.
\]

Assume on the periodic eigenshell class

\[
B(a,b)=0.
\]

Choose an active noncollinear pair maximizing `|p+m|`. If its output cancels, another decomposition of the same output must exist. Rank-one completion then produces an active off-diagonal cross pair with strictly larger output radius, contradiction.

Hence no active noncollinear pair exists.

Therefore

\[
\boxed{
B(a_x,b_y)=0,\quad |x|\ne|y|
\Longrightarrow
\operatorname{supp}\hat a\cup\operatorname{supp}\hat b
\text{ lies on one Fourier line.}
}
\]

The converse is immediate because common-line interactions are collinear and Leray-null.

So the globally physically completed unequal-shell cancellation kernel is only the collinear stratum.

Equal radii are exactly exceptional: the off-diagonal rectangle can collapse into zero/collinear channels. This is the precise thin-shell exception.

---

## 6. Binary cancellation has an outward Möbius law

For two antipodal decompositions, define

\[
R=r^2+s^2,
\qquad
d=r^2-s^2,
\]

\[
X=\frac{|k|^2}{R},
\qquad
\Delta=\frac{d^2}{R^2}.
\]

The unavoidable off-diagonal completion generates a new sum-radius

\[
\boxed{
X_{n+1}=U(X_n)=2-\frac{\Delta}{X_n}.
}
\]

The strict triangle interval is

\[
X_-<X<X_+,
\]

with

\[
X_\pm=1\pm\sqrt{1-\Delta}.
\]

Exactly,

\[
\boxed{
U(X)-X
=\frac{(X-X_-)(X_+-X)}{X}>0.
}
\]

Furthermore

\[
\boxed{
\frac{X_+-X_n}{X_n-X_-}
=
\left(\frac{X_-}{X_+}\right)^n
\frac{X_+-X_0}{X_0-X_-}.
}
\]

Thus binary cancellation radiates monotonically toward the collinear Poisson characteristic `X_+`; there is no compact interior binary cycle.

---

## 7. Radial-edge SVD compression

Let `P_r` be the spectral projector onto radius `r`, and set

\[
\mathcal H_r=P_rL^2.
\]

For `r≠c`, define

\[
Q_{cr}=P_cJ_uP_r.
\]

Skewness gives

\[
Q_{rc}=-Q_{cr}^*.
\]

On

\[
\mathcal H_r\oplus\mathcal H_c,
\]

the isolated radial-edge Formation operator is

\[
\boxed{
\mathbb J_{rc}
=
\begin{pmatrix}
0&-Q_{cr}^*\\
Q_{cr}&0
\end{pmatrix}.
}
\]

Take an SVD

\[
Q_{cr}v_j=g_jw_j.
\]

Each singular pair is invariant and reduces exactly to

\[
\boxed{
\frac d{dt}
\begin{pmatrix}X_j\\Y_j\end{pmatrix}
=
\begin{pmatrix}
-\nu r^2&-g_j\\
g_j&-\nu c^2
\end{pmatrix}
\begin{pmatrix}X_j\\Y_j\end{pmatrix}.
}
\]

Therefore arbitrary angular/high-valence multiplicity inside one radial pair compresses exactly into independent `2×2` passive channels.

---

## 8. Exact isolated reverse-block passivity

Let

\[
\bar d=\frac\nu2(r^2+c^2),
\qquad
\delta=\frac\nu2(c^2-r^2).
\]

For one singular pair,

\[
A=
-\bar dI
+
\begin{pmatrix}
\delta&-g\\
g&-\delta
\end{pmatrix}.
\]

The traceless part squares to

\[
(\delta^2-g^2)I.
\]

If

\[
g^2>\delta^2,
\]

put

\[
\omega=\sqrt{g^2-\delta^2}.
\]

At the projective Formation return time

\[
T_*=\frac\pi\omega,
\]

\[
\boxed{e^{T_*A}=-e^{-\bar dT_*}I.}
\]

Therefore critical block stock obeys

\[
\boxed{
M_{\rm block}(T_*)
=e^{-\nu(r^2+c^2)T_*}M_{\rm block}(0).
}
\]

If `g^2≤δ^2`, the block is overdamped / critically damped and no recurrent Formation turn exists.

Thus every isolated physical reverse block is strictly passive at finite viscosity.

---

## 9. Stronger theorem: arbitrary internal recycling in a bounded spectral module is passive

Let

\[
Q=1_{[\rho,R\rho]}(\Lambda)
\]

and

\[
x=Qu.
\]

The exact projected equation is

\[
\boxed{
x_t=J_Q(t)x-\nu\Lambda^2x+F_Q,
}
\]

with

\[
J_Q=QJ_uQ,
\qquad
J_Q^*=-J_Q,
\]

and external forcing

\[
F_Q=QJ_u(I-Q)u.
\]

For the homogeneous module (`F_Q=0`),

\[
\frac d{dt}\|x\|_2^2
=-2\nu\|\Lambda x\|_2^2
\le-2\nu\rho^2\|x\|_2^2.
\]

Since inside the band

\[
\rho\|x\|_2^2\le M(x)\le R\rho\|x\|_2^2,
\]

its propagator satisfies

\[
\boxed{
\|V(t,s)\|_{M\to M}
\le
\sqrt R\,e^{-\nu\rho^2(t-s)}.
}
\]

This is mode-count independent and allows arbitrary time-dependent internal skew recycling.

Therefore after

\[
T>\frac{\log R}{2\nu\rho^2},
\]

the whole closed module is strictly critically contractive.

This solves the closed three-shell/high-valence recycling problem.

---

## 10. Exact whole-module forcing debt

Duhamel gives

\[
x(t_1)
=V(t_1,t_0)x(t_0)
+\int_{t_0}^{t_1}V(t_1,s)F_Q(s)\,ds.
\]

If the module critical stock does not decrease over a horizon with

\[
q_Q=\sqrt R\,e^{-\nu\rho^2T}<1,
\]

then necessarily

\[
\boxed{
\int_{t_0}^{t_1}
e^{-\nu\rho^2(t_1-s)}\|F_Q(s)\|_M\,ds
\ge
\frac{1-q_Q}{\sqrt R}\|x(t_0)\|_M.
}
\]

All internal multiplicity has already been summed before this estimate.

Thus persistent neutrality requires genuine cross-module Formation forcing, not merely complicated internal holonomy.

---

## 11. The forcing is a flag commutator

Since

\[
[Q,J_u]u
=QJ_u(I-Q)u-(I-Q)J_uQu
\]

and the two terms live in orthogonal spectral subspaces,

\[
\boxed{
\|[Q,J_u]u\|_2^2
=
\|QJ_u(I-Q)u\|_2^2
+
\|(I-Q)J_uQu\|_2^2.
}
\]

Hence

\[
\boxed{
\|F_Q\|_2\le\|[Q,J_u]u\|_2.
}
\]

So the whole-module forcing debt is an actual-state spectral-flag commutator debt inside the existing Theory-2 ontology.

---

## 12. Only `T` creates new signed-root directions

Resolve

\[
Cu_x=xu_x.
\]

The modulation normal form gives

\[
\boxed{
\dot u_x=\ell_x(t)u_x+T_x,
}
\]

where

\[
\ell_x
=\gamma|x|(|x|-a-bx)-\nu x^2.
\]

Therefore

\[
\boxed{
u_x=0\Longrightarrow\dot u_x=T_x.}
\]

And projectively,

\[
\boxed{
(I-\Pi_{u_x})\dot u_x
=(I-\Pi_{u_x})T_x.
}
\]

So only `T` can create a new signed-root direction or rotate the direction inside an eigenspace. The commuting constrained-gradient/heat part can only amplify or attenuate an already existing direction.

---

## 13. Status

### EXACT

Local angular kernel, rank-one completion, outward grading, unequal-shell rigidity, binary radiation law, radial SVD, isolated-block passivity, bounded-module contraction, forcing debt, `T`-only projective recruitment.

### Consequence

All recycling confined to a bounded finite-ratio spectral module is already passive at finite viscosity.

### OPEN

Persistent regenerative dynamics must continually obtain cross-module / transverse forcing, i.e. rebuild spectral leverage rather than merely recycle it internally.
