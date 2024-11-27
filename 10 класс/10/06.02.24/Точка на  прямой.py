def line(s,t):
    x1,x2=map(int,t.split(';'))
    s1,s2=map(str,s.split('+'))
    if s1!='x':
        s1 = (s1.replace('x',''))
    a=(int(s2)/int(s1))
    if x1<a<x2:
        print('true')
    else:
        print('false')

line("1x+6", "1;7")

