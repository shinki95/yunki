# guess the number
import random
numbers = []
for x in range(1,21):
    numbers.append(x)
goal = random.choice(numbers)
count = 0
num = 0
name = input("What is your name: ")
print(name)
while num != goal:
    num = int(input())
    if num > goal:
        print("Your guess is too high")
        count =+ 1
    elif num < goal:
        print("Your guess is too low")
        count =+ 1
    else:
        print("Good job")
        print(count)
    
