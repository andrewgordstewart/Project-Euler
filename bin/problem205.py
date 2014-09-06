from copy import copy as copy


peters_die = {i:1 for i in range(1, 4+1)}
# print peters_die
colins_die = {i:1 for i in range(1, 6+1)}

# print colins_die

def new_roll(dice, original_die):
    new_dice = {}
    for i in dice:
        for j in original_die:
            new_dice[i+j] = 0
    for i in dice:
        for j in original_die:
            new_dice[i+j] += 1
    return new_dice

peters_roll = peters_die
for i in range(8):
    peters_roll = new_roll(peters_roll, peters_die)



colins_roll = colins_die
for i in range(5):
    colins_roll = new_roll(colins_roll, colins_die)

print 'Peter\'s roll: %r' % peters_roll
print '\n'
print 'Colin\'s roll: %r' % colins_roll



# print sum(x for x in peters_probs)
# print peters_probs


peters_sum = sum(peters_roll[i] for i in peters_roll)
colins_sum = sum(colins_roll[i] for i in colins_roll)

peters_probs = {i:float(peters_roll[i])/peters_sum for i in peters_roll}
colins_probs = {i:float(colins_roll[i])/colins_sum for i in colins_roll}

print sum(peters_probs[i] for i in peters_probs)
print sum(colins_probs[i] for i in colins_probs)


peter_beats_colin = 0
check_sum = 0
for p in peters_probs:
    for c in colins_probs:
        if p > c:
            # print p, c
            peter_beats_colin += peters_probs[p]*colins_probs[c]
        check_sum += peters_probs[p]*colins_probs[c]

print peter_beats_colin, check_sum

