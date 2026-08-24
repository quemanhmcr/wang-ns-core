# THEORY-2 / NEO NAVIER–STOKES
# Finite Companion Rigidity — Curated Current Proof

> **Document policy.** This file now contains only the mathematically active proof chain. Superseded recurrence/FWE/UPN/FSSS/GWCI-descent explorations remain recoverable from Git history and are intentionally removed from the main proof text.
>
> **Current status.** The whole-state Mother coordinate, finite-viscosity radial inverse, exact unfolded helical channel closure, support-geometric companion rectangles, strict heat–Poisson rectangle curvature, positive channel-lift conductance, and the channel-quotient descent no-go are proved below under their stated hypotheses. The remaining terminal theorem is the **Canonical Physical Heat-Rigidity theorem (CPHR)**.

---

# 0. Structural setup

Let

\[
C=\operatorname{curl},
\qquad
\nabla_v w=P[(v\cdot\nabla)w],
\qquad
N(v)=P[(v\cdot\nabla)v].
\]

For the normalized finite-\(\kappa\) theory we use

\[
E=\|v\|_2^2,
\qquad
M=\|\Lambda^{1/2}v\|_2^2,
\qquad
D_2=\|\Lambda v\|_2^2,
\qquad
D_3=\|\Lambda^{3/2}v\|_2^2,
\]

with

\[
E=M=1,
\qquad
0<\kappa_0\le\kappa\le\kappa_1.
\]

The constrained-gradient decomposition is

\[
N=\gamma G+T,
\qquad
Y=rG+R_{\rm fv},
\qquad
r=\frac{D_3}{d^2},
\]

so

\[
N-\kappa Y
=(\gamma-\kappa r)G+(T-\kappa R_{\rm fv}).
\tag{0.1}
\]

On the scalar stationary stratum

\[
\Sigma_\kappa
:=
\{v:W(v)=2\kappa(v)D_3(v)\},
\tag{0.2}
\]

we have

\[
\gamma
=\frac{W}{2d^2}
=\kappa\frac{D_3}{d^2}
=\kappa r,
\]

hence

\[
\boxed{
N-\kappa Y
=T-\kappa R_{\rm fv}
\quad\text{on }\Sigma_\kappa.
}
\tag{0.3}
\]

This identity is the bridge from stationary exclusion to the transverse defect.

---

# 1. Mother / Spectral-Flag completeness

For smooth mean-zero divergence-free fields on \(\mathbb T^3\), define

\[
\boxed{
\mathcal M(u):=E_u=[\nabla_u,C].
}
\tag{1.1}
\]

Let

\[
S(u)=\frac12(\nabla u+\nabla u^T).
\]

## Theorem 1.1 — Mother completeness

On the smooth mean-zero periodic divergence-free class,

\[
\boxed{
E_u=E_v
\iff
S(u)=S(v)
\iff
u=v.
}
\tag{1.2}
\]

Moreover \(u\) is explicitly recovered from the principal symbol of \(E_u\).

### Proof

Since Leray projection commutes with curl on the flat torus,

\[
E_u w
=-P\sum_{j=1}^3\nabla u_j\times\partial_jw.
\tag{1.3}
\]

For \(\xi\neq0\) and \(b\perp\xi\), its principal symbol is

\[
\sigma_1(E_u)(x,\xi)b
=-iP_\xi\bigl((\nabla u(x))^T\xi\times b\bigr).
\]

Write

\[
(\nabla u)^T\xi=\alpha\xi+r,
\qquad r\perp\xi.
\]

For \(b\perp\xi\), the vector \(r\times b\) is parallel to \(\xi\), hence killed by \(P_\xi\). Therefore

\[
\sigma_1(E_u)(x,\xi)b
=-i\alpha\,\xi\times b.
\]

The skew part of \(\nabla u\) has zero quadratic form, so

\[
\alpha
=\frac{\xi^TS(u)(x)\xi}{|\xi|^2}.
\]

Thus

\[
\boxed{
\sigma_1(E_u)(x,\xi)b
=-i\frac{\xi^TS(u)(x)\xi}{|\xi|^2}\,\xi\times b.
}
\tag{1.4}
\]

Hence the symbol determines the quadratic form

\[
q_u(x,n)=n^TS(u)(x)n.
\]

Since \(\operatorname{tr}S(u)=0\), spherical polarization reconstructs \(S(u)\); one convenient formula is

\[
\boxed{
S(u)(x)
=\frac{15}{2}
\fint_{S^2}q_u(x,n)n\otimes n\,dn.
}
\tag{1.5}
\]

Finally incompressibility gives

\[
\operatorname{div}S(u)=\frac12\Delta u,
\]

and the mean-zero condition yields

\[
\boxed{
u=2\Delta^{-1}\operatorname{div}S(u).}
\tag{1.6}
\]

Therefore \(E_u\) is injective and determines the state. \(\square\)

### Quantitative observation

For every admissible homogeneous index \(s\),

\[
\boxed{
2\|S(u)\|_{\dot H^s}^2
=\|u\|_{\dot H^{s+1}}^2.
}
\tag{1.7}
\]

In particular, if

\[
W=T-\kappa R_{\rm fv},
\]

then whenever the Mother decoder is legitimate,

\[
\boxed{
\|W\|_{\dot H^{-1/2}}^2
=2\|S(W)\|_{\dot H^{-3/2}}^2.
}
\tag{1.8}
\]

Mother completeness is an observability theorem; it does not by itself prove \(W\neq0\).

---

# 2. Exact finite-viscosity radial inverse

For a helicity sign \(\sigma\), freeze the normalized scalar coefficients and set

\[
\mathscr R_\sigma
=
-2D_2\rho\partial_\rho
-\chi_\sigma\rho^2
+ra\rho
-4D_2,
\qquad
\chi_\sigma>0.
\tag{2.1}
\]

Define

\[
h_\sigma(\rho)
:=
\rho^{-2}
\exp\left(
-\frac{\chi_\sigma}{4D_2}\rho^2
+\frac{ra}{2D_2}\rho
\right).
\tag{2.2}
\]

A direct differentiation gives

\[
\boxed{\mathscr R_\sigma h_\sigma=0.}
\tag{2.3}
\]

## Theorem 2.1 — canonical finite-energy absorber

Let \(F\) be smooth and supported in an annulus

\[
0<\rho_0<\rho<\rho_1<\infty.
\]

Then

\[
\kappa\mathscr R_\sigma f=F
\]

has the unique finite-\(H^{-1/2}\) solution

\[
\boxed{
(\mathcal S_\sigma F)(\rho,\omega)
=
-\frac{h_\sigma(\rho)}{2\kappa D_2}
\int_0^\rho
\frac{F(s,\omega)}{s h_\sigma(s)}\,ds.
}
\tag{2.4}
\]

### Proof

Write \(f=h_\sigma c\). Since \(\mathscr R_\sigma h_\sigma=0\),

\[
\mathscr R_\sigma(h_\sigma c)
=-2D_2\rho h_\sigma c'.
\]

Thus

\[
c'
=-\frac{F}{2\kappa D_2\rho h_\sigma},
\]

which gives (2.4) after imposing the zero infrared branch.

If two finite-energy solutions existed, their difference would be

\[
C(\omega)h_\sigma(\rho).
\]

But

\[
h_\sigma(\rho)\sim\rho^{-2}
\qquad(\rho\downarrow0),
\]

and the radial \(H^{-1/2}\) measure is \(\rho\,d\rho\,d\omega\), so

\[
\int_0^\varepsilon\rho|h_\sigma|^2d\rho
\sim
\int_0^\varepsilon\rho^{-3}d\rho
=\infty.
\]

Hence \(C=0\). \(\square\)

The Green kernel is

\[
\boxed{
G_\sigma(\rho,s)
=
-\frac{s}{2\kappa D_2\rho^2}
\exp\left[
-\frac{\chi_\sigma}{4D_2}(\rho^2-s^2)
+\frac{ra}{2D_2}(\rho-s)
\right]
\mathbf 1_{s<\rho}.
}
\tag{2.5}
\]

Thus the radial step is scalar, exact, and injective on forcing:

\[
\boxed{
F\neq0\Longrightarrow\mathcal S_\sigma F\neq0.
}
\tag{2.6}
\]

For finitely many labeled edges the inverse acts by direct sum. Therefore radial inversion alone creates no cross-edge loop law.

---

# 3. Bridge 1 — exact unfolded helical channel closure

## 3.1 One-dimensional helical fibers

For \(k\neq0\), let

\[
V_k=\{z\in\mathbb C^3:k\cdot z=0\},
\qquad
H_k=\frac{i\,k\times}{|k|}.
\]

On \(V_k\), \(H_k^2=I\), and the two eigenspaces

\[
E_\sigma(k)=\ker(H_k-\sigma I),
\qquad \sigma=\pm1,
\]

have complex dimension one:

\[
\boxed{\dim_\mathbb C E_\sigma(k)=1.}
\tag{3.1}
\]

Along a ray \(k=\rho\omega\),

\[
H_{\rho\omega}=i\omega\times,
\]

so

\[
\boxed{E_\sigma(\rho\omega)=E_\sigma(\omega).}
\tag{3.2}
\]

Hence a fixed ray/helicity packet has scalar radial profile times one polarization vector.

## 3.2 Polarized Curl–Killing scalar channel

Choose nonzero representatives

\[
a_p=Ae_{\sigma_p}(p),
\qquad
b_q=Be_{\sigma_q}(q),
\qquad
k=p+q.
\]

The polarized identity gives

\[
2B(a_p,b_q)
=
(\sigma_p|p|-\sigma_q|q|)
P_k(b_q\times a_p).
\]

Projecting to output helicity \(\tau\),

\[
Q_\tau(k)
\bigl(e_{\sigma_q}(q)\times e_{\sigma_p}(p)\bigr)
=
m^\tau(p,q)e_\tau(k)
\]

for a unique scalar \(m^\tau(p,q)\). Therefore

\[
\boxed{
B_{p,q}^\tau(a_p,b_q)
=AB\,\beta^\tau(p,q)e_\tau(k),
}
\tag{3.3}
\]

where

\[
\boxed{
\beta^\tau(p,q)
=
\frac{\sigma_p|p|-\sigma_q|q|}{2}
\,m^\tau(p,q).
}
\tag{3.4}
\]

The channel is nonexceptional exactly when

\[
\beta^\tau(p,q)\neq0.
\tag{3.5}
\]

## 3.3 Radial preservation and packet-level closure

Since the helical frame is independent of \(\rho\),

\[
\mathscr R_\sigma(fe_\sigma)
=(\mathscr R_\sigma f)e_\sigma,
\qquad
\mathcal S_\sigma(Fe_\sigma)
=(\mathcal S_\sigma F)e_\sigma.
\tag{3.6}
\]

For a labeled nonexceptional channel \(e=(p,q\to r)\), define

\[
\mathcal T_e:=\mathcal S_e\circ B_e.
\]

If \(L_p=\mathbb C\psi_p\) and \(L_q=\mathbb C\psi_q\), define

\[
\boxed{
L_r
:=
\operatorname{span}_\mathbb C
\{\mathcal T_e(\psi_p,\psi_q)\}.
}
\tag{3.7}
\]

Bilinearity shows that this line is independent of the nonzero representatives chosen for \(L_p,L_q\).

Choose a representative \(\psi_r\in L_r\setminus\{0\}\). Then there is a unique

\[
h_e\in\mathbb C^\times
\]

such that

\[
\boxed{
\mathcal T_e(\psi_p,\psi_q)
=h_e\psi_r.
}
\tag{3.8}
\]

Under projective gauge changes

\[
\psi_c\mapsto g_c\psi_c,
\]

one has

\[
\boxed{
h_e\mapsto g_pg_qg_r^{-1}h_e.}
\tag{3.9}
\]

## 3.4 Exact unfolding of additive mixing

Different genealogical channels may arrive at the same physical Fourier label. They must be retained before physical summation. Define

\[
\widetilde{\mathcal H}_r
=
\bigoplus_{e\to r}L_{r,e},
\qquad
\Sigma_r((u_e)_e)=\sum_eu_e.
\tag{3.10}
\]

If

\[
u=\sum_\alpha u_\alpha,
\qquad
v=\sum_\beta v_\beta,
\]

then exactly

\[
B(u,v)=\sum_{\alpha,\beta}B(u_\alpha,v_\beta).
\tag{3.11}
\]

Thus every finite interaction genealogy admits an exact unfolded channel description; physical cancellation occurs only after applying \(\Sigma\).

Reality is compatible with the construction:

\[
L_{\bar c}=\overline{L_c},
\qquad
h_{\bar e}=\overline{h_e}.
\tag{3.12}
\]

### Theorem 3.1 — Bridge 1

Every finite reality-complete nonexceptional polarized interaction history, followed by the frozen finite-viscosity absorber, carries exact one-dimensional channel lines and gauge-covariant scalar gains. The construction iterates to every finite depth without constants depending on mode count or completion depth.

\[
\boxed{\mathrm{QED}_{\mathrm{Bridge\ 1}}}
\]

### Rank-one reminder

If input amplitudes factor as

\[
Z_{ij}=A_iB_j,
\]

then

\[
\boxed{Z_{11}Z_{22}=Z_{12}Z_{21}.}
\tag{3.13}
\]

This rank-one identity is flat. Any nontrivial curvature must come from physical transfer, not from the algebra \(Z_{ij}=A_iB_j\) itself.

---

# 4. Positive-measure companion rectangles

Let \(v\in L^2(\mathbb R^3)\) be nonzero and divergence free. For at least one helicity sign \(\sigma\), the component \(\widehat v_\sigma\) is nonzero in \(L^2\).

## Lemma 4.1 — active annular support

There exist

\[
0<r_0<r_1<\infty,
\qquad
\eta>0,
\]

such that

\[
S
:=
\{k:r_0<|k|<r_1,\ |\widehat v_\sigma(k)|\ge\eta\}
\tag{4.1}
\]

has finite positive measure.

### Proof

The nonzero set of \(\widehat v_\sigma\) is a countable union of sets of the form

\[
\left\{\frac1m<|k|<N,\ |\widehat v_\sigma(k)|\ge\frac1n\right\}.
\]

Since the union has positive measure, one member has positive measure. \(\square\)

Set

\[
g(k)=(\mathbf1_S*\mathbf1_S)(k).
\]

Then

\[
\int g(k)dk=|S|^2>0,
\]

so the set \(\{k:g(k)>0\}\) has positive measure. For every such \(k_0\), the fiber

\[
S_{k_0}:=\{p\in S:k_0-p\in S\}
\]

has positive measure.

Choose two distinct points \(p,p'\in S_{k_0}\), set

\[
q=k_0-p,
\qquad
q'=k_0-p',
\qquad
d=p-p'\neq0.
\]

Then

\[
\boxed{
\begin{array}{ccc}
(p,q)&\to&k_0,\\
(p',q')&\to&k_0,\\
(p,q')&\to&k_0+d,\\
(p',q)&\to&k_0-d.
\end{array}
}
\tag{4.2}
\]

This is an exact support-geometric companion rectangle.

To exclude thin-shell, same-root, collinear, and Formation-null degeneracies we use the explicit active-support hypothesis:

### (NE-S) Active support nonexceptionality

There is a positive-measure family of tuples \((k_0,p,p')\) for which all four incidences in (4.2) are uniformly nonexceptional.

Under (NE-S), every nonzero normalized state contains a positive-measure family of nonexceptional support rectangles.

No recurrence, finite Fourier support, projective discreteness, or Fourier cutoff is used.

---

# 5. Strict heat–Poisson rectangle curvature

For

\[
y\ge0,
\qquad
\tau>0,
\]

define

\[
m_{y,\tau}(k)
=e^{-y|k|-\tau|k|^2}.
\tag{5.1}
\]

For the rectangle (4.2), define

\[
\mathfrak M_{y,\tau}(k_0,d)
:=
\frac{m_{y,\tau}(k_0)^2}
{m_{y,\tau}(k_0+d)m_{y,\tau}(k_0-d)}.
\tag{5.2}
\]

## Theorem 5.1 — strict semigroup curvature

For every \(d\neq0\),

\[
\boxed{
\log\mathfrak M_{y,\tau}(k_0,d)
=
y\bigl(|k_0+d|+|k_0-d|-2|k_0|\bigr)
+2\tau|d|^2>0.
}
\tag{5.3}
\]

### Proof

Convexity gives

\[
|k_0+d|+|k_0-d|-2|k_0|\ge0,
\]

while the parallelogram identity gives

\[
|k_0+d|^2+|k_0-d|^2-2|k_0|^2
=2|d|^2>0.
\]

Thus (5.3) follows. \(\square\)

Hence

\[
\boxed{
\mathfrak M_{y,\tau}(k_0,d)>1.
}
\tag{5.4}
\]

If \(Z_{ij}=A_iB_j\) are the four rank-one amplitudes and

\[
\widetilde Z_{ij}=m_{y,\tau}(k_{ij})Z_{ij},
\]

then

\[
\boxed{
\frac{\widetilde Z_{11}\widetilde Z_{22}}
{\widetilde Z_{12}\widetilde Z_{21}}
=
\mathfrak M_{y,\tau}(k_0,d)>1.
}
\tag{5.5}
\]

This is a strict **semigroup multiplier rectangle defect**. It is not automatically the projective channel holonomy, because physical channel gains also contain Curl-root, polarization, Leray, and radial-transfer factors.

---

# 6. Positive channel-lift conductance

The semigroup curvature may be assembled into a positive channel-space functional. This remains useful information even though Section 7 proves that it does not descend faithfully through physical aggregation.

Choose local helical frames and define the polarized symbol

\[
\mathfrak b_\sigma^\tau(p,q)
=
\frac{\sigma(|p|-|q|)}2
Q_\tau(p+q)
\bigl(e_\sigma(q)\times e_\sigma(p)\bigr),
\tag{6.1}
\]

and channel amplitude

\[
\mathcal F_\sigma^\tau[v](p,q)
=f_\sigma(p)f_\sigma(q)
\mathfrak b_\sigma^\tau(p,q).
\tag{6.2}
\]

For same-output coordinates

\[
p+q=k,
\qquad
p'+q'=k,
\qquad
d=p-p',
\]

set

\[
\Xi_{\tau,y}(k,d)
=
2\tau|d|^2
+y\bigl(|k+d|+|k-d|-2|k|\bigr),
\]

and

\[
\boxed{
\Gamma_{\tau,y}(k,d)
=1-e^{-\Xi_{\tau,y}(k,d)}.
}
\tag{6.3}
\]

Then

\[
\Gamma_{\tau,y}(k,d)>0
\qquad(d\neq0).
\tag{6.4}
\]

Define

\[
\mathcal M_v(k,p,p')
=
\sum_{\sigma,\tau_+,\tau_-}
|\mathcal F_\sigma^{\tau_+}[v](p,k-p')|^2
|\mathcal F_\sigma^{\tau_-}[v](p',k-p)|^2
\tag{6.5}
\]

and

\[
\boxed{
\mathfrak C_{\tau,y}(v)
=
\iiint
\Gamma_{\tau,y}(k,p-p')
\mathcal M_v(k,p,p')
\,dk\,dp\,dp'.
}
\tag{6.6}
\]

We state explicitly the needed hypotheses:

- **(G-Reg):** \(\mathfrak C_{\tau,y}(v)<\infty\), and the functional is continuous in the chosen compact graph topology.
- **(G-NE):** there is a positive-measure triple set on which \(p\neq p'\) and both cross companion channels are nonzero.

## Theorem 6.1 — strict channel conductance

Under (G-Reg) and (G-NE),

\[
\boxed{
\mathfrak C_{\tau,y}(v)>0.
}
\tag{6.7}
\]

### Proof

The integrand in (6.6) is nonnegative. By (G-NE), \(\mathcal M_v>0\) on a positive-measure set with \(p\neq p'\). By (6.4), \(\Gamma_{\tau,y}>0\) there. Hence the integral is strictly positive. \(\square\)

If the compact class \(K\) satisfies these assumptions continuously, then

\[
\boxed{
\min_{v\in K}\mathfrak C_{\tau,y}(v)>0.
}
\tag{6.8}
\]

No pointwise lower bound on \(|p-p'|\) is required.

---

# 7. Structural stop theorem — channel quotient descent fails

The physical nonlinear output sums all incidence channels before any observable is evaluated. This creates a quotient map. The positive channel functional of Section 6 would yield a stationary contradiction only if its derivative descended through that quotient. We now prove that the natural descent fails generically.

## 7.1 Physical aggregation on one output fiber

Fix an output \(k\neq0\), input helicities \(\alpha,\beta\), and output helicity \(\tau\). Let

\[
q=k-p.
\]

The exact scalar Curl–Killing symbol is

\[
\boxed{
\beta_{\alpha\beta}^{\tau}(p,k-p)
=
\frac{\alpha|p|-\beta|k-p|}{2}
\,m_{\alpha\beta}^{\tau}(p,k-p).
}
\tag{7.1}
\]

The channel lift is

\[
F_k(p)
=
\beta_{\alpha\beta}^{\tau}(p,k-p)
\,a_\alpha(p)a_\beta(k-p).
\tag{7.2}
\]

Physical Formation sees only the integral in \(p\).

For a finite-measure incidence patch \(U\), define

\[
X_U=L^2(U;\mathbb C),
\qquad
\Sigma_UF=\int_UF(p)dp.
\tag{7.3}
\]

Then \(\Sigma_U:X_U\to\mathbb C\) is bounded and

\[
\boxed{
(\Sigma_U^*z)(p)=z,
\qquad
\operatorname{Ran}\Sigma_U^*
=\{\text{constant functions on }U\}.
}
\tag{7.4}
\]

Thus a channel derivative can descend through physical aggregation only if all decompositions feeding the same physical output receive the same dual coefficient.

## 7.2 Wave-packet symbol extraction

### Lemma 7.1

Any universal polynomial Fourier identity built from finitely many smooth multipliers, Leray/helical projections, and Curl–Killing interactions must hold on every finite nonexceptional discrete frequency configuration.

### Proof

Choose distinct nonzero frequency centers \(\xi_j\), localize each by a disjoint Schwartz Fourier packet

\[
\varphi_{\varepsilon,j}(k)
=
\varepsilon^{-3/2}
\varphi\left(\frac{k-\xi_j}{\varepsilon}\right),
\]

and complete by reality. Smooth multipliers converge uniformly to their symbols at the packet centers. Distinct prescribed interaction histories remain separated at leading order. Divide by the common packet-scaling power and let \(\varepsilon\to0\). The continuous identity yields the corresponding discrete symbol identity. \(\square\)

## 7.3 Two channels into one physical output

Choose four same-output decompositions

\[
p_i+q_i=k,
\qquad i=1,2,3,4,
\]

with

\[
\boxed{
p_1-p_2=p_3-p_4=d\neq0.}
\tag{7.5}
\]

Then

\[
e_{12}=(p_1,q_2\to k+d),
\qquad
e_{34}=(p_3,q_4\to k+d)
\]

are two distinct channels feeding the same output, while

\[
e_{21}=(p_2,q_1\to k-d),
\qquad
e_{43}=(p_4,q_3\to k-d)
\]

are the reverse companions.

Choose the configuration generically so that

\[
\beta_{12},\beta_{21},\beta_{34},\beta_{43}\neq0.
\tag{7.6}
\]

Let

\[
A_i=a_{\alpha_i}(p_i),
\qquad
B_i=a_{\beta_i}(q_i),
\qquad
z_{ij}=\beta_{ij}A_iB_j.
\tag{7.7}
\]

The discrete paired-conductance energy contains

\[
\mathfrak C_{\rm disc}
=
\sum_{i<j}
\Gamma_{ij}|z_{ij}|^2|z_{ji}|^2.
\tag{7.8}
\]

Its Wirtinger gradient satisfies

\[
(\mathcal Q_{\rm disc})_{ij}
=
\Gamma_{ij}z_{ij}|z_{ji}|^2.
\tag{7.9}
\]

Because the two rectangles have the same \(d\),

\[
\Gamma_{12}=\Gamma_{34}=:\Gamma>0.
\]

At output \(k+d\), the relevant gradient coordinates are therefore

\[
\Gamma
\bigl(
 z_{12}|z_{21}|^2,
 z_{34}|z_{43}|^2
\bigr).
\tag{7.10}
\]

But

\[
\operatorname{Ran}\Sigma_{k+d}^*
=
\{(\zeta,\zeta):\zeta\in\mathbb C\}.
\tag{7.11}
\]

Thus descent would require

\[
\boxed{
z_{12}|z_{21}|^2
=z_{34}|z_{43}|^2.}
\tag{7.12}
\]

Substituting (7.7),

\[
\beta_{12}A_1B_2|\beta_{21}A_2B_1|^2
=
\beta_{34}A_3B_4|\beta_{43}A_4B_3|^2.
\tag{7.13}
\]

Fix every amplitude except \(A_1=t\neq0\). The left side is \(Ct\) with \(C\neq0\), while the right side is a fixed nonzero constant. Hence (7.13) cannot hold identically in \(t\).

By Lemma 7.1, (7.12) cannot be a universal physical identity.

## Theorem 7.2 — channel-faithful range no-go

Generically on nonexceptional configurations,

\[
\boxed{
\mathcal Q_{\tau,y}(\mathcal B(v))
\notin\operatorname{Ran}\Sigma^*.
}
\tag{7.14}
\]

Therefore there is no universal physical Ward field \(\Phi(v)\) satisfying

\[
\boxed{
\mathcal Q_{\tau,y}(\mathcal B(v))
=
\Sigma^*\Phi(v)
}
\tag{7.15}
\]

for all sufficiently regular active nonexceptional states.

\[
\boxed{\mathrm{QED}}
\]

### Kernel witness

If

\[
q_{12}=\Gamma z_{12}|z_{21}|^2,
\qquad
q_{34}=\Gamma z_{34}|z_{43}|^2,
\]

and \(q_{12}\neq q_{34}\), set

\[
H=(q_{12}-q_{34},-(q_{12}-q_{34})).
\]

Then

\[
\Sigma H=0,
\]

but

\[
\operatorname{Re}\langle(q_{12},q_{34}),H\rangle
=|q_{12}-q_{34}|^2>0.
\tag{7.16}
\]

Thus the derivative fails to annihilate the hidden-cancellation direction.

## Theorem 7.3 — quotient descent criterion

Let \(X,H\) be real Hilbert spaces, \(\Sigma:X\to H\) bounded and linear, and \(C:X\to\mathbb R\) continuously Fréchet differentiable. Then the following are equivalent:

1. \(C=\widetilde C\circ\Sigma\) for some function on \(\operatorname{Ran}\Sigma\);
2. \(DC(F)[K]=0\) for every \(F\) and every \(K\in\ker\Sigma\);
3. \(\nabla C(F)\in(\ker\Sigma)^\perp=\overline{\operatorname{Ran}\Sigma^*}\) for every \(F\).

### Proof

The implication \(1\Rightarrow2\) follows from the chain rule. If 2 holds and \(\Sigma F_1=\Sigma F_2\), then \(F_2-F_1\in\ker\Sigma\); differentiating \(C(F_1+t(F_2-F_1))\) shows that \(C(F_1)=C(F_2)\), so \(C\) factors through \(\Sigma\). Finally 2 and 3 are equivalent by the Hilbert representation of the derivative and

\[
(\ker\Sigma)^\perp
=\overline{\operatorname{Ran}\Sigma^*}.
\]

\(\square\)

### Consequence

The channel conductance \(\mathfrak C_{\tau,y}\) is genuine positive information on the unfolded channel space, but it is **not** a physical quotient functional of the aggregated nonlinear output.

This eliminates the specific route

\[
\text{channel conductance}
\to
\nabla_{\rm channel}\mathfrak C
\to
\Sigma^*(\text{physical Ward field}).
\tag{7.17}
\]

It does **not** rule out every conceivable physical Ward identity constructed directly after convolution has already been summed.

---

# 8. Physical semigroup reset

A viable terminal functional must be formed after physical aggregation.

Let

\[
H_\tau=e^{-\tau\Lambda^2}.
\]

One quotient-safe object is

\[
\boxed{
\mathcal K_\tau(v)
=
H_\tau N(v)
-
B(H_{\tau/2}v,H_{\tau/2}v).
}
\tag{8.1}
\]

In Fourier variables,

\[
\widehat{\mathcal K_\tau(v)}(k)
=
\int
\left[
 e^{-\tau|k|^2}
-
 e^{-\frac\tau2(|p|^2+|q|^2)}
\right]
\widehat B_v(p,q)\,dp,
\qquad q=k-p.
\tag{8.2}
\]

The physical channels are summed before one forms

\[
\|\mathcal K_\tau(v)\|_2^2.
\]

Thus Theorem 7.2 does not obstruct this object.

However, stationarity does not imply \(\mathcal K_\tau(v)=0\). The exact usable relation comes instead from the canonical heat depth.

---

# 9. Canonical heat identity

Recall

\[
L=\frac32+x\cdot\nabla,
\qquad
Y=\Lambda^2-D_2+2D_2L.
\tag{9.1}
\]

In Fourier variables,

\[
\widehat{Lv}
=-\left(\frac32+\rho\partial_\rho\right)\widehat v.
\]

A direct differentiation gives

\[
\boxed{
L H_\tau
=H_\tau L+2\tau\Lambda^2H_\tau,
}
\tag{9.2}
\]

or

\[
H_\tau L
=L H_\tau-2\tau\Lambda^2H_\tau.
\]

Therefore

\[
\begin{aligned}
H_\tau Y
&=
\Lambda^2H_\tau-D_2H_\tau+2D_2H_\tau L\\
&=
(1-4D_2\tau)\Lambda^2H_\tau
-D_2H_\tau+2D_2LH_\tau.
\end{aligned}
\tag{9.3}
\]

At

\[
\boxed{
\tau_*=\frac1{4D_2},
}
\tag{9.4}
\]

we obtain

\[
\boxed{
H_{\tau_*}Y
=D_2(2L-1)H_{\tau_*}.
}
\tag{9.5}
\]

Hence every stationary finite-\(\kappa\) profile satisfying

\[
N(v)=\kappa Y_v
\]

obeys the exact **physical** identity

\[
\boxed{
H_{\tau_*}N(v)
=
\kappa D_2(2L-1)H_{\tau_*}v.
}
\tag{9.6}
\]

All nonlinear incidences have already been physically aggregated inside \(N(v)\).

The heat multiplier is strictly positive at every finite frequency, so \(H_{\tau_*}\) is injective on the natural distribution classes where these formulas are valid. Equation (9.6) is therefore an exact semigroup rewriting of stationarity, not a lossy finite reader.

---

# 10. Terminal theorem — Canonical Physical Heat-Rigidity

## Conjectural Theorem 10.1 — CPHR

Let \(v\) belong to the normalized active nonexceptional finite-\(\kappa\) class, with sufficient regularity for all displayed terms. Put

\[
\tau_*(v)=\frac1{4D_2(v)},
\qquad
w=H_{\tau_*}v.
\]

Assume

\[
\boxed{
H_{\tau_*}N(v)
=
\kappa D_2(2L-1)w.
}
\tag{10.1}
\]

Then

\[
\boxed{v=0.}
\tag{10.2}
\]

### Status

CPHR is the only terminal theorem left open in this curated proof. It is formulated entirely in the physical output space and therefore avoids:

- exact genealogical recurrence;
- FWE/UPN;
- finite Fourier support;
- projective discreteness;
- channel-faithful GWCI descent;
- continuum inversion by finitely many semigroup readers.

A proof of CPHR would exclude normalized active nonexceptional stationary finite-\(\kappa\) profiles directly.

---

# 11. Conditional transverse consequences of CPHR

Assume CPHR.

If \(v\in\Sigma_\kappa\) and

\[
T(v)=\kappa R_{\rm fv}(v),
\]

then by (0.3)

\[
N(v)-\kappa Y_v=0.
\]

Hence (9.6) holds, CPHR gives \(v=0\), and this contradicts the normalization \(E(v)=1\).

Therefore

\[
\boxed{
T(v)\neq\kappa R_{\rm fv}(v)
\qquad
\forall v\in\Sigma_\kappa.
}
\tag{11.1}
\]

Assume now that \(K\) is compact, the maps

\[
T,
\qquad
R_{\rm fv},
\qquad
\kappa,
\qquad
W,
\qquad
D_3
\]

are continuous in the chosen topology, and \(\Sigma_\kappa\subset K\) is nonempty. Then \(\Sigma_\kappa\) is compact.

From the homogeneous radial theorem,

\[
R_{\rm fv}(v)=0
\Longrightarrow
v=0,
\]

so normalization gives

\[
R_{\rm fv}(v)\neq0
\qquad(v\in\Sigma_\kappa).
\]

Define

\[
\Psi(v)
=
\frac{
\|T(v)-\kappa(v)R_{\rm fv}(v)\|_{H^{-1/2}}
}{
\|T(v)\|_{H^{-1/2}}
+
\kappa(v)\|R_{\rm fv}(v)\|_{H^{-1/2}}
}.
\tag{11.2}
\]

By (11.1), \(\Psi>0\) on the compact stratum. Hence

\[
\eta_K
:=
\min_{v\in\Sigma_\kappa}\Psi(v)>0.
\]

Therefore

\[
\boxed{
\|T-\kappa R_{\rm fv}\|_{H^{-1/2}}
\ge
\eta_K
\bigl(
\|T\|_{H^{-1/2}}
+
\kappa\|R_{\rm fv}\|_{H^{-1/2}}
\bigr)
\quad\text{on }\Sigma_\kappa.
}
\tag{11.3}
\]

If in addition \(T\neq0\) throughout the compact stratum and every positive proportionality \(T=\lambda R_{\rm fv}\) is excluded there, the usual compact Cauchy–Schwarz argument gives an angle

\[
\theta_K>0
\]

with

\[
\angle(T,R_{\rm fv})\ge\theta_K,
\]

and then

\[
\boxed{
\|T-\kappa R_{\rm fv}\|
\ge
\sin\frac{\theta_K}{2}
\bigl(
\|T\|+
\kappa\|R_{\rm fv}\|
\bigr).
}
\tag{11.4}
\]

---

# 12. Current dependency graph

The active proof program is now

\[
\boxed{
\begin{gathered}
\text{Mother completeness}\
\Downarrow\\
\text{one-dimensional helical fibers}\
\Downarrow\\
\text{polarized scalar Curl--Killing channels}\
\Downarrow\\
\text{exact scalar finite-viscosity radial transfer}\
\Downarrow\\
\boxed{\text{Bridge 1: exact unfolded channel closure}}\\
\Downarrow\\
\text{positive-measure support rectangles}\
+\text{ strict heat--Poisson curvature}\
\Downarrow\\
\text{positive channel-lift conductance}\
\Downarrow\\
\boxed{\text{channel quotient descent fails generically}}\\
\Downarrow\\
\text{work directly after physical aggregation}\
\Downarrow\\
H_{\tau_*}N(v)
=\kappa D_2(2L-1)H_{\tau_*}v\\
\Downarrow\\
\boxed{\textbf{CPHR}}\\
\Downarrow\\
\text{stationary exclusion}\
\Downarrow\\
\text{transverse gap on }\Sigma_\kappa.
\end{gathered}
}
\tag{12.1}
\]

## What has been deliberately removed from this file

The following material is retained in Git history but no longer occupies the main proof:

- repeated rank-one/direct-product no-go formulations;
- exact recurrence/projective discreteness branches;
- FWE and UPN conditional completion theorems;
- same-sign primitive-loop decomposition discussions;
- FSSS as a separate finite-reader program;
- conditional GWCI consequences after the channel-descent construction was disproved;
- repeated compactness and angle-gap derivations.

Those routes were useful during discovery, but they are no longer the shortest current path.

---

# Final status

The current document proves:

\[
\boxed{
\begin{aligned}
&\text{Mother whole-state completeness},\\
&\text{canonical finite-energy radial inversion},\\
&\text{Bridge 1 exact unfolded projective channel closure},\\
&\text{positive-measure companion rectangle extraction under (NE-S)},\\
&\text{strict heat--Poisson rectangle curvature},\\
&\text{positive channel-lift conductance under (G-Reg)+(G-NE)},\\
&\text{channel-faithful quotient-descent no-go}.
\end{aligned}
}
\]

The remaining terminal statement is

\[
\boxed{
\textbf{Canonical Physical Heat-Rigidity (CPHR):}
\qquad
H_{\tau_*}N(v)
=
\kappa D_2(2L-1)H_{\tau_*}v
\Longrightarrow
v=0.
}
\]

A proof of CPHR would close the stationary nonexceptional branch without recurrence, FWE, holonomy completion, or channel-faithful Ward descent.
