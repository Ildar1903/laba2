import random

def kratnost():
    while True:
        try:
            x = int(input("Введите цифру X для поиска кратных чисел: "))
            if x <= 0 and x >= 10:
                print("Ошибка: X должно быть цифрой!")
                continue
            break
        except ValueError:
            print("Ошибка: введите цифру!")
    
    kratn = list(filter(lambda num: num % x == 0, nlist))
    
    if kratn:
        print(f"Числа, кратные {x}: {kratn}")
    else:
        print(f"Нет чисел, кратных {x}.")

nlist = [random.randint(0, 200) for _ in range(random.randint(10, 20))]
print("Список чисел:", nlist)

kratnost()

