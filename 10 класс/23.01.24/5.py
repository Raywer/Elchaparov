s = 0
c = 0
for i in range(100,1000):
    s = (i//100)+(i%10)+((i%100)-i%10)
    if 0<s<27:
        c+=1
print(c)
