def voo(n):
    while n>0:
        if n>=1000:
            n-=1000
            print('M', end='')
        elif n>=500:
            n-=500
            print('D', end='')
        elif n>=100:
            n-=100
            print('C', end='')
        elif n>=50:
            n-=50
            print('L', end='')
        elif n>=10:
            n-=10
            print('X', end='')
        elif n == 9:
            n-=9
            print('IX', end='')
        elif n>=5:
            n-=5
            print('V', end='')
        elif n>=1:
            n-=1
            print('I', end='')
voo(int(input()))