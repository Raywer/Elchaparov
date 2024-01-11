import random
a = random.randint(100,999)
print(f'Получено число {a}')
print(f'сотни: {str(a)[0:1]}')
print(f'десятки: {str(a)[1:2]}')
print(f'еденицы: {str(a)[2:3]}')