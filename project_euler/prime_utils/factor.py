import sieve
sieve = sieve.sieve



def prime_factors(n):  # currently terribly inefficient for just one call.
    s = sieve(n/2+1)
    factors = [1]
    for i in s:
        if n % i == 0:
            print i
            factors.append(i)
    factors.append(n)

    return factors

def factors_with_multiplicity(n):
    x = n
    li = [1]
    while x > 1:
        i = 2
        while i <= x:
            if x%i == 0:
                li.append(i)
                x = x/i
                i == 2
            else:
                i += 1

    return li


if __name__ == '__main__':

    print factors_with_multiplicity(600851475143)[-1]
    print dir()

    pass
