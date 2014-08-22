import math

def is_prime(n):
    for i in xrange(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

# inserts 'i' into the 'digit' digit of 'number'
# expects: i between 0 and 9, digit >= 0, number is an (int)
def insert(i, digit, number):
    if i not in range(10):
        raise ValueError
    if digit < 0 or type(digit) != int:
        raise ValueError
    N = 10 ** digit
    return 10*N*(number/N) + N*i + (number - N*(number/N))

# generates the pandigital numbers of 'digits' digits
# http://en.wikipedia.org/wiki/Pandigital_number
def pandigitals(digits):
    if not digits in range(1, 10):
      raise ValueError
    if digits == 1:
        yield 1
    else:
        panner = pandigitals(digits - 1)
        for i in panner:
            for j in range(digits):
                yield insert(digits, j, i)
                # insert digit into the jth position of i

max_pan_prime = 1
for n in range(1, 10):
    p = pandigitals(n)
    for i in p:
        if is_prime(i):
            max_pan_prime = max(i, max_pan_prime)

print max_pan_prime
