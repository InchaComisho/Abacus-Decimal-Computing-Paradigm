#!/usr/bin/env python3
"""
Civilization adoption scenario simulation for the Abacus Decimal Computing Paradigm.

This simulation compares two simplified futures:

1. fragmented
   Each company or institution develops electronic-optical / optical computing
   independently, with low software reuse and late standardization.

2. shared_layer
   A common five-bit abacus decimal compatibility layer is adopted early,
   improving software continuity, standardization, and hardware transition.

The model is intentionally simplified. It is not a prediction. It is a scenario
comparison tool for exploring how standardization and compatibility may affect
computer ecosystem development speed.

Usage:

    python simulations/civilization_adoption_sim.py
    python simulations/civilization_adoption_sim.py --start-year 2026 --end-year 2060
    python simulations/civilization_adoption_sim.py --csv outputs/civilization_adoption.csv
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Tuple


LAYERS: Tuple[str, ...] = (
    "electronic_abacus_decimal",
    "led_cmos_validation",
    "electronic_optical_hybrid",
    "optical_cpu_photonic_processor",
    "personal_computer_integration",
    "quantum_compatible_photonic_extension",
)

THRESHOLDS: Tuple[Tuple[str, float], ...] = (
    ("research_prototype", 0.30),
    ("developer_ecosystem", 0.50),
    ("early_commercial", 0.70),
    ("personal_computer_ready", 0.85),
    ("mature_ecosystem", 0.95),
)


@dataclass(frozen=True)
class ScenarioParameters:
    name: str
    research_rate: float
    standardization_factor: float
    software_reuse_factor: float
    transition_efficiency: float
    fragmentation_factor: float
    os_integration_factor: float
    pc_adoption_factor: float
    standardization_weight: float = 0.030
    software_reuse_weight: float = 0.028
    inheritance_weight: float = 0.035
    fragmentation_weight: float = 0.040
    os_weight: float = 0.020
    pc_weight: float = 0.020


@dataclass
class YearState:
    year: int
    scenario: str
    layer_maturity: Dict[str, float] = field(default_factory=dict)
    os_integration: float = 0.0
    software_ecosystem: float = 0.0
    pc_readiness: float = 0.0


def clamp(value: float, lower: float = 0.0, upper: float = 1.0) -> float:
    return max(lower, min(upper, value))


def initial_state(start_year: int, scenario: ScenarioParameters) -> YearState:
    """Create the initial maturity state.

    The shared-layer scenario starts with a small advantage in the first layer
    because the compatibility abstraction is assumed to be defined early.
    """
    if scenario.name == "shared_layer":
        initial = {
            "electronic_abacus_decimal": 0.16,
            "led_cmos_validation": 0.08,
            "electronic_optical_hybrid": 0.03,
            "optical_cpu_photonic_processor": 0.01,
            "personal_computer_integration": 0.00,
            "quantum_compatible_photonic_extension": 0.00,
        }
        return YearState(
            year=start_year,
            scenario=scenario.name,
            layer_maturity=initial,
            os_integration=0.05,
            software_ecosystem=0.08,
            pc_readiness=0.00,
        )

    initial = {
        "electronic_abacus_decimal": 0.06,
        "led_cmos_validation": 0.02,
        "electronic_optical_hybrid": 0.01,
        "optical_cpu_photonic_processor": 0.00,
        "personal_computer_integration": 0.00,
        "quantum_compatible_photonic_extension": 0.00,
    }
    return YearState(
        year=start_year,
        scenario=scenario.name,
        layer_maturity=initial,
        os_integration=0.01,
        software_ecosystem=0.02,
        pc_readiness=0.00,
    )


def update_state(previous: YearState, scenario: ScenarioParameters) -> YearState:
    """Advance one year using a simplified ecosystem-development model."""
    new_layers: Dict[str, float] = {}

    for index, layer in enumerate(LAYERS):
        current = previous.layer_maturity[layer]
        previous_layer_maturity = 0.0 if index == 0 else previous.layer_maturity[LAYERS[index - 1]]

        standardization_bonus = scenario.standardization_factor * scenario.standardization_weight
        reuse_bonus = scenario.software_reuse_factor * scenario.software_reuse_weight
        inheritance_bonus = previous_layer_maturity * scenario.transition_efficiency * scenario.inheritance_weight
        fragmentation_penalty = scenario.fragmentation_factor * scenario.fragmentation_weight

        # Later layers should not mature too far ahead of their dependencies.
        dependency_gate = 1.0 if index == 0 else clamp(previous_layer_maturity + 0.15)

        delta = (
            scenario.research_rate
            + standardization_bonus
            + reuse_bonus
            + inheritance_bonus
            - fragmentation_penalty
        ) * dependency_gate

        # Early layers are easier to validate than late photonic/quantum-compatible layers.
        difficulty = 1.0 + index * 0.18
        new_layers[layer] = clamp(current + delta / difficulty)

    software_ecosystem = clamp(
        previous.software_ecosystem
        + scenario.research_rate * 0.40
        + scenario.software_reuse_factor * 0.035
        + scenario.standardization_factor * 0.030
        - scenario.fragmentation_factor * 0.030
    )

    os_integration = clamp(
        previous.os_integration
        + scenario.os_integration_factor * scenario.os_weight
        + software_ecosystem * 0.025
        + new_layers["electronic_optical_hybrid"] * 0.015
        - scenario.fragmentation_factor * 0.015
    )

    pc_readiness = clamp(
        previous.pc_readiness
        + scenario.pc_adoption_factor * scenario.pc_weight
        + os_integration * 0.020
        + software_ecosystem * 0.020
        + new_layers["optical_cpu_photonic_processor"] * 0.025
        - scenario.fragmentation_factor * 0.020
    )

    # Personal computer integration is modeled both as its own layer and as a platform score.
    new_layers["personal_computer_integration"] = max(
        new_layers["personal_computer_integration"],
        pc_readiness * 0.85,
    )

    return YearState(
        year=previous.year + 1,
        scenario=scenario.name,
        layer_maturity=new_layers,
        os_integration=os_integration,
        software_ecosystem=software_ecosystem,
        pc_readiness=pc_readiness,
    )


def run_scenario(start_year: int, end_year: int, scenario: ScenarioParameters) -> List[YearState]:
    states = [initial_state(start_year, scenario)]
    while states[-1].year < end_year:
        states.append(update_state(states[-1], scenario))
    return states


def threshold_years(states: Iterable[YearState], metric: str) -> Dict[str, int | None]:
    """Return the first year in which the selected metric reaches each threshold."""
    result: Dict[str, int | None] = {name: None for name, _ in THRESHOLDS}
    for state in states:
        if metric in state.layer_maturity:
            value = state.layer_maturity[metric]
        else:
            value = getattr(state, metric)
        for name, threshold in THRESHOLDS:
            if result[name] is None and value >= threshold:
                result[name] = state.year
    return result


def rows_from_states(states: Iterable[YearState]) -> List[Dict[str, str | int | float]]:
    rows: List[Dict[str, str | int | float]] = []
    for state in states:
        row: Dict[str, str | int | float] = {
            "year": state.year,
            "scenario": state.scenario,
            "os_integration": round(state.os_integration, 4),
            "software_ecosystem": round(state.software_ecosystem, 4),
            "pc_readiness": round(state.pc_readiness, 4),
        }
        for layer in LAYERS:
            row[layer] = round(state.layer_maturity[layer], 4)
        rows.append(row)
    return rows


def write_csv(path: str, states: Iterable[YearState]) -> None:
    rows = rows_from_states(states)
    if not rows:
        return
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def print_summary(fragmented: List[YearState], shared: List[YearState]) -> None:
    metrics = (
        "software_ecosystem",
        "os_integration",
        "optical_cpu_photonic_processor",
        "personal_computer_integration",
        "pc_readiness",
        "quantum_compatible_photonic_extension",
    )

    print("Civilization Adoption Simulation")
    print("================================")
    print("This is a scenario comparison, not a prediction.\n")

    for metric in metrics:
        print(f"Metric: {metric}")
        f_years = threshold_years(fragmented, metric)
        s_years = threshold_years(shared, metric)
        print("  Threshold                    fragmented  shared_layer  acceleration")
        for name, _threshold in THRESHOLDS:
            fy = f_years[name]
            sy = s_years[name]
            if fy is None or sy is None:
                accel = "n/a"
            else:
                accel = f"{fy - sy:+d} years"
            print(f"  {name:<28} {str(fy):>10}  {str(sy):>12}  {accel:>12}")
        print()

    print("Final year values")
    print("-----------------")
    for states in (fragmented, shared):
        last = states[-1]
        print(f"Scenario: {last.scenario}")
        print(f"  software_ecosystem                {last.software_ecosystem:.3f}")
        print(f"  os_integration                    {last.os_integration:.3f}")
        print(f"  pc_readiness                      {last.pc_readiness:.3f}")
        for layer in LAYERS:
            print(f"  {layer:<35} {last.layer_maturity[layer]:.3f}")
        print()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Civilization adoption scenario simulation")
    parser.add_argument("--start-year", type=int, default=2026)
    parser.add_argument("--end-year", type=int, default=2060)
    parser.add_argument("--csv", help="Optional CSV output path")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    if args.end_year <= args.start_year:
        raise ValueError("end-year must be greater than start-year")

    fragmented_params = ScenarioParameters(
        name="fragmented",
        research_rate=0.030,
        standardization_factor=0.25,
        software_reuse_factor=0.20,
        transition_efficiency=0.25,
        fragmentation_factor=0.75,
        os_integration_factor=0.30,
        pc_adoption_factor=0.35,
    )

    shared_layer_params = ScenarioParameters(
        name="shared_layer",
        research_rate=0.034,
        standardization_factor=0.78,
        software_reuse_factor=0.72,
        transition_efficiency=0.70,
        fragmentation_factor=0.25,
        os_integration_factor=0.72,
        pc_adoption_factor=0.66,
    )

    fragmented = run_scenario(args.start_year, args.end_year, fragmented_params)
    shared = run_scenario(args.start_year, args.end_year, shared_layer_params)

    print_summary(fragmented, shared)

    if args.csv:
        write_csv(args.csv, [*fragmented, *shared])
        print(f"CSV written: {args.csv}")


if __name__ == "__main__":
    main()
