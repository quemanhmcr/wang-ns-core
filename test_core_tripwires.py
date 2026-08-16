import unittest

from core_tripwires import (
    PhysicalHit,
    hard_shell_terminal_supply_cover,
    mode_set_endpoint_energy,
    resolve_material_locator,
    resolve_role_probe_locator,
    certified_role_transition_generation_depth,
    observer_partition_channel_energies,
    probe_readout,
    physical_witness_relay,
    witness_chain_owner,
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

    def test_terminal_hard_shell_energy_has_only_stock_or_actual_nonlinear_inflow_supply(self):
        from core_tripwires import HARD_SHELL_ENERGY_SUPPLY_TYPES
        self.assertEqual(
            HARD_SHELL_ENERGY_SUPPLY_TYPES,
            frozenset({"modal_stock", "actual_nonlinear_boundary_inflow"}),
        )
        self.assertEqual(
            hard_shell_terminal_supply_cover(
                initial_energy=0.1,
                terminal_energy=1.0,
                nonlinear_inflow=1.1,
                nonlinear_outflow=0.1,
                viscous_dissipation=0.1,
            ),
            frozenset({"actual_nonlinear_boundary_inflow"}),
        )

    def test_hard_shell_supply_cover_retains_exact_stock_inflow_tie(self):
        self.assertEqual(
            hard_shell_terminal_supply_cover(
                initial_energy=0.2,
                terminal_energy=1.0,
                nonlinear_inflow=0.8,
                nonlinear_outflow=0.0,
                viscous_dissipation=0.0,
            ),
            frozenset({"modal_stock", "actual_nonlinear_boundary_inflow"}),
        )

    def test_dissipation_and_outflow_cannot_be_positive_hard_shell_suppliers(self):
        cover = hard_shell_terminal_supply_cover(
            initial_energy=1.2,
            terminal_energy=0.5,
            nonlinear_inflow=0.0,
            nonlinear_outflow=0.4,
            viscous_dissipation=0.3,
        )
        self.assertEqual(cover, frozenset({"modal_stock"}))
        self.assertNotIn("strain_dissipation", cover)
        self.assertNotIn("source_sgs", cover)

    def test_hard_shell_supply_cover_refuses_a_nonphysical_balance(self):
        with self.assertRaises(ValueError):
            hard_shell_terminal_supply_cover(
                initial_energy=0.1,
                terminal_energy=1.0,
                nonlinear_inflow=0.1,
                nonlinear_outflow=0.0,
                viscous_dissipation=0.0,
            )

    def test_raw_material_locator_must_resolve_to_a_different_native_type(self):
        with self.assertRaises(ValueError):
            resolve_material_locator("material_relink", native_owner=None)
        with self.assertRaises(ValueError):
            resolve_material_locator("material_relink", native_owner="material_relink")
        self.assertEqual(
            resolve_material_locator("material_relink", native_owner="strain_dissipation"),
            "strain_dissipation",
        )

    def test_post_role_probe_native_owner_vocabulary_is_exactly_physical(self):
        from core_tripwires import NATIVE_OWNER_TYPES
        self.assertEqual(
            NATIVE_OWNER_TYPES,
            frozenset({
                "source_sgs",
                "strain_dissipation",
                "actual_nonlinear_work",
            }),
        )

    def test_shell_and_service_are_physical_witnesses_not_fourth_owner_type(self):
        from core_tripwires import NATIVE_OWNER_TYPES, PHYSICAL_STATE_WITNESS_TYPES
        self.assertNotIn("shell_service", NATIVE_OWNER_TYPES)
        self.assertIn("coherent_service", PHYSICAL_STATE_WITNESS_TYPES)
        self.assertIn("critical_shell", PHYSICAL_STATE_WITNESS_TYPES)
        self.assertIn("hard_tail_state", PHYSICAL_STATE_WITNESS_TYPES)

    def test_source_service_shell_chain_keeps_one_upstream_causal_owner(self):
        self.assertEqual(
            witness_chain_owner("source_sgs", ("coherent_service", "critical_shell")),
            "source_sgs",
        )
        relay = physical_witness_relay("source_sgs", "coherent_service")
        self.assertFalse(relay.new_causal_charge_created)

    def test_dissipation_and_nonlinear_work_can_supply_shell_state_without_owner_clone(self):
        self.assertEqual(witness_chain_owner("strain_dissipation", ("critical_shell",)), "strain_dissipation")
        self.assertEqual(
            witness_chain_owner("actual_nonlinear_work", ("hard_tail_state", "critical_shell")),
            "actual_nonlinear_work",
        )

    def test_state_witness_cannot_self_authorize_as_upstream_owner(self):
        with self.assertRaises(ValueError):
            physical_witness_relay("shell_service", "critical_shell")
        with self.assertRaises(ValueError):
            physical_witness_relay("critical_shell", "coherent_service")

    def test_role_probe_locator_cannot_self_authorize_as_an_owner(self):
        for locator in ("role_change", "probe_change", "role_probe_change"):
            with self.assertRaises(ValueError):
                resolve_role_probe_locator(locator, native_owner=None)
            with self.assertRaises(ValueError):
                resolve_role_probe_locator(locator, native_owner="genuine_role_probe_change")
        self.assertEqual(
            resolve_role_probe_locator("probe_change", native_owner="actual_nonlinear_work"),
            "actual_nonlinear_work",
        )
        self.assertEqual(
            resolve_role_probe_locator("role_change", native_owner="strain_dissipation"),
            "strain_dissipation",
        )

    def test_material_locator_cannot_escape_through_a_role_probe_alias(self):
        with self.assertRaises(ValueError):
            resolve_material_locator("material_relink", native_owner="genuine_role_probe_change")

    def test_certified_gauge_reanchor_and_kphys_relink_have_zero_depth(self):
        for kind in ("same_state_reanchor", "common_transport_gauge", "kphys_relink"):
            self.assertEqual(certified_role_transition_generation_depth(kind), 0)
        with self.assertRaises(ValueError):
            certified_role_transition_generation_depth("unresolved_probe_jump")

    def test_observer_partition_can_move_channel_energy_with_fixed_total_physics(self):
        e0 = observer_partition_channel_energies(10.0, 0.0)
        e1 = observer_partition_channel_energies(10.0, 0.7853981633974483)
        self.assertAlmostEqual(sum(e0), 10.0)
        self.assertAlmostEqual(sum(e1), 10.0)
        self.assertNotEqual(e0, e1)

    def test_probe_can_change_coefficient_while_carrier_is_identical(self):
        w = (3.0 + 0j, 0j)
        parallel = probe_readout(w, (1.0 + 0j, 0j))
        orthogonal = probe_readout(w, (0j, 1.0 + 0j))
        self.assertEqual(parallel, 3.0 + 0j)
        self.assertEqual(orthogonal, 0j)
        self.assertEqual(sum(abs(x) ** 2 for x in w), 9.0)

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
