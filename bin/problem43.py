# WARNING!!! factorial runtime!!!!
def pandigital_numbers(list_of_digits):
    if len(list_of_digits) == 0:
        return []
    elif len(list_of_digits) == 1:
        return [str(list_of_digits[0])]

    result = []

    for i in list_of_digits:

        li = list_of_digits[:]
        li.remove(i)
        sub_numbers = pandigital_numbers(li)

        for j in sub_numbers:
            result.append(str(i) + str(j))
    return result


print len(pandigital_numbers([0, 1, 2, 3, 4, 5, 6, 7, 8]))
