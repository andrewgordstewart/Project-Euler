from proj_eul.prime_tools.factor import is_abundant as _is_abundant

n = 28123
abundant_numbers = []
for i in range(1, n):
    if _is_abundant(i):
        abundant_numbers.append(i)

print len(abundant_numbers)

abundant_sums = set()
for i in abundant_numbers:
    for j in abundant_numbers:
        abundant_sums.add(i+j)

x = sum(i for i in set(range(1,n)) - abundant_sums)
print x

