from proj_eul.prime_tools.factor import proper_factors as _factors
# insert 'char' into 'position'-th position of 'string'
def insert(char, position, string):
    if position > len(string):
        raise ValueError

    return string[:position] + char + string[position:]


def digits(i, j, num):
    if (i > j
        or not isinstance(i, int)
        or not isinstance(j, int)
        or i < 0
        or j < 0
        ):
        raise ValueError
    s = str(num)
    sub_string = s[i-1:j]
    return int(sub_string)




if __name__ == '__main__':
    # print insert(1, 2, 0)
    # digits(2,2,3)
    # print digits(1, 2, 123456789)
    # print insert('0', 0, 'abcd')
    print is_abundant(28)

    print is_abundant(12)
