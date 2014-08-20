def is_perm(a, b):
    s1 = list(str(a))
    s2 = list(str(b))

    for i in s1:
        if i in s2: s2.remove(i)
    if s2 == []:
        return True
    else:
        return False
