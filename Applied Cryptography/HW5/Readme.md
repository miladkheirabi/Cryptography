# Problem Statement

Given two arbitrary integers \( x \) and \( y \) in the range [1, p-1], consider the following hash function:

$\[ H(x, y) := a^x b^y \mod p \]$

where:
- a = 123456789
- b = 987654321
- p = 45944761914051133163

### Task 1

Provide an example of a collision for the pair (1402, 2023).

### Task 2

Provide an example of a collision for the pair (p - 1402, p - 2023).

### Solution

```python
a = 123456789
b = 987654321
p = 45944761914051133163

def h(x, y):
    assert 1 <= x <= p-1 and 1 <= y <= p-1
    return pow(a, x, p) * pow(b, y, p) % p

q = (p-1)//2
print(h(1402, 2023+q) == h(1402, 2023))  # True
print(h(p-1402, p-2023-q) == h(p-1402, p-2023))  # True
```

### Explanation of Collisions

To understand why \( q \) causes collisions in the hash function, let’s analyze the modular arithmetic properties of the hash function:

The hash function is defined as $\[ H(x, y) = (a^x \mod p) \cdot (b^y \mod p) \mod p \]$

where:
- a = 123456789
- b = 987654321
- p = 45944761914051133163

The value of \( q \) is $\[ q = \frac{p-1}{2} \]$

### First Collision Check

This checks whether: $\[ H(1402, 2023+q) = H(1402, 2023) \]$

Breaking it down:

- For H(1402, 2023+q): $\[ H(1402, 2023+q) = (a^{1402} \mod p) \cdot (b^{2023+q} \mod p) \mod p \]$

- For H(1402, 2023): $\[ H(1402, 2023) = (a^{1402} \mod p) \cdot (b^{2023} \mod p) \mod p \]$

We have:

$\[ b^{2023+q} \equiv b^{2023} \cdot b^q \mod p \]$

Given $\( q = \frac{p-1}{2} \)$:

$\[ b^q \equiv b^{(p-1)/2} \equiv -1 \mod p \]$

Thus:

$\[ b^{2023+q} \equiv b^{2023} \cdot (-1) \mod p \]$

Therefore:

$\[ H(1402, 2023+q) \equiv (a^{1402} \mod p) \cdot (b^{2023} \mod p) \cdot (-1) \mod p \]$

This simplifies to:

$\[ H(1402, 2023+q) \equiv -H(1402, 2023) \mod p \]$

Thus:

$\[ H(1402, 2023+q) = H(1402, 2023) \]$

### Second Collision Check

This checks whether:

$\[ H(p-1402, p-2023-q) = H(p-1402, p-2023) \]$

Breaking it down:

- For \( H(p-1402, p-2023-q) \):

$\[ H(p-1402, p-2023-q) = (a^{p-1402} \mod p) \cdot (b^{p-2023-q} \mod p) \mod p \]$

- For \( H(p-1402, p-2023) \):

$\[ H(p-1402, p-2023) = (a^{p-1402} \mod p) \cdot (b^{p-2023} \mod p) \mod p \]$

We have:

$\[ b^{p-2023-q} \equiv b^{p-2023} \cdot b^{-q} \mod p \]$

Given $\( q = \frac{p-1}{2} \)$:

$\[ b^{-q} \equiv b^{-(p-1)/2} \equiv -1 \mod p \]$

Thus:

$\[ b^{p-2023-q} \equiv b^{p-2023} \cdot (-1) \mod p \]$

Therefore:

$\[ H(p-1402, p-2023-q) \equiv (a^{p-1402} \mod p) \cdot (b^{p-2023} \mod p) \cdot (-1) \mod p \]$

This simplifies to:

$\[ H(p-1402, p-2023-q) \equiv -H(p-1402, p-2023) \mod p \]$

Thus:

$\[ H(p-1402, p-2023-q) = H(p-1402, p-2023) \]$

### Conclusion

The collisions occur because adding \( q \) to \( y \) in the hash function effectively negates the value due to the properties of modular arithmetic. Specifically, $\( b^q \equiv -1 \mod p \) \when\ \( q = \frac{p-1}{2} \)$. This results in collisions in the hash function.
