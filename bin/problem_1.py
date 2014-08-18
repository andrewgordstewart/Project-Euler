li = range(1000)[::3]
li.extend(range(1000)[::5])

for i in range(1000)[::15]:
    li.remove(i)

x = 0
for i in li:
    x += i

print x
