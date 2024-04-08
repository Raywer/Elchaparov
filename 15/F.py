from random import randint

n = int(input('Введите кол-во элементов '))
s = [randint(-100, 100) for _ in range(n)]
print('Массив:')
print(*s)
c = []
p = 0
for i in s:
    if i > 0:
        c.append(i)
        p+=1
for i in s:
    if i < 0:
        c.append(i)
for i in s:
    if i == 0:
        c.append(i)
print('Результат:')
print(*c)
print(f'Кол-во положительных элементов: {p}')
