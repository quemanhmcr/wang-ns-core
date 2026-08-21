# History and Falsification

This note records only the discovery steps that materially determined the final core.  It is not a dump of the research worktree.

## 1. Two apparently separate cores

The repository first reached two mature structural descriptions:

- the metric–Lie/Hodge **formation core**, centered on the bilinear Riesz form
  \[
  \ell_{\nu,u}(a,b)
  =-\langle u,[a,b]\rangle-\nu\langle Ca,Cb\rangle;
  \]
- the **spectral-signature core**, centered on the complete mother
  \[
  E_u=[\nabla_u,C]
  \]
  and its shifted spectral-flag normal form.

The natural question was whether these were merely compatible theories or two levels of one geometry.

## 2. First unification experiment: forward and reverse maps

A blind finite-dimensional physical algebra was built in which the core path retained only the metric-Lie tensor \(T\) and curl matrix \(C\).  The physical Fourier implementation was kept separate.

From \(T\), the core path reconstructed the connection by Koszul, then the mother \(E\), then the full shifted flag.  On the selected 28-dimensional mean-zero model, both mother and flag maps had full rank, with condition numbers near \(2.4\).

The reverse path reconstructed state and the full formation operator.  Independent trajectory integrations in physical and signature coordinates commuted at roundoff.

This established that, on a fixed core, the spectral theory was carrying more than static state information: it carried the full formation dynamics.

## 3. First major falsification: the signature image is not Euclidean

An early attempt treated reduced mother coordinates as if their coordinate metric were the identity.  The formation form then failed by order one.  This was not a numerical bug; it exposed the missing transported Riesz metric.

With the induced metric, the same identities returned to roundoff.  The later exact Sobolev argument clarified the result:

\[
L^2_u\longleftrightarrow \dot H^{-1}_q,
\qquad
\|Cu\|_2^2\longleftrightarrow L^2_q.
\]

The failure therefore forced a genuine structural upgrade: complete coordinates do not automatically preserve the formation metric unless the metric is transported.

## 4. Second major falsification: naive operator commutator is not the formation bracket

The tempting guess

\[
E_{[u,v]}=[E_u,E_v]
\]

failed at order one.  The exact Jacobi calculation revealed the missing term:

\[
E_{[u,v]}
=[\nabla_u,E_v]-[\nabla_v,E_u]-[R(u,v),C].
\]

This turned curvature from a secondary renderer into a necessary part of the induced Lie geometry.

An infinitesimal loop experiment then measured \([R,C]\) directly as curl holonomy, confirming that the correction was geometric rather than bookkeeping.

## 5. Third major falsification: snapshot signature does not determine an arbitrary core

An exact dark-sector collision was constructed inside a degenerate curl eigenspace.  Two abstract metric-Lie cores had identical mother maps, identical full shifted flags, and identical diagonal dissipative dynamics for every state, while their full Poisson operators differed by order one.

This killed the overclaim

\[
\text{signature snapshot}\Rightarrow\text{universal background core}.
\]

The surviving statement became fiberwise: the signature is complete over the canonical physical NS core.  A separate local-isotropic derivation tribunal then showed why the physical core is rigid: the vector-field bracket and curl direction are selected by locality/derivation and oriented Euclidean equivariance in the tested class.

## 6. Fourth major falsification: arbitrary Galerkin projection can lie

Changing the retained Fourier library produced projected mother ranks such as \(18/24\) and \(28/40\), even though the six-direction physical microlocal signature remained full rank.  Some projected brackets had Jacobi defects around \(0.4\)–\(0.6\).

A first Bianchi/curved-DG experiment inside such a Galerkin algebra failed badly.  Measuring the projected Jacobi identity exposed the reason: the truncated algebra was not a faithful Lie category.

The experiment was repeated on full pseudospectral divergence-free fields with low-frequency support.  Jacobi, Bianchi and the first curved-covariant tower identities then held at \(10^{-15}\)–\(10^{-13}\) scale.

This established a methodological rule for the core:

\[
\boxed{
\text{finite Galerkin models are useful coordinate labs, but higher Lie/curvature claims require a faithful physical check.}
}
\]

## 7. Curvature tomography closes the two theories

The shifted spectral family had already tomographed the mother deformation.  The decisive next test asked whether the same spectral cuts tomograph curvature action.

They do:

\[
\frac12\int[R,H_a]\,da=[R,C].
\]

The result was verified both in finite spectral geometry and independently on full physical helical Fourier multipliers.  This moved the relation between the two theories beyond state reconstruction:

\[
\boxed{
\text{formation curvature holonomy}
\longleftrightarrow
\text{shifted spectral curvature tomography}.
}
\]

## 8. Final compression

The resulting canonical picture is

\[
\boxed{
(\mathfrak g_\sigma,g,T,C)
\to
\nabla
\to
E=d_\nabla C
\leftrightarrow
\text{shifted spectral flag},
}
\]

with the next degrees governed by

\[
\boxed{
 d_\nabla^2=R\text{-action},
\qquad
C\to E\to[R,C]\to R\wedge E\to\cdots.
}
\]

The historical lesson is the same one learned repeatedly elsewhere in the repository: when a new “mechanism” appears after changing representation or differentiating, first ask whether it is a generated degree of an existing structure.  In this case the answer led from two apparently separate cores to one curved formation–signature geometry.

---

## 9. Fifth major correction: “curved representation” is not a curved embedding

The phrase “curved signature geometry” was initially too loose.  An exact \(so(3)\) test used a linear signature image with constant transported metric.  Its ordinary coordinate curvature was zero, while the transported formation curvature was nonzero and matched the physical curvature at roundoff.

This forced the wording:

\[
\boxed{
\text{signature image = linear state representation carrying a curved formation connection.}
}
\]

The curvature belongs to the represented formation geometry, not to a nonlinear embedding of the signature image.

## 10. The spectral-sheet picture emerges

Writing the connection in a curl spectral frame revealed the split

\[
\nabla=V+B,
\qquad [V,C]=0,
\]

so that

\[
E=[B,C].
\]

This exposed the mother as the gap-weighted cross-sheet mixing of the formation connection.  Curvature then decomposed into within-sheet and cross-sheet pieces, with

\[
K=[R,C]
\]

seeing only the latter.  Finite spectral and full physical helical audits agreed.

Gauss, Ricci and Codazzi therefore stopped looking like historical costumes: they are the natural block geometry of the curl spectral reduction.

## 11. Sixth falsification: the first curl commutant is not the final gauge

At first order, a connection component commuting with curl is invisible to \(E\).  It was tempting to call the entire commutant a gauge sector.

That interpretation failed.  Generic vertical connection components alter curvature through interaction with the cross-sheet component, and the pair \((E,K)\) reconstructed the hidden lift in every tested compatible-connection degeneracy pattern.

The corrected statement is:

\[
\boxed{
\operatorname{comm}(C)=\text{first-order stabilizer}.
}
\]

Only transformations stabilizing the complete generated sensor algebra deserve to be called truly dark.

## 12. Seventh falsification: higher tower does not always add new connection information

When curvature was treated as an independent unknown, the higher Bianchi degrees formed a real observability filtration.  A \(3+3\) spectrum left one vertical curvature direction after degree three and lost it only after degree four.

But when curvature was constrained to arise from the same compatible connection that generated \(E\), the degree-two data \((E,K)\) were already generically full rank for the hidden vertical connection.  Higher degrees then added consistency rather than new independent connection information.

This separated two inverse problems that had previously been conflated.

## 13. Eighth falsification: curvature is not a danger amplitude

The mother and curvature mother remained nonzero on harmless classes:

- 2D incompressible flows with zero self-stretching;
- exact Beltrami states with vanishing Euler self-dynamics;
- shear flows with vanishing Euler self-dynamics.

Therefore the third core must remain a structural theory of ambient state-space geometry.  Nonzero \(E\) or \([R,C]\) cannot by itself be advertised as evidence of singular behavior.

## 14. Ninth falsification: zero curl is not gauge

An annular harmonic circulation has \(Ch=0\) but can have \([D_h,C]\neq0\) on probes.  A separate algebraic model placed both a visible harmonic-like direction and a truly central direction in \(\ker C\).

This killed the shortcut

\[
\ker C=\text{gauge}.
\]

The true kernel is interaction- and domain-dependent, and topology must be carried explicitly.

## 15. Tenth falsification: BCH is not geometric curvature

Euler–heat BCH descendants and the geometric curvature mother are both generated from the same formation core, but they are not the same object.  Beltrami and shear controls had zero tested Euler–heat diagonal mixed term while ambient \([R,C]\) remained nonzero.

The correct relation is ancestry, not identity:

\[
(T,C)
\longrightarrow
\begin{cases}
\text{Euler–heat BCH descendants},\\
\text{formation connection curvature descendants}.
\end{cases}
\]

## 16. What the second campaign changed

The first campaign established that the spectral-signature theory carries the formation dynamics and curvature.  The second campaign changed the interpretation from a generic “curved representation” into a much more specific statement:

\[
\boxed{
\textbf{curl supplies a spectral reduction of the formation connection.}
}
\]

The mother measures spectral-sheet mixing.  The curvature mother measures cross-sheet curvature.  Gauss/Ricci curvature lives within sheets.  Bianchi identities couple the visible and hidden sectors.  The first commutant is only a stabilizer, not automatically a physical gauge.  Boundary, topology, orientation and metric typing remain indispensable.

The most useful methodological lesson is that each attractive slogan was accepted only after adversarial controls tried to break it.  Several slogans did break, and the resulting theory became both narrower and clearer.
