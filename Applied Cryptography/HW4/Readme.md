Consider the following relations:

$x^ {a} \equiv z \pmod{N}, \quad y^ {b} \equiv z \pmod{N}, \quad w^ {ab} \equiv z \pmod{N}$

where:

- N = 51477399871343954567451032427835692323
- a = 19049383051957442773063827502460138756
- b = 40581011429749366588465472687417132497
- x = 42262668107226134502521488253731224431
- y = 22860843198302662681629113752353217222
- z = 11550537085346654381869258148777389840

## Task

Determine \( w \) given the above conditions.

## Solution

Using the extended Euclidean algorithm, we can find u and v such that:

$\gcd(a, b)=1 \quad \Rightarrow \quad u \times a+v \times b=1$

$w^ {ab} \pmod{N} = Z^ {1} \pmod{N} = Z^ {au+vb} \pmod{N} = z^ {au} \times z^ {bv} \pmod{N} = (y^ {b})^ {au} \times (x^ {a})^ {bv} \pmod{N} = y^ {bau} \times x^ {abv} \pmod{N} =  (y^ {u} \times x^ {v})^ {ab} \pmod{N} $ 

then:

$w=\left(x^v * y^u\right) \quad \bmod N$
