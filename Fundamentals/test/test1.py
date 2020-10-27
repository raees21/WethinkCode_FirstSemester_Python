import random
obstacles = []

for i in range(40):
    obsi = []
    for j in range(20):
        if j == 10:
            obsi.append(1)
        else:
            obsi.append(random.randint(0, 1))
    obstacles.append(obsi)

print(obstacles)
print (len(obstacles))


a = []
for i in range(40):
    obsi = []
    for j in range(20):
        obsi.append(random.randint(0, 1))
    a.append(obsi)