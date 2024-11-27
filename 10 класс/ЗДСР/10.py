from random import randint
import math
n = int(input('Введите кол-во элементов '))
s = [randint(-100, 100) for _ in range(n)]
print('Массив:')
print(*s)
f = 0
for i in range(0, n):
    if f < abs(s[i]):
        f = s[i]*-1
print(f)
