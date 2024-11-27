for i in range(100,1000):
    a = (i//100)**3
    b = (((i%100)-(i%10))//10)**3
    c = (i%10)**3
    if i==a+b+c:
        print(i)