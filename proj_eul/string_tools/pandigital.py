def is_pandigital(n):
    li = [c for c in str(s)]
    length = len(c)

    for i in range(1, n+1):
        if not i in c:
            return False
        c.remove(i)

    if c == []:
        return True
    else:
        return False

