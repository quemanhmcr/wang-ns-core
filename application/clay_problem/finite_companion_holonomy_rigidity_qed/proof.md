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
\boxed{
\mathscr R_\sigma h_\sigma=0.
}
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
\begin{aligned}
\mathscr R_\sigma h_\sigma
&=
\left(
4D_2+\chi_\sigma\rho^2-ra\rho
-\chi_\sigma\rho^2+ra\rho-4D_2
\right)h_\sigma\\
&=0.
\end{aligned}
\]

\(\square\)

---

## Theorem 1.2 — canonical annular right inverse

Let \(F_\sigma\) be smooth and supported in

\[
\rho_0<\rho<\rho_1,
\qquad
0<\rho_0<\rho_1<\infty.
\]

Then the equation

\[
\kappa\mathscr R_\sigma f=F_\sigma
\tag{1.1}
\]

has a unique finite-\(H^{-1/2}\) solution. It is

\[
\boxed{
(\mathcal S_\sigma F)(\rho,\omega)
=
-\frac{h_\sigma(\rho)}{2\kappa D_2}
\int_0^\rho
\frac{F(s,\omega)}
{s\,h_\sigma(s)}\,ds.
}
\tag{1.2}
\]

### Proof

Write

\[
f=h_\sigma c.
\]

Using Lemma 1.1,

\[
\begin{aligned}
\mathscr R_\sigma(h_\sigma c)
&=
-2D_2\rho
(h_\sigma'c+h_\sigma c')
+
(-\chi_\sigma\rho^2+ra\rho-4D_2)h_\sigma c\\
&=
-2D_2\rho h_\sigma c'.
\end{aligned}
\]

Equation (1.1) becomes

\[
-2\kappa D_2\rho h_\sigma c'=F,
\]

hence

\[
c'
=
-\frac{F}{2\kappa D_2\rho h_\sigma}.
\]

Taking zero infrared integration constant gives (1.2).

Differentiating (1.2) shows exactly that

\[
\kappa\mathscr R_\sigma\mathcal S_\sigma F=F.
\]

For \(\rho<\rho_0\), the integral in (1.2) vanishes, so

\[
f(\rho,\omega)=0.
\]

For \(\rho>\rho_1\),

\[
f(\rho,\omega)
=
C_\sigma(\omega)h_\sigma(\rho)
\]

for a \(\rho\)-independent coefficient \(C_\sigma\).

Since \(\chi_\sigma>0\),

\[
h_\sigma(\rho)
=
\rho^{-2}
e^{-\frac{\chi_\sigma}{4D_2}\rho^2+O(\rho)},
\]

so the ultraviolet tail has Gaussian decay.

For uniqueness, suppose \(f_1,f_2\) are finite-energy solutions. Then

\[
w=f_1-f_2
\]

satisfies

\[
\mathscr R_\sigma w=0.
\]

Therefore

\[
w=C(\omega)h_\sigma(\rho).
\]

Near \(\rho=0\),

\[
h_\sigma(\rho)\sim\rho^{-2}.
\]

The \(H^{-1/2}\) radial measure is

\[
\rho\,d\rho\,d\omega.
\]

Thus a nonzero homogeneous solution would satisfy

\[
\int_0^\varepsilon
\rho|w|^2\,d\rho
\asymp
|C(\omega)|^2
\int_0^\varepsilon \rho^{-3}\,d\rho
=\infty.
\]

Hence \(C=0\) almost everywhere and \(w=0\).

Thus (1.2) is the unique finite-energy solution. \(\square\)

---

# 2. The radial coercivity estimate is consistent with, not opposed to, solvability

The pairing identity can also be proved exactly.

## Lemma 2.1

For smooth compactly supported \(f\),

\[
\boxed{
\operatorname{Re}
\langle f,\mathscr R_\sigma f\rangle_{H^{-1/2}}
=
\int
\rho
\left(
-\chi_\sigma\rho^2
+ra\rho
-2D_2
\right)|f|^2
\,d\rho\,d\omega.
}
\]

### Proof

The differential contribution is

\[
-2D_2
\operatorname{Re}
\int
\rho^2\overline f f'\,d\rho\,d\omega.
\]

Since

\[
2\operatorname{Re}(\overline f f')
=(|f|^2)',
\]

this equals

\[
-D_2
\int
\rho^2(|f|^2)'\,d\rho\,d\omega.
\]

Integrating by parts,

\[
=
2D_2
\int
\rho|f|^2\,d\rho\,d\omega.
\]

The zeroth-order \(-4D_2\) term contributes

\[
-4D_2
\int \rho|f|^2.
\]

Combining gives the net coefficient

\[
-2D_2.
\]

The other terms are immediate. \(\square\)

On a compact coefficient class with

\[
\chi_\sigma\ge\chi_K>0
\]

and bounded \(ra,D_2\), there exists \(\rho_K\) such that

\[
\chi_\sigma\rho^2-ra\rho+2D_2
\ge c_K\rho^2
\]

for \(\rho\ge\rho_K\). Hence

\[
-\operatorname{Re}
\langle f,\mathscr R_\sigma f\rangle
\ge
c_K
\int \rho^3|f|^2.
\]

On

\[
\rho_*\le\Lambda\le R\rho_*,
\]

Cauchy–Schwarz yields

\[
c_K\rho_*^2\|f\|_{H^{-1/2}}^2
\le
\|f\|_{H^{-1/2}}
\|\mathscr R_\sigma f\|_{H^{-1/2}},
\]

so

\[
\boxed{
\|f\|_{H^{-1/2}}
\le
C_K\rho_*^{-2}
\|\mathscr R_\sigma f\|_{H^{-1/2}}.
}
\tag{2.1}
\]

This is a resolvent estimate.

It does **not** imply \(f=0\) when the right-hand side is nonzero.

Indeed Theorem 1.2 explicitly constructs \(f\).

Thus

\[
\boxed{
\text{high-frequency coercivity}
=
\text{small absorber},
\quad
\text{not}
\quad
\text{absence of absorber}.
}
\]

This distinction will be fundamental below.

---

# 3. Complete classification of rank-one multiplicative identities

Let \(I,J\) be finite index sets and let

\[
Z_{ij}=A_iB_j
\]

on a finite bipartite incidence graph.

We first classify all Laurent-monomial identities.

## Theorem 3.1 — rank-one cycle lattice

Let

\[
M(Z)
=
\prod_{(i,j)} Z_{ij}^{n_{ij}},
\qquad
n_{ij}\in\mathbb Z.
\]

Then

\[
M(Z)=1
\]

for every choice of nonzero \(A_i,B_j\) if and only if

\[
\sum_j n_{ij}=0
\qquad
\forall i,
\tag{3.1}
\]

and

\[
\sum_i n_{ij}=0
\qquad
\forall j.
\tag{3.2}
\]

Every such exponent pattern is an integer combination of alternating bipartite cycles.

### Proof

Substitute

\[
Z_{ij}=A_iB_j.
\]

Then

\[
M
=
\prod_i
A_i^{\sum_jn_{ij}}
\prod_j
B_j^{\sum_in_{ij}}.
\]

For this to equal \(1\) for arbitrary nonzero \(A_i,B_j\), every exponent must vanish, giving (3.1)–(3.2).

Orient the bipartite graph from \(I\) to \(J\). Conditions (3.1)–(3.2) are precisely the zero-boundary condition for an integral circulation on the graph.

The integral circulation lattice of a finite graph is generated by its cycle lattice. Because the graph is bipartite, every cycle is alternating and even.

Hence all rank-one Laurent identities are generated by alternating cycles. \(\square\)

---

## Corollary 3.2 — rectangle holonomy

For a \(2\times2\) rectangle,

\[
\boxed{
\operatorname{Hol}^{Z}_{ij}
=
\frac{Z_{ii}Z_{jj}}
{Z_{ij}Z_{ji}}
=1.
}
\]

For a longer alternating cycle

\[
i_1-j_1-i_2-j_2-\cdots-i_m-j_m-i_1,
\]

one convenient representation is

\[
\boxed{
\operatorname{Hol}^{Z}_\Gamma
=
\prod_{\ell=1}^m
\frac{Z_{i_\ell j_\ell}}
     {Z_{i_{\ell+1}j_\ell}}
=1.
}
\tag{3.3}
\]

This is invariant under the requested rescaling

\[
A_i\mapsto cA_i,\qquad
B_j\mapsto c^{-1}B_j,
\]

indeed under the much larger independent row/column gauge.

So the exact holonomy contained in rank one is **flat**.

---

# 4. Finite simultaneous radial absorption is a direct-product system

Let \(E(\Gamma)\) be a finite collection of physical companion edges.

For each \(e\),

\[
F_e
=
\kappa\mathscr R_{\sigma_e}f_e.
\]

Define

\[
\mathbf R_\Gamma
=
\bigoplus_{e\in E(\Gamma)}
\kappa\mathscr R_{\sigma_e}
\]

and

\[
\mathbf S_\Gamma
=
\bigoplus_{e\in E(\Gamma)}
\mathcal S_{\sigma_e}.
\]

## Theorem 4.1

\[
\boxed{
\mathbf R_\Gamma\mathbf S_\Gamma=I.
}
\tag{4.1}
\]

Hence every finite family of admissible annular companion forcings has the unique edgewise absorber

\[
\boxed{
f_e=\mathcal S_{\sigma_e}F_e.
}
\tag{4.2}
\]

### Proof

Theorem 1.2 gives

\[
\kappa\mathscr R_{\sigma_e}
\mathcal S_{\sigma_e}=I
\]

on every edge separately.

Taking the finite direct sum proves (4.1). \(\square\)

---

# 5. Incorporating the Curl–Killing rank-one amplitudes

Write the physical edge forcing schematically as

\[
F_e=Z_e\Phi_e,
\]

where \(Z_e\) is the rank-one coefficient and \(\Phi_e\) includes all geometric data:

\[
(x-y),
\qquad
P_k,
\qquad
\text{polarization},
\qquad
\text{helicity branch}.
\]

By linearity,

\[
f_e
=
\mathcal S_{\sigma_e}(Z_e\Phi_e)
=
Z_e\mathcal S_{\sigma_e}\Phi_e.
\]

Define

\[
G_e
=
\mathcal S_{\sigma_e}\Phi_e.
\]

Then

\[
\boxed{
f_e=Z_eG_e.
}
\tag{5.1}
\]

Now rank one gives relations among \(Z_e\).

For a rectangle,

\[
Z_{ii}Z_{jj}=Z_{ij}Z_{ji}.
\]

But there is no corresponding identity

\[
G_{ii}G_{jj}=G_{ij}G_{ji}.
\]

Indeed the \(G_e\)'s generally live in different Fourier/helicity/radial output fibers, so that expression is not even intrinsically defined.

This is the first exact obstruction.

---

# 6. Reality completion adds conjugation, not cross-edge transport

Because the coefficients of \(\mathscr R_\sigma\) are real,

\[
\mathcal S_{\bar e}\overline{F_e}
=
\overline{\mathcal S_eF_e}
\]

under the appropriate reality-completed Fourier identification.

Thus

\[
F_{\bar e}
=
\overline{F_e}
\]

implies

\[
f_{\bar e}
=
\overline{f_e}.
\]

This supplies the reverse conjugate edge.

It does not impose a relation between two unrelated forward edges \(e\neq e'\).

Hence reality completion does not repair the missing projective transport.

---

# 7. A formal no-go theorem for Part A/B

We can now state the logical obstruction abstractly.

## Theorem 7.1 — absorption cannot generate a nontrivial loop consistency condition by itself

Suppose \(\mathcal H\) is a scalar functional of a finite collection

\[
\{F_e,\mathscr R_{\sigma_e},Z_e\}_{e\in E}
\]

such that

\[
\text{rank one + reality + simultaneous exact absorption}
\Longrightarrow
\mathcal H=1.
\tag{7.1}
\]

Assume the admissible forcing class is the annular class of Theorem 1.2.

Then \(\mathcal H=1\) on every locally admissible rank-one/reality-complete forcing family.

Therefore no such \(\mathcal H\) can simultaneously obey

\[
|\mathcal H-1|
\ge c>0
\]

throughout the same class.

### Proof

Given any admissible finite rank-one/reality-complete forcing family \((F_e)\), Theorem 4.1 provides simultaneous exact absorbers

\[
f_e=\mathcal S_{\sigma_e}F_e.
\]

Thus the antecedent of (7.1) holds.

Therefore

\[
\mathcal H=1.
\]

This holds for every admissible forcing family under consideration.

Hence

\[
|\mathcal H-1|=0,
\]

so no strictly positive lower bound is possible. \(\square\)

---

This does **not** prove that the full Navier–Stokes PDE possesses a forbidden saturated state.

It proves something more precise and relevant to the olympiad:

\[
\boxed{
\text{the finite data explicitly listed in A/B do not contain the global state-incidence compatibility needed to create the contradiction.}
}
\]

That missing compatibility must be stated as an additional theorem or hypothesis.

---

# 8. Additive interaction mixing creates a second obstruction

There is an additional issue that must be handled before one can define an ordinary multiplicative connection.

Navier–Stokes forcing is additive.

Suppose two physical interactions \(e_1,e_2\) feed the same occupied output packet \(r\).

Even if each absorbed contribution lies in the same one-dimensional output line,

\[
\mathcal S_rF_{e_1}=c_1\psi_r,
\qquad
\mathcal S_rF_{e_2}=c_2\psi_r,
\]

the total state contribution is

\[
(c_1+c_2)\psi_r.
\]

The amplitude law is therefore

\[
\boxed{
a_r
=
h_{e_1}a_{p_1}a_{q_1}
+
h_{e_2}a_{p_2}a_{q_2}
+\cdots .
}
\tag{8.1}
\]

It is **not**

\[
a_r=h_ea_pa_q
\]

edge by edge.

But an ordinary product holonomy requires precisely such an edgewise multiplicative law.

Therefore a scalar holonomy requires more than one-dimensional output lines.

It requires **channel resolution before physical summation**.

This is particularly important because the companion construction itself begins with same-output cancellation:

\[
\sum_i A_iB_i=0.
\]

Thus additive mixing is not peripheral—it is intrinsic to the geometry.

---

# 9. Exact formulation of the missing channel-resolution axiom

A legitimate projective holonomy theorem therefore requires the following additional structure.

## Channel-Resolved Projective Closure (CRPC)

For every edge

\[
e=(p,q\to r)
\]

in a chosen finite witness network, there are one-dimensional complex packet/channel lines

\[
L_p,\quad L_q,\quad L_{r,e},
\]

and a specified projective identification

\[
\iota_e:
L_{r,e}\longrightarrow L_r
\]

with the next input line used by the witness loop, such that

\[
\mathcal S_{r,e}
B_e(L_p,L_q)
\subseteq
L_{r,e},
\tag{9.1}
\]

nontrivially.

Moreover, the channel is followed **before summation with other incoming channels**.

This is the exact condition that turns a vector-valued interaction into scalar edge transport.

It is not currently contained in the Theory-2 frontier.

---

# 10. Genuine scalar transport under CRPC

Choose nonzero representatives

\[
\psi_v\in L_v.
\]

For each edge \(e=(p,q\to r)\), CRPC gives a unique nonzero scalar \(h_e\) such that

\[
\boxed{
\iota_e
\mathcal S_e
B_e(\psi_p,\psi_q)
=
h_e\psi_r.
}
\tag{10.1}
\]

## Theorem 10.1 — gauge law

Under

\[
\psi_v\mapsto g_v\psi_v,
\qquad
g_v\in\mathbb C^\times,
\]

we have

\[
\boxed{
h_e\mapsto
g_pg_qg_r^{-1}h_e.
}
\tag{10.2}
\]

### Proof

By bilinearity,

\[
B_e(g_p\psi_p,g_q\psi_q)
=
g_pg_qB_e(\psi_p,\psi_q).
\]

Applying the linear absorber and channel identification,

\[
\iota_e\mathcal S_eB_e(g_p\psi_p,g_q\psi_q)
=
g_pg_qh_e\psi_r.
\]

Since the new output representative is

\[
\psi_r'=g_r\psi_r,
\]

the new scalar is

\[
h_e'
=
g_pg_qg_r^{-1}h_e.
\]

\(\square\)

---

# 11. Incidence-cycle holonomy

Associate to an interaction

\[
e=(p,q\to r)
\]

the incidence vector

\[
\partial e
=
[p]+[q]-[r].
\]

Let \(n=(n_e)\) be a finitely supported integral cycle satisfying

\[
\boxed{
\sum_e n_e\partial e=0.
}
\tag{11.1}
\]

Define

\[
\boxed{
\operatorname{Hol}_n
=
\prod_e h_e^{n_e}.
}
\tag{11.2}
\]

## Theorem 11.1

\(\operatorname{Hol}_n\) is independent of every projective choice \(\psi_v\).

### Proof

Under (10.2),

\[
\operatorname{Hol}_n'
=
\operatorname{Hol}_n
\prod_e
(g_{p_e}g_{q_e}g_{r_e}^{-1})^{n_e}.
\]

For a fixed vertex \(v\), its exponent in the last product is exactly the \(v\)-component of

\[
\sum_e n_e\partial e.
\]

By (11.1), this is zero.

All gauge factors cancel, so

\[
\operatorname{Hol}_n'
=
\operatorname{Hol}_n.
\]

\(\square\)

This is the correct finite projective holonomy.

---

# 12. Global multiplicative state consistency forces flatness

Suppose actual channel amplitudes \(a_v\neq0\) satisfy

\[
\boxed{
a_r=h_ea_pa_q
}
\tag{12.1}
\]

along every edge of the chosen channel-resolved loop.

## Theorem 12.1

Every incidence cycle satisfies

\[
\boxed{
\operatorname{Hol}_n=1.
}
\]

### Proof

From (12.1),

\[
h_e
=
\frac{a_r}{a_pa_q}.
\]

Therefore

\[
\operatorname{Hol}_n
=
\prod_e
\left(
\frac{a_{r_e}}
{a_{p_e}a_{q_e}}
\right)^{n_e}.
\]

The total exponent of \(a_v\) is the negative of the \(v\)-component of

\[
\sum_e n_e\partial e,
\]

which vanishes.

Hence every amplitude cancels and

\[
\operatorname{Hol}_n=1.
\]

\(\square\)

So Problem A has exactly the desired mathematical answer **after** CRPC is supplied.

---

# 13. Why Problem B should use an existential witness, not every loop

The statement

\[
|\operatorname{Hol}_\Gamma-1|
\ge c_K
\]

for **every** loop is unnecessarily strong and generally structurally impossible.

For instance, if \(\Gamma^{-1}\) is the reverse path,

\[
\operatorname{Hol}_{\Gamma\Gamma^{-1}}
=
\operatorname{Hol}_\Gamma
\operatorname{Hol}_\Gamma^{-1}
=1.
\]

Thus trivial/retraced cycles always exist in an ordinary connection unless explicitly excluded.

The correct rigidity statement is:

\[
\boxed{
\forall v\in P
\quad
\exists\text{ a finite physical witness }\Gamma_v
\quad
|\operatorname{Hol}_{\Gamma_v}(v)-1|>0.
}
\tag{13.1}
\]

Here \(P\) is the forbidden saturation set.

This is enough.

Indeed compactness converts it into a uniform finite theorem.

---

# 14. Compactness converts pointwise finite witnesses into a uniform finite family

This is one of the most important positive results.

## Theorem 14.1 — finite-witness compactness principle

Let \(P\subset K\) be compact.

Assume that for every \(v\in P\) there exists a finite witness loop \(\Gamma_v\), defined on a neighborhood of \(v\), with continuous defect

\[
d_{\Gamma_v}(w)
=
|\operatorname{Hol}_{\Gamma_v}(w)-1|
\]

and

\[
d_{\Gamma_v}(v)>0.
\]

Then there exist finitely many loops

\[
\Gamma_1,\ldots,\Gamma_N
\]

and

\[
c_K>0
\]

such that

\[
\boxed{
\max_{1\le j\le N}
|\operatorname{Hol}_{\Gamma_j}(v)-1|
\ge c_K
\qquad
\forall v\in P.
}
\tag{14.1}
\]

Moreover,

\[
\boxed{
L_K:=\max_j|\Gamma_j|<\infty.
}
\]

### Proof

For each \(v\in P\),

\[
d_{\Gamma_v}(v)>0.
\]

By continuity there is a neighborhood \(U_v\) such that

\[
d_{\Gamma_v}(w)
>
\frac12d_{\Gamma_v}(v)
=:c_v>0
\]

for \(w\in U_v\).

The collection \(\{U_v\}_{v\in P}\) covers compact \(P\). Choose a finite subcover

\[
U_{v_1},\dots,U_{v_N}.
\]

Set

\[
\Gamma_j=\Gamma_{v_j},
\qquad
c_K=\min_j c_{v_j}>0.
\]

Given arbitrary \(w\in P\), choose \(j\) with

\[
w\in U_{v_j}.
\]

Then

\[
|\operatorname{Hol}_{\Gamma_j}(w)-1|
\ge c_{v_j}
\ge c_K.
\]

This proves (14.1).

Because only finitely many loops remain,

\[
L_K=\max_j|\Gamma_j|
\]

is finite. \(\square\)

This theorem gives precisely the desired independence from

\[
\text{mode count},
\quad
\text{shell count},
\quad
\text{completion-tree depth},
\quad
\text{Fourier cutoff}.
\]

Crucially, there was **no a priori finite-mode assumption**.

The only genuinely hard step is the pointwise finite-witness theorem (13.1).

---

# 15. Why ordinary compactness does not itself produce a finite witness

Compactness provides a finite subcover **after** each point already has a finite witness.

It does not prove that such a witness exists.

This distinction matters.

An infinite companion cascade may continually export to new spectral data:

\[
e_1\to e_2\to e_3\to\cdots
\]

without ever producing an exact state-transport cycle.

Compactness may create approximate recurrence, but

\[
\text{approximate recurrence}
\not\Rightarrow
\text{exact algebraic holonomy cycle}.
\]

An exact multiplicative identity needs exact recurrence/projective closure.

Thus the missing pointwise finite-witness theorem cannot be replaced merely by compactness.

---

# 16. Finite Poisson/heat readers: exact negative theorem

Consider finitely many depths

\[
y_0,\dots,y_m
\]

and heat depths

\[
\tau_0,\dots,\tau_n.
\]

A typical reader is

\[
L_j f(\omega)
=
\int_I
K_j(\rho)f(\rho,\omega)\,d\rho
\]

on a fixed annulus \(I\Subset(0,\infty)\).

The output may retain the entire angular function \(\omega\mapsto L_jf(\omega)\).

Even then, finitely many depths are not injective on arbitrary smooth radial packets.

## Theorem 16.1

For any finite family of Poisson/heat readers, and any finite family of the same readers applied to \(\mathscr R_\sigma f\), there exists a nonzero smooth compactly supported packet \(g\) invisible to all of them.

### Proof

Let

\[
X=C_c^\infty(I)
\]

for the radial variable.

Each selected measurement gives a linear functional on \(X\). Measurements of \(\mathscr R_\sigma g\) are also linear functionals of \(g\).

Hence altogether we obtain finitely many linear functionals

\[
\ell_1,\dots,\ell_N:X\to\mathbb C.
\]

Since \(X\) is infinite-dimensional,

\[
\bigcap_{j=1}^N\ker\ell_j
\]

has nonzero elements.

Choose

\[
0\ne g_0
\]

in this intersection.

Choose any nonzero angular profile \(\phi(\omega)\), and define

\[
g(\rho,\omega)=g_0(\rho)\phi(\omega).
\]

Then for every chosen radial kernel \(K_j\),

\[
\int K_j(\rho)g(\rho,\omega)\,d\rho
=
\phi(\omega)\ell_j(g_0)
=0.
\]

Thus the entire angular output vanishes.

Likewise all selected measurements of \(\mathscr R_\sigma g\) vanish.

Finally,

\[
\mathscr R_\sigma g\neq0.
\]

Otherwise \(g_0\) would be a compactly supported homogeneous solution. But all homogeneous solutions are multiples of \(h_\sigma\), which is nowhere compactly supported unless the coefficient vanishes. Hence \(g_0=0\), contradiction.

Thus a nonzero exactly absorbable packet is invisible to every finite reader. \(\square\)

---

# 17. Compactness does not rescue finite-depth injectivity

This can be demonstrated in the strongest elementary manner.

Let \(L\) denote any fixed finite reader map and choose

\[
0\neq g\in\ker L.
\]

Take arbitrary \(f_0\) and consider

\[
K_0
=
\{f_0+t g:0\le t\le1\}.
\]

This is compact.

Yet

\[
L(f_0+t g)=L(f_0)
\]

for every \(t\).

Hence:

\[
\boxed{
\text{compactness}
\not\Rightarrow
\text{finite-reader injectivity}.
}
\tag{17.1}
\]

So Problem C cannot be derived from compactness alone.

---

# 18. What the Vandermonde determinant does prove

Suppose one already knows that near \(\rho_0\),

\[
f(\rho_0+s)
=
\sum_{r=0}^m c_rs^r
\]

with no unknown higher-order remainder.

Then

\[
e^{-y_j(\rho_0+s)}
=
e^{-y_j\rho_0}
\sum_{r=0}^m
\frac{(-y_j)^r}{r!}s^r+\cdots.
\]

The coefficient matrix is

\[
V_{jr}=e^{-y_j\rho_0}(-y_j)^r.
\]

Its determinant is

\[
\det V
=
e^{-\rho_0\sum_jy_j}
\prod_{i<j}(y_j-y_i)
\]

up to a nonzero sign/factorial normalization.

Thus

\[
\det V\neq0.
\]

Therefore:

\[
\boxed{
m+1\text{ depths separate an }m\text{-jet}.
}
\]

They do not separate arbitrary smooth functions.

So the Vandermonde result is perfectly valid, but finite-dimensional.

---

# 19. Positive finite-depth theorem under a genuine finite-dimensional packet hypothesis

There is nevertheless a useful exact positive result.

## Theorem 19.1

Let \(X\) be a finite-dimensional space of radial packet profiles, \(\dim X=N\), supported in a fixed compact annulus.

Assume the full Poisson transform

\[
Tf(y)
=
\int
w(\rho)e^{-y\rho}f(\rho)\,d\rho
\]

is injective on \(X\), with \(w(\rho)\neq0\).

Then there exist at most \(N\) positive depths

\[
y_1,\dots,y_N
\]

such that

\[
f\mapsto
(Tf(y_1),\dots,Tf(y_N))
\]

is injective on \(X\).

### Proof

For each \(y>0\), define

\[
\ell_y(f)=Tf(y)\in\mathbb C.
\]

Suppose the linear span of

\[
\{\ell_y:y>0\}
\]

were a proper subspace of \(X^*\).

Then there would exist a nonzero \(f\in X\) annihilated by every \(\ell_y\):

\[
Tf(y)=0
\qquad\forall y>0.
\]

By injectivity of the full transform, \(f=0\), contradiction.

Hence the family \(\{\ell_y\}\) spans \(X^*\).

Because \(X^*\) is \(N\)-dimensional, one can choose \(N\) members

\[
\ell_{y_1},\dots,\ell_{y_N}
\]

forming a basis of \(X^*\).

Their joint evaluation map is injective. \(\square\)

Thus finite-depth semigroup closure is possible once a genuinely finite-dimensional packet class has independently been proved.

It is not a consequence of compactness alone.

---

# 20. The stationary positive-alignment issue must be stated carefully

Recall

\[
N=\gamma G+T,
\]

and

\[
Y=rG+R_{\rm fv},
\qquad
r=\frac{D_3}{d^2}.
\]

For any \(\lambda\),

\[
N-\lambda Y
=
(\gamma-\lambda r)G
+
(T-\lambda R_{\rm fv}).
\]

Since the two summands are \(H^{-1/2}\)-orthogonal,

\[
\|N-\lambda Y\|^2
=
\|T-\lambda R_{\rm fv}\|^2
+
d^2(\gamma-\lambda r)^2.
\]

Using

\[
\gamma d^2=\frac W2,
\qquad
rd^2=D_3,
\]

we obtain

\[
\boxed{
\|N-\lambda Y\|^2
=
\|T-\lambda R_{\rm fv}\|^2
+
\frac{(W/2-\lambda D_3)^2}{d^2}.
}
\tag{20.1}
\]

Therefore:

## Lemma 20.1

If

\[
T=\lambda R_{\rm fv},
\]

then

\[
N=\lambda Y
\]

if and only if

\[
\boxed{
W=2\lambda D_3.
}
\tag{20.2}
\]

For a stationary finite-\(\kappa\) profile,

\[
W=2\kappa D_3,
\]

hence necessarily

\[
\lambda=\kappa.
\]

So the stationary equations directly test

\[
\boxed{
T=\kappa R_{\rm fv},
}
\]

not arbitrary positive alignment \(T=\lambda R_{\rm fv}\).

To exclude every \(\lambda>0\), the finite-loop theorem itself must apply to the entire positive-alignment stratum, independently of stationarity.

That is a separate assumption.

---

# 21. Holonomy contradiction theorem

Now suppose CRPC has been established and suppose the physical nonflatness theorem has also been established.

Let \(P\subset K\) denote the forbidden candidate set.

Assume:

\[
v\in P
\Longrightarrow
\text{global channel consistency forces }
\operatorname{Hol}_{\Gamma_v}(v)=1,
\tag{21.1}
\]

while finite physical geometry gives

\[
|\operatorname{Hol}_{\Gamma_v}(v)-1|>0.
\tag{21.2}
\]

Then no \(v\in P\) exists.

This is immediate:

\[
1
=
\operatorname{Hol}_{\Gamma_v}(v)
\neq1.
\]

\(\square\)

For stationary candidates,

\[
P_{\rm stat}
=
\{v:T(v)=\kappa R_{\rm fv}(v)\}.
\]

Thus a valid nonflatness theorem proves

\[
\boxed{
T(v)\neq\kappa R_{\rm fv}(v).
}
\tag{21.3}
\]

Since an actual stationary state satisfies equality, it follows that there is no nonzero stationary profile in the nonexceptional class.

---

# 22. Direct quantitative transverse gap by compactness

The norm gap actually requires less than an angle theorem.

Because

\[
R_{\rm fv}(v)=0\Longrightarrow v=0
\]

and

\[
E(v)=1,
\]

we have

\[
R_{\rm fv}(v)\neq0
\]

throughout the normalized class.

Assume

\[
T(v)\neq\kappa(v)R_{\rm fv}(v)
\qquad
\forall v\in K.
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
\tag{22.1}
\]

The denominator is positive.

By continuity,

\[
\Psi:K\to(0,\infty)
\]

is continuous.

Compactness gives

\[
\eta_K
=
\min_{v\in K}\Psi(v)>0.
\]

Therefore

\[
\boxed{
\|T(v)-\kappa R_{\rm fv}(v)\|_{H^{-1/2}}
\ge
\eta_K
\left(
\|T(v)\|_{H^{-1/2}}
+
\kappa\|R_{\rm fv}(v)\|_{H^{-1/2}}
\right).
}
\tag{22.2}
\]

This is already the desired transverse saturation gap.

It requires no Fourier cutoff, mode-count bound or higher Sobolev constant.

\(\square\)

---

# 23. Uniform angular separation

For the stronger angular conclusion we need

\[
T(v)\neq0
\]

as well as

\[
R_{\rm fv}(v)\neq0.
\]

Assume both are nonzero on compact \(K\), and assume

\[
T(v)\neq\lambda R_{\rm fv}(v)
\qquad
\forall \lambda>0.
\tag{23.1}
\]

Define

\[
q(v)
=
\frac{
\langle T(v),R_{\rm fv}(v)\rangle_{H^{-1/2}}
}{
\|T(v)\|_{H^{-1/2}}
\|R_{\rm fv}(v)\|_{H^{-1/2}}
}.
\]

Then \(q\) is continuous.

Cauchy–Schwarz gives

\[
q(v)\le1.
\]

Equality \(q(v)=1\) occurs precisely when

\[
T(v)=\lambda R_{\rm fv}(v)
\]

with \(\lambda>0\).

By (23.1),

\[
q(v)<1
\]

for all \(v\).

Compactness yields

\[
q_*=\max_Kq<1.
\]

Set

\[
\boxed{
\theta_K=\arccos q_*>0.
}
\]

Then

\[
\boxed{
\angle(T(v),R_{\rm fv}(v))
\ge\theta_K.
}
\tag{23.2}
\]

\(\square\)

---

# 24. Exact angle/gain inequality

Let

\[
A=\|T\|,
\qquad
B=\kappa\|R_{\rm fv}\|,
\qquad
\theta=\angle(T,R_{\rm fv}).
\]

Then

\[
\|T-\kappa R_{\rm fv}\|^2
=
A^2+B^2-2AB\cos\theta.
\]

If

\[
\theta\ge\theta_K,
\]

then

\[
\cos\theta\le\cos\theta_K=:c.
\]

Hence

\[
\|T-\kappa R_{\rm fv}\|^2
\ge
A^2+B^2-2ABc.
\]

Set

\[
s
=
\sin\frac{\theta_K}{2}.
\]

Since

\[
s^2=\frac{1-c}{2},
\]

we calculate

\[
\begin{aligned}
&A^2+B^2-2ABc
-
s^2(A+B)^2
\\
&=
A^2+B^2-2ABc
-\frac{1-c}{2}(A^2+2AB+B^2)
\\
&=
\frac{1+c}{2}(A-B)^2
\ge0.
\end{aligned}
\]

Therefore

\[
\boxed{
\|T-\kappa R_{\rm fv}\|
\ge
\sin\left(\frac{\theta_K}{2}\right)
\left(
\|T\|+\kappa\|R_{\rm fv}\|
\right).
}
\]

Thus

\[
\boxed{
\eta_K
=
\sin\left(\frac{\theta_K}{2}\right)>0.
}
\tag{24.1}
\]

\(\square\)

---

# 25. Relation to the finite-network theorem already present in Part I

Part I states that for a genuinely finite completed nonexceptional network,

\[
T=\lambda R_{\rm fv},
\qquad
\lambda>0,
\]

is impossible.

That is already a finite-network rigidity theorem.

But it does **not** automatically give the PDE theorem.

To pass from an infinite/continuum state to that finite theorem, one would need:

\[
\boxed{
\textbf{Finite Witness Extraction (FWE)}
}
\]

meaning:

> Whenever a normalized PDE state \(v\in K\) satisfies the forbidden positive-alignment condition, there exists a finite reality-complete, nonexceptional, channel-resolved subnetwork whose inherited state data satisfy the same exact saturation compatibility.

If FWE were available, Part I's finite-network theorem would immediately produce a contradiction.

Indeed:

\[
T=\lambda R_{\rm fv}
\]

globally

\[
\overset{\mathrm{FWE}}{\Longrightarrow}
\]

a finite completed nonexceptional saturation network,

contradicting the established finite-network theorem.

Thus

\[
T\neq\lambda R_{\rm fv}.
\]

Compactness then gives the quantitative gap as above.

So FWE is an alternative formulation of the missing bridge.

---

# 26. Why FWE does not follow automatically from ordinary compactness

An infinite interaction network may export forever:

\[
\Gamma_1
\subset
\Gamma_2
\subset
\Gamma_3
\subset\cdots
\]

with each finite stage having open companion outputs feeding the next stage.

Every finite subsystem then fails to be a closed completed network.

Taking a Fourier cutoff would artificially close it—but that is exactly forbidden.

Similarly, compactness of the state can imply subsequential convergence of packets or parameters, but this gives approximate rather than exact recurrence.

The finite-network theorem requires exact completion.

Hence

\[
\boxed{
\text{compactness}
+
\text{finite-network rigidity}
\not\Rightarrow
\text{PDE rigidity}
}
\]

without a finite-witness extraction principle.

This is why the completion-depth issue is genuinely substantive.

---

# 27. The precise corrected theorem that closes the program

We can now state the final theorem in its mathematically valid form.

## Corrected Finite Companion Holonomy Rigidity Theorem

Let \(K\) be a compact normalized finite-\(\kappa\) Theory-2 class satisfying the quantitative nonexceptionality assumptions.

Assume additionally:

### (H1) Channel-resolved projective closure

Every finite witness interaction can be decomposed into one-dimensional channels satisfying CRPC.

### (H2) Exact candidate consistency

For every forbidden saturation candidate, the channel amplitudes satisfy the multiplicative edge relations

\[
a_r=h_ea_pa_q.
\]

### (H3) Pointwise finite physical nonflatness

For every forbidden candidate \(v\), there exists a finite reality-complete physical incidence cycle \(\Gamma_v\) for which

\[
|\operatorname{Hol}_{\Gamma_v}(v)-1|>0.
\]

### (H4) Local continuity

For each witness \(\Gamma_v\), its holonomy remains defined and depends continuously on the state on a neighborhood of \(v\).

Then:

\[
\boxed{
\text{there exist finitely many witnesses }
\Gamma_1,\dots,\Gamma_N
}
\]

and

\[
\boxed{
c_K>0
}
\]

such that every forbidden candidate satisfies

\[
\boxed{
\max_j
|\operatorname{Hol}_{\Gamma_j}-1|
\ge c_K.
}
\]

But exact candidate consistency gives

\[
\operatorname{Hol}_{\Gamma_j}=1
\]

on every applicable closed cycle.

Therefore no forbidden candidate exists.

In particular, in the stationary case,

\[
\boxed{
T(v)\neq\kappa R_{\rm fv}(v)
\qquad
\forall v\in K.
}
\]

Consequently there exists

\[
\boxed{
\eta_K>0
}
\]

such that

\[
\boxed{
\|T-\kappa R_{\rm fv}\|_{H^{-1/2}}
\ge
\eta_K
\left(
\|T\|_{H^{-1/2}}
+
\kappa\|R_{\rm fv}\|_{H^{-1/2}}
\right).
}
\]

If the hypotheses are strengthened so that all positive proportionalities

\[
T=\lambda R_{\rm fv},
\quad \lambda>0
\]

are excluded and both vectors are uniformly nonzero, then

\[
\boxed{
\angle(T,R_{\rm fv})\ge\theta_K>0
}
\]

and one may take

\[
\boxed{
\eta_K
=
\sin\left(\frac{\theta_K}{2}\right).
}
\]

### Proof

- H1 gives well-defined scalar edge gains \(h_e\).
- Theorem 11.1 gives gauge-invariant finite holonomy.
- H2 and Theorem 12.1 give
  \[
  \operatorname{Hol}_\Gamma=1
  \]
  on every exact candidate loop.
- H3 gives, pointwise, a finite loop with nonzero defect.
- H4 and compactness, via Theorem 14.1, produce finitely many loops and a uniform \(c_K>0\).
- This contradicts exact candidate consistency.
- Hence the forbidden saturation set is empty.
- The continuous normalized residual \(\Psi\) from (22.1) is strictly positive on compact \(K\), giving \(\eta_K>0\).
- Under uniform nonvanishing and exclusion of every positive proportionality, Theorems 23–24 yield the angular estimate.

\[
\boxed{\mathrm{QED}}
\]

---

# 28. What remains genuinely unproved from the original axioms

At this point every analytic and compactness step is closed.

The unresolved content has been reduced to exactly two physical statements:

\[
\boxed{
\textbf{(A) Channel/Fiber Closure}
}
\]

Prove directly from actual Curl–Killing/Navier–Stokes geometry that the relevant absorbed companion channels can be followed projectively from one incidence into the next **before additive mixing destroys edge identity**.

And

\[
\boxed{
\textbf{(B) Pointwise Finite Nonflatness / Finite Witness Extraction}
}
\]

Prove that every putative positive saturation candidate contains a finite, exact, nonexceptional physical witness whose projective transfer is incompatible with flat holonomy.

Neither statement follows from:

\[
2B(a_x,b_y)
=(x-y)P(b_y\times a_x),
\]

rank-one alone,

\[
\chi_\sigma>0,
\]

radial coercivity,

or finite semigroup moments.

That is now a theorem-level diagnosis, not a heuristic one.

---

# 29. Final QED status of the original Olympiad

The original requested implication was

\[
\boxed{
\text{finite companion/rank-one geometry}
\Longrightarrow
\text{transverse saturation gap}.
}
\]

The rigorous result is:

\[
\boxed{
\begin{aligned}
&\text{rank-one geometry}
\\
&\quad+\text{edgewise radial absorption}
\\
&\quad+\text{reality completion}
\\
&\quad+\text{finite Poisson/heat depths}
\\
&\not\Longrightarrow
\text{a nontrivial finite holonomy defect}.
\end{aligned}
}
\]

The missing bridge is precisely

\[
\boxed{
\text{channel-resolved state-incidence closure}
+
\text{finite physical nonflat witness}.
}
\]

Once those two statements are proved,

\[
\boxed{
\begin{gathered}
\text{finite physical witness}\\
\Downarrow\\
\text{nonflat projective holonomy}\\
\Downarrow\\
\text{contradiction with exact saturation consistency}\\
\Downarrow\\
T\neq\kappa R_{\rm fv}\\
\Downarrow\\
\|T-\kappa R_{\rm fv}\|
\ge
\eta_K(\|T\|+\kappa\|R_{\rm fv}\|),
\end{gathered}
}
\]

and, under the stronger positive-alignment hypotheses,

\[
\boxed{
\angle(T,R_{\rm fv})\ge\theta_K>0.
}
\]

That closes every part of the argument that follows from the formal frontier and identifies, with no remaining ambiguity, the exact new theorem that must be established to complete the physical Theory-2 program.