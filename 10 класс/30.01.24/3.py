n = int(input())
for i in range(1,n+1):
    t = False
    for j in str(i):
        j=int(j)
        if j!=0 and i%j==0:
            t = True
        else:
            t = False
    if t:
        print(i)