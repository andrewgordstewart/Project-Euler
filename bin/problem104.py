from proj_eul.math_tools.fibo import fib_gen as _fib_generator

from proj_eul.string_tools.pandigital import is_pandigital as _is_pandigital

def _fib_generator_mod_10(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield b
        a, b = b, (a+b) % 10**9
        count += 1

n = 10**5
f = _fib_generator(n)
false_f = _fib_generator_mod_10(n)

counter = 0
# print _is_pandigital(false_f.next())


counter, a = 0, 0
while not _is_pandigital(a):
    counter += 1
    a = false_f.next()
print counter, a


b, counter = 0, 0
while not _is_pandigital(b):
    counter += 1
    b = str(f.next())[0:9]
print counter, b

f = _fib_generator(n)
false_f = _fib_generator_mod_10(n)


a, b, counter = 0, 0, 0
try:
    while not (_is_pandigital(str(a))
               and _is_pandigital(str(b))):
        a, b = f.next, false_f.next()
        counter += 1
except StopIteration:
    print counter
