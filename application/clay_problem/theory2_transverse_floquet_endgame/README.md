# Theory-2 stationary finite-viscosity endgame

This folder is the current **formal proof package** for the normalized stationary finite-\(\kappa\) Theory-2 branch.

It is intentionally short. Historical proof attempts, superseded frontiers and narrative development are kept only in Git history.

> **Status:** no claim of 3D Navier–Stokes global regularity is made. The stationary endgame is reduced to two explicit OPEN physical statements: channel-resolved projective closure and finite physical witness extraction/nonflatness.

---

## File map

1. `00_DEFINITIONS_AND_HYPOTHESES.md`  
   Ambient class, Theory-2 definitions, normalized stationary hypotheses, compactness assumptions and explicit non-hypotheses.

2. `01_EXACT_THEOREMS_AND_PROOFS.md`  
   Poisson Formation identities, critical work, constrained-gradient split, Curl–Killing companions, rank-one completion, and the finite completed-network rigidity theorem.

3. `02_STATIONARY_FINITE_VISCOSITY.md`  
   Exact stationary reduction
   \[
   T=\kappa R_{\rm fv},
   \]
   residual Pythagorean identity, helicity-ray form of \(R_{\rm fv}\), canonical finite-energy radial inverse, trivial kernel and high-frequency resolvent estimate.

4. `03_NO_GO_THEOREMS.md`  
   Rigorous impossibility statements: edgewise absorption is a direct product; rank-one holonomy is flat; finite readers are not injective; compactness does not create finite exact recurrence; additive mixing destroys ordinary edgewise transport.

5. `04_OPEN_FRONTIER.md`  
   The only unresolved physical bridge:
   \[
   \boxed{\text{CRPC / exact channel inheritance + pointwise finite nonflat witness (or FWE)}.}
   \]

6. `05_CONDITIONAL_CLOSURE.md`  
   Full downstream proof under the OPEN bridge: genuine finite holonomy, contradiction with exact saturation consistency, compactness upgrade, and quantitative transverse saturation gap.

---

## Dependency chain

The proved part is

\[
\boxed{
\begin{gathered}
\text{Theory-2 Poisson/Curl–Killing structure}\\
\Downarrow\\
N=\gamma G+T\\
\Downarrow\\
\text{stationary scalar constraint }W=2\kappa D_3\\
\Downarrow\\
\boxed{T=\kappa R_{\rm fv}}\\
\Downarrow\\
\text{radial finite-viscosity operator }\mathscr R_\sigma
\text{ has a unique finite-energy absorber}\\
\Downarrow\\
\text{rank one + radial absorption alone do not generate a nontrivial loop obstruction.}
\end{gathered}
}
\]

The OPEN physical bridge is

\[
\boxed{
\begin{gathered}
\text{preserve an identifiable companion channel before additive mixing}\\
\Downarrow\\
\text{projective edge transport }h_e\\
\Downarrow\\
\text{extract a finite exact nonflat physical witness from every saturated PDE candidate.}
\end{gathered}
}
\]

If that bridge is proved, the remainder is already rigorous:

\[
\boxed{
\begin{gathered}
\text{exact channel consistency}\Rightarrow \operatorname{Hol}=1,\\
\text{finite witness nonflatness}\Rightarrow \operatorname{Hol}\neq1,\\
\Downarrow\\
T\neq\kappa R_{\rm fv},\\
\Downarrow\\
\|T-\kappa R_{\rm fv}\|_{H^{-1/2}}
\ge
\eta_K\bigl(\|T\|_{H^{-1/2}}+\kappa\|R_{\rm fv}\|_{H^{-1/2}}\bigr).
\end{gathered}
}
\]

---

## Current OPEN theorem

The preferred formulation is:

### Channel-Resolved Projective Closure / Finite Witness Theorem

For every normalized nonexceptional state satisfying the forbidden stationary saturation

\[
T(v)=\kappa(v)R_{\rm fv}(v),
\]

prove that actual Curl–Killing/Navier–Stokes ancestry contains a finite reality-complete channel-resolved witness in which:

1. every selected absorbed companion contribution remains projectively identifiable before summation with other incoming channels;
2. the inherited channel amplitudes obey exact multiplicative edge transport;
3. at least one finite incidence cycle is nonflat.

Equivalently, prove Finite Witness Extraction (FWE): every saturated PDE candidate contains a finite exact nonexceptional completed saturation witness, contradicting the established finite-network rigidity theorem.

---

## Nonclaims

This dossier does not prove:

- the CRPC/FWE theorem;
- absence of all stationary finite-\(\kappa\) states outside the stated class;
- periodic/Floquet rigidity;
- Euler recurrence rigidity;
- 3D Navier–Stokes global regularity.

The formal threshold remains

\[
\boxed{\mathbf{NO}.}
\]

The value of the present package is that the remaining gap is now stated as an exact finite physical ancestry theorem rather than as another scalar estimate or moment hierarchy.