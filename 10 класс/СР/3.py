def f(n):
    return g(n - 1)


def g(n):
    if n < 10:
        return n
    return g(n - 2) + 1


count = 0
for n in range(1, 101):
    if (f(n) ** 0.5) % 1 == 0:
        count += 1
print(count)
