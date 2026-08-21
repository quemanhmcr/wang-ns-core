# Evidence, Falsification, and Scope

This note separates exact identities from the stronger structural interpretation that the metric-Lie/Hodge datum is a canonical formation core.

## 1. What is exact once the datum is fixed

The following are algebraic/geometric identities on the smooth typed setting:

- Koszul reconstruction of \(\nabla\) from the metric and Lie bracket;
- Riesz reconstruction of \(\mathcal J_u\) from \(-\langle u,[a,b]\rangle\);
- \(N(u)=\mathcal J_uu=-\nabla_uu\);
- the metric-defect/strain identity for \(\mathfrak D\);
- the formation pencil \(\mathcal L_{\nu,u}=\mathcal J_u-\nu C^2\);
- the helicity/Killing contraction of curl;
- the local pressure-source identity \(-\Delta p=|\nabla u|^2-|\omega|^2\);
- the functorial relations between material and Poisson curl commutators;
- the first Euler–heat BCH identities and their Jacobi syzygies;
- boundary Green identity and de Rham chain identities.

## 2. Restricted uniqueness / formation evidence

Adversarial invariant-tensor classifications on local Euclidean polynomial laws found:

\[
81\xrightarrow{SO(3)}3\xrightarrow{\nabla\cdot u=0,\,P}1
\]

for quadratic first-order vector laws, leaving projected advection; Galilean covariance fixes its normalization.

For linear second-order isotropic laws, second-derivative symmetry and \(SO(3)\) reduce the family to

\[
\Delta u,
\qquad
\nabla\operatorname{div}u,
\]

and incompressibility leaves the Laplacian/Stokes direction.

The unique isotropic cubic zero-derivative direction is \(|u|^2u\), which Galilean covariance rejects.

These results support a restricted local-Euclidean characterization of the NS formation law.  They are not stated here as a classification theorem for arbitrary nonlocal, manifold, boundary, forcing, or variable-coefficient equations.

## 3. Black-box reconstruction evidence

Several inverse tests were used precisely to avoid verifying formulas only in the forward direction:

- linear probes of the two core brackets reconstruct the complete NS vector field by Riesz tomography;
- querying a black-box vector field at \(u\) and \(2u\) separates its quadratic Euler and linear heat components, after which polarization reconstructs the Euler bilinear product;
- the nonlinear Euler work nullspace over arbitrary signed-radius weights has exactly the two universal directions corresponding to energy and signed curl/helicity;
- independently measured linear damping rates are proportional to the square of that hidden signed coordinate, so reversible Euler and irreversible heat identify the same \(C\)/\(C^2\) geometry;
- sparse regression over a much larger library of core-generated vector fields selects only \(\mathcal J_uu\) and \(-\nu C^2u\) on generic, 2D, shear, and Beltrami validation states.

These are evidence for structural minimality, not substitutes for an unrestricted theorem.

## 4. Falsifications that shaped the final theory

Several stronger or simpler candidates were rejected:

- raw \([D_u,C]\) is a useful connection carrier but is nonzero on harmless shear/Beltrami/2D states, so it is not by itself a singularity obstruction;
- helicity torsion/curvature can be nonzero on regular 2D flows;
- energy and helicity conservation alone do not characterize the vector-field Lie bracket: fake isotropic antisymmetric brackets can preserve those contractions while violating Jacobi/Leibniz;
- replacing \(C\) by a nearby self-adjoint spectral operator such as \(C+\varepsilon C^3\) breaks the Euler Killing identity;
- replacing the \(L^2\) metric by another positive isotropic metric still gives an Euler–Arnold system but changes the dynamics away from Navier–Stokes;
- hyperviscous \(C^4\) dissipation breaks the ordinary NS carré-du-champ and homogeneity lock;
- formal curl without domain data fails on boundaries because of the nonzero boundary Green form.

The surviving object is therefore not a single local tensor.  It is the oriented metric-Lie formation structure together with a typed Hodge/de Rham realization.

## 5. Open scope

The canonical claims in this folder do **not** establish:

- global regularity or singularity exclusion;
- a completed cohomological obstruction class for blow-up;
- classification on arbitrary Riemannian manifolds or domains with all boundary conditions;
- forced, variable-density, compressible, MHD, or variable-coefficient extensions;
- that the mixed Euler–heat Lie algebra is globally free at every grade (the rank evidence currently reaches finite depth only).

The next structural questions are whether the typed formation datum admits a coordinate-free classification on general oriented Hodge manifolds/domains and whether the compatibility/curvature descendants possess a canonical quotient that isolates non-integrable classes without discarding harmonic topology.
