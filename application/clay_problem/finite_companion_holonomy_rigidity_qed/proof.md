Yes. I will close the argument at the strongest level that is mathematically justified.

There are really two statements to prove:

1. **A no-go theorem:** the axioms presently written in Parts A–C do not imply a nontrivial holonomy defect. This can be proved completely.
2. **A corrected finite-holonomy theorem:** once the missing channel/state-incidence closure and finite-witness property are stated explicitly, the desired mode-count-independent transverse gap follows rigorously. This can also be proved completely.

What cannot responsibly be supplied is a fictitious proof of the missing physical nonflatness assertion from hypotheses that do not contain enough information to imply it.

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

However, if one supplements the theory by an exact **channel-resolved projective state-incidence closure law** and a **pointwise finite nonflat witness theorem**, then compactness produces finitely many witness loops and a uniform \(c_K>0\); this excludes positive saturation and yields the desired transverse norm gap. Under uniform nonvanishing, it also yields the angular gap.

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
\boxed{
h_e\mapsto g_pg_qg_r^{-1}h_e.}
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