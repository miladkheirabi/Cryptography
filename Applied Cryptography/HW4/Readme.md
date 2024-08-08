# Modular Congruences Problem

## Problem Statement

Given the following modular congruences:

$x^ {a} \equiv z \pmod{N}, \quad y^ {b} \equiv z \pmod{N}, \quad w^ {ab} \equiv z \pmod{N}$

where the values are defined as:

- N = 51477399871343954567451032427835692323
- a = 19049383051957442773063827502460138756
- b = 40581011429749366588465472687417132497
- x = 42262668107226134502521488253731224431
- y = 22860843198302662681629113752353217222
- z = 11550537085346654381869258148777389840

## Objective

Determine the value of \( w \) under the given conditions.

## Solution

We can use the extended Euclidean algorithm to find integers \( u \) and \( v \) such that:

$\gcd(a, b)=1 \quad \Rightarrow \quad u \times a+v \times b=1$

From this, we derive the equation:

$w^ {ab} \pmod{N} = Z^ {1} \pmod{N} = Z^ {au+vb} \pmod{N} = z^ {au} \times z^ {bv} \pmod{N} = (y^ {b})^ {au} \times (x^ {a})^ {bv} \pmod{N} = y^ {bau} \times x^ {abv} \pmod{N} =  (y^ {u} \times x^ {v})^ {ab} \pmod{N} $ 

Thus, the value of \( w \) can be determined as:

$w= x^v \times y^u \pmod{N}$


### Python Implementation

Below is a Python code snippet to compute u, v and w:

```python
N = 51477399871343954567451032427835692323
a = 19049383051957442773063827502460138756
b = 40581011429749366588465472687417132497
x = 42262668107226134502521488253731224431
y = 22860843198302662681629113752353217222
z = 11550537085346654381869258148777389840

def extended_gcd(a, b):
    if a == 0:
        return 0, 1
    else:
        x1, y1 = extended_gcd(b % a, a)
        u = y1 - (b // a) * x1
        v = x1
        return u, v


u, v = extended_gcd(a, b)
tmp1 = pow(x,v,N)
tmp2 = pow(y,u,N)
w = pow(tmp1*tmp2,1,N)
print(f"u: {u}, v: {v}, w:{w}")
```
- u = 10616958366426942569600531678716415266
- v = -4983771957455134258169495341793746135
- w = 35766277574666954059893916652511119753
