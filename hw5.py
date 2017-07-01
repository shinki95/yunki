# 식사/뒷풀이 장소 고르기 프로그램
import random

list_1 = []
list_2 = []

def meal():
    a = input("식당: ")
    b = input("음식: ")
    list_1.append((a,b))
    if input(" ") == "End":
        drink()
    
def drink():
    c = input("장소: ")
    d = input("종류: ")
    list_2.append((c,d))
    if input(" ") == "End": 
        random_choice()

def random_choice():
    list_3 = list_1.extend(list_2)
    if input("랜덤뽑기를 하시겠어요?: ") == "Y":
        print(random.choice(list_1))
    elif input("랜덤뽑기를 하시겠어요?: ") == "N":
        pass




if input("원하시는 것을 선택하세요: ") == '식사':
    meal()

elif input("원하시는 것을 선택하세요: ") == '뒷풀이':
    drink()




