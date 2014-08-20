import sieve

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



def foo(bar):
    return None

if __name__ == '__main__':

    n = 1211012432
    fac = prime_decomposition(n)
    print fac
    x = 1
    for i in fac:
        x = x * i**fac[i]
    print x, n
