# Architecture Diagrams

This document provides Mermaid diagrams for the **Abacus Decimal Computing Paradigm**.

These diagrams are intended for README integration, documentation, presentations, and future visual assets.

---

# 1. Five-Bit Abacus Decimal Cell

```mermaid
flowchart TB
    H[Upper bit H<br/>Value = 5]
    L1[Lower bit L1<br/>Value = 1]
    L2[Lower bit L2<br/>Value = 1]
    L3[Lower bit L3<br/>Value = 1]
    L4[Lower bit L4<br/>Value = 1]

    H --> D[Decimal digit D = 5H + L1 + L2 + L3 + L4]
    L1 --> D
    L2 --> D
    L3 --> D
    L4 --> D
```

---

# 2. Canonical Digit Patterns

```mermaid
flowchart LR
    D0[0<br/>H0 L0000]
    D1[1<br/>H0 L1000]
    D2[2<br/>H0 L1100]
    D3[3<br/>H0 L1110]
    D4[4<br/>H0 L1111]
    D5[5<br/>H1 L0000]
    D6[6<br/>H1 L1000]
    D7[7<br/>H1 L1100]
    D8[8<br/>H1 L1110]
    D9[9<br/>H1 L1111]
```

---

# 3. Encoding and Decoding Flow

```mermaid
flowchart LR
    A[Decimal digit 0-9]
    B[Encoder]
    C[Five-bit abacus decimal cell]
    D[Validity checker]
    E[Decoder]
    F[Decimal digit output]

    A --> B --> C --> D --> E --> F
    D -->|invalid state| X[Error / reserved state]
```

---

# 4. Multi-Digit Decimal Architecture

```mermaid
flowchart LR
    A0[Digit 3<br/>5-bit cell]
    A1[Digit 2<br/>5-bit cell]
    A2[Digit 1<br/>5-bit cell]
    A3[Digit 0<br/>5-bit cell]

    A0 --- A1 --- A2 --- A3

    A3 --> C0[Carry / Borrow]
    C0 --> A2
    A2 --> C1[Carry / Borrow]
    C1 --> A1
    A1 --> C2[Carry / Borrow]
    C2 --> A0
```

---

# 5. Electronic to Optical Development Path

```mermaid
flowchart LR
    A[Electronic five-bit decimal cell]
    B[LED visible abacus pattern]
    C[Camera / CMOS recognition]
    D[Optical cell array]
    E[Multi-valued photonic state]
    F[Quantum-compatible photonic architecture]

    A --> B
    B --> C
    B --> D
    D --> E
    E --> F
```

---

# 6. Multi-Layer Validation Model

```mermaid
flowchart TB
    S[Abacus decimal state]

    S --> E[Electronic validation]
    S --> L[LED pattern validation]
    S --> C[Camera / CMOS validation]
    S --> H[Human pattern recognition]

    E --> R[Validation result]
    L --> R
    C --> R
    H --> R

    R --> OK[Canonical state]
    R --> NG[Invalid / noisy / reserved state]
```

---

# 7. Relationship to Related Architectures

```mermaid
flowchart TB
    A[Abacus Decimal Computing Paradigm<br/>Electronic decimal-spatial foundation]
    B[Electronic-Optical Hybrid<br/>Quantum-Compatible Computing]
    C[Electronic-Optical Hybrid<br/>Computing Architecture]
    D[Optical Bead Quantum Computing<br/>Multi-Valued Photonic Paradigm]
    E[Future Optical Quantum Computing]

    A --> B
    A --> C
    B --> D
    C --> D
    D --> E
```

---

# 8. Claim Boundary Diagram

```mermaid
flowchart LR
    A[Current confirmed layer<br/>Concept + digital specification + simulation]
    B[Near-term layer<br/>FPGA / LED / camera validation]
    C[Research layer<br/>Optical cell and photonic extension]
    D[Future hypothesis layer<br/>Quantum-compatible photonic computing]

    A --> B --> C --> D
```

This diagram is important because it separates the current implementation from future research hypotheses.
