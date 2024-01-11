a,b,c,d,e = map(int, input('Введите пять целых чисел: ').split())
if a>b and a>c and a>d and a>e:
    m = a
elif b>c and b>d and b>e:
    m = b
elif c>d and c>e:
    m = c
elif d>e:
    m = d
else:
    m = e
print(f'Максимальное число {m}')