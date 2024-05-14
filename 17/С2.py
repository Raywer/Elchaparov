s = input(' '.join).split('and')
s1 = ''
for i in range(len(s)-1):
    d = s[i]+'&'
    s1 += d
s1 += s[len(s)-1]
print(s1)