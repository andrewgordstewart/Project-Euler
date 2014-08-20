li = set()

n = 100
for i in range(2, n+1):
    for j in range(2, n+1):
        li.add(i**j)

print len(li)
