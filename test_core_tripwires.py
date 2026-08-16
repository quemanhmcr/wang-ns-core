import unittest

from core_tripwires import (
    PhysicalHit,
    mode_set_endpoint_energy,
    resolve_material_locator,
    antisymmetric_subset_flux,
    high_strain_epoch_upper_scales,
    inherited_stock_component,
    physical_first_stop,
    restrict_canonical_positive_mass,
    selected_family_boundary,
    signed_good_required_backshift,
    triad_donor_kernel,
)


class CoreTripwires(unittest.TestCase):
    def test_triad_kernel_has_exact_negative_and_positive_marginals(self):
        transfers = (-3.0, 1.0, 2.0)
        M = triad_donor_kernel(transfers)
        self.assertEqual([sum(row) for row in M], [3.0, 0.0, 0.0])
        self.assertEqual([sum(M[i][j] for i in range(3)) for j in range(3)], [0.0, 1.0, 2.0])

    def test_two_donors_do_not_clone_one_recipient_charge(self):
        transfers = (-1.0, -2.0, 3.0)
        M = triad_donor_kernel(transfers)
        self.assertEqual(sum(M[i][2] for i in range(3)), 3.0)
        self.assertEqual(sum(sum(row) for row in M), 3.0)

    def test_resolved_contact_only_restricts_existing_positive_mass(self):
        mixed, hh = restrict_canonical_positive_mass(7.5, 0.2)
        self.assertAlmostEqual(mixed, 1.5)
        self.assertAlmostEqual(hh, 6.0)
        self.assertAlmostEqual(mixed + hh, 7.5)

    def test_inherited_stock_gate_cannot_erase_large_simultaneous_work(self):
        self.assertTrue(inherited_stock_component(E0=1.0, E1=1.0, residual_positive_work=0.19,
                                                  same_carrier=True, no_first_stop=True,
                                                  earlier_endpoint_non_event=True))
        self.assertFalse(inherited_stock_component(E0=1.0, E1=1.0, residual_positive_work=0.20,
                                                   same_carrier=True, no_first_stop=True,
                                                   earlier_endpoint_non_event=True))

    def test_positive_selected_family_boundary_can_exist_without_generation(self):
        energies = {"a": 2.0, "b": 3.0, "c": 5.0}
        self.assertEqual(selected_family_boundary(energies, {"a"}, {"b"}), 5.0)
        # The function returns boundary provenance only; no event object is created.

    def test_smooth_relink_subset_divergence_is_exact_boundary_flux(self):
        T = (
            (0.0, 2.0, -1.0),
            (-2.0, 0.0, 4.0),
            (1.0, -4.0, 0.0),
        )
        divergence, boundary = antisymmetric_subset_flux(T, {0, 1})
        self.assertAlmostEqual(divergence, boundary)
        self.assertAlmostEqual(boundary, 3.0)

    def test_mode_set_stock_uses_boundary_flow_not_internal_traffic(self):
        self.assertAlmostEqual(mode_set_endpoint_energy(10.0, inflow=3.0, outflow=2.0, dissipation=4.0), 7.0)

    def test_raw_material_locator_must_resolve_to_a_different_native_type(self):
        with self.assertRaises(ValueError):
            resolve_material_locator("material_relink", native_owner=None)
        with self.assertRaises(ValueError):
            resolve_material_locator("material_relink", native_owner="material_relink")
        self.assertEqual(
            resolve_material_locator("material_relink", native_owner="strain_dissipation"),
            "strain_dissipation",
        )

    def test_sidecar_cannot_create_or_move_physical_first_stop(self):
        hits = [PhysicalHit(2.0, "source"), PhysicalHit(2.0, "strain"), PhysicalHit(3.0, "hh")]
        stop = physical_first_stop(hits, sidecars=["R_switch=5"])
        self.assertEqual(stop.time, 2.0)
        self.assertEqual(stop.causes, frozenset({"source", "strain"}))
        self.assertEqual(stop.sidecars, ("R_switch=5",))
        no_hit = physical_first_stop([], sidecars=["R_switch=5"])
        self.assertIsNone(no_hit.time)
        self.assertEqual(no_hit.causes, frozenset())

    def test_consecutive_high_strain_scales_descend_by_physical_three_sixteenths(self):
        scales = high_strain_epoch_upper_scales(16.0, 3)
        self.assertEqual(scales, (16.0, 3.0, 0.5625, 0.10546875))

    def test_signed_good_generated_required_backshift_grows_geometrically(self):
        shifts = [signed_good_required_backshift(1.0, n) for n in range(5)]
        self.assertEqual(shifts[0], 0.0)
        self.assertTrue(all(b > a for a, b in zip(shifts, shifts[1:])))


if __name__ == "__main__":
    unittest.main()
