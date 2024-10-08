A grayscale image is encrypted using the Vigenere method and attached.
Assumptions:
- The value of the most redundant pixel is 180.
- The key length is not bigger than 20.
The original picture must be recovered.

The encryption code is written below:

```python
import numpy as np
from PIL import Image
from itertools import product

p = np.array(Image.open("plain.png").convert("L"))
k = np.random.randint(255, size=(N, N), dtype=np.uint8)
assert p.shape[0] == p.shape[1] and p.shape[0] % k.shape[0] == 0
m = p.shape[0]
n = k.shape[0]

c = p.copy()
for i, j in product(range(m // n), range(m // n)):
    c[i * n : (i + 1) * n, j * n : (j + 1) * n] ^= k

Image.fromarray(c).save("cipher.png")
