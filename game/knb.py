import random
def play(p1, p2):
    if p1 == "камень":
        if p2 == "камень":
            return "Ничья"
        elif p2 == "бумага":
            return "Вы проиграли"
        elif p2 == "ножницы":
            return "Вы выиграли"
        else:
            raise ValueError(f"Неверный выбор: {p2}")
    elif p1 == "бумага":
        if p2 == "камень":
            return "Вы выиграли"
        elif p2 == "бумага":
            return "Ничья"
        elif p2 == "ножницы":
            return "Вы проиграли"
        else:
            raise ValueError(f"Неверный выбор: {p2}")
    elif p1 == "ножницы":
        if p2 == "камень":
            return "Вы проиграли"
        elif p2 == "бумага":
            return "Вы выиграли"
        elif p2 == "ножницы":
            return "Ничья"
        else:
            raise ValueError(f"Неверный выбор: {p2}")
    else:
        raise ValueError(f"Неверный выбор: {p1}")

listv=["камень", "ножницы", "бумага"]
while True:
    p_in=input('Выберите цифру, чтобы сделать ход: камень(1), ножницы(2), бумага(3), или введите q для выхода\n')
    p2=random.choice(listv)
    if p_in.isdigit():
        p1=listv[int(p_in)-1]
        print(f'Ваш выбор: {p1}, выбор компьютера: {p2}')    
        print(play(p1, p2))
    if p_in == 'q':
        break