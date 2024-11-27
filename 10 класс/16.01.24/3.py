a = int(input(f'Введите номер месяца:\n'))
if a < 3 and a > 0 or a == 12:
    print('Зима.')
elif a > 2 and a < 6:
    print('Весна.')
elif a > 5 and a < 9:
    print('Лето.')
elif a > 8 and a < 12:
    print('Осень.')
else:
    print('Неверный номер месяца.')