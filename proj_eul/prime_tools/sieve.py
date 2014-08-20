import math


# A terrible, terrible primality test. Mainly for testing purposes.
def naive_is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

# primes up to, but not including n
# this defines a generator
def prime_sieve(limit):
    a = [True] * limit        # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            n, step = i*i, i
            while n < limit:     # Mark factors non-prime
                a[n] = False
                n += step

# This generates the list of primes up to, and including n
def primes_to_n(limit):
    primes= prime_sieve(limit+1)
    list_of_primes = []
    for i in primes:
            list_of_primes.append(i)
    return list_of_primes

def is_prime(n):
    is_prime = {}
    primes = primes_to_n(n)
    for i in range(1, n):
        is_prime[i] = False
    for i in primes:
        is_prime[i] = True
    return is_prime





if __name__ == '__main__':
    # print is_prime(7)

    print primes_to_n(10000)[-1]
    print primes_to_n(20)
    print primes_to_n(3)
    print is_prime(4)
    s = prime_sieve(10)
    for i in s:
        print i
