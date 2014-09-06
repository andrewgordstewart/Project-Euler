from proj_eul.prime_tools.sieve import prime_sieve as _sieve
from proj_eul.math_tools.permutations import is_perm as _is_perm

n = 10000
primes = [i for i in _sieve(n) if i >= n/10]

result = []
for i in primes:
    # if int(float(i)/10) % 10 == 0: print float(i)/n
    for j in primes:
        if 2*j-i in primes and i != j:
            result.append((i, j, 2*j-i))

for a, b, c in result:
    if _is_perm(a, b) and _is_perm(b, c):
        print a, b, c
