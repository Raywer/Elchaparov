from random import randint
n = int(input('Введите кол-во элементов '))
s = [randint(1, 100) for _ in range(n)]
print('Массив')
print(*s)
for i in s:
