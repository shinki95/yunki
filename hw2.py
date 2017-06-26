import random
list_1 = []
for x in range(1,21):
    list_1.append(x)
k = int(input())
for a in list_1:
    b = k-a
    if b in list_1:
        print (a,b)



