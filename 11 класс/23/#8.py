a=[0]*21
a[12]=18
for i in range(12,20):
    if i+1<=20:
        a[i+1]+=a[i]
    if i+3<=20:
        a[i+3]+=a[i]
    if i*2<=20:
        a[i*2]+=a[i]
print(a[20])
