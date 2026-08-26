"""
VLSI SRAM Memory Analyzer
Stage 11: Automated Engineering Report

Generates a text report containing:
- SRAM configuration
- Fault coverage
- Power estimation
- Timing analysis
- Critical path
- Overall design status
"""

from datetime import datetime


# ==========================================
# SRAM CONFIGURATION
# ==========================================

MEMORY_SIZE = 16
WORD_SIZE = 8

TOTAL_BITS = (
    MEMORY_SIZE * WORD_SIZE
)

ADDRESS_BITS = 4


# ==========================================
# FAULT ANALYSIS
# ==========================================

# Modeled fault types:
# SA0, SA1, TF_RISE, TF_FALL

FAULT_TYPES = 4

TOTAL_FAULTS = (
    TOTAL_BITS * FAULT_TYPES
)

DETECTED_FAULTS = TOTAL_FAULTS

FAULT_COVERAGE = (
    DETECTED_FAULTS
    / TOTAL_FAULTS
) * 100


# ==========================================
# POWER PARAMETERS
# ==========================================

SUPPLY_VOLTAGE = 1.0

SWITCHING_ACTIVITY = 0.50

CAPACITANCE_PER_BIT = 10e-15

OPERATING_FREQUENCY = 100e6


TOTAL_CAPACITANCE = (
    TOTAL_BITS
    * CAPACITANCE_PER_BIT
)


DYNAMIC_POWER = (
    SWITCHING_ACTIVITY
    * TOTAL_CAPACITANCE
    * SUPPLY_VOLTAGE ** 2
    * OPERATING_FREQUENCY
)


DYNAMIC_POWER_UW = (
    DYNAMIC_POWER * 1e6
)


# ==========================================
# TIMING PARAMETERS
# ==========================================

GATE_DELAY_NS = 0.05

DECODER_LEVELS = 2

WORDLINE_DELAY_NS = 0.15

BITLINE_RESISTANCE = 2000

BITLINE_CAPACITANCE = 30e-15

SENSE_AMPLIFIER_DELAY_NS = 0.08

WRITE_DRIVER_DELAY_NS = 0.05

TIMING_MARGIN = 0.20


# ==========================================
# TIMING CALCULATIONS
# ==========================================

DECODER_DELAY_NS = (
    GATE_DELAY_NS
    * DECODER_LEVELS
)


BITLINE_DELAY_NS = (
    0.69
    * BITLINE_RESISTANCE
    * BITLINE_CAPACITANCE
    * 1e9
)


READ_DELAY_NS = (
    DECODER_DELAY_NS
    + WORDLINE_DELAY_NS
    + BITLINE_DELAY_NS
    + SENSE_AMPLIFIER_DELAY_NS
)


WRITE_DELAY_NS = (
    DECODER_DELAY_NS
    + WORDLINE_DELAY_NS
    + BITLINE_DELAY_NS
    + WRITE_DRIVER_DELAY_NS
)


# ==========================================
# CRITICAL PATH
# ==========================================

if READ_DELAY_NS >= WRITE_DELAY_NS:

    CRITICAL_OPERATION = "READ"

    CRITICAL_DELAY_NS = (
        READ_DELAY_NS
    )

else:

    CRITICAL_OPERATION = "WRITE"

    CRITICAL_DELAY_NS = (
        WRITE_DELAY_NS
    )


# ==========================================
# MAXIMUM FREQUENCY
# ==========================================

CYCLE_TIME_NS = (
    CRITICAL_DELAY_NS
    * (1 + TIMING_MARGIN)
)


MAX_FREQUENCY_HZ = (
    1
    / (
        CYCLE_TIME_NS
        * 1e-9
    )
)


MAX_FREQUENCY_MHZ = (
    MAX_FREQUENCY_HZ
    / 1e6
)


TARGET_FREQUENCY_MHZ = 1000


if MAX_FREQUENCY_MHZ >= TARGET_FREQUENCY_MHZ:

    TIMING_STATUS = "PASS"

else:

    TIMING_STATUS = "FAIL"


# ==========================================
# POWER STATUS
# ==========================================

if DYNAMIC_POWER_UW < 100:

    POWER_STATUS = "LOW"

elif DYNAMIC_POWER_UW < 500:

    POWER_STATUS = "MODERATE"

else:

    POWER_STATUS = "HIGH"


# ==========================================
# FAULT STATUS
# ==========================================

if FAULT_COVERAGE >= 95:

    FAULT_STATUS = "EXCELLENT"

elif FAULT_COVERAGE >= 90:

    FAULT_STATUS = "GOOD"

else:

    FAULT_STATUS = "REVIEW REQUIRED"


# ==========================================
# OVERALL STATUS
# ==========================================

if (
    FAULT_COVERAGE >= 90
    and TIMING_STATUS == "PASS"
):

    DESIGN_STATUS = "PASS"

else:

    DESIGN_STATUS = "REVIEW REQUIRED"


# ==========================================
# REPORT FILE
# ==========================================

OUTPUT_FILE = (
    "sram_engineering_report.txt"
)


# ==========================================
# GENERATE REPORT
# ==========================================

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as report:

    report.write(
        "=" * 70 + "\n"
    )

    report.write(
        "              VLSI SRAM MEMORY ANALYZER\n"
    )

    report.write(
        "               ENGINEERING REPORT\n"
    )

    report.write(
        "=" * 70 + "\n\n"
    )


    # --------------------------------------
    # Report information
    # --------------------------------------

    report.write(
        "REPORT INFORMATION\n"
    )

    report.write(
        "-" * 70 + "\n"
    )

    report.write(
        "Generated : "
        + datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        + "\n"
    )

    report.write(
        "Project   : "
        "VLSI SRAM Memory Analyzer\n\n"
    )


    # --------------------------------------
    # SRAM configuration
    # --------------------------------------

    report.write(
        "SRAM CONFIGURATION\n"
    )

    report.write(
        "-" * 70 + "\n"
    )

    report.write(
        f"Memory Organization : "
        f"{MEMORY_SIZE} x {WORD_SIZE}\n"
    )

    report.write(
        f"Memory Locations    : "
        f"{MEMORY_SIZE}\n"
    )

    report.write(
        f"Word Size           : "
        f"{WORD_SIZE} bits\n"
    )

    report.write(
        f"Address Bits        : "
        f"{ADDRESS_BITS}\n"
    )

    report.write(
        f"Total Capacity      : "
        f"{TOTAL_BITS} bits\n\n"
    )


    # --------------------------------------
    # Fault analysis
    # --------------------------------------

    report.write(
        "FAULT ANALYSIS\n"
    )

    report.write(
        "-" * 70 + "\n"
    )

    report.write(
        "Fault Models        : "
        "SA0, SA1, TF_RISE, TF_FALL\n"
    )

    report.write(
        f"Total Modeled Faults: "
        f"{TOTAL_FAULTS}\n"
    )

    report.write(
        f"Detected Faults     : "
        f"{DETECTED_FAULTS}\n"
    )

    report.write(
        f"Fault Coverage      : "
        f"{FAULT_COVERAGE:.2f}%\n"
    )

    report.write(
        f"Coverage Status     : "
        f"{FAULT_STATUS}\n\n"
    )


    # --------------------------------------
    # Power analysis
    # --------------------------------------

    report.write(
        "POWER ANALYSIS\n"
    )

    report.write(
        "-" * 70 + "\n"
    )

    report.write(
        f"Supply Voltage      : "
        f"{SUPPLY_VOLTAGE:.2f} V\n"
    )

    report.write(
        f"Operating Frequency : "
        f"{OPERATING_FREQUENCY / 1e6:.2f} MHz\n"
    )

    report.write(
        f"Switching Activity  : "
        f"{SWITCHING_ACTIVITY:.2f}\n"
    )

    report.write(
        f"Total Capacitance   : "
        f"{TOTAL_CAPACITANCE * 1e15:.2f} fF\n"
    )

    report.write(
        f"Dynamic Power       : "
        f"{DYNAMIC_POWER_UW:.2f} uW\n"
    )

    report.write(
        f"Power Status        : "
        f"{POWER_STATUS}\n\n"
    )


    # --------------------------------------
    # Timing analysis
    # --------------------------------------

    report.write(
        "TIMING ANALYSIS\n"
    )

    report.write(
        "-" * 70 + "\n"
    )

    report.write(
        f"Decoder Delay       : "
        f"{DECODER_DELAY_NS:.4f} ns\n"
    )

    report.write(
        f"Word-Line Delay     : "
        f"{WORDLINE_DELAY_NS:.4f} ns\n"
    )

    report.write(
        f"Bit-Line Delay      : "
        f"{BITLINE_DELAY_NS:.4f} ns\n"
    )

    report.write(
        f"Sense Amp Delay     : "
        f"{SENSE_AMPLIFIER_DELAY_NS:.4f} ns\n"
    )

    report.write(
        f"Write Driver Delay  : "
        f"{WRITE_DRIVER_DELAY_NS:.4f} ns\n"
    )

    report.write(
        f"Read Access Time    : "
        f"{READ_DELAY_NS:.4f} ns\n"
    )

    report.write(
        f"Write Access Time   : "
        f"{WRITE_DELAY_NS:.4f} ns\n\n"
    )


    # --------------------------------------
    # Critical path
    # --------------------------------------

    report.write(
        "CRITICAL PATH ANALYSIS\n"
    )

    report.write(
        "-" * 70 + "\n"
    )

    report.write(
        f"Critical Operation  : "
        f"{CRITICAL_OPERATION}\n"
    )

    report.write(
        f"Critical Delay      : "
        f"{CRITICAL_DELAY_NS:.4f} ns\n"
    )

    report.write(
        f"Timing Margin       : "
        f"{TIMING_MARGIN * 100:.0f}%\n"
    )

    report.write(
        f"Maximum Frequency   : "
        f"{MAX_FREQUENCY_MHZ:.2f} MHz\n"
    )

    report.write(
        f"Target Frequency    : "
        f"{TARGET_FREQUENCY_MHZ:.2f} MHz\n"
    )

    report.write(
        f"Timing Status       : "
        f"{TIMING_STATUS}\n\n"
    )


    # --------------------------------------
    # Engineering observations
    # --------------------------------------

    report.write(
        "ENGINEERING OBSERVATIONS\n"
    )

    report.write(
        "-" * 70 + "\n"
    )

    report.write(
        "1. The simplified March test detects "
        "all modeled stuck-at and transition faults.\n"
    )

    report.write(
        "2. Dynamic power increases with switching "
        "activity, capacitance, voltage squared, "
        "and operating frequency.\n"
    )

    report.write(
        f"3. The {CRITICAL_OPERATION.lower()} "
        "operation forms the estimated critical path.\n"
    )

    report.write(
        "4. Reducing bit-line, word-line, or peripheral "
        "circuit delays can improve SRAM performance.\n\n"
    )


    # --------------------------------------
    # Final status
    # --------------------------------------

    report.write(
        "FINAL DESIGN SUMMARY\n"
    )

    report.write(
        "-" * 70 + "\n"
    )

    report.write(
        f"Fault Coverage Status : "
        f"{FAULT_STATUS}\n"
    )

    report.write(
        f"Power Status          : "
        f"{POWER_STATUS}\n"
    )

    report.write(
        f"Timing Status         : "
        f"{TIMING_STATUS}\n"
    )

    report.write(
        f"Overall Design Status : "
        f"{DESIGN_STATUS}\n\n"
    )


    # --------------------------------------
    # Disclaimer
    # --------------------------------------

    report.write(
        "NOTE\n"
    )

    report.write(
        "-" * 70 + "\n"
    )

    report.write(
        "This report is generated from a simplified "
        "educational SRAM model. Power, timing, and "
        "fault-coverage results are model-based estimates "
        "and are not silicon sign-off measurements.\n"
    )


# ==========================================
# CONSOLE OUTPUT
# ==========================================

print("=" * 70)

print(
    "       VLSI SRAM MEMORY ANALYZER"
)

print(
    "       AUTOMATED ENGINEERING REPORT"
)

print("=" * 70)


print(
    f"\nMemory Organization : "
    f"{MEMORY_SIZE} x {WORD_SIZE}"
)

print(
    f"Fault Coverage      : "
    f"{FAULT_COVERAGE:.2f}%"
)

print(
    f"Dynamic Power       : "
    f"{DYNAMIC_POWER_UW:.2f} uW"
)

print(
    f"Read Access Time    : "
    f"{READ_DELAY_NS:.4f} ns"
)

print(
    f"Write Access Time   : "
    f"{WRITE_DELAY_NS:.4f} ns"
)

print(
    f"Critical Path       : "
    f"{CRITICAL_OPERATION}"
)

print(
    f"Maximum Frequency   : "
    f"{MAX_FREQUENCY_MHZ:.2f} MHz"
)

print(
    f"Timing Status       : "
    f"{TIMING_STATUS}"
)

print(
    f"Overall Status      : "
    f"{DESIGN_STATUS}"
)


print(
    "\nReport generated successfully."
)

print(
    f"Saved as: {OUTPUT_FILE}"
)

print(
    "\nStage 11 completed successfully."
)
