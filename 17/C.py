s = input(' '.join).split(' ')
t = 0
m = 0
l = ''
f = False

for i in s:
    for j in i:
        t += 1
    if m < t:
        m = t
        l = i
    t = 0
print(f'Самое длинное слово: {l}, длина {m}')
