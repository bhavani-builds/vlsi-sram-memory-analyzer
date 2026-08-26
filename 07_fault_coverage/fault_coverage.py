"""
VLSI SRAM Memory Analyzer
Stage 07: Fault Coverage Analysis

Calculates detection coverage for:

1. Stuck-at-0 faults
2. Stuck-at-1 faults
3. 0->1 transition faults
4. 1->0 transition faults

SRAM organization:
16 addresses x 8 bits
"""

from dataclasses import dataclass


# ==========================================
# SRAM CONFIGURATION
# ==========================================

MEMORY_SIZE = 16
WORD_SIZE = 8


# ==========================================
# FAULT MODEL
# ==========================================

@dataclass
class Fault:

    address: int
    bit: int
    fault_type: str


# ==========================================
# FAULTY MEMORY
# ==========================================

class FaultyMemory:

    def __init__(self, fault):

        self.memory = [
            "00000000"
            for _ in range(MEMORY_SIZE)
        ]

        self.fault = fault


    # --------------------------------------
    # Reset memory
    # --------------------------------------

    def reset(self):

        self.memory = [
            "00000000"
            for _ in range(MEMORY_SIZE)
        ]


    # --------------------------------------
    # Write operation
    # --------------------------------------

    def write(self, address, data):

        previous_data = self.memory[address]

        new_data = list(data)


        # ----------------------------------
        # Stuck-at faults
        # ----------------------------------

        if address == self.fault.address:

            if self.fault.fault_type == "SA0":

                new_data[self.fault.bit] = "0"


            elif self.fault.fault_type == "SA1":

                new_data[self.fault.bit] = "1"


        # ----------------------------------
        # Transition faults
        # ----------------------------------

        if address == self.fault.address:

            previous_bit = (
                previous_data[self.fault.bit]
            )

            requested_bit = (
                data[self.fault.bit]
            )


            # 0 -> 1 transition failure

            if (
                self.fault.fault_type == "TF_RISE"
                and previous_bit == "0"
                and requested_bit == "1"
            ):

                new_data[self.fault.bit] = "0"


            # 1 -> 0 transition failure

            elif (
                self.fault.fault_type == "TF_FALL"
                and previous_bit == "1"
                and requested_bit == "0"
            ):

                new_data[self.fault.bit] = "1"


        self.memory[address] = (
            "".join(new_data)
        )


    # --------------------------------------
    # Read operation
    # --------------------------------------

    def read(self, address):

        data = self.memory[address]

        return data


# ==========================================
# MARCH TEST
# ==========================================

def run_march_test(memory):

    """
    Simplified March test:

    ↑ (w0)
    ↑ (r0,w1)
    ↓ (r1,w0)
    ↓ (r0)
    """

    # --------------------------------------
    # Element 1: ↑ w0
    # --------------------------------------

    for address in range(MEMORY_SIZE):

        memory.write(
            address,
            "00000000"
        )


    # --------------------------------------
    # Element 2: ↑ r0,w1
    # --------------------------------------

    for address in range(MEMORY_SIZE):

        if memory.read(address) != "00000000":

            return False

        memory.write(
            address,
            "11111111"
        )


    # --------------------------------------
    # Element 3: ↓ r1,w0
    # --------------------------------------

    for address in range(
        MEMORY_SIZE - 1,
        -1,
        -1
    ):

        if memory.read(address) != "11111111":

            return False

        memory.write(
            address,
            "00000000"
        )


    # --------------------------------------
    # Element 4: ↓ r0
    # --------------------------------------

    for address in range(
        MEMORY_SIZE - 1,
        -1,
        -1
    ):

        if memory.read(address) != "00000000":

            return False


    return True


# ==========================================
# FAULT GENERATION
# ==========================================

def generate_faults():

    faults = []


    fault_types = [
        "SA0",
        "SA1",
        "TF_RISE",
        "TF_FALL"
    ]


    for address in range(
        MEMORY_SIZE
    ):

        for bit in range(
            WORD_SIZE
        ):

            for fault_type in fault_types:

                faults.append(
                    Fault(
                        address,
                        bit,
                        fault_type
                    )
                )


    return faults


# ==========================================
# FAULT COVERAGE
# ==========================================

def calculate_coverage(faults):

    detected_faults = []

    undetected_faults = []


    for fault in faults:

        memory = FaultyMemory(
            fault
        )


        detected = not run_march_test(
            memory
        )


        if detected:

            detected_faults.append(
                fault
            )

        else:

            undetected_faults.append(
                fault
            )


    return (
        detected_faults,
        undetected_faults
    )


# ==========================================
# MAIN
# ==========================================

if __name__ == "__main__":

    print("=" * 70)

    print(
        "       VLSI SRAM MEMORY ANALYZER"
    )

    print(
        "          STAGE 07"
    )

    print(
        "       FAULT COVERAGE ANALYSIS"
    )

    print("=" * 70)


    # --------------------------------------
    # Generate faults
    # --------------------------------------

    faults = generate_faults()


    print(
        f"\nMemory Organization : "
        f"{MEMORY_SIZE} × {WORD_SIZE}"
    )

    print(
        f"Memory Cells        : "
        f"{MEMORY_SIZE * WORD_SIZE}"
    )

    print(
        f"Total Faults        : "
        f"{len(faults)}"
    )


    # --------------------------------------
    # Calculate coverage
    # --------------------------------------

    detected, undetected = (
        calculate_coverage(faults)
    )


    detected_count = len(
        detected
    )

    undetected_count = len(
        undetected
    )


    total_faults = len(
        faults
    )


    coverage = (
        detected_count
        / total_faults
    ) * 100


    # --------------------------------------
    # Fault category statistics
    # --------------------------------------

    fault_categories = [
        "SA0",
        "SA1",
        "TF_RISE",
        "TF_FALL"
    ]


    print(
        "\nFault Coverage by Type"
    )

    print(
        "-" * 55
    )


    for fault_type in fault_categories:

        total = sum(
            fault.fault_type == fault_type
            for fault in faults
        )


        detected_type = sum(
            fault.fault_type == fault_type
            for fault in detected
        )


        type_coverage = (
            detected_type
            / total
        ) * 100


        print(
            f"{fault_type:<10}"
            f"Total: {total:<6}"
            f"Detected: {detected_type:<6}"
            f"Coverage: {type_coverage:.2f}%"
        )


    # --------------------------------------
    # Overall result
    # --------------------------------------

    print(
        "\nOverall Fault Coverage"
    )

    print(
        "-" * 55
    )


    print(
        f"Total Faults     : "
        f"{total_faults}"
    )

    print(
        f"Detected Faults  : "
        f"{detected_count}"
    )

    print(
        f"Undetected Faults: "
        f"{undetected_count}"
    )

    print(
        f"Fault Coverage   : "
        f"{coverage:.2f}%"
    )


    # --------------------------------------
    # Status
    # --------------------------------------

    if coverage == 100:

        print(
            "\nPASS: All modeled faults detected."
        )

    elif coverage >= 90:

        print(
            "\nGOOD: High fault coverage achieved."
        )

    else:

        print(
            "\nWARNING: Additional test patterns "
            "may be required."
        )


    # --------------------------------------
    # Undetected faults
    # --------------------------------------

    if undetected:

        print(
            "\nUndetected Faults"
        )

        print(
            "-" * 55
        )


        for fault in undetected[:10]:

            print(
                f"Address={fault.address}, "
                f"Bit={fault.bit}, "
                f"Type={fault.fault_type}"
            )


        if len(undetected) > 10:

            print(
                f"... and "
                f"{len(undetected) - 10} more"
            )


    print(
        "\nStage 07 completed successfully."
    )
