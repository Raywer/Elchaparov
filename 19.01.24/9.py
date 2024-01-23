x = int(input())
y = int(input())
p = int(input())
l = 0
while x<y:
    x = x+((x/100)*p)
    x = int(x)
    l+=1
print(l)
