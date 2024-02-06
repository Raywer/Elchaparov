def boo(a):
    dlinna = 10**(len(str(a))-1)
    for i in range(len(str(a))):
        print(int(a//dlinna))
        a%=dlinna
        dlinna/=10
boo(int(input()))