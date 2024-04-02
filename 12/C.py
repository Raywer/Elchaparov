x, d = map(int, input('Введите X и D:\n ').split())
print('Массив:')
s = []
for i in range(4):
    x += d
for i in range(5):
    s.append(x)
    x -= d
print(' '.join(str(i) for i in s))
