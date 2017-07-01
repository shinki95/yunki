for j in range(4):
    for i in range(5):
        print('*', end='')
    print(' ')

for j in range(5):
    for i in range(j+1):
        print('*', end='')
    print(' ')

for j in range(5):
    for i in range(5-j):
        print('*', end='')
    print(' ')

for j in range(5):
    for i in range(4-j):
        print(' ', end='')
    for i in range(j+1):
        print('*', end='')
    print(' ')


for j in range(5):
    for i in range(j):
        print(' ', end='')
    for i in range(5-j):
        print('*',end='')
    print(' ')

for j in range(5):
    for i in range(4-j):
        print(' ', end='')
    for i in range(2*(j+1)-1):
        print('*', end='')
    print(' ')

for j in range(5):
    for i in range(j):
        print(' ', end='')
    for i in range(2*(5-j)-1):
        print('*', end='')
    print(' ')
