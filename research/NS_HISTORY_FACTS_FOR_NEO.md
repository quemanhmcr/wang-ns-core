# NS HISTORY FACTS FOR NEO
Purpose: a compact team-facing literature ledger for the active contract in `DEFINE_PROBLEM.md`.
Use this file only to decide what the terminal-extraction / NEO-normal-form programme may legally assume, what history supports, and where the real open seams are.
Do not read this as a regularity proof.
Do not promote any `TEAM DEDUCTION` below to an external theorem.
The ontology remains
\[
u(t),\qquad P,\qquad C=\operatorname{curl},\qquad C^2=(-\Delta)P,\qquad t.
\]
The strategic architecture remains
\[
T_*<\infty
\to
\text{terminal object}
\to
\text{finite NEO normal forms}
\to
\text{rigidity contradiction}.
\]
---
## A. Historical vote on the proof architecture
### A01. Local singularity theory is fundamentally scale-local.
**EXTERNAL EXACT.** Caffarelli--Kohn--Nirenberg prove partial regularity for suitable weak solutions using scale-local quantities on parabolic cylinders.
**TEAM USE.** A singular endpoint should be attacked by quantities that survive shrinking cylinders; global trajectory surveillance is not historically necessary.
Paper: Caffarelli--Kohn--Nirenberg, *Partial regularity of suitable weak solutions of the Navier-Stokes equations* (1982).
https://doi.org/10.1002/cpa.3160350604
### A02. CKN was later recast in a compact local form.
**EXTERNAL EXACT.** Lin gave a self-contained proof of the CKN theorem with a cleaner compactness/local-energy architecture.
**TEAM USE.** Compactness and local rigidity are legitimate external layers; NEO need not regenerate them from the anchors.
Paper: Fang-Hua Lin, *A new proof of the Caffarelli-Kohn-Nirenberg theorem* (1998).
https://doi.org/10.1002/(SICI)1097-0312(199803)51:3%3C241::AID-CPA2%3E3.0.CO;2-A
### A03. Endpoint regularity can be proved by contradiction after blow-up.
**EXTERNAL EXACT.** Escauriaza--Seregin--Sverak prove the endpoint \(L_t^\infty L_x^3\) regularity criterion using blow-up plus backward uniqueness.
**TEAM USE.** A proof can legitimately reduce a global continuation problem to a rigidity statement for a rescaled terminal object.
Paper: Escauriaza--Seregin--Sverak, *L_{3,\infty}-solutions of the Navier-Stokes equations and backward uniqueness* (2003).
https://doi.org/10.1070/RM2003v058n02ABEH000609
### A04. Concentration-compactness + rigidity is a proven NS architecture.
**EXTERNAL EXACT.** Kenig--Koch prove that a mild solution bounded in \(\dot H^{1/2}\) cannot blow up in finite time, using concentration-compactness plus a rigidity theorem.
**TEAM USE.** The architecture
\[
\text{blowup assumption}\to\text{critical object}\to\text{rigidity}
\]
is established methodology in NS.
Paper: Kenig--Koch, *An alternative approach to regularity for the Navier-Stokes equations in critical spaces*.
https://arxiv.org/abs/0908.3349
### A05. Critical-element machinery has a strict scope.
**EXTERNAL EXACT.** Kenig--Koch assumes control in a critical space; the method does not turn an arbitrarily diverging critical norm into a normalized bounded one by scaling.
**TEAM USE.** Do not identify arbitrary Clay blow-up with the Kenig--Koch critical-element class.
Same paper:
https://arxiv.org/abs/0908.3349
### A06. Minimal singular data exist conditionally in \(\dot H^{1/2}\).
**EXTERNAL EXACT.** Rusin--Sverak prove: if any \(\dot H^{1/2}\) data produce singularity, then there are singularity-producing data of minimal \(\dot H^{1/2}\)-norm.
**TEAM USE.** Minimal-object extraction is historically sound when a critical norm supplies compactness; this does not license the same conclusion for an arbitrary terminal class.
Paper: Rusin--Sverak, *Minimal initial data for potential Navier-Stokes singularities*.
https://arxiv.org/abs/0911.0500
### A07. The terminal/Liouville programme is explicit in the literature.
**EXTERNAL EXACT.** Seregin--Shilkin describe an approach reducing local regularity questions to Liouville-type theorems for bounded ancient solutions.
**TEAM USE.** `DEFINE_PROBLEM.md` is aligned with an established regularity programme: extraction and rigidity are separate layers.
Paper: Seregin--Shilkin, *Liouville-type theorems for the Navier-Stokes equations* (2018).
https://doi.org/10.1070/RM9822
---
## B. Ancient extraction and the Galilean seam
### B01. Finite-time singularity can generate a bounded ancient mild solution.
**EXTERNAL EXACT.** Koch--Nadirashvili--Seregin--Sverak develop bounded ancient solutions and derive them from blow-up rescaling in the regularity context.
**TEAM USE.** Bounded ancient mild solutions are a natural terminal class.
Paper: Koch--Nadirashvili--Seregin--Sverak, *Liouville theorems for the Navier-Stokes equations and applications*.
https://arxiv.org/abs/0709.3599
### B02. Amplitude normalization does not remove constants.
**EXTERNAL EXACT.** In the KNSS blow-up normalization one can obtain a nonzero bounded ancient profile with a normalized velocity amplitude, but a nonzero bounded ancient solution could still be constant.
**TEAM USE.** Never write
\[
U\neq0\Rightarrow CU\neq0.
\]
The exact seam is nonconstancy modulo Galilean constants.
Same paper:
https://arxiv.org/abs/0709.3599
### B03. Weak ancient and mild ancient are not interchangeable.
**EXTERNAL EXACT.** KNSS distinguish mild bounded ancient solutions from weaker ancient classes; weak formulations permit parasitic spatially constant time-dependent fields with compensating pressure.
**TEAM USE.** The terminal solution class is part of the theorem statement, not bookkeeping.
Same paper:
https://arxiv.org/abs/0709.3599
### B04. Singular points generate nontrivial bounded mild ancient solutions under local hypotheses.
**EXTERNAL EXACT.** Albritton--Barker prove localized singularity conditions and extraction of a nontrivial mild bounded ancient solution in \(\mathbb R^3\) or the half-space.
**TEAM USE.** External extraction is strong enough to produce bounded ancient objects, but the theorem says nontrivial, not automatically nonconstant modulo Galilean symmetry.
Paper: Albritton--Barker, *Localised necessary conditions for singularity formation in the Navier-Stokes equations with curved boundary*.
https://arxiv.org/abs/1811.00507
### B05. Type-I singularity has an ancient-profile equivalence.
**EXTERNAL EXACT.** Albritton--Barker prove Type-I singularity occurs iff there exists a nontrivial mild bounded ancient solution satisfying a Type-I decay condition.
**TEAM USE.** When extraction carries an extra scale law, the ancient class becomes substantially more rigid.
Paper: Albritton--Barker, *On local Type I singularities of the Navier-Stokes equations and Liouville theorems*.
https://arxiv.org/abs/1811.00502
### B06. Galilean invariance is a real blow-up tool, not cosmetic symmetry.
**EXTERNAL EXACT.** Vasseur explicitly uses Galilean invariance in blow-up estimates for higher derivatives.
**TEAM USE.** Designing the extraction quantity modulo Galilean frames has precedent in NS regularity analysis.
Paper: Vasseur, *Higher derivatives estimate for the 3D Navier-Stokes equation*.
https://arxiv.org/abs/0904.2422
### B07. Singular-time oscillation has appeared as a rigorous obstruction.
**EXTERNAL EXACT.** Kozono--Sohr show that if a smooth solution loses regularity at a finite time while the critical \(L^n\) norm does not diverge, then the solution must oscillate with sufficiently large amplitude around its weak limit.
**TEAM USE.** A singularity-forces-oscillation principle has real precedent.
Paper: Kozono--Sohr, *Regularity criterion on weak solutions to the Navier-Stokes equations* (1997).
https://waseda.elsevierpure.com/en/publications/regularity-criterion-on-weak-solutions-to-the-navier-stokes-equat/
### B08. Candidate extraction quantity suggested by history.
**TEAM DEDUCTION.** Search for a scale-invariant local quantity of the schematic form
\[
\mathcal O(u;Q_r)=\inf_{c\in\mathbb R^3}\mathcal N_r(u-c),
\]
possibly with a Galilean-tilted cylinder rather than a fixed vertical cylinder.
**OPEN.** No paper in this ledger proves the exact Galilean Oscillation Nondegeneracy Theorem needed by NEO.
---
## C. Epsilon-regularity and scale nondegeneracy
### C01. A singular point must fail every valid smallness criterion at arbitrarily small scale.
**EXTERNAL EXACT.** This is the contrapositive content of epsilon-regularity theorems such as CKN/Lin and their descendants.
**TEAM USE.** The most promising route to Galilean nondegeneracy is to find a Galilean-invariant epsilon-regularity quantity.
CKN:
https://doi.org/10.1002/cpa.3160350604
Lin:
https://doi.org/10.1002/(SICI)1097-0312(199803)51:3%3C241::AID-CPA2%3E3.0.CO;2-A
### C02. One-component local criteria exist.
**EXTERNAL EXACT.** Kukavica--Rusin--Ziane prove an interior criterion where smallness of a scale-invariant quantity involving only one velocity component implies regularity.
**TEAM USE.** A small reader of the full state can carry the singular obstruction.
Paper: *An anisotropic partial regularity criterion for the Navier-Stokes equations*.
https://arxiv.org/abs/1511.02807
### C03. One directional derivative can be enough under critical integrability.
**EXTERNAL EXACT.** Kukavica--Ziane give regularity conditions involving one spatial directional derivative of velocity rather than the full gradient.
**TEAM USE.** Full tensor surveillance is not historically necessary.
Paper: Kukavica--Ziane, *Navier-Stokes equations with regularity in one direction*.
https://doi.org/10.1063/1.2395919
### C04. Two vorticity components can be enough.
**EXTERNAL EXACT.** Chae--Choe derive regularity conditions using only two components of vorticity.
**TEAM USE.** A finite projection of the curl face may encode enough obstruction to regularity.
Paper: Chae--Choe, *Regularity of solutions to the Navier-Stokes equation* (1999).
https://ejde.math.txstate.edu/Volumes/1999/05/abstr.html
### C05. A varying plane of vorticity can be enough.
**EXTERNAL EXACT.** Miller proves a locally anisotropic criterion controlling vorticity restricted to a plane; the plane may vary under controlled geometry.
**TEAM USE.** Canonical local readers need not be globally fixed coordinate components.
Paper: Miller, *A locally anisotropic regularity criterion for the Navier-Stokes equation in terms of vorticity*.
https://arxiv.org/abs/2002.02152
### C06. Historical synthesis from component criteria.
**TEAM DEDUCTION.** Literature repeatedly shows
\[
\text{small finite face}+\text{correct scale control}\Rightarrow\text{regularity}.
\]
This supports NEO minimalism.
It does not support a pointwise finite-jet classifier without scale information.
---
## D. Pressure: compiled but analytically nontrivial
### D01. Local pressure can be reconstructed by projection.
**EXTERNAL EXACT.** Wolf develops local pressure representations/projections for incompressible systems.
**TEAM USE.** Pressure need not be treated as an independent ontology primitive.
Paper: Wolf, *On the local pressure of the Navier-Stokes equations and related systems*.
https://arxiv.org/abs/1611.01482
### D02. Epsilon-regularity can be formulated using local pressure projection.
**EXTERNAL EXACT.** Jiu--Wang--Zhou prove epsilon-regularity criteria using Wolf's local pressure projection.
**TEAM USE.** Pressure can be routed through a derived local object during compactness/iteration.
Paper: Jiu--Wang--Zhou, *On Wolf's regularity criterion of suitable weak solutions to the Navier-Stokes equations*.
https://arxiv.org/abs/1805.04841
### D03. Pressure still creates analytic seams.
**EXTERNAL EXACT.** Modern pressure-regularity work studies precisely how pressure decomposition affects local regularity and epsilon-regularity.
**TEAM USE.** `pressure is a costume` means algebraic parentage, not analytic harmlessness.
Paper: Kwon, *The role of the pressure in the regularity theory for the Navier-Stokes equations* (2023).
https://doi.org/10.1016/j.jde.2023.01.049
### D04. Never convert local Hodge reconstruction into global spectral integrability.
**TEAM RULE.** A local pressure projection theorem does not grant
\[
U\in L^2,\qquad U\in\dot H^{1/2},\qquad H U\in L^2,
\]
for a bounded ancient terminal profile.
---
## E. Ancient Liouville facts and warnings
### E01. General 3D bounded-ancient Liouville is not solved.
**EXTERNAL EXACT.** KNSS state that the general three-dimensional bounded ancient problem is beyond the methods developed there; they prove lower-dimensional / symmetric partial results.
**TEAM USE.** NEO must add genuine terminal structure; bounded ancientness alone is not known to imply constancy.
https://arxiv.org/abs/0709.3599
### E02. Liouville results become strong after extra structure is added.
**EXTERNAL EXACT.** The ancient-solution literature contains rigidity in 2D, axisymmetric, no-swirl, integrable, Type-I, and other restricted classes.
**TEAM USE.** The classifier must reduce the terminal class analytically, not merely rename local jets.
Survey:
https://doi.org/10.1070/RM9822
### E03. Sublinear growth can be a Liouville threshold.
**EXTERNAL EXACT.** Lei--Zhang--Zhao prove sharp Liouville theorems in 2D / axisymmetric settings under sublinear growth and additional vorticity conditions.
**TEAM USE.** Growth control at infinity can be decisive.
Paper: Lei--Zhang--Zhao, *Improved Liouville theorems for axially symmetric Navier-Stokes equations*.
https://arxiv.org/abs/1701.00868
### E04. Linear growth admits counterexamples in those Liouville settings.
**EXTERNAL EXACT.** The same paper gives counterexamples at linear spatial growth.
**TEAM USE.** Gradient/curl normalization can move the terminal field into the dangerous affine/linear-growth class.
Same paper:
https://arxiv.org/abs/1701.00868
### E05. This matches the affine C0 countermodel in the NEO notebook.
**TEAM DEDUCTION.** A terminal normalization that preserves nonzero derivatives but loses bounded velocity can cross a known Liouville threshold.
Therefore raw curl/gradient normalization should not automatically replace bounded-velocity extraction.
### E06. Preferred two-stage architecture.
**TEAM DEDUCTION.** First extract bounded mild ancient \(U\) with nonzero Galilean oscillation.
Then deduce
\[
U\notin\mathbb R^3\Rightarrow CU\not\equiv0
\]
for bounded incompressible ancient mild fields.
Only then perform curl-contact normalization.
---
## F. Self-similar terminal forms: historical prototype of finite classification
### F01. Backward self-similar profiles have been excluded under natural hypotheses.
**EXTERNAL EXACT.** Nečas--Růžička--Šverák exclude nontrivial backward self-similar Navier--Stokes singularity profiles in the classical Leray form under their integrability setting.
**TEAM USE.** A singularity problem can be solved on a restricted terminal normal form by a Liouville theorem.
Paper: Nečas--Růžička--Šverák, *On Leray's self-similar solutions of the Navier-Stokes equations* (1996).
DOI landing/search reference:
https://doi.org/10.1007/BF02551584
### F02. Tsai strengthened self-similar nonexistence results.
**EXTERNAL EXACT.** Tsai excludes nontrivial self-similar solutions under broader local-integrability hypotheses.
**TEAM USE.** Finite-profile exclusion is a real historical success mode.
Paper: Tai-Peng Tsai, *On Leray's self-similar solutions of the Navier-Stokes equations satisfying local energy estimates* (1998).
https://doi.org/10.1007/s002050050099
### F03. Asymptotically self-similar singularities can also be ruled out under convergence hypotheses.
**EXTERNAL EXACT.** Chae proves nonexistence results for asymptotically self-similar singularities under specified convergence assumptions.
**TEAM USE.** Approximate terminal structure becomes useful only when the convergence topology is explicit.
Paper: Chae, *Nonexistence of asymptotically self-similar singularities in the Euler and the Navier-Stokes equations*.
https://arxiv.org/abs/math/0604234
### F04. Discrete self-similarity has also been attacked as a terminal scenario.
**EXTERNAL EXACT.** Chae--Wolf remove discretely self-similar singularities in a regime of scaling parameter near one.
**TEAM USE.** Singular scenarios can be eliminated branch by branch when each branch includes enough global/scale structure.
Paper: Chae--Wolf, *Removing discretely self-similar singularities for the 3D Navier-Stokes equations*.
https://doi.org/10.1080/03605302.2017.1358275
### F05. Lesson for NEO finite normal forms.
**TEAM DEDUCTION.** A useful terminal normal form must shrink the analytic class.
A label such as
\[
\omega\cdot S\omega=0
\]
at one point is not yet analogous to a self-similar profile equation.
---
## G. Vorticity and strain geometry
### G01. Vorticity direction geometry can prevent blow-up.
**EXTERNAL EXACT.** Constantin--Fefferman establish regularity under geometric coherence assumptions on vorticity direction in regions of large vorticity.
**TEAM USE.** Vortex-stretching geometry contains genuine regularity information beyond norm size.
Paper: Constantin--Fefferman, *Direction of vorticity and the problem of global regularity for the Navier-Stokes equations* (1993).
https://iumj.org/article/3627/
### G02. Vortex-stretching geometry can be localized.
**EXTERNAL EXACT.** Grujić shows vortex stretching and vorticity evolution can be localized on arbitrarily small space-time cylinders, localizing geometric depletion conditions.
**TEAM USE.** Local NEO is compatible with serious vorticity regularity mechanisms.
Paper: Grujić, *Localization and Geometric Depletion of Vortex-Stretching in the 3D NSE*.
https://doi.org/10.1007/s00220-008-0726-8
### G03. Geometry of superlevel sets can be enough.
**EXTERNAL EXACT.** Grujić gives a regularity criterion using local one-dimensional sparseness of intense-activity superlevel sets.
**TEAM USE.** A finite classifier may include a set-geometry renderer of a NEO quantity without enlarging the ontology.
Paper: Grujić, *A geometric measure-type regularity criterion for solutions to the 3D Navier-Stokes equations*.
https://doi.org/10.1088/0951-7715/26/1/289
### G04. Strain's middle eigenvalue is a meaningful compressed reader.
**EXTERNAL EXACT.** Miller derives scale-critical regularity/blow-up conditions depending on the positive part of the middle eigenvalue of the strain tensor.
**TEAM USE.** In the extensional branch, \(\lambda_2^+(S)\) is historically more motivated than indiscriminate higher Riccati descendants.
Paper: Miller, *A regularity criterion for the Navier-Stokes equation involving only the middle eigenvalue of the strain tensor*.
https://arxiv.org/abs/1710.05569
### G05. Pointwise maximum contact alone is historically weak.
**TEAM DEDUCTION.** Geometric regularity theorems usually control a neighborhood, active set, or scale-integrated quantity.
They do not establish that a finite Taylor jet at one vorticity maximum forces global rigidity.
### G06. Maximum-point geometry has nevertheless been used.
**EXTERNAL EXACT.** Nakai--Yoneda formulate blow-up criteria along maximum points using local geometric behavior around those points.
**TEAM USE.** Distinguished terminal extrema are legitimate places to normalize, but one should expect a neighborhood condition in addition to contact equalities.
Paper: Nakai--Yoneda, *A blowup criteria along maximum points of the 3D-Navier-Stokes flow...*.
https://arxiv.org/abs/1408.0159
---
## H. Curl/helicity/operator history
### H01. Curl has a complete rotational eigenmode decomposition.
**EXTERNAL EXACT.** Moses constructs curl eigenfunctions yielding one irrotational mode and two circularly polarized rotational modes of opposite sign.
**TEAM USE.** Treating curl as an organizing operator has deep historical precedent.
Paper: Moses, *Eigenfunctions of the Curl Operator, Rotationally Invariant Helmholtz Theorem, and Applications to Electromagnetic Theory and Fluid Mechanics* (1971).
https://doi.org/10.1137/0121015
### H02. Helical decomposition compresses nonlinear triad taxonomy.
**EXTERNAL EXACT.** Waleffe uses two helical modes per wave vector and reduces eight elementary triad interactions to two dynamical classes.
**TEAM USE.** Finite normal-form compression through curl/helicity variables is historically plausible.
Paper: Waleffe, *The nature of triad interactions in homogeneous turbulence* (1992).
https://doi.org/10.1063/1.858309
### H03. Curl spectral projections appear in rigorous regularity criteria.
**EXTERNAL EXACT.** Neustupa--Penel formulate regularity conditions using spectral projections associated with the self-adjoint curl operator, even using one component of a projected vorticity field.
**TEAM USE.** Signed-curl spectral faces are mathematically meaningful, not merely turbulence notation.
Paper: Neustupa--Penel, *Regularity of a Weak Solution to the Navier-Stokes Equations via One Component of a Spectral Projection of Vorticity*.
https://arxiv.org/abs/1207.3692
### H04. Modern work explicitly organizes NS around curl diagonalization.
**EXTERNAL EXACT.** Lerner--Vigneron study curl diagonalization, its relation to \(( -\Delta)^{1/2}\), spin-definite fields, helicity, and implications for NS regularity/blow-up.
**TEAM USE.** The NEO statement that matrix and spectral faces of curl are structurally rich has strong external precedent.
Paper: Lerner--Vigneron, *On some properties of the curl operator and their consequences for the Navier-Stokes system*.
https://arxiv.org/abs/2203.07950
### H05. Signed-curl regularity criteria continue to appear.
**EXTERNAL EXACT.** Guo--Nie develop regularity criteria via signed curl operators and Fourier/Littlewood--Paley analysis.
**TEAM USE.** Global spectral NEO has a real analytic literature when the function space licenses it.
Paper: Guo--Nie, *Some regularity criteria via the signed curl operators for the 3D Navier-Stokes equations* (2024).
https://doi.org/10.3934/dcdss.2024090
### H06. Spectral-curl papers generally require global Fourier/function-space structure.
**TEAM RULE.** Do not import these results into a merely bounded ancient terminal profile unless the extraction theorem supplies the required domain/integrability.
Therefore
\[
\text{Local NEO first},\qquad \text{Global spectral NEO only when licensed}.
\]
---
## I. Negative evidence and adversarial warnings
### I01. Energy cancellation plus generic harmonic analysis are not enough.
**EXTERNAL EXACT.** Tao constructs finite-time blow-up for an averaged Navier--Stokes equation preserving the standard energy cancellation and much of the coarse harmonic-analytic structure.
**TEAM USE.** Any proposed NEO rigidity mechanism should exploit finer structure specific to the true NS nonlinearity.
Paper: Tao, *Finite time blowup for an averaged three-dimensional Navier-Stokes equation*.
https://arxiv.org/abs/1402.0290
### I02. Tao gives an adversarial test for candidate mechanisms.
**TEAM RULE.** Ask:
> Would this argument still work for Tao's averaged nonlinearity?
If yes, it may be using structure too coarse to settle true 3D NS.
### I03. Finite-energy weak class is not automatically rigid.
**EXTERNAL EXACT.** Buckmaster--Vicol prove nonuniqueness in a class of finite-energy weak solutions.
**TEAM USE.** The provenance and regularity class of the terminal object must remain explicit; `weak ancient solution` is not enough.
Paper: Buckmaster--Vicol, *Nonuniqueness of weak solutions to the Navier-Stokes equation*.
https://doi.org/10.4007/annals.2019.189.1.3
### I04. Original finite energy does not imply terminal finite energy under blow-up scaling.
**TEAM DEDUCTION.** Under velocity-amplitude scaling
\[
V(y)=M^{-1}u(x_0+y/M),
\]
one has
\[
\|V\|_2^2=M\|u\|_2^2.
\]
Therefore a bounded ancient amplitude limit cannot be assigned global \(L^2\) by inheritance.
### I05. Critical norms are scale invariant, not normalizable by parabolic scaling.
**TEAM RULE.** If a critical norm diverges toward blow-up, scaling does not turn that divergence into norm one.
This is why arbitrary Clay blow-up is not automatically a critical element.
### I06. Nonzero is not nonconstant.
**TEAM RULE.** Constants are the first hostile terminal model for amplitude extraction.
The desired nondegeneracy statement must survive quotient by Galilean constants.
### I07. Curl-active is not automatically globally spectral.
**TEAM RULE.** \(CU\neq0\) is a local differential fact.
It does not imply
\[
U\in L^2,\qquad \Lambda^{1/2}U\in L^2,
\]
or any global helicity decomposition in an integrable Hilbert space.
### I08. Flat contact is not local rigidity.
**TEAM FACT.** At a normalized vorticity maximum, C0 gives strong contact equalities such as \(\nabla\omega=0\) at the contact point.
**TEAM WARNING.** Exact affine NS countermodels show that even stronger local equalities can coexist with nonconstant flow if boundedness/global admissibility is dropped.
Therefore do not prolong C0 into an infinite local jet tower without a propagation mechanism.
---
## J. Immediate extraction contract implied by the literature audit
### J01. Desired external output.
The weakest clean target currently visible is:
\[
\boxed{
U:\mathbb R^3\times(-\infty,0]\to\mathbb R^3
\text{ bounded mild ancient},
\qquad
[U]_{\rm Gal}\neq0.
}
\]
Do not require global \(L^2\), \(\dot H^{1/2}\), spectral tightness, or helicity unless separately supplied.
### J02. Why this is enough for Local NEO entry.
For bounded incompressible ancient mild \(U\),
\[
CU\equiv0
\Rightarrow
-\Delta U=C^2U=0
\Rightarrow
U\text{ spatially constant}.
\]
Within the admissible mild class this is the Galilean-null terminal form.
Thus
\[
[U]_{\rm Gal}\neq0
\Rightarrow
CU\not\equiv0.
\]
### J03. Two-stage normalization is preferred.
Stage 1:
\[
\text{bounded ancient compactness}
+
\text{Galilean nondegeneracy}.
\]
Stage 2:
\[
CU\not\equiv0
\to
\text{almost-maximal curl rescaling/contact normalization}.
\]
This avoids demanding that raw derivative normalization itself preserve bounded velocity.
### J04. Candidate theorem to search/prove.
**OPEN. Galilean Oscillation Nondegeneracy Lemma.** Find a scale-invariant local functional \(\mathcal O\), invariant under the correct Galilean frame change, such that
\[
z_*\text{ singular}
\Rightarrow
\limsup_{r\downarrow0}\mathcal O(u;Q_r(z_*))\ge\varepsilon_*>0.
\]
Then prove the lower bound survives the bounded-ancient extraction.
### J05. Galilean geometry must be exact.
A Galilean change modifies both velocity and spatial frame.
Do not confuse
\[
U\mapsto U+c
\]
as a pointwise quotient with the full spacetime symmetry
\[
U^{(c)}(x,t)=U(x+ct,t)-c
\]
(up to sign convention).
A local cylinder functional may need tilted cylinders or a moving center to be genuinely invariant.
### J06. Pressure normalization at extraction.
Use only pressure normalization required by the selected mild/suitable compactness theorem.
Do not introduce a new pressure state.
Do not require a global pressure Fourier representation unless integrability supports it.
---
## K. Immediate local classifier discipline
### K01. First split remains useful.
\[
\boxed{G0:CU\equiv0\quad\vee\quad G1:CU\not\equiv0.}
\]
G0 is the Galilean-null class for bounded ancient mild profiles.
Therefore the real difficulty of G0 lies in extraction nondegeneracy, not local curl algebra.
### K02. Curl contact remains a plausible second normalizer.
After G1 and a justified second normalization, aim for
\[
|\omega|\le1,
\qquad
|\omega(0,0)|=1.
\]
Do not assume this follows from the first bounded-velocity extraction without proof.
### K03. Exact scalar contact law.
For smooth terminal profiles,
\[
(\partial_t+U\cdot\nabla-\nu\Delta)\frac{|\omega|^2}{2}
=
\omega\cdot S\omega-
u|\nabla\omega|^2.
\]
At a true past-space-time maximum,
\[
\omega\cdot S\omega\ge\nu|\nabla\omega|^2\ge0.
\]
This licenses the finite contact split C0/C1.
### K04. C0 is not yet eliminated.
\[
C0:\quad \omega\cdot S\omega=0
\]
forces contact flatness including \(\nabla\omega=0\) at the normalized point.
It does not by itself propagate to \(CU\equiv0\).
### K05. Historical requirement before further C0 jets.
Before differentiating C0 again, search for a finite propagation input from one of:
- bounded ancientness;
- scale oscillation;
- near-maximum set geometry;
- strong maximum principle with a valid neighborhood sign condition;
- backward uniqueness / unique continuation with correctly verified hypotheses.
If none applies, stop.
### K06. C1 should first be compressed spectrally at the local matrix level.
For
\[
C1:\quad \xi\cdot S\xi>0,
\qquad \xi=\omega/|\omega|,
\]
inspect the eigenvalue allocation of the trace-free matrix \(S\) before launching higher Riccati descendants.
Miller's \(\lambda_2^+\) criterion gives historical reason to treat the middle strain eigenvalue as a high-value reader.
https://arxiv.org/abs/1710.05569
---
## L. Anti-loop rules strengthened by history
### L01.
Do not regenerate a descendant merely because the local equations permit it.
History rewards normal forms that reduce an analytic class, not infinite diagnostic trees.
### L02.
Do not replace missing compactness with ontology.
Compactness is an external analytic layer.
### L03.
Do not replace missing unique continuation with a formal jet argument.
Finite formal jet closure is not analytic continuation.
### L04.
Do not globalize local boundedness.
A bounded ancient profile need not have finite energy.
### L05.
Do not globalize curl spectral calculus without domain control.
The spectral literature is evidence for the compiler, not a free theorem on every terminal class.
### L06.
Do not call nontriviality nondegeneracy.
The hostile constant ancient mode must be removed explicitly.
### L07.
Do not call pointwise flatness rigidity.
Neighborhood/scale propagation is the missing ingredient.
### L08.
Do not dismiss pressure analytically just because it is compiled algebraically.
### L09.
Do not use a theorem that would also prove regularity for Tao's averaged NS unless the theorem uses some finer property absent from the averaged nonlinearity.
### L10.
Do not broaden the terminal class to arbitrary finite-energy weak solutions.
Buckmaster--Vicol shows weak-solution rigidity can fail badly outside the intended classical-derived/mild/suitable provenance.
---
## M. Literature-driven priority ranking for the team
### M01. Priority 1 -- Galilean oscillation extraction.
Find the weakest local scale-invariant quantity that:
1. vanishes on constant/Galilean-null profiles;
2. satisfies an epsilon-regularity theorem or can plausibly be inserted into one;
3. is stable under the extraction compactness;
4. does not require terminal global energy;
5. yields \([U]_{\rm Gal}\neq0\).
### M02. Priority 2 -- bounded ancient to curl contact.
Once nonconstant bounded ancient \(U\) exists, prove a clean second normalization giving an exact curl extremal contact while preserving enough bounded/mild structure for local regularity.
### M03. Priority 3 -- C0 finite propagation.
Seek one theorem that upgrades terminal point flatness to a neighborhood/scale statement.
Do not generate higher jets unless they feed that theorem.
### M04. Priority 4 -- C1 strain normal form.
Only after C0 is eliminated or sharply reduced, compress C1 using local matrix invariants/eigenvalues and existing Riccati/contact identities.
### M05. Priority 5 -- spectral upgrade only on licence.
If a later extraction theorem supplies \(L^2\), critical-space control, tightness, or another global domain, then activate
\[
H,\Lambda,\Pi_\pm,
\]
and the global spectral normalizer.
Until then keep it off.
---
## N. Current theorem target after the history audit
**OPEN.** Prove or locate an external theorem of the following shape.
There exists a local scale-invariant Galilean quantity \(\mathcal O\) and \(\varepsilon_*>0\) such that any genuine finite-energy classical singular endpoint \(z_*\) satisfies
\[
\limsup_{r\downarrow0}\mathcal O(u;Q_r(z_*))\ge\varepsilon_*.
\]
The same quantity must be stable enough under a blow-up sequence to produce a bounded mild ancient limit \(U\) with
\[
\mathcal O(U;Q_1)>0.
\]
Hence
\[
[U]_{\rm Gal}\neq0.
\]
For bounded incompressible mild ancient \(U\), this yields
\[
CU\not\equiv0.
\]
Only after this extraction theorem is secure should Local NEO normalize an exact curl contact and classify C0/C1.
---
## O. Team bottom line
The historical record gives a strong vote for the architecture
\[
\boxed{
\text{singularity}
\to
\text{scale-normalized terminal object}
\to
\text{rigidity}
}
\]
and a strong vote for using small local geometric readers rather than the whole trajectory.
It also gives a strong vote for curl as a serious structural operator.
It does **not** give a strong vote for pointwise finite jets alone.
The most literature-compatible NEO bet is therefore
\[
\boxed{
\text{bounded Galilean-nondegenerate ancient object}
+
\text{finite Local-NEO contact type}
+
\text{one finite scale-propagation invariant}
\to
\text{rigidity}.
}
\]
The current missing theorem is not another NEO descendant.
It is the Galilean nondegeneracy / oscillation extraction bridge.
