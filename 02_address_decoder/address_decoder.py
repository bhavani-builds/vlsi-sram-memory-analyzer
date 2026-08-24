# ==========================================
# VLSI SRAM MEMORY ANALYZER
# STAGE 02 — ADDRESS DECODER
# ==========================================


# ------------------------------------------
# Configuration
# ------------------------------------------

ADDRESS_BITS = 4

MEMORY_SIZE = 2 ** ADDRESS_BITS


# ==========================================
# ADDRESS DECODER
# ==========================================

def decode_address(address):
    """
    Convert a binary address into
    a one-hot decoded output.
    """

    if address < 0 or address >= MEMORY_SIZE:

        print("❌ Invalid address")

        return None


    decoded = [
        0
        for _ in range(MEMORY_SIZE)
    ]


    decoded[address] = 1


    return decoded


# ==========================================
# BINARY ADDRESS
# ==========================================

def binary_address(address):

    return format(
        address,
        f"0{ADDRESS_BITS}b"
    )


# ==========================================
# DISPLAY DECODER
# ==========================================

def display_decoder():

    print("=" * 60)

    print(
        "        VLSI SRAM ADDRESS DECODER"
    )

    print("=" * 60)

    print(
        f"\nAddress Bits : {ADDRESS_BITS}"
    )

    print(
        f"Memory Size  : {MEMORY_SIZE} locations"
    )


    print(
        "\nAddress → Selected Memory Row"
    )

    print("-" * 60)


    for address in range(
        MEMORY_SIZE
    ):

        binary = binary_address(
            address
        )

        decoded = decode_address(
            address
        )

        selected_row = (
            decoded.index(1)
        )


        print(
            f"{binary} → "
            f"Row {selected_row:02d}"
        )


# ==========================================
# TEST SPECIFIC ADDRESSES
# ==========================================

def test_address(address):

    binary = binary_address(
        address
    )

    decoded = decode_address(
        address
    )


    print(
        f"\nAddress : {binary}"
    )

    print(
        f"Decimal : {address}"
    )

    print(
        f"Decoded : {decoded}"
    )


# ==========================================
# MAIN PROGRAM
# ==========================================

display_decoder()


print(
    "\n--- ADDRESS TESTS ---"
)


test_address(0)

test_address(3)

test_address(7)

test_address(15)


# ==========================================
# VERIFICATION
# ==========================================

print(
    "\n--- DECODER VERIFICATION ---"
)


decoder_pass = True


for address in range(
    MEMORY_SIZE
):

    decoded = decode_address(
        address
    )


    # Exactly one output must be HIGH

    if sum(decoded) != 1:

        decoder_pass = False

        print(
            f"❌ Address {address} FAILED"
        )

        break


    # The selected output must
    # correspond to the address

    if decoded[address] != 1:

        decoder_pass = False

        print(
            f"❌ Address {address} FAILED"
        )

        break


if decoder_pass:

    print(
        "✅ All 16 addresses decoded correctly!"
    )

    print(
        "✅ One-hot selection verified!"
    )

else:

    print(
        "❌ Address decoder verification FAILED"
    )


print(
    "\n🎉 STAGE 02 COMPLETED!"
)
