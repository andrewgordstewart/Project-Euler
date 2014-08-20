def fib(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fib(n-1) + fib(n-2)
    else:
        print "Garbage input."
        return None

def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

def fib_printer(n):
    a, b = 0, 1
    while b < n:
        print b
        a, b = b, a+b

def fib_list(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

if __name__ == '__main__':
    n = 100
    fib_printer(n)
