import random as rd
zoz = []
for i in range(5):
    y = rd.randrange(0,20)
    zoz.append(y)
print(zoz)

for i in range(len(zoz)-1):
    for i in range(0,len(zoz)-1):
        if zoz[i] > zoz[(i+1)]:
            zoz[i],zoz[i+1]= zoz[i+1],zoz[i]
print(zoz)