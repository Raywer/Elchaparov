a,b = map(int, input('Введите два целых числа:\n').split())
n = a
print(f'{n}*{n}={n ** 2}')
while n < b:
    p = n**2
    n+=1
    print(f'{n}*{n}={n**2}')

