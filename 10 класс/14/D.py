from random import randint

s = [randint(1, 5) for _ in range(5)]
print('Массив:')
print(*s)
min = s[0]
max = s[0]
min_i = 0
max_i = 0
for i in range(5):
    if s[i] > max:
        max = s[i]
        max_i = i
    if s[i] < min:
        min = s[i]
        min_i = i
print(f'Минимальный элемент: A[{min_i+1}]={min}')
print(f'Максимальный элемент: A[{max_i+1}]={max}')