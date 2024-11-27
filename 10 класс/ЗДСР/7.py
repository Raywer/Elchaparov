from random import randint
s = [randint(1, 20) for _ in range(35)]
print('Массив:')
print(*s)
p = 0
c = 0
for i in range(len(s)):
    if s[i]  0:
        p += 1
        c = max(p, c)
    else:
        p = 0
print(c)