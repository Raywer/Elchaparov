a = int(input('Возраст Антона: '))
b = int(input('Возраст Бориса: '))
v = int(input('Возраст Виктора: '))
if a>b and a>v:
    print('Антон старше всех')
elif b>a and b>v:
    print('Борис старше всех')
elif v>a and v>b:
    print('Виктор старше всех')
elif a == b>v:
    print('Антон и Борис старше Виктора')
elif v == b > a:
    print('Виктор и Борис старше Антона')
elif a == v > b:
    print('Антон и Виктор старше бориса')


