# 10 — Output-frequency null form and scale genealogy

This chapter records the exact locality statement that prevents arbitrary long-range spectral recruitment from being treated as a free control.

## 1. Exact output-frequency null form

Let `a_p,b_q` be divergence-free polarized Fourier atoms at frequencies `p,q`, and let

\[
k=p+q.
\]

The symmetric Euler Formation bilinear term is

\[
2B(a_p,b_q)
=-P\big((a_p\cdot\nabla)b_q+(b_q\cdot\nabla)a_p\big).
\]

At output `k`,

\[
2B(a_p,b_q)_k
=-iP_k
\left[(a_p\cdot q)b_q+(b_q\cdot p)a_p\right].
\]

Since

\[
a_p\cdot p=0,
\qquad
b_q\cdot q=0,
\]

and `k=p+q`,

\[
a_p\cdot q=a_p\cdot k,
\qquad
b_q\cdot p=b_q\cdot k.
\]

Therefore

\[
\boxed{
2B(a_p,b_q)_k
=-iP_k
\left[(a_p\cdot k)b_q+(b_q\cdot k)a_p\right].
}
\]

Hence

\[
\boxed{
|B(a_p,b_q)_k|
\le |k|\,|a_p|\,|b_q|.
}
\]

This is **EXACT**.

The derivative in the complete physical bilinear interaction can be read as an output derivative. A high-high interaction landing at low frequency is therefore suppressed by the low output scale rather than carrying a naked high-parent derivative.

Polarized Curl–Killing and the helical geometric suppression of high-high-to-low interactions are compatible realizations of this same complete physical null form.

---

## 2. Far UV cannot directly exert order-one forcing on a fixed IR module

Let `v` be divergence-free on `R^3`. From the output null form,

\[
|\widehat{N(v)}(k)|
\lesssim
|k|\,\|v\|_2^2.
\]

Therefore for a fixed low-output ball,

\[
\begin{aligned}
\|P_{\le K}N(v)\|_{\dot H^{-1/2}}^2
&\lesssim
\int_{|k|\le K}
|k|^{-1}|k|^2\|v\|_2^4\,dk
\\
&\lesssim K^4\|v\|_2^4.
\end{aligned}
\]

Thus

\[
\boxed{
\|P_{\le K}N(v)\|_{\dot H^{-1/2}}
\lesssim K^2\|v\|_2^2.
}
\]

Now suppose one parent lies above `L` while the output is below `K`, with

\[
L\ge2K.
\]

Then the other parent is automatically above `L/2`. Hence every such contribution is high-high.

Taking

\[
v=P_{>L/2}u
\]

gives the far-UV contribution bound

\[
\boxed{
\|P_{\le K}N_{\rm far}(u)\|_{\dot H^{-1/2}}
\lesssim
K^2\|P_{>L/2}u\|_2^2.
}
\]

Since

\[
\|P_{>L/2}u\|_2^2
\le\frac{2M(u)}{L},
\]

we obtain

\[
\boxed{
\|P_{\le K}N_{\rm far}(u)\|_{\dot H^{-1/2}}
\lesssim
\frac{K^2}{L}M(u).
}
\]

This is a **DEDUCTION** from the exact output-null identity plus the critical norm bound.

At fixed normalized `K`, direct remote UV-to-IR Formation forcing vanishes as `L→∞`.

---

## 3. Remote ultraviolet scales cannot be created without ancestry

If both parents lie below `K`, then

\[
|p+q|\le2K.
\]

Therefore

\[
\boxed{
P_{>2K}N(P_{\le K}u)=0.
}
\]

This is **EXACT**.

Thus a genuinely new scale above `2K` requires at least one parent already above `K`.

Combining Sections 2 and 3:

\[
\boxed{
\text{physical Formation recruitment is genealogically local in log-frequency.}
}
\]

There is neither direct full-strength remote UV-to-IR forcing nor spontaneous creation of arbitrarily remote UV scales from a compact low-frequency core.

---

## 4. Relation to bounded spectral modules

The bounded-module theorem says that arbitrary internal skew dynamics in

\[
[\rho,R\rho]
\]

is critically contractive after a finite viscous horizon.

To defeat that contraction, the trajectory must obtain external Formation forcing from outside the current module.

The genealogy theorem now says that this external forcing cannot repeatedly skip arbitrarily many dyadic generations at full strength.

Thus a persistent regenerative ancestry is forced into a chained structure schematically of the form

\[
\cdots
\longrightarrow
2^{-1}K
\longrightarrow
K
\longrightarrow
2K
\longrightarrow
4K
\longrightarrow\cdots.
\]

This is not a scalar traffic model. It is a consequence of exact physical convolution support plus the output-frequency null form.

---

## 5. Relation to `T`

For each signed curl eigenspace,

\[
\dot u_x=\ell_xu_x+T_x.
\]

The commuting scalar part cannot create a new projective signed-root direction. Therefore the genealogical recruitment needed to keep invalidating the current coercive module must be realized by transverse Formation.

The dangerous portion of `T` is therefore not merely large `T`; it is **module-expanding `T`**.

---

## 6. Relation to the skinny infrared branch

The high-high-low degeneration

\[
a\sim b\gg c
\]

is the opposite endpoint of the same locality picture.

After normalizing by the high carrier scale, the low mediator satisfies

\[
\frac{c}{a+b}\to0.
\]

At that boundary:

- the low output derivative suppresses direct high-high-to-low Formation;
- relative real companion strength can vanish;
- a single skinny triad becomes critically inefficient;
- bounded critical Reynolds requires diverging incidence complexity;
- the finite-Reynolds Floquet monodromy develops its critical infrared translation characteristic.

Thus skinny beat ancestry and normalized infrared Floquet degeneracy are two views of the same terminal boundary.

---

## 7. What this theorem removes

The remaining endgame does **not** have to control an arbitrary all-to-all spectral control system.

The physical equation forbids that abstraction.

Any persistent module-expanding countermechanism must instead organize a locally chained, transverse, actual-state Formation ancestry across logarithmic scales.

This is a substantial structural reduction.

---

## 8. What remains open

The locality theorem does not show that an infinite adjacent-scale ancestry is impossible.

At the critical scaling, Formation and heat both operate on the local `K^2` time scale, so an adjacent-scale chain can in principle advance geometrically in physical frequency while remaining `O(1)` in normalized Formation time.

That possibility is exactly what the transverse Floquet fixed-point theorem must exclude or classify as genuine radiation.

Status: **OPEN beyond the exact locality statements above.**
