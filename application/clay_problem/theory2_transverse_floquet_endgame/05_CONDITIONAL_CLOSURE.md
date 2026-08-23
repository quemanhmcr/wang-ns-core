# 05 — Conditional closure theorem

This file proves the entire downstream argument assuming the OPEN physical bridge from `04_OPEN_FRONTIER.md`.

Nothing in this file claims CRPC, exact channel inheritance, or finite nonflat witnesses have already been derived from the current Theory-2 axioms.

---

## Hypotheses

Let \(K\) be a compact normalized finite-\(\kappa\) class satisfying the hypotheses of `00_DEFINITIONS_AND_HYPOTHESES.md`.

Assume:

### (H1) Channel-resolved projective closure

Every witness edge carries a nonzero scalar gain \(h_e\) induced by CRPC:

\[
\iota_e\mathcal S_eB_e(\psi_p,\psi_q)=h_e\psi_r.
\]

### (H2) Exact candidate channel consistency

For every forbidden stationary saturation candidate, the inherited channel amplitudes satisfy

\[
\boxed{a_r=h_ea_pa_q}
\]

along each edge of the selected witness cycle.

### (H3) Pointwise finite nonflatness

For every

\[
v\in P_{\rm stat}:=\{v\in K:T(v)=\kappa(v)R_{\rm fv}(v)\},
\]

there exists a finite physical incidence cycle \(\Gamma_v\) such that

\[
\boxed{|\operatorname{Hol}_{\Gamma_v}(v)-1|>0.}
\]

### (H4) Local continuity

Each witness loop remains defined and its holonomy is continuous on a neighborhood of its base state.

---

## Theorem 1 — Exact candidate consistency forces flat holonomy

Let a finite incidence cycle be represented by integers \(n_e\) satisfying

\[
\sum_en_e([p_e]+[q_e]-[r_e])=0.
\]

Under H1–H2,

\[
\boxed{\operatorname{Hol}_n=1.}
\]

### Proof

By H2,

\[
h_e=\frac{a_{r_e}}{a_{p_e}a_{q_e}}.
\]

Therefore

\[
\operatorname{Hol}_n
=
\prod_e
\left(
\frac{a_{r_e}}{a_{p_e}a_{q_e}}
\right)^{n_e}.
\]

The exponent of every vertex amplitude is the negative of its coefficient in the incidence sum, hence zero. All amplitudes cancel. ∎

---

## Theorem 2 — Pointwise nonflatness excludes stationary saturation

Under H1–H3,

\[
\boxed{P_{\rm stat}=\varnothing.}
\]

Equivalently,

\[
\boxed{T(v)\neq\kappa(v)R_{\rm fv}(v)\qquad\forall v\in K.}
\]

### Proof

Assume \(v\in P_{\rm stat}\). H3 provides a finite witness \(\Gamma_v\) with

\[
|\operatorname{Hol}_{\Gamma_v}(v)-1|>0.
\]

But H1–H2 and Theorem 1 give

\[
\operatorname{Hol}_{\Gamma_v}(v)=1.
\]

Contradiction. ∎

Since every normalized stationary finite-\(\kappa\) state must satisfy

\[
T=\kappa R_{\rm fv},
\]

Theorem 2 excludes nonzero stationary states in the class \(K\).

---

## Theorem 3 — Compactness upgrades pointwise witnesses to a uniform finite family

Assume H3–H4 on a compact candidate set \(P\subseteq K\). Then there exist finitely many loops

\[
\Gamma_1,\dots,\Gamma_N
\]

and a constant

\[
c_K>0
\]

such that

\[
\boxed{
\max_{1\le j\le N}
|\operatorname{Hol}_{\Gamma_j}(v)-1|
\ge c_K
\qquad\forall v\in P.
}
\]

Moreover

\[
\boxed{L_K:=\max_j|\Gamma_j|<\infty.}
\]

### Proof

For each \(v\in P\), choose a witness \(\Gamma_v\) with defect

\[
d_v:=|\operatorname{Hol}_{\Gamma_v}(v)-1|>0.
\]

By continuity there is a neighborhood \(U_v\) on which the same witness satisfies defect at least \(d_v/2\). The \(U_v\) cover compact \(P\); choose a finite subcover. Taking the minimum of the finitely many positive local constants gives \(c_K>0\), and the maximum of the finitely many witness lengths gives \(L_K<\infty\). ∎

No Fourier cutoff, mode-count bound, shell-count bound, or a priori completion-depth bound enters this argument.

---

## Theorem 4 — Direct transverse saturation gap

Assume only the exact exclusion

\[
T(v)\neq\kappa(v)R_{\rm fv}(v)
\qquad\forall v\in K,
\]

with \(K\) compact and \(T,R_{\rm fv},\kappa\) continuous. Since

\[
R_{\rm fv}(v)\neq0
\]

on the normalized class, define

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
\]

Then \(\Psi\) is continuous and strictly positive on \(K\). Hence

\[
\eta_K:=\min_K\Psi>0,
\]

and

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

This is the preferred quantitative endpoint. It does not require \(T\neq0\).

---

## Theorem 5 — Optional angular gap

Assume in addition

\[
T(v)\neq0,
\qquad
R_{\rm fv}(v)\neq0,
\]

and exclude every positive proportionality

\[
T(v)\neq\lambda R_{\rm fv}(v)
\qquad(\lambda>0).
\]

Then compactness gives

\[
\boxed{
\angle(T(v),R_{\rm fv}(v))\ge\theta_K>0.
}
\]

Moreover

\[
\boxed{
\|T-\kappa R_{\rm fv}\|
\ge
\sin(\theta_K/2)
\left(
\|T\|+
\kappa\|R_{\rm fv}\|
\right).
}
\]

### Proof

Normalize the pairing

\[
q(v)=
\frac{\operatorname{Re}(T,R_{\rm fv})_{-1/2}}
{\|T\|_{-1/2}\|R_{\rm fv}\|_{-1/2}}.
\]

Exclusion of positive proportionality gives \(q(v)<1\). Compactness gives \(q_*<1\), hence \(\theta_K=\arccos q_*>0\). Finally, with \(A=\|T\|\), \(B=\kappa\|R_{\rm fv}\|\), and \(c=\cos\theta_K\),

\[
A^2+B^2-2ABc
-
\frac{1-c}{2}(A+B)^2
=
\frac{1+c}{2}(A-B)^2\ge0.
\]

∎

---

## Conditional QED chain

Under H1–H4,

\[
\boxed{
\begin{gathered}
\text{CRPC + exact channel inheritance}\\
\Downarrow\\
\text{genuine gauge-invariant finite holonomy}\\
\Downarrow\\
\text{exact saturation consistency forces }\operatorname{Hol}=1\\
\Downarrow\\
\text{pointwise finite nonflat witness gives }\operatorname{Hol}\neq1\\
\Downarrow\\
T\neq\kappa R_{\rm fv}\\
\Downarrow\\
\|T-\kappa R_{\rm fv}\|
\ge
\eta_K(\|T\|+\kappa\|R_{\rm fv}\|).
\end{gathered}
}
\]

Everything in this file is proved **conditional on H1–H4**. The only unproved physical content is isolated in `04_OPEN_FRONTIER.md`.