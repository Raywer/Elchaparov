a = int(input('Введите отработанные часы: '))
b = int(input('Введите траты на одежду: '))
v = int(input('Введите траты на еду: '))
p = ((250*a)//(2**3))+a
if p>=b+v:
    print('Часов хватает. Можно отдохнуть.')
else:
    print('Часов не хватает. Придётся работать больше!')