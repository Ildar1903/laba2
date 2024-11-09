from datetime import date

 
def vozrast():
    today = date.today()
    print(f'Сегодня {today.day}.{today.month}.{today.year}')
    dr = input('Введите дату рождения в формате день.месяц.год цифрами:\n')
    if dr.replace('.','',2).isdigit():
        drlist = dr.split('.',2)
        if int(drlist[0])<=31 and int(drlist[0])>0 and int(drlist[1])<=12 and int(drlist[1])>0 and int(drlist[2])<int(today.year):
            age = int(today.year) - int(drlist[2])
            if int(today.month) < int(drlist[1]):
                age -= 1
            elif (int(today.month) == int(drlist[1])) and (int(today.day) < int(drlist[0])):
                age -= 1
            print(f'Сегодня Вам {age}')
            return age
        else:
            print('Вы ввели дату неверно! Перезапустите и введите дату правильно')
    else:
        print('Вы ввели дату неверно! Перезапустите и введите дату правильно')
   
vozrast()

    