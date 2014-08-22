from proj_eul.prime_tools.sieve import naive_is_prime as _is_prime

from proj_eul.string_tools.pandigital import pandigitals as _panner

# not totally optimal, as _panner(i) is created 10-i times.
# but it's modular!

max_pan_prime = 1
for n in range(1, 10):
    p = _panner(n)
    for i in p:
        if _is_prime(i):
            max_pan_prime = max(i, max_pan_prime)

print max_pan_prime
