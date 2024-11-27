from random import randint
n = int(input('Введите кол-во элементов '))
s = [randint(1, 5) for _ in range(n)]
print('Массив:')
print(*s)
for i in range(0, n, 2):
    d = s[i+1]
    f = s[i]
    s[i] = d
    s[i+1] = f
print(*s)