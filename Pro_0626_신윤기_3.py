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

def print_triangle_1(num):
    for i in range(num+1):
        print('*' * i)

x = int(input())
print_triangle_1(x)

def print_triangle_2(num):
    for i in range(num+1):
        print(' '*i, end=" ")
        print('*'*(num-i))

x = int(input())
print_triangle_2(x)

def print_triangle_3(num):
    for i in range(num+1):
        print(' '*i, end=" ")
        print('*'*(num-i))

x = int(input())
print_triangle_2(x)