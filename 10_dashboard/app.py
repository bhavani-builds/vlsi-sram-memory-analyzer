"""
VLSI SRAM Memory Analyzer
Stage 10: Interactive Dashboard

Combines:

- SRAM architecture
- Fault coverage
- Dynamic power estimation
- Timing analysis
"""

import numpy as np
import pandas as pd
import streamlit as st


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="VLSI SRAM Analyzer",
    page_icon="💾",
    layout="wide"
)


# ==========================================
# TITLE
# ==========================================

st.title(
    "💾 VLSI SRAM Memory Analyzer"
)

st.subheader(
    "SRAM Testing • Power • Timing • Fault Analysis"
)

st.write(
    "Educational VLSI memory-analysis dashboard "
    "for a 16 × 8 SRAM architecture."
)

st.divider()


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.header(
    "⚙️ SRAM Configuration"
)


memory_size = st.sidebar.number_input(
    "Memory Locations",
    min_value=1,
    max_value=1024,
    value=16,
    step=1
)


word_size = st.sidebar.number_input(
    "Word Size (bits)",
    min_value=1,
    max_value=64,
    value=8,
    step=1
)


supply_voltage = st.sidebar.slider(
    "Supply Voltage (V)",
    min_value=0.5,
    max_value=2.0,
    value=1.0,
    step=0.1
)


frequency_mhz = st.sidebar.slider(
    "Operating Frequency (MHz)",
    min_value=10,
    max_value=3000,
    value=100,
    step=10
)


switching_activity = st.sidebar.slider(
    "Switching Activity",
    min_value=0.0,
    max_value=1.0,
    value=0.5,
    step=0.05
)


target_frequency_mhz = st.sidebar.slider(
    "Target Frequency (MHz)",
    min_value=10,
    max_value=3000,
    value=1000,
    step=10
)


# ==========================================
# SRAM PARAMETERS
# ==========================================

total_bits = (
    memory_size * word_size
)

address_bits = int(
    np.ceil(
        np.log2(memory_size)
    )
)


# ==========================================
# FAULT COVERAGE MODEL
# ==========================================

# Four modeled fault types:
#
# SA0
# SA1
# TF_RISE
# TF_FALL

total_faults = (
    total_bits * 4
)


# Our simplified March test detects
# all four modeled fault classes.

detected_faults = total_faults


fault_coverage = (
    detected_faults
    / total_faults
) * 100


# ==========================================
# POWER MODEL
# ==========================================

capacitance_per_bit = 10e-15

total_capacitance = (
    total_bits
    * capacitance_per_bit
)


frequency_hz = (
    frequency_mhz * 1e6
)


dynamic_power = (
    switching_activity
    * total_capacitance
    * supply_voltage ** 2
    * frequency_hz
)


dynamic_power_microwatts = (
    dynamic_power * 1e6
)


# ==========================================
# TIMING MODEL
# ==========================================

gate_delay_ns = 0.05

decoder_levels = 2

decoder_delay_ns = (
    gate_delay_ns
    * decoder_levels
)


wordline_delay_ns = 0.15

bitline_resistance = 2000

bitline_capacitance = 30e-15


bitline_delay_ns = (
    0.69
    * bitline_resistance
    * bitline_capacitance
    * 1e9
)


sense_amplifier_delay_ns = 0.08

write_driver_delay_ns = 0.05


read_access_time_ns = (
    decoder_delay_ns
    + wordline_delay_ns
    + bitline_delay_ns
    + sense_amplifier_delay_ns
)


write_access_time_ns = (
    decoder_delay_ns
    + wordline_delay_ns
    + bitline_delay_ns
    + write_driver_delay_ns
)


# Read is the critical path if it is slower.

critical_delay_ns = max(
    read_access_time_ns,
    write_access_time_ns
)


critical_operation = (
    "READ"
    if read_access_time_ns >= write_access_time_ns
    else "WRITE"
)


timing_margin = 0.20


maximum_frequency_hz = (
    1
    / (
        critical_delay_ns
        * (1 + timing_margin)
        * 1e-9
    )
)


maximum_frequency_mhz = (
    maximum_frequency_hz
    / 1e6
)


# ==========================================
# TIMING STATUS
# ==========================================

if (
    maximum_frequency_mhz
    >= target_frequency_mhz
):

    timing_status = "PASS"

else:

    timing_status = "FAIL"


# ==========================================
# TOP METRICS
# ==========================================

st.header(
    "📊 SRAM Overview"
)


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Memory Capacity",
        f"{total_bits} bits"
    )


with col2:

    st.metric(
        "Fault Coverage",
        f"{fault_coverage:.1f}%"
    )


with col3:

    st.metric(
        "Dynamic Power",
        f"{dynamic_power_microwatts:.2f} µW"
    )


with col4:

    st.metric(
        "Max Frequency",
        f"{maximum_frequency_mhz:.1f} MHz"
    )


# ==========================================
# MEMORY ARCHITECTURE
# ==========================================

st.divider()

st.header(
    "🧠 SRAM Architecture"
)


architecture_col1, architecture_col2 = (
    st.columns(2)
)


with architecture_col1:

    st.write(
        f"**Memory Organization:** "
        f"{memory_size} × {word_size}"
    )

    st.write(
        f"**Address Bits:** "
        f"{address_bits}"
    )

    st.write(
        f"**Total Storage:** "
        f"{total_bits} bits"
    )


with architecture_col2:

    st.code(
        f"""
Address
   ↓
Address Decoder
   ↓
Word Line
   ↓
SRAM Cell Array
   ↓
Bit Line
   ↓
Sense Amplifier
   ↓
Data Output
        """,
        language="text"
    )


# ==========================================
# FAULT ANALYSIS
# ==========================================

st.divider()

st.header(
    "🧪 Fault Analysis"
)


fault_data = pd.DataFrame({

    "Fault Type": [

        "Stuck-at-0",

        "Stuck-at-1",

        "Transition 0→1",

        "Transition 1→0"

    ],

    "Total Faults": [

        total_bits,

        total_bits,

        total_bits,

        total_bits

    ],

    "Detected": [

        total_bits,

        total_bits,

        total_bits,

        total_bits

    ],

    "Coverage (%)": [

        100,

        100,

        100,

        100

    ]

})


st.dataframe(
    fault_data,
    width="stretch",
    hide_index=True
)


st.success(
    f"✅ Overall modeled fault coverage: "
    f"{fault_coverage:.2f}%"
)


# ==========================================
# POWER ANALYSIS
# ==========================================

st.divider()

st.header(
    "⚡ Dynamic Power Analysis"
)


power_col1, power_col2 = (
    st.columns(2)
)


with power_col1:

    st.metric(
        "Supply Voltage",
        f"{supply_voltage:.2f} V"
    )

    st.metric(
        "Switching Activity",
        f"{switching_activity:.2f}"
    )

    st.metric(
        "Operating Frequency",
        f"{frequency_mhz} MHz"
    )


with power_col2:

    st.metric(
        "Total Capacitance",
        f"{total_capacitance * 1e15:.2f} fF"
    )

    st.metric(
        "Dynamic Power",
        f"{dynamic_power_microwatts:.2f} µW"
    )


st.latex(
    r"P_{dynamic} = \alpha C V^2 f"
)


# ==========================================
# POWER ACTIVITY GRAPH
# ==========================================

activity_values = np.linspace(
    0.05,
    1.0,
    20
)


power_values = []

for activity in activity_values:

    power = (
        activity
        * total_capacitance
        * supply_voltage ** 2
        * frequency_hz
    )

    power_values.append(
        power * 1e6
    )


power_dataframe = pd.DataFrame({

    "Switching Activity":
        activity_values,

    "Dynamic Power (µW)":
        power_values

})


st.line_chart(
    power_dataframe,
    x="Switching Activity",
    y="Dynamic Power (µW)"
)


# ==========================================
# TIMING ANALYSIS
# ==========================================

st.divider()

st.header(
    "⏱️ Timing Analysis"
)


timing_col1, timing_col2, timing_col3 = (
    st.columns(3)
)


with timing_col1:

    st.metric(
        "Read Access Time",
        f"{read_access_time_ns:.4f} ns"
    )


with timing_col2:

    st.metric(
        "Write Access Time",
        f"{write_access_time_ns:.4f} ns"
    )


with timing_col3:

    st.metric(
        "Critical Path",
        critical_operation
    )


timing_data = pd.DataFrame({

    "Timing Component": [

        "Decoder",

        "Word Line",

        "Bit Line",

        "Sense Amplifier",

        "Write Driver"

    ],

    "Delay (ns)": [

        decoder_delay_ns,

        wordline_delay_ns,

        bitline_delay_ns,

        sense_amplifier_delay_ns,

        write_driver_delay_ns

    ]

})


st.bar_chart(
    timing_data,
    x="Timing Component",
    y="Delay (ns)"
)


st.write(
    f"**Critical Delay:** "
    f"{critical_delay_ns:.4f} ns"
)


st.write(
    f"**Estimated Maximum Frequency:** "
    f"{maximum_frequency_mhz:.2f} MHz"
)


if timing_status == "PASS":

    st.success(
        f"🟢 Timing PASS — target "
        f"{target_frequency_mhz} MHz is supported."
    )

else:

    st.error(
        f"🔴 Timing FAIL — target "
        f"{target_frequency_mhz} MHz exceeds "
        f"the estimated limit."
    )


# ==========================================
# DESIGN HEALTH
# ==========================================

st.divider()

st.header(
    "🎯 SRAM Design Health"
)


health_col1, health_col2, health_col3 = (
    st.columns(3)
)


with health_col1:

    if fault_coverage >= 90:

        st.success(
            "🟢 FAULT COVERAGE: GOOD"
        )

    else:

        st.warning(
            "🟡 FAULT COVERAGE: REVIEW"
        )


with health_col2:

    if dynamic_power_microwatts < 100:

        st.success(
            "🟢 POWER: LOW"
        )

    else:

        st.warning(
            "🟡 POWER: HIGH"
        )


with health_col3:

    if timing_status == "PASS":

        st.success(
            "🟢 TIMING: PASS"
        )

    else:

        st.error(
            "🔴 TIMING: FAIL"
        )


# ==========================================
# ENGINEERING SUMMARY
# ==========================================

st.divider()

st.header(
    "📋 Engineering Summary"
)


summary_data = pd.DataFrame({

    "Parameter": [

        "Memory Organization",

        "Total Capacity",

        "Fault Coverage",

        "Dynamic Power",

        "Read Access Time",

        "Write Access Time",

        "Critical Operation",

        "Maximum Frequency",

        "Target Frequency",

        "Timing Status"

    ],

    "Value": [

        f"{memory_size} × {word_size}",

        f"{total_bits} bits",

        f"{fault_coverage:.2f}%",

        f"{dynamic_power_microwatts:.2f} µW",

        f"{read_access_time_ns:.4f} ns",

        f"{write_access_time_ns:.4f} ns",

        critical_operation,

        f"{maximum_frequency_mhz:.2f} MHz",

        f"{target_frequency_mhz} MHz",

        timing_status

    ]

})


st.dataframe(
    summary_data,
    width="stretch",
    hide_index=True
)


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "VLSI SRAM Memory Analyzer | "
    "Educational ECE/VLSI Portfolio Project"
)

st.caption(
    "Power and timing values are simplified "
    "architectural estimates, not silicon "
    "sign-off results."
)
