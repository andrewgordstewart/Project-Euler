def is_palindrome(li):
    if isinstance(li, int) or isinstance(li, long):
        li = str(li)
    tag = True
    for i in range(len(li)/2+1):
        if li[i] != li[-i-1]:
            tag = False
    return tag


def lychrel_check(n, counter):
    if counter == 50:
        # print 'hit the max'
        return True
    s = str(n)
    rev_s = s[::-1]
    x = int(s)
    x += int(rev_s)
    if is_palindrome(x):
        return False
    else:
        return lychrel_check(x, counter+1)


