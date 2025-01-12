a=[0]*14
a[1]=1
for i in range(1,13):
    if i+1<=13:
        a[i+1]+=a[i]
    if i+2<=13:
        a[i+2]+=a[i]
    if i*4<=13:
        a[i*4]+=a[i]
print(a[13])