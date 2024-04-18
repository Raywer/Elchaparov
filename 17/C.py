s = input()
t = 0
m = 0
f = False

for i in range(len(s)):
    if s[i] != ' ':
        t += 1
    elif s[i] == ' ':
        if t > m:
            m = t
        t = 0
print(m)