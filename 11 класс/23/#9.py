a=[0]*103
a[43]=2
for i in range(43,5,-1):
    if i-8>=5:
        a[i-8]+=a[i]
    if i//2>=5:
        a[i//2]+=a[i]
print(a[5])