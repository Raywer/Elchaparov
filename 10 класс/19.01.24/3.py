n = int(input('Введите число N:\n'))
s = [1,1]
p = 0
f = 0
o = 2
while f<n:
    f = s[p]+s[p+1]
    s.append(f)
    p += 1
    o+=f
    if s[p+1]+f>=n:
        break
print(o)