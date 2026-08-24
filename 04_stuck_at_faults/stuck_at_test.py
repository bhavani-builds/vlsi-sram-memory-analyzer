"""
VLSI SRAM Memory Analyzer
Stage 04: Stuck-at Fault Injection

Simulates stuck-at-0 and stuck-at-1
faults in SRAM memory cells.
"""


# ------------------------------------------
# SRAM Configuration
# ------------------------------------------

MEMORY_SIZE = 16
WORD_SIZE = 8


# ------------------------------------------
# SRAM Memory
# ------------------------------------------

memory = [
    "00000000"
    for _ in range(MEMORY_SIZE)
]


# ------------------------------------------
# Fault Configuration
# ------------------------------------------

fault_address = 5
fault_bit = 3

fault_type = "SA0"


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

    memory[address] = data


# ------------------------------------------
# Apply Stuck-at Fault
# ------------------------------------------

def apply_stuck_at_fault(data):

    bits = list(data)

    if fault_type == "SA0":

        bits[fault_bit] = "0"

    elif fault_type == "SA1":

        bits[fault_bit] = "1"

    else:

        raise ValueError(
            "Fault type must be SA0 or SA1."
        )

    return "".join(bits)


# ------------------------------------------
# Read Operation
# ------------------------------------------

def read_memory(address):

    if not 0 <= address < MEMORY_SIZE:
        raise ValueError(
            "Invalid SRAM address."
        )

    normal_data = memory[address]

    # Apply fault only at selected address

    if address == fault_address:

        return apply_stuck_at_fault(
            normal_data
        )

    return normal_data


# ------------------------------------------
# Fault Detection Test
# ------------------------------------------

def test_fault():

    print("\nFault Detection Test")
    print("-" * 70)

    test_data = "11111111"

    write_memory(
        fault_address,
        test_data
    )

    actual_data = read_memory(
        fault_address
    )

    print(
        f"Fault Address : "
        f"{fault_address}"
    )

    print(
        f"Fault Bit     : "
        f"{fault_bit}"
    )

    print(
        f"Fault Type    : "
        f"{fault_type}"
    )

    print(
        f"Expected Data : "
        f"{test_data}"
    )

    print(
        f"Actual Data   : "
        f"{actual_data}"
    )


    if actual_data != test_data:

        print(
            "\n🚨 FAULT DETECTED"
        )

        return True

    print(
        "\n✅ NO FAULT DETECTED"
    )

    return False


# ------------------------------------------
# Test Both Fault Types
# ------------------------------------------

def run_fault_tests():

    global fault_type

    results = []


    # Test stuck-at-0

    fault_type = "SA0"

    detected = test_fault()

    results.append(
        ("SA0", detected)
    )


    # Test stuck-at-1

    fault_type = "SA1"

    detected = test_fault()

    results.append(
        ("SA1", detected)
    )


    return results


# ------------------------------------------
# Main
# ------------------------------------------

if __name__ == "__main__":

    print("=" * 60)

    print(
        "       VLSI SRAM MEMORY ANALYZER"
    )

    print(
        "          STAGE 04"
    )

    print(
        "        STUCK-AT FAULT TEST"
    )

    print("=" * 60)


    results = run_fault_tests()


    print(
        "\nFault Test Summary"
    )

    print(
        "-" * 40
    )


    for fault, detected in results:

        status = (
            "DETECTED"
            if detected
            else "NOT DETECTED"
        )

        print(
            f"{fault:<8} : {status}"
        )


    detected_count = sum(
        detected
        for _, detected in results
    )


    print(
        "\nDetected Faults : "
        f"{detected_count}"
    )

    print(
        "Total Faults    : "
        f"{len(results)}"
    )


    print(
        "\nStage 04 completed successfully."
    )
