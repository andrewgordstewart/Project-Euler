import math
import  copy
copy = copy.copy

def naive_is_prime(n):         # A terrible, terrible primality test. Mainly for testing purposes.
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

def sieve(n):              # returns prime sieve up to, but not including n
    sqrt_n = int(math.sqrt(n))
    candidates = range(n)
    divisors = range(2, sqrt_n + 1)
    is_prime = [True for i in range(n)]

    for i in divisors:
        for j in range(n)[2*i::i]:
            is_prime[j] = False

    primes = []
    for i in range(2, n):
        if is_prime[i]:
            primes.append(i)

    return primes



if __name__ == '__main__':
    # print is_prime(7)

    print sieve(10000)[-1]
    print sieve(20)

