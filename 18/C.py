s = input()
list_dig = []
list_zn = []
p = 0
for i in range(len(s)):
    if not (s[i].isdigit()):
        list_dig.append(int(s[p:i]))
        p = i + 1
        list_zn.append(s[i])
list_dig.append(int(s[p:]))

while '*' in list_zn or '/' in list_zn:
    pdiv = list_zn.index('/') if '/' in list_zn else len(list_zn)+100
    pdiv = list_zn.index('*') if '*' in list_zn else len(list_zn) + 100