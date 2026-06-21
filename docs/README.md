# Documentation Index

This directory contains technical documents that strengthen the **Abacus Decimal Computing Paradigm** as a research and implementation-oriented repository.

---

## Core Documents

- [Specification](./SPEC.md)  
  Formal definition of the five-bit abacus decimal cell, canonical patterns, encoding, decoding, arithmetic, normalization, and optical mapping.

- [Comparison with BCD](./COMPARISON_WITH_BCD.md)  
  Explains how the abacus decimal cell differs from Binary-Coded Decimal. The key distinction is that BCD is a compact decimal code, while the abacus decimal cell is a decimal-spatial computing structure.

- [Validation Plan](./VALIDATION_PLAN.md)  
  Defines a staged roadmap from software simulation to FPGA, LED display, machine vision, optical cells, and quantum-compatible photonic mapping.

- [Architecture Diagrams](./ARCHITECTURE_DIAGRAMS.md)  
  Mermaid diagrams for the cell structure, encoding/decoding flow, electronic-to-optical path, multi-layer validation, and relationship to related architectures.

---

## Japanese Documents

- [仕様書（日本語）](./SPEC_ja.md)
- [BCDとの比較（日本語）](./COMPARISON_WITH_BCD_ja.md)
- [検証計画（日本語）](./VALIDATION_PLAN_ja.md)
- [アーキテクチャ図解（日本語）](./ARCHITECTURE_DIAGRAMS_ja.md)

---

## Recommended Reading Order

1. `SPEC.md`  
2. `COMPARISON_WITH_BCD.md`  
3. `VALIDATION_PLAN.md`  
4. `ARCHITECTURE_DIAGRAMS.md`  
5. `../simulations/README.md`  
6. `../simulations/abacus_decimal.py`

---

## Project Position

The Abacus Decimal Computing Paradigm should be understood as:

```text
electronic decimal-spatial foundation
↓
LED-visible computing
↓
electronic-optical hybrid computing
↓
multi-valued photonic computing
↓
quantum-compatible photonic architecture
```

It is not presented as a completed quantum computer. It is a staged architecture for connecting electronic, optical, and future quantum-compatible computing through a shared decimal-spatial information structure.
