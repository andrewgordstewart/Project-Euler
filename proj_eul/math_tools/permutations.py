

def is_perm(a, b):
    s1 = list(str(a))
    s2 = list(str(b))

    for i in s1:
        if i in s2: s2.remove(i)
    if s2 == []:
        return True
    else:
        return False

def cyclic_permute(n):
    s = str(n)
    li = [s[i] for i in range(1, len(s))]
    li.append(s[0])
    result = ''
    for char in li: result += char
    return int(result)

def min_cyclic_perm(n):
    minn = n
    x = n
    enter = True
    while x != n or enter:
        enter = False
        x = cyclic_permute(x)
        minn = min(minn, x)
    return minn

if __name__ == '__main__':
    print cyclic_permute(11)
    print min_cyclic_perm(21), min_cyclic_perm(24321)
    print min_cyclic_perm(14)
