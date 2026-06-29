# Comparison with BCD

## Overview

This document compares the **Abacus Decimal Computing Paradigm** with conventional **Binary-Coded Decimal (BCD)**.

The abacus decimal cell is not proposed as a more compact replacement for BCD. Instead, it is proposed as a **spatial, visual, and optically extendable decimal information structure**.

---

## 1. BCD in Brief

BCD represents one decimal digit using four binary bits.

```text
0 = 0000
1 = 0001
2 = 0010
3 = 0011
4 = 0100
5 = 0101
6 = 0110
7 = 0111
8 = 1000
9 = 1001
```

Since four bits can represent 16 states, BCD uses 10 valid states and leaves 6 states unused or invalid.

BCD is useful because it allows decimal digits to be represented in a digital system while remaining closer to human decimal notation than pure binary integers.

---

## 2. Abacus Decimal Cell in Brief

The abacus decimal cell uses five binary positions.

```text
[H, L1, L2, L3, L4]
```

Where:

- `H = 5`
- `L1, L2, L3, L4 = 1 each`

The value is:

```text
D = 5H + L1 + L2 + L3 + L4
```

Canonical patterns:

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

Five bits can represent 32 states, but only 10 are canonical decimal states.

---

## 3. Key Difference

BCD is primarily a **compact machine-readable decimal code**.

The abacus decimal cell is a **structured decimal-spatial cell**.

Its purpose is not simple storage efficiency. Its purpose is to support:

- decimal arithmetic
- visual readability
- LED display
- human pattern recognition
- camera-based recognition
- invalid-state detection
- optical extension
- photonic multi-valued mapping
- quantum-compatible architectural continuity

---

## 4. Comparison Table

| Feature | BCD | Abacus Decimal Cell |
|---|---|---|
| Bits per decimal digit | 4 | 5 |
| Valid decimal states | 10 | 10 |
| Total possible states | 16 | 32 |
| Unused/non-canonical states | 6 | 22 |
| Human-readable bit pattern | Low | Higher, if displayed spatially |
| Abacus-like structure | No | Yes |
| LED visualization | Possible, but not structurally abacus-like | Native to the concept |
| Camera/machine-vision readability | Possible | Stronger due to canonical spatial patterns |
| Optical extension | Not inherent | Designed as an extension path |
| Primary design goal | Decimal encoding | Decimal-spatial architecture |

---

## 5. Why Five Bits Instead of Four?

Four bits are enough to encode 0 to 9.

However, the goal of this project is not minimum-bit encoding.

Five bits are used because they reproduce the structure of one abacus column:

```text
1 upper position = 5
4 lower positions = 1 + 1 + 1 + 1
```

This gives the digit a visible and spatial structure.

A digit is no longer only a binary symbol. It becomes a pattern that can be:

- seen
- counted
- checked
- photographed
- recognized
- mapped to optical cells

---

## 6. Error Detection Difference

BCD has 6 invalid states out of 16.

The abacus decimal cell has 22 non-canonical states out of 32.

This larger non-canonical space may be useful for detecting abnormal states, especially when the cell is visualized or optically read.

However, this does not automatically mean better error correction. It means that the structure provides a larger invalid-state space that can be studied for detection, redundancy, or transition-state design.

---

## 7. Suitable Use Cases

BCD is suitable for:

- compact decimal encoding
- decimal arithmetic in digital systems
- financial and commercial systems
- decimal floating point implementation

The abacus decimal cell may be suitable for:

- visible decimal computing
- educational decimal logic
- abacus-inspired arithmetic circuits
- LED-based decimal displays
- machine-vision validation
- optical pattern experiments
- electronic-optical hybrid computing
- quantum-compatible photonic architecture studies

---

## 8. Boundary of Claim

This comparison does not claim that the abacus decimal cell is universally superior to BCD.

BCD is more compact and already well established.

The abacus decimal cell is proposed for a different purpose: to create a shared structure between electronic logic, human-readable patterns, optical cells, and future photonic or quantum-compatible systems.

The important distinction is:

```text
BCD = decimal code
Abacus Decimal Cell = decimal-spatial computing structure
```
