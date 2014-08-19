import sieve

def prime_factors(n):  # currently terribly inefficient for just one call.
    print 'in prime_factors'
    s = sieve.sieve(n/2+1)
    factors = []
    for i in s:
        if n % i == 0:
            print i
            factors.append(i)
    if factors == []:
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

def foo(bar):
    return None

if __name__ == '__main__':

    print sieve.is_prime(11523)
    print factors_with_multiplicity(6043)[-1]
    print prime_factors(71)

    pass
