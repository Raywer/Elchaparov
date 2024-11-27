import sys

sys.setrecursionlimit(8 ** 10 + 1)
k = 0


def f(n):
    if n == 0:
        return 0
    elif n > 0 and n % 2 == 0:
        return f(n // 8) + n % 8
    elif n > 0 and n % 2 != 0:
        return f(n // 8)


for n in range(8**4, 8 **5 + 1):
    if f(n) == 2:
        k += 1
print(k)
