a,b,c = map(int, input('Введите три целых числа: ').split())
if a>b and a>c:
    m = a
elif b>c and b>a:
    m = b
else:
    m = c
print(f'Максимальное число {m}')