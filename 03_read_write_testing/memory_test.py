"""
VLSI SRAM Memory Analyzer
Stage 03: Read/Write Verification

Tests basic SRAM read and write operations
and verifies stored data.
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
# Write Operation
# ------------------------------------------

def write_memory(address, data):
    """
    Write an 8-bit binary value
    into the specified SRAM address.
    """

    if not 0 <= address < MEMORY_SIZE:
        raise ValueError(
            "Invalid SRAM address."
        )

    if len(data) != WORD_SIZE:
        raise ValueError(
            "Data must contain exactly 8 bits."
        )

    if any(bit not in "01" for bit in data):
        raise ValueError(
            "Data must contain only 0 and 1."
        )

    memory[address] = data


# ------------------------------------------
# Read Operation
# ------------------------------------------

def read_memory(address):
    """
    Read data from the specified SRAM address.
    """

    if not 0 <= address < MEMORY_SIZE:
        raise ValueError(
            "Invalid SRAM address."
        )

    return memory[address]


# ------------------------------------------
# Verify Single Location
# ------------------------------------------

def verify_location(address, expected_data):
    """
    Compare expected data with actual
    SRAM contents.
    """

    actual_data = read_memory(address)

    return actual_data == expected_data


# ------------------------------------------
# Test Pattern
# ------------------------------------------

test_pattern = {

    0: "10101010",

    1: "01010101",

    3: "11110000",

    5: "00001111",

    7: "11001100",

    10: "00110011",

    15: "11111111"
}


# ------------------------------------------
# Write Test
# ------------------------------------------

def run_write_test():

    print("\nWrite Test")
    print("-" * 55)

    for address, data in test_pattern.items():

        write_memory(
            address,
            data
        )

        print(
            f"WRITE | "
            f"Address: {address:02d} | "
            f"Data: {data}"
        )


# ------------------------------------------
# Read Test
# ------------------------------------------

def run_read_test():

    print("\nRead Test")
    print("-" * 55)

    passed = 0
    failed = 0

    for address, expected_data in (
        test_pattern.items()
    ):

        actual_data = read_memory(
            address
        )

        if actual_data == expected_data:

            print(
                f"READ  | "
                f"Address: {address:02d} | "
                f"Expected: {expected_data} | "
                f"Actual: {actual_data} | "
                f"PASS"
            )

            passed += 1

        else:

            print(
                f"READ  | "
                f"Address: {address:02d} | "
                f"Expected: {expected_data} | "
                f"Actual: {actual_data} | "
                f"FAIL"
            )

            failed += 1

    return passed, failed


# ------------------------------------------
# Memory Dump
# ------------------------------------------

def display_memory():

    print("\nMemory Contents")
    print("-" * 35)

    print(
        f"{'Address':<10}"
        f"{'Data':<12}"
    )

    print("-" * 35)

    for address in range(MEMORY_SIZE):

        print(
            f"{address:<10}"
            f"{memory[address]:<12}"
        )


# ------------------------------------------
# Main
# ------------------------------------------

if __name__ == "__main__":

    print("=" * 60)

    print(
        "       VLSI SRAM MEMORY ANALYZER"
    )

    print(
        "          STAGE 03"
    )

    print(
        "       READ/WRITE VERIFICATION"
    )

    print("=" * 60)

    print(
        f"\nMemory Size : "
        f"{MEMORY_SIZE} × {WORD_SIZE}"
    )

    # Run write operations

    run_write_test()

    # Run read operations

    passed, failed = run_read_test()

    # Display memory

    display_memory()

    # Verification summary

    print("\nVerification Summary")
    print("-" * 35)

    print(
        f"Total Tests : "
        f"{passed + failed}"
    )

    print(
        f"Passed      : "
        f"{passed}"
    )

    print(
        f"Failed      : "
        f"{failed}"
    )

    if failed == 0:

        print(
            "\nPASS: SRAM read/write verification successful."
        )

    else:

        print(
            "\nFAIL: SRAM verification detected errors."
        )

    print(
        "\nStage 03 completed successfully."
    )
