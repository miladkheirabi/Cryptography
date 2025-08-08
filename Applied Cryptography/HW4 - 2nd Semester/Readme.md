# Weak DES / Triple-DES API — Applied Cryptography Challenge

**Sharif University of Technology**  
**School of Computer Engineering**  
**Course:** Applied Cryptography  
**Assignment:** Weak DES / Triple-DES API  
**Author:** Milad Kheirabi

---

## Problem Description

Although single-DES was cryptanalyzed long ago, variants such as **Triple-DES** were invented to mitigate the small key length. However, DES (and consequently some uses of Triple-DES) still has a dangerous property: the existence of *weak* and *semi-weak* keys that drastically reduce effective security.

This challenge provides two endpoints (also available through a simple web UI):

- `https://miladkheirabi.pythonanywhere.com/encrypt/<key>/<plaintext>/`  
  — encrypts the supplied plaintext (hex) using the supplied key (hex). Key length may be 16 or 24 bytes (i.e., 2-key or 3-key 3DES). Plaintext length must be a multiple of 8 bytes and inputs/outputs are hex.

- `https://miladkheirabi.pythonanywhere.com/encrypt_flag/<key>/`  
  — encrypts the hidden flag using a *pre-determined random key* (internal to the service) and returns the ciphertext (hex). You can supply a key parameter to the endpoint as part of the challenge interface.

> **Important:** A simple web UI is provided at the address below. You do **not** need** to write code or use external HTTP libraries — the UI accepts keys/plaintext and shows ciphertext.  
> **Challenge UI:** https://miladkheirabi.pythonanywhere.com

The flag format is: Mercer{flag}


---

## Task

1. Use the provided web UI to interact with both APIs. You can submit chosen keys and plaintexts using the interface (no additional code required).  
2. Investigate DES/3DES **weak keys** and **semi-weak key pairs**. These keys produce predictable or mirrored encryption behaviour that can be exploited.  
3. Design experiments (using the UI) to detect if the service’s encryption is vulnerable to a weak-key attack. In particular, try keys from the known sets of weak and semi-weak DES keys and observe the encryption outputs for chosen plaintexts.  
4. Using the information obtained from the UI, recover the hidden flag encrypted by the service.

---

## Hint

- DES has a small but well-known set of *weak* and *semi-weak* keys (see the Wikipedia page below). When those keys (or equivalent keys in 3DES) are used, encryption can be inverted or reduced to a much smaller search space.  
- For 3DES (two-key or three-key modes), certain combinations of DES weak keys or key repetitions can yield equivalent or weak effective keys.  
- Typical approach:
  - Use the UI to encrypt a fixed, known plaintext with candidate keys (including all known weak and semi-weak keys).  
  - Compare patterns and relationships between the ciphertexts from `encrypt/<key>/<plaintext>/` and the output of `encrypt_flag/<key>/`.  
  - If you find a key that produces a predictable relation (or an easily invertible transform), exploit it to recover the flag bytes.  
- Useful references:
  - PyCryptodome 3DES docs: https://pycryptodome.readthedocs.io/en/latest/src/cipher/des3.html  
  - DES weak keys (overview): https://en.wikipedia.org/wiki/Weak_key

---

## Notes on Practical Use

- The UI performs the HTTP requests for you, so you can iterate quickly without writing code.  
- Keep experiments light: the service is hosted on PythonAnywhere free tier; avoid heavy brute-force flooding.  
- Log every key/plaintext you test and their ciphertext lengths/values — that will help you spot patterns.

---
