# PART 0. MOTHER / SPECTRAL-FLAG COMPLETENESS FOUNDATION

> **Structural status.** The theorem in this part is a whole-state coordinate theorem for smooth homogeneous incompressible Navier--Stokes. It is logically prior to the finite-companion/holonomy argument below. It is **not** a regularity theorem, a blow-up exclusion theorem, or a weak-solution theorem. Its role here is to identify the complete operator-valued state coordinate on which the later helical, channel, semigroup, and rigidity constructions live.

The decisive object is the **mother deformation**

\[
\boxed{
\mathcal M(u):=E_u=[\nabla_u,C],
}
\tag{0.1}
\]

where

\[
C=\operatorname{curl},
\qquad
\nabla_vw=P[(v\cdot\nabla)w],
\qquad
S(u)=\frac12(\nabla u+\nabla u^T).
\]

The full shifted spectral flag is a canonical spectral tomography of this smaller complete object.

> **Notation warning.** The mother operator \(E_u=[\nabla_u,C]\) is not the scalar normalized energy \(E\) appearing later in conditions such as \(E=M=1\). The subscript on \(E_u\) will be retained throughout this Part 0 to keep those objects distinct.

---

## 0.1 Periodic state space and shifted spectral flag

Let

\[
\mathcal X_\infty
:=
\left\{
 u\in C^\infty(\mathbb T^3;\mathbb R^3):
 \nabla\cdot u=0,
 \ \int_{\mathbb T^3}u\,dx=0
\right\}.
\]

On \(\mathcal X_\infty\), periodic curl is self-adjoint and has no zero mode. For every real threshold \(a\), set

\[
H_a:=\operatorname{sgn}(C-aI),
\qquad
\Gamma_u:=\nabla_u,
\]

\[
A_a(u):=[\Gamma_u,H_a],
\qquad
\mathscr O_a(u):=H_aA_a(u)-A_a(H_au).
\tag{0.2}
\]

At a discrete spectral seam one may take either one-sided sign convention. The seam set is countable and does not affect the layer-cake integral below.

---

## 0.2 Mother / Spectral-Flag Completeness Theorem

### Theorem 0.1 — complete structural compiler

For \(u,v\in\mathcal X_\infty\), the following are equivalent:

\[
\boxed{
\mathscr O_a(u)=\mathscr O_a(v)
\quad\text{for a.e. }a\in\mathbb R,
}
\tag{0.3}
\]

\[
\boxed{E_u=E_v,}
\tag{0.4}
\]

\[
\boxed{S(u)=S(v),}
\tag{0.5}
\]

\[
\boxed{u=v.}
\tag{0.6}
\]

More precisely, the reconstruction is explicit:

\[
\boxed{
\{\mathscr O_a(u)\}_{a\in\mathbb R}
\longrightarrow
E_u
\longrightarrow
\sigma_1(E_u)
\longrightarrow
q_u(x,n)
\longrightarrow
S(u)
\longrightarrow
u,
}
\tag{0.7}
\]

where the last symbol in (0.7) is the recovered velocity \(u\) itself, namely

\[
\boxed{u=2\Delta^{-1}\operatorname{div}S(u).}
\tag{0.8}
\]

Thus the intended compiler is

\[
\boxed{
\mathscr O
\longleftrightarrow
E
\longleftrightarrow
S
\longleftrightarrow
u/\operatorname{Kill}.
}
\tag{0.9}
\]

Here \(u/\operatorname{Kill}\) means that before periodic mean-zero normalization the only kernel is the flat Killing sector; on the mean-zero torus that kernel is zero.

### Proof

Because \(\Gamma_u^*=-\Gamma_u\), \(H_a^*=H_a\), and \(H_a^2=I\), one has

\[
A_a(u)^*=A_a(u),
\qquad
H_aA_a(u)+A_a(u)H_a=0.
\]

Hence \(H_aA_a(u)\) is skew-adjoint, while \(A_a(H_au)\) is self-adjoint. Therefore

\[
\boxed{
A_a(u)=H_a\operatorname{skew}\mathscr O_a(u).
}
\tag{0.10}
\]

For scalar curl spectral values \(x,y\),

\[
\frac12\int_{\mathbb R}
\bigl(\operatorname{sgn}(y-a)-\operatorname{sgn}(x-a)\bigr)\,da
=y-x.
\]

Consequently, first on trigonometric test fields and then in the natural weak operator sense,

\[
\boxed{
E_u
=[\Gamma_u,C]
=\frac12\int_{\mathbb R}A_a(u)\,da
=\frac12\int_{\mathbb R}
H_a\operatorname{skew}\mathscr O_a(u)\,da.
}
\tag{0.11}
\]

Since Leray projection commutes with curl on the flat torus,

\[
\boxed{
E_uv
=-P\sum_{j=1}^3\nabla u_j\times\partial_jv.
}
\tag{0.12}
\]

Thus \(E_u\) is an exact projected first-order operator in the probe field. For \(\xi\neq0\), \(b\perp\xi\), its principal symbol is

\[
\sigma_1(E_u)(x,\xi)b
=-iP_\xi\bigl((\nabla u(x))^T\xi\times b\bigr).
\]

Writing \((\nabla u)^T\xi=\alpha\xi+r\) with \(r\perp\xi\), the term \(r\times b\) is parallel to \(\xi\) and is killed by \(P_\xi\). Since the skew part of \(\nabla u\) has zero quadratic form,

\[
\alpha
=\frac{\xi^TS(u)\xi}{|\xi|^2}.
\]

Therefore

\[
\boxed{
\sigma_1(E_u)(x,\xi)b
=-i\frac{\xi^TS(u)(x)\xi}{|\xi|^2}\,\xi\times b.
}
\tag{0.13}
\]

For \(n\in S^2\), define the scalar strain reader

\[
q_u(x,n):=n^TS(u)(x)n.
\tag{0.14}
\]

Equation (0.13) determines \(q_u\) exactly. The spherical fourth-moment identity and \(\operatorname{tr}S=0\) give

\[
\boxed{
S(u)(x)
=\frac{15}{2}
\fint_{S^2}q_u(x,n)n\otimes n\,dn.
}
\tag{0.15}
\]

Finally incompressibility gives

\[
\operatorname{div}S(u)=\frac12\Delta u,
\]

so the mean-zero normalization yields (0.8). Thus equality of the full flag implies equality of \(E\), equality of \(E\) implies equality of strain, and equality of strain implies equality of the state. The converse implications are immediate from the definitions. \(\square\)

---

## 0.3 The mother is already complete

### Corollary 0.2

The smaller map

\[
\boxed{
\mathcal M:u\mapsto E_u=[\nabla_u,C]
}
\tag{0.16}
\]

is injective on \(\mathcal X_\infty\), with an explicit linear decoder obtained from its principal symbol. The full shifted flag is therefore a spectral resolution of an already-complete mother coordinate rather than an independent enlargement of the state.

This is the structural compression used throughout the remainder of the proof:

\[
\boxed{
\text{stronger compiler}\quad\Longrightarrow\quad\text{smaller primitive object}.
}
\tag{0.17}
\]

---

## 0.4 Exact Sobolev observability of the mother coordinate

For every real \(s\) for which the homogeneous norms are finite,

\[
\boxed{
2\|S(u)\|_{\dot H^s}^2
=\|u\|_{\dot H^{s+1}}^2.
}
\tag{0.18}
\]

Moreover

\[
\boxed{
\|u\|_{\dot H^{s+1}}^2
=15\int_{\mathbb T^3}
\fint_{S^2}
|\Lambda_x^sq_u(x,n)|^2\,dn\,dx.
}
\tag{0.19}
\]

A continuum of directions is not required for quantitative inversion. With

\[
n_1=e_1,
\quad n_2=e_2,
\quad n_3=e_3,
\]

\[
n_4=\frac{e_1+e_2}{\sqrt2},
\quad
n_5=\frac{e_1+e_3}{\sqrt2},
\quad
n_6=\frac{e_2+e_3}{\sqrt2},
\]

one has the deterministic six-reader estimate

\[
\boxed{
\frac{7-\sqrt{17}}{16}
\|u\|_{\dot H^{s+1}}^2
\le
\sum_{r=1}^6
\|\Lambda_x^sq_u(\cdot,n_r)\|_2^2
\le
\frac{7+\sqrt{17}}{16}
\|u\|_{\dot H^{s+1}}^2.
}
\tag{0.20}
\]

The constants are universal, bandwidth independent, and scale covariant.

In particular, whenever a residual

\[
W:=T-\kappa R_{\rm fv}
\]

lies in the domain of the mother decoder, the target transverse norm admits the exact structural reader

\[
\boxed{
\|W\|_{\dot H^{-1/2}}^2
=2\|S(W)\|_{\dot H^{-3/2}}^2,
}
\tag{0.21}
\]

and the six fixed strain directions quantitatively observe the same residual by taking \(s=-3/2\) in (0.20).

This does **not** by itself prove that \(W\neq0\); it says that once non-saturation is established, the mother coordinate supplies a mode-count-independent quantitative measurement of the residual.

---

## 0.5 Mother embedding of the projective channel calculus

Whenever a channel representative \(\psi_c\) lies in the domain of \(\mathcal M\), define its mother line

\[
\boxed{
\mathbb E_c
:=\mathcal M(L_c)
=\mathbb C E_{\psi_c}.
}
\tag{0.22}
\]

Because \(\mathcal M\) is linear and injective on the physical state class,

\[
\boxed{
L_c=L_d
\iff
\mathbb E_c=\mathbb E_d.
}
\tag{0.23}
\]

Under a projective gauge change \(\psi_c\mapsto g_c\psi_c\),

\[
E_{\psi_c}\mapsto g_cE_{\psi_c}.
\]

Thus the one-dimensional channel geometry constructed later in Bridge 1 admits a faithful mother-coordinate realization. In particular, projective equality need not be tested by an ad hoc metric when the full mother data are available.

This embedding is a **coordinate statement**, not a recurrence theorem: completeness does not imply that two distinct genealogical descendants ever become exactly equal.

---

## 0.6 Compatibility with the no-go theorems below

Mother completeness does not invalidate any of the no-go statements in Parts I–VI.

1. The complete object is operator/tensor valued. A finite list of scalar Poisson/heat readers can have a large kernel even though \(E_u\) or the full flag is complete.
2. Exact radial inversion remains a direct-product operation when edge forcings are treated as independent data.
3. Rank-one amplitude identities remain flat: rank one alone produces holonomy \(1\).
4. Mother completeness supplies neither exact genealogical recurrence nor primitive nonflatness.
5. Compactness of a continuous complete state geometry does not imply exact projective discreteness.

Accordingly Sections 28–32 below remain valid as **conditional finite-state recurrence lemmas**, but exact discreteness is not promoted here to a structural consequence of Theory-2.

---

## 0.7 Whole-space scope

For divergence-free Schwartz fields on \(\mathbb R^3\), the local mother formula (0.12), principal-symbol identity (0.13), spherical inversion (0.15), Poisson reconstruction, and Sobolev identities remain valid; decay removes the Euclidean Killing sector. The shifted spectral family is defined by the Fourier/helical spectral calculus and (0.11) is interpreted weakly against Schwartz test fields.

The later continuum \(L^2\)-support arguments in Part VI use less regular objects. **No step below may silently use Mother Theorem 0.1 to upgrade an arbitrary rough \(L^2\) state to the smooth/Schwartz class.** Whenever the mother decoder or its principal symbol is invoked in the whole-space terminal program, the required regularity/topology must be stated at that point.

This keeps structural completeness separate from the regularity problem.

---

## 0.8 Updated dependency chain for the present proof

The current proof should therefore be read in the following order:

\[
\boxed{
\begin{gathered}
\text{whole-state mother completeness}
\\
\mathscr O\longleftrightarrow E=[\nabla_u,C]\longleftrightarrow S\longleftrightarrow u/\operatorname{Kill}
\\
\Downarrow
\\
\text{helical one-dimensional spectral fibers}
\\
\Downarrow
\\
\text{polarized scalar Curl--Killing Formation channels}
\\
\Downarrow
\\
\text{scalar finite-viscosity radial transfer}
\\
\Downarrow
\\
\text{exact genealogical unfolding and gauge-covariant gains}
\\
\Downarrow
\\
\boxed{\text{BRIDGE 1}}
\\
\Downarrow
\\
\text{support-geometric companion rectangles}
\\
+\ \text{strict semigroup multiplier curvature}
\\
\Downarrow
\\
\boxed{\text{FSSS / finite bounded-reader separation}}
\\
\Downarrow
\\
T\neq\lambda R_{\rm fv}\quad(\lambda>0)
\\
\Downarrow
\\
\text{compactness + mother/physical norm observability}
\\
\Downarrow
\\
\|T-\kappa R_{\rm fv}\|_{H^{-1/2}}
\ge
\eta_K\bigl(\|T\|_{H^{-1/2}}+\kappa\|R_{\rm fv}\|_{H^{-1/2}}\bigr).
\end{gathered}
}
\tag{0.24}
\]

The Mother theorem therefore strengthens the foundation and the quantitative readout, but it does **not** manufacture the missing Bridge-2 separation identity. In the current frontier of this file, the genuinely new terminal task remains the finite bounded-reader determinant/FSSS problem formulated in Part VI.

---

# BEGIN FINITE-COMPANION / HOLONOMY RIGIDITY PROOF

The material below is retained as the current finite-companion proof and its successive Bridge-2 audits. The Mother theorem above is logically prior to it and should be used as the structural whole-state compiler throughout.

---

This file records the strongest level of the finite-companion argument that is mathematically justified after importing the Mother / Spectral-Flag Completeness Theorem above.

There are now three structural layers:

1. **No-go layer.** The radial equations, rank-one identities, compactness, and finite scalar readers do not by themselves imply a nontrivial holonomy defect.
2. **Bridge-1 layer.** Exact channel-resolved projective closure is proved from helical one-dimensionality, polarized Curl--Killing Formation, scalar finite-viscosity transfer, and genealogical unfolding. It is no longer an additional axiom.
3. **Bridge-2 terminal layer.** The current proof extracts positive-measure support-geometric companion rectangles and proves strict mixed heat--Poisson semigroup multiplier curvature. What remains unproved is the finite bounded-reader separation statement FSSS (or an equivalent theorem forcing saturation-flat finite data).

Accordingly, what cannot responsibly be supplied is a fictitious proof of the remaining saturation-separation identity from hypotheses that do not yet imply it.

---

# Main Resolution Theorem

Let \(K\) satisfy the normalized finite-\(\kappa\) assumptions in the problem, including

\[
E=M=1,\qquad
0<\kappa_0\le \kappa\le\kappa_1,
\qquad
\frac{d^2}{D_3}\ge\delta_0>0,
\]

and let

\[
\mathscr R_\sigma
=
-2D_2\rho\partial_\rho
-\chi_\sigma\rho^2+ra\rho-4D_2,
\qquad
\chi_\sigma\ge\chi_K>0.
\]

Then:

\[
\boxed{\text{I.}}
\]

Every smooth annular forcing has a unique finite-\(H^{-1/2}\) radial absorber.

\[
\boxed{\text{II.}}
\]

For a finite rank-one incidence network \(Z_{ij}=A_iB_j\), all Laurent-monomial identities generated solely by rank one are cycle identities, and every such cycle holonomy is exactly \(1\).

\[
\boxed{\text{III.}}
\]

A finite collection of equations

\[
F_e=\kappa\mathscr R_{\sigma_e}f_e
\]

is a direct-product problem. These equations themselves impose no cross-edge multiplicative consistency condition.

\[
\boxed{\text{IV.}}
\]

Finitely many Poisson/heat depths do not, in general, determine arbitrary radial packets, even if the complete angular dependence is retained and even if the admissible family is compact.

Consequently the requested positive defect

\[
|\operatorname{Hol}_\Gamma-1|\ge c_K>0
\]

does **not** follow from the displayed assumptions of A–C.

The remainder of this file goes further than these no-go statements. Bridge 1 proves the exact channel-resolved projective closure law rather than assuming it. Later parts then replace the failed compactness-to-recurrence route by support-geometric rectangle extraction and strict semigroup multiplier curvature. The current terminal bottleneck is FSSS: a finite bounded-reader identity for which positive saturation forces flatness while the extracted semigroup rectangle forces nonflatness. Once such a pointwise separation theorem is established, compactness of the normalized class produces the desired uniform transverse gap; under uniform nonvanishing it also yields the angular gap.

We now prove every assertion.

---

# 1. Exact inversion of the finite-viscosity radial operator

Fix \(\sigma\in\{\pm1\}\). Set

\[
\mathscr R_\sigma
=
-2D_2\rho\partial_\rho
-\chi_\sigma\rho^2
+ra\rho
-4D_2,
\]

where

\[
D_2>0,\qquad \chi_\sigma>0.
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
\]

## Lemma 1.1

\[
\boxed{\mathscr R_\sigma h_\sigma=0.}
\]

### Proof

We have

\[
\frac{h_\sigma'}{h_\sigma}
=
-\frac2\rho
-\frac{\chi_\sigma}{2D_2}\rho
+\frac{ra}{2D_2}.
\]

Thus

\[
-2D_2\rho\frac{h_\sigma'}{h_\sigma}
=
4D_2+\chi_\sigma\rho^2-ra\rho.
\]

Therefore

\[
\mathscr R_\sigma h_\sigma=0.
\]

\(\square\)

## Theorem 1.2 — canonical annular right inverse

Let \(F_\sigma\) be smooth and supported in

\[
\rho_0<\rho<\rho_1,
\qquad
0<\rho_0<\rho_1<\infty.
\]

Then

\[
\kappa\mathscr R_\sigma f=F_\sigma
\]

has the unique finite-\(H^{-1/2}\) solution

\[
\boxed{
(\mathcal S_\sigma F)(\rho,\omega)
=
-\frac{h_\sigma(\rho)}{2\kappa D_2}
\int_0^\rho
\frac{F(s,\omega)}{s\,h_\sigma(s)}\,ds.
}
\]

### Proof

Write \(f=h_\sigma c\). Since \(\mathscr R_\sigma h_\sigma=0\),

\[
\mathscr R_\sigma(h_\sigma c)
=-2D_2\rho h_\sigma c'.
\]

Hence

\[
c'=-\frac{F}{2\kappa D_2\rho h_\sigma},
\]

which yields the formula above after imposing the finite-energy infrared branch. For \(\rho<\rho_0\), the solution vanishes; for \(\rho>\rho_1\), it is a scalar multiple of \(h_\sigma\), hence has Gaussian ultraviolet decay because \(\chi_\sigma>0\).

If two finite-energy solutions exist, their difference is \(C(\omega)h_\sigma(\rho)\). Since \(h_\sigma(\rho)\sim \rho^{-2}\) as \(\rho\downarrow0\),

\[
\int_0^\varepsilon \rho |h_\sigma|^2\,d\rho
\sim
\int_0^\varepsilon \rho^{-3}\,d\rho
=\infty.
\]

Therefore \(C=0\), proving uniqueness. \(\square\)

---

# 2. Radial pairing and high-frequency resolvent estimate

For smooth compactly supported \(f\), integration by parts gives

\[
\boxed{
\operatorname{Re}\langle f,\mathscr R_\sigma f\rangle_{H^{-1/2}}
=
\int \rho\left(-\chi_\sigma\rho^2+ra\rho-2D_2\right)|f|^2\,d\rho\,d\omega.
}
\]

On a compact coefficient class with \(\chi_\sigma\ge\chi_K>0\), one obtains for sufficiently large \(\rho_*\), on a fixed-ratio annulus,

\[
\boxed{
\|f\|_{H^{-1/2}}
\le C_K\rho_*^{-2}\|\mathscr R_\sigma f\|_{H^{-1/2}}.
}
\]

This is a gain estimate and is fully compatible with the exact solvability above.

---

# 3. Rank-one cycle identities

Let \(Z_{ij}=A_iB_j\) on a finite bipartite graph. For any alternating cycle

\[
\Gamma:i_1-j_1-i_2-j_2-\cdots-i_m-j_m-i_1,
\]

define

\[
\operatorname{Hol}^Z_\Gamma
=
\prod_{\ell=1}^m\frac{Z_{i_\ell j_\ell}}{Z_{i_{\ell+1}j_\ell}},
\qquad i_{m+1}=i_1.
\]

Then

\[
\boxed{\operatorname{Hol}^Z_\Gamma=1.}
\]

All Laurent-monomial identities valid for arbitrary nonzero factors \(A_i,B_j\) are generated by these cycle relations, because the exponent vector must have zero row and column sums, i.e. be an integral circulation in the bipartite graph.

For a rectangle,

\[
\boxed{Z_{ii}Z_{jj}=Z_{ij}Z_{ji}.}
\]

---

# 4. Direct-product radial absorption

For finitely many edges \(e\), define

\[
\mathbf R_\Gamma=\bigoplus_e\kappa\mathscr R_{\sigma_e},
\qquad
\mathbf S_\Gamma=\bigoplus_e\mathcal S_{\sigma_e}.
\]

Then

\[
\boxed{\mathbf R_\Gamma\mathbf S_\Gamma=I.}
\]

Thus locally specified edge forcings can be absorbed edgewise. If

\[
F_e=Z_e\Phi_e,
\]

then

\[
\boxed{f_e=Z_e\mathcal S_{\sigma_e}\Phi_e.}
\]

This proves that radial inversion alone does not create cross-edge multiplicative compatibility.

---

# 5. Reality completion

The radial coefficients are real, hence under the reality-completed Fourier involution,

\[
F_{\bar e}=\overline{F_e}
\quad\Longrightarrow\quad
f_{\bar e}=\overline{f_e}.
\]

Reality supplies conjugate channels but does not by itself create recurrence between distinct forward edges.

---

# 6. Finite-depth readers are not injective on the full packet space

For a fixed annulus \(I\Subset(0,\infty)\), the space \(C_c^\infty(I)\) is infinite-dimensional. Any finite collection of Poisson/heat readers, including finitely many readers applied to \(\mathscr R_\sigma f\), gives finitely many linear functionals. Their common kernel is nontrivial. Therefore finite depths cannot exactly reconstruct arbitrary radial packets without an independently proved finite-dimensional packet structure.

The Vandermonde determinant correctly proves only finite-jet separation.

---

# 7. Provisional projective formulation and finite-witness compactness

The first version of the argument introduced a Channel-Resolved Projective Closure hypothesis (CRPC), scalar gains \(h_e\), incidence-cycle holonomy, and the compactness principle converting pointwise finite witnesses into finitely many uniform witnesses.

Those formal conclusions are correct once a scalar channel connection exists. The question left open there was whether CRPC itself had to be assumed.

The remainder of this file now resolves that question.

---

# PART II. BRIDGE 1 — EXACT UNFOLDED CHANNEL/FIBER CLOSURE

> **Status update.** This part supersedes the earlier provisional treatment of CRPC as an additional axiom. The closure statement is derived from the complex helical Fourier geometry, the polarized Curl–Killing identity, the scalar radial Green operator, and exact genealogical unfolding before physical summation. What remains after this section is only the finite exact recurrence/nonflat-witness problem, called **Bridge 2**.

We prove

\[
\boxed{
\text{physical Curl–Killing interaction}
\Longrightarrow
\text{exact channel-resolved projective state/fiber closure}
}
\]

on the unfolded interaction network.

Throughout this part, fix a normalized finite-\(\kappa\) state and freeze the stationary scalar coefficients

\[
D_2,\qquad r=\frac{D_3}{d^2},\qquad a,\qquad b,
\]

so that

\[
\mathscr R_\sigma
=
-2D_2\rho\partial_\rho
-\chi_\sigma\rho^2+ra\rho-4D_2,
\qquad
\chi_\sigma=r(1-\sigma b)-1>0.
\]

All Fourier fibers below are complexified. Reality is restored by conjugate completion at the end.

---

## 8. One-dimensional helical Fourier fibers

Let \(k\in\mathbb R^3\setminus\{0\}\). The complexified divergence-free Fourier fiber is

\[
V_k:=\{z\in\mathbb C^3:k\cdot z=0\},
\]

which has complex dimension two. Let

\[
P_k=I-\frac{k\otimes k}{|k|^2}
\]

and define

\[
H_k:=\frac{i\,k\times}{|k|}.
\]

On \(V_k\),

\[
k\times(k\times z)=-|k|^2z,
\]

so

\[
H_k^2=I\qquad\text{on }V_k.
\]

Moreover \(k\times\) is real skew-adjoint, hence \(i\,k\times\) is Hermitian. Therefore \(H_k\) is Hermitian on the two-dimensional complex space \(V_k\), with eigenvalues \(\pm1\).

Define

\[
E_\sigma(k):=\ker(H_k-\sigma I),
\qquad \sigma\in\{+1,-1\}.
\]

Since the two eigenvalues are distinct and \(\dim_\mathbb C V_k=2\),

\[
\boxed{\dim_\mathbb C E_\sigma(k)=1.}
\tag{8.1}
\]

Extending \(H_k\) by zero on the longitudinal direction, the helical projector is

\[
\boxed{
Q_\sigma(k)=\frac12(P_k+\sigma H_k).
}
\tag{8.2}
\]

For \(z\in E_\sigma(k)\),

\[
i\,k\times z=\sigma|k|z.
\]

Thus a Fourier atom \(ze^{ik\cdot x}\) with \(z\in E_\sigma(k)\) is a Curl eigenmode of signed root \(\sigma|k|\).

Hence

\[
\boxed{
\text{one nonzero frequency and one helicity sign determine one complex projective line.}
}
\tag{8.3}
\]

---

## 9. Helical fibers are constant along positive radial rays

Write

\[
k=\rho\omega,\qquad \rho>0,\quad |\omega|=1.
\]

Then

\[
H_{\rho\omega}
=
\frac{i(\rho\omega)\times}{\rho}
=i\omega\times,
\]

which is independent of \(\rho\). Hence

\[
\boxed{
E_\sigma(\rho\omega)=E_\sigma(\omega)
\qquad(\rho>0).
}
\tag{9.1}
\]

Fix a nonzero frame vector

\[
e_\sigma(\omega)\in E_\sigma(\omega).
\]

Every field on this ray/helicity component has the form

\[
\widehat u_\sigma(\rho,\omega)
=f_\sigma(\rho,\omega)e_\sigma(\omega).
\]

No radial derivative of the polarization frame appears. Consequently all radial evolution on a fixed helical ray is scalar.

---

## 10. Exact polarized Curl–Killing channel closure

Take polarized Fourier inputs

\[
a_p=Ae_{\sigma_p}(p),
\qquad
b_q=Be_{\sigma_q}(q),
\]

with \(p,q\neq0\), and set

\[
k=p+q\neq0.
\]

Their signed Curl roots are

\[
x=\sigma_p|p|,
\qquad
y=\sigma_q|q|.
\]

The polarized Curl–Killing identity is

\[
2B(a_p,b_q)
=(x-y)P_k(b_q\times a_p).
\]

Projecting to output helicity \(\tau\),

\[
B^\tau_{p,q}(a_p,b_q)
:=Q_\tau(k)B(a_p,b_q)
=
\frac{x-y}{2}Q_\tau(k)(b_q\times a_p).
\tag{10.1}
\]

Substituting the one-dimensional input representatives,

\[
B^\tau_{p,q}(a_p,b_q)
=
AB\frac{x-y}{2}
Q_\tau(k)
\bigl(e_{\sigma_q}(q)\times e_{\sigma_p}(p)\bigr).
\]

Because \(\operatorname{Ran}Q_\tau(k)=E_\tau(k)\) is one-dimensional, there is a unique scalar \(m^\tau(p,q)\) such that

\[
Q_\tau(k)
\bigl(e_{\sigma_q}(q)\times e_{\sigma_p}(p)\bigr)
=
m^\tau(p,q)e_\tau(k).
\]

Define

\[
\boxed{
\beta^\tau(p,q)
:=
\frac{\sigma_p|p|-\sigma_q|q|}{2}
\,m^\tau(p,q).
}
\tag{10.2}
\]

Then

\[
\boxed{
B^\tau_{p,q}(a_p,b_q)
=AB\,\beta^\tau(p,q)e_\tau(k).
}
\tag{10.3}
\]

Thus every ordered polarized interaction is a bilinear map

\[
E_{\sigma_p}(p)\times E_{\sigma_q}(q)
\longrightarrow
E_\tau(p+q)
\]

between one-dimensional complex lines.

The channel is nonexceptional precisely when

\[
\boxed{\beta^\tau(p,q)\neq0.}
\tag{10.4}
\]

The two evident degeneracies are contained in this criterion: same signed Curl root makes the factor \(x-y\) vanish, while Leray/helical-polarization degeneracy makes \(m^\tau(p,q)=0\).

---

## 11. Exact separation of rank-one amplitude and physical geometry

If the two input families carry scalar factors \(A_i\) and \(B_j\), then

\[
Z_{ij}=A_iB_j.
\]

For a fixed projected channel \((i,j)\),

\[
\boxed{
F_{ij}
=A_iB_j\,\beta_{ij}e_{\tau_{ij}}(k_{ij})
=Z_{ij}\Phi_{ij},
}
\tag{11.1}
\]

where \(\Phi_{ij}\) contains the Curl-root, Leray and helicity geometry.

The rank-one identity

\[
Z_{ii}Z_{jj}=Z_{ij}Z_{ji}
\]

belongs solely to the input amplitudes. There is no reason for

\[
\beta_{ii}\beta_{jj}
=
\beta_{ij}\beta_{ji}.
\]

This is exactly where a future nontrivial geometric holonomy may arise: the rank-one factors cancel, while the physical channel gains need not.

---

## 12. Reality completion of helical channels

For a real vector field,

\[
\widehat u(-k)=\overline{\widehat u(k)}.
\]

If \(z\in E_\sigma(k)\), then

\[
i\,k\times z=\sigma|k|z.
\]

Conjugation gives

\[
-i\,k\times\overline z=\sigma|k|\overline z,
\]

which is equivalent to

\[
i(-k)\times\overline z=\sigma|k|\overline z.
\]

Hence

\[
\boxed{
\overline{E_\sigma(k)}=E_\sigma(-k).
}
\tag{12.1}
\]

For a finite interaction network we may choose reality-compatible local frames

\[
e_\sigma(-k)=\overline{e_\sigma(k)}.
\]

Then

\[
\boxed{
\beta^\tau(-p,-q)=\overline{\beta^\tau(p,q)}.
}
\tag{12.2}
\]

No global continuous choice of helical phase on the full sphere is required; only finitely many local choices are needed, and their phase dependence will be absorbed by gauge covariance.

---

## 13. The radial transfer operator preserves the helical line

On a fixed ray \(\omega\) write

\[
\widehat f(\rho,\omega)
=f(\rho,\omega)e_\sigma(\omega).
\]

Since \(e_\sigma(\omega)\) is independent of \(\rho\),

\[
\boxed{
\mathscr R_\sigma(fe_\sigma)
=(\mathscr R_\sigma f)e_\sigma.
}
\tag{13.1}
\]

The same holds for the canonical finite-energy inverse:

\[
\boxed{
\mathcal S_\sigma(Fe_\sigma)
=(\mathcal S_\sigma F)e_\sigma.
}
\tag{13.2}
\]

Therefore finite-viscosity radial absorption preserves the one-dimensional helical polarization line exactly.

Moreover, because

\[
\kappa\mathscr R_\sigma\mathcal S_\sigma=I,
\]

we have the injectivity-on-forcing statement

\[
\boxed{
F\neq0
\Longrightarrow
\mathcal S_\sigma F\neq0.
}
\tag{13.3}
\]

Thus the radial absorber creates no new channel nullity.

---

## 14. Exact radial Green kernel

The canonical inverse can be written

\[
(\mathcal S_\sigma F)(\rho)
=
\int_0^\infty G_\sigma(\rho,s)F(s)\,ds,
\]

where

\[
\boxed{
G_\sigma(\rho,s)
=
-\frac{h_\sigma(\rho)}{2\kappa D_2\,s\,h_\sigma(s)}
\mathbf 1_{\{s<\rho\}}.
}
\tag{14.1}
\]

Substitution of the explicit homogeneous profile gives

\[
\boxed{
G_\sigma(\rho,s)
=
-\frac{s}{2\kappa D_2\rho^2}
\exp\left[
-\frac{\chi_\sigma}{4D_2}(\rho^2-s^2)
+\frac{ra}{2D_2}(\rho-s)
\right]
\mathbf 1_{\{s<\rho\}}.
}
\tag{14.2}
\]

For \(0<s<\rho\), this scalar Green kernel is nonzero. Consequently a radial point-source channel, interpreted distributionally, is propagated to every larger radius on the same ray with a nonzero scalar kernel. For general smooth source packets, cancellations may occur at individual target radii, but the full absorbed channel is nonzero by (13.3).

This distinction avoids confusing nonvanishing of the Green kernel with pointwise nonvanishing of an arbitrary integrated packet.

---

## 15. Atomic Formation-plus-radial channel gain

For an elementary frequency interaction \(p+q=k\), write \(s=|k|\) and \(\omega_k=k/|k|\). For output helicity \(\tau\), the atomic source coefficient is \(AB\beta^\tau(p,q)\).

In the distributional Green representation, its contribution at a target radius \(\rho>s\) on the same ray has scalar coefficient

\[
AB\,G_\tau(\rho,s)\beta^\tau(p,q).
\]

Define the elementary gain

\[
\boxed{
\mathfrak h_e(\rho;p,q,\tau)
:=
G_\tau(\rho,|p+q|)\beta^\tau(p,q).
}
\tag{15.1}
\]

Then

\[
\boxed{
A_{\rm out}^{(e)}
=
\mathfrak h_e A B.
}
\tag{15.2}
\]

Explicitly,

\[
\boxed{
\begin{aligned}
\mathfrak h_e
&=
-\frac{|k|}{2\kappa D_2\rho^2}
\exp\left[
-\frac{\chi_\tau}{4D_2}(\rho^2-|k|^2)
+\frac{ra}{2D_2}(\rho-|k|)
\right]
\\
&\qquad\times
\frac{\sigma_p|p|-\sigma_q|q|}{2}
\,m^\tau(p,q).
\end{aligned}
}
\tag{15.3}
\]

This formula is useful for atomic bookkeeping. The packet-level theorem below is the rigorous finite-energy formulation and does not require delta functions.

---

## 16. Packet-level projective channel closure

Let \(\mathcal X_p,\mathcal X_q,\mathcal X_r\) denote the relevant channel packet spaces and let

\[
L_p=\mathbb C\psi_p\subset\mathcal X_p,
\qquad
L_q=\mathbb C\psi_q\subset\mathcal X_q
\]

be one-dimensional input channel lines.

Fix a labeled physical channel \(e\), including its ordered inputs, output-frequency/ray restriction, output helicity, Leray projection, reality branch, and frozen radial inverse. Let

\[
\mathcal T_e:=\mathcal S_e\circ B_e.
\]

The map \(\mathcal T_e\) is bilinear. Assume the channel is nonexceptional:

\[
\mathcal T_e(\psi_p,\psi_q)\neq0.
\]

Define

\[
\boxed{
L_e
:=
\operatorname{span}_{\mathbb C}
\{\mathcal T_e(\psi_p,\psi_q)\}.
}
\tag{16.1}
\]

### Lemma 16.1 — representative independence

The line \(L_e\) is independent of the chosen nonzero representatives of \(L_p,L_q\).

### Proof

If

\[
\psi_p\mapsto c_p\psi_p,
\qquad
\psi_q\mapsto c_q\psi_q,
\]

then bilinearity gives

\[
\mathcal T_e(c_p\psi_p,c_q\psi_q)
=
c_pc_q\mathcal T_e(\psi_p,\psi_q).
\]

Its span is unchanged. \(\square\)

Therefore each nonzero labeled channel defines canonically a projective output line

\[
\boxed{
\mathcal T_e(L_p,L_q)=L_e
}
\]

in the projective sense.

This is the exact packet-level closure statement. It does **not** claim that the aggregated physical packet at the same Fourier label is one-dimensional.

---

## 17. Finite-depth iteration

Start from a finite collection of seed channel vertices, each carrying a one-dimensional line \(L_c\). Suppose the channel lines have been defined through depth \(n\). For a nonexceptional interaction

\[
e=(c_1,c_2\to c_3)
\]

with parents of depth at most \(n\), define

\[
L_{c_3}
:=
\mathcal T_e(L_{c_1},L_{c_2}).
\]

By Lemma 16.1 this is a well-defined one-dimensional line.

Induction proves:

### Theorem 17.1 — finite-depth projective closure

Every finite rooted interaction history built from nonexceptional polarized Curl–Killing channels and frozen finite-viscosity radial absorption carries a canonically defined one-dimensional complex channel line at every genealogical vertex.

No bound or constant in this construction depends on the total number of Fourier modes, shells, or already generated channels.

\(\square\)

---

## 18. Exact unfolding of additive physical mixing

Several genealogically distinct channels may feed the same physical Fourier/ray/helicity label. They must not be collapsed before the next bilinear expansion.

For a fixed physical label \(r\), define the unfolded channel space

\[
\boxed{
\widetilde{\mathcal H}_r
:=
\bigoplus_{e\to r}L_{r,e}.
}
\tag{18.1}
\]

The physical summation map is

\[
\boxed{
\Sigma_r:\widetilde{\mathcal H}_r\to\mathcal H_r,
\qquad
\Sigma_r((u_e)_e)=\sum_eu_e.
}
\tag{18.2}
\]

Hidden cancellation is simply membership in \(\ker\Sigma_r\). The individual channel coordinates remain present in the unfolded space even if their physical sum vanishes.

Now suppose

\[
u=\sum_\alpha u_\alpha,
\qquad
v=\sum_\beta v_\beta
\]

are finite unfolded decompositions. Bilinearity gives the exact identity

\[
\boxed{
B(u,v)=\sum_{\alpha,\beta}B(u_\alpha,v_\beta).
}
\tag{18.3}
\]

After output projection and radial absorption, linearity gives

\[
\boxed{
\mathcal S B(u,v)
=
\sum_{\alpha,\beta}
\mathcal S B(u_\alpha,v_\beta).
}
\tag{18.4}
\]

Thus every downstream physical interaction has an exact expansion into interactions of individual upstream channels. No nonlinear term is discarded: the cross terms are precisely the ordered channel pairs \((\alpha,\beta)\).

At the physical packet level the amplitude law is additive,

\[
a_r^{\rm phys}
=
\sum_{e\to r}a_{r,e},
\]

whereas at the unfolded channel level each channel separately obeys a multiplicative bilinear law.

This resolves the additive-mixing obstruction exactly.

---

## 19. Canonical genealogical labels

A convenient canonical label for a channel is its finite interaction history.

Seed channels carry primitive labels. If channels \(c_1,c_2\) interact through a physical edge specification \(e\), define the child label

\[
c=(e;c_1,c_2).
\]

Iterating produces finite rooted binary trees with physical edge labels. Different histories remain distinct even if they land at the same physical frequency and helicity.

The physical state is recovered by summing all histories with the same physical label:

\[
\boxed{
\text{unfolded genealogical network}
\overset{\Sigma}{\longrightarrow}
\text{physical state}.
}
\tag{19.1}
\]

The kernel of \(\Sigma\) is precisely where exact hidden cancellations live.

At every fixed finite interaction depth, the expansion is finite whenever the seed decomposition and branching specification are finite. Bridge 1 makes no claim that the infinite-depth unfolded network has finite cardinality.

---

## 20. Scalar edge gains and gauge covariance

Choose a nonzero representative

\[
\psi_c\in L_c
\]

for every channel vertex in a finite unfolded network. For an edge

\[
e=(p,q\to r),
\]

nonexceptionality and one-dimensionality give a unique scalar \(h_e\in\mathbb C^\times\) such that

\[
\boxed{
\mathcal T_e(\psi_p,\psi_q)
=
h_e\psi_r.
}
\tag{20.1}
\]

Under independent changes of representatives

\[
\psi_c\mapsto g_c\psi_c,
\qquad
g_c\in\mathbb C^\times,
\]

bilinearity gives

\[
\boxed{h_e\mapsto g_pg_qg_r^{-1}h_e.}
\tag{20.2}
\]

This is exactly the multiplicative gauge law required for projective holonomy.

For atomic channels, \(h_e\) may be represented by the explicit coefficient \(\mathfrak h_e\) in (15.3), up to the chosen normalization of the three channel representatives.

---

## 21. Reality covariance on the unfolded network

Define conjugation recursively on genealogical labels. A seed channel at \((k,\sigma)\) is sent to its conjugate at \((-k,\sigma)\). If

\[
c=(e;c_1,c_2),
\]

define

\[
\bar c=(\bar e;\bar c_1,\bar c_2).
\]

Because the physical bilinear operator and the frozen radial coefficients are real,

\[
\boxed{L_{\bar c}=\overline{L_c}.}
\tag{21.1}
\]

With reality-compatible representatives,

\[
\psi_{\bar c}=\overline{\psi_c},
\]

and therefore

\[
\boxed{h_{\bar e}=\overline{h_e}.}
\tag{21.2}
\]

Thus the projective channel calculus respects reality completion exactly.

---

## 22. Local continuity for a fixed finite channel pattern

For later compactness arguments, consider a fixed finite nonexceptional channel pattern and let the underlying normalized state vary in \(K\).

The radial Green kernel is

\[
G_{\sigma,v}(\rho,s)
=
-\frac{s}{2\kappa(v)D_2(v)\rho^2}
\exp\left[
-\frac{\chi_\sigma(v)}{4D_2(v)}(\rho^2-s^2)
+\frac{r(v)a(v)}{2D_2(v)}(\rho-s)
\right]
\mathbf1_{\{s<\rho\}}.
\]

On the compact normalized class,

\[
\kappa\ge\kappa_0>0,
\qquad
\chi_\sigma\ge\chi_K>0.
\]

Also, by Cauchy–Schwarz in spectral measure,

\[
M^2\le ED_2.
\]

Since \(E=M=1\),

\[
\boxed{D_2\ge1.}
\tag{22.1}
\]

The helicity-gap assumption gives

\[
r=\frac{D_3}{d^2}\le\delta_0^{-1}.
\]

Under the stated graph-topology continuity of the displayed scalar functionals, all frozen coefficients remain locally controlled. On every fixed compact radial rectangle separated from \(0\), the Green kernel depends continuously on \(v,\rho,s\). The helical projectors \(Q_\sigma(k)\) are smooth for \(k\neq0\).

Therefore any fixed finite nonexceptional channel pattern has locally continuous channel lines in projective space and locally continuous edge gains after a local gauge choice. Gauge-invariant holonomies, when a finite cycle exists, are consequently continuous without making a global phase choice.

This is precisely the continuity needed for the finite-witness compactness principle proved earlier.

---

## 23. Exact Unfolded Channel/Fiber Closure Theorem

We can now package Bridge 1.

### Theorem 23.1 — Exact Unfolded Channel/Fiber Closure

Let \(v\) be a normalized finite-\(\kappa\) Theory-2 state with

\[
d>0,
\qquad
\chi_\sigma>0.
\]

Consider any finite reality-complete collection of nonexceptional polarized Curl–Killing interaction channels, and apply the frozen finite-viscosity radial absorber to every channel output. Then there exists an exact unfolded genealogical channel network satisfying:

1. **One-dimensional channel fibers.** Every channel vertex \(c\) carries a complex one-dimensional state line \(L_c\).
2. **Exact edge closure.** For every edge \(e=(p,q\to r)\),
   \[
   \boxed{\mathcal S_eB_e(L_p,L_q)=L_r}
   \]
   in the projective sense.
3. **Nonvanishing.** A nonzero projected Formation channel has a nonzero absorbed channel.
4. **Scalar edge law.** For nonzero representatives,
   \[
   \boxed{\mathcal S_eB_e(\psi_p,\psi_q)=h_e\psi_r,\qquad h_e\neq0.}
   \]
5. **Gauge covariance.** Under \(\psi_c\mapsto g_c\psi_c\),
   \[
   \boxed{h_e\mapsto g_pg_qg_r^{-1}h_e.}
   \]
6. **Exact additive reconstruction.** The physical state is obtained by summing unfolded channel contributions sharing the same physical label.
7. **Exact downstream expansion.** Every interaction of physical sums is the sum of interactions of all ordered pairs of unfolded channels.
8. **Reality covariance.** Under reality-compatible choices,
   \[
   \boxed{L_{\bar c}=\overline{L_c},\qquad h_{\bar e}=\overline{h_e}.}
   \]
9. **Arbitrary finite-depth iteration.** The construction iterates exactly to every finite interaction depth without any coercivity constant depending on the number of channels, Fourier modes, shells, or completion depth.

### Proof

Item 1 follows from the one-dimensional helical Fourier-fiber theorem at atomic level and, for general packet channels, from the representative-independent definition (16.1).

Item 2 follows from bilinearity of the polarized Curl–Killing map, preservation of helicity lines by the radial transfer operator, and the definition of the child channel line.

Item 3 follows from

\[
\kappa\mathscr R_e\mathcal S_e=I:
\]

if \(\mathcal S_eF_e=0\), then applying \(\kappa\mathscr R_e\) gives \(F_e=0\).

Item 4 follows because every nonzero vector in a one-dimensional complex line is a unique scalar multiple of any fixed nonzero representative.

Item 5 is the gauge calculation (20.2).

Items 6 and 7 follow from the physical summation map, bilinearity of Formation, and linearity of all output projections and radial absorbers.

Item 8 follows from (12.1), reality of the physical bilinear operator, and reality of the frozen radial coefficients.

Item 9 follows by induction on genealogical depth, using Items 1–4 at each new vertex. No step introduces a constant depending on the size of the already constructed network.

Therefore channel-resolved projective closure is an exact theorem on the unfolded interaction network.

\[
\boxed{\mathrm{QED}_{\text{Bridge 1}}}
\]

---

## 24. Reconciliation with the earlier no-go theorem

There is no contradiction between Bridge 1 and the earlier direct-product no-go theorem.

The no-go theorem considered a finite family of radial equations

\[
F_e=\kappa\mathscr R_e f_e
\]

with the edge forcings treated as locally independent data. Such equations indeed impose no cross-edge compatibility by themselves.

Bridge 1 adds information that is not contained in radial inversion alone: in the actual nonlinear interaction genealogy, each \(F_e\) is generated bilinearly from specified parent channel lines, and the resulting child contribution is retained as a labeled state before physical summation. This produces a canonical scalar edge calculus.

What Bridge 1 still does **not** produce is a finite exact recurrence identifying a descendant channel with a previously existing channel in a way that closes an incidence cycle. Thus it does not yet produce a nontrivial holonomy contradiction.

So the logical status is now

\[
\boxed{
\text{radial inversion alone: no loop law}
}
\]

but

\[
\boxed{
\text{physical bilinear genealogy + unfolding: exact scalar channel connection}.
}
\]

---

## 25. Relation to the rank-one companion rectangle

For a same-output rank-one rectangle,

\[
Z_{mn}=A_mB_n.
\]

After a labeled Formation-plus-radial transfer, write the scalar channel outputs as

\[
a_{mn}^{\rm out}=h_{mn}Z_{mn}.
\]

Whenever the four channel coordinates are compared through compatible projective identifications, rank one gives

\[
\boxed{
\frac{a_{ii}^{\rm out}a_{jj}^{\rm out}}
{a_{ij}^{\rm out}a_{ji}^{\rm out}}
=
\frac{h_{ii}h_{jj}}{h_{ij}h_{ji}}.
}
\tag{25.1}
\]

The \(A_iB_j\) factors cancel exactly. The remaining ratio is purely geometric/radial channel transfer.

Equation (25.1) is not yet a closed holonomy invariant: a genuine holonomy requires an exact finite cycle of channel identifications. But it identifies the precise scalar quantity in which nonflatness must ultimately appear.

---

## 26. What Bridge 1 does not prove

The unfolded interaction network is genealogical. Before recurrence is proved, it is naturally a directed acyclic expansion: each new interaction history creates a new channel label.

One may therefore have

\[
c_0\to c_1\to c_2\to\cdots
\]

with every edge carrying a perfectly well-defined nonzero scalar gain, while no descendant channel is ever exactly identified with an earlier channel.

One-dimensionality does not imply recurrence. Compactness gives approximate recurrence at best and cannot replace exact algebraic identification.

Accordingly Bridge 1 proves scalarization and exact channel/fiber closure, but not a finite loop and not a nonflatness defect.

---

# PART III. THE ONLY REMAINING STRUCTURAL BRIDGE

## 27. Bridge 2 — Finite Channel Recurrence / Nonflat Witness

After Theorem 23.1, the previously provisional assumption “channel-resolved projective closure” is removed from the list of hypotheses.

The remaining theorem is now sharply stated:

\[
\boxed{
\textbf{Finite Channel Recurrence / Nonflat Witness Theorem}
}
\]

For every forbidden positive-alignment or stationary saturation candidate \(v\in K\), prove that the exact unfolded physical channel network contains a finite collection of nonexceptional channel vertices and edges together with exact projective channel identifications forming an incidence cycle \(\Gamma_v\) such that:

1. every edge gain is the physical gain supplied by Bridge 1;
2. reality completion is respected;
3. exact candidate consistency forces
   \[
   \operatorname{Hol}_{\Gamma_v}(v)=1;
   \]
4. the Curl–Killing/radial transfer geometry gives
   \[
   \operatorname{Hol}_{\Gamma_v}(v)\neq1.
   \]

Once this pointwise finite witness is proved, the compactness theorem already established gives finitely many witness patterns and a uniform defect \(c_K>0\), independent of mode count, shell count, Fourier cutoff, and uncontrolled completion depth. The transverse saturation gap then follows from the normalized residual compactness argument.

Thus the updated dependency chain is

\[
\boxed{
\begin{gathered}
\text{helical one-dimensionality}
\\
\Downarrow
\\
\text{polarized scalar Formation channels}
\\
\Downarrow
\\
\text{scalar finite-viscosity radial transfer}
\\
\Downarrow
\\
\text{exact genealogical channel unfolding}
\\
\Downarrow
\\
\text{gauge-covariant scalar edge gains }h_e
\\
\Downarrow
\\
\boxed{\text{BRIDGE 1 CLOSED}}
\\
\Downarrow
\\
\text{finite exact recurrence/nonflat witness}
\\
\Downarrow
\\
\text{uniform holonomy defect by compactness}
\\
\Downarrow
\\
T\neq\kappa R_{\rm fv}
\\
\Downarrow
\\
\|T-\kappa R_{\rm fv}\|
\ge
\eta_K(\|T\|+\kappa\|R_{\rm fv}\|).
\end{gathered}
}
\]

No continuum Poisson inversion, infinite moment hierarchy, Galerkin evidence, Fourier cutoff, bounded mode count, or uncontrolled higher Sobolev coercivity has been used in Bridge 1.

\[
\boxed{\mathrm{QED}_{\text{Bridge 1}}}
\]

The mathematical frontier is now Bridge 2 alone.

---

# PART IV. BRIDGE 2 — FIRST LAYER: EXACT RECURRENCE AND PRIMITIVE CURVATURE

> **Logical status.** The statements in this part are rigorous conditional theorems. They isolate two genuinely new hypotheses that are not consequences of Bridge 1: exact projective discreteness and quantitative primitive nonflatness. The purpose of this part is to prove exactly what follows from those hypotheses and to prevent compactness or curvature language from being used beyond its legitimate scope.

Bridge 2 naturally splits into two logically distinct tasks:

\[
\boxed{
\text{recurrence: produce an exact finite return}
}
\]

and

\[
\boxed{
\text{nonflatness: prove a nonzero gauge-invariant defect on that return.}
}
\]

Compactness alone gives neither statement.

---

## 28. Reachable projective channel states

Let \(\mathfrak P_K\) denote the set of all projective channel states reachable from candidates \(v\in K\) through the exact unfolded construction of Bridge 1.

A point \(X\in\mathfrak P_K\) is understood to contain **all data required for exact future reuse of the channel**, not merely its Fourier direction or its polarization line. In particular, equality \(X=Y\) means that the two states are interchangeable as inputs for the subsequent channel calculus, including all labels that enter the allowed successor rule.

Equip \(\mathfrak P_K\) with a metric \(d_{\rm proj}\) satisfying

\[
\boxed{
d_{\rm proj}(X,Y)=0\iff X=Y.
}
\tag{28.1}
\]

The metric is not assumed to be induced by a finite Fourier truncation.

We distinguish a single-channel state from a **completed frontier state**. A completed frontier state records the entire finite collection of open channel ends, with their projective data and incidence labels, at a given stage of a companion-completion procedure. Exact recurrence of one distinguished channel is weaker than exact recurrence of a completed frontier state; only the latter automatically closes all side parents and open boundaries needed for an incidence-cycle holonomy.

---

## 29. Exact projective discreteness hypotheses

Assume the following.

### (R1) Compactness

\[
\boxed{\mathfrak P_K\text{ is compact}.}
\tag{R1}
\]

### (R2) Exact projective discreteness

There exists \(\delta_K>0\) such that for all reachable states \(X,Y\in\mathfrak P_K\),

\[
\boxed{
X\neq Y
\Longrightarrow
d_{\rm proj}(X,Y)\ge\delta_K.
}
\tag{R2}
\]

### (R3) Nontermination outside the excluded exceptional set

Every open nonexceptional channel admits at least one allowed successor channel.

These hypotheses are deliberately stronger than compactness. Their role is transparent: (R1)+(R2) make the reachable projective state set finite, while (R3) forces an infinite successor process whenever no exceptional termination occurs.

---

## 30. Uniform Finite Exact Channel Recurrence Theorem

### Theorem 30.1

Assume (R1)–(R3). Then every infinite nonexceptional successor path

\[
c_0\to c_1\to c_2\to\cdots
\]

contains an exact repeated projective channel state. More precisely, there exists an integer \(N_K<\infty\), depending only on \((\mathfrak P_K,d_{\rm proj},\delta_K)\), such that along every such path there exist

\[
0\le i<j\le N_K
\]

with

\[
[c_i]=[c_j].
\]

Consequently the first exact channel recurrence has length at most \(N_K\).

### Proof

Because \(\mathfrak P_K\) is compact, it is totally bounded. Choose

\[
\varepsilon=\frac{\delta_K}{3}.
\]

There exist points \(X_1,\dots,X_{N_K}\in\mathfrak P_K\) such that

\[
\mathfrak P_K
\subset
\bigcup_{\ell=1}^{N_K}
B_{\delta_K/3}(X_\ell).
\tag{30.1}
\]

Each ball in (30.1) contains at most one reachable projective state. Indeed, if reachable \(Y,Z\) lie in the same ball, then

\[
d_{\rm proj}(Y,Z)
\le d(Y,X_\ell)+d(X_\ell,Z)
<\frac{2\delta_K}{3}<\delta_K.
\]

By (R2), this forces \(Y=Z\).

Hence

\[
\boxed{
\#\mathfrak P_K^{\rm reach}\le N_K.
}
\tag{30.2}
\]

By (R3), an open nonexceptional channel can be continued recursively to obtain an infinite successor path. Consider the first \(N_K+1\) projective states

\[
[c_0],[c_1],\dots,[c_{N_K}].
\]

There are at most \(N_K\) distinct reachable states by (30.2), so the pigeonhole principle gives indices

\[
0\le i<j\le N_K
\]

such that

\[
[c_i]=[c_j].
\]

Because equality in \(\mathfrak P_K\) is equality of the full channel data needed for exact reuse, this is an exact recurrence, not merely an approximate return. Its length satisfies

\[
1\le j-i\le N_K.
\]

No mode count, shell count, Fourier cutoff, or preassigned completion depth enters \(N_K\). \(\square\)

---

## 31. Channel recurrence versus completed-incidence recurrence

Theorem 30.1 must not be overinterpreted.

A bilinear channel edge has the form

\[
e=(p,q\to r).
\]

Following one distinguished successor chain records only one line of descent. The intermediate edges may involve side parents not belonging to that chain. Therefore equality

\[
[c_i]=[c_j]
\]

alone does **not** imply that the sum of incidence boundaries of the intervening edges vanishes.

For a genuine multiplicative holonomy one needs an incidence-balanced finite object. Accordingly define a **completed frontier state** \(\mathfrak F\) to record all open channel ends of a finite companion-completion stage. A finite completion block \(\mathcal B\) from \(\mathfrak F_i\) to \(\mathfrak F_j\) is exactly closed when

\[
\boxed{\mathfrak F_i=\mathfrak F_j.}
\tag{31.1}
\]

In that case every open boundary channel at the beginning is matched by the corresponding channel at the end, and the signed sum of the internal interaction incidences has zero total boundary. Thus the closed block defines an integral incidence cycle and therefore supports gauge-invariant product holonomy.

This leads to the correct strengthened recurrence hypothesis.

### (R2-F) Exact completed-frontier discreteness

The set \(\mathfrak F_K\) of reachable completed frontier states is compact and \(\delta_K^{\rm F}\)-separated in a metric that detects exact equality of all open channel data.

### Corollary 31.1 — uniform completed recurrence

If the completion rule has no nonexceptional terminal frontier and (R2-F) holds, then every infinite companion-completion trajectory contains an exact closed completion block of length at most a constant \(N_K^{\rm F}<\infty\) depending only on the compact completed-frontier class.

### Proof

Apply the proof of Theorem 30.1 verbatim to the state space \(\mathfrak F_K\). Equality of two frontier states closes all open boundaries, so the intervening finite block is incidence-balanced. \(\square\)

This is the form of exact recurrence actually needed by the holonomy theorem.

---

## 32. Exact discreteness is genuinely necessary

Compactness without (R2) does not imply exact recurrence.

Let \(S^1\) carry its usual compact metric, let \(R_\alpha\) denote rotation by angle \(\alpha\), and assume

\[
\frac{\alpha}{2\pi}\notin\mathbb Q.
\]

For \(X_0\in S^1\), define

\[
X_n=R_\alpha^nX_0.
\]

Then the orbit lies in a compact space and is dense in \(S^1\), hence contains arbitrarily close pairs. Nevertheless

\[
X_n\neq X_m
\qquad(n\neq m).
\]

Therefore

\[
\boxed{
\text{compactness alone}
\not\Longrightarrow
\text{exact recurrence}.
}
\tag{32.1}
\]

The same obstruction applies a fortiori to projective channel dynamics. Exact discreteness, or some different arithmetic/algebraic mechanism with the same consequence, is substantive mathematical input.

---

## 33. Gauge-invariant holonomy on a closed completion block

Let \(\mathcal B\) be an exact completed-incidence recurrence block, so its internal edge multiset admits integers \(n_e\) satisfying

\[
\boxed{
\sum_e n_e\partial e=0,
\qquad
\partial e=[p_e]+[q_e]-[r_e].
}
\tag{33.1}
\]

Bridge 1 assigns each nonexceptional edge a nonzero scalar gain \(h_e\) with gauge transformation

\[
h_e\mapsto g_{p_e}g_{q_e}g_{r_e}^{-1}h_e.
\]

Define

\[
\boxed{
\operatorname{Hol}_{\mathcal B}
:=
\prod_e h_e^{n_e}.
}
\tag{33.2}
\]

By (33.1), all gauge factors cancel. Hence \(\operatorname{Hol}_{\mathcal B}\) is a well-defined gauge-invariant scalar attached to the exact completed recurrence block.

If actual nonzero channel amplitudes satisfy the exact multiplicative consistency law

\[
a_{r_e}=h_ea_{p_e}a_{q_e}
\]

on every edge of the block, then the same incidence cancellation gives

\[
\boxed{\operatorname{Hol}_{\mathcal B}=1.}
\tag{33.3}
\]

Thus recurrence supplies the finite object on which nonflatness must contradict exact candidate consistency.

---

## 34. Primitive completed rectangles and curvature

A primitive completed rectangle \(R\) is, by definition here, a four-channel completed block whose signed edge multiplicities form an incidence-balanced cycle. Write its four gains as

\[
h_{ii},\quad h_{ij},\quad h_{ji},\quad h_{jj},
\]

with the orientation chosen so that

\[
\boxed{
H_R
:=
\frac{h_{ii}h_{jj}}{h_{ij}h_{ji}}
}
\tag{34.1}
\]

is the holonomy of the rectangle cycle.

The incidence-balance requirement is essential: without it, the quotient in (34.1) need not be gauge invariant because the four output channel lines may carry independent gauge factors.

For an incidence-balanced completed rectangle, Bridge 1's gauge law implies that \(H_R\) is gauge invariant.

Define the logarithmic modulus curvature

\[
\boxed{
\Omega(R):=\log|H_R|.
}
\tag{34.2}
\]

The rank-one amplitudes have disappeared from \(H_R\); only the physical Formation-plus-radial edge gains remain.

---

## 35. Quantitative primitive-curvature hypotheses

To turn the qualitative frontier statement about positive reverse-pair curvature into a uniform theorem, one needs an explicit nonflatness hypothesis.

Let \(\mathfrak R_K\) be the set of primitive completed nonexceptional rectangle configurations reachable from \(K\). Assume:

### (C1) Strict primitive nonflatness with fixed orientation

\[
\boxed{
\Omega(R)>0
\qquad
\forall R\in\mathfrak R_K.
}
\tag{C1}
\]

Equivalently, after the chosen common orientation,

\[
|H_R|>1.
\]

### (C2) Compactness and continuity

The configuration space \(\mathfrak R_K\) is compact and

\[
R\mapsto\Omega(R)
\]

is continuous.

These assumptions are not supplied merely by Bridge 1. In particular, (C1) is the local geometric statement that must ultimately be derived from the explicit channel gain if the program is to become unconditional.

---

## 36. Uniform Primitive Curvature Gap Lemma

### Lemma 36.1

Under (C1)–(C2), there exists \(\omega_K>0\) such that

\[
\boxed{
\Omega(R)\ge\omega_K
\qquad
\forall R\in\mathfrak R_K.
}
\tag{36.1}
\]

Equivalently,

\[
\boxed{|H_R|\ge e^{\omega_K}>1.}
\tag{36.2}
\]

### Proof

By compactness of \(\mathfrak R_K\) and continuity of \(\Omega\), the minimum

\[
\omega_K
:=
\min_{R\in\mathfrak R_K}\Omega(R)
\]

is attained.

By (C1), every value of \(\Omega\) on \(\mathfrak R_K\) is strictly positive. If \(\omega_K=0\), attainment would produce \(R_*\in\mathfrak R_K\) with \(\Omega(R_*)=0\), contradicting (C1). Hence

\[
\omega_K>0.
\]

Exponentiating gives (36.2). \(\square\)

---

## 37. Orientation-free form

If the physical convention yields the opposite sign,

\[
\Omega(R)<0
\]

on every primitive rectangle, the same compactness argument gives

\[
\Omega(R)\le-\omega_K<0.
\]

A convention-independent statement is therefore

\[
\boxed{
|\Omega(R)|
=
\bigl|\log|H_R|\bigr|
\ge\omega_K.
}
\tag{37.1}
\]

For a single primitive rectangle this implies

\[
|H_R-1|
\ge
1-e^{-\omega_K}.
\tag{37.2}
\]

The passage from primitive rectangles to an arbitrary recurrent witness loop requires one more combinatorial/geometric statement: a same-sign rectangle decomposition with no cancellation of logarithmic curvature. That statement is the next subproblem of Bridge 2 and is **not** assumed proved here.

---

## 38. Status after the first layer of Bridge 2

The rigorous conclusions established in this part are:

\[
\boxed{
\begin{gathered}
\text{compactness + exact projective discreteness + nontermination}
\\
\Longrightarrow
\\
\text{uniform finite exact channel recurrence},
\end{gathered}
}
\]

and, at the stronger completed-frontier level,

\[
\boxed{
\text{uniform finite exact completed-incidence recurrence}.
}
\]

On every exact closed completion block, Bridge 1 supplies a gauge-invariant holonomy, and exact multiplicative candidate consistency forces that holonomy to equal \(1\).

Separately,

\[
\boxed{
\text{compact primitive rectangle class + strict primitive nonflatness}
\Longrightarrow
\text{uniform primitive curvature gap }\omega_K>0.
}
\]

What remains to complete Bridge 2 is now sharply divided into three local/global rigidity tasks:

1. derive exact projective or completed-frontier discreteness from the physical channel data, or replace it by another exact recurrence mechanism;
2. derive strict primitive nonflatness \(\Omega(R)\neq0\) with a fixed sign directly from the explicit Curl–Killing/radial channel gains;
3. prove that every exact recurrent witness admits an incidence-balanced primitive-rectangle decomposition whose logarithmic curvatures have the same orientation and therefore cannot cancel.

Only after these three points are established can one conclude a depth-independent lower bound

\[
|\operatorname{Hol}_\Gamma-1|\ge c_K>0
\]

for the completed recurrent witness and then invoke the already proved compactness argument to obtain the transverse saturation gap.

Thus the current exact frontier is

\[
\boxed{
\text{BRIDGE 1 CLOSED}
\quad\Longrightarrow\quad
\text{BRIDGE 2 REDUCED TO EXACT RECURRENCE + PRIMITIVE NONFLATNESS + SAME-SIGN DECOMPOSITION}.
}
\]

---

# PART V. BRIDGE 2 — MIDDLE LAYER: COMPLETION THEOREM AND MINIMALITY

> **Logical status.** This part packages the remaining Bridge-2 information in the cleanest theorem form. It does not promote the missing recurrence/nonflatness mechanisms to established facts. Instead it proves exactly what follows if a finite witness can be extracted, and it identifies the minimal hypothesis needed when the finite-network rigidity theorem from Part I.3 is taken as established.

The key distinction is now:

\[
\boxed{
\text{local channel calculus is proved (Bridge 1),}
}
\]

while

\[
\boxed{
\text{finite exact witness extraction is not yet proved.}
}
\]

---

## 39. Finite Witness Extraction and Uniform Primitive Nonflatness

Let

\[
\mathcal P_K
:=
\{v\in K:\exists\lambda>0\text{ with }T(v)=\lambda R_{\rm fv}(v)\}
\]

be the forbidden positive-alignment set.

We formulate two structural conditions.

### (FWE) Finite Witness Extraction

For every \(v\in\mathcal P_K\), there exists a finite exact reality-complete nonexceptional channel subnetwork

\[
\mathcal N_v
\]

consisting only of occupied, nonzero channel states, such that:

1. every channel edge and edge gain is the physical one furnished by Bridge 1;
2. the exact channel amplitude relations inherited from \(v\) hold on \(\mathcal N_v\);
3. all projective identifications used to close \(\mathcal N_v\) are exact;
4. \(\mathcal N_v\) is a legitimate finite saturation witness in the sense needed by the finite-network rigidity theorem of Part I.3.

This formulation deliberately avoids asserting that FWE follows from compactness. It is an exact extraction statement.

### (UPN) Uniform Primitive Nonflatness

There exists \(c_K>0\) such that every finite witness \(\mathcal N_v\) supplied by FWE contains at least one incidence-balanced primitive physical cycle \(R\) for which

\[
\boxed{
|\operatorname{Hol}_R-1|
\ge c_K.
}
\tag{39.1}
\]

The cycle \(R\) is required to use occupied nonzero channels, so that the exact scalar amplitude relations are available on every edge.

UPN is a direct primitive-witness formulation. It is stronger than merely asking for a qualitative nonzero curvature, but it has the advantage that it bypasses any need to decompose an arbitrary recurrent loop into many rectangles. A same-sign rectangle decomposition, if later proved, is one possible route to UPN rather than a logically necessary part of the final theorem.

---

## 40. Exact saturation consistency forces primitive holonomy one

### Lemma 40.1

Let \(R\) be any incidence-balanced finite channel cycle contained in an exact occupied channel witness. Suppose its nonzero channel amplitudes satisfy on each edge \(e=(p,q\to r)\)

\[
\boxed{
a_r=h_ea_pa_q.}
\tag{40.1}
\]

If \((n_e)\) are the signed edge multiplicities of the balanced cycle,

\[
\sum_e n_e([p_e]+[q_e]-[r_e])=0,
\tag{40.2}
\]

then

\[
\boxed{
\operatorname{Hol}_R
:=
\prod_eh_e^{n_e}
=1.
}
\tag{40.3}
\]

### Proof

Since all participating channel amplitudes are nonzero, (40.1) gives

\[
h_e=\frac{a_{r_e}}{a_{p_e}a_{q_e}}.
\]

Hence

\[
\operatorname{Hol}_R
=
\prod_e
\left(
\frac{a_{r_e}}{a_{p_e}a_{q_e}}
\right)^{n_e}.
\]

For every channel vertex \(x\), the total exponent of \(a_x\) in this product is the negative of the coefficient of \([x]\) in the incidence sum (40.2). That coefficient is zero. Thus every amplitude factor cancels exactly, leaving

\[
\operatorname{Hol}_R=1.
\]

The argument is gauge independent because the cycle is incidence-balanced. \(\square\)

This lemma is the precise projective consistency statement needed in the contradiction argument.

---

## 41. Theory-2 Completion Theorem under FWE and UPN

### Theorem 41.1

Assume Bridge 1, FWE, and UPN. Then

\[
\boxed{
T(v)\neq\lambda R_{\rm fv}(v)
\qquad
\forall v\in K,
\quad\forall\lambda>0.
}
\tag{41.1}
\]

### Proof

Assume for contradiction that there exist \(v\in K\) and \(\lambda>0\) such that

\[
T(v)=\lambda R_{\rm fv}(v).
\]

Then \(v\in\mathcal P_K\). By FWE, \(v\) admits a finite exact reality-complete nonexceptional witness \(\mathcal N_v\) inheriting the exact occupied-channel amplitude relations.

By UPN, \(\mathcal N_v\) contains an incidence-balanced primitive physical cycle \(R\) with

\[
|\operatorname{Hol}_R-1|
\ge c_K>0.
\tag{41.2}
\]

But Lemma 40.1 applies to this exact occupied cycle and yields

\[
\operatorname{Hol}_R=1.
\tag{41.3}
\]

Substituting (41.3) into (41.2) gives

\[
0\ge c_K>0,
\]

a contradiction.

Therefore no positive alignment can occur on \(K\), proving (41.1). \(\square\)

---

## 42. Immediate exclusion of the stationary finite-\(\kappa\) branch

For an actual stationary finite-\(\kappa\) profile, the established finite-viscosity decomposition gives

\[
\boxed{
T(v)=\kappa(v)R_{\rm fv}(v).
}
\tag{42.1}
\]

Since

\[
\kappa(v)\ge\kappa_0>0,
\]

(42.1) is a positive alignment with \(\lambda=\kappa(v)\). Theorem 41.1 therefore implies:

### Corollary 42.1

Under Bridge 1, FWE, and UPN, the normalized nonexceptional class contains no nonzero stationary finite-\(\kappa\) profile:

\[
\boxed{
K\cap
\{\text{nonzero stationary finite-}\kappa\text{ profiles}\}
=\varnothing.
}
\tag{42.2}
\]

If \(K\) itself was introduced as a compact class of putative stationary candidates, the conclusion is that this candidate class is empty.

\(\square\)

---

## 43. Uniform transverse norm gap without an angle theorem

The quantitative defect does not require a separate angular argument.

From the radial homogeneous theorem already proved,

\[
R_{\rm fv}(v)=0
\Longrightarrow
v=0.
\]

Since the normalized class satisfies \(E(v)=1\),

\[
\boxed{
R_{\rm fv}(v)\neq0
\qquad
\forall v\in K.
}
\tag{43.1}
\]

Define

\[
\Psi(v)
:=
\frac{
\|T(v)-\kappa(v)R_{\rm fv}(v)\|_{H^{-1/2}}
}{
\|T(v)\|_{H^{-1/2}}
+
\kappa(v)\|R_{\rm fv}(v)\|_{H^{-1/2}}
}.
\tag{43.2}
\]

The denominator is strictly positive by (43.1) and \(\kappa>0\). Theorem 41.1, applied with \(\lambda=\kappa(v)\), makes the numerator strictly positive.

Assume, as in the definition of the compact Theory-2 class, that \(T\), \(R_{\rm fv}\), and \(\kappa\) depend continuously on \(v\). Then \(\Psi\in C(K)\) and \(\Psi(v)>0\) for every \(v\in K\). Compactness gives

\[
\eta_K
:=
\min_{v\in K}\Psi(v)>0.
\]

Therefore:

### Theorem 43.1 — uniform transverse saturation gap

\[
\boxed{
\|T(v)-\kappa(v)R_{\rm fv}(v)\|_{H^{-1/2}}
\ge
\eta_K
\left(
\|T(v)\|_{H^{-1/2}}
+
\kappa(v)\|R_{\rm fv}(v)\|_{H^{-1/2}}
\right)
}
\tag{43.3}
\]

for every \(v\in K\), with \(\eta_K>0\) depending only on the compact class.

### Proof

Equation (43.3) is simply the definition of \(\Psi\) multiplied by its positive denominator and the lower bound \(\Psi\ge\eta_K\). \(\square\)

This is the strongest estimate needed to exclude stationary saturation, and it remains valid even if \(T(v)=0\) at some points.

---

## 44. Uniform angle gap under nonvanishing of \(T\)

Assume in addition

\[
T(v)\neq0
\qquad
\forall v\in K.
\tag{44.1}
\]

We regard \(H^{-1/2}\) as a real Hilbert space when defining angles; equivalently, for complex Fourier representatives use the real part of the Hermitian pairing.

Define

\[
q(v)
:=
\frac{
\operatorname{Re}\langle T(v),R_{\rm fv}(v)\rangle_{H^{-1/2}}
}{
\|T(v)\|_{H^{-1/2}}
\|R_{\rm fv}(v)\|_{H^{-1/2}}
}.
\tag{44.2}
\]

Then \(q\in C(K)\) and \(q(v)\le1\). Equality \(q(v)=1\) is exactly the equality case of Cauchy–Schwarz with the same orientation, hence

\[
T(v)=\lambda R_{\rm fv}(v)
\]

for some \(\lambda>0\), which is excluded by Theorem 41.1. Therefore \(q(v)<1\) everywhere.

Compactness gives

\[
q_*:=\max_{v\in K}q(v)<1.
\]

Set

\[
\boxed{
\theta_K:=\arccos q_*>0.
}
\tag{44.3}
\]

Then

\[
\boxed{
\angle(T(v),R_{\rm fv}(v))
\ge\theta_K
\qquad
\forall v\in K.
}
\tag{44.4}
\]

\(\square\)

---

## 45. Exact angle/gain inequality

Let

\[
A=\|T\|_{H^{-1/2}},
\qquad
B=\kappa\|R_{\rm fv}\|_{H^{-1/2}},
\qquad
\theta=\angle(T,R_{\rm fv}).
\]

Then

\[
\|T-\kappa R_{\rm fv}\|^2
=A^2+B^2-2AB\cos\theta.
\tag{45.1}
\]

Under (44.4), \(\theta\ge\theta_K\). Put

\[
c=\cos\theta_K,
\qquad
s=\sin\frac{\theta_K}{2},
\qquad
s^2=\frac{1-c}{2}.
\]

Since \(\cos\theta\le c\),

\[
\|T-\kappa R_{\rm fv}\|^2
\ge A^2+B^2-2ABc.
\]

A direct calculation gives

\[
A^2+B^2-2ABc-s^2(A+B)^2
=
\frac{1+c}{2}(A-B)^2
\ge0.
\]

Hence

\[
\boxed{
\|T-\kappa R_{\rm fv}\|_{H^{-1/2}}
\ge
\sin\left(\frac{\theta_K}{2}\right)
\left(
\|T\|_{H^{-1/2}}
+
\kappa\|R_{\rm fv}\|_{H^{-1/2}}
\right).
}
\tag{45.2}
\]

Thus in the angular formulation one may take

\[
\boxed{
\eta_K=\sin\left(\frac{\theta_K}{2}\right)>0.
}
\tag{45.3}
\]

\(\square\)

---

## 46. UPN is not needed if Part I.3 finite-network rigidity is already established

The preceding FWE+UPN theorem is useful when one wants holonomy itself to supply the finite-network contradiction. But the established frontier already contains the stronger finite-network statement:

\[
\boxed{
\text{for every genuinely finite completed nonexceptional network, }
T=\lambda R_{\rm fv},\ \lambda>0,
\text{ is impossible.}
}
\tag{46.1}
\]

If (46.1) is accepted as an independently proved theorem rather than as a target to be reproved by holonomy, then UPN is logically redundant for the final PDE exclusion.

### Theorem 46.1 — minimal Bridge-2 implication

Assume Bridge 1, FWE, and the finite-network rigidity theorem (46.1). Then

\[
\boxed{
T(v)\neq\lambda R_{\rm fv}(v)
\qquad
\forall v\in K,
\quad\forall\lambda>0.
}
\tag{46.2}
\]

Consequently the norm gap (43.3) follows, and under (44.1) the angle gap (44.4) and estimate (45.2) follow.

### Proof

If positive alignment held for some \(v\), FWE would produce a finite exact reality-complete nonexceptional saturation witness \(\mathcal N_v\) inheriting that alignment. This is forbidden by (46.1). Thus no positive alignment exists. The quantitative conclusions then follow from Sections 43–45. \(\square\)

Therefore, **if Part I.3 is genuinely established independently, the only missing Bridge-2 theorem needed for the final exclusion is FWE.**

---

## 47. Why FWE cannot be obtained from compactness alone

The exactness in FWE is essential. Compactness only supplies approximate returns.

The irrational-rotation construction of Section 32 already gives the basic obstruction: a compact continuous state space may carry an infinite orbit with no exact repeat. Thus an implication of the form

\[
\text{compact reachable class}
\Longrightarrow
\text{finite exact witness}
\]

is false without additional algebraic, arithmetic, or finite-rank structure.

In particular, neither ordinary compactness of \(K\) nor continuity of the channel gains can replace FWE.

One must prove FWE by a mechanism that forces a finite algebraic circuit, or else abandon finite recurrence and rule out an infinite nonexceptional saturation tree directly.

---

## 48. Why strict pointwise curvature does not by itself give UPN

Likewise, a qualitative statement

\[
\operatorname{Hol}_R\neq1
\]

for every nondegenerate primitive rectangle does not automatically yield a uniform \(c_K>0\).

Indeed, suppose there exists a sequence of admissible nonexceptional rectangles \(R_n\) approaching a degenerate or coalesced boundary configuration \(R_0\) for which

\[
H_{R_n}\to1.
\]

Then

\[
|H_{R_n}-1|\to0,
\]

so

\[
\inf_n|H_{R_n}-1|=0
\]

despite strict nonflatness at every finite \(n\).

Therefore a uniform primitive defect requires either:

- compactness of the **closed nonexceptional primitive configuration class** together with strict nonflatness on that compact set, as in (C1)–(C2); or
- an explicit quantitative lower bound that excludes coalescence/degeneration at the level of the holonomy formula.

This is the precise distinction between qualitative curvature and UPN.

---

## 49. Relation between the first and middle layers of Bridge 2

The first layer isolated exact recurrence, primitive curvature, and possible same-sign decomposition. The middle layer shows that there are two clean routes from that local structure to the final contradiction.

### Route H — holonomy route

Prove a finite witness extraction statement and then prove UPN, for example by:

\[
\boxed{
\text{FWE}
+
\text{primitive-cycle extraction}
+
\text{uniform primitive curvature}
\Longrightarrow
\text{UPN}.
}
\]

A same-sign decomposition of the entire recurrent block is one possible way to produce a nonflat witness, but it is not required if a single incidence-balanced primitive cycle with uniform defect can already be extracted.

Then Theorem 41.1 gives positive-alignment exclusion.

### Route F — finite-network route

If Part I.3 finite-network rigidity is already established, prove only

\[
\boxed{\text{FWE}.}
\]

Then Theorem 46.1 gives the same exclusion without using UPN.

Thus the holonomy program and the finite-network rigidity program should not be counted twice. One must decide whether holonomy is intended to **prove** finite-network rigidity or whether finite-network rigidity is already an input.

---

## 50. Two logically viable mechanisms for proving FWE

Since compactness-to-recurrence is false in continuous geometry, an unconditional proof of FWE must use additional structure. Two logically distinct routes remain.

### Route A — finite algebraic circuit without dynamical recurrence

Show directly that the exact saturation equation

\[
T=\lambda R_{\rm fv},
\qquad \lambda>0,
\]

forces a finite algebraic dependence among actual companion contributions. Such a theorem would extract a finite reality-complete witness without requiring any Fourier frequency or projective state to recur dynamically.

This route would bypass the irrational-rotation obstruction entirely.

### Route B — contradiction for the full infinite completion tree

Allow the exact nonexceptional completion tree to be genuinely infinite and prove that such an infinite saturated tree contradicts a global quantity. The needed functional must be stronger than the currently available shell recursion, since a recursion of the form

\[
a_{n+1}\lesssim_K\frac{a_n^2}{\kappa\rho_n}
\]

is compatible with super-exponentially small finite-energy tails.

A successful global functional would therefore have to detect something not already controlled by the existing energy or critical-moment estimates, for example a monotone signed flux, a coercive weighted channel sum, or an exact conservation/curvature quantity that cannot be supported by an infinite nonexceptional tree.

Neither Route A nor Route B has yet been proved by the current frontier. They are the genuinely new mathematical tasks.

---

## 51. Middle-layer status of Bridge 2

The exact logical picture is now:

\[
\boxed{
\begin{gathered}
\text{Bridge 1: exact projective channel connection}\\
\Downarrow\\
\text{FWE + UPN}\\
\Downarrow\\
T\neq\lambda R_{\rm fv}\quad(\lambda>0)\\
\Downarrow\\
\text{stationary finite-}\kappa\text{ exclusion}\\
\Downarrow\\
\text{uniform transverse norm gap}\\
\Downarrow\\
\text{uniform angle gap when }T\neq0.
\end{gathered}
}
\]

If Part I.3 finite-network rigidity is accepted as established independently, this simplifies to

\[
\boxed{
\begin{gathered}
\text{Bridge 1}\\
+\boxed{\text{FWE}}\\
+\text{Part I.3 finite-network rigidity}\\
\Downarrow\\
T\neq\lambda R_{\rm fv}\quad(\lambda>0)\\
\Downarrow\\
\|T-\kappa R_{\rm fv}\|_{H^{-1/2}}
\ge
\eta_K
\bigl(\|T\|_{H^{-1/2}}+\kappa\|R_{\rm fv}\|_{H^{-1/2}}\bigr).
\end{gathered}
}
\tag{51.1}
\]

Accordingly, in the minimal reading of the established Theory-2 frontier,

\[
\boxed{
\textbf{the remaining Bridge-2 bottleneck is Finite Witness Extraction.}
}
\tag{51.2}
\]

This statement is conditional on Part I.3 truly being an independent established theorem. If Part I.3 is instead intended to be proved by the holonomy mechanism, then both FWE and a nonflat finite witness theorem such as UPN remain necessary.

The next layer of Bridge 2 must therefore attack FWE itself, rather than attempting to deduce exact recurrence from compactness.

---

# PART VI. BRIDGE 2 — NEAR-FINAL LAYER: MEASURABLE RECTANGLES AND SEMIGROUP SEPARATION

> **Logical reset.** The preceding FWE formulation asks a continuum PDE equality to restrict exactly to a finite closed subsystem. That is stronger than what the Fourier convolution structure presently supplies. The purpose of this part is to replace the recurrence paradigm by a measure-theoretic finite-rectangle mechanism, while carefully separating what is proved from the one final separation identity that remains open.

The new mechanism has three stages:

\[
\boxed{
\text{positive-measure Fourier support}
\Longrightarrow
\text{positive-measure family of exact support rectangles}
\Longrightarrow
\text{strict semigroup rectangle multiplier curvature}.
}
\]

The last implication needed for the full Theory-2 contradiction is different:

\[
\boxed{
T=\lambda R_{\rm fv}
\Longrightarrow
\text{a finite bounded-reader flatness identity on one such rectangle}.
}
\]

That final implication is the **Finite Semigroup Separation of Saturation** problem.

---

## 52. Positive-measure helical support

Let \(v\in L^2(\mathbb R^3;\mathbb R^3)\) be divergence-free and normalized by \(E(v)=1\). Decompose

\[
\widehat v=\widehat v_++\widehat v_-
\]

using the measurable helical projectors \(Q_\pm(k)\). At least one helicity component, say \(\widehat v_\sigma\), has nonzero \(L^2\) norm.

### Lemma 52.1

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
\tag{52.1}
\]

has finite positive Lebesgue measure.

### Proof

Because \(\widehat v_\sigma\neq0\) in \(L^2\), its nonzero set has positive measure. Write that set, up to a null set, as the countable union

\[
\bigcup_{m,n,N\ge1}
\left\{
\frac1m<|k|<N,
\quad
|\widehat v_\sigma(k)|\ge\frac1n
\right\}.
\]

If every member of this union had measure zero, the nonzero set would have measure zero, contradiction. Hence one member has positive measure. It lies in a bounded annulus and therefore has finite measure. \(\square\)

The use of \(|\widehat v_\sigma(k)|\) is frame independent; no global helical phase choice is needed.

---

## 53. Same-output fibers on a positive-measure set

Define

\[
g(k)
:=(\mathbf1_S*\mathbf1_S)(k)
=
\int_{\mathbb R^3}
\mathbf1_S(p)\mathbf1_S(k-p)\,dp.
\tag{53.1}
\]

Since \(S\) has finite positive measure,

\[
g\ge0,
\qquad
\int_{\mathbb R^3}g(k)\,dk
=|S|^2>0.
\tag{53.2}
\]

Consequently the set

\[
K_S:=\{k:g(k)>0\}
\]

has positive measure. For every \(k_0\in K_S\), define the same-output fiber

\[
S_{k_0}
:=
\{p\in S:k_0-p\in S\}.
\tag{53.3}
\]

Then

\[
\boxed{|S_{k_0}|=g(k_0)>0.}
\tag{53.4}
\]

Thus a nonzero finite-energy state does not merely supply one isolated same-output incidence: on a positive-measure set of outputs it supplies positive-measure families of input pairs.

---

## 54. Exact support-geometric companion rectangles

Fix \(k_0\in K_S\). Since \(S_{k_0}\) has positive measure, the product set

\[
S_{k_0}\times S_{k_0}
\]

has positive six-dimensional measure, whereas the diagonal \(\{p=p'\}\) has measure zero. Hence one may choose

\[
p,p'\in S_{k_0},
\qquad
p\neq p'.
\]

Set

\[
q=k_0-p,
\qquad
q'=k_0-p',
\qquad
d=p-p'\neq0.
\]

Then all four input points lie in \(S\), and

\[
\boxed{
\begin{array}{ccc}
(p,q)&\longrightarrow&k_0,\\
(p',q')&\longrightarrow&k_0,\\
(p,q')&\longrightarrow&k_0+d,\\
(p',q)&\longrightarrow&k_0-d.
\end{array}
}
\tag{54.1}
\]

This is an exact algebraic companion rectangle in Fourier support.

### Important measure-theoretic qualification

For an \(L^2\) Fourier state, individual point values are defined only after choosing an a.e. representative, and a single frequency point has zero measure in the convolution integral. Therefore (54.1) is **not yet a finite physical subsystem of the nonlinear convolution**. Its rigorous content is support geometry: almost every chosen tuple consists of Lebesgue points of a representative and obeys the exact frequency identities above.

This corrects the stronger but unjustified interpretation that four isolated Fourier points by themselves contribute a nonzero finite summand to \(N(v)\).

We call (54.1) a **support-geometric physical rectangle**.

---

## 55. Nonexceptional selection

Some geometric degeneracies can be removed by null-set arguments. For example, on a fixed same-helicity fiber \(q=k_0-p\), same-root degeneracy

\[
|p|=|q|
\]

is equivalent to

\[
2k_0\cdot p=|k_0|^2,
\]

an affine plane and hence a three-dimensional null set. Collinearity conditions are likewise lower-dimensional.

For the helical polarization factor, on each local helical chart the projected coefficient

\[
Q_\tau(p+q)
\bigl(e_{\sigma_q}(q)\times e_{\sigma_p}(p)\bigr)
\]

is smooth, and in the analytic regions of the standard helical frame its scalar representative is real-analytic. If that branch is not identically Formation-null, its zero set is null on the corresponding connected chart.

The high-high-low/thin-shell exclusions are not automatically null-set statements. Accordingly the precise nonexceptional extraction assumption needed here is:

### (NE-S) Active support nonexceptionality

There exists a positive-measure set of outputs \(K_S^{\rm act}\subset K_S\) such that, for each \(k_0\in K_S^{\rm act}\), the set of pairs \((p,p')\in S_{k_0}^2\) for which all four incidences in (54.1) lie in the uniformly nonexceptional region has positive measure.

If the phrase “uniformly separated from the exceptional configurations” in the definition of \(K\) is intended in this measure-theoretic support sense, then (NE-S) is exactly that hypothesis specialized to the extracted rectangle family.

### Theorem 55.1 — finite support rectangle extraction

Under Lemma 52.1 and (NE-S), every nonzero normalized state in the active nonexceptional class contains an exact support-geometric rank-one companion rectangle of the form (54.1), and in fact a positive-measure family of such rectangles.

No recurrence, Fourier cutoff, mode-count bound, or projective discreteness is used.

\(\square\)

This is the rigorous form of **Finite Physical Rectangle Extraction (FPRE)** available at the \(L^2\)-support level.

---

## 56. Rank-one identity on almost-everywhere rectangle data

Choose a local measurable helical frame on a chart containing the selected points and write

\[
\widehat v_\sigma(k)=a_\sigma(k)e_\sigma(k)
\]

for an a.e. scalar coefficient \(a_\sigma\). At Lebesgue points of this representative define

\[
A_1=a_\sigma(p),
\quad A_2=a_\sigma(p'),
\quad B_1=a_\sigma(q),
\quad B_2=a_\sigma(q').
\]

Because the four points lie in \(S\), these coefficients are nonzero a.e. on the selected active family. Put

\[
Z_{ij}=A_iB_j.
\]

Then purely algebraically

\[
\boxed{
Z_{11}Z_{22}=Z_{12}Z_{21}.
}
\tag{56.1}
\]

This identity is exact for the almost-everywhere fiber data. Again, it should not be confused with a decomposition of the full convolution integral into four atomic terms.

---

## 57. Reality completion remains finite at the geometric level

If \(v\) is real,

\[
\widehat v(-k)=\overline{\widehat v(k)}.
\]

Therefore every support-geometric rectangle (54.1) has the conjugate rectangle

\[
(-p,-q)\to-k_0,
\quad
(-p',-q')\to-k_0,
\]

\[
(-p,-q')\to-(k_0+d),
\quad
(-p',-q)\to-(k_0-d).
\]

Thus geometric reality completion requires only finitely many companion incidences. This is an exact support statement, not an assertion of finite closure of the full nonlinear integral.

---

## 58. Exact mixed heat–Poisson rectangle multiplier curvature

For \(y\ge0\) and \(\tau>0\), define the positive radial semigroup multiplier

\[
m_{y,\tau}(k)
:=
\exp(-y|k|-\tau|k|^2).
\tag{58.1}
\]

For the rectangle (54.1), define

\[
\mathfrak M_{y,\tau}(k_0,d)
:=
\frac{m_{y,\tau}(k_0)^2}
{m_{y,\tau}(k_0+d)m_{y,\tau}(k_0-d)}.
\tag{58.2}
\]

### Theorem 58.1 — strict semigroup rectangle curvature

For every \(y\ge0\), \(\tau>0\), and \(d\neq0\),

\[
\boxed{
\log\mathfrak M_{y,\tau}(k_0,d)
=
y\bigl(|k_0+d|+|k_0-d|-2|k_0|\bigr)
+2\tau|d|^2>0.
}
\tag{58.3}
\]

Consequently

\[
\boxed{
\mathfrak M_{y,\tau}(k_0,d)>1.
}
\tag{58.4}
\]

### Proof

The Poisson contribution is

\[
y\bigl(|k_0+d|+|k_0-d|-2|k_0|\bigr),
\]

which is nonnegative by convexity of the Euclidean norm. For the heat contribution, the parallelogram identity gives

\[
|k_0+d|^2+|k_0-d|^2
=2|k_0|^2+2|d|^2,
\]

hence the logarithmic heat ratio equals \(2\tau|d|^2\), strictly positive because \(\tau>0\) and \(d\neq0\). Summing proves (58.3). \(\square\)

The heat factor is what guarantees strictness even in the collinear case where the Poisson contribution may vanish.

---

## 59. Semigroup weighting breaks the rank-one rectangle exactly

Weight the four a.e. rank-one coefficients by their output multipliers:

\[
\widetilde Z_{ij}
:=
m_{y,\tau}(k_{ij})Z_{ij},
\]

where

\[
k_{11}=k_{22}=k_0,
\qquad
k_{12}=k_0+d,
\qquad
k_{21}=k_0-d.
\]

Then (56.1) gives

\[
\boxed{
\frac{\widetilde Z_{11}\widetilde Z_{22}}
{\widetilde Z_{12}\widetilde Z_{21}}
=
\mathfrak M_{y,\tau}(k_0,d)>1.
}
\tag{59.1}
\]

This is an exact **semigroup multiplier rectangle defect**.

### Distinction from projective channel holonomy

The quantity \(\mathfrak M_{y,\tau}\) is not, by itself, the projective channel holonomy

\[
H_R=\frac{h_{11}h_{22}}{h_{12}h_{21}}.
\]

The gains \(h_{ij}\) also contain Curl–Killing root factors, helical/Leray polarization coefficients, and finite-viscosity radial transfer. Therefore (59.1) proves a strict semigroup curvature mechanism, but it does **not** prove UPN or a holonomy contradiction without an additional identity coupling the saturation equation to these weighted rectangle data.

This distinction is essential.

---

## 60. Why the old FWE does not follow from rectangle extraction

Suppose globally

\[
T=\lambda R_{\rm fv}.
\tag{60.1}
\]

Both sides are full Hilbert-space objects assembled from continuum Fourier data. Even if the nonlinear side is unfolded into labeled contributions, a physical output packet generally has an additive representation

\[
a_r^{\rm phys}
=\sum_{\alpha\to r}a_{r,\alpha}
\]

or, in the continuum representation, an integral over input fibers. Equality (60.1) does not imply that any selected finite subset of those contributions satisfies the same equality by itself.

The elementary scalar model

\[
1=\sum_{n=1}^\infty 2^{-n}
\]

already shows the logical issue: the exact infinite relation need not be inherited by a finite subcollection.

Thus

\[
\boxed{
\text{global saturation equality}
\not\Longrightarrow
\text{exact finite subsystem saturation}
}
\tag{60.2}
\]

from linearity and bilinearity alone.

This is a separate obstruction from the failure of compactness to imply recurrence. Even though support rectangles exist immediately, the old FWE requirement remains too strong without another algebraic theorem.

---

## 61. Point evaluation cannot serve as the final reader

There is a second functional-analytic reason not to stop at the four pointwise coefficients in Section 56. Point evaluation at a prescribed Fourier frequency is not a bounded functional on \(L^2(\mathbb R^3)\), nor on the natural critical Hilbert spaces without additional regularity.

Therefore the final contradiction must be formulated using bounded linear readers: localized integrals, semigroup pairings, or other continuous functionals on the state space. The support-geometric rectangle and the strict multiplier formula provide the geometry that such readers should detect, but do not themselves constitute a bounded finite certificate.

---

## 62. Canonical heat commutator identity on the stationary branch

The canonical heat depth remains useful because it simplifies the stationary linear side exactly.

Let

\[
H_\tau=e^{-\tau\Lambda^2}.
\]

In Fourier radial variables,

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
\tag{62.1}
\]

or equivalently

\[
H_\tau L
=L H_\tau-2\tau\Lambda^2H_\tau.
\tag{62.2}
\]

Recall

\[
Y=\Lambda^2-D_2+2D_2L.
\]

Using (62.2),

\[
\begin{aligned}
H_\tau Y
&=
\Lambda^2H_\tau-D_2H_\tau+2D_2H_\tau L\\
&=
(1-4D_2\tau)\Lambda^2H_\tau
-D_2H_\tau+2D_2L H_\tau.
\end{aligned}
\tag{62.3}
\]

At the canonical depth

\[
\tau_*=\frac1{4D_2},
\]

the quadratic spectral term disappears:

\[
\boxed{
H_{\tau_*}Y
=D_2(2L-1)H_{\tau_*}.
}
\tag{62.4}
\]

Hence on a stationary profile \(N(v)=\kappa Yv\),

\[
\boxed{
H_{\tau_*}N(v)
=
\kappa D_2(2L-1)H_{\tau_*}v.
}
\tag{62.5}
\]

If \(w=H_{\tau_*}v\), the heat covariance becomes

\[
\boxed{
\mathcal C_{\tau_*}(v)
=
\kappa D_2(2L-1)w-N(w).
}
\tag{62.6}
\]

There is no identity in the present frontier forcing the right-hand side to vanish. Thus strict semigroup curvature does not automatically contradict stationarity merely by applying \(H_{\tau_*}\).

---

## 63. Finite Saturation Certificate: the correct finite target

The preceding analysis suggests replacing old FWE by a weaker and more natural finite-certificate theorem.

### Finite Saturation Certificate (FSC)

For every forbidden saturation candidate

\[
T(v)=\lambda R_{\rm fv}(v),
\qquad \lambda>0,
\]

one seeks finitely many bounded linear readers

\[
\ell_1,\dots,\ell_m
\]

and a finite active support-geometric companion rectangle \(R\) such that:

1. the reader data retain an exact finite rank-one compatibility associated with \(R\);
2. the saturation equality forces those finite data to satisfy a flat scalar relation
   \[
   \mathscr D(v)=0;
   \]
3. the strict semigroup rectangle multiplier curvature of Section 58 forces
   \[
   \mathscr D(v)\neq0.
   \]

FSC is a finite **certificate of incompatibility**, not a finite invariant subsystem of the PDE.

This formulation is compatible with continuum Fourier convolution because bounded readers may integrate the full continuum while returning only finitely many scalar outputs.

---

## 64. Finite-reader noninjectivity is not an obstruction to FSC

Earlier we proved that no fixed finite collection of Poisson/heat depths is injective on the full infinite-dimensional radial packet space. That theorem remains valid.

FSC does not ask for injectivity. To contradict

\[
T=\lambda R_{\rm fv},
\]

one only needs a finite functional \(\mathscr D\) that separates the forbidden equality from the actual geometric data. A finite family of readers may fail to reconstruct the state while still detecting one specific incompatibility.

Thus

\[
\boxed{
\text{finite reconstruction is unnecessary; finite separation is sufficient.}
}
\tag{64.1}
\]

This is precisely why the finite-reader program remains viable despite the no-injectivity theorem of Section 6.

---

## 65. Finite Semigroup Separation of Saturation (FSSS)

The final missing theorem can now be stated without recurrence or finite-support assumptions.

### Conjectural Theorem 65.1 — FSSS

There exist finitely many positive Poisson depths

\[
y_0,\dots,y_m
\]

and finitely many heat depths

\[
\tau_0,\dots,\tau_n,
\]

with the canonical depth \(\tau_*=1/(4D_2)\) included after normalization, together with finitely many bounded angular/radial test functionals, such that the following holds uniformly on the compact nonexceptional class \(K\):

if

\[
T(v)=\lambda R_{\rm fv}(v),
\qquad \lambda>0,
\]

then the resulting finite reader data satisfy a flat compatibility identity

\[
\boxed{\mathscr D(v)=0.}
\tag{65.1}
\]

On the other hand, whenever the active support of \(v\) contains the nonexceptional rectangle furnished by Theorem 55.1, the same finite reader determinant satisfies

\[
\boxed{\mathscr D(v)\neq0,}
\tag{65.2}
\]

with the nonzero sign ultimately controlled by the strict multiplier curvature

\[
\mathfrak M_{y,\tau}(k_0,d)>1.
\]

If Theorem 65.1 is proved, then positive alignment is impossible and the compactness argument of Sections 43–45 immediately supplies the uniform transverse gap and, under nonvanishing of \(T\), the uniform angle gap.

### Status

Theorem 65.1 is **not proved** by the present frontier. In particular, Sections 52–59 do not yet construct the bounded determinant \(\mathscr D\), and (62.6) shows that naive vanishing of heat covariance cannot be used as the missing flatness identity.

---

## 66. What has genuinely been gained

The near-final layer removes several artificial requirements from the earlier Bridge-2 route.

The proved support/semigroup geometry does not require:

- completion-tree recurrence;
- exact projective discreteness;
- a minimum Fourier mode spacing;
- finite Fourier support;
- a Fourier cutoff;
- continuum Poisson inversion.

The new proved chain is

\[
\boxed{
\begin{gathered}
v\neq0,\quad v\in L^2\\
\Downarrow\\
\text{positive-measure helical support}\\
\Downarrow\\
\text{positive-measure same-output fibers}\\
\Downarrow\\
\text{exact support-geometric companion rectangles}\\
\Downarrow\\
\text{strict mixed heat--Poisson multiplier curvature}.
\end{gathered}
}
\tag{66.1}
\]

Under (NE-S), the rectangles can be selected entirely in the nonexceptional active region.

What has **not** been gained is an exact finite restriction of the saturation equation.

---

## 67. Updated Bridge-2 frontier

The old logical target

\[
\text{compactness}
\Longrightarrow
\text{recurrence}
\Longrightarrow
\text{finite saturation network}
\]

is no longer the preferred route, because neither implication is available in the continuum setting without new assumptions.

The refined target is

\[
\boxed{
\begin{gathered}
\text{Bridge 1 exact channel calculus}\\
+\\
\text{support-geometric rectangle extraction}\\
+\\
\text{strict semigroup multiplier curvature}\\
+\\
\boxed{\text{FSSS}}\\
\Downarrow\\
T\neq\lambda R_{\rm fv}\quad(\lambda>0)\\
\Downarrow\\
\|T-\kappa R_{\rm fv}\|_{H^{-1/2}}
\ge
\eta_K
\bigl(\|T\|_{H^{-1/2}}+
\kappa\|R_{\rm fv}\|_{H^{-1/2}}\bigr).
\end{gathered}
}
\tag{67.1}
\]

Thus the mathematically sharp near-final problem is no longer “prove recurrence.” It is:

\[
\boxed{
\textbf{construct a finite bounded-reader determinant }\mathscr D
\textbf{ for which saturation forces flatness and semigroup rectangle curvature forces nonflatness.}
}
\tag{67.2}
\]

That is the remaining candidate bridge to an unconditional Theory-2 theorem.

---

# PART VII. RETROFIT PART I.5 — GLOBAL PAIRED CONDUCTANCE (GCC)

> **Logical status.** This part installs the strongest rigorous form of the proposed Part I.5. The positive conductance representation (GCC-2), strict kernel positivity (GCC-3), and strict positivity on the active nonexceptional class (GCC-4) are proved below, subject to the explicit regularity and active-support hypotheses stated here. The stationary vanishing statement (GCC-1) requires one additional global identity, called the **Global Ward–Conductance Identity (GWCI)**. GWCI is isolated as the sole new identity in this layer and is not asserted to follow from the preceding local rectangle theory.

This part should be read as a retrofit: logically it belongs near the semigroup covariance material, but it is appended here to preserve the audit trail of the proof program.

---

## 68. Helical channel symbol and same-output coordinates

Choose local unit helical frames \(e_\sigma(k)\) and write

\[
\widehat v(k)=\sum_{\sigma=\pm} f_\sigma(k)e_\sigma(k),
\qquad
ik\times e_\sigma(k)=\sigma|k|e_\sigma(k).
\tag{68.1}
\]

For a same-helicity input pair \((p,q)\) with \(p+q=k\), define the vector-valued polarized Curl–Killing symbol

\[
\boxed{
\mathfrak b_\sigma^\tau(p,q)
:=
\frac{\sigma(|p|-|q|)}{2}
Q_\tau(k)
\bigl(e_\sigma(q)\times e_\sigma(p)\bigr)
\in E_\tau(k).
}
\tag{68.2}
\]

The corresponding channel amplitude is

\[
\boxed{
\mathcal F_\sigma^\tau[v](p,q)
:=
f_\sigma(p)f_\sigma(q)\,
\mathfrak b_\sigma^\tau(p,q).
}
\tag{68.3}
\]

Only norms of these channel amplitudes will enter the conductance density, so the definition is independent of the local phase choice of the helical frame.

The same-helicity sector is sufficient for the positivity mechanism whenever one active helicity sheet carries positive mass. A mixed-helicity version is obtained by adding the finite sum over the two input signs and does not alter the structural arguments below.

Now parameterize two same-output incidences by

\[
p+q=k,
\qquad
p'+q'=k,
\tag{68.4}
\]

and set

\[
d:=p-p'.
\tag{68.5}
\]

Then

\[
q'=q+d,
\]

and the two partner-swapped outputs are

\[
\boxed{
k_+=p+q'=k+d,\qquad k_-=p'+q=k-d.}
\tag{68.6}
\]

This is exactly the companion rectangle geometry of Sections 54–59.

---

## 69. Mixed heat–Poisson conductance kernel

Fix

\[
\tau>0,
\qquad y\ge0,
\]

and set

\[
m_{\tau,y}(k)
:=e^{-\tau|k|^2-y|k|}.
\tag{69.1}
\]

Define

\[
\Delta_H(k,d)
:=|k+d|^2+|k-d|^2-2|k|^2,
\tag{69.2}
\]

and

\[
\Delta_P(k,d)
:=|k+d|+|k-d|-2|k|.
\tag{69.3}
\]

The parallelogram identity gives

\[
\boxed{\Delta_H(k,d)=2|d|^2,}
\tag{69.4}
\]

whereas convexity of the Euclidean norm gives

\[
\boxed{\Delta_P(k,d)\ge0.}
\tag{69.5}
\]

Set

\[
\Xi_{\tau,y}(k,d)
:=\tau\Delta_H(k,d)+y\Delta_P(k,d).
\tag{69.6}
\]

Then

\[
\frac{m_{\tau,y}(k+d)m_{\tau,y}(k-d)}{m_{\tau,y}(k)^2}
=e^{-\Xi_{\tau,y}(k,d)}.
\tag{69.7}
\]

### Definition 69.1 — paired conductance kernel

Define

\[
\boxed{
\Gamma_{\tau,y}(k,d)
:=1-e^{-\Xi_{\tau,y}(k,d)}.
}
\tag{69.8}
\]

### Lemma 69.2 — strict reverse-pair conductance

For all \(k,d\in\mathbb R^3\),

\[
0\le \Gamma_{\tau,y}(k,d)<1,
\]

and

\[
\boxed{
d\neq0\quad\Longrightarrow\quad
\Gamma_{\tau,y}(k,d)>0.}
\tag{69.9}
\]

### Proof

By (69.4)–(69.6),

\[
\Xi_{\tau,y}(k,d)
=2\tau|d|^2+y\Delta_P(k,d)
\ge0.
\]

If \(d\neq0\), then \(2\tau|d|^2>0\), so \(\Xi_{\tau,y}>0\). The claims follow immediately from \(\Gamma=1-e^{-\Xi}\). \(\square\)

This is the exact global kernel counterpart of the strict rectangle multiplier curvature in Theorem 58.1.

---

## 70. Companion rectangle mass density

For \((k,p,p')\in\mathbb R^9\), set

\[
q:=k-p,
\qquad
q':=k-p'.
\tag{70.1}
\]

Define the nonnegative companion density

\[
\boxed{
\mathcal M_v(k,p,p')
:=
\sum_{\sigma=\pm}
\sum_{\tau_+,\tau_-=\pm}
\bigl|\mathcal F_\sigma^{\tau_+}[v](p,q')\bigr|^2
\bigl|\mathcal F_\sigma^{\tau_-}[v](p',q)\bigr|^2.
}
\tag{70.2}
\]

This density contains all four Fourier amplitude factors \(f_\sigma(p),f_\sigma(p'),f_\sigma(q),f_\sigma(q')\). It is phase-insensitive and nonnegative. The degree-eight homogeneity in the Fourier amplitude is intentional: the role of \(\mathcal M_v\) is not to reproduce \(N(v)\) itself, but to provide a positive companion-pair mass that cannot be destroyed by phase cancellation.

Because \(L^2\) alone does not guarantee integrability of the degree-eight weighted density, we state the regularity input explicitly.

### (G-Reg) Global conductance regularity

For the selected \((\tau,y)\), assume

\[
\boxed{
\mathfrak C_{\tau,y}(v)<\infty
}
\tag{G-Reg}
\]

for every \(v\in K\), where \(\mathfrak C_{\tau,y}\) is defined below, and assume that

\[
v\longmapsto \mathfrak C_{\tau,y}(v)
\]

is continuous in the graph topology of \(K\).

This is a genuine regularity assumption and should not be hidden inside the bare \(L^2\) normalization.

---

## 71. Global paired-conductance functional

Define

\[
\boxed{
\mathfrak C_{\tau,y}(v)
:=
\iiint_{\mathbb R^9}
\Gamma_{\tau,y}(k,p-p')
\mathcal M_v(k,p,p')
\,dk\,dp\,dp'.
}
\tag{71.1}
\]

Under (G-Reg), this is a finite nonnegative real number.

### GCC-2 — positive Fourier representation

Equation (71.1) is exactly a positive Fourier representation of the form

\[
\boxed{
\mathfrak C(v)
=
\int_\Omega
\Gamma(\zeta)
|\mathcal A_v(\zeta)|^2\,d\mu(\zeta),
}
\tag{71.2}
\]

where the finitely many helicity-output pairs are regarded as the components of the vector \(\mathcal A_v\).

Thus GCC-2 holds by construction.

\[
\boxed{\mathrm{QED}_{\mathrm{GCC2}}}
\]

---

## 72. GCC-3 — strict positivity of the conductance kernel

By Lemma 69.2,

\[
\Gamma_{\tau,y}(k,p-p')>0
\]

whenever \(p\neq p'\). The diagonal

\[
\{(k,p,p'):p=p'\}
\]

has Lebesgue measure zero in \(\mathbb R^9\). Therefore

\[
\boxed{
\Gamma_{\tau,y}>0
\quad\text{a.e. on genuine companion pairs.}
}
\tag{72.1}
\]

No uniform pointwise lower bound

\[
\Gamma_{\tau,y}\ge c>0
\]

is claimed or needed; such a bound would fail as \(p'\to p\).

Hence GCC-3 is proved in the sharp form relevant to the integral functional.

\[
\boxed{\mathrm{QED}_{\mathrm{GCC3}}}
\]

---

## 73. Active nonexceptionality at the triple level

To prove strict positivity of the full integral, it is not enough merely to say that the state is “not identically Formation-null.” What is needed is positive companion mass on a positive-measure subset of the triple space. The support hypothesis (NE-S) from Section 55 supplies precisely this after restriction to the active helical sheet.

For clarity we record the equivalent conductance-level formulation.

### (G-NE) Active triple nonexceptionality

For every \(v\in K\), there exist a helicity sign \(\sigma\) and a measurable set

\[
\Omega_v^\sharp\subset\mathbb R^9,
\qquad
|\Omega_v^\sharp|>0,
\]

such that for every \((k,p,p')\in\Omega_v^\sharp\):

1. \(p\neq p'\);
2. the four Fourier inputs \(p,p',k-p,k-p'\) lie in an active positive-amplitude region of \(v\);
3. for at least one pair \((\tau_+,\tau_-)\),
   \[
   \mathcal F_\sigma^{\tau_+}[v](p,k-p')\neq0,
   \qquad
   \mathcal F_\sigma^{\tau_-}[v](p',k-p)\neq0.
   \]

The measure-theoretic rectangle theorem plus (NE-S) imply (G-NE). Conversely, (G-NE) is exactly the hypothesis needed by the integral positivity proof and avoids overclaiming from pointwise genericity.

---

## 74. GCC-4 — strict global companion conductance

### Theorem 74.1

Assume \(E(v)=1\), (G-Reg), and (G-NE). Then

\[
\boxed{
\mathfrak C_{\tau,y}(v)>0.
}
\tag{74.1}
\]

### Proof

By (G-NE), there is a positive-measure set \(\Omega_v^\sharp\) on which at least one term in the finite sum (70.2) is strictly positive. Hence

\[
\mathcal M_v(k,p,p')>0
\qquad\text{on }\Omega_v^\sharp.
\]

Also \(p\neq p'\) there, so Lemma 69.2 gives

\[
\Gamma_{\tau,y}(k,p-p')>0
\qquad\text{on }\Omega_v^\sharp.
\]

Thus the nonnegative integrand in (71.1) is strictly positive on a set of positive measure. Since the integral is finite by (G-Reg), it follows that

\[
\mathfrak C_{\tau,y}(v)>0.
\]

\(\square\)

Therefore

\[
\boxed{\mathrm{QED}_{\mathrm{GCC4}}}
\]

under the explicit active-support and regularity hypotheses.

---

## 75. Compactness upgrades integrated positivity to a uniform gap

Assume now that \(K\) is compact, (G-Reg) holds continuously on \(K\), and every \(v\in K\) satisfies (G-NE). By Theorem 74.1,

\[
\mathfrak C_{\tau,y}(v)>0
\qquad\forall v\in K.
\]

Since \(v\mapsto\mathfrak C_{\tau,y}(v)\) is continuous and \(K\) is compact,

\[
\boxed{
c_K^{\rm GCC}
:=
\min_{v\in K}\mathfrak C_{\tau,y}(v)>0.
}
\tag{75.1}
\]

This is the correct way to obtain a uniform conductance gap. No pointwise lower bound on \(|p-p'|\) or on \(\Gamma_{\tau,y}\) is required. In particular, the possible degeneration \(p'\to p\) is handled only after integration and compactness.

---

## 76. GCC-1 and the exact missing global identity

The stationary equation is

\[
N(v)=\kappa Y_v.
\]

Define its full defect

\[
\boxed{
D_\kappa(v)
:=N(v)-\kappa Y_v.
}
\tag{76.1}
\]

Stationarity is exactly

\[
D_\kappa(v)=0.
\tag{76.2}
\]

The local rectangle and semigroup-curvature results do not imply that \(\mathfrak C_{\tau,y}\) vanishes when (76.2) holds, because the physical nonlinear output is an additive continuum integral and phase/cross-channel cancellations occur before one reaches a positive channel-pair square.

Thus GCC-1 requires one genuinely global identity.

### Required Supplementary Theorem 76.1 — Global Ward–Conductance Identity (GWCI)

There exist fixed finite parameters

\[
\tau>0,
\qquad
y\ge0,
\]

and a continuous real-valued functional

\[
\mathfrak W_{\tau,y}(v;D),
\]

real-linear in its second variable \(D\in H^{-1/2}\), constructed from finitely many admissible semigroup operations, helical/Leray projections, and finite polarized companion symmetrizations, such that for every sufficiently regular normalized state in the class,

\[
\boxed{
\mathfrak W_{\tau,y}
\bigl(v;N(v)-\kappa Y_v\bigr)
=
\mathfrak C_{\tau,y}(v).
}
\tag{76.3}
\]

Equation (76.3) is the **Global Ward–Conductance Identity**.

### Status of GWCI

GWCI is not proved by the current frontier. In particular:

- local semigroup rectangle curvature does not imply (76.3);
- the canonical heat commutator identity (62.6) does not imply (76.3);
- additive channel aggregation prevents one from replacing the required global symmetrization by a formal four-point argument.

A proof of GWCI must exhibit \(\mathfrak W_{\tau,y}\) explicitly and verify, at the Fourier-symbol level, that all cross terms reorganize exactly into the positive density \(\Gamma_{\tau,y}\mathcal M_v\). Merely asserting that such a reorganization occurs would be circular.

---

## 77. GCC-1 follows immediately from GWCI

### Proposition 77.1

Assume GWCI. If \(v\) is a stationary finite-\(\kappa\) state, then

\[
\boxed{
\mathfrak C_{\tau,y}(v)=0.
}
\tag{77.1}
\]

### Proof

Stationarity gives \(D_\kappa(v)=0\). Since \(\mathfrak W_{\tau,y}(v;\cdot)\) is real-linear,

\[
\mathfrak W_{\tau,y}(v;0)=0.
\]

Applying (76.3),

\[
\mathfrak C_{\tau,y}(v)
=
\mathfrak W_{\tau,y}(v;D_\kappa(v))
=0.
\]

\(\square\)

Thus

\[
\boxed{\mathrm{QED}_{\mathrm{GCC1}}\quad\text{conditional on GWCI}.}
\]

---

## 78. Conditional stationary exclusion

### Theorem 78.1 — no nonexceptional stationary state under GWCI

Assume GWCI, (G-Reg), and (G-NE). Then no normalized nonzero stationary finite-\(\kappa\) state belongs to the active class.

### Proof

If \(v\) were stationary, Proposition 77.1 would give

\[
\mathfrak C_{\tau,y}(v)=0.
\]

But Theorem 74.1 gives

\[
\mathfrak C_{\tau,y}(v)>0.
\]

Contradiction. \(\square\)

Therefore

\[
\boxed{
\{v:\ E(v)=1,\ v\text{ active nonexceptional},\ N(v)=\kappa Y_v\}
=\varnothing
}
\tag{78.1}
\]

under GWCI.

This is the exact stationary conclusion supplied by GCC-1–4.

---

## 79. From GWCI to the transverse defect on the scalar stationary stratum

A careful distinction is required here. GWCI directly excludes

\[
D_\kappa=N-\kappa Y=0.
\]

It does **not**, on an arbitrary normalized state, directly exclude the transverse equality

\[
T=\kappa R_{\rm fv},
\]

because the constrained-gradient component of \(N-\kappa Y\) may still be nonzero.

Recall

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
=(\gamma-\kappa r)G
+(T-\kappa R_{\rm fv}).
\tag{79.1}
\]

Define the **scalar stationary stratum**

\[
\boxed{
\Sigma_\kappa
:=
\{v\in K:\ W(v)=2\kappa(v)D_3(v)\}.
}
\tag{79.2}
\]

On \(\Sigma_\kappa\),

\[
\gamma
=\frac{W}{2d^2}
=\kappa\frac{D_3}{d^2}
=\kappa r.
\]

Hence (79.1) reduces exactly to

\[
\boxed{
N-\kappa Y
=T-\kappa R_{\rm fv}
\qquad\text{on }\Sigma_\kappa.
}
\tag{79.3}
\]

### Corollary 79.1

Assume GWCI, (G-Reg), and (G-NE). Then for every \(v\in\Sigma_\kappa\),

\[
\boxed{
T(v)\neq\kappa(v)R_{\rm fv}(v).
}
\tag{79.4}
\]

### Proof

If equality held, then (79.3) would give \(D_\kappa(v)=0\). GWCI would force \(\mathfrak C_{\tau,y}(v)=0\), contradicting Theorem 74.1. \(\square\)

If the compact class \(K\) is itself defined inside the scalar stationary stratum, then (79.4) holds on all of \(K\). If \(K\) is a larger normalized class, the conclusion is only asserted on the closed subset \(\Sigma_\kappa\).

---

## 80. Uniform transverse gap on the scalar stationary stratum

Assume \(K\) is compact and the displayed scalar functionals are continuous. Then \(\Sigma_\kappa\) is closed in \(K\), hence compact.

By the radial homogeneous theorem,

\[
R_{\rm fv}(v)=0\Longrightarrow v=0.
\]

Since \(E(v)=1\),

\[
R_{\rm fv}(v)\neq0
\qquad\forall v\in\Sigma_\kappa.
\tag{80.1}
\]

Define

\[
\Psi_\kappa(v)
:=
\frac{
\|T(v)-\kappa(v)R_{\rm fv}(v)\|_{H^{-1/2}}
}{
\|T(v)\|_{H^{-1/2}}
+
\kappa(v)\|R_{\rm fv}(v)\|_{H^{-1/2}}
}.
\tag{80.2}
\]

The denominator is positive by (80.1), and Corollary 79.1 makes the numerator positive. Continuity and compactness therefore give

\[
\eta_K^{\rm GCC}
:=
\min_{v\in\Sigma_\kappa}\Psi_\kappa(v)>0,
\]

provided \(\Sigma_\kappa\neq\varnothing\). Thus

\[
\boxed{
\|T-\kappa R_{\rm fv}\|_{H^{-1/2}}
\ge
\eta_K^{\rm GCC}
\bigl(
\|T\|_{H^{-1/2}}
+
\kappa\|R_{\rm fv}\|_{H^{-1/2}}
\bigr)
\quad\text{on }\Sigma_\kappa.
}
\tag{80.3}
\]

If \(\Sigma_\kappa=\varnothing\), the stationary candidate stratum is already absent and no quantitative minimum on it is needed.

This is the rigorous transverse-gap consequence of GWCI. It avoids the stronger but unjustified inference that stationary exclusion alone implies \(T\neq\kappa R_{\rm fv}\) on every point of an arbitrary larger class \(K\).

---

## 81. Parameterized positive-alignment version

For \(\lambda>0\), define

\[
D_\lambda(v):=N(v)-\lambda Y_v
\]

and the scalar alignment stratum

\[
\Sigma_\lambda
:=
\{v:\ W(v)=2\lambda D_3(v)\}.
\tag{81.1}
\]

On \(\Sigma_\lambda\), the same decomposition gives

\[
\boxed{
D_\lambda
=T-\lambda R_{\rm fv}.
}
\tag{81.2}
\]

Thus a parameterized GWCI of the form

\[
\boxed{
\mathfrak W_{\tau,y}^{(\lambda)}
\bigl(v;N(v)-\lambda Y_v\bigr)
=
\mathfrak C_{\tau,y}^{(\lambda)}(v),
}
\tag{81.3}
\]

with a strictly positive right-hand side on the active nonexceptional part of \(\Sigma_\lambda\), would imply

\[
\boxed{
T(v)\neq\lambda R_{\rm fv}(v)
\qquad
\text{for every }v\in\Sigma_\lambda.
}
\tag{81.4}
\]

If such a parameterized identity is uniform in \(\lambda\) over a compact positive interval and if \(T,R_{\rm fv}\) are nonzero, the compact angle argument from Sections 44–45 yields a uniform angular gap.

No such parameterized GWCI is presently claimed proved.

---

## 82. Relationship between GCC and FSSS

GCC and FSSS describe the same remaining obstruction at two different levels.

FSSS asks for a finite bounded-reader determinant \(\mathscr D\) such that saturation forces flatness while semigroup rectangle geometry forces nonflatness.

GWCI asks for a stronger global Ward functional whose evaluation on the full defect equals an explicitly positive companion integral:

\[
\mathfrak W(v;D_\kappa)=\mathfrak C(v).
\]

Therefore

\[
\boxed{
\text{GWCI}\Longrightarrow\text{a global finite-separation certificate of stationary saturation}.
}
\tag{82.1}
\]

A successful explicit construction of \(\mathfrak W\) would close the stationary FSSS problem in one stroke. Conversely, an FSSS determinant need not factor through a positive integral of the precise form (71.1), so FSSS is logically weaker than GWCI.

This hierarchy is useful:

\[
\boxed{
\text{GWCI is a strong sufficient theorem; FSSS is the minimal finite-separation target.}
}
\tag{82.2}
\]

---

## 83. Exact status of Part I.5

The rigorous status is now:

### Proved from explicit semigroup geometry plus the stated regularity/nonexceptionality hypotheses

\[
\boxed{\mathrm{GCC2}}
\qquad
\boxed{\mathrm{GCC3}}
\qquad
\boxed{\mathrm{GCC4}}
\]

and the compactness upgrade

\[
\boxed{
\inf_{v\in K}\mathfrak C_{\tau,y}(v)>0
}
\]

whenever \(K\) is compact, (G-Reg) is continuous, and (G-NE) holds throughout \(K\).

### Conditional on the new global identity

GWCI implies GCC-1:

\[
D_\kappa(v)=0
\Longrightarrow
\mathfrak C_{\tau,y}(v)=0.
\]

Combining GCC-1 with GCC-4 excludes active nonexceptional stationary states.

On the scalar stationary stratum \(W=2\kappa D_3\), the exact decomposition identifies

\[
D_\kappa=T-\kappa R_{\rm fv},
\]

so the same argument yields the uniform transverse gap (80.3) by compactness.

### Not proved by the bare frontier

\[
\boxed{\text{GWCI (76.3)}}
\]

remains a genuinely new global multilinear identity. Until an explicit Ward operator \(\mathfrak W_{\tau,y}\) is constructed and its Fourier symbol is checked term by term, Part I.5 does not give an unconditional Navier–Stokes contradiction.

Thus the exact endpoint of this layer is

\[
\boxed{
\begin{gathered}
\text{local companion geometry}\\
+\text{positive-measure support rectangles}\\
+\text{strict heat--Poisson conductance}\\
\Downarrow\\
\mathfrak C_{\tau,y}(v)>0\\
\text{for active nonexceptional }v,\\[1mm]
\boxed{\text{GWCI still required}}\\
\Downarrow\\
D_\kappa=0\Rightarrow\mathfrak C_{\tau,y}=0\\
\Downarrow\\
\text{stationary contradiction and transverse gap on }\Sigma_\kappa.
\end{gathered}
}
\tag{83.1}
\]

The next mathematically decisive task is therefore not another compactness argument. It is the explicit construction—or rigorous disproof—of the Ward functional in (76.3).

---

# PART VIII. STRUCTURAL STOP — CHANNEL-QUOTIENT DESCENT NO-GO AND PHYSICAL HEAT-RIGIDITY RESET

> **Status update.** This part performs the promised final audit of the most natural GWCI construction. The conclusion is a genuine no-go theorem: the positive paired-conductance functional of Part VII does not, in general, descend through physical additive channel aggregation by pushing its channel gradient through the adjoint aggregation map. This invalidates the **channel-faithful descent route** to GWCI. It does **not** rule out every logically possible Ward identity; a functional constructed directly after physical aggregation remains a separate possibility.

The exact test is

\[
\boxed{
\mathcal Q_{\tau,y}(\mathcal B(v))
\stackrel{?}{\in}
\operatorname{Ran}\Sigma^*,
}
\tag{84.1}
\]

where \(\mathcal B(v)\) denotes the unfolded channel lift and \(\mathcal Q_{\tau,y}\) is the channel gradient of the paired-conductance energy. We show that (84.1) fails generically already at the exact Curl--Killing symbol level.

---

## 84. Localized physical aggregation on one output fiber

Fix a nonzero output frequency \(k\), input helicities \(\alpha,\beta\in\{\pm1\}\), and output helicity \(\tau\). Write

\[
q=k-p.
\]

The exact polarized Curl--Killing scalar symbol is

\[
\boxed{
\beta_{\alpha\beta}^{\tau}(p,k-p)
=
\frac{\alpha|p|-\beta|k-p|}{2}
\,m_{\alpha\beta}^{\tau}(p,k-p),
}
\tag{84.2}
\]

where

\[
Q_\tau(k)
\bigl(e_\beta(k-p)\times e_\alpha(p)\bigr)
=
m_{\alpha\beta}^{\tau}(p,k-p)e_\tau(k).
\tag{84.3}
\]

If

\[
a_\alpha(p)
:=\langle\widehat v(p),e_\alpha(p)\rangle,
\]

then the channel lift on this output fiber is

\[
\boxed{
F_k(p)
:=
\beta_{\alpha\beta}^{\tau}(p,k-p)
\,a_\alpha(p)a_\beta(k-p).
}
\tag{84.4}
\]

The physical Formation coefficient sees only the additive aggregate

\[
N_\tau(k)
=
\int F_k(p)\,dp
\]

up to the finite sum over input-helicity sectors.

For the functional-analytic range calculation we localize to a finite-measure incidence patch \(U\Subset\mathbb R^3\) containing the wave packets used below. Set

\[
X_U:=L^2(U;\mathbb C),
\qquad
\Sigma_UF:=\int_UF(p)\,dp.
\tag{84.5}
\]

Then \(\Sigma_U:X_U\to\mathbb C\) is bounded. Its adjoint is

\[
\boxed{
(\Sigma_U^*z)(p)=z
\quad\text{for a.e. }p\in U,
}
\tag{84.6}
\]

and therefore

\[
\boxed{
\operatorname{Ran}\Sigma_U^*
=
\{\text{constant functions on }U\}.
}
\tag{84.7}
\]

Thus channel-faithful descent requires the channel derivative at a fixed physical output to assign the same dual coefficient to every incidence decomposition represented inside \(U\).

---

## 85. Wave-packet symbol localization

The obstruction can be tested on a finite symbol configuration.

### Lemma 85.1 — wave-packet symbol extraction

Let \(\mathscr I(v)=0\) be a universal polynomial Fourier identity built from finitely many multilinear interactions, Fourier multipliers smooth on the frequencies under consideration, Leray/helical projections, and Curl--Killing symbols. If \(\mathscr I(v)=0\) for every real Schwartz field, then the corresponding discrete algebraic symbol identity holds on every finite nonexceptional frequency configuration.

### Proof

Choose distinct nonzero frequencies

\[
\xi_1,\dots,\xi_M
\]

and a bump \(\varphi\in C_c^\infty(B(0,1))\). Put

\[
\varphi_{\varepsilon,j}(k)
:=
\varepsilon^{-3/2}
\varphi\left(\frac{k-\xi_j}{\varepsilon}\right).
\]

For sufficiently small \(\varepsilon\), the supports are pairwise disjoint and avoid every singular multiplier locus. Define

\[
\widehat v_\varepsilon
=
\sum_jc_j\varphi_{\varepsilon,j}e_{\sigma_j}
+
\text{reality completion}.
\tag{85.1}
\]

Every smooth multiplier converges uniformly on the \(j\)-th packet to its value at \(\xi_j\). By separation of the packet supports, each prescribed finite interaction history has a leading term given by the corresponding discrete symbol, while histories with distinct output centers remain separated at leading order. After dividing by the common packet-scaling factor of the polynomial expression and letting \(\varepsilon\downarrow0\), the asserted universal identity yields its discrete symbol identity.

Therefore a single finite nonexceptional symbol configuration violating a proposed algebraic range identity disproves the corresponding universal Schwartz-field identity. \(\square\)

---

## 86. Four same-output decompositions with two common companion outputs

Choose four decompositions

\[
p_i+q_i=k,
\qquad i=1,2,3,4,
\tag{86.1}
\]

such that

\[
\boxed{
p_1-p_2=p_3-p_4=:d\neq0.}
\tag{86.2}
\]

Then

\[
p_1+q_2=k+d,
\qquad
p_3+q_4=k+d,
\]

so there are two distinct channels into the same physical output \(k+d\):

\[
e_{12}:=(p_1,q_2\to k+d),
\qquad
e_{34}:=(p_3,q_4\to k+d).
\tag{86.3}
\]

Their reverse companions are

\[
e_{21}:=(p_2,q_1\to k-d),
\qquad
e_{43}:=(p_4,q_3\to k-d).
\tag{86.4}
\]

Choose \((k,d,p_1,p_3)\) generically so that all relevant frequencies are distinct and nonzero, no relevant pair is collinear or same-root, and the required helical projections are nonzero. The excluded conditions form a finite union of proper algebraic/analytic subvarieties on any fixed helical chart, so such nonexceptional configurations exist. In particular we may assume

\[
\boxed{
\beta_{12},\beta_{21},\beta_{34},\beta_{43}\neq0.
}
\tag{86.5}
\]

Let

\[
A_i:=a_{\alpha_i}(p_i),
\qquad
B_i:=a_{\beta_i}(q_i),
\]

and define the exact discrete channel amplitudes

\[
\boxed{
z_{ij}:=\beta_{ij}A_iB_j.}
\tag{86.6}
\]

Because the positive-frequency packet centers are chosen distinct, the \(A_i,B_i\) are independent complex parameters in the discrete symbol test. Reality completion only adds their conjugate partners at negative frequencies.

---

## 87. Discrete paired-conductance gradient

For a same-output pair \((i,j)\), let

\[
\Gamma_{ij}
:=
1-\exp[-\Xi_{\tau,y}(k,p_i-p_j)].
\tag{87.1}
\]

The finite symbol localization of the paired-conductance functional contains

\[
\boxed{
\mathfrak C_{\rm disc}
=
\sum_{i<j}
\Gamma_{ij}
|z_{ij}|^2|z_{ji}|^2.
}
\tag{87.2}
\]

Using the Wirtinger derivative,

\[
\frac{\partial}{\partial\overline{z}_{ij}}
\bigl(|z_{ij}|^2|z_{ji}|^2\bigr)
=
z_{ij}|z_{ji}|^2.
\]

Hence the channel gradient coordinate is

\[
\boxed{
(\mathcal Q_{\rm disc})_{ij}
=
\Gamma_{ij}z_{ij}|z_{ji}|^2,
}
\tag{87.3}
\]

up to a harmless common factor if oriented pairs are double counted.

At the output \(k+d\), physical aggregation of the two coordinates in (86.3) is

\[
\Sigma_{k+d}(z_{12},z_{34})
=z_{12}+z_{34},
\tag{87.4}
\]

so

\[
\boxed{
\operatorname{Ran}\Sigma_{k+d}^*
=
\{(\zeta,\zeta):\zeta\in\mathbb C\}.
}
\tag{87.5}
\]

By (86.2),

\[
\Gamma_{12}=\Gamma_{34}=:\Gamma>0.
\tag{87.6}
\]

Therefore the two relevant gradient coordinates are

\[
\boxed{
\Gamma
\bigl(
 z_{12}|z_{21}|^2,
 z_{34}|z_{43}|^2
\bigr).
}
\tag{87.7}
\]

For this vector to lie in (87.5), one would need the universal identity

\[
\boxed{
z_{12}|z_{21}|^2
=
z_{34}|z_{43}|^2.
}
\tag{87.8}
\]

We now show that no such Curl--Killing symbol identity exists.

---

## 88. Amplitude-scaling contradiction

Substituting (86.6) into (87.8) gives

\[
\beta_{12}A_1B_2
\,|\beta_{21}A_2B_1|^2
=
\beta_{34}A_3B_4
\,|\beta_{43}A_4B_3|^2.
\tag{88.1}
\]

Fix all amplitudes except \(A_1\), with every fixed amplitude nonzero, and set

\[
A_1=t,
\qquad t\in\mathbb C^\times.
\]

The left side of (88.1) is

\[
C t,
\qquad C\neq0,
\]

whereas the right side is a nonzero constant \(C_0\) independent of \(t\). Thus (88.1) would require

\[
Ct=C_0
\]

for every \(t\in\mathbb C^\times\), which is impossible.

Hence (87.8) is not a universal discrete symbol identity.

By Lemma 85.1, no universal sufficiently regular field identity can force the channel gradient of paired conductance into the adjoint aggregation range.

### Theorem 88.1 — channel-faithful range no-go

For generic nonexceptional states/configurations,

\[
\boxed{
\mathcal Q_{\tau,y}(\mathcal B(v))
\notin
\operatorname{Ran}\Sigma^*.
}
\tag{88.2}
\]

In particular, there is no universal physical Ward field \(\Phi_{\tau,y}(v)\) satisfying

\[
\boxed{
\mathcal Q_{\tau,y}(\mathcal B(v))
=
\Sigma^*\Phi_{\tau,y}(v)
}
\tag{88.3}
\]

for all sufficiently regular active nonexceptional states.

\[
\boxed{\mathrm{QED}}
\]

---

## 89. Exact kernel-cancellation witness

The failure can be written directly in the kernel of aggregation. Let

\[
q_{12}:=\Gamma z_{12}|z_{21}|^2,
\qquad
q_{34}:=\Gamma z_{34}|z_{43}|^2.
\]

For a configuration with \(q_{12}\neq q_{34}\), set

\[
H
:=
(q_{12}-q_{34},-(q_{12}-q_{34})).
\tag{89.1}
\]

Then

\[
\Sigma_{k+d}H=0,
\]

but with the real Hilbert pairing,

\[
\operatorname{Re}
\langle(q_{12},q_{34}),H\rangle
=
|q_{12}-q_{34}|^2>0.
\tag{89.2}
\]

Thus the conductance derivative does not annihilate the hidden-cancellation direction \(\ker\Sigma\). This is the exact infinitesimal obstruction to physical quotient descent.

---

## 90. General quotient-descent criterion

The preceding phenomenon is not specific to Curl--Killing.

### Theorem 90.1 — quotient descent criterion

Let \(X,H\) be real Hilbert spaces, let \(\Sigma:X\to H\) be bounded and linear, and let \(C:X\to\mathbb R\) be continuously Fréchet differentiable. Then the following are equivalent:

1. there exists a function \(\widetilde C:\operatorname{Ran}\Sigma\to\mathbb R\) such that
   \[
   C=\widetilde C\circ\Sigma;
   \]
2. for every \(F\in X\) and every \(K\in\ker\Sigma\),
   \[
   \boxed{DC(F)[K]=0;}
   \tag{90.1}
   \]
3. for every \(F\in X\),
   \[
   \boxed{
   \nabla C(F)\in(\ker\Sigma)^\perp
   =\overline{\operatorname{Ran}\Sigma^*}.
   }
   \tag{90.2}
   \]

If \(\operatorname{Ran}\Sigma\) is closed, the closure in (90.2) may be removed.

### Proof

If \(C=\widetilde C\circ\Sigma\), then the chain rule gives

\[
DC(F)=D\widetilde C(\Sigma F)\circ\Sigma,
\]

so (90.1) follows for every \(K\in\ker\Sigma\).

Conversely, assume (90.1). If \(F_1,F_2\) satisfy \(\Sigma F_1=\Sigma F_2\), then \(K:=F_2-F_1\in\ker\Sigma\). Along the affine line \(F(t)=F_1+tK\),

\[
\frac{d}{dt}C(F(t))
=DC(F(t))[K]=0.
\]

Hence \(C(F_1)=C(F_2)\). Thus \(C\) is constant on every affine fiber of \(\Sigma\), and \(\widetilde C(\Sigma F):=C(F)\) is well-defined on \(\operatorname{Ran}\Sigma\).

Finally, in a Hilbert space,

\[
DC(F)[K]
=\langle\nabla C(F),K\rangle.
\]

Therefore (90.1) is equivalent to \(\nabla C(F)\perp\ker\Sigma\), and the standard adjoint identity gives

\[
(\ker\Sigma)^\perp
=
\overline{\operatorname{Ran}\Sigma^*}.
\]

\(\square\)

The paired companion conductance violates (90.1) by Section 89. Therefore it is not a functional of the physical quotient variable \(\Sigma F\).

---

## 91. Consequence for the proposed GWCI descent route

Part VII left open a GWCI of the schematic form

\[
\mathfrak W(v;D_\kappa)=\mathfrak C(v).
\]

One natural attempted construction was:

\[
\text{positive channel conductance}
\longrightarrow
\text{differentiate in channel space}
\longrightarrow
\mathcal Q(\mathcal B(v))
\stackrel{?}{=}
\Sigma^*\Phi(v)
\longrightarrow
\langle\Phi(v),D_\kappa(v)\rangle
=
\mathfrak C(v).
\tag{91.1}
\]

Theorem 88.1 proves that the third arrow in (91.1) fails generically. Therefore:

\[
\boxed{
\text{the channel-gradient / adjoint-aggregation route to GWCI is impossible in general.}
}
\tag{91.2}
\]

This is a structural no-go, not an estimate failure. No strengthening of a norm inequality can force a generic vector outside \(\operatorname{Ran}\Sigma^*\) into that range.

### Scope of the no-go

Theorem 88.1 does **not** prove that every conceivable identity named “GWCI” is impossible. It excludes identities obtained by making the paired channel conductance descend through physical aggregation in the channel-faithful manner (88.3), or equivalently by treating \(\mathfrak C\) itself as a physical quotient functional. A genuinely different Ward functional built directly from physical aggregate fields after convolution is not covered by this no-go theorem.

Accordingly the status statement in Section 83 is now sharpened: the most natural channel-descent construction of GWCI has been rigorously disproved.

---

## 92. What survives the stop theorem

The stop theorem does not invalidate the previously proved local/channel results. In particular:

1. **Bridge 1 remains valid:** exact unfolded projective channel closure and gauge-covariant scalar gains are unchanged.
2. **Support rectangle extraction remains valid:** under (NE-S), active nonexceptional states possess positive-measure families of companion rectangles.
3. **Heat--Poisson reverse-pair curvature remains valid:**
   \[
   \Gamma_{\tau,y}(k,d)>0
   \qquad(d\neq0).
   \]
4. **Channel-lift conductance remains positive:** under (G-Reg) and (G-NE),
   \[
   \mathfrak C_{\tau,y}(v)>0.
   \]

What fails is exactly the additional assertion

\[
\boxed{
\mathfrak C_{\tau,y}
\text{ descends through the additive physical aggregation }\Sigma.
}
\tag{92.1}
\]

Thus channel curvature remains genuine information, but it cannot by itself be converted into a physical Ward pairing by quotient descent.

---

## 93. Physical semigroup commutator: a quotient-safe candidate

The next candidate must be formed **after** physical convolution channels have already been summed.

Let

\[
H_\tau:=e^{-\tau\Lambda^2},
\]

and write the quadratic nonlinearity as \(N(v)=B(v,v)\). Define

\[
\boxed{
\mathcal K_\tau(v)
:=
H_\tau N(v)
-
B(H_{\tau/2}v,H_{\tau/2}v).
}
\tag{93.1}
\]

In Fourier variables, with \(q=k-p\),

\[
\boxed{
\widehat{\mathcal K_\tau(v)}(k)
=
\int
\left[
 e^{-\tau|k|^2}
-
 e^{-\frac\tau2(|p|^2+|q|^2)}
\right]
\widehat B_v(p,q)\,dp.
}
\tag{93.2}
\]

The integral in (93.2) is the physical aggregate. Only after that aggregation does one take a norm such as

\[
\boxed{
\|\mathcal K_\tau(v)\|_2^2\ge0.
}
\tag{93.3}
\]

Therefore hidden channel cancellation is treated exactly as the PDE treats it, and the quotient obstruction of Theorem 88.1 is absent by construction.

However, stationarity does not imply \(\mathcal K_\tau(v)=0\). Indeed, even if

\[
N(v)=\kappa Yv,
\]

there is no established identity identifying

\[
B(H_{\tau/2}v,H_{\tau/2}v)
\]

with \(\kappa YH_\tau v\). Thus \(\mathcal K_\tau\) is a structurally admissible physical object, but not yet the final Ward functional.

---

## 94. Canonical heat identity: the exact physical starting point

The correct physical starting point is the canonical heat identity already proved in Section 62. At

\[
\tau_*
=
\frac{1}{4D_2},
\qquad
w:=H_{\tau_*}v,
\]

we have

\[
\boxed{
H_{\tau_*}Yv
=
D_2(2L-1)w.
}
\tag{94.1}
\]

Hence every stationary finite-\(\kappa\) state satisfies the exact physical relation

\[
\boxed{
H_{\tau_*}N(v)
=
\kappa D_2(2L-1)H_{\tau_*}v.
}
\tag{94.2}
\]

No channel quotient appears in (94.2). All nonlinear incidences have already been physically aggregated inside \(N(v)\).

Moreover, because the heat multiplier \(e^{-\tau_*|k|^2}\) is strictly positive for every finite frequency, \(H_{\tau_*}\) is injective on the natural tempered-distribution classes on which the expressions are defined. Together with (94.1), relation (94.2) is therefore an exact semigroup re-expression of the stationary equation, not a lossy finite reader.

---

## 95. New terminal theorem: Canonical Physical Heat-Rigidity

The Bridge-2 terminal problem is now reset as follows.

### Conjectural Theorem 95.1 — Canonical Physical Heat-Rigidity (CPHR)

Let \(v\) belong to the normalized active nonexceptional finite-\(\kappa\) class, with enough regularity that all terms below are defined, and put

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
\tag{95.1}
\]

Then

\[
\boxed{v=0.}
\tag{95.2}
\]

Equivalently, because \(E(v)=1\) in the normalized class, no such nonexceptional normalized state exists.

### Status

Theorem 95.1 is **not proved** by the present file. It is the new physical-space semigroup rigidity target. Unlike FWE, recurrence, holonomy, FSSS-by-channel-descent, or channel-faithful GWCI, it is posed entirely after physical nonlinear aggregation.

A proof of CPHR would exclude stationary finite-\(\kappa\) profiles directly.

---

## 96. Consequence for the transverse defect on the scalar stationary stratum

The same logical distinction emphasized in Section 79 remains necessary. CPHR directly excludes the stationary equation

\[
N=\kappa Y.
\]

On an arbitrary normalized state, this is not identical to the transverse relation \(T=\kappa R_{\rm fv}\). But on

\[
\Sigma_\kappa
=
\{v:W=2\kappa D_3\},
\]

Section 79 proved

\[
N-\kappa Y
=
T-\kappa R_{\rm fv}.
\tag{96.1}
\]

Therefore, if CPHR is proved and \(v\in\Sigma_\kappa\) satisfied

\[
T(v)=\kappa R_{\rm fv}(v),
\]

then (96.1) would give \(N(v)=\kappa Y_v\), hence (94.2), and CPHR would force \(v=0\), contradicting \(E(v)=1\).

Thus CPHR would imply

\[
\boxed{
T(v)\neq\kappa R_{\rm fv}(v)
\qquad
\forall v\in\Sigma_\kappa.
}
\tag{96.2}
\]

Compactness of \(\Sigma_\kappa\) would then reproduce the uniform transverse gap of Section 80 without any GWCI, FWE, or recurrence assumption.

---

## 97. Final status after the structural stop

The proof program has now eliminated one entire false route.

### QED in this part

\[
\boxed{
\mathcal Q_{\tau,y}(\mathcal B(v))
\notin\operatorname{Ran}\Sigma^*
\quad\text{generically}.
}
\tag{97.1}
\]

Consequently

\[
\boxed{
\text{channel-descent GWCI is impossible in general.}
}
\tag{97.2}
\]

The precise meaning of (97.2) is the channel-gradient / adjoint-aggregation construction of Section 91; it does not exclude every possible physical Ward identity.

### Still valid

\[
\boxed{
\text{Bridge 1}
+
\text{support-geometric rectangles}
+
\text{strict semigroup curvature}
+
\text{positive channel-lift conductance}
}
\]

remain established under their stated hypotheses.

### New terminal frontier

The preferred terminal theorem is now

\[
\boxed{
\textbf{Canonical Physical Heat-Rigidity:}
\qquad
H_{\tau_*}N(v)
=
\kappa D_2(2L-1)H_{\tau_*}v
\Longrightarrow
v=0
}
\tag{97.3}
\]

on the normalized active nonexceptional class.

If (97.3) is established, then stationary finite-\(\kappa\) states are excluded directly. On the scalar stationary stratum it also excludes \(T=\kappa R_{\rm fv}\), after which the already proved compactness argument gives

\[
\|T-\kappa R_{\rm fv}\|_{H^{-1/2}}
\ge
\eta_K
\bigl(
\|T\|_{H^{-1/2}}
+
\kappa\|R_{\rm fv}\|_{H^{-1/2}}
\bigr).
\]

Thus the updated dependency chain is

\[
\boxed{
\begin{gathered}
\text{Bridge 1 exact unfolded channel calculus}\\
+\text{support rectangles and semigroup curvature}\\
\Downarrow\\
\text{channel-descent route audited and ruled out}\\
\Downarrow\\
\boxed{\text{work directly after physical aggregation}}\\
\Downarrow\\
H_{\tau_*}N(v)
=
\kappa D_2(2L-1)H_{\tau_*}v\\
\Downarrow\\
\boxed{\text{CPHR — the remaining terminal rigidity theorem}}\\
\Downarrow\\
\text{stationary exclusion}\\
\Downarrow\\
\text{transverse gap on }\Sigma_\kappa.
\end{gathered}
}
\tag{97.4}
\]

No further claim of unconditional QED is made until CPHR, or an equivalent physical-output rigidity theorem, is proved.
