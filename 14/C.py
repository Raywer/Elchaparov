from random import randint
n = int(input('Введите кол-во элементов '))
s = [randint(1, 5) for _ in range(n)]
print('Массив:')
print(*s)
d = []
for i in range(n):
    for j in range(i+1, n):
        if s[i] == s[j]:
            if not(i in d):
                d.append(s[i])

if d:
    print('Есть:', ', '.join(str(i) for i in d))
else:
    print('Нет')


