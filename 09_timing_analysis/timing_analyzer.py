"""
VLSI SRAM Memory Analyzer
Stage 09: Timing Analysis

Educational SRAM timing model.

Estimates:
- Address decoder delay
- Word-line delay
- Bit-line RC delay
- Sense amplifier delay
- Read access time
- Write access time
- Critical path
- Maximum operating frequency

Note:
This is a simplified timing model and is not
intended for physical design sign-off.
"""

import csv


# ==========================================
# SRAM CONFIGURATION
# ==========================================

MEMORY_SIZE = 16
WORD_SIZE = 8

ADDRESS_BITS = 4


# ==========================================
# TECHNOLOGY PARAMETERS
# ==========================================

# Delay of one decoder logic level

GATE_DELAY_NS = 0.05


# Number of logic levels in decoder

DECODER_LEVELS = 2


# Word-line propagation delay

WORDLINE_DELAY_NS = 0.15


# Bit-line parameters

BITLINE_RESISTANCE_OHM = 2000

BITLINE_CAPACITANCE_F = 30e-15


# Sense amplifier delay

SENSE_AMPLIFIER_DELAY_NS = 0.08


# Write driver delay

WRITE_DRIVER_DELAY_NS = 0.05


# Timing safety margin

TIMING_MARGIN = 0.20


# ==========================================
# DECODER DELAY
# ==========================================

def calculate_decoder_delay():

    return (
        GATE_DELAY_NS
        * DECODER_LEVELS
    )


# ==========================================
# BIT-LINE RC DELAY
# ==========================================

def calculate_bitline_delay():

    resistance = (
        BITLINE_RESISTANCE_OHM
    )

    capacitance = (
        BITLINE_CAPACITANCE_F
    )

    # RC delay:
    #
    # t = 0.69 × R × C

    delay_seconds = (
        0.69
        * resistance
        * capacitance
    )

    delay_ns = (
        delay_seconds
        * 1e9
    )

    return delay_ns


# ==========================================
# READ ACCESS TIME
# ==========================================

def calculate_read_delay():

    decoder_delay = (
        calculate_decoder_delay()
    )

    bitline_delay = (
        calculate_bitline_delay()
    )


    read_delay = (

        decoder_delay

        + WORDLINE_DELAY_NS

        + bitline_delay

        + SENSE_AMPLIFIER_DELAY_NS
    )


    return read_delay


# ==========================================
# WRITE ACCESS TIME
# ==========================================

def calculate_write_delay():

    decoder_delay = (
        calculate_decoder_delay()
    )

    bitline_delay = (
        calculate_bitline_delay()
    )


    write_delay = (

        decoder_delay

        + WORDLINE_DELAY_NS

        + bitline_delay

        + WRITE_DRIVER_DELAY_NS
    )


    return write_delay


# ==========================================
# MAXIMUM FREQUENCY
# ==========================================

def calculate_max_frequency(
    critical_delay_ns
):

    # Apply timing margin

    required_cycle_time_ns = (
        critical_delay_ns
        * (1 + TIMING_MARGIN)
    )


    frequency_hz = (
        1
        / (
            required_cycle_time_ns
            * 1e-9
        )
    )


    return frequency_hz


# ==========================================
# TIMING STATUS
# ==========================================

def timing_status(
    frequency_mhz,
    target_frequency_mhz
):

    if frequency_mhz >= target_frequency_mhz:

        return "PASS"

    return "FAIL"


# ==========================================
# MAIN ANALYSIS
# ==========================================

if __name__ == "__main__":

    print("=" * 70)

    print(
        "       VLSI SRAM MEMORY ANALYZER"
    )

    print(
        "          STAGE 09"
    )

    print(
        "         TIMING ANALYSIS"
    )

    print("=" * 70)


    # --------------------------------------
    # Configuration
    # --------------------------------------

    print(
        "\nSRAM Configuration"
    )

    print(
        "-" * 50
    )

    print(
        f"Memory Size       : "
        f"{MEMORY_SIZE} × {WORD_SIZE}"
    )

    print(
        f"Address Bits      : "
        f"{ADDRESS_BITS}"
    )


    # --------------------------------------
    # Calculate delays
    # --------------------------------------

    decoder_delay = (
        calculate_decoder_delay()
    )

    bitline_delay = (
        calculate_bitline_delay()
    )

    read_delay = (
        calculate_read_delay()
    )

    write_delay = (
        calculate_write_delay()
    )


    # --------------------------------------
    # Critical path
    # --------------------------------------

    if read_delay >= write_delay:

        critical_operation = "READ"

        critical_delay = read_delay

    else:

        critical_operation = "WRITE"

        critical_delay = write_delay


    # --------------------------------------
    # Maximum frequency
    # --------------------------------------

    max_frequency_hz = (
        calculate_max_frequency(
            critical_delay
        )
    )

    max_frequency_mhz = (
        max_frequency_hz
        / 1e6
    )


    # --------------------------------------
    # Target frequency
    # --------------------------------------

    target_frequency_mhz = 1000


    status = timing_status(
        max_frequency_mhz,
        target_frequency_mhz
    )


    # ======================================
    # TIMING REPORT
    # ======================================

    print(
        "\nTiming Components"
    )

    print(
        "-" * 60
    )

    print(
        f"Decoder Delay      : "
        f"{decoder_delay:.4f} ns"
    )

    print(
        f"Word-Line Delay    : "
        f"{WORDLINE_DELAY_NS:.4f} ns"
    )

    print(
        f"Bit-Line RC Delay  : "
        f"{bitline_delay:.4f} ns"
    )

    print(
        f"Sense Amp Delay    : "
        f"{SENSE_AMPLIFIER_DELAY_NS:.4f} ns"
    )

    print(
        f"Write Driver Delay : "
        f"{WRITE_DRIVER_DELAY_NS:.4f} ns"
    )


    # ======================================
    # ACCESS TIMES
    # ======================================

    print(
        "\nAccess Time"
    )

    print(
        "-" * 60
    )

    print(
        f"Read Access Time   : "
        f"{read_delay:.4f} ns"
    )

    print(
        f"Write Access Time  : "
        f"{write_delay:.4f} ns"
    )


    # ======================================
    # CRITICAL PATH
    # ======================================

    print(
        "\nCritical Path"
    )

    print(
        "-" * 60
    )

    print(
        f"Critical Operation : "
        f"{critical_operation}"
    )

    print(
        f"Critical Delay     : "
        f"{critical_delay:.4f} ns"
    )

    print(
        f"Timing Margin      : "
        f"{TIMING_MARGIN * 100:.0f}%"
    )


    # ======================================
    # MAXIMUM FREQUENCY
    # ======================================

    print(
        "\nFrequency Analysis"
    )

    print(
        "-" * 60
    )

    print(
        f"Estimated Maximum Frequency : "
        f"{max_frequency_mhz:.2f} MHz"
    )

    print(
        f"Target Frequency            : "
        f"{target_frequency_mhz:.2f} MHz"
    )

    print(
        f"Timing Status               : "
        f"{status}"
    )


    # ======================================
    # TIMING FORMULA
    # ======================================

    print(
        "\nTiming Model"
    )

    print(
        "-" * 60
    )

    print(
        "Read Delay = Decoder + Wordline "
        "+ Bitline + Sense Amplifier"
    )

    print(
        "Write Delay = Decoder + Wordline "
        "+ Bitline + Write Driver"
    )

    print(
        "Bitline Delay = 0.69 × R × C"
    )


    # ======================================
    # ENGINEERING OBSERVATION
    # ======================================

    print(
        "\nEngineering Observation"
    )

    print(
        "-" * 60
    )

    if read_delay > write_delay:

        print(
            "READ operation is the critical path."
        )

        print(
            "Improving bit-line or sense-amplifier "
            "delay could improve read performance."
        )

    else:

        print(
            "WRITE operation is the critical path."
        )

        print(
            "Improving write-driver or bit-line "
            "delay could improve write performance."
        )


    # ======================================
    # SAVE TIMING DATA
    # ======================================

    output_file = (
        "timing_analysis.csv"
    )


    rows = [

        [
            "Parameter",
            "Value",
            "Unit"
        ],

        [
            "Decoder Delay",
            decoder_delay,
            "ns"
        ],

        [
            "Word-Line Delay",
            WORDLINE_DELAY_NS,
            "ns"
        ],

        [
            "Bit-Line RC Delay",
            bitline_delay,
            "ns"
        ],

        [
            "Sense Amplifier Delay",
            SENSE_AMPLIFIER_DELAY_NS,
            "ns"
        ],

        [
            "Write Driver Delay",
            WRITE_DRIVER_DELAY_NS,
            "ns"
        ],

        [
            "Read Access Time",
            read_delay,
            "ns"
        ],

        [
            "Write Access Time",
            write_delay,
            "ns"
        ],

        [
            "Critical Delay",
            critical_delay,
            "ns"
        ],

        [
            "Maximum Frequency",
            max_frequency_mhz,
            "MHz"
        ],

        [
            "Target Frequency",
            target_frequency_mhz,
            "MHz"
        ],

        [
            "Timing Status",
            status,
            "-"
        ]
    ]


    with open(
        output_file,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerows(rows)


    print(
        f"\nTiming data saved to: "
        f"{output_file}"
    )


    print(
        "\nStage 09 completed successfully."
    )
