def f(n):
    if n == 0:
        return 1
    elif n > 0 and n % 2 == 1:
        return f(n // 100) * (n % 10)
    return f(n // 100)


count = 0
for n in range(1, 6 * 10 ** 9):
    if f(n) == 21:
        print(n)
        count += 1
print(count)
