# guess the number
import random
numbers = list(range(1,21))
goal = random.choice(numbers)
count = 0
num = 0
name = input("What is your name: ")
print(name, "Guess the number!")
while num != goal:
    num = int(input())
    count += 1
    if num > goal:
        print("Your guess is too high")
    elif num < goal:
        print("Your guess is too low")
    else:
        print("Good job")
        print("Count:", count)   