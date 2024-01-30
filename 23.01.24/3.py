n = int(input('Введите N: \n'))
for i in range(1,n+1):
    c = i**2
    if c%(10**(len(str(i)))) == i:
        print(f'{i}*{i}={c}')