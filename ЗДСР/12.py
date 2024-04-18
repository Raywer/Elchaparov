from random import randint
n = int(input('Введите кол-во элементов '))
s = [5]
s += [randint(1, 5) for _ in range(n-1)]
d = n
i = n
print('Массив:')
print(*s)
while s[d-1] != 5 and i >= 0:
    i -= 1
    d = i

print(d)
