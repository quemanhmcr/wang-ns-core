# Theory 2 Self-Describing Algebra Lab

## 0. Research status

This note records a research-only campaign built from

```text
origin/main = fcb809f7b825606d2aba9709ac0e63c9e78cd717
branch      = research/theory2-universal-compiler
```

The purpose is to test a claim **strictly stronger** than the current Core-3 target

\[
\text{Curl-Spectral Formation-Geometry Completeness}.
\]

Nothing in this note is promoted automatically to a continuum Navier--Stokes theorem.
The campaign deliberately mixes:

- exact finite metric-Lie models;
- the canonical 28-dimensional physical coordinate lab;
- exact full-helical Fourier actions without a projected Lie bracket;
- negative controls designed to destroy attractive but false formulations.

The strongest interpretation surviving the campaign is:

\[
\boxed{
\textbf{Theory 2 behaves like a self-describing curl--mother generator--relations language.}
}
\]

At a generic interacting finite state:

1. \(C\) and one generic mother \(E_u\) can generate the full finite observable matrix algebra;
2. low-degree noncommutative relations of \((C,E_u)\) contain the curl spectral law and physical interaction-incidence information;
3. a relation extracted from one generic snapshot can generalize to unseen states and reveal state-independent selection rules;
4. polarized differential data \((E,K)\) then identifies the formation connection/grammar at generic points;
5. the higher Cartan tower adds no new generic local connection rank, but remains essential at singular spectral strata;
6. viscosity \(\nu\) remains a separate dissipative scalar calibration.

This is stronger than saying that Theory 2 is state-complete or geometry-complete.  It suggests that the representation can contain both an **operator alphabet** and part of the **laws obeyed by that alphabet**.

---

# I. Starting point: what was already known

Core 3 before this campaign had the spectral splitting

\[
\nabla=V+B,
\qquad [V,C]=0,
\qquad E=[B,C],
\]

and the curvature mother

\[
K=[R,C].
\]

The previous reconstruction campaign showed, in exact finite metric-Lie models, that after \(E\) determines the cross-sheet connection \(B\), the hidden within-sheet connection \(V\) enters \(K\) through an affine-linear Codazzi measurement map

\[
K=K_B+\mathcal A_{C,E}(V).
\]

When \(\mathcal A_{C,E}\) has full rank,

\[
(g,C,E,K)
\Longrightarrow
\nabla
\Longrightarrow
T,R,\mathcal J.
\]

That result led to the candidate phrase

\[
\text{Curl-Spectral Formation-Geometry Completeness}.
\]

The new question was more severe:

> Once geometry can be reconstructed, is Theory 2 merely a complete coordinate system, or is there a much smaller algebraic object inside it that generates the whole local observable theory and carries its own structural relations?

That question produced the present campaign.

---

# II. New conjectural hierarchy

The experiments now suggest four distinct levels of completeness.

## II.1. State completeness

On the canonical smooth periodic physical core,

\[
E_u\Longleftrightarrow u
\]

modulo the already-typed Killing/Galilean sector.

This is the existing theorem-level parent result.

## II.2. Geometric completeness

The full differential data

\[
(g,C,E(\cdot),K(\cdot,\cdot))
\]

generically reconstruct the formation connection in the tested finite metric-Lie category.

This is conditional exact algebra plus strong audit evidence, not yet the infinite-dimensional theorem.

## II.3. Algebraic universality

A much smaller object may already provide an operator language:

\[
\boxed{
(C,E_{u_*})
}
\]

for one generic interacting state \(u_*\).

The central experimental claim is that, in rich finite physical windows,

\[
\boxed{
\operatorname{Alg}(C,E_{u_*})=\operatorname{End}(V).
}
\]

This is stronger than injectivity of \(u\mapsto E_u\).  It says one state-dependent mother, together with the fixed curl operator, can generate every matrix observable in the finite representation.

## II.4. Self-description / law archaeology

The strongest phenomenon is that the **relations** among words in \(C,E_{u_*}\) are not arbitrary numerical dependencies.  Their first layers separate into:

- spectral relations inherited from the curl polynomial;
- extra relations caused by the physically allowed interaction incidence.

A relation extracted from one generic state can then predict a state-independent selection rule obeyed by all unseen mother states in the same finite physical category.

That is the sense in which Theory 2 begins to look **self-describing**.

---

# III. Tribunal A — generic finite-jet rank collapse

The first stronger test asked whether the apparently infinite tower

\[
E,\ K,\ dK,\ d^2K,\ldots
\]

contains infinitely many independent local connection degrees of freedom.

In six dimensions a metric-compatible connection has

\[
6\binom62=90
\]

skew connection coefficients.

The audit `finite_jet_rank_collapse.py` linearized the complete tower with respect to all 90 coefficients.

## III.1. Generic spectra

For the tested generic multiplicity patterns:

### Spectrum \(2+2+2\)

\[
\operatorname{rank}DE=72,
\]

but

\[
\boxed{
\operatorname{rank}D(E,K)=90.
}
\]

Adding all available higher degrees kept the rank exactly 90.

### Spectrum \(3+3\)

\[
54\to90\to90\to90\to\cdots.
\]

### Spectrum \(4+2\)

\[
48\to90\to90\to90\to\cdots.
\]

Thus, at these generic points,

\[
\boxed{
\operatorname{rank}D(E,K)
=
\operatorname{rank}D(E,K,dK,d^2K,\ldots)
=90.
}
\]

The higher tower contributes **zero additional local connection rank** after degree two.

This is the first finite-type signal.

## III.2. Singular strata remain real

The test deliberately preserved high degeneracy.

For \(so(3)\oplus so(3)\) with spectrum \(5+1\):

\[
E:30,
\qquad
(E,K):88,
\qquad
(E,K,dK):90.
\]

For the harder \(h_3\oplus\mathbb R^3\) case:

\[
30\to79\to81\to84\to84\to84,
\]

so nullity drops

\[
60\to11\to9\to6
\]

but does not vanish through the maximal exterior tower.

For scalar curl:

\[
C=\lambda I
\]

the entire commutator tower is dark:

\[
E=K=dK=\cdots=0.
\]

Therefore the finite-type statement is **generic and stratified**, never universal.

---

# IV. Tribunal B — one mother generates the full operator algebra

The next question was qualitatively different:

> Forget reconstruction for a moment.  How expressive is the pair \((C,E_u)\) itself?

## IV.1. Exact six-dimensional models

In five independent exact metric-Lie trials, curl alone generated an algebra of dimension 3, reflecting its three distinct spectral values.

After adding **one generic mother direction**:

\[
\boxed{
3\longrightarrow36=6^2.
}
\]

This occurred in 5/5 seeds.

A vertical commuting control remained small, showing that this is not a generic consequence of adding any skew/symmetric matrix to curl.

## IV.2. Physical 28D coordinate lab

The canonical 28D physical coordinate lab has six signed curl roots:

\[
-\sqrt3,-\sqrt2,-1,1,\sqrt2,\sqrt3.
\]

Curl alone generates a 6-dimensional commutative spectral algebra.

For one generic state mother:

\[
\boxed{
\dim\operatorname{Alg}(C,E_u)=784=28^2.
}
\]

Thus a single generic \(E_u\) breaks the spectral block decomposition strongly enough to generate the full matrix algebra.

This was not inferred from a single Gram--Schmidt tolerance.  The complete set of 1023 normalized words through degree 9 gave a \(784\times1023\) matrix with rank 784 in 4/4 generic states.

The final singular ratio was

\[
\frac{\sigma_{784}}{\sigma_1}
\approx
6.4\times10^{-5}	ext{--}1.1\times10^{-4},
\]

well separated from numerical zero.

---

# V. Tribunal C — essentially maximal two-letter word growth

Let the only noncommuting letters be

\[
C,\qquad E=E_u.
\]

In the 28D lab the dimension of the span of words up to successive depths was

\[
\boxed{
1,\ 3,\ 7,\ 15,\ 31,\ 63,\ 125,\ 246,\ 483,\ 784.
}
\]

The first six terms are nearly the complete binary-tree count.

There is also an information-theoretic lower bound.  With two letters, the total number of words through depth \(L\) is at most

\[
2^{L+1}-1.
\]

For \(d=28\), a full operator algebra needs 784 independent words.  Since

\[
2^9-1=511<784,
\qquad
2^{10}-1=1023>784,
\]

no two-letter system can possibly saturate \(M_{28}\) before depth 9.

The physical base7 lab saturates **exactly at depth 9**.

Thus the observed growth reaches the information-theoretic minimum word depth.

This is a much stronger statement than merely saying the final algebra is full.

---

# VI. Falsification — maximal growth is not automatic

The nested Fourier-set tribunal prevented a false universal statement.

## VI.1. No-triad control

For the three coordinate axes only:

- signed triad pairs: 0;
- \(\|E_u\|\approx2.6\times10^{-15}\);
- generated algebra:
  \[
  2/144.
  \]

No meaningful algebraic explosion occurs.

## VI.2. Increasing interaction richness

Nested mode sets gave:

| set | signed triad pairs | generated algebra |
|---|---:|---:|
| axes3 | 0 | \(2/144\) |
| plus one pair | 12 | \(38/256\) |
| plus two pairs | 24 | \(400/400\) |
| all pair modes | 36 | \(576/576\) |
| base7 | 72 | \(784/784\) |

The 24D connected set reaches full algebra two word-depth levels above the counting lower bound.

The 28D base7 set reaches the exact lower bound.

Therefore:

\[
\boxed{
\text{operator-algebra irreducibility tracks interaction-network richness.}
}
\]

This is not a formal property of curl alone.

---

# VII. Tribunal D — exact full-helical interaction percolation

Because finite Galerkin brackets can fail Jacobi, the interaction-percolation story was checked again using exact helical Fourier action of \(E_u\), without a projected Lie bracket.

In a helical observation window with 160 nodes and 12 signed curl roots:

- one Fourier support direction gave 28 connected components, largest size 10;
- two directions gave 5 components;
- three coordinate directions gave
  \[
  \boxed{1\text{ component of size }160};
  \]
- additional pair modes increased cross-root edge density.

Thus a small increase in physical support produces a sharp graph-connectivity transition in exact Fourier mother action.

This corroborates the finite algebra-percolation picture at the support level.

---

# VIII. Tribunal E — one generic mother destroys almost all curl symmetry

The full operator commutant was measured.

In the 28D base7 lab:

\[
\dim\operatorname{comm}(C)=152.
\]

After adding one generic mother:

\[
\boxed{
\dim\operatorname{comm}(C,E_u)=1.
}
\]

The surviving one-dimensional commutant is the scalar identity.

Across nested mode sets:

\[
72\to72,
\qquad
80\to12,
\qquad
104\to1,
\qquad
144\to1,
\qquad
152\to1.
\]

So once the interaction network becomes sufficiently rich, one generic mother destroys every nontrivial linear symmetry commuting with curl.

This is the dual statement to full-algebra generation.

---

# IX. Tribunal F — one generic probe becomes cyclic at the minimum depth

Choose one generic probe vector \(q\in\mathbb R^{28}\).

Apply all short words in \(C,E_u\) to \(q\).

The state-span ranks were

\[
\boxed{
1,\ 3,\ 7,\ 15,\ 28
}
\]

at depths \(0,1,2,3,4\).

Depth 4 is the minimum possible: through depth 3 there are at most 15 words, insufficient to span 28 dimensions.

The result held in 6/6 random state/probe trials.

Therefore one generic state mother and one generic probe make the probe cyclic at the information-theoretic minimum depth.

---

# X. Tribunal G — near-minimal single-port operator tomography

Using the complete depth-4 word orbit gives 31 left states and 31 right states.

Scalar bilinear measurements

\[
Y_{ab}=p_a^T X q_b
\]

therefore provide

\[
31^2=961
\]

numbers to identify an arbitrary \(28\times28\) operator with

\[
28^2=784
\]

unknown entries.

The oversampling factor is only

\[
\boxed{961/784=1.226.}
\]

Across five random trials:

- both word frames had rank 28;
- noiseless arbitrary-operator recovery was \(10^{-13}\)--\(10^{-14}\);
- noise amplification was linear, with slopes approximately 0.89--1.03.

Frame condition numbers varied from roughly 120 to 1085, so algebraic identifiability does **not** remove conditioning.

That caveat is important.

---

# XI. Tribunal H — compressed geometry compiler near the information limit

An exact eight-dimensional metric-Lie model was built with 56 within-sheet connection coefficients invisible to \(E\).

Instead of giving the full curvature mother, the inverse received random scalar curvature measurements.

Budgets tested:

\[
56,\ 62,\ 70,\ 84,\ 112
\]

measurements for 56 unknowns.

Even the square 56-by-56 systems reconstructed the hidden geometry in all three tested seeds at roughly \(10^{-14}\).

With mild 1.25x oversampling, the reconstructed compact code was asked to predict data **never used in the fit**:

- full curvature;
- the complete available higher covariant tower;
- 40 random spectral readers;
- 30 finite transport commutators;
- 30 frozen formation propagators;
- 12 nonlinear trajectories at unseen viscosities.

Errors were typically \(10^{-14}\)--\(10^{-15}\).

The noise ladder gave connection-reconstruction slope

\[
\boxed{0.9999998.}
\]

Thus a measurement budget near the number of hidden geometric degrees of freedom compiles a much larger observable zoo.

---

# XII. Tribunal I — random operator-program fuzzing

A task-specific fit can look impressive without revealing a universal structure.  To attack this possibility, 1000 unseen random operator programs were generated from:

- connection matrices;
- curvature operators;
- Poisson operators;
- spectral functions of \(C\);
- products;
- commutators;
- anticommutators;
- linear combinations;
- exponentials.

The compressed \(E+K\) compiler was evaluated on the same programs.

After regularizing near-zero semantic cancellations, results were:

\[
\text{median relative error}\approx2.8\times10^{-15},
\]

\[
\text{99th-percentile absolute error}\approx4.7\times10^{-15},
\]

\[
\text{maximum absolute error}\approx6.5\times10^{-15}.
\]

The \(E\)-only control failed broadly:

\[
\text{median error}\approx0.594,
\]

and 95.8% of programs had error above \(10^{-3}\).

An earlier version of this tribunal produced order-one *relative* outliers whenever the requested program was nearly zero and then normalized.  That was correctly classified as an observable-conditioning singularity, not a geometry-reconstruction failure.

Universality does not abolish the condition number of the requested observable.

---

# XIII. Tribunal J — one state supplies a universal operator alphabet

Once a single generic state \(u_*\) fixes the pair

\[
(C,E_{u_*}),
\]

its degree-9 word span is all of \(M_{28}\).

Therefore every tested operator in the finite formation core can be expanded in that same word language:

- all 28 mother directions \(E_{e_i}\);
- all 28 connection directions \(\nabla_{e_i}\);
- all 28 Poisson directions \(J_{e_i}\);
- all tested curvature operators \(R_{ij}\).

At degree 9, projection residuals are \(\sim10^{-16}\).

This statement must be typed carefully:

> One snapshot supplies a universal **alphabet/frame**, but does not by itself identify the expansion coefficients of all formation operators.

The polarized differential data \((E,K)\) remain the mechanism that identifies the formation grammar.

---

# XIV. Generator--relations discovery

Full-algebra generation is only half the story.  The second half is the pattern of noncommutative relations.

Let words be formed from two letters

\[
C,\qquad E=E_u.
\]

## XIV.1. Degree six: exactly two relations

There are

\[
1+2+4+8+16+32+64=127
\]

words through degree 6.

In the 28D physical lab their span has rank 125.

Thus the nullspace dimension is exactly 2.

The first relation is curl's minimal polynomial:

\[
\boxed{
p(C)=C^6-6C^4+11C^2-6I=0,
}
\]

with

\[
p(x)=(x^2-1)(x^2-2)(x^2-3).
\]

The second is the first variation/commutator derivative of the same polynomial:

\[
\boxed{
Dp_C(E)=0,
}
\]

namely

\[
\sum_{j=0}^{5}C^jEC^{5-j}
-6\sum_{j=0}^{3}C^jEC^{3-j}
+11(EC+CE)=0.
\]

Across four random states:

- both residuals were \(10^{-17}\)--\(10^{-16}\);
- numerical nullity was exactly 2;
- principal cosines between the theoretical two-relation span and the complete numerical nullspace were
  \[
  \boxed{1,1}.
  \]

Therefore, through degree 6, **no relation exists beyond the spectral polynomial and its mother derivative**.

---

# XV. Degree seven: the first physical interaction relation

At degree 7:

\[
\text{words}=255,
\qquad
\text{rank}=246,
\qquad
\text{nullity}=9.
\]

The degree-7 two-sided consequences of \(p(C)=0\) and \(Dp_C(E)=0\) span only 8 relation directions.

Therefore there is exactly

\[
\boxed{1}
\]

new relation.

After quotienting the spectral ideal with the correct SVD projector:

- the quotient relation is unique;
- it is the same across random physical states up to sign, with cosine \(1\);
- essentially 100% of its coefficient mass lies on words containing **exactly one \(E\)**.

Thus the first non-spectral relation is a universal bivariate relation

\[
q(C_L,C_R)E=0,
\]

not an \(E^2\) or higher nonlinear state relation.

---

# XVI. Pure curl roots do not explain the extra relation

A pure spectral-root calculation was run on all 30 ordered off-diagonal pairs of the six roots

\[
\{\pm1,\pm\sqrt2,\pm\sqrt3\}.
\]

Through bivariate polynomial degree 7, every vanishing polynomial on the complete off-diagonal root set is generated by:

- \(p(x)\);
- \(p(y)\);
- the divided difference
  \[
  p^{[1]}(x,y)=\frac{p(x)-p(y)}{x-y};
  \]
- their allowed polynomial multiples.

There is no extra root-only relation.

Therefore the ninth word relation cannot be explained by eigenvalues or multiplicities alone.

---

# XVII. Physical interaction incidence explains the extra relation exactly

The complete 28D mother one-form was transformed to a curl eigenbasis.

There are 30 ordered cross-sheet pairs in total.

The physical mother uses 26 of them.

The four never-used ordered transitions are

\[
\boxed{
-\sqrt3\to+\sqrt3,
\quad
-\sqrt2\to+\sqrt2,
\quad
+\sqrt2\to-\sqrt2,
\quad
+\sqrt3\to-\sqrt3.
}
\]

When the degree-6 bivariate vanishing problem is restricted to the **26 active physical edges**, its nullspace has exactly one extra direction beyond the pure spectral polynomial family.

That extra active-incidence polynomial agrees with the relation extracted from one generic \(E_u\) with cosine

\[
\boxed{1.000000000000000}
\]

in four independent states.

Thus the new word relation is precisely an interaction-incidence/selection rule.

---

# XVIII. Blind archaeology from one state

The strongest selection-rule tribunal gave the algorithm only

\[
C,\qquad E_{u_*}
\]

for one generic state.

It did **not** receive:

- the full mother one-form;
- \(T\);
- \(\nabla\);
- the Fourier support graph;
- the list of allowed or forbidden spectral transitions.

From the first non-spectral word relation, the algorithm constructed a bivariate polynomial score on the 30 ordered curl-sheet pairs.

In 8/8 random training states, the four largest scores identified exactly the four globally forbidden transitions of the full mother tensor.

The separation between the smallest forbidden score and the largest active score was

\[
\boxed{
6.3\times10^{11}	ext{--}4.5\times10^{12}.
}
\]

This is not a marginal classifier.

A generic single snapshot reveals a state-independent interaction-selection rule of the whole finite physical mother family.

---

# XIX. Same-spectrum control

To ensure the extra relation was not secretly caused by curl multiplicities, a control kept:

- the same 28-dimensional state space;
- the same six curl roots;
- the same spectral multiplicities;

but replaced the physical mother by a generic symmetric matrix with **all off-sheet blocks active**.

At degree 7:

- physical mother nullity = 9;
- generic full-offblock control nullity = 8;
- pure spectral two-sided ideal rank = 8.

This occurred in 6/6 controls.

Therefore the ninth relation is a physical interaction-support invariant, not a multiplicity artifact.

---

# XX. One-state law generalization

A relation \(q\) was extracted from one generic mother \(E_{u_*}\).

No further fitting was performed.

The same \(q\) was applied to 200 unseen physical mother states:

\[
q(C_L,C_R)E_v.
\]

Residuals were:

\[
\text{median}\approx5.16\times10^{-14},
\]

\[
\text{maximum}\approx6.02\times10^{-14}.
\]

A same-spectrum generic full-offblock control gave

\[
\boxed{0.0807}.
\]

Thus the relation learned from one state is a state-independent structural law of the finite physical mother family.

---

# XXI. Coordinate covariance of the recovered law

The entire pair \((C,E_u)\) was conjugated by ten independent random orthogonal state-coordinate changes.

The relation extracted in every chart agreed with the original relation up to sign, with cosine

\[
\boxed{1}
\]

to machine precision.

Therefore the relation belongs to the operator pair \((C,E_u)\), not to the Fourier coordinates used to display it.

---

# XXII. Closed-form finite-window selection identity

For the 28D base7 spectral window, the unique extra incidence polynomial simplifies to

\[
\boxed{
q(x,y)=(x^2-1)(y^2-1)(x^2+y^2-5).
}
\]

Hence every physical mother direction in this window satisfies

\[
\boxed{
(C^2-I)
\big(C^2E+EC^2-5E\big)
(C^2-I)=0.
}
\]

Checks:

- maximum residual over the 28 basis mother directions:
  \[
  1.17\times10^{-13};
  \]
- median basis residual:
  \[
  1.07\times10^{-15};
  \]
- random-state maximum:
  \[
  7.79\times10^{-14};
  \]
- cosine with the blindly extracted forbidden-edge signal:
  \[
  1
  \]
  in 8/8 states;
- same-spectrum full-offblock control residual:
  \[
  0.475.
  \]

This is a striking compression of a Fourier/helicity selection rule into an intrinsic polynomial operator identity.

---

# XXIII. Critical scope correction: the fixed polynomial is not continuum-universal

This point is essential.

The base7 polynomial identity was tested on **exact full-helical action**, without a projected Lie bracket.

## XXIII.1. Restricted base7 helical window

There were 264 active exact-helical transitions.

The weighted selection residual was

\[
\boxed{0.0}.
\]

Thus the identity is not created by Galerkin projection.

## XXIII.2. Expanded helical window

On the larger window

\[
|k|^2\le6
\]

with 160 helical nodes and 2640 active transitions, the same fixed polynomial failed strongly, with residual

\[
\boxed{120}.
\]

Therefore the fixed base7 polynomial must **not** be promoted to a continuum NS law.

The robust concept is instead:

\[
\boxed{
\textbf{a spectral interaction-incidence ideal attached to the chosen finite spectral window/category.}
}
\]

As the window grows, the incidence ideal changes.

---

# XXIV. One generic dense full-helical state recovers the union graph

The finite-window one-state archaeology phenomenon was tested directly in exact helical Fourier variables.

Observation window:

\[
|k|^2\le6,
\]

with 160 helical nodes.

Allowed support category:

\[
|p|^2\le3,
\]

represented by 13 positive support directions plus their conjugates.

The structural union over **every** support direction and helicity contained

\[
\boxed{4608}
\]

directed mother transitions.

A single generic dense state supported on the 13 representatives realized

\[
\boxed{4608/4608}
\]

of those transitions, with zero missing and zero extra edges, in 6/6 random amplitude trials.

Thus one generic dense state can reveal the complete structural mother graph of a finite support category.

This is the exact-helical finite-window analogue of one-snapshot interaction-law archaeology.

---

# XXV. Stable weighted spectral interaction quiver

Within the 28D curl eigenbasis, generic mother block ranks were sampled over 20 random states.

They were stable for every sheet pair.

Examples:

- active \(2\times6\) blocks had generic matrix rank 2;
- active \(6\times6\) blocks had generic matrix rank 6;
- forbidden blocks had rank 0;
- the full polarized mother map on an edge could have larger linear-map capacity, commonly 6 or 16 in the tested lab.

This motivates a useful, but still candidate, language:

- vertices = curl spectral sheets;
- arrows = active mother transitions;
- edge weights/capacities = generic block rank or polarized mother-map rank;
- paths = noncommutative words in \(C,E\);
- relations = spectral polynomial identities plus interaction-incidence constraints;
- irreducibility/full algebra = percolation of the path language.

This is structurally close to a quiver/path-algebra viewpoint, but no formal NS quiver theorem is being claimed here.

---

# XXVI. Relation growth beyond the first physical law

The word relation count grows rapidly after degree 7.

In the physical 28D lab:

| max degree | words | word rank | nullity | spectral-ideal rank | unexplained |
|---:|---:|---:|---:|---:|---:|
| 6 | 127 | 125 | 2 | 2 | 0 |
| 7 | 255 | 246 | 9 | 8 | 1 |
| 8 | 511 | 483 | 28 | 24 | 4 |
| 9 | 1023 | 784 | 239 | 64 | 175 |

Interpretation:

- degree 6: curl spectral law + first mother derivative;
- degree 7: first physical interaction-incidence relation;
- degree 8: more path/incidence constraints;
- degree 9: massive relation growth because the finite matrix algebra has saturated at dimension 784.

The relation ideal therefore appears to record both **kinematic spectral laws** and **finite interaction-channel capacity**.

---

# XXVII. What is stronger than formation-geometry completeness?

Formation-geometry completeness asks:

\[
\text{Does differential Theory 2 determine }\nabla,T,R,\mathcal J?
\]

The new campaign asks something stronger:

> Does Theory 2 provide a compact algebraic language in which the entire finite observable theory is generated, and do the relations of that language reveal the structural laws of the theory itself?

The evidence says **yes in the tested finite generic categories**, with exact-helical support-level corroboration.

The strongest surviving architecture is:

\[
\boxed{
\begin{aligned}
\text{one generic snapshot: }&(C,E_{u_*})
\longrightarrow
\text{operator alphabet + relation ideal},\\[1mm]
\text{spectral relations: }&p(C)=0,\quad Dp_C(E)=0,\\[1mm]
\text{physical relations: }&\text{interaction-incidence / selection rules},\\[1mm]
\text{polarized data: }&(E,K)
\longrightarrow
\text{formation grammar }(\nabla,T,R,\mathcal J),\\[1mm]
\text{generic jet structure: }&E+K\text{ exhaust local connection rank},\\[1mm]
\text{singular strata: }&dK,d^2K,\ldots\text{ add observability},\\[1mm]
\text{dynamics: }&\text{geometry}+\nu\longrightarrow\text{NS formation law}.
\end{aligned}
}
\]

A concise name for this candidate is

\[
\boxed{
\textbf{Curl--Mother Spectral Bootstrap.}
}
\]

An even more descriptive phrase is

\[
\boxed{
\textbf{Self-Describing Curl--Mother Algebra.}
}
\]

---

# XXVIII. What “self-describing” means and does not mean

## It means

In the tested finite interacting categories:

1. one generic \(E_u\) together with \(C\) can generate all finite matrix observables;
2. the first relations among those generators are not arbitrary numerical accidents;
3. spectral relations reproduce curl's polynomial law;
4. extra relations reproduce physical interaction support/selection rules;
5. a relation extracted from one state can generalize to unseen states;
6. polarized \((E,K)\) data identify the formation connection coefficients;
7. higher observables can then be compiled without separate fitting.

## It does not mean

1. one snapshot alone reconstructs all connection coefficients;
2. the 28D word algebra is a faithful finite Lie algebra;
3. the base7 selection polynomial is continuum-universal;
4. every flow/support sector is algebraically irreducible;
5. every generic finite result is already a continuum theorem;
6. full algebra generation solves regularity;
7. algebraic identifiability guarantees good conditioning for every observable.

---

# XXIX. Main falsifications retained by the campaign

A useful theory must remember what failed.

## XXIX.1. “Higher tower always adds new local geometry” — false

At generic spectral points, \(E+K\) already saturates full local connection rank.

## XXIX.2. “One mother always generates the full algebra” — false

No-triad sectors remain highly reducible.

## XXIX.3. “Full algebra is a numerical Gram--Schmidt artifact” — falsified

The 784th singular direction stays quantitatively separated from zero across independent generic states.

## XXIX.4. “The extra relation comes from curl roots alone” — false

The complete off-diagonal root incidence has no extra degree-7 relation beyond the spectral polynomial family.

## XXIX.5. “The extra relation comes from multiplicities” — false

Same-spectrum all-offblock controls lose exactly the physical ninth relation.

## XXIX.6. “The base7 polynomial is a global continuum law” — false

It is exact on the base7 full-helical window and fails strongly on a larger helical window.

## XXIX.7. “A relation learned from one state is state-specific” — false in the finite physical lab

It annihilates 200 unseen states at machine precision.

## XXIX.8. “Universal compiler means no conditioning problems” — false

Near-zero semantics and poorly conditioned cyclic frames can amplify noise even when identifiability is exact.

---

# XXX. Standard mathematics versus NS-specific content

The following surrounding mathematical ideas are standard:

- irreducible matrix algebras and full matrix-algebra generation;
- cyclic vectors;
- noncommutative word algebras;
- polynomial identities/minimal polynomials;
- quivers/path algebras and relations;
- finite-dimensional observability and rank conditions.

No novelty claim should be attached to those concepts themselves.

The potentially distinctive NS-specific content is their conjunction with the canonical formation/signature objects:

1. signed curl \(C\) is selected by the NS formation core;
2. the canonical mother is \(E_u=[\nabla_u,C]\) and is state-complete;
3. one generic physical mother can make the curl operator algebra irreducible in rich finite windows;
4. its first relations recover both curl's spectral polynomial and physical interaction-selection incidence;
5. those interaction relations can be recovered blindly from one generic snapshot and generalize to unseen physical states;
6. polarized curvature \(K=[R,C]\) recovers the hidden within-sheet connection grammar generically;
7. exact full-helical experiments corroborate the support/interaction interpretation without relying on a projected Lie bracket.

That package is the actual object requiring future literature comparison and theoremization.

---

# XXXI. Candidate theorem targets opened by this campaign

## XXXI.1. Generic finite-window algebra generation theorem

Given a finite curl spectral window and a sufficiently interacting generic state, characterize when

\[
\operatorname{Alg}(C,E_u)=\operatorname{End}(V).
\]

The natural criterion should be formulated in terms of spectral-edge connectivity and edge block irreducibility, not random-matrix genericity alone.

## XXXI.2. One-state incidence theorem

For a finite Fourier support category, prove that a generic dense state realizes the union of all mother transition edges allowed by the support category.

The exact-helical 4608/4608 experiment is a strong finite-window target.

## XXXI.3. Spectral relation-ideal theorem

Describe the kernel of the noncommutative evaluation map

\[
\mathbb R\langle C,E\rangle
\to
\operatorname{End}(V)
\]

as a hierarchy containing:

- spectral polynomial relations;
- their covariant/mother derivatives;
- interaction-incidence relations;
- finite path-capacity relations.

## XXXI.4. Blind law-recovery theorem

Under a genericity condition on \(u\), characterize when the relation ideal of \((C,E_u)\) determines the state-independent support/selection ideal of the full mother family.

## XXXI.5. Continuum/microlocal bootstrap

Replace finite matrix words by typed pseudodifferential/Fourier multiplier compositions and identify the correct local/microlocal analogue of:

\[
\text{generator algebra},
\qquad
\text{interaction incidence},
\qquad
\text{relation ideal}.
\]

This is the real continuum target.  The finite base7 polynomial should not be mistaken for it.

## XXXI.6. Generator-plus-grammar theorem

Combine:

- snapshot alphabet \((C,E_{u_*})\);
- polarized geometry \((E,K)\);
- transported metric \(g_\Sigma\);

and prove a local equivalence between a curl--mother generator--relations presentation and the formation core modulo the true stabilizer.

This would be stronger than ordinary formation-geometry completeness because it would identify not only the geometry but a compact intrinsic presentation of its observable algebra.

---

# XXXII. Most conservative strongest wording

The strongest wording supported by the current campaign, without pretending the continuum theorem exists, is:

> **In the tested finite interacting Navier--Stokes representations, a single generic curl mother together with curl is algebraically universal: it generates the full observable matrix algebra, and its first noncommutative relations encode both the curl spectral polynomial and state-independent physical interaction-incidence rules.  Polarized curvature data then identifies the hidden formation grammar.  Exact full-helical experiments corroborate the interaction-graph interpretation and show that the relevant law is a scale/window-dependent incidence ideal rather than a fixed finite polynomial.**

Or, compressed:

\[
\boxed{
\textbf{Theory 2 is beginning to look self-describing, not merely complete.}
}
\]

---

# XXXIII. Reproduction map

The research suite contains 26 scripts.

### Finite-jet and compiler layer

- `finite_jet_rank_collapse.py`
- `compressed_universal_compiler.py`
- `random_operator_program_fuzz.py`

### Operator-algebra universality

- `sensor_operator_algebra_saturation.py`
- `two_letter_word_growth.py`
- `two_letter_svd_robustness.py`
- `maximal_word_growth_scaling.py`
- `single_mother_centralizer_collapse.py`
- `single_probe_cyclic_tomography.py`
- `redundant_single_port_tomography.py`
- `single_state_spectral_bootstrap.py`

### Interaction percolation / exact-helical controls

- `interaction_percolation_algebra.py`
- `full_helical_interaction_graph_percolation.py`
- `full_helical_one_state_recovers_union_graph.py`
- `generic_mother_edge_capacities.py`

### Generator--relations / law archaeology

- `first_word_relations_are_spectral.py`
- `spectral_relation_ideal_growth.py`
- `extract_degree7_new_relation.py`
- `bivariate_spectral_incidence_relations.py`
- `physical_incidence_explains_new_relation.py`
- `blind_selection_rule_recovery.py`
- `same_spectrum_support_control.py`
- `one_snapshot_law_generalization.py`
- `relation_coordinate_covariance.py`
- `closed_form_selection_law.py`
- `full_helical_window_selection_scope.py`

All 26 scripts compile.

A full clean rerun gave:

\[
\boxed{26/26\text{ research audits pass}.}
\]

The suite deliberately counts negative controls as passes only when the expected failure/scope correction is observed.

---

# XXXIV. Final research compression

The campaign began by asking for something stronger than

\[
\text{Curl-Spectral Formation-Geometry Completeness}.
\]

The answer suggested by the experiments is not merely “even more completeness”.

It is a change of ontology.

The formation/signature system may admit a two-layer presentation:

### Layer A — one-state algebraic language

\[
\boxed{
(C,E_{u_*})
}
\]

can, at generic interacting finite points:

- generate all finite operator observables;
- destroy all nontrivial curl-commuting symmetry;
- make one generic probe cyclic;
- expose spectral and interaction relations;
- reveal the structural transition graph of the finite support category.

### Layer B — polarized geometric grammar

\[
\boxed{
(g,E,K)
}

selects the actual formation connection and its coefficients inside that language.

Then

\[
\boxed{
\text{alphabet + relations + grammar + }\nu
\longrightarrow
\text{full formation dynamics and its observable calculus}.
}
\]

That is the current deepest candidate interpretation of Theory 2.

Not just a signature.

Not just a complete coordinate chart.

Not just a reconstruction of geometry.

But a candidate **self-describing spectral bootstrap language for the formation theory itself**.

---

# Campaign IV — Presentation, law holography, and the syntax/parameter split

The next campaign deliberately tested a stronger candidate than formation-geometry completeness:

\[
\boxed{
\text{Can one generic mother snapshot expose a generator--relations presentation of its physical interaction category?}
}
\]

The answer in the tested finite/exact-helical settings is substantially stronger than expected, but with an essential boundary: **one snapshot identifies syntax/presentation, not the full polarized geometry coefficients.**

## A. Three defining relations close the entire pre-saturation word ideal

In the canonical 28D physical coordinate lab, let \(E=E_u\) for a generic state and

\[
p(x)=(x^2-1)(x^2-2)(x^2-3).
\]

The three state-independent relations are

\[
\boxed{p(C)=0,}
\]

\[
\boxed{Dp_C(E)=0,}
\]

and the physical selection relation

\[
\boxed{
Q(C,E)
=(C^2-I)(C^2E+EC^2-5E)(C^2-I)=0.
}
\]

The two-sided ideal generated by these three laws has exactly the same dimension as the full numerical word-relation space through degree eight:

\[
\begin{array}{c|c|c}
\text{degree}&\text{numerical nullity}&\text{three-law ideal rank}\\\hline
6&2&2\\
7&9&9\\
8&28&28.
\end{array}
\]

At degree nine the word algebra reaches the finite representation ceiling \(M_{28}\), and 163 additional finite-representation relations appear.  Thus, before saturation, the tested algebra admits the finite presentation

\[
\boxed{
\langle C,E\mid p(C),Dp_C(E),Q(C,E)\rangle.
}
\]

This is audit evidence for a finite-window presentation, not a continuum theorem.

## B. The full degree-eight relation space transfers from one state

A 28-dimensional degree-eight nullspace learned numerically from one generic physical mother was frozen and tested against 80 unseen physical states.  The minimum principal cosine was

\[
0.9999999999999991.
\]

After quotienting the 24-dimensional common spectral relation space, four physical-specific relation directions remained.  Their residual on unseen physical states was at most

\[
5.54\times10^{-16},
\]

while a same-spectrum generic off-block law produced

\[
3.31\times10^{-7},
\]

a separation of about

\[
5.98\times10^8.
\]

Thus the transferred object is a state-independent presentation subspace, not merely one fitted polynomial.

## C. Same-spectrum rival-theory identification

The interaction law was challenged against rivals with identical curl roots, multiplicities and forbidden-edge count.  The classifier was allowed to see only the quotient noncommutative relation extracted from one snapshot.

In the physical same-count regime, all three codimension-one rival laws were identified exactly.  A broader synthetic stress family of eight same-spectrum/same-count laws also produced an identity confusion matrix.  The physical three-law classifier remained exact through relative snapshot perturbation \(10^{-3}\).

This shows that the relation ideal carries more than spectral multiplicity or the number of missing channels: it carries the **shape of interaction incidence**.

## D. Exact-helical confirmation

The three defining relations were then tested on the exact complex helical mother operator restricted to the base7 spectral window, without using the projected Galerkin Lie bracket.  Across eight generic real dense states, normalized residuals were at approximately

\[
10^{-19}\text{--}10^{-21}.
\]

Hence the three-law presentation is already present in the exact Fourier/helical action on that finite window.

## E. Sparse-state law holography

For the exact window \(|k|^2\le6\):

- 160 helical nodes;
- 12 signed curl roots;
- 13 support representatives in the state category;
- 120 active signed-root transitions;
- 12 forbidden transitions.

An exact set-cover search showed that only three support directions are required to illuminate the complete root-level law:

\[
(0,0,1),\qquad(0,1,-1),\qquad(1,-1,-1).
\]

The first physical incidence relation appears only at polynomial degree 16.  Nevertheless, a generic state supported on those three modes recovers from its exact mother matrix:

- the same 37-dimensional degree-16 relation space as the full 13-support category;
- the unique physical quotient relation with cosine \(1\) to machine precision;
- all 12 forbidden root transitions.

The smallest forbidden/allowed score separation across six states was

\[
1.53\times10^9.
\]

This is the strongest current evidence for **law holography**: a sparse generic state can expose the interaction law of a much larger support category.

## F. Multi-window scaling and projective consistency

The same three support directions were tested across exact helical windows from 52 to 512 nodes.  They recover the full root-level interaction category in every tested window:

\[
\begin{array}{c|c|c|c|c}
R^2&\text{nodes}&\text{signed roots}&\text{active channels}&\text{forbidden channels}\\\hline
3&52&6&28&2\\
4&64&8&44&12\\
5&112&10&78&12\\
6&160&12&120&12\\
8&184&14&144&38\\
9&244&16&186&54\\
10&292&18&228&78\\
12&356&22&300&162\\
14&500&26&416&234\\
16&512&28&432&324.
\end{array}
\]

For the first six windows, the full first physical quotient-relation space was reconstructed directly from the three-support mother matrix; relation degrees increase

\[
8,8,12,16,16,19,
\]

while support complexity remains bounded by three.

Even more importantly, window refinement is projectively consistent: restricting a larger-window interaction law back to previously present curl roots changes **zero** old-root transitions at every tested refinement step from \(R^2=3\) through \(16\).

This suggests a possible inverse-system architecture for finite-window presentations.  It does not yet prove a continuum inverse limit.

## G. Noise basin

In the exact 160-node degree-16 law-archeology problem, orbit-tangent perturbations were added to the mother matrix.

- \(1\%\) relative perturbation: relation cosine \(0.99994\), 12/12 forbidden transitions still exact;
- \(3\%\): cosine \(0.99684\), still exact classification;
- \(10\%\): forbidden-channel classification begins to fail.

Thus the interaction-law fingerprint has a finite stability basin and is not merely an exact-zero phenomenon.

## H. Why the operator algebra becomes universal

A block-graph phase diagram used the physical curl multiplicities

\[
(2,6,6,6,6,2).
\]

Connectivity alone is insufficient.  Across all 1296 labeled trees, the common centralizer never collapsed to scalars; median nullity was 44.  With generic full block couplings, scalar centralizers become common as edge count increases and were universal in the sampled ensemble from 12 edges upward.  A complete graph with rank-one block channels retained centralizer dimension 45.

Thus the observed algebraic percolation requires both

\[
\boxed{\text{spectral-sheet connectivity}+\text{channel richness}.}
\]

This supplies a concrete theorem target for a Burnside-type irreducibility criterion.

## I. Critical falsification: one snapshot is not the full theory coefficients

A continuous family of metric-compatible connection one-forms was constructed so that, at one training state \(u_*\),

\[
(C,E_{u_*},\nabla_{u_*})
\]

was identical to machine precision for all family parameters.  The competing mother maps remained injective and obeyed the same degree-eight presentation, yet their image subspaces had minimum principal cosine \(0.539\).  On unseen directions the mother difference had median \(17.2\%\), while connection difference had median \(22.4\%\).

Therefore

\[
\boxed{
\text{one snapshot does not determine the polarized mother/connection one-form.}
}
\]

The correct hierarchy is

\[
\boxed{
\text{snapshot}\Rightarrow\text{syntax/presentation category},
}
\]

\[
\boxed{
\text{polarized }E,K\Rightarrow\text{geometry coefficients}.
}
\]

## J. One curvature scalar breaks a continuous snapshot collision

The previous ambiguity was sharpened into a one-parameter family \(\nabla^{(\delta)}\) with the same training \((C,E_{u_*},\nabla_{u_*})\).  The perturbation was chosen so that one generic curvature scalar

\[
\langle z,K^{(\delta)}(u_*,v)w\rangle
\]

is affine in \(\delta\).

Across 80 random trials a **single scalar curvature reading** recovered \(\delta\) with median error

\[
9.1\times10^{-15}
\]

and worst error

\[
4.1\times10^{-13}.
\]

Noise propagated linearly with fitted slope \(0.995\).

This gives the cleanest current operational split:

\[
\boxed{
\text{mother snapshot = language / law fingerprint},
}
\]

\[
\boxed{
\text{curvature polarization = hidden geometry calibration}.
}
\]

## K. Current candidate after Campaign IV

The strongest candidate supported by the combined tribunals is no longer simply “formation-geometry completeness.”  It is a two-level bootstrap architecture:

\[
\boxed{
\begin{aligned}
(C,E_{u_*})
&\rightsquigarrow
\text{generator algebra + state-independent relation ideal},\\
E(\cdot),K(\cdot,\cdot)
&\rightsquigarrow
\text{formation-geometry coefficients inside that language},\\
\nu
&\rightsquigarrow
\text{dissipative calibration}.
\end{aligned}
}
\]

A useful provisional name is

\[
\boxed{\textbf{Curl--Mother Presentation Bootstrap}.}
\]

The strongest continuum theorem target is not that a single state determines every coefficient of the physical theory.  That is false abstractly and has now been falsified constructively.  The sharper target is:

> In a generic interacting spectral category, a mother snapshot determines the local generator--relations presentation / interaction incidence, while polarized differential signature data determine the compatible formation geometry within that presentation.

The exact function-space hypotheses, inverse-limit formulation across spectral windows, and relation to physical Fourier selection rules remain open.
