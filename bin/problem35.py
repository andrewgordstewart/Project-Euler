from proj_eul.prime_tools.sieve import primes_to_n as _sieve
from proj_eul.math_tools.permutations import cyclic_permute as _cyclic_permute

import timeit

n = 1000000
print n
s = _sieve(n)
primes = set(s)
print len(s)

result = set()
for i in s:
    length = len(str(i))
    for j in range(length):
        if not i in primes:
            # print 'not cyclic prime: ', i, _cyclic_permute(i)
            break
        i = _cyclic_permute(i)

    if i in primes: result.add(i)

print len(result)
