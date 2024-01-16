a = int(input('Введите возраст: '))
if a > 10 and a < 15:
    print(f'Вам {a} лет')
elif a%10==1 and a<100:
    print(f'Вам {a} год')
elif a % 10 > 1 and a%10 < 5:
    print(f'Вам {a} года')
elif a%10>4:
    print(f'Вам {a} лет')
elif a > 99:
    if a == 100:
        print(f'Вам {a} лет')
    elif a == 101:
        print(f'Вам {a} год')
    elif a%100 > 1 and a%100<5:
        print(f'Вам {a} года')
    elif a>104:
        print(f'Вам {a} лет')