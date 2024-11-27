from random import randint

n = int(input('Введите кол-во элементов '))
s = [randint(0, 6) for _ in range(n)]
print('Массив:')
print(*s)
c = list(reversed(s[0:n//2])) + list(reversed(s[n//2:]))
print('Результат:')
print(*c)
