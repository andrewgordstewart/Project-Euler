import math

import sieve
sieve = sieve.sieve


def prime_factors(n):
    s = sieve(n/2+1)
    factors = [1]
    for i in s:
        if n % i == 0:
            print i
            factors.append(i)
    factors.append(n)

    return factors

def factors(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 2]
    for i in range(2, n+1):
        if n%i == 0:
            li = factors(n/i)
            li.append(n)
            return li

if __name__ == '__main__':

    for i in range(10):
        print i, factors(i)
