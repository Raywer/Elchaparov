a,b,c = map(int, input('Введите три числа: ').split())
if a == b and a == c:
    print('Все числа одинаковые.')
elif a == b or a == c or b == c:
    print('Два числа одинаковые.')
else:
    print('Нет одинаковых чисел.')