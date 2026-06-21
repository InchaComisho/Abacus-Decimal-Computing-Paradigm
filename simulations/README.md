# Simulations

This directory contains executable reference simulations for the **Abacus Decimal Computing Paradigm**.

The current implementation is intentionally simple and dependency-free. It is designed to verify the minimum technical layer of the proposal before moving toward FPGA, LED, optical, or quantum-compatible experiments.

---

## File

- `abacus_decimal.py`  
  Reference implementation of the five-bit abacus decimal cell.

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

## Usage

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

---

## What This Simulation Tests

This reference implementation tests:

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

---

## Next Simulation Targets

Recommended future additions:

- CSV output for error simulations
- plots of detection rates
- BCD comparison benchmark
- LED pattern PNG generation
- camera recognition mockup
- FPGA/HDL equivalent tests
