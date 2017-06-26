# guess the number
import random
numbers = []
for x in range(1,21):
    numbers.append(x)
goal = random.choice(numbers)
num = 0
while num != goal:
    num = int(input())
    if num > goal:
        print("Your guess is too high")
    elif num < goal:
        print("Your guess is too low")
    else:
        print("Good job")
    
