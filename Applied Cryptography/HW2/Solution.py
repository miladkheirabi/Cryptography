from javarandom import Random  # Import Java-like Random generator


def decode_message(filename):
    # Load chaffed data
    chaffed = list(map(eval, open(filename).readlines()))

    # Extract random values for the first and second parts of the message
    r0 = [chaffed[i][2] for i in range(27)]
    r1 = [chaffed[i][2] for i in range(27, 54)]

    # Create an instance of the Java-like Random generator
    rng = Random()

    # Try different seed values to find the correct PRNG state
    for i, s in enumerate(r0):
        if s < 0:
            s += (1 << 32)  # Ensure the value is unsigned
        s <<= 16  # Shift left to account for unknown bits

        for x in range(2 ** 16):  # Brute-force to find the correct seed
            rng._seed = s + x  # Set the seed of the PRNG

            # Discard initial values
            for _ in range(26 - i):
                rng.nextInt()  # Call nextInt to advance PRNG state

            # Compare PRNG output with known values
            for j, y in enumerate(r1):
                if rng.nextInt() == y:
                    # PRNG state found, reconstruct the message
                    message = [chaffed[i][1], chaffed[j + 27][1]]

                    # Verify the remaining values
                    for k in range(27 + j + 1, len(chaffed)):
                        if rng.nextInt() == chaffed[k][2]:
                            message.append(chaffed[k][1])

                    print(''.join(message))  # Output the decoded message
                    return


# Call the function with the filename of the chaffed data
decode_message("chaffed.txt")
