from random import randint
s = [1, 3, 4, 1, 3, 5]
print('Массив:')
print(*s)
p = 0
c = 0
for i in s:
    if i % 2 != 0:
        p += 1
        c = max(p, c)
    else:
        p = 0
print(c)

