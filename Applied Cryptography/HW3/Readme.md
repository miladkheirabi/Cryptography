## Problem Description

In the Merkle-Damgård structure, we can use a full-block CFB mode to create a hash function. This code utilizes AES with a 192-bit key length, where the first block of the message is used as the Initialization Vector (IV). The message length is encoded in bytes, and an additional 4 bytes are used to represent the length of the message. Consequently, the maximum length of the message can be up to \(2^{32}\) bytes.

### Task

Find a colliding message for 'salam' that starts with 'bye'.

### Code

```python
from Crypto.Cipher import AES

def h(x):
    r = 16 - len(x) % 16  # Merkle–Damgård pad
    if r < 5:  # if dummy block needed
        r += 16
    x += b"\x80" + b"\0" * (r - 5) + len(x).to_bytes(4, "big")
    cfb = AES.new(mode=AES.MODE_CFB,  # compress with AES-192-CFB-128
                  key=b"\xff" * 24,  # constant key
                  iv=x[:16],  # IV = first input block
                  segment_size=128)  # Full-block (128 bit segments)
    return cfb.encrypt(x)[-16:]  # last block = hashed value
