from proj_eul.string_tools.tools import insert as _insert

def is_pandigital(n, digits = 9):
    li = [i for i in str(n)]
    # print li, len(li)
    for i in range(1, digits + 1):
        # print i, str(i) in li
        if not str(i) in li:
            return False
    return True

def pandigitals(digits):
    if digits == 1:
        yield '1'
    elif digits == 10:
        panner = pandigitals(9)
        for small_pan in panner:
            for position in range(10):
                yield _insert('0', position, small_pan)
    else:
        panner = pandigitals(digits - 1)
        for small_pan in panner:
            for position in range(digits):
                yield _insert(str(digits), position, small_pan)
              # insert digit into the jth position of i


if __name__ == '__main__':
    # print is_pandigital(1234)
    # print is_pandigital(1324)
    # print is_pandigital(1225)
    # print is_pandigital(12)

    # p = pandigitals(10)
    # print p.next()

    print is_pandigital(1234, 4)
