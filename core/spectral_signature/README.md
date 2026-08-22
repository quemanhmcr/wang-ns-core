# Spectral Signature Core

This directory is the canonical home of the whole-state curl spectral signature of homogeneous incompressible Navier--Stokes.

The central objects are
\[
E_u=[\nabla_u,C]
\]
and the shifted spectral-flag family
\[
\mathscr O_a(v)
=H_a[\nabla_v,H_a]-[\nabla_{H_av},H_a],
\qquad
H_a=\operatorname{sgn}(C-aI).
\]

The final structural hierarchy is
\[
\boxed{
E=[\nabla,C]
\quad\longleftrightarrow\quad
\{\mathscr O_a\}_{a\in\mathbb R}
\quad\longrightarrow\quad
\mathscr O_0
\quad\longrightarrow\quad
J_0
\quad\longrightarrow\quad
W_0.
}
\]

The first arrow is an equivalence through spectral tomography.  The later arrows are information-losing readers or contractions.

## Read in this order

1. [SPECTRAL_FLAG_SIGNATURE.md](SPECTRAL_FLAG_SIGNATURE.md) — defines the shifted operator-valued signature, its reverse compiler, tomography, quotient by the curl commutant, and the relation to torsion/stress/curvature renderers.
2. [SPECTRAL_FLAG_COMPLETENESS.md](SPECTRAL_FLAG_COMPLETENESS.md) — records the adversarial experiments that tested whether the signature carries the whole physical state and the full NS vector field.
3. [MOTHER_COMPLETENESS_THEOREM.md](MOTHER_COMPLETENESS_THEOREM.md) — gives the clean structural theorem: the mother deformation is complete modulo Killing symmetry, the signature is its canonical spectral normal form, and smooth NS is exactly conjugate to a flow on the signature image.
4. [HISTORY_AND_FALSIFICATION.md](HISTORY_AND_FALSIFICATION.md) — the short record of what failed and why the final object has its present tensor/operator form.
5. [HALF_DERIVATIVE_POLAR_KORN_BRIDGE.md](HALF_DERIVATIVE_POLAR_KORN_BRIDGE.md) — the late regularity-frontier reconstruction: the moving flag supplies the missing half derivative, reciprocal Lemmas A/B close the aligned static incidence seam, and the remaining key is retyped as a hypocoercive Polar--Korn coupling rather than a stand-alone Codazzi budget.

For the longer discovery narrative, begin at the repository root: [Core_signature.md](../../Core_signature.md).

## Theorem core

On smooth mean-zero divergence-free fields on \(\mathbb T^3\), the mother operator has principal symbol
\[
\boxed{
\sigma_1(E_u)(x,\xi)b
=-i\frac{\xi^TS(u)(x)\xi}{|\xi|^2}\,\xi\times b,
\qquad b\perp\xi.
}
\]
Thus the mother reads the strain quadratic form
\[
q_u(x,n)=n^TS(u)(x)n.
\]
Spherical inversion gives
\[
\boxed{
S(u)(x)
=\frac{15}{2}\fint_{S^2}q_u(x,n)n\otimes n\,dn,
}
\]
and incompressibility gives
\[
\boxed{
\Delta u=2\operatorname{div}S(u).
}
\]
Therefore the state is reconstructed modulo the Euclidean Killing sector, and uniquely on the mean-zero periodic class.

The canonical Sobolev identity is
\[
\boxed{
\|u\|_{\dot H^{s+1}}^2
=15\int_{\mathbb T^3}\fint_{S^2}
|\Lambda_x^sq_u(x,n)|^2\,dn\,dx.
}
\]
Six fixed directions already give a uniform frame with exact constants
\[
\boxed{
\frac{7-\sqrt{17}}{16}\|u\|_{\dot H^{s+1}}^2
\le
\sum_{r=1}^6\|\Lambda_x^sq_u(\cdot,n_r)\|_2^2
\le
\frac{7+\sqrt{17}}{16}\|u\|_{\dot H^{s+1}}^2.
}
\]

## Whole-NS meaning

The signature does not equal the entire connection directly.  The curl-commuting block is a real vertical isospectral gauge motion.  The signature determines the horizontal/off-spectral part; the recovered physical state determines the vertical part.  Consequently the full connection and the full smooth NS vector field are recovered from the signature state.

This is a structural completeness statement.  It is not a global regularity theorem and does not by itself exclude singularity formation.

## Reproduce the canonical audits

```bash
python core/spectral_signature/audits/spectral_flag_signature.py
python core/spectral_signature/audits/spectral_flag_completeness.py
python core/spectral_signature/audits/mother_completeness_theorem.py
python core/spectral_signature/audits/reciprocal_lemma_a_certificate.py
python core/spectral_signature/audits/reciprocal_lemma_b_certificate.py
python core/spectral_signature/audits/equal_heat_collision_gap.py
```

These audits are the canonical executable core and late-frontier certificates.  Older G3, Riccati, discriminant, scale, and propagation experiments remain recoverable from Git history, but are intentionally not part of this directory because they are discovery history rather than the final spectral-signature theory.

## Relation to NEO

NEO remains the compiler discipline that made this compression possible.  Its two canonical documents live at [../NEO/](../NEO/).  NEO is not the subject of this directory.  The subject here is the resulting whole-state Navier--Stokes geometry:
\[
\boxed{
\mathscr O
\longleftrightarrow
E
\longleftrightarrow
S
\longleftrightarrow
u/\mathrm{Kill}
\longrightarrow
F_{NS}(u).
}
\]

For the pre-signature worktree history — terminal normal forms, C0/C1/G3/Type-I geometry and the material-curl precursor — see [../../history/worktrees/README.md](../../history/worktrees/README.md).
