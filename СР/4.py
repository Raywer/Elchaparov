def f(n):
    if n < 2:
        return n
    return f(n // 2) + f(n % 2)


# count = 0
# for n in range(1, 100000):
#     if f(n) == 27:
#         print(n)
#         count += 1
# print(count)
q = 1
for i in range(1,28):
    q = q*i
for j in range(1,28-27)