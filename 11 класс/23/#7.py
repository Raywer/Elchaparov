a=[0]*31
a[12]=20
for i in range(12,30):
    if i+1<=30:
        a[i+1]+=a[i]
    if i*2<=30:
        a[i*2]+=a[i]
print(a[30])