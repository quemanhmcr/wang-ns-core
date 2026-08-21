# Applications

## Application 1 — Blow-up via Theory 1

**Theory 1** in this repository means the canonical **Metric–Lie / Hodge Formation Core** in [`core/metric_lie_hodge/`](../core/metric_lie_hodge/).  Application 1 applies that full-state theory to the three-dimensional Navier–Stokes finite-time blow-up/global-regularity problem.

This directory contains application-level programmes built on the canonical structural cores in [`core/`](../core/).  Application notes may combine exact core identities with additional reductions tailored to a concrete mathematical problem, but they must keep a strict distinction between:

1. identities already implied by the canonical core;
2. application-specific exact reductions;
3. conjectural or open rigidity statements.

Current application programmes:

- **Application 1 / Theory 1:** [`blowup_core_rigidity/`](blowup_core_rigidity/) — observer-free reduction of the 3D Navier–Stokes finite-time blow-up question using the Metric–Lie/Hodge Formation Core, ending at a normalized full-core rigidity theorem target.

Nothing in this directory should be read as changing the claim level of the canonical theory folders.  In particular, an application folder is not a proof of global regularity unless its final rigidity theorem is actually established.
