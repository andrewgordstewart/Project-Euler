from proj_eul.string_tools.tools import digits as _digits

def wierd_prime_test(n):
    if (_digits(2, 4, n) % 2 == 0
        and _digits(3, 5, n) % 3 == 0
        and _digits(4, 6, n) % 5 == 0
        and _digits(5, 7, n) % 7 == 0
        and _digits(6, 8, n) % 11 == 0
        and _digits(7, 9, n) % 13 == 0
        and _digits(8, 10, n) % 17 == 0
        ):
        return True
    else:
        return False

# print wierd_prime_test(1406357289)

from proj_eul.string_tools.pandigital import pandigitals as _panner

p = _panner(10)

pan_sum = 0
for s in p:
    if wierd_prime_test(int(s)):
        pan_sum += int(s)

print pan_sum
