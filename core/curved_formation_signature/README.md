# Curved Formation–Signature Core

This directory is the canonical home of the structural bridge between the repository's two existing Navier–Stokes cores:

- the [Metric–Lie / Hodge formation core](../metric_lie_hodge/README.md), which generates the equation from the physical metric-Lie/curl datum;
- the [Spectral Signature Core](../spectral_signature/README.md), which encodes the complete smooth state through the mother curl deformation and shifted spectral flags.

The central conclusion of the present core is not that those two theories are identical.  It is the more precise statement

\[
\boxed{
\text{the spectral-signature theory is a complete curved representation of the canonical physical formation core.}
}
\]

On the smooth periodic divergence-free class, the formation datum is

\[
\mathcal C_{NS}
=(\mathfrak g_\sigma,\langle\cdot,\cdot\rangle_{L^2},T,C),
\qquad
T(a,b,c)=\langle a,[b,c]\rangle,
\qquad C=\operatorname{curl}.
\]

Its Levi–Civita connection \(\nabla\) induces the mother

\[
\boxed{
E=d_\nabla C,
\qquad
E_u=[\nabla_u,C].
}
\]

The shifted spectral family is a tomography of that deformation.  The stronger bridge proved algebraically and stress-tested here is that curvature enters at the next covariant degree:

\[
\boxed{
 d_\nabla E=d_\nabla^2C=[R,C],
\qquad
R(a,b)=[\nabla_a,\nabla_b]-\nabla_{[a,b]}.
}
\]

Thus the first structural tower is

\[
\boxed{
C
\xrightarrow{d_\nabla}
E
\xrightarrow{d_\nabla}
[R,C]
\xrightarrow{d_\nabla}
R\wedge E
\xrightarrow{d_\nabla}\cdots,
\qquad
d_\nabla^2=R\text{-action}.
}
\]

The shifted cuts also tomograph the curvature action:

\[
\boxed{
\frac12\int_{\mathbb R}[R,H_a]\,da=[R,C],
\qquad
H_a=\operatorname{sgn}(C-aI),
}
\]

with the integral understood in the same spectral layer-cake sense used in the spectral-signature core.

## Read in this order

1. [FORMATION_SIGNATURE_EQUIVALENCE.md](FORMATION_SIGNATURE_EQUIVALENCE.md) — forward functor, reverse state/operator reconstruction, induced metric-Lie structures, and the commuting dynamical diagram.
2. [CURVED_CURL_MODULE.md](CURVED_CURL_MODULE.md) — curvature-corrected bracket, holonomy, Bianchi identities, curved covariant tower, and shifted-cut curvature tomography.
3. [SIGNATURE_METRIC_DYNAMICS.md](SIGNATURE_METRIC_DYNAMICS.md) — exact bridge from the formation \(L^2\)/Dirichlet pair to \(\dot H^{-1}\)/\(L^2\) metrics on the strain signature; viscosity as their Riesz ratio.
4. [PHYSICAL_RIGIDITY_AND_IDENTIFIABILITY.md](PHYSICAL_RIGIDITY_AND_IDENTIFIABILITY.md) — what a signature state does and does not determine, the exact dark-sector counterexample, and why physical locality/derivation removes that abstract ambiguity.
5. [THEOREM_STATUS_AND_SCOPE.md](THEOREM_STATUS_AND_SCOPE.md) — exact statements, inherited theorems, experimental evidence, and the boundary between theorem and current candidate.
6. [HISTORY_AND_FALSIFICATION.md](HISTORY_AND_FALSIFICATION.md) — concise discovery path and the failures that forced the final formulation.

For the longer research-worktree record, Git history on `research/metric-lie-spectral-unification` retains the full laboratory notebook.  This directory intentionally keeps only the canonical theory and its executable tribunals.

## Core diagram

The relation between the three canonical layers is

\[
\boxed{
(\mathfrak g_\sigma,g,T,C)
\xrightarrow{\text{Koszul/Riesz}}
(\nabla,\mathcal L_{\nu,u})
\xrightarrow{\ d_\nabla C\ }
E_u
\xleftrightarrow{\text{spectral tomography}}
\{\mathscr O_a(u)\}_{a\in\mathbb R}.
}
\]

On a fixed physical formation core, the mother and full shifted flag reconstruct the state modulo the known Killing/Galilean sector; after state reconstruction they recover the complete state-dependent formation operator.  The signature image must carry the **transported \(L^2\) Riesz metric**; treating raw operator coordinates as Euclidean produces order-one errors.

The induced formation bracket on the mother side is also not the naive operator commutator.  The exact identity is

\[
\boxed{
E_{[u,v]}
=[\nabla_u,E_v]-[\nabla_v,E_u]-[R(u,v),C].
}
\]

The curvature term is not a formal correction: infinitesimal loop transport measures it as the holonomy of curl.

## Exact metric bridge

For the strain signature

\[
q_u(x,n)=n^TS(u)(x)n,
\]

the spectral Sobolev identity yields, by polarization,

\[
\boxed{
\langle u,v\rangle_{L^2}
=15\int\!\fint_{S^2}
(\Lambda^{-1}q_u)(\Lambda^{-1}q_v)\,dn\,dx,
}
\]

and

\[
\boxed{
\langle Cu,Cv\rangle_{L^2}
=15\int\!\fint_{S^2}q_uq_v\,dn\,dx.
}
\]

Hence, on signature coordinates,

\[
\boxed{
 g^{\Sigma}_{\rm kinetic}=15\,\dot H^{-1},
\qquad
 g^{\Sigma}_{\rm Dirichlet}=15\,L^2,
\qquad
(g^{\Sigma}_{\rm kinetic})^{-1}g^{\Sigma}_{\rm Dirichlet}=\Lambda^2.
}
\]

This explains the heat operator as the Riesz ratio of the two formation metrics after passing to signature geometry.

## What is and is not being claimed

The strongest current structural claim is:

> On the canonical smooth periodic physical NS core, the mother/spectral-signature coordinates form a complete state representation of the formation dynamics, with the formation metric, curl, bracket and curvature transported nontrivially to the signature image.  Curvature of the distinguished curl object is represented by the covariant tower generated by \(d_\nabla\), and shifted spectral cuts tomograph both first deformation and the tested curvature action.

This does **not** say that a single signature snapshot determines an arbitrary abstract metric-Lie core.  Exact counterexamples show that it does not.  It also does not prove global regularity, identify a final singularity obstruction norm, or settle the correct cohomological quotient for the curved tower.

## Reproduce the canonical audits

Run from repository root:

```bash
python core/curved_formation_signature/audits/metric_lie_spectral_unification.py
python core/curved_formation_signature/audits/signature_to_formation_microlocal.py
python core/curved_formation_signature/audits/signature_core_identifiability.py
python core/curved_formation_signature/audits/physical_axiom_rigidity.py
python core/curved_formation_signature/audits/signature_metric_heat_bridge.py
python core/curved_formation_signature/audits/galerkin_probe_lie_failure.py
python core/curved_formation_signature/audits/curved_curl_dg_physical.py
python core/curved_formation_signature/audits/physical_curvature_flag_tomography.py
```

The suite deliberately contains negative controls.  In particular, `signature_core_identifiability.py` exhibits an exact abstract core collision, and `galerkin_probe_lie_failure.py` demonstrates that arbitrary Galerkin projection can destroy mother completeness and Jacobi even when the full microlocal signature remains complete.
