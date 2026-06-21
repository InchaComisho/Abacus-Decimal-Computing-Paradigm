# Abacus Decimal Cell Specification

## Purpose

This document defines the minimum technical specification for the **Abacus Decimal Computing Paradigm**.

The goal is to separate the core cell rules from the broader conceptual README so that the architecture can be implemented, tested, simulated, and later mapped to electronic, optical, and quantum-compatible systems.

---

## 1. Cell Model

An abacus decimal cell represents one decimal digit using five binary positions.

```text
Cell = [H, L1, L2, L3, L4]
```

Where:

- `H` is the upper bead position and has value 5.
- `L1`, `L2`, `L3`, and `L4` are lower bead positions and each has value 1.
- Each position is either `0` or `1`.

The numerical value is:

```text
D = 5H + L1 + L2 + L3 + L4
```

The valid decimal range is:

```text
D ∈ {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
```

---

## 2. Canonical Pattern Rule

A five-bit cell has 32 possible binary states.

This specification reserves 10 canonical states as valid decimal digits. All other states are treated as non-canonical unless explicitly assigned to an extension layer.

The canonical representation activates lower beads in sequence.

```text
Digit  H  L1 L2 L3 L4
0      0   0  0  0  0
1      0   1  0  0  0
2      0   1  1  0  0
3      0   1  1  1  0
4      0   1  1  1  1
5      1   0  0  0  0
6      1   1  0  0  0
7      1   1  1  0  0
8      1   1  1  1  0
9      1   1  1  1  1
```

Note: physical display orientation may be reversed depending on LED layout, abacus orientation, or optical cell orientation. The logical rule remains the same: the lower part stores a count from 0 to 4.

---

## 3. Encoding Rule

To encode a decimal digit `D`:

```text
if D < 5:
    H = 0
    lower_count = D
else:
    H = 1
    lower_count = D - 5
```

Then set the first `lower_count` lower bits to `1` and the rest to `0`.

---

## 4. Decoding Rule

To decode a canonical cell:

```text
D = 5H + count(L1, L2, L3, L4)
```

A decoder must also validate whether the lower-bit pattern is canonical.

Examples of canonical lower patterns:

```text
0000
1000
1100
1110
1111
```

Examples of non-canonical lower patterns:

```text
0100
1010
0011
0110
```

A non-canonical state may still have a numerical sum, but it is not a valid abacus decimal pattern under this specification.

---

## 5. Validity Rule

A cell is valid if and only if:

1. `H ∈ {0, 1}`
2. every lower bit is in `{0, 1}`
3. the lower-bit sequence is canonical
4. the decoded digit is within `0..9`

A cell is invalid if it violates any of these rules.

Invalid states may be used for:

- error detection
- transition-state detection
- debugging
- reserved extension states
- control signaling in future designs

---

## 6. Normalization Rule

Normalization converts a decimal digit into the canonical five-bit pattern.

```text
raw input
↓
extract or compute decimal digit
↓
map digit to canonical abacus pattern
↓
output normalized cell
```

Normalization should be applied after arithmetic operations, noisy reads, optical classification, or external input.

---

## 7. Addition Rule

Digit-wise addition follows ordinary decimal arithmetic.

```text
S = A + B + carry_in

if S >= 10:
    result = S - 10
    carry_out = 1
else:
    result = S
    carry_out = 0
```

The result digit must be normalized into a canonical abacus decimal cell.

---

## 8. Subtraction Rule

Digit-wise subtraction follows ordinary decimal borrowing.

```text
S = A - B - borrow_in

if S < 0:
    result = S + 10
    borrow_out = 1
else:
    result = S
    borrow_out = 0
```

The result digit must be normalized into a canonical abacus decimal cell.

---

## 9. Multi-Digit Rule

A multi-digit number is represented as an ordered list of abacus decimal cells.

```text
1234 = [1] [2] [3] [4]
```

For arithmetic, cells may be processed from the least significant digit toward the most significant digit, using carry or borrow propagation.

---

## 10. Electronic Display Mapping

Each bit may be connected to an LED or equivalent visual output.

```text
bit 1 = light on
bit 0 = light off
```

This creates a visible abacus-like decimal pattern that can be inspected by:

- humans
- cameras
- CMOS sensors
- machine vision algorithms
- optical feedback systems

---

## 11. Optical Extension Mapping

The same cell may later be mapped to optical or photonic structures.

Possible physical mappings include:

- LED arrays
- micro-LED arrays
- optical bead cells
- waveguide nodes
- spatial light modulator pixels
- photonic resonator states
- sensor-readable optical patterns

Additional optical degrees of freedom may include:

- wavelength
- color
- intensity
- phase
- polarization
- time bin
- spatial mode

These extensions must preserve the canonical decimal layer unless an explicit extended-mode specification is introduced.

---

## 12. Boundary of Claim

This specification defines a decimal-spatial information cell.

It does not claim that:

- binary computing should be abandoned
- current CPUs or GPUs are immediately surpassed
- quantum advantage has been achieved
- this is already a completed quantum computer

The specification is intended as a practical starting point for simulation, electronic implementation, optical transition, and quantum-compatible architectural study.
