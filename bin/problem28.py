def spiral(n): # n = floor(size/2)
    step = 2
    x = 1
    next_number = 3
    for i in range(n):
        x += next_number
        x += next_number + step
        x += next_number + 2*step
        x += next_number + 3*step

        next_number += step * 4 + 2
        step += 2

    return x


n = 500
print spiral(n)
