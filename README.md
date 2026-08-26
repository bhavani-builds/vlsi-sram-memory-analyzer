# 💾 VLSI SRAM Memory Analyzer

A Python-based educational VLSI project for analyzing a
16 × 8 SRAM architecture through memory testing,
fault detection, power estimation, timing analysis,
and an interactive dashboard.

---

## 📌 Project Overview

This project demonstrates how an SRAM memory can be
modeled and analyzed using software.

The analyzer covers:

- SRAM memory modeling
- Address decoding
- Read/write verification
- Stuck-at fault testing
- Transition fault testing
- March testing
- Fault coverage analysis
- Dynamic power estimation
- Timing analysis
- Interactive visualization
- Automated engineering report

The project is designed as an educational ECE/VLSI
portfolio project.

---

## 🎯 Objectives

The main objectives are:

1. Model a basic SRAM architecture.
2. Implement memory read and write operations.
3. Simulate common memory fault models.
4. Apply March-style memory testing.
5. Calculate fault coverage.
6. Estimate dynamic power.
7. Estimate SRAM access timing.
8. Identify the critical timing path.
9. Visualize analysis results.
10. Generate an automated engineering report.

---

## 🏗️ SRAM Architecture

The project models a:

**16 × 8 SRAM**

This means:

- 16 memory locations
- 8 bits per location
- 4 address bits
- 128 total storage bits

Basic architecture:

```text
                Address
                   │
                   ▼
          ┌─────────────────┐
          │ Address Decoder │
          └────────┬────────┘
                   │
                   ▼
          ┌─────────────────┐
          │   SRAM Array    │
          │    16 × 8       │
          └────────┬────────┘
                   │
                   ▼
              Bit Lines
                   │
                   ▼
          ┌─────────────────┐
          │ Sense Amplifier │
          └────────┬────────┘
                   │
                   ▼
                Data Out
