import random

a, b = map(int, input('Введите границы диапазона: ').split())
s = []
for i in range(5):
    d = random.randint(a, b)
    s.append(d)
print(*s)
