# a vector [a, b, c, d, e, f, g, h] will represent 'a' 200 pence coins,
# 'b' 100 pence coins, 'c' 50p, 'd' 20p, 'e' 10p, 'f' 5p, 'g' 2p and
# 'h' 1p

configs = set([1,0,0,0,0,0,0,0])

def exchange(coinlist):
    set_of_changes = set()
    if coinlist[0] > 0: # 200 = 100 + 100
        temp = coinlist[:]
        temp[0] -= 1
        temp[1] += 2
        set_of_changes.add(temp)

    if coinlist[1] > 0: # 100 = 50 + 50 = 20 + 20 + 20 + 20 + 20
        temp = coinlist[:]
        temp[1] -= 1
        temp[2] += 2
        set_of_changes.add(temp)

        temp = coinlist[:]
        temp[1] -= 1
        temp[3] += 5
        set_of_changes.add(temp)

    if coinlist[2] > 0: # 50 = 20 + 20 + 10
        temp = coinlist[:]
        temp[2] -= 1
        temp[3] += 2
        temp[4] += 1
        set_of_changes.add(temp)

    if coinlist[3] > 0: # 20 = 10 + 10
        temp = coinlist[:]
        temp[3] -= 1
        temp[4] += 2
        set_of_changes.add(temp)

    if coinlist[4] > 0: # 10 = 5 + 5 = 2 + 2 + 2 + 2 + 2
        temp = coinlist[:]
        temp[4] -= 1
        temp[5] += 2
        set_of_changes.add(temp)

        temp = coinlist[:]
        temp[4] -= 1
        temp[6] += 5
        set_of_changes.add(temp)

    if coinlist[5] > 0: # 5 = 2 + 2 + 1
        temp = coinlist[:]
        temp[5] -= 1
        temp[6] += 2
        temp[7] += 1
        set_of_changes.add(temp)

    if coinlist[6] > 0: # 2 = 1 + 1
        temp = coinlist[:]
        temp[6] -= 1
        temp[7] += 2
        set_of_changes.add(temp)

    if coinlist[7] > 0:
        set_of_changes.add(coinlist)

    return set_of_changes
