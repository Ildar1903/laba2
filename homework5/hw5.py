def get_number():
    for num in range(30):
        if num % 2 != 0:  
            yield num

gen = get_number()
    
nechet = list(gen)
    
if len(nechet) >= 5:
    print(f"Первое нечетное число: {nechet[0]}")
    print(f"Пятое нечетное число: {nechet[4]}")
    print(f"Последнее нечетное число: {nechet[-1]}")
else:
    print("Недостаточно чисел в диапазоне.")
