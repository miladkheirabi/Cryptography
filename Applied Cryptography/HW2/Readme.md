Farmers use encryption to transmit their messages, ensuring the confidentiality of their communications by combining straw and remaining leaves. The most well-known method to do this among wheat farmers is to maintain this secrecy. This nature-friendly technique is a combination of chaff and winnowing.

### Process Overview:

1. **Agreement Phase:**
   - Before starting the message transmission process, the two farmers agree on a confidential amount, denoted as `s`.
   - This confidential amount is used for every message transmission.

2. **Message Preparation:**
   - The message `m` is assumed to be a sequence of letters from the English alphabet plus space, `m = m_1 m_2 ... m_n`, where the alphabet size `|Σ| = 27`.

3. **Pseudo-random Number Generation:**
   - A pseudo-random number generator (PRNG) initialized with the agreed amount `s` is used. Here, the standard Java library's PRNG (version before 17) is used.
   - The generated pseudo-random numbers will be denoted by `g_i`.

4. **Message Encoding:**
   - For each letter `m_i` in the message, `Σ` packets will be sent:
     - Each packet contains three values:
       1. The position `i`.
       2. The letter (`' '`, `'a'`, `'b'`, ...).
       3. If `m_i == j`, the third value will be `g_i * |Σ| + j`.

5. **Message Decoding:**
   - On the receiver side, the sequence of pseudo-random numbers `g_i` is regenerated using the agreed amount `s`.
   - By comparing the numbers in each packet with the regenerated sequence, the original message can be retrieved.

### Example Code:

Below is an example implementation of the described process in Python, showing the chaffing and winnowing technique:

```python
from string import ascii_lowercase
from os import urandom # system random generator
import javarandom # java random generator

# Initialize the Java random generator with the agreed seed
SEED = 12345  # Example seed
G = javarandom.Random(SEED)

# Read the message from a file and convert to lowercase
M = open("wheat.txt").read().lower()

# Define the alphabet including space
alphabet = ascii_lowercase + " "

# Chaffing process
c = []
for i, m in enumerate(M):
    assert m in alphabet  # Ensure message can be sent
    for j, a in enumerate(alphabet):  # j -> alphabet index
        if a == m:
            c.append((i, m, G.nextInt() * len(alphabet) + j))  # g_i * |Σ| + j
        else:
            _ = G.nextInt()  # Discard next number in PRNG series
            c.append((i, a, int.from_bytes(urandom(4), "big", signed=True)))  # Use true random number

# Write the chaffed message to a file
open("chaffed.txt", "w").write("\n".join(map(str, c)))
