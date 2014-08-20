from proj_eul.prime_tools.factor import prime_decomposition as _factors
from proj_eul.prime_tools.sieve import sieve as _sieve

n = 20

s = _sieve(n)


power = {}
for prime in s:
    power[prime] = 0
    for j in range(2, n):
        fac = _factors(j)
        if prime in fac.keys():
            power[prime] = max(fac[prime], power[prime])

x = 1
for i in power:
    x *= i**power[i]

print x
