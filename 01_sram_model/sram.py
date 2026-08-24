# ==========================================
# VLSI SRAM MEMORY ANALYZER
# STAGE 01 — SRAM MEMORY MODEL
# ==========================================


# ------------------------------------------
# SRAM Configuration
# ------------------------------------------

MEMORY_SIZE = 16
WORD_SIZE = 8


# ------------------------------------------
# Create SRAM memory
# ------------------------------------------

memory = [
    "00000000"
    for _ in range(MEMORY_SIZE)
]


# ==========================================
# WRITE OPERATION
# ==========================================

def write_memory(address, data):

    if address < 0 or address >= MEMORY_SIZE:
        print("❌ Invalid memory address")
        return

    if len(data) != WORD_SIZE:
        print("❌ Data must contain 8 bits")
        return

    if any(bit not in "01" for bit in data):
        print("❌ Data must contain only 0 and 1")
        return

    memory[address] = data

    print(
        f"WRITE  Address: {address:02d} "
        f"Data: {data}"
    )


# ==========================================
# READ OPERATION
# ==========================================

def read_memory(address):

    if address < 0 or address >= MEMORY_SIZE:
        print("❌ Invalid memory address")
        return None

    data = memory[address]

    print(
        f"READ   Address: {address:02d} "
        f"Data: {data}"
    )

    return data


# ==========================================
# MEMORY DUMP
# ==========================================

def display_memory():

    print("\n")
    print("=" * 40)
    print("           SRAM MEMORY")
    print("=" * 40)

    print(
        "Address        Data"
    )

    print("-" * 40)

    for address in range(MEMORY_SIZE):

        print(
            f"{address:02d}             "
            f"{memory[address]}"
        )

    print("=" * 40)


# ==========================================
# TEST SRAM
# ==========================================

print("=" * 50)

print(
    "        VLSI SRAM MEMORY ANALYZER"
)

print(
    "             16 × 8 SRAM"
)

print("=" * 50)


print(
    f"\nMemory Locations : {MEMORY_SIZE}"
)

print(
    f"Word Size        : {WORD_SIZE} bits"
)

print(
    f"Total Capacity   : "
    f"{MEMORY_SIZE * WORD_SIZE} bits"
)


# ------------------------------------------
# Write test data
# ------------------------------------------

print("\n--- WRITE OPERATIONS ---")

write_memory(
    0,
    "10101010"
)

write_memory(
    3,
    "11001100"
)

write_memory(
    7,
    "11110000"
)

write_memory(
    15,
    "00001111"
)


# ------------------------------------------
# Read test data
# ------------------------------------------

print("\n--- READ OPERATIONS ---")

read_memory(0)

read_memory(3)

read_memory(7)

read_memory(15)


# ------------------------------------------
# Display complete memory
# ------------------------------------------

display_memory()


# ==========================================
# VERIFICATION
# ==========================================

print("\n--- MEMORY VERIFICATION ---")


if read_memory(0) == "10101010":

    print("✅ Address 0 verification PASS")

else:

    print("❌ Address 0 verification FAIL")


if read_memory(3) == "11001100":

    print("✅ Address 3 verification PASS")

else:

    print("❌ Address 3 verification FAIL")


if read_memory(7) == "11110000":

    print("✅ Address 7 verification PASS")

else:

    print("❌ Address 7 verification FAIL")


if read_memory(15) == "00001111":

    print("✅ Address 15 verification PASS")

else:

    print("❌ Address 15 verification FAIL")


print(
    "\n🎉 STAGE 01 COMPLETED!"
)
