a,b = map(int, input('Введите два числа:\n').split())
if abs(a)>abs(b):
    s = b
else:
    s = a
c = 0
while s!=0:
    if a<0 and b<0:
        c+=b
        s+=1
    elif a<0:
        c+=b
        s+=1
    else:
        c+=b
        s-=1
if a<0 and b<0:
    c = abs(c)
print(f'{a}*{b}={c}')

