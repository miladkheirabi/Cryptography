# Weak Elliptic Curve Diffie-Hellman Challenge

## Challenge Description

One of the key applications of asymmetric cryptography is the exchange of symmetric encryption keys. Elliptic curve cryptography (ECC) allows for faster computations while maintaining the security level of the Diffie-Hellman protocol. However, just like RSA can be insecure under certain conditions, not all elliptic curves are secure.

In this challenge, the curve parameters are intentionally chosen to be weak:  
- The order of the generator point is composed of small prime factors.  
- This allows the discrete logarithm problem (DLP) to be solved efficiently using the **Pohlig–Hellman algorithm** and the **Baby-step Giant-step** method.

Your task is to recover the shared secret from the provided public keys and curve parameters, and then use it to decrypt the flag.

---

## Provided Python Code

```python
from Crypto.Cipher import AES
from Crypto.Util.number import inverse
from Crypto.Util.Padding import pad, unpad
from collections import namedtuple
from random import randint
import hashlib
import os

# Create a simple Point class to represent the affine points.
Point = namedtuple("Point", "x y")

# The point at infinity (origin for the group law).
O = 'Origin'

FLAG = b'crypto{??????????????????????????????}'

def check_point(P: tuple):
    if P == O:
        return True
    else:
        return (P.y**2 - (P.x**3 + a*P.x + b)) % p == 0 and 0 <= P.x < p and 0 <= P.y < p

def point_inverse(P: tuple):
    if P == O:
        return P
    return Point(P.x, -P.y % p)

def point_addition(P: tuple, Q: tuple):
    if P == O:
        return Q
    elif Q == O:
        return P
    elif Q == point_inverse(P):
        return O
    else:
        if P == Q:
            lam = (3*P.x**2 + a)*inverse(2*P.y, p)
            lam %= p
        else:
            lam = (Q.y - P.y) * inverse((Q.x - P.x), p)
            lam %= p
    Rx = (lam**2 - P.x - Q.x) % p
    Ry = (lam*(P.x - Rx) - P.y) % p
    R = Point(Rx, Ry)
    assert check_point(R)
    return R

def double_and_add(P: tuple, n: int):
    Q = P
    R = O
    while n > 0:
        if n % 2 == 1:
            R = point_addition(R, Q)
        Q = point_addition(Q, Q)
        n = n // 2
    assert check_point(R)
    return R

def gen_shared_secret(Q: tuple, n: int):
    S = double_and_add(Q, n)
    return S.x

def encrypt_flag(shared_secret: int):
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(FLAG, 16))
    data = {}
    data['iv'] = iv.hex()
    data['encrypted_flag'] = ciphertext.hex()
    return data

# Define the curve
p = 310717010502520989590157367261876774703
a = 2
b = 3

# Generator
g_x = 179210853392303317793440285562762725654
g_y = 105268671499942631758568591033409611165
G = Point(g_x, g_y)

# My secret int
n = randint(1, p)

# Send this to Bob!
public = double_and_add(G, n)
print(public)

# Bob's public key
b_x = 272640099140026426377756188075937988094
b_y = 51062462309521034358726608268084433317
B = Point(b_x, b_y)

# Calculate Shared Secret
shared_secret = gen_shared_secret(B, n)

# Send this to Bob!
ciphertext = encrypt_flag(shared_secret)
print(ciphertext)
```

---

## Task

1. Analyze the provided elliptic curve parameters.
2. Notice that the generator order is composed of **small prime factors**, making the discrete log problem easier.
3. Use algorithms such as **Pohlig–Hellman** or **Baby-step Giant-step** to recover the private key `n` from the public key.
4. Compute the shared secret using Bob's public key.
5. Derive the AES key from the shared secret using SHA-1 (first 16 bytes).
6. Decrypt the flag using the AES key in CBC mode.

---

## Hints

- Use `SageMath` — it already implements a combination of Pohlig–Hellman and Baby-step Giant-step, which is perfect for this challenge.
- The SHA-1 derivation step is implemented exactly like in the code above:
  ```python
  sha1 = hashlib.sha1()
  sha1.update(str(shared_secret).encode('ascii'))
  key = sha1.digest()[:16]
  ```
- AES uses CBC mode with PKCS#7 padding.
- Both public keys and parameters are provided, so you have all you need to recover the flag.
