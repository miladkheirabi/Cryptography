# Hidden in Compression — Applied Cryptography Assignment 3

**Sharif University of Technology**  
**School of Computer Engineering**  
**Course:** Applied Cryptography  
**Assignment:** #3 — Hidden in Compression  
**Author:** Milad Kheirabi  
**Thanks to:** Saleh Estaki  

---

## Problem Description

In this challenge, you are given access to an **AES encryption oracle** that operates in **CTR mode**.  
You can interact with the encryption service through the provided web interface:

🔗 [Challenge Website](https://miladsaleh.pythonanywhere.com/)  
*(Hosted on PythonAnywhere — free tier. May expire after 90 days.)*

The goal is to understand **why compressing plaintext before encryption** can introduce security vulnerabilities when patterns exist in the original message.

**Important Notes:**
- A helper tool is provided on the challenge website to:
  - XOR two HEX strings
  - Convert ASCII ⇆ HEX
- The encryption function and CTR mode diagram are shown on the site.
- Avoid heavy brute-force attacks — the server is hosted on a free plan and may crash.

The flag format is: appliedcrypto{flag}

For simplicity, no special characters (other than `{}`, `_`) or digits are used in the flag.

---

## Challenge Code (Server-Side)

```python
from Crypto.Cipher import AES
from Crypto.Util import Counter
import zlib
import os

KEY = ?  # Secret key
FLAG = "appliedcrypto{XXXXXXXXXXXXXXXXXXX}"

@chal.route('/<plaintext>/')
def encrypt(plaintext):
    plaintext = bytes.fromhex(plaintext)

    iv = int.from_bytes(os.urandom(16), 'big')
    cipher = AES.new(KEY, AES.MODE_CTR, counter=Counter.new(128, initial_value=iv))
    encrypted = cipher.encrypt(zlib.compress(plaintext + FLAG.encode()))

    return {"ciphertext": encrypted.hex()}
```

## Task
1. Use the provided web interface to send **chosen-plaintext queries** to the encryption service.  
2. Craft inputs where part of the plaintext is under your control, immediately followed by the hidden flag.  
3. Measure and compare the ciphertext lengths to detect when your guess matches the actual flag prefix.  
4. Repeat the process iteratively to recover the entire flag, character by character.

## Hint
- Normally, **AES-CTR** is secure, but compressing the plaintext with **zlib** before encryption can leak information about repeated sequences shared between your input and the secret flag.  
- This vulnerability is conceptually similar to the **CRIME** and **BREACH** attacks against TLS, which exploit changes in compressed data length to deduce secrets.  
- Key insight: When your guessed prefix matches part of the flag, compression becomes more efficient, producing a shorter ciphertext — and this difference is measurable.

