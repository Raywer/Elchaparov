from random import randint

n = int(input('Введите кол-во элементов '))
s = [randint(0, 100) for _ in range(n)]
print('Массив A:')
print(*s)


def ordinary(i):
    if i % 2 == 0:
        return i == 2
    d = 3
    while d * d <= i and i % d != 0:
        d += 2
    return d * d > i


d = [i for i in s if ordinary(i)]
print('Массив B:')
print(*d)
