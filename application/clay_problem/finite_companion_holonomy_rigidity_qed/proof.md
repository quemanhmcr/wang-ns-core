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
H_R=rac{h_{11}h_{22}}{h_{12}h_{21}}.
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
=
\sum_{\alpha\to r}a_{r,\alpha}
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
\text{finite reconstruction is unnecessary;
finite separation is sufficient.}
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
