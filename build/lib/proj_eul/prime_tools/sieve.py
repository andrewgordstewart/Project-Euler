import math
import  copy
copy = copy.copy

def is_prime(n):         # A terrible, terrible primality test. Mainly for testing purposes.
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def prime_sieve(n):              # returns prime sieve up to, but not including n
    sqrt_n = int(math.sqrt(n))
    divisors = range(2, sqrt_n + 1)
    is_prime = [True for i in range(n+1)]

    for i in divisors:
        for j in range(n+1)[2*i::i]:
            is_prime[j] = False

    primes = []
    for i in range(2, n+1):
        if is_prime[i]:
            primes.append(i)

    return primes



if __name__ == '__main__':
    # print is_prime(7)

    print prime_sieve(10000)[-1]
    print prime_sieve(20)
    print prime_sieve(3)
    print is_prime(4)
