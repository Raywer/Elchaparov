def boo(n):
    if n == 0 or n == 1:
        return 1
    count = 0
    for i in range(1,n):
        count += boo(n - i)
    return count

n = int(input('Введите натуральное число \n'))
count = boo(n)
print(f'Количество разложений: {count}')