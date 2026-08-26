"""
VLSI SRAM Memory Analyzer
Stage 06: March Test

Implements a simplified March-style SRAM
memory test using read and write operations.
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
# March Test
# ------------------------------------------

def run_march_test():

    passed = 0
    failed = 0

    print("\nMARCH ELEMENT 1")
    print("↑ (w0)")

    # --------------------------------------
    # Element 1
    # Upward traversal
    # Write all zeros
    # --------------------------------------

    for address in range(MEMORY_SIZE):

        write_memory(
            address,
            "00000000"
        )

        print(
            f"Address {address:02d} : "
            f"W0 PASS"
        )

        passed += 1


    # --------------------------------------
    # Element 2
    # Upward traversal
    # r0, w1
    # --------------------------------------

    print("\nMARCH ELEMENT 2")
    print("↑ (r0, w1)")

    for address in range(MEMORY_SIZE):

        expected = "00000000"

        actual = read_memory(
            address
        )

        if actual == expected:

            print(
                f"Address {address:02d} : "
                f"R0 PASS"
            )

            passed += 1

        else:

            print(
                f"Address {address:02d} : "
                f"R0 FAIL"
            )

            failed += 1


        write_memory(
            address,
            "11111111"
        )

        print(
            f"Address {address:02d} : "
            f"W1 PASS"
        )

        passed += 1


    # --------------------------------------
    # Element 3
    # Downward traversal
    # r1, w0
    # --------------------------------------

    print("\nMARCH ELEMENT 3")
    print("↓ (r1, w0)")

    for address in range(
        MEMORY_SIZE - 1,
        -1,
        -1
    ):

        expected = "11111111"

        actual = read_memory(
            address
        )

        if actual == expected:

            print(
                f"Address {address:02d} : "
                f"R1 PASS"
            )

            passed += 1

        else:

            print(
                f"Address {address:02d} : "
                f"R1 FAIL"
            )

            failed += 1


        write_memory(
            address,
            "00000000"
        )

        print(
            f"Address {address:02d} : "
            f"W0 PASS"
        )

        passed += 1


    # --------------------------------------
    # Element 4
    # Downward traversal
    # r0
    # --------------------------------------

    print("\nMARCH ELEMENT 4")
    print("↓ (r0)")

    for address in range(
        MEMORY_SIZE - 1,
        -1,
        -1
    ):

        expected = "00000000"

        actual = read_memory(
            address
        )

        if actual == expected:

            print(
                f"Address {address:02d} : "
                f"R0 PASS"
            )

            passed += 1

        else:

            print(
                f"Address {address:02d} : "
                f"R0 FAIL"
            )

            failed += 1


    return passed, failed


# ------------------------------------------
# Main
# ------------------------------------------

if __name__ == "__main__":

    print("=" * 65)

    print(
        "       VLSI SRAM MEMORY ANALYZER"
    )

    print(
        "          STAGE 06"
    )

    print(
        "          MARCH TEST"
    )

    print("=" * 65)

    print(
        f"\nMemory Size : "
        f"{MEMORY_SIZE} × {WORD_SIZE}"
    )

    reset_memory()

    passed, failed = run_march_test()


    # --------------------------------------
    # Summary
    # --------------------------------------

    print("\n")
    print("=" * 65)

    print(
        "             MARCH TEST SUMMARY"
    )

    print("=" * 65)

    print(
        f"Total Operations : "
        f"{passed + failed}"
    )

    print(
        f"Passed           : "
        f"{passed}"
    )

    print(
        f"Failed           : "
        f"{failed}"
    )


    if failed == 0:

        print(
            "\nPASS: March test completed successfully."
        )

    else:

        print(
            "\nFAIL: Memory faults detected."
        )


    print(
        "\nStage 06 completed successfully."
    )
