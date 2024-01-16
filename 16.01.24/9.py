a = int(input())
b = str(a)[0:1]
c = str(a)[1:2]
m = str(a)[2:3]
sum1 = int(b)+int(c)
sum2 = int(c)+int(m)
if sum1>sum2:
    print(str(sum1)+str(sum2))
else:
    print(int(str(sum2)+str(sum1)))
