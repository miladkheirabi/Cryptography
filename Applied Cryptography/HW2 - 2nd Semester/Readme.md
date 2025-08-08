## Challenge — Weak Random Number Generator: Cryptographers' Playground

### Problem Description
In this challenge, you are dealing with a **random number generator** that suffers from a serious security flaw.  
Although the code may initially appear complex, this is due to the use of **basic obfuscation techniques** — intended to make the code harder to read but not truly secure.

Due to the incorrect use of functions and weak internal structures, the generator is **easily breakable**.  
Your task is to carefully analyze the code, identify the weaknesses, and exploit them to recover the flag.

**Background:**  
- *Obfuscation* is the process of deliberately making code harder to understand, often to hinder reverse engineering.  
- *Deobfuscation* is the process of reversing obfuscation to recover the original, more readable code.  
- The obfuscation level in this challenge is intentionally simple to serve as an introductory exercise.

The flag is in the format: MERCER{flag}

---

## Given Code

```python
PINK = 118
RED = 101
YELLOW = 97
GREEN = 108
BLACK = __builtins__

e = getattr(BLACK, bytes([RED, PINK, YELLOW, GREEN]).decode())
g = e(''.__dir__()[4].strip('_')[:7])
t = ['72616e64696e74', '72616e646f6d', '5f5f696d706f72745f5f', '2bf8ae2175e04baef248']
d = lambda x: bytes.fromhex(x).decode()
_i = lambda x: e(d(t[2]))(x)

def enc(f):
    return [
        (
            g(_i(d(t[1])), d(t[0]))(10**10, 10**15) * int(bit)
            + int(t[3], 16)
            + (g(_i(d(t[1])), d(t[0]))(10**10, 10**15) ** 2)
        )
        for bit in ''.join([bin(i)[2:].zfill(8) for i in f])
    ]

FLAG = b'MERCER{XXXXXXXXXXXXXXXXX}'
cipher = enc(FLAG)

# Write the list to the file
with open('Output.txt', 'w') as file:
    for item in cipher:
        file.write(f"{item}\n")
