# Curved Formation–Signature Core

This directory is the canonical home of the structural bridge between the repository's two existing Navier–Stokes cores:

- the [Metric–Lie / Hodge formation core](../metric_lie_hodge/README.md), which generates the equation from the physical metric-Lie/curl datum;
- the [Spectral Signature Core](../spectral_signature/README.md), which encodes the complete smooth state through the mother curl deformation and shifted spectral flags.

The central conclusion of the present core is not that those two theories are identical.  The deep geometry campaign sharpens the statement to

\[
\boxed{
\text{the spectral-signature theory is the canonical curl-spectral representation of the physical formation geometry.}
}
\]

Here “curved representation” means that the signature coordinates carry the transported formation connection and curvature.  The signature image itself is linear and flat as an ordinary constant-metric embedded space; the curvature belongs to the represented formation geometry.

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

## Deep geometric reduction: curl spectral sheets

The second adversarial campaign exposed a sharper internal geometry.  In a curl spectral frame the formation connection splits

\[
\boxed{
\nabla=V+B,
\qquad
[V,C]=0,
}
\]

where \(V\) rotates within a curl eigenspace and \(B\) mixes different eigenspaces.  Therefore

\[
\boxed{
E=[B,C],
}
\]

so the complete mother is the gap-weighted spectral sheet-mixing part of the formation connection.

Formation curvature splits correspondingly:

\[
R=R_\parallel+R_\perp,
\qquad
[R_\parallel,C]=0,
\]

with the Gauss/Ricci-type within-sheet sector

\[
R_\parallel=[V,V]+\Pi_\parallel[B,B]
\]

and the Codazzi-type cross-sheet sector \(R_\perp\).  The curvature mother sees exactly the latter:

\[
\boxed{
K=[R,C]=[R_\perp,C].
}
\]

This is the geometric meaning of the new canonical phrase **curl-spectral reduction of formation geometry**.  The full account is in [CURL_SPECTRAL_REDUCTION.md](CURL_SPECTRAL_REDUCTION.md); the falsifications and scope corrections are collected in [DEEP_GEOMETRY_LESSONS.md](DEEP_GEOMETRY_LESSONS.md).

## Read in this order

1. [FORMATION_SIGNATURE_EQUIVALENCE.md](FORMATION_SIGNATURE_EQUIVALENCE.md) — forward functor, reverse state/operator reconstruction, induced metric-Lie structures, and the commuting dynamical diagram.
2. [CURL_SPECTRAL_REDUCTION.md](CURL_SPECTRAL_REDUCTION.md) — the matured geometry: isospectral orbit, stabilizer splitting, spectral sheets, Gauss–Codazzi–Ricci decomposition, Cartan/Bianchi structure, and higher-degree observability.
3. [CURVED_CURL_MODULE.md](CURVED_CURL_MODULE.md) — curvature-corrected bracket, holonomy, curved covariant tower, and shifted-cut curvature tomography.
4. [SIGNATURE_METRIC_DYNAMICS.md](SIGNATURE_METRIC_DYNAMICS.md) — exact bridge from the formation \(L^2\)/Dirichlet pair to \(\dot H^{-1}\)/\(L^2\) metrics on the strain signature; viscosity as their Riesz ratio.
5. [PHYSICAL_RIGIDITY_AND_IDENTIFIABILITY.md](PHYSICAL_RIGIDITY_AND_IDENTIFIABILITY.md) — what signature data determine, physical rigidity, first-order stabilizers, and topology/domain caveats.
6. [DEEP_GEOMETRY_LESSONS.md](DEEP_GEOMETRY_LESSONS.md) — negative controls, failed interpretations, boundary/topology lessons, and the exact limits of the new geometry.
7. [THEOREM_STATUS_AND_SCOPE.md](THEOREM_STATUS_AND_SCOPE.md) — exact statements, inherited theorems, standard geometric identities, executable evidence, and current open scope.
8. [HISTORY_AND_FALSIFICATION.md](HISTORY_AND_FALSIFICATION.md) — the discovery path and the failures that forced the final formulation.

For the longer research records, Git history retains the uncompressed laboratory notebooks on the research branches.  This directory intentionally keeps only the canonical theory and executable tribunals.

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

> On the canonical smooth periodic physical NS core, curl defines a canonical spectral reduction of the formation connection.  The complete mother \(E=d_\nabla C\) solders the physical state into a distinguished distribution in the curl isospectral orbit; formation curvature splits into within-sheet Gauss/Ricci and cross-sheet Codazzi sectors; \([R,C]\) is the curvature mother of the cross-sheet sector; and the full signature-side operator field carries the transported formation dynamics autonomously.

This does **not** say that the signature image is itself a curved embedding, that \([R,C]\) is a blow-up indicator, that the whole curl commutant is a final gauge, or that a single signature snapshot determines an arbitrary abstract metric-Lie core.  Exact counterexamples show each of those stronger readings to be false.  It also does not prove global regularity or settle the optimal boundary/cohomological formulation.

## Reproduce the canonical audits

Run from repository root:

```bash
# Original formation/signature bridge
python core/curved_formation_signature/audits/metric_lie_spectral_unification.py
python core/curved_formation_signature/audits/signature_to_formation_microlocal.py
python core/curved_formation_signature/audits/signature_core_identifiability.py
python core/curved_formation_signature/audits/physical_axiom_rigidity.py
python core/curved_formation_signature/audits/signature_metric_heat_bridge.py
python core/curved_formation_signature/audits/galerkin_probe_lie_failure.py
python core/curved_formation_signature/audits/curved_curl_dg_physical.py
python core/curved_formation_signature/audits/physical_curvature_flag_tomography.py

# Deep curl-spectral reduction / falsification tribunals
python core/curved_formation_signature/audits/curl_solder_cartan_structure.py
python core/curved_formation_signature/audits/curl_orbit_stabilizer.py
python core/curved_formation_signature/audits/spectral_gauss_codazzi_ricci.py
python core/curved_formation_signature/audits/full_physical_gauss_codazzi.py
python core/curved_formation_signature/audits/connection_lift_curvature_recovery.py
python core/curved_formation_signature/audits/full_physical_vertical_curvature.py
python core/curved_formation_signature/audits/full_physical_vertical_degree4.py
python core/curved_formation_signature/audits/blind_reversible_irreversible_split.py
python core/curved_formation_signature/audits/orientation_double_cover.py
python core/curved_formation_signature/audits/bch_vs_geometric_curvature.py
python core/curved_formation_signature/audits/harmless_class_curvature.py
python core/curved_formation_signature/audits/harmonic_zero_mode_signature.py
python core/curved_formation_signature/audits/boundary_metric_typing.py
python core/curved_formation_signature/audits/representation_curvature_not_embedding_curvature.py
```

The suite deliberately contains negative controls.  `signature_core_identifiability.py` exhibits an exact abstract core collision; `galerkin_probe_lie_failure.py` demonstrates that arbitrary Galerkin projection can destroy mother completeness and Jacobi; `harmless_class_curvature.py` prevents curvature from being misread as a danger amplitude; `representation_curvature_not_embedding_curvature.py` prevents the phrase “curved representation” from being misread as embedding curvature; and the topology/boundary audits keep the periodic operator formulas correctly typed.
