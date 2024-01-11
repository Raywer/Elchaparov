import random
a = random.randint(1,6)
b = random.randint(1,6)
c = random.randint(1,6)
print(f'Выпало очков: \n{a} {b} {c}')
print(f'Число {a}{b}{c}')
d = str(a)+str(b)+str(c)
print(f'Его квадрат {int(d)**2}')
