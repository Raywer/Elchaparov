a,b=[int(i) for i in input('Введите границы \n').split()]
for i in range(a,b+1):
    d = True
    for j in range(2,i):
        if i % j == 0:
            d = False
    if d:
        print(i,end=' ')