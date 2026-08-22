# 02 — Analytic frontier and lessons

## Status ledger

### EXACT

- Mother/full-flag completeness on the stated smooth normalized class.
- Anchored interaction-frame identities
  \[
  v_t=-\nu(C^\sharp)^2v,
  \quad C^\sharp_t=U^*E_uU,
  \quad (H_a^\sharp)_t=U^*A_aU.
  \]
- Critical metric law and normalized spectral-probability law.
- Finite \(L_t^2\mathfrak M_0\) Mother action from kinetic viscosity.
- Shifted-flag half-derivative identity.
- Exact zero flag motion is rigid: if \(A_a(u)=0\) for a.e. \(a\), then \(E_u=0\), hence \(u=0\) modulo the known Killing sector.

### DEDUCTION / interpretation

At a heat scale \(K\), a dangerous state must move spectral mass outward on time \(\sim K^{-2}\) fast enough to defeat the positive operator \(\nu(C^\sharp)^2\). This motivates the language

\[
\text{adiabatic heat decay}
\quad\vee\quad
\text{nonadiabatic flag motion},
\]

but the quantitative adiabatic theorem is not yet proved.

Similarly, (4.2) in `00_THEOREM_SPINE.md` gives the exact broad/thin heat statistic

\[
\operatorname{Var}_\mu(\kappa),
\]

but converting a thin outward-moving heat fiber into spatial Mother concentration is still an analytic step.

### OPEN

The preferred target is a one-step critical monodromy theorem. Let \(\mathcal U(t,s)\) solve

\[
\partial_t\mathcal U(t,s)=-\nu(C^\sharp(t))^2\mathcal U(t,s),
\]

and set \(\Lambda^\sharp=|C^\sharp|\). On a normalized positive spectral sector define

\[
\mathcal K_{s,T}
=(\Lambda^\sharp(s))^{-1/2}
\mathcal U(T,s)^*\Lambda^\sharp(T)\mathcal U(T,s)
(\Lambda^\sharp(s))^{-1/2}.
\tag{1.1}
\]

The desired theorem has only two legitimate branches:

\[
\boxed{
\|\mathcal K_{s,T}\|\le1-\varepsilon
\quad\vee\quad
\text{a near-neutral normalized complete state compactifies into an exact harmless kernel.}
}
\tag{1.2}
\]

The zero kernel is structurally classified; the quantitative passage to it is open.

## No-go ledger

1. **Do not use \(X/Y\), traffic, a hinge scalar, Fisher action, or a source ray as the master state.** They are downstream contractions.
2. **Do not claim finite weak Mother action closes the cascade.** A critical generation at scale \(K\) may cost only \(K^{-1}\) over one parabolic time.
3. **Do not identify the flag edge norm with the physical Mother norm without a theorem.** Their half-derivative relation is the seam to be proved, not assumed.
4. **Do not prove an abstract “skew + heat” theorem and call it NS.** The final estimate must use 3D physical-section information, e.g. the Mother principal symbol
   \[
   \sigma_1(E_u)(x,\xi)b
   =-i\frac{\xi^TS(u)\xi}{|\xi|^2}\,\xi\times b,
   \qquad \operatorname{tr}S=0,
   \]
   or an equivalent incompressible 3D convolution identity.
5. **Do not call \((v,C^\sharp)\) complete after discarding the frame gauge.** Keep \(U\), or keep \(u/E/\Sigma\) as ontology.

## Two genuine analytic enemies

The interaction frame removes observer-induced ambiguity but not physical noncompactness. Two useful hostile classes remain:

- **localized affine-strain escape:** on a core where \(u\approx A(t)x\), \(A=A^T\), \(\operatorname{tr}A=0\), viscosity does not see the exact affine field because \(\Delta(Ax)=0\); finite-energy localization alone has the wrong scaling to exclude an expanding normalized affine core;
- **genuinely non-affine concentrated Mother motion:** the complete strain/Mother varies on the parabolic scale and must be controlled by a true compactness/coercivity theorem.

These are physical analytic enemies, not missing-information artifacts.

## Lessons to carry forward

- **Complete first, contract last.**
- **Euler is geometry motion, not a new source, in the interaction frame.**
- **Heat is the only sign-definite normal generator.**
- **The missing half derivative is already present geometrically in the full moving flag.**
- **The remaining task is quantitative monodromy/compactness, not ontology discovery.**
- **A successful END should become smaller than the historical endgame, not accumulate descendants.**
