from random import randint

s = [randint(2, 100) for _ in range(5)]
print('Массив:')
print(*s)
p = []
for j in s:
    k = 2
    while k * k <= j and j % k != 0:
        k += 1
    if k * k > j and j != 1:
        p.append(j)
print('Простые числа:')
print(*p)
d = sum(i for i in p)
sr = None if len(p) == 0 else d / len(p)
print(f'Среднее арифмитическое {sr}')