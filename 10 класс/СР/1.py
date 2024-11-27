import sys
sys.setrecursionlimit(2025)
def f(n):
    if n < 11:
        return n
    return n + f(n - 1)


print(f(2024) - f(2021))
