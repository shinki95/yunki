list_1 = [2, 4, 7, 9]
list_2 = [8, 6, 4, 2]
K = 10
for x in list_1:
    for y in list_2:
        if x + y == K:
            print(x, y)
