# DEFINE THE PROBLEM
## Clay -> singular endpoint -> NEO Singularity Normal Form

This file is the active problem contract for the Wang--Navier--Stokes programme.
The long exploratory files are archived under `history/`.
They remain evidence and audit history, but they are no longer the proof surface.
The canonical compiler is `core/NEO/NEO_ANCHOR_COMPILER.md`.
This file states what problem we are actually trying to solve and how NEO should be used.

## 0. Status labels

Use the labels **EXTERNAL EXACT**, **NEO EXACT**, **DEDUCTION**, **CANDIDATE**, **OPEN**, and **AUDIT**.
Do not silently promote a compactness heuristic, numerical test, terminal picture, or local normal form into a global regularity theorem.
The ontology is frozen unless a genuine obstruction forces an extension.

## 1. Clay target -- EXTERNAL EXACT

We target Clay assertion (A) on \(\mathbb R^3\):
\[
\nu>0,\qquad f=0,
\]
with smooth divergence-free rapidly decaying initial data \(u_0\).
The equation is
\[
\partial_tu+(u\cdot\nabla)u=-\nabla p+\nu\Delta u,
\qquad \nabla\cdot u=0.
\]
Let \(T_*\) be the maximal classical smooth lifespan.
The desired conclusion is
\[
\boxed{T_*=\infty.}
\]
Equivalently, the contradiction problem is
\[
\boxed{T_*<\infty\quad\Longrightarrow\quad\bot.}
\]
We do not need to classify all turbulence, all transfers, or every transient geometry.
We need only exclude a finite singular endpoint.

## 2. Standard endpoint information -- EXTERNAL EXACT

Smooth rapidly decaying data lie in \(L^2\cap\dot H^{1/2}\) and in every classical Sobolev space.
Classical/mild uniqueness identifies the classical solution with the local mild solution on the common lifespan.
Kenig--Koch implies that a mild solution bounded in \(\dot H^{1/2}\) cannot become singular in finite time.
Hence
\[
\boxed{
T_*<\infty
\Longrightarrow
\sup_{t<T_*}\|u(t)\|_{\dot H^{1/2}}=\infty.
}
\]
This is a necessary endpoint fact, not yet a terminal compactness theorem.
Because \(\dot H^{1/2}\) is Navier--Stokes scale invariant, one cannot normalize an arbitrarily diverging critical norm to one by parabolic scaling.
Therefore the Kenig--Koch critical-element construction must not be assumed to describe every possible Clay blow-up.

## 3. NEO core -- NEO EXACT

The fixed typed anchors are
\[
\boxed{
u(t),\qquad P,\qquad C=\operatorname{curl},\qquad C^2=(-\Delta)P,\qquad t.}
\]
On the physical incompressible state, \(Pu=u\) and \(C^2u=-\Delta u\).
With \(X_av=a\times v\), the projected Navier--Stokes equation is
\[
\boxed{
 u_t=P[X_u,C]u-\nu C^2u.
}
\]
The matrix face of \(C\) generates constant-coefficient spatial differentiation.
The spectral face of \(C\) generates \(H=\operatorname{sgn}C\), \(\Lambda=|C|\), helicity projectors, and admissible isotropic spectral readers when the function spaces permit them.
The square \(C^2\) is the physical heat generator.
Transport, pressure, strain, vorticity stretching, hard crossing, spectral jets, variational descendants, and parabolic descendants are compiled costumes rather than new primitive physics.

## 4. What the old programme accomplished -- DEDUCTION

The archived work was not wasted.
It established that many apparently different NS mechanisms repeatedly collapse to the same small curl-genetic grammar.
It exposed exact parentage of pressure/Hodge faces, helicity crossing, regeneration, spectral work, Riccati geometry, Codazzi-type renderings, and order-two spectral normal forms.
It also revealed a methodological danger:
\[
\text{defect}\to\text{next defect}\to\text{next jet}\to\text{next seam}\to\cdots.
\]
Formal finite-jet closure guarantees that NEO can keep generating descendants.
Therefore successful regeneration of another descendant is no longer evidence of analytic closure.

## 5. Strategic correction -- RESEARCH RULE

The earlier implicit task was too strong:
\[
\boxed{
\text{reconstruct and control every metamorphosis of an arbitrary NS trajectory}.
}
\]
Clay does not ask for that.
The correct target is
\[
\boxed{
\text{classify and exclude what must survive after zooming into a hypothetical singular endpoint}.
}
\]
Thus
\[
\boxed{
\text{reconstruction completeness}\ne\text{control completeness}.
}
NEO is strongest as a reconstruction, normalization, and rigidity compiler.
It need not be a surveillance system for the entire pre-singular history.

## 6. Old question versus new question

The old question was
\[
\boxed{\text{How can blow-up happen along the whole trajectory?}}
\]
The new question is
\[
\boxed{\text{What object must exist if blow-up happens?}}
\]
Both begin by assuming \(T_*<\infty\).
The difference is the object of analysis.
The old route tries to control \(u(t)\) for all \(t<T_*\).
The new route tries to extract one normalized singular object \(U\) and prove that no admissible \(U\) exists.
Schematically,
\[
\boxed{
T_*<\infty
\to U
\to\text{finite NEO normal forms}
\to\bot.
}
\]

## 7. External singular microscope -- EXTERNAL EXACT / SCOPE

Known blow-up-rescaling theory for suitable weak solutions shows that a singular point can generate a non-trivial mild bounded ancient solution in \(\mathbb R^3\) by zooming in.
This is the correct external analytic doorway for the terminal programme.
The extracted object is ancient:
\[
U:\mathbb R^3\times(-\infty,0]\to\mathbb R^3,
\]
and satisfies Navier--Stokes in the appropriate mild sense.
The word **bounded** here concerns velocity, not finite global energy.
Do not infer
\[
U\in L^2(\mathbb R^3),
\qquad
U\in\dot H^{1/2}(\mathbb R^3),
\]
or global frequency tightness unless an extraction theorem explicitly supplies them.
This typing restriction is essential.

## 8. Local NEO first, spectral NEO only when licensed -- RESEARCH RULE

For a bounded mild ancient terminal object, local parabolic regularity makes the following natural NEO faces legitimate:
\[
\nabla U,\quad CU,\quad C^2U,\quad S=\operatorname{sym}\nabla U,
\quad \omega=CU,
\]
together with local transport, vorticity, strain/Riccati, pressure-Hessian, and finite local jet identities.
Global spectral readers such as \(H\), \(\Lambda\), affine spectral Gram matrices, and global \(L^2\) helicity decompositions are conditional.
They may be activated only after the extraction class supplies the required integrability/domain control.
Hence
\[
\boxed{
\text{Local NEO = default terminal compiler},
\qquad
\text{Global spectral NEO = typed upgrade}.
}
\]

## 9. Galilean quotient -- NEO EXACT

Constant velocity is invisible to curl:
\[
C(U+c)=CU.
\]
It is also removable by Galilean symmetry.
Therefore terminal local geometry should be regarded modulo constants:
\[
\boxed{[U]_{\rm Gal}=U+\mathbb R^3.}
\]
If a bounded incompressible ancient field satisfies \(CU=0\), then \(-\Delta U=C^2U=0\).
Each spatial component is bounded harmonic, hence spatially constant.
For the admissible mild class, the curl-null terminal form is therefore the Galilean-null class.
This is a legitimate NEO zero set, not a loss of physical information.

## 10. First terminal split -- CANDIDATE NORMALIZER

The first terminal classifier is deliberately small:
\[
\boxed{
\text{G0: }CU\equiv0
\qquad\vee\qquad
\text{G1: }CU\not\equiv0.
}
\]
G0 is Galilean-null and should be killed or shown incompatible with singular extraction by the external non-degeneracy argument.
G1 is the curl-active class and is the natural input to the local NEO compiler.
No global helicity machinery is needed at this first pass.

## 11. Galilean non-degeneracy seam -- OPEN

A non-trivial bounded ancient blow-up limit need not automatically mean non-constant modulo Galilean symmetry.
Therefore the full Clay route needs an extraction/non-degeneracy statement strong enough to prevent the singular core from disappearing into a constant ancient limit.
Call the required statement:
\[
\boxed{\text{Galilean Nondegeneracy Theorem}.}
\]
Its desired content is that a genuine finite-energy singular endpoint produces at least one terminal limit with
\[
CU\not\equiv0,
\]
or another equivalent NEO-visible non-degeneracy normalization.
This is an analytic extraction problem, not a new NEO primitive.

## 12. Curl-active normalization -- CANDIDATE / EXTERNAL COMPACTNESS NEEDED

Suppose the terminal ancient object is curl-active.
Let
\[
\omega=CU.
\]
Bounded ancient regularity suggests that \(\omega\) and its local derivatives are bounded on compact time interiors.
After scaling, translation, and a compactness pass, the natural desired terminal normalization is
\[
\boxed{
|\omega(x,t)|\le1,
\qquad
|\omega(0,0)|=1,
\qquad
U(0,0)=0
}
\]
modulo the appropriate Galilean choice.
This converts a possible singular terminal object into an exact curl-contact object.
The existence of such a normalized subsequential profile must be proved within the extraction class; it is not simply assumed.

## 13. First exact local contact law -- NEO EXACT ONCE NORMALIZED

The pressure-free vorticity face is
\[
\boxed{
(\partial_t+U\cdot\nabla-\nu\Delta)\omega
=(\omega\cdot\nabla)U.
}
\]
Writing \(S=\operatorname{sym}\nabla U\),
\[
\boxed{
(\partial_t+U\cdot\nabla-\nu\Delta)\frac{|\omega|^2}{2}
=\omega\cdot S\omega-\nu|\nabla\omega|^2.
}
\]
At an exact normalized past-space-time maximum of \(|\omega|\), the maximum principle forces
\[
\boxed{
\omega\cdot S\omega\ge\nu|\nabla\omega|^2\ge0.
}
\]
Thus a curl-active terminal profile cannot be compressive in its maximal-vorticity direction.
It must be either flat at contact or genuinely extensional.
This is a terminal restriction, not a global regularity theorem.

## 14. First two local terminal forms -- CANDIDATE CLASSIFICATION

The curl-contact split is
\[
\boxed{
\text{C0: }\omega\cdot S\omega=0,
\qquad
\text{C1: }\omega\cdot S\omega>0.
}
\]
At C0, the exact contact law also forces the square-anchor angular cost to vanish at the contact point:
\[
\nabla\omega=0
\]
there, together with the corresponding maximum-principle flatness conditions that can be justified from the chosen terminal normalization.
C0 is therefore the first rigidity target.
C1 is the genuinely extensional terminal geometry and is the proper place to activate the local Riccati/contact compiler.
The order is important: do not deploy the full Riccati machinery before the terminal extraction has forced us into C1.

## 15. Relation to the bounded ancient Liouville problem -- OPEN

A theorem saying that every bounded mild ancient 3D Navier--Stokes solution is constant would kill all curl-active terminal profiles.
The general three-dimensional bounded-ancient Liouville problem is not known in this full strength.
Therefore NEO Singularity Normal Form is not a trivial restatement of an already solved theorem.
Its purpose is to add structure to the ancient object until the relevant class is smaller than the general bounded-ancient class.
Progress is measured by elimination of admissible terminal forms, not by generation of more diagnostics.

## 16. Candidate proof architecture

The active programme is
\[
\boxed{
\begin{array}{c}
T_*<\infty\\
\Downarrow\\
\text{external blow-up extraction}\\
\Downarrow\\
\text{Galilean-nondegenerate terminal object}\\
\Downarrow\\
\text{local NEO normalizer}\\
\Downarrow\\
\text{finite terminal forms}\\
\Downarrow\\
\text{Liouville / rigidity contradiction}.
\end{array}
}
\]
The external extraction layer and the NEO structural layer must remain logically separate.
Compactness is not a NEO primitive.
NEO parentage is not a compactness theorem.

## 17. What NEO is expected to contribute

NEO should contribute exactly what it does best:

- canonical quotienting of irrelevant gauges;
- exact local curl and square-anchor normal forms;
- exact zero-set and contact classifications;
- finite algebraic alternatives when a continuum contact tries to persist;
- parentage checks preventing fake mechanisms from entering the proof;
- typed decisions about which spectral tools are legal on the extracted class.

NEO is not required to estimate every interaction of the raw trajectory.
NEO is not required to regenerate concentration compactness or unique continuation from the anchors.
NEO is not strengthened by naming the next defect if that defect does not remove a terminal form.

## 18. Anti-loop protocol -- RESEARCH RULE

A new calculation counts as progress only if it does at least one of the following:

1. proves a stronger singular-profile extraction or non-degeneracy statement;
2. eliminates one admissible terminal normal form;
3. lowers a real derivative/integrability requirement needed for rigidity;
4. produces coercivity paid by an already finite physical budget;
5. yields a direct contradiction with the terminal extraction contract.

If a calculation only moves the unknown freedom into the next NEO jet, record its parentage and stop.
Do not restart trajectory surveillance under terminal vocabulary.
Do not turn the ancient solution into a new infinite descendant tower.

## 19. Immediate research targets

The next targets, in order, are:

**Target A -- Galilean nondegeneracy.**
Determine exactly what known singular-point extraction guarantees beyond non-triviality, and find a NEO-visible normalization that cannot collapse to a constant ancient profile.

**Target B -- C0 rigidity.**
Assuming an exact curl-contact terminal profile with zero stretching at the maximum, determine whether the flatness forced by the vorticity equation propagates to \(CU\equiv0\).

**Target C -- C1 finite normal form.**
Only if C0 is eliminated, apply the already-compiled local Riccati/contact normalizer to the extensional terminal point and seek a finite alternative: transverse escape, finite directions, curl-null, or explicit square-anchor visibility.

**Target D -- typed spectral upgrade.**
If extraction later provides global integrability/tightness, activate the spectral NEO results such as affine bend and finite signed-curl closure. Do not use them earlier.

## 20. Success criterion

The programme succeeds if we prove a finite statement of the form
\[
\boxed{
T_*<\infty
\Longrightarrow
U\in\mathcal N_1\cup\cdots\cup\mathcal N_m,
}
\]
where each \(\mathcal N_j\) is an exact NEO terminal normal form, followed by
\[
\boxed{
\mathcal N_j=\varnothing
\quad\text{for every admissible non-degenerate singular profile}.
}
\]
Then
\[
\boxed{T_*<\infty\Longrightarrow\bot.}
\]
The number of regenerated NS costumes is irrelevant.
The number of surviving singular normal forms is the metric that matters.

## 21. What is not claimed

No global regularity theorem is claimed here.
No exhaustive singular-profile classification is claimed here.
No proof of Galilean nondegeneracy is claimed here.
No proof of the general bounded-ancient Liouville conjecture is claimed here.
No global \(L^2\) property is assigned to an ancient terminal limit without proof.
No local NEO contact identity is globalized without an extraction/compactness argument.

## 22. Compact definition of the problem

The problem is no longer:
\[
\text{understand every way 3D Navier--Stokes can transform before }T_*.
\]
The problem is:
\[
\boxed{
\begin{gathered}
\text{Assume a finite Clay singular endpoint.}\\
\text{Extract a non-degenerate scale-normalized terminal object.}\\
\text{Use the smallest legally typed part of NEO to put it into finite normal form.}\\
\text{Prove every such normal form impossible.}
\end{gathered}
}
\]
This is the active meaning of **NEO Singularity Normal Form**.

## 23. External references used by this contract

1. Charles L. Fefferman, *Existence and Smoothness of the Navier--Stokes Equation*, Clay Mathematics Institute official problem description.
2. Carlos E. Kenig and Gabriel S. Koch, *An alternative approach to regularity for the Navier--Stokes equations in critical spaces*, arXiv:0908.3349.
3. Dallas Albritton and Tobias Barker, *Localised necessary conditions for singularity formation in the Navier--Stokes equations with curved boundary*, arXiv:1811.00507.
4. G. Koch, N. Nadirashvili, G. Seregin, V. Sverak, *Liouville theorems for the Navier--Stokes equations and applications*, arXiv:0709.3599.

The references provide the external PDE scope.
They do not change the NEO ontology.
