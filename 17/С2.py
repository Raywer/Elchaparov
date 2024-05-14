s = input('')
c = input('Что меняем: ')
n = input('На что меняем: ')
s1 = s.split(c)
s2 = ''
for i in range(len(s1)-1):
    d = s1[i]+n
    s2 += d
s2 += s1[len(s1)-1]
print(s2)