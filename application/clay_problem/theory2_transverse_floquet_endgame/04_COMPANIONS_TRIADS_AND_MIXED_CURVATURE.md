# 04 — Physical companions, triads, and mixed Poisson–heat curvature

## 1. Reality supplies a physical sum–difference pair

For two noncollinear unequal-root helical atoms at frequencies `p,m`,

\[
Ca=x a,
\qquad
Cb=y b,
\qquad
x\ne y,
\]

polarized Curl–Killing gives

\[
\boxed{
2B(a_x,b_y)=(x-y)P(b_y\times a_x)\ne0.
}
\]

Reality supplies both outputs

\[
\boxed{p+m,\qquad p-m.}
\]

Therefore an isolated projected triad which deletes one of these outputs is not faithful to the full physical equation.

If one companion output is absent and no other physical incidence cancels it, then at that mode

\[
G=0,
\qquad
T=N\ne0.
\]

So exact single-triad saturation in a projected model is a truncation artifact.

---

## 2. Exact radial heat defect of companions

The real pair obeys

\[
\boxed{
(|p+m|^2-|p|^2)+(|p-m|^2-|p|^2)=2|m|^2.
}
\]

Hence at least one real companion has an `O(|m|^2)` radial heat defect.

A hidden interaction must therefore generate at least one of:

- radial heat-visible transfer;
- support leakage;
- overlap cancellation by another physical incidence.

Persistent invisibility forces a nontrivial overlap network.

---

## 3. Finite Poisson + heat depths separate radial overlap classes

Suppose several physical incidences cancel at one output:

\[
\sum_jc_j=0.
\]

At an empty output `k`,

\[
(\Pi_y(u)u)_k
=-\sum_j e^{-y(|p_j|+|m_j|)}c_j,
\]

and

\[
(\mathcal C_\tau(u)u)_k
=-\sum_j e^{-\tau(|p_j|^2+|m_j|^2)}c_j.
\]

If cancellation survives all Poisson depths, it occurs separately inside fixed

\[
|p_j|+|m_j|.
\]

If it also survives all heat depths, it occurs separately inside fixed

\[
|p_j|^2+|m_j|^2.
\]

These two invariants determine the unordered pair of parent radii. The complete signed curl flag further separates signed-root classes.

Thus the unresolved all-depth kernel is purely angular equal-spectral-data cancellation.

---

## 4. Mixed Poisson–heat commuting square

Because

\[
P_yH_\tau=H_\tau P_y,
\]

the existing cocycles satisfy the exact square identity

\[
\boxed{
H_\tau\Pi_y(u)-\Pi_y(H_\tau u)H_\tau
=
P_y\mathcal C_\tau(u)-\mathcal C_\tau(P_yu)P_y.
}
\]

Call this existing composite

\[
\mathscr R_{y,\tau}(u).
\]

It is not a new ontology.

For an incidence with

\[
r=|p|,
\qquad
s=|\eta|,
\qquad
c=|p+\eta|,
\]

define forward/reverse Poisson defects

\[
a_+=e^{-yc}-e^{-y(r+s)},
\]

\[
a_-=e^{-yr}-e^{-y(c+s)},
\]

and heat defects

\[
b_+=e^{-\tau c^2}-e^{-\tau(r^2+s^2)},
\]

\[
b_-=e^{-\tau r^2}-e^{-\tau(c^2+s^2)}.
\]

Then exactly

\[
\boxed{a_+b_++a_-b_->0}
\]

for every

\[
s>0,
\qquad
y,\tau>0.
\]

So the physical forward/reverse mixed curvature has no nonzero characteristic.

---

## 5. Infinitesimal mixed curvature

Let

\[
\delta_+=r+s-c,
\qquad
\delta_-=c+s-r,
\]

\[
q_+=r^2+s^2-c^2,
\qquad
q_-=c^2+s^2-r^2.
\]

Then

\[
\boxed{
\delta_+q_++\delta_-q_-
\ge2s^3.
}
\]

More precisely, put

\[
x=r-c.
\]

Then exactly

\[
\boxed{
\delta_+q_++\delta_-q_-
=2s^3+2(r-c)^2(r+c).
}
\]

and

\[
\boxed{
\delta_+q_+-\delta_-q_-
=2s(r-c)(r+c+s).
}
\]

Thus the paired infinitesimal curvature decomposes into a strictly positive symmetric conductance plus a directed radial part.

The antisymmetric part is an exact pair-potential drop. With

\[
\Psi(a,b)=ab(a+b),
\]

\[
\boxed{
s(r-c)(r+c+s)=\Psi(r,s)-\Psi(c,s).
}
\]

Therefore any positive conserved circulation on the radius-pair graph telescopes the antisymmetric part and retains the positive `s^3` core.

---

## 6. Actual-state critical contraction of mixed curvature

Define

\[
\boxed{
\mathcal P_{y,\tau}(u)
=\operatorname{Re}\langle u,[\Lambda,\mathscr R_{y,\tau}(u)]u\rangle.
}
\]

For one physical forward/reverse edge, let

\[
j_e
=\operatorname{Re}\langle u_k,(J_{u_\eta}u_p)_k\rangle.
\]

The edge critical work is

\[
W_e=2(c-r)j_e.
\]

Skewness supplies the reverse edge, and the combined curvature reader is

\[
\boxed{
(\mathcal P_{y,\tau})_e
=\frac{a_+b_++a_-b_-}{2}
W_e.
}
\]

Thus every physical reverse pair has the same critical orientation under the finite mixed-curvature reader.

This is the correct “sum before square” contraction at the edge level.

---

## 7. Complete mixed-helicity triads preserve curvature sign

For signed roots

\[
+a,
\qquad
+b,
\qquad
-c,
\]

the critical determinant is

\[
\Theta=2c(b-a).
\]

For the infinitesimal mixed curvature define the edge conductance

\[
\mu(r,c;s)
=s^3+(r-c)^2(r+c).
\]

After summing all three physical edges of one complete mixed-helicity triad, the cyclic identities collapse to

\[
\boxed{
\mathcal P_{{\rm PH},{\rm tri}}
=\mu_{ab|c}\,W_{{\rm tri}},
}
\]

where

\[
\boxed{
\mu_{ab|c}=c^3+(a-b)^2(a+b)>0.
}
\]

Therefore

\[
\boxed{
\operatorname{sgn}\mathcal P_{{\rm PH},{\rm tri}}
=\operatorname{sgn}W_{{\rm tri}}.
}
\]

If all three roots have the same sign, both quantities vanish.

So neither an individual physical reverse pair nor a complete mixed-helicity triad is the remaining static sign obstruction.

---

## 8. Exact inter-triad countercondition

Globally,

\[
W_\Lambda=\sum_{\mathfrak t}W_{\mathfrak t},
\]

while

\[
\mathcal P_{\rm PH}
=\sum_{\mathfrak t}\mu_{\mathfrak t}W_{\mathfrak t},
\qquad
\mu_{\mathfrak t}>0.
\]

If

\[
W_\Lambda>0
\]

but

\[
\mathcal P_{\rm PH}\le0,
\]

then positive and negative triads must coexist. Let

\[
W_+=\sum_{W_{\mathfrak t}>0}W_{\mathfrak t},
\qquad
W_-=\sum_{W_{\mathfrak t}<0}|W_{\mathfrak t}|,
\]

and define their curvature barycentres `\bar μ_±`. Then necessarily

\[
\boxed{
\frac{\bar\mu_-}{\bar\mu_+}
\ge
\frac{W_+}{W_-}>1.
}
\]

So a wrong global curvature sign requires negative critical creation to live at a strictly larger average mixed-curvature scale than the positive creation.

The remaining static obstruction is therefore inter-triad cross-spectral sign anti-correlation.

---

## 9. Exact hostile pointwise counterexample

A universal pointwise curvature sign theorem is false.

Take one finite physical mixed triad with positive critical work `W_1>0`. Take a rotated/dilated nonresonant copy at scale `L>1`, reverse its phase, and choose its amplitude so that its critical work is

\[
W_2=-qW_1,
\qquad
L^{-3}<q<1.
\]

Then

\[
W=(1-q)W_1>0,
\]

while because the curvature weight scales cubically,

\[
\mathcal P_{\rm PH}
=\mu_1W_1(1-qL^3)<0.
\]

Scale the whole state by `α` and choose

\[
\alpha=\frac{2\nu D_3(v)}{W(v)}.
\]

Then

\[
\boxed{M'=0,\qquad W>0,\qquad\mathcal P_{\rm PH}<0.}
\]

This is an exact smooth finite-Fourier physical state, not a Galerkin deletion.

Therefore finite time is essential. No instantaneous mixed-curvature scalar closes Navier–Stokes passivity.

---

## 10. Skinny high–high–low complementarity

For a mixed-helicity triad `+a,+b,-c`, set

\[
S=a+b,
\qquad
d=|a-b|,
\qquad
\varepsilon=\frac cS,
\qquad
\delta=\frac dS.
\]

Strict triangle geometry gives

\[
0\le\delta<\varepsilon<1.
\]

Let

\[
\mathsf Q=a^2+b^2+c^2.
\]

Then exactly

\[
\frac{\mathsf Q}{S^2}
=\frac{1+\delta^2}{2}+\varepsilon^2,
\]

\[
\frac{\mu}{S^3}
=\varepsilon^3+\delta^2,
\]

and

\[
\frac{|\Theta|}{S^2}=2\varepsilon\delta.
\]

Hence

\[
\boxed{
\frac{\mu}{\mathsf Q^{3/2}}\to0
\iff
\varepsilon\to0
\iff
a\sim b\gg c.
}
\]

This is the skinny infrared-mediated high–high–low regime.

The real high companion can become weak there; its power ratio relative to the main low output behaves as

\[
\boxed{
\frac{G_\Delta}{G_\Sigma}\sim2\varepsilon^2.
}
\]

But the cubic-stock creation factor satisfies

\[
\boxed{
\frac{\varrho_3}{\mathsf Q}\to\infty.
}
\]

Thus:

\[
\boxed{
\text{weak companion leakage}
\iff
\text{weak normalized mixed curvature}
\iff
\text{strong cubic-stock amplification}.
}
\]

This three-channel complementarity sharply classifies the only degeneration of relative companion strength.

---

## 11. Status

### EXACT

Physical companions, paired curvature positivity, edge reader, complete-triad sign preservation, inter-triad countercondition, skinny complementarity.

### NO-GO

A universal pointwise scalar mixed-curvature sign theorem is false, even at exact instantaneous critical neutrality.

### OPEN

The remaining problem is finite-step redistribution among oppositely signed complete triads and the transverse physical network that repopulates their spectral classes.
