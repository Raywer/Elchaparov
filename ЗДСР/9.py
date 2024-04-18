from random import randint
s = [randint(180, 200) for _ in range(35)]
print('Массив:')
print(*s)
p = 0
c = 0
for i in s:
    if i > p:
        p = i
for i in s:
    if p == i:
        c += 1
print(p)
print(c)
