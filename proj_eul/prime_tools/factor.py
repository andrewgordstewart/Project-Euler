import math

def prime_decomposition(n):
    factor_list = prime_factors_with_multiplicity(n)
    factors = {}

    for i in factor_list:
        if not i in factors.keys():
            factors[i] = 1
        else:
            factors[i] += 1

    return factors


def prime_factors_with_multiplicity(n):
    x = n
    li = []
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

def unordered_prime_factors(num):       #Returns the prime factors of num (with multiplicity)
    if type(num) != int or num < 2:
        print "Domain problem"
        return
    for i in range(2,int(math.sqrt(num))+1):
        if num%i == 0:
            factors = unordered_prime_factors(num/i)
            factors.append(i)
            return factors
    return [num]

def prime_factorization(num):
    if num == 1:
        return [[1,1]]
    repeated_prime_factors = unordered_prime_factors(num)
    facs = prime_factors(num)
    factorization = []
    num_factors = 1
    for i in facs:
        factorization.append([i, repeated_prime_factors.count(i)])
        num_factors *= repeated_prime_factors.count(i)+1
    return factorization



def prime_factors(n):
    return set(prime_factors_with_multiplicity(n))

def proper_factors(num):
    factorization = prime_factorization(num)
    num_factors = len(factorization)
    factors = set([1])
    for i in range(num_factors):
        new_factors = set([])
        for f in factors:
            for j in range(factorization[i][1]+1):
                new_factors.add(f*factorization[i][0]**j)
        factors.update(new_factors)
    return factors

def is_abundant(num):
    factors = proper_factors(num)
    x = sum(i for i in factors) - num
    if x > num:
        return True
    else:
        return False



if __name__ == '__main__':

    print unordered_prime_factors(12)
    print prime_factorization(12)
    print proper_factors(124)
    print proper_factors(1)

    # n = 1211012432
    # fac = prime_decomposition(n)
    # print fac
    # x = 1
    # for i in fac:
    #     x = x * i**fac[i]
    # print x, n
