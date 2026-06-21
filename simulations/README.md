---

# Navigation

- [Repository Top](../README.md)
- [Japanese README](../README_ja.md)
- [Documentation Index](../docs/README.md)
- [Japanese Simulation Index](./README_ja.md)

---

# Simulations

This directory contains executable reference simulations for the **Abacus Decimal Computing Paradigm**.

The current implementations are intentionally simple and dependency-free. They are designed to test the minimum technical layer of the proposal and to explore ecosystem-level adoption scenarios before moving toward FPGA, LED, optical, or quantum-compatible experiments.

---

## Files

- `abacus_decimal.py`  
  Reference implementation of the five-bit abacus decimal cell.

- `test_abacus_decimal.py`  
  Basic unit tests for the abacus decimal reference implementation.

- `civilization_adoption_sim.py`  
  Scenario simulation comparing fragmented computer development with a shared abacus decimal compatibility layer.

---

## Cell Convention

The reference simulation uses this logical cell order:

```text
[H, L1, L2, L3, L4]
```

Where:

- `H` represents 5.
- `L1`, `L2`, `L3`, and `L4` each represent 1.

Canonical lower-bit patterns are sequential:

```text
0 -> 0000
1 -> 1000
2 -> 1100
3 -> 1110
4 -> 1111
```

Physical LED orientation may be reversed without changing the logical model.

---

## Abacus Decimal Cell Usage

Run from the repository root.

```bash
python simulations/abacus_decimal.py table
```

Show the canonical table.

```bash
python simulations/abacus_decimal.py encode 7
```

Encode one digit.

```bash
python simulations/abacus_decimal.py decode 1 1 1 0 0
```

Decode one five-bit cell.

```bash
python simulations/abacus_decimal.py add 1234 5678
```

Run digit-wise decimal addition.

```bash
python simulations/abacus_decimal.py sub 9000 1234
```

Run digit-wise decimal subtraction.

```bash
python simulations/abacus_decimal.py states
```

List all 32 possible five-bit states and classify them as canonical or non-canonical.

```bash
python simulations/abacus_decimal.py error --trials 10000 --flips 1
```

Run a random bit-flip error detection simulation.

```bash
python -m unittest simulations/test_abacus_decimal.py
```

Run unit tests.

---

## Civilization Adoption Scenario Usage

```bash
python simulations/civilization_adoption_sim.py
```

Run the default scenario comparison from 2026 to 2060.

```bash
python simulations/civilization_adoption_sim.py --start-year 2026 --end-year 2070
```

Run a longer scenario.

```bash
python simulations/civilization_adoption_sim.py --csv outputs/civilization_adoption.csv
```

Export year-by-year maturity scores to CSV.

The simulation compares:

- `fragmented`: each company or institution develops incompatible electronic-optical or optical computing architectures.
- `shared_layer`: a common five-bit abacus decimal compatibility layer is adopted early, improving software reuse, standardization, and hardware transition efficiency.

This is not a prediction. It is a scenario comparison model.

---

## What These Simulations Test

The abacus decimal reference implementation tests:

- decimal digit encoding
- decimal digit decoding
- canonical pattern validation
- non-canonical state detection
- one-digit addition
- one-digit subtraction
- multi-digit addition
- multi-digit subtraction
- random bit-flip detection
- silent valid-state mutation rate

The civilization adoption simulation explores:

- software ecosystem formation
- operating system integration speed
- optical CPU / photonic processor readiness
- personal computer adoption readiness
- fragmented development versus shared compatibility-layer development
- threshold year differences between scenarios

---

## Important Limitation

Canonical-state validation alone cannot detect every error.

A bit flip may transform one valid digit into another valid digit. This is called a silent valid mutation.

For safety-critical use, additional mechanisms should be studied:

- parity
- checksum
- redundant cells
- temporal consistency
- repeated sampling
- electronic and optical cross-validation

The civilization adoption simulation also has limitations. It uses simplified variables and should not be read as a date prediction.

---

## Next Simulation Targets

Recommended future additions:

- CSV output for error simulations
- plots of detection rates
- BCD comparison benchmark
- LED pattern PNG generation
- camera recognition mockup
- FPGA/HDL equivalent tests
- sensitivity analysis for civilization adoption parameters
- alternative scenarios for open standards, proprietary standards, and government-backed standards
