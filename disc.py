flag1 = 'Y'
while flag1 == 'Y':
    a, b, c, d, x1, x2 = input('Введите коэффицент a: '), input('Введите коэффицент b: '), input('Введите коэффицент c: '), 0, 0, 0
    if a.isdigit() and b.isdigit() and c.isdigit():
        d = float(b) ** 2 - 4 * float(a) * float(c)
        if d == 0:
            x1 = - float(b) / (2 * float(a))
            print("x1 =", x1)
        elif d < 0:
            print("Корней нет")
        else:
            x1 = (-float(b) + (d ** (1 / 2)))
            x2 = (-float(b) - (d ** (1 / 2)))
            print(f'x1 = {x1}, x2 = {x2}')
    else:
        print("Неверный ввод.")
    flag1 = input("Хотите продолжить? Y/N: ")