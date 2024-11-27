from random import randint
n = int(input('Введите кол-во элементов '))
s = [randint(1, 100) for _ in range(n)]
print('Массив')
print(*s)
c=0
d = 0
for i in s:
    if c%2!=0:
        i*=-1
        d+=i
    else:
        d+=i   
    print(d) 
    c+=1
print(f'Знакопеременная сумма {d}')