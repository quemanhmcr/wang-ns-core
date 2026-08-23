# 01 — Core Theory-2 state: curl flag, Poisson Formation, complete mothers

## 1. Curl-side state

Set

\[
C=\operatorname{curl},
\qquad
E_u=[\nabla_u,C].
\]

For each real shift `a`, define

\[
H_a=\operatorname{sgn}(C-aI),
\]

\[
A_a(u)=[\nabla_u,H_a],
\]

\[
O_a(u)=H_aA_a(u)-A_a(H_au).
\]

On the smooth mean-zero periodic class,

\[
\boxed{
O_a(u)\ \forall a
\iff
E_u
\iff
S(u)
\iff
u.
}
\]

This is the first complete Theory-2 equivalence: the full shifted curl flag is not an auxiliary diagnostic but a complete encoding of the velocity state through its deformation of curl geometry.

### Proof architecture

1. `E_u=[∇_u,C]` is equivalent to the symmetric deformation tensor because curl commutator with advection eliminates the pure rigid/Killing part.
2. The complete shifted-sign family `H_a` resolves the spectral flag of the fixed self-adjoint curl operator.
3. Commutators with all `H_a` determine the off-diagonal spectral action of `∇_u`; the polarized second commutator `O_a` removes gauge components.
4. On mean-zero periodic fields, the remaining Killing ambiguity is trivial, so the velocity is recovered.

The point is structural completeness, not a regularity estimate.

---

## 2. Poisson / Formation formulation

Define

\[
J_ub=P(b\times Cu),
\]

and

\[
N(u)=J_uu.
\]

The Navier–Stokes equation is

\[
\boxed{
u_t=J_uu-\nu C^2u.
}
\]

The operator `J_u` satisfies

\[
\boxed{J_u^*=-J_u}
\]

and the exact Curl–Killing null relation

\[
\boxed{J_u(Cu)=0.}
\]

Hence Formation is a skew Poisson motion in `L^2`, while viscosity is the positive self-adjoint `C^2` channel.

### Immediate conserved Euler pairings

For Euler (`ν=0`), skewness gives

\[
\langle u,N(u)\rangle=0.
\]

Using `J_u(Cu)=0`,

\[
\langle Cu,N(u)\rangle=0.
\]

Thus energy and helicity are exact Formation invariants.

---

## 3. The complete Poisson mother

Define

\[
K_u=[C,J_u].
\]

A direct computation gives

\[
\boxed{
K_ub=-2P(S(Cu)b).
}
\]

Hence

\[
\boxed{
K_u\iff S(Cu)\iff u.
}
\]

Moreover

\[
\boxed{K_u^*=K_u}
\]

because `C` is self-adjoint and `J_u` is skew-adjoint.

Finally,

\[
\boxed{CN=K_uu.}
\]

### Proof of `CN=K_uu`

Since

\[
K_uu=CJ_uu-J_uCu,
\]

and `J_u(Cu)=0`,

\[
K_uu=CJ_uu=CN(u).
\]

This identity is fundamental: the self-adjoint mother `K_u` turns the quadratic Formation vector into its exact curl derivative without introducing a new state species.

---

## 4. Critical modulus and critical work

Let

\[
\Lambda=|C|=HC,
\qquad
H=\operatorname{sgn}C.
\]

Define the critical stock

\[
M(u)=\langle u,\Lambda u\rangle.
\]

Its Euler Formation work is

\[
W_\Lambda=2\langle\Lambda u,N(u)\rangle.
\]

Using skewness,

\[
\boxed{
W_\Lambda
=\langle u,[\Lambda,J_u]u\rangle.
}
\]

Using `Λ=HC`, `CN=K_uu`, and self-adjointness,

\[
\boxed{
W_\Lambda=2\langle Hu,K_uu\rangle.
}
\]

Thus

\[
\boxed{
W_\Lambda
=2\langle\Lambda u,N\rangle
=\langle u,[\Lambda,J_u]u\rangle
=2\langle Hu,K_uu\rangle.
}
\]

This is the canonical critical scalar reader. It is applied only after the complete vector/operator Formation state has been retained.

---

## 5. Parity of the complete state

Under

\[
u\mapsto-u,
\]

linearity of `J_u` in the state argument gives

\[
J_{-u}=-J_u,
\]

but therefore

\[
N(-u)=J_{-u}(-u)=N(u).
\]

So the actual Formation vector is **even**.

Likewise actual-state Poisson and heat covariance vectors are even.

By contrast,

\[
W_\Lambda(-u)=-W_\Lambda(u).
\]

Therefore:

\[
\boxed{
\text{vector Formation observability is even, while critical orientation is odd.}
}
\]

This gives an exact no-go: no instantaneous scalar built only from even vector norms or even pairings can determine the sign of critical creation. An odd state reader is necessary.

---

## 6. Canonical odd Poisson reader

Let

\[
P_y=e^{-y\Lambda}.
\]

Define

\[
\chi_y(u)
=\langle P_yu,\Pi_y(u)u\rangle,
\]

where `Π_y` is introduced later in the covariance chapter.

Because

\[
\Pi_y(u)u=P_yN(u)-N(P_yu)
\]

and

\[
\langle P_yu,N(P_yu)\rangle=0,
\]

we obtain

\[
\boxed{
\chi_y(u)=\langle P_{2y}u,N(u)\rangle.
}
\]

Differentiating at `y=0`,

\[
\boxed{
W_\Lambda(u)=-\chi'_0(u).
}
\]

Thus the existing actual-state Poisson family already contains the minimal odd scalar reader needed to orient critical work.

---

## 7. What this chapter proves — and does not prove

### EXACT

- complete shifted-curl state equivalence;
- skew Poisson Formation representation;
- complete mother `K_u`;
- exact critical-work identities;
- even/odd parity split;
- canonical odd Poisson reader.

### NOT PROVED HERE

None of these identities gives a global sign for `W_Λ` or a finite-time Navier–Stokes return inequality. They decode the complete state and the correct scalar reader; the analytic coercivity problem appears only after physical overlap and finite time are included.
