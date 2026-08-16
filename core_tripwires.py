"""Executable semantic tripwires for the distilled Wang–NS core.

These functions are NOT PDE proofs.  They encode a few invariants whose accidental
reversal would signal that the research language has drifted away from the current
physical ontology.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isclose
from typing import Iterable, Mapping, Sequence


def positive(x: float) -> float:
    return x if x > 0.0 else 0.0


def triad_donor_kernel(transfers: Sequence[float], *, tol: float = 1e-12) -> tuple[tuple[float, ...], ...]:
    """Canonical dW- -> dW+ donor kernel for one closed signed triad."""
    if len(transfers) != 3:
        raise ValueError("a closed helical triad has exactly three signed transfers")
    if not isclose(sum(transfers), 0.0, abs_tol=tol, rel_tol=0.0):
        raise ValueError("signed triad transfer must cancel before Hahn")
    p = [positive(t) for t in transfers]
    n = [positive(-t) for t in transfers]
    q = sum(p)
    if not isclose(q, sum(n), abs_tol=tol, rel_tol=tol):
        raise ValueError("positive and negative triad masses must agree")
    if q == 0.0:
        return tuple(tuple(0.0 for _ in transfers) for _ in transfers)
    return tuple(tuple(n_i * p_j / q for p_j in p) for n_i in n)


def restrict_canonical_positive_mass(mu: float, q: float) -> tuple[float, float]:
    """Restrict an already-canonical positive charge; never Hahn-split again."""
    if mu < 0.0 or not 0.0 <= q <= 1.0:
        raise ValueError("positive mass and a [0,1] restriction are required")
    return q * mu, (1.0 - q) * mu


def mode_set_endpoint_energy(E0: float, inflow: float, outflow: float, dissipation: float) -> float:
    """Exact set balance: E1 + D + out = E0 + in."""
    if min(E0, inflow, outflow, dissipation) < 0.0:
        raise ValueError("stock, boundary flows and dissipation are nonnegative")
    E1 = E0 + inflow - outflow - dissipation
    if E1 < -1e-12:
        raise ValueError("inputs imply negative endpoint stock")
    return max(E1, 0.0)


def inherited_stock_component(
    *,
    E0: float,
    E1: float,
    residual_positive_work: float,
    same_carrier: bool,
    no_first_stop: bool,
    earlier_endpoint_non_event: bool,
) -> bool:
    """Current stock gate.  True means the inherited component has zero generation depth."""
    if E0 < 0.0 or E1 < 0.0 or residual_positive_work < 0.0:
        raise ValueError("energies/work must be nonnegative")
    face = E1 / 5.0
    return (
        same_carrier
        and no_first_stop
        and earlier_endpoint_non_event
        and E0 >= face
        and residual_positive_work < face
    )


def selected_family_boundary(energies: Mapping[str, float], old: Iterable[str], new: Iterable[str]) -> float:
    """Moyal symmetric-difference boundary charge; provenance, not generation."""
    old_set, new_set = set(old), set(new)
    if any(e < 0.0 for e in energies.values()):
        raise ValueError("cell energies must be nonnegative")
    return sum(energies[c] for c in old_set ^ new_set)


def antisymmetric_subset_flux(matrix: Sequence[Sequence[float]], subset: Iterable[int], *, tol: float = 1e-12) -> tuple[float, float]:
    """Return (row-divergence on O, O-to-complement boundary flux)."""
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("square transfer matrix required")
    for a in range(n):
        for b in range(n):
            if not isclose(matrix[a][b], -matrix[b][a], abs_tol=tol, rel_tol=tol):
                raise ValueError("K_phys role transfer must be antisymmetric")
    O = set(subset)
    if any(a < 0 or a >= n for a in O):
        raise ValueError("subset index out of range")
    row_divergence = sum(sum(matrix[a]) for a in O)
    boundary = sum(matrix[a][b] for a in O for b in range(n) if b not in O)
    return row_divergence, boundary


RAW_MATERIAL_LOCATORS = frozenset({"material_relink", "new_coherent_ancestry"})
NATIVE_OWNER_TYPES = frozenset({
    "source_sgs",
    "strain_dissipation",
    "actual_nonlinear_work",
    "shell_service",
})

RAW_ROLE_PROBE_LOCATORS = frozenset({
    "role_change",
    "probe_change",
    "role_probe_change",
})

ZERO_DEPTH_CERTIFIED_ROLE_TRANSITIONS = frozenset({
    "same_state_reanchor",
    "common_transport_gauge",
    "kphys_relink",
})


def resolve_material_locator(locator: str, *, native_owner: str | None) -> str:
    """A raw material locator must resolve to a separately typed native PDE owner."""
    if locator not in RAW_MATERIAL_LOCATORS:
        raise ValueError("this resolver is only for raw material-state locators")
    if native_owner not in NATIVE_OWNER_TYPES:
        raise ValueError("raw material state has no canonical owner without native PDE evidence")
    return native_owner


def resolve_role_probe_locator(locator: str, *, native_owner: str | None) -> str:
    """A role/probe change is a locator until an existing native PDE owner resolves it."""
    if locator not in RAW_ROLE_PROBE_LOCATORS:
        raise ValueError("this resolver is only for raw role/probe locators")
    if native_owner not in NATIVE_OWNER_TYPES:
        raise ValueError("role/probe change has no canonical owner without native PDE evidence")
    return native_owner


def certified_role_transition_generation_depth(kind: str) -> int:
    """Certified gauge/reanchor/K_phys transitions add no recursive generation depth."""
    if kind not in ZERO_DEPTH_CERTIFIED_ROLE_TRANSITIONS:
        raise ValueError("unresolved role transition must fail closed to native PDE resolution")
    return 0


@dataclass(frozen=True)
class PhysicalHit:
    time: float
    cause: str


@dataclass(frozen=True)
class JointStop:
    time: float | None
    causes: frozenset[str]
    sidecars: tuple[str, ...]


def physical_first_stop(hits: Iterable[PhysicalHit], *, sidecars: Iterable[str] = (), tol: float = 1e-12) -> JointStop:
    """Classify physical first time first; attach representation sidecars afterward."""
    hits = tuple(hits)
    if not hits:
        return JointStop(None, frozenset(), tuple(sidecars))
    t0 = min(h.time for h in hits)
    causes = frozenset(h.cause for h in hits if isclose(h.time, t0, abs_tol=tol, rel_tol=0.0))
    return JointStop(t0, causes, tuple(sidecars))


def high_strain_epoch_upper_scales(N0: float, steps: int) -> tuple[float, ...]:
    """Maximum scales along a consecutive certified high-strain lineage."""
    if N0 <= 0.0 or steps < 0:
        raise ValueError("positive root scale and nonnegative step count required")
    return tuple(N0 * (3.0 / 16.0) ** j for j in range(steps + 1))


def signed_good_required_backshift(T0: float, depth: int) -> float:
    """Certified lower bound on cumulative registration-surface backshift."""
    if T0 <= 0.0 or depth < 0:
        raise ValueError("positive natural lifetime and nonnegative depth required")
    return (1792.0 / 7605.0) * T0 * ((64.0 / 25.0) ** depth - 1.0)
