from Crypto.Cipher import AES

xor = lambda a, b: bytes(aa ^ bb for aa, bb in zip(a, b))

def h(x):
    r = 16 - len(x) % 16 # Merkle–Damgård pad
    if r < 5: # if dummy block needed
        r += 16
    x += b"\x80" + b"\0" * (r - 5) + len(x).to_bytes(4, "big")
    cfb = AES.new(mode=AES.MODE_CFB, # compress with AES-192-CFB-128
        key=b"\xff" * 24, # constant key
        iv=x[:16], # IV = first input block
        segment_size=128) # Full-block (128 bit segments)
    return cfb.encrypt(x)[-16:] # last block = hashed value

# Original message and its hash
original_message = b'salam'
original_hash = h(original_message)

# Define AES encryption and decryption in ECB mode with a constant key
encryption = AES.new(key=b"\xff" * 24, mode=AES.MODE_ECB).encrypt
decryption = AES.new(key=b"\xff" * 24, mode=AES.MODE_ECB).decrypt

# Calculate intermediate values for collision
padding = b'\x80' + b'\0' * 11 + (2 * 16).to_bytes(4, "big")
intermediate = decryption(xor(b'\x80' + b'\0' * 11 + (2 * 16).to_bytes(4, "big"), original_hash))
prefix = b'bye' + b'\0' * 13
ciphertext_prefix = xor(prefix, encryption(prefix))
collision_part = xor(encryption(ciphertext_prefix), intermediate)
collision_message = prefix + collision_part

# Verify the hash values match
assert h(collision_message) == h(original_message)
print(original_message, collision_message, h(collision_message).hex())
