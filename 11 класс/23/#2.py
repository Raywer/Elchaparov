a=[0]*155
a[5]=1
for i in range(5,154):
    if i+1<=154:
        a[i+1]+=a[i]
    if i*2<=154:
        a[i*2]+=a[i]
    if i**2<=154:
        a[i**2]+=a[i]
print(a[154])