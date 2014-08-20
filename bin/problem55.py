from proj_eul.string_tools.palindrome import lychrel_check as _lychrel_check

lychrel_numbers = []

n = 10000
for i in range(n):
    if _lychrel_check(i, 0):
        lychrel_numbers.append(i)

print len(lychrel_numbers)
