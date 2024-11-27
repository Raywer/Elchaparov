a,b=[int(i) for i in input('Введите границы \n').split()]
c=0
s=''
for i in range(a,b+1):
    c=0
    for j in range(2,i):
        if i % j == 0:
            c+=1
        if c>2:
            break
    if c == 2:
        s+=str(i)+' '
print(', '.join(i for i in s.split()))