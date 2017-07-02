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
    for i in range(num):
        print(' '*(num-i-1), end="")
        print('*'*(2*i+1))

x = int(input())
print_triangle_3(x)

def print_triangle_3(num):
    for i in range(num):
        print(' '*(num-i-1), end="")
        print('*'*(2*i+1))

x = int(input())
print_triangle_3(x)

def print_triangle_4(num):
    for i in range(num):
        print(' '*i, end="")
        print('*'*(2*(num-i)-1))

x = int(input())
print_triangle_4(x)

def print_triangle_5(num):
    for i in range(num):
        print(' '*(num-i-1), end="")
        print('*'*(2*i+1))

    for i in range(num):
        print(' '*(i+1), end="")
        print('*'*(2*(num-i)-3))

x = int(input())
print_triangle_5(x)

def print_triangle_5(num):
    for i in range(num):
        print(' '*(num-i-1), end="")
        print('*'*(2*i+1))

    for i in range(num):
        print(' '*(i+1), end="")
        print('*'*(2*(num-i)-3))

x = int(input())
print_triangle_5(x)

def print_triangle_5(num):
    for i in range(num):
        print(' '*(num-i-1), end="")
        print('*'*(2*i+1))

    for i in range(num):
        print(' '*(i+1), end="")
        print('*'*(2*(num-i)-3))

x = int(input())
print_triangle_5(x)

def print_triangle_6(num, c='#'):
    for i in range(num):
        spc = i * 2 - 1
        if spc >= num - 1:
            spc = num - spc % n - 4
        if spc < 1:
            print(c.center(num))
        else:
            print((c + spc * '*' + c).center(num))

print_triangle_6(int(input("Input an odd integer: ")))