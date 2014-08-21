# insert i into the kth digit of n
# # numbers are thoght to have infinitely many
# # leading 0's, so insert(1, 2, 0) returns 100
def insert(i, digit, number):
    if i not in range(10):
        raise ValueError
    N = 10 ** digit
    return 10*N*(number/N) + N*i + (number - N*(number/N))

if __name__ == '__main__':
    print insert(1, 2, 0)

