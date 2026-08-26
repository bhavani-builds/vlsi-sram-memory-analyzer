"""
VLSI SRAM Memory Analyzer
Stage 08: Power Estimation

Estimates CMOS dynamic power using:

P = alpha * C * V^2 * f

This is an educational estimation model.
"""


# ==========================================
# SRAM CONFIGURATION
# ==========================================

MEMORY_SIZE = 16
WORD_SIZE = 8

TOTAL_BITS = (
    MEMORY_SIZE * WORD_SIZE
)


# ==========================================
# TECHNOLOGY PARAMETERS
# ==========================================

SUPPLY_VOLTAGE = 1.0       # Volts

CAPACITANCE_PER_BIT = 10e-15
# 10 femtofarads per bit

OPERATING_FREQUENCY = 100e6
# 100 MHz


# ==========================================
# DYNAMIC POWER FUNCTION
# ==========================================

def calculate_dynamic_power(
    switching_activity,
    capacitance,
    voltage,
    frequency
):
    """
    Calculate dynamic CMOS power.

    P = alpha * C * V^2 * f
    """

    power = (
        switching_activity
        * capacitance
        * voltage ** 2
        * frequency
    )

    return power


# ==========================================
# TOTAL SRAM CAPACITANCE
# ==========================================

total_capacitance = (
    TOTAL_BITS
    * CAPACITANCE_PER_BIT
)


# ==========================================
# POWER FOR DIFFERENT ACTIVITY LEVELS
# ==========================================

activity_levels = {

    "Low Activity": 0.10,

    "Medium Activity": 0.50,

    "High Activity": 0.90
}


# ==========================================
# DISPLAY PARAMETERS
# ==========================================

print("=" * 65)

print(
    "       VLSI SRAM MEMORY ANALYZER"
)

print(
    "          STAGE 08"
)

print(
    "        POWER ESTIMATION"
)

print("=" * 65)


print(
    "\nSRAM Configuration"
)

print(
    "-" * 45
)

print(
    f"Memory Size          : "
    f"{MEMORY_SIZE} × {WORD_SIZE}"
)

print(
    f"Total Memory Bits    : "
    f"{TOTAL_BITS}"
)

print(
    f"Supply Voltage       : "
    f"{SUPPLY_VOLTAGE:.2f} V"
)

print(
    f"Capacitance / Bit    : "
    f"{CAPACITANCE_PER_BIT * 1e15:.2f} fF"
)

print(
    f"Total Capacitance    : "
    f"{total_capacitance * 1e15:.2f} fF"
)

print(
    f"Operating Frequency  : "
    f"{OPERATING_FREQUENCY / 1e6:.2f} MHz"
)


# ==========================================
# CALCULATE POWER
# ==========================================

print(
    "\nDynamic Power Estimation"
)

print(
    "-" * 65
)

print(
    f"{'Activity':<20}"
    f"{'Alpha':<12}"
    f"{'Power':<15}"
    f"{'Power (uW)':<15}"
)

print(
    "-" * 65
)


power_results = []


for activity_name, alpha in (
    activity_levels.items()
):

    power = calculate_dynamic_power(
        alpha,
        total_capacitance,
        SUPPLY_VOLTAGE,
        OPERATING_FREQUENCY
    )


    power_microwatts = (
        power * 1e6
    )


    print(
        f"{activity_name:<20}"
        f"{alpha:<12.2f}"
        f"{power:<15.6e}"
        f"{power_microwatts:<15.4f}"
    )


    power_results.append({

        "activity": activity_name,

        "alpha": alpha,

        "power_watts": power,

        "power_microwatts":
            power_microwatts
    })


# ==========================================
# POWER COMPARISON
# ==========================================

low_power = power_results[0][
    "power_watts"
]

medium_power = power_results[1][
    "power_watts"
]

high_power = power_results[2][
    "power_watts"
]


print(
    "\nPower Comparison"
)

print(
    "-" * 45
)

print(
    f"Low Activity    : "
    f"{low_power * 1e6:.4f} µW"
)

print(
    f"Medium Activity : "
    f"{medium_power * 1e6:.4f} µW"
)

print(
    f"High Activity   : "
    f"{high_power * 1e6:.4f} µW"
)


# ==========================================
# POWER INCREASE
# ==========================================

increase = (
    high_power
    / low_power
)


print(
    "\nHigh/Low Power Ratio"
)

print(
    "-" * 45
)

print(
    f"High activity consumes "
    f"{increase:.1f}× the low-activity "
    f"dynamic power."
)


# ==========================================
# ENGINEERING OBSERVATION
# ==========================================

print(
    "\nEngineering Observation"
)

print(
    "-" * 45
)

print(
    "Higher switching activity increases "
    "dynamic power consumption."
)

print(
    "Reducing unnecessary switching can "
    "help reduce dynamic power."
)


# ==========================================
# POWER STATUS
# ==========================================

if high_power < 1e-3:

    print(
        "\nPower Estimate: "
        "LOW for this educational model."
    )

else:

    print(
        "\nPower Estimate: "
        "HIGH for this educational model."
    )


print(
    "\nStage 08 completed successfully."
)
