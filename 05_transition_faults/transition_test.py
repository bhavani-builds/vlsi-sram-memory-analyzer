"""
VLSI SRAM Memory Analyzer
Stage 05: Transition Fault Testing

Simulates 0->1 and 1->0 transition faults
in SRAM memory cells.
"""

# ------------------------------------------
# SRAM Configuration
# ------------------------------------------

MEMORY_SIZE = 16
WORD_SIZE = 8


# ------------------------------------------
# Fault Configuration
# ------------------------------------------

fault_address = 5
fault_bit = 3

# Possible values:
# NONE
# RISE_FAULT  -> 0 to 1 transition fails
# FALL_FAULT  -> 1 to 0 transition fails

fault_type = "RISE_FAULT"


# ------------------------------------------
# SRAM Memory
# ------------------------------------------

memory = [
    "00000000"
    for _ in range(MEMORY_SIZE)
]


# ------------------------------------------
# Write Operation
# ------------------------------------------

def write_memory(address, data):

    if not 0 <= address < MEMORY_SIZE:
        raise ValueError(
            "Invalid SRAM address."
        )

    if len(data) != WORD_SIZE:
        raise ValueError(
            "Data must contain 8 bits."
        )

    if any(bit not in "01" for bit in data):
        raise ValueError(
            "Data must contain only 0 and 1."
        )

    previous_data = memory[address]

    new_data = list(data)

    # --------------------------------------
    # Apply transition fault
    # --------------------------------------

    if address == fault_address:

        previous_bit = previous_data[fault_bit]
        requested_bit = data[fault_bit]

        # 0 -> 1 transition fault
        if (
            fault_type == "RISE_FAULT"
            and previous_bit == "0"
            and requested_bit == "1"
        ):

            new_data[fault_bit] = "0"


        # 1 -> 0 transition fault
        elif (
            fault_type == "FALL_FAULT"
            and previous_bit == "1"
            and requested_bit == "0"
        ):

            new_data[fault_bit] = "1"


    memory[address] = "".join(new_data)


# ------------------------------------------
# Read Operation
# ------------------------------------------

def read_memory(address):

    if not 0 <= address < MEMORY_SIZE:
        raise ValueError(
            "Invalid SRAM address."
        )

    return memory[address]


# ------------------------------------------
# Reset Memory
# ------------------------------------------

def reset_memory():

    for address in range(MEMORY_SIZE):

        memory[address] = "00000000"


# ------------------------------------------
# Test 0 -> 1 Transition
# ------------------------------------------

def test_rise_transition():

    global fault_type

    fault_type = "RISE_FAULT"

    reset_memory()

    print("\n0 -> 1 Transition Test")
    print("-" * 65)

    # First write all zeros
    write_memory(
        fault_address,
        "00000000"
    )

    # Try to change bit 3 from 0 to 1
    write_memory(
        fault_address,
        "00001000"
    )

    actual_data = read_memory(
        fault_address
    )

    expected_bit = "1"
    actual_bit = actual_data[fault_bit]

    print(
        f"Address       : {fault_address}"
    )

    print(
        f"Fault Bit     : {fault_bit}"
    )

    print(
        f"Expected Bit  : {expected_bit}"
    )

    print(
        f"Actual Bit    : {actual_bit}"
    )


    if actual_bit != expected_bit:

        print(
            "\n🚨 0 -> 1 TRANSITION FAULT DETECTED"
        )

        return True

    print(
        "\n✅ 0 -> 1 transition passed"
    )

    return False


# ------------------------------------------
# Test 1 -> 0 Transition
# ------------------------------------------

def test_fall_transition():

    global fault_type

    fault_type = "FALL_FAULT"

    reset_memory()

    print("\n1 -> 0 Transition Test")
    print("-" * 65)

    # First write 1
    write_memory(
        fault_address,
        "00001000"
    )

    # Try to change bit 3 from 1 to 0
    write_memory(
        fault_address,
        "00000000"
    )

    actual_data = read_memory(
        fault_address
    )

    expected_bit = "0"
    actual_bit = actual_data[fault_bit]

    print(
        f"Address       : {fault_address}"
    )

    print(
        f"Fault Bit     : {fault_bit}"
    )

    print(
        f"Expected Bit  : {expected_bit}"
    )

    print(
        f"Actual Bit    : {actual_bit}"
    )


    if actual_bit != expected_bit:

        print(
            "\n🚨 1 -> 0 TRANSITION FAULT DETECTED"
        )

        return True

    print(
        "\n✅ 1 -> 0 transition passed"
    )

    return False


# ------------------------------------------
# Main
# ------------------------------------------

if __name__ == "__main__":

    print("=" * 65)

    print(
        "       VLSI SRAM MEMORY ANALYZER"
    )

    print(
        "          STAGE 05"
    )

    print(
        "       TRANSITION FAULT TEST"
    )

    print("=" * 65)


    rise_detected = (
        test_rise_transition()
    )

    fall_detected = (
        test_fall_transition()
    )


    print(
        "\nTransition Fault Summary"
    )

    print(
        "-" * 45
    )

    print(
        f"0 -> 1 Fault : "
        f"{'DETECTED' if rise_detected else 'NOT DETECTED'}"
    )

    print(
        f"1 -> 0 Fault : "
        f"{'DETECTED' if fall_detected else 'NOT DETECTED'}"
    )


    detected = (
        int(rise_detected)
        + int(fall_detected)
    )


    print(
        f"\nDetected Faults : {detected}/2"
    )


    if detected == 2:

        print(
            "PASS: Both transition faults detected."
        )

    else:

        print(
            "FAIL: One or more transition faults "
            "were not detected."
        )


    print(
        "\nStage 05 completed successfully."
    )
