from random import randint

s = [randint(1, 5) for _ in range(7)]
print('Массив:')
print(*s)
max = s[0]
c = 0
for i in range(7):
    if s[i] >= max:
        max = s[i]
        c += 1
print(f'Максимальное значение {max}')
print(f'Кол-во элементов {c}')