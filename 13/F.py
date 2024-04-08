from random import randint
s = [randint(150, 180) for _ in range(30)]
d = 0 
for i in s:
    if i>170:
        d+=1
if d>=5:
    print('Yes')
else:
    print('No')