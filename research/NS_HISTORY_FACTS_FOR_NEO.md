# NS HISTORY FACTS FOR NEO
Purpose: a compact team-facing literature ledger for the active contract in `DEFINE_PROBLEM.md`.
Keep only facts that change an extraction, typing, normal-form, propagation, or anti-loop decision.
Do not read this file as a regularity proof.
Do not promote `TEAM DEDUCTION`, `CANDIDATE`, or `OPEN` to external theorems.
The NEO ontology remains frozen:
\[
u(t),\qquad P,\qquad C=\operatorname{curl},\qquad C^2=(-\Delta)P,\qquad t.
\]
The genetic equation remains
\[
\boxed{u_t=P[X_u,C]u-\nu C^2u.}
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
## A. Master dependency map after the literature audit
### A01. The proof is best split into five arrows.
**TEAM DEDUCTION.** The broad literature now suggests
\[
\boxed{\begin{aligned}
\mathrm{E1}:&\ \text{singular point}\to\text{nonvanishing scale activity modulo Galilean symmetry},\\
\mathrm{E2}:&\ \text{that activity}\to\text{bounded nondegenerate ancient compactness},\\
\mathrm{R1}:&\ \text{NEO contact type}\to\text{finite scale geometry},\\
\mathrm{R2}:&\ \text{finite scale geometry}\to\text{exact zero set / terminal trace},\\
\mathrm{P}:&\ \text{zero set}\to\text{global contradiction by external propagation}.
\end{aligned}}
\]
### A02. Historical support is uneven across the five arrows.
**TEAM STATUS.** E1 is close to known epsilon-regularity machinery; E2 is the hard extraction seam; R1 is the main NEO seam; R2 has several geometric precedents; P has backward-uniqueness/Carleman precedents but strict hypotheses.
### A03. Terminal-object architecture is mainstream NS methodology.
**EXTERNAL EXACT.** CKN/Lin localize singularity analysis; ESS uses blow-up plus backward uniqueness; Kenig--Koch uses concentration-compactness plus rigidity; KNSS and Albritton--Barker produce ancient objects.
**TEAM USE.** `DEFINE_PROBLEM.md` is historically aligned: compactness and propagation are external layers, not NEO primitives.
CKN: https://doi.org/10.1002/cpa.3160350604
Lin: https://doi.org/10.1002/(SICI)1097-0312(199803)51:3%3C241::AID-CPA2%3E3.0.CO;2-A
ESS: https://doi.org/10.1070/RM2003v058n02ABEH000609
Kenig--Koch: https://arxiv.org/abs/0908.3349
### A04. Exact terminal normal forms can later be decompactified.
**EXTERNAL EXACT.** Tao quantitatively replaces compactness and backward uniqueness in the ESS strategy by quantitative estimates and Carleman inequalities; Barker later localizes the quantitative strategy near a singular point.
**TEAM USE.** An ancient profile can be a discovery/compiler object first. A successful exact NEO zero set may later admit a finite-scale quantitative version.
Tao, *Quantitative bounds for critically bounded solutions to the Navier-Stokes equations*: https://arxiv.org/abs/1908.04958
Barker, *Localized quantitative estimates and potential blow-up rates for the Navier-Stokes equations*: https://arxiv.org/abs/2209.15627
### A05. Therefore NEO should optimize for exactness before quantitative stability.
**TEAM RULE.** Prefer a canonical exact zero set or finite normal form over a weak inequality with no known propagation route. Exact normal forms are candidates for later Carleman/quantitative stabilization.
---
## B. Ancient extraction and the Galilean seam
### B01. Bounded ancient mild solutions are a natural terminal class.
**EXTERNAL EXACT.** KNSS develop bounded ancient solutions and obtain them by blow-up rescaling in regularity arguments.
Paper: Koch--Nadirashvili--Seregin--Sverak, *Liouville theorems for the Navier-Stokes equations and applications*.
https://arxiv.org/abs/0709.3599
### B02. Nonzero ancient does not mean nonconstant modulo Galilean symmetry.
**EXTERNAL EXACT.** KNSS explicitly note that amplitude normalization can yield a nonzero bounded ancient profile while constants remain possible.
**TEAM RULE.** Never infer
\[
U\neq0\Rightarrow CU\neq0.
\]
The extraction seam is
\[
[U]_{\rm Gal}\neq0.
\]
Same paper: https://arxiv.org/abs/0709.3599
### B03. The ancient solution class is part of the theorem.
**EXTERNAL EXACT.** KNSS distinguish bounded mild ancient solutions from weaker ancient classes; weak formulations permit parasitic spatially constant time-dependent fields with compensating pressure.
**TEAM USE.** Preserve mild/suitable/classical-derived provenance through extraction.
### B04. Local singular points can produce nontrivial bounded mild ancient profiles.
**EXTERNAL EXACT.** Albritton--Barker obtain nontrivial mild bounded ancient solutions under localized singularity hypotheses, including boundary settings.
**TEAM USE.** Known extraction gives nontriviality, not automatically Galilean nondegeneracy.
https://arxiv.org/abs/1811.00507
### B05. Type-I structure can make the ancient class more rigid.
**EXTERNAL EXACT.** Albritton--Barker characterize local Type-I singularity in terms of nontrivial mild bounded ancient solutions with a Type-I condition.
**TEAM USE.** Extra scale law can materially shrink the terminal class; this belongs to extraction typing, not NEO ontology.
https://arxiv.org/abs/1811.00502
### B06. Galilean invariance is already used as a regularity tool.
**EXTERNAL EXACT.** Vasseur uses Galilean invariance in blow-up/higher-derivative estimates.
**TEAM USE.** Quotienting by constant frames is analytically motivated, not cosmetic.
https://arxiv.org/abs/0904.2422
### B07. A singularity-forces-oscillation principle has precedent.
**EXTERNAL EXACT.** Kozono--Sohr obtain a singular-time alternative involving sufficiently large oscillation around a weak limit when critical norm divergence does not occur in the other branch.
**TEAM USE.** An oscillation-based nondegeneracy theorem is historically plausible.
https://waseda.elsevierpure.com/en/publications/regularity-criterion-on-weak-solutions-to-the-navier-stokes-equat/
---
## C. Critical topology, profile compactness, and why scaling alone is insufficient
### C01. Critical scaling does not determine analytic behavior.
**EXTERNAL EXACT.** Koch--Tataru prove small-data well-posedness in critical \(BMO^{-1}\); Bourgain--Pavlovic prove norm inflation in the larger critical \(\dot B^{-1}_{\infty,\infty}\).
**TEAM USE.** `scale invariant` is not enough for an extraction quantity. The topology must also support stability/compactness.
Koch--Tataru: https://doi.org/10.1006/aima.2000.1937
Bourgain--Pavlovic: https://arxiv.org/abs/0807.0882
### C02. Critical elements are legitimate only when the critical class is controlled.
**EXTERNAL EXACT.** Kenig--Koch use concentration-compactness in a bounded critical class. A diverging critical norm cannot be scaled to one because the norm is invariant.
**TEAM RULE.** Do not identify arbitrary Clay blow-up with a Kenig--Koch critical element.
https://arxiv.org/abs/0908.3349
### C03. Minimal singular objects exist conditionally in controlled critical spaces.
**EXTERNAL EXACT.** Rusin--Sverak prove conditional existence of minimal \(\dot H^{1/2}\) singular data. Gallagher--Koch--Planchon develop profile decomposition/critical-element methods in \(L^3\) and critical Besov settings.
**TEAM USE.** Minimal-bad-object logic is sound when one owns the compactness defects.
Rusin--Sverak: https://arxiv.org/abs/0911.0500
Gallagher--Koch--Planchon: https://arxiv.org/abs/1012.0145
### C04. Profile decomposition identifies concrete compactness defects.
**EXTERNAL EXACT / INTERPRETATION.** Critical profile decompositions organize loss of compactness through translations/scales and profile splitting.
**TEAM DEDUCTION.** A Galilean terminal theorem should keep an explicit defect ledger:
\[
\boxed{
\text{space translation},\quad
\text{parabolic dilation},\quad
\text{Galilean frame},\quad
\text{profile splitting/tightness}.
}
\]
### C05. A correct-dimensional Galilean functional can still fail E2.
**TEAM RULE.** Even if \(\mathcal G\) is scale invariant and kills constants, extraction can lose nondegeneracy through optimizer escape, scale separation, or profile splitting. E2 must rule these out on one subsequence.
---
## D. Epsilon-regularity, local smoothing, and critical-radius selection
### D01. Singular points must fail every valid smallness criterion at arbitrarily small scale.
**EXTERNAL EXACT.** This is the contrapositive content of CKN/Lin and later epsilon-regularity theorems.
**TEAM USE.** E1 should be derived from a smallness criterion, not invented by normalization.
CKN: https://doi.org/10.1002/cpa.3160350604
Lin: https://doi.org/10.1002/(SICI)1097-0312(199803)51:3%3C241::AID-CPA2%3E3.0.CO;2-A
### D02. Local-in-space smoothing provides the dual viewpoint.
**EXTERNAL EXACT.** Jia--Sverak prove local-in-space estimates near initial time; Barker--Prange push localized smoothing to critical \(L^3\) and derive concentration near possible Type-I singularities.
**TEAM USE.** `local controlled data -> smoothing` contraposes to `singular point -> persistent critical activity`.
Jia--Sverak: https://arxiv.org/abs/1204.0529
Barker--Prange: https://arxiv.org/abs/1812.09115
### D03. Type-I concentration produces a distinguished parabolic scale in its regime.
**EXTERNAL EXACT / SCOPE.** Barker--Prange obtain a universal local \(L^3\) concentration lower bound at radius comparable to \(\sqrt{T_*-t}\) under Type-I hypotheses.
**TEAM USE.** A `critical radius` is a real NS phenomenon, but not yet an arbitrary-blowup theorem.
https://arxiv.org/abs/1812.09115
### D04. Pressure-free one-scale epsilon regularity is especially useful for Galilean work.
**EXTERNAL EXACT.** Wang--Wu--Zhou prove one-scale interior regularity from sufficiently small \(L^{5/2+\delta}\) velocity without pressure smallness in the hypothesis.
**TEAM USE.** This is a strong candidate engine for E1 after an exact Galilean transformation audit.
https://arxiv.org/abs/1811.09927
### D05. Campanato oscillation meets a real mean-drift obstruction.
**EXTERNAL EXACT.** In localized smoothing/Campanato arguments, Albritton--Barker--Prange control oscillation such as \(v-(v)_Q\), but a large mean velocity creates transport drift and must be handled separately.
**TEAM USE.** Algebraically subtracting a constant on a fixed vertical cylinder is not the exact Galilean quotient of the PDE.
https://arxiv.org/abs/2112.10705
### D06. Exact Galilean localization naturally uses tilted cylinders.
**TEAM DEDUCTION.** For constant frame velocity \(c\), use
\[
u^{(c)}(x,t)=u(x+c(t-t_0),t)-c
\]
(up to sign convention), with
\[
Q_r^c(z_0)=\{t_0-r^2<t<t_0,\ |x-x_0-c(t-t_0)|<r\}.
\]
### D07. Candidate Galilean scale activity.
**CANDIDATE.** For \(q>5/2\), test
\[
\mathcal G_q(u;z_0,r)
:=
\inf_c r^{1-5/q}\|u-c\|_{L^q(Q_r^c(z_0))}.
\]
It has the correct NS scaling and vanishes on constant/Galilean-null flows.
**OPEN.** The admissible set of frames, localization geometry, continuity under compactness, and suitability transform must be proved.
### D08. E1 and E2 must remain separate.
**TEAM DEDUCTION.** Literature suggests
\[
\boxed{\mathrm{E1}:\text{Galilean epsilon nonvanishing}}
\qquad
\boxed{\mathrm{E2}:\text{Galilean critical-radius compactness}.}
\]
E1 should show singularity forces \(\mathcal G_q\ge\varepsilon_q\) at small scales. E2 must choose scales/frames where this survives in a bounded mild ancient limit.
### D09. Critical activity and bounded ancient compactness may select different scales.
**OPEN / WARNING.** The scale optimizing \(\mathcal G_q\) need not be the scale producing a uniformly bounded ancient velocity sequence. The theorem must own both on one subsequence.
### D10. Amplitude and parabolic scales can separate in Type-II behavior.
**TEAM DEDUCTION.** Amplitude normalization uses roughly
\[
r_{amp}\sim\|u(t)\|_\infty^{-1},
\]
while endpoint parabolic scale is
\[
r_{par}\sim\sqrt{T_*-t}.
\]
If \(\|u(t)\|_\infty\sqrt{T_*-t}\to\infty\), then \(r_{amp}\ll r_{par}\). Critical concentration at \(r_{par}\) may look almost constant at \(r_{amp}\).
### D11. The frame optimizer itself can escape.
**OPEN / WARNING.** A tilted tube drifts \(|c|r^2\), i.e. \(|c|r\) radii over its lifespan. If \(|c|r\gg1\), an unconstrained optimizer can sample a remote corridor.
**TEAM USE.** Audit a controlled frame class, canonical local mean frame, or another quotient preventing optimizer escape.
### D12. Use constant Galilean frames unless acceleration is explicitly typed.
**TEAM RULE.** Arbitrary \(c(t)\) is not the same symmetry; accelerating frames introduce extra terms/pressure effects.
---
## E. Pressure and solution-class discipline
### E01. Pressure is reconstructible locally but analytically nontrivial.
**EXTERNAL EXACT.** Wolf develops local pressure projection/representation; Jiu--Wang--Zhou use local pressure projection in epsilon-regularity; Kwon analyzes pressure's role in local regularity.
**TEAM USE.** `pressure is a costume` is an ontology statement, not a statement that pressure causes no analytic seam.
Wolf: https://arxiv.org/abs/1611.01482
Jiu--Wang--Zhou: https://arxiv.org/abs/1805.04841
Kwon: https://doi.org/10.1016/j.jde.2023.01.049
### E02. Never turn local Hodge reconstruction into global spectral integrability.
**TEAM RULE.** A local pressure theorem does not grant
\[
U\in L^2,\quad U\in\dot H^{1/2},\quad HU\in L^2
\]
for a merely bounded ancient profile.
### E03. Weak finite-energy provenance is not automatically rigid.
**EXTERNAL EXACT.** Buckmaster--Vicol prove nonuniqueness in a finite-energy weak solution class.
**TEAM USE.** Terminal mild/suitable/classical-derived provenance is part of the extraction contract.
https://doi.org/10.4007/annals.2019.189.1.3
---
## F. Ancient Liouville, self-similar forms, and microscope dependence
### F01. General 3D bounded-ancient Liouville remains open in the needed strength.
**EXTERNAL EXACT.** KNSS prove partial Liouville results and explicitly leave the general three-dimensional bounded ancient problem beyond their methods.
**TEAM USE.** NEO must add structure; bounded ancientness alone is not the contradiction.
https://arxiv.org/abs/0709.3599
### F02. Liouville becomes stronger after real analytic restrictions are added.
**EXTERNAL EXACT.** Ancient rigidity is available in lower-dimensional, symmetric, Type-I, integrable, or growth-restricted subclasses.
**TEAM USE.** A terminal classifier must shrink the analytic class, not merely rename jets.
Survey: https://doi.org/10.1070/RM9822
### F03. Linear growth is a genuine danger for derivative normalization.
**EXTERNAL EXACT.** Lei--Zhang--Zhao obtain strong sublinear-growth Liouville results in axisymmetric/2D settings and exhibit linear-growth counterexamples in the same line.
**TEAM USE.** Raw gradient/curl normalization can cross from bounded velocity into an affine/linear-growth class where Liouville fails.
https://arxiv.org/abs/1701.00868
### F04. Therefore bounded velocity first, curl contact second is the safer ordering.
**TEAM DEDUCTION.** Preferred route:
\[
\text{bounded mild ancient }U+[U]_{\rm Gal}\neq0
\to
CU\not\equiv0
\to
\text{second curl-contact normalization}.
\]
### F05. Self-similar exclusions are historical prototypes of finite terminal classification.
**EXTERNAL EXACT.** Nečas--Růžička--Šverák and Tsai exclude backward self-similar profiles under stated integrability/local-energy hypotheses; Chae and Chae--Wolf treat asymptotically/discretely self-similar scenarios under additional hypotheses.
**TEAM USE.** Finite terminal branches can be killed when each branch carries a real profile equation/topology.
NRS: https://doi.org/10.1007/BF02551584
Tsai: https://doi.org/10.1007/s002050050099
Chae: https://arxiv.org/abs/math/0604234
Chae--Wolf: https://doi.org/10.1080/03605302.2017.1358275
### F06. Type-II analysis may use a different microscope.
**RECENT EXTERNAL PREPRINT / SCOPE.** Seregin's 2026 note studies specified potential Type-II scenarios using Euler scaling and Liouville theorems for ancient Euler classes.
**TEAM USE.** Extraction microscope need not be universal; NEO parentage can remain fixed while the effective square-anchor coefficient changes in a limit.
https://arxiv.org/abs/2606.29468
---
## G. Small readers, BMO/oscillation, and finite scale geometry
### G01. Small projections can carry regularity information.
**EXTERNAL EXACT.** Chae--Choe use only two vorticity components; Kukavica--Ziane use one directional regularity channel; Miller gives locally anisotropic vorticity criteria.
**TEAM USE.** A low-cardinality NEO reader can in principle carry a singular obstruction if coupled to the correct scale control.
Chae--Choe: https://ejde.math.txstate.edu/Volumes/1999/05/abstr.html
Kukavica--Ziane: https://doi.org/10.1063/1.2395919
Miller anisotropic: https://arxiv.org/abs/2002.02152
### G02. BMO is a natural functional language for oscillation rather than absolute level.
**EXTERNAL EXACT.** Kozono--Taniuchi show BMO control of velocity/vorticity can control breakdown; Grujić--Guberović localize the BMO vorticity criterion spatio-temporally.
**TEAM USE.** Mean oscillation appears naturally both near extraction (modulo baseline drift) and near rigidity (vorticity/stretching control).
Kozono--Taniuchi: https://doi.org/10.1007/s002090000130
Grujić--Guberović: https://doi.org/10.1016/J.ANIHPC.2009.11.009
### G03. Vorticity direction geometry can deplete stretching.
**EXTERNAL EXACT.** Constantin--Fefferman establish regularity under coherence assumptions on vorticity direction in high-vorticity regions; Grujić localizes vortex-stretching geometry to small cylinders.
**TEAM USE.** Local NEO variables \(\omega,S\) are compatible with serious geometric regularity mechanisms.
Constantin--Fefferman: https://iumj.org/article/3627/
Grujić localization: https://doi.org/10.1007/s00220-008-0726-8
### G04. Geometry of superlevel sets can be sufficient.
**EXTERNAL EXACT.** Grujić gives a criterion based on local one-dimensional sparseness of intense superlevel sets.
**TEAM USE.** A superlevel-set renderer of \(CU\) can be part of a finite normal form without becoming a new primitive.
https://doi.org/10.1088/0951-7715/26/1/289
### G05. A useful regularity criterion is not enough; extraction must force it.
**EXTERNAL EXACT / WARNING.** Albritton--Bradshaw give a simple proof that sufficient sparseness prevents singularity and critically examine claims that available a priori sparseness estimates close the scaling gap.
**TEAM RULE.** Never count a sufficient criterion as progress until a singular terminal extraction is shown to land in that criterion.
https://arxiv.org/abs/2110.02187
### G06. The strain middle eigenvalue is a high-value compressed reader.
**EXTERNAL EXACT.** Miller derives scale-critical blow-up/regularity conditions depending only on the positive part \(\lambda_2^+(S)\).
**TEAM USE.** C1 should be compressed through local strain spectrum before any Riccati descendant tower.
https://arxiv.org/abs/1710.05569
### G07. Distinguished maximum points are legitimate normalization sites, but neighborhood geometry still matters.
**EXTERNAL EXACT.** Nakai--Yoneda formulate criteria along maximum points using local geometric behavior around those points.
**TEAM USE.** Curl maxima are natural contacts; a pointwise Taylor jet alone is not the historical mechanism.
https://arxiv.org/abs/1408.0159
### G08. A very recent preprint follows an NEO-like exact-structure -> scale-geometry chain.
**RECENT PREPRINT / DO NOT PROMOTE.** Grujić 2026 studies a restricted class of critical-point singularities; the abstract chain uses vorticity-direction log-BMO, exact directional cancellation, singular-integral commutator depletion, Lorentz-Zygmund gain, superlevel sparseness, analyticity/harmonic measure, then singularity exclusion.
**TEAM USE.** This is a concrete recent precedent for
\[
\text{exact local structure}\to\text{finite scale geometry}\to\text{analytic rigidity},
\]
but its hypotheses are specialized and must not be imported into NEO without proof.
https://arxiv.org/abs/2607.08866
---
## H. Curl/helicity/operator history
### H01. Curl is historically an organizing operator, not merely an observable.
**EXTERNAL EXACT.** Moses constructs curl eigenmodes with one irrotational and two oppositely polarized rotational modes; Waleffe uses helical curl modes to compress triad taxonomy.
**TEAM USE.** Finite structural compression in curl variables has real precedent.
Moses: https://doi.org/10.1137/0121015
Waleffe: https://doi.org/10.1063/1.858309
### H02. Curl spectral projections enter rigorous regularity theory.
**EXTERNAL EXACT.** Neustupa--Penel formulate criteria using spectral projections of the self-adjoint curl operator; Lerner--Vigneron organize NS around curl diagonalization, \(( -\Delta)^{1/2}\), spin-definite fields, and helicity; Guo--Nie continue signed-curl criteria.
Neustupa--Penel: https://arxiv.org/abs/1207.3692
Lerner--Vigneron: https://arxiv.org/abs/2203.07950
Guo--Nie: https://doi.org/10.3934/dcdss.2024090
### H03. This supports the ontology but not a free spectral upgrade.
**TEAM RULE.** Spectral-curl literature normally owns global Fourier/function-space structure. A bounded ancient profile does not automatically license \(H,\Lambda,\Pi_\pm\) as global Hilbert-space tools.
\[
\boxed{\text{Local NEO first};\quad\text{Global spectral NEO only on domain licence}.}
\]
---
## I. Zero-set propagation and the quantitative upgrade path
### I01. Stokes/parabolic unique continuation is an external technology.
**EXTERNAL EXACT / SCOPE.** Fabre--Lebeau prove unique continuation for Stokes; Fabre's 1996 account records the result and control consequences.
**TEAM USE.** NEO does not need to regenerate unique continuation from the anchors.
Fabre: https://numdam.org/item/COCV_1996__1__267_0/
Fabre--Lebeau bibliographic reference is listed there: *Prolongement unique des solutions de l'équation de Stokes*, CPDE 21 (1996), 573--596.
### I02. ESS shows backward uniqueness can close an NS contradiction.
**EXTERNAL EXACT / SCOPE.** ESS use backward-uniqueness machinery for the vorticity/parabolic system in the endpoint \(L^3\) regularity proof.
**TEAM USE.** NEO may only need to force a terminal zero set/trace satisfying a verified propagation theorem, not prove general ancient Liouville.
https://doi.org/10.1070/RM2003v058n02ABEH000609
### I03. Tao shows qualitative propagation can be quantitative.
**EXTERNAL EXACT.** Tao replaces the ESS compactness/unique-continuation steps by quantitative substitutes and Carleman inequalities.
**TEAM USE.** Exact NEO zero sets are valuable even if the final mature proof later uses a small-defect quantitative version.
https://arxiv.org/abs/1908.04958
### I04. Barker localizes the quantitative ESS/Tao mechanism near a singular point.
**EXTERNAL EXACT.** Barker proves localized quantitative estimates and local \(L^3\) blow-up-rate consequences near a singular point.
**TEAM USE.** There is a plausible route from terminal-profile discovery back to finite-scale contradiction.
https://arxiv.org/abs/2209.15627
### I05. Recent forced quantitative work shows localization itself creates a typed forcing seam.
**RECENT PREPRINT / SCOPE.** Barker--Popkin 2026 obtain quantitative estimates for forced NS arising from localization and track the forcing in Carleman/Caccioppoli arguments.
**TEAM USE.** If a future NEO zero-set argument is localized quantitatively, the induced forcing must be typed rather than ignored.
https://arxiv.org/abs/2602.09951
### I06. Preferred division of labor.
**TEAM DEDUCTION.** Aim for
\[
\boxed{
\text{external extraction}
\to
\text{NEO finite zero/contact form}
\to
\text{external propagation}
\to
CU\equiv0
\to
[U]_{\rm Gal}=0.
}
\]
**TEAM RULE.** Any backward-uniqueness/Carleman invocation must state coefficient, growth, domain, terminal-trace, and forcing hypotheses exactly.
---
## J. Adversarial negative evidence
### J01. Coarse NS structure is provably insufficient.
**EXTERNAL EXACT.** Tao constructs finite-time blow-up for an averaged NS equation retaining the energy cancellation and much coarse harmonic-analytic structure.
**TEAM TEST.** Ask of every candidate rigidity lemma:
> Would essentially the same argument also prove regularity for Tao's averaged model?
If yes, it may not use enough exact NS structure.
https://arxiv.org/abs/1402.0290
### J02. Original finite energy does not become terminal finite energy under amplitude scaling.
**TEAM DEDUCTION.** For
\[
V(y)=M^{-1}u(x_0+y/M),
\]
\[
\|V\|_2^2=M\|u\|_2^2.
\]
**TEAM RULE.** Never assign global \(L^2\) to a bounded ancient amplitude limit by inheritance.
### J03. Critical norms cannot be normalized by parabolic scaling.
**TEAM RULE.** A diverging critical norm stays diverging under critical dilation. This blocks naïve import of critical-element normalization to arbitrary Clay blow-up.
### J04. Nonzero is not nonconstant; curl-active is not globally spectral.
**TEAM RULE.** Keep these implications separate:
\[
U\neq0\not\Rightarrow CU\neq0,
\qquad
CU\neq0\not\Rightarrow U\in L^2\text{ or global spectral domain}.
\]
### J05. Flat point contact is not local rigidity.
**TEAM FACT.** C0 at a normalized vorticity maximum gives strong point equalities such as \(\nabla\omega=0\), but exact affine NS countermodels show stronger local equalities can coexist with nonconstant flow when boundedness/global admissibility is dropped.
**TEAM RULE.** Do not prolong C0 into an infinite jet tower without a finite propagation mechanism.
---
## K. Current extraction contract
### K01. Weakest desired external output.
\[
\boxed{
U:\mathbb R^3\times(-\infty,0]\to\mathbb R^3
\text{ bounded mild ancient},
\qquad
[U]_{\rm Gal}\neq0.
}
\]
Do not require terminal global \(L^2\), \(\dot H^{1/2}\), Fourier tightness, or helicity unless separately supplied.
### K02. This output is enough to enter Local NEO.
For bounded incompressible mild ancient \(U\),
\[
CU\equiv0
\Rightarrow
C^2U=-\Delta U=0
\Rightarrow
U\text{ spatially constant}.
\]
Within the admissible mild class this is the Galilean-null class. Hence
\[
[U]_{\rm Gal}\neq0\Rightarrow CU\not\equiv0.
\]
### K03. Preferred two-stage normalization.
\[
\boxed{
\text{bounded ancient + Galilean nondegeneracy}
\to
\text{curl-active}
\to
\text{second curl-contact normalization}.
}
\]
Do not make raw derivative normalization carry bounded-velocity compactness unless a theorem proves it.
### K04. Current E1 candidate.
**OPEN / NEAR-KNOWN.** Audit whether pressure-free one-scale epsilon regularity plus exact constant Galilean symmetry yields, for some \(q>5/2\),
\[
z_*\text{ singular}
\Rightarrow
\mathcal G_q(u;z_*,r)\ge\varepsilon_q
\quad\forall r\ll1.
\]
The proof must transform the suitable/local-energy class and tilted spacetime cylinder exactly.
### K05. Current E2 theorem target.
**OPEN. Galilean Critical-Radius Compactness.** Prove existence of \(r_k\downarrow0\) and constant frames \(c_k\) such that exact Galilean-rescaled solutions converge locally to bounded mild ancient \(U\) and
\[
\mathcal G_q(U;0,1)\ge\varepsilon_*>0.
\]
Then \([U]_{\rm Gal}\neq0\) and \(CU\not\equiv0\).
### K06. E2 should explicitly close the four compactness defects.
**TEAM CHECKLIST.** On the chosen subsequence, account for:
1. space translation;
2. parabolic dilation;
3. Galilean frame drift/escape;
4. profile splitting or loss of tightness.
If one is merely assumed away, E2 is not proved.
---
## L. Current Local-NEO classifier contract
### L01. First classifier remains
\[
\boxed{G0:CU\equiv0\quad\vee\quad G1:CU\not\equiv0.}
\]
G0 is Galilean-null for bounded mild ancient profiles; extraction nondegeneracy should remove it.
### L02. Curl-active second normalization remains a candidate.
After justified compactness/rescaling, seek
\[
|\omega|\le1,
\qquad
|\omega(0,0)|=1.
\]
### L03. Exact contact law.
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
Thus
\[
\boxed{C0:\omega\cdot S\omega=0\quad\vee\quad C1:\omega\cdot S\omega>0.}
\]
### L04. C0 is a contact type, not yet a terminal normal form.
C0 forces point flatness such as \(\nabla\omega=0\) at contact. It does not currently propagate to \(CU\equiv0\).
### L05. R1 target for C0 is scale geometry, not the next jet.
**OPEN.** Ask whether C0 + bounded ancientness forces one finite property of
\[
\{(x,t):|\omega(x,t)|>1-\varepsilon\}
\]
on a shrinking cylinder: coherence, sparseness, oscillation control, or another NEO-compiled renderer.
If no finite property appears, stop.
### L06. C1 should be compressed by strain spectrum before Riccati.
Diagonalize
\[
Se_i=\lambda_i e_i,
\qquad
\lambda_1\le\lambda_2\le\lambda_3,
\qquad
\lambda_1+\lambda_2+\lambda_3=0.
\]
First split
\[
\boxed{\lambda_2\le0\quad\vee\quad\lambda_2>0.}
\]
Miller's \(\lambda_2^+\) criterion makes this a high-value finite reader.
### L07. Finite normal form should now be thought of as three coordinates.
**TEAM DEDUCTION.** Candidate architecture:
\[
\boxed{\mathcal N=(\mathcal A,\mathcal G,\mathcal Z)}
\]
where
\[
\mathcal A=\text{finite algebraic contact type},
\quad
\mathcal G=\text{one finite scale-geometry type},
\quad
\mathcal Z=\text{zero-set/terminal-trace class}.
\]
The desired chain is
\[
\mathcal A\to\mathcal G\to\mathcal Z\to\text{external propagation}\to\bot.
\]
### L08. A scale/set renderer does not enlarge the ontology.
**TEAM RULE.** Superlevel sets, tilted cylinders, coherence, or sparseness derived from \(U,CU,S\) are renderers/conditions, not new primitives.
---
## M. Anti-loop rules strengthened by the literature
### M01.
Do not generate a descendant merely because the compiler permits it. Progress must eliminate a terminal class, lower an extraction/propagation gap, create finite coercivity, or contradict the contract.
### M02.
Do not replace missing compactness with ontology. Compactness is external analysis.
### M03.
Do not replace unique continuation by formal jet closure. Finite jet algebra is not analytic continuation.
### M04.
Do not globalize bounded ancientness into finite energy or global spectral domain.
### M05.
Do not call nontriviality Galilean nondegeneracy.
### M06.
Do not call pointwise C0 flatness rigidity. R1 requires scale propagation.
### M07.
Do not dismiss pressure analytically because it is compiled algebraically.
### M08.
Do not use a beautiful sufficient regularity criterion unless extraction is proved to force it.
### M09.
Do not use a candidate mechanism that would work unchanged for Tao's averaged NS unless the true-NS structure used is identified.
### M10.
Do not broaden the terminal class to arbitrary weak solutions; provenance is part of the theorem.
### M11.
Do not infer compactness from critical scaling alone; Koch--Tataru versus Bourgain--Pavlovic is the standing warning.
### M12.
Do not assume one singular microscope works for all Type-I/Type-II regimes.
---
## N. Team priority ranking
### N01. Priority 1 -- prove/audit E1.
Turn the Wang--Wu--Zhou pressure-free one-scale theorem plus exact Galilean symmetry into a rigorously typed Galilean epsilon-nonvanishing lemma, or identify the exact obstruction.
### N02. Priority 2 -- solve E2.
Build a critical-radius scale/frame selection that preserves both bounded ancient compactness and positive Galilean quotient activity while closing the four defect channels.
### N03. Priority 3 -- bounded ancient to true curl contact.
Once E2 is secure, prove the second curl normalization without losing the mild/bounded structure needed by local parabolic regularity.
### N04. Priority 4 -- R1 on C0.
Seek one finite scale geometry of the near-maximal curl set. No higher jet unless it feeds that geometry.
### N05. Priority 5 -- R1/R2 on C1.
Use local strain spectrum \(\lambda_2\) before Riccati; seek a finite geometry/zero-set consequence, not a descendant tower.
### N06. Priority 6 -- propagation audit.
For any proposed zero set, find the exact Stokes/parabolic unique-continuation or backward-uniqueness theorem and check all coefficient/growth/domain hypotheses.
### N07. Priority 7 -- global spectral upgrade only on licence.
Activate \(H,\Lambda,\Pi_\pm\) globally only if extraction later supplies the required integrability/domain/tightness.
---
## O. Current theorem targets
### O01. Near-term theorem target -- Galilean epsilon nonvanishing.
**OPEN / NEAR-KNOWN.** Find \(q>5/2\), \(\varepsilon_q>0\) and a correctly defined Galilean local activity such that
\[
z_*\text{ singular}\Rightarrow\mathcal G_q(u;z_*,r)\ge\varepsilon_q
\quad\forall r\ll1.
\]
### O02. Main extraction theorem -- Galilean critical-radius compactness.
**OPEN.** Extract bounded mild ancient \(U\) with
\[
\mathcal G_q(U;0,1)>0,
\]
without assuming terminal global \(L^2\), \(\dot H^{1/2}\), Fourier tightness, or global spectral calculus.
### O03. Main NEO rigidity theorem after extraction.
**OPEN.** From a true curl contact, prove a finite implication
\[
C0\vee C1
\Longrightarrow
\mathcal G_{scale}
\Longrightarrow
\mathcal Z,
\]
where \(\mathcal G_{scale}\) is one finite NEO-derived scale geometry and \(\mathcal Z\) is an exact zero set/terminal trace suitable for a verified external propagation theorem.
---
## P. Team bottom line
The historical record now supports a sharper programme than the original vague `terminal object -> rigidity` slogan:
\[
\boxed{
\text{singularity}
\to
\text{Galilean-critical activity}
\to
\text{bounded nondegenerate ancient object}
\to
\text{finite Local-NEO contact type}
\to
\text{finite scale geometry}
\to
\text{exact zero set}
\to
\text{external propagation}
\to
\bot.
}
\]
The strongest historical vote is for:
- endpoint zooming rather than whole-trajectory surveillance;
- small local readers plus correct scale information;
- exact symmetry quotienting;
- explicit compactness-defect accounting;
- finite geometric classifications rather than infinite jets;
- zero-set production followed by external unique continuation;
- eventual quantitative decompactification via Carleman estimates.
The weakest historical support is for:
- raw amplitude nontriviality as nondegeneracy;
- raw curl normalization as the first microscope;
- pointwise finite jets as a complete classifier;
- global spectral NEO on a merely bounded ancient profile;
- one universal scale for all blow-up regimes.
The research frontier is therefore concentrated in two arrows:
\[
\boxed{
\mathrm{E2}:\ \text{Galilean critical activity}\to\text{bounded nondegenerate ancient compactness}
}
\]
and
\[
\boxed{
\mathrm{R1/R2}:\ \text{Local-NEO contact}\to\text{finite scale geometry}\to\text{zero set}.
}
\]
Everything else should be treated as supporting technology until one of these arrows moves.
