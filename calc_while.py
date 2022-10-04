import math
action = ''
while action != 'Выход':
    action = input('''Вас приветствует калькулятор. Выберите нужную операцию. \n"+" - сложение \n"-" - вычитание
                    \n"*" - произведение \n"//" - деление на цело \n"/" - деление \n"%" - остаток от деления
                    \n"~" - округление \n"c~" - округление вверх \n"f~" - округление вниз \n"||" - модуль числа
                    \n"√" - квадратный корень числа \n"^" - возведение числа в степень \n"log" - натуральный логорифм числа
                    \n"log10" - десятичный логарифм числа \n"log(x,b)" - логарифм числа по основанию \n"fact" - факториал числа
                    \n"tab" - таблица степеней \n"Выход" - для завершения программы \n''')
    if action == '+':
        n_1 = float(input('Введите первое число\n'))
        n_2 = float(input('Введите второе число\n'))
        print('Результат равен ', n_1 + n_2)
    elif action == '-':
        n_1 = float(input('Введите первое число\n'))
        n_2 = float(input('Введите второе число\n'))
        print('Результат равен ', n_1 - n_2)
    elif action == '*':
        n_1 = float(input('Введите первое число\n'))
        n_2 = float(input('Введите второе число\n'))
        print('Результат равен ', n_1 * n_2)
    elif action == '//':
        n_1 = float(input('Введите первое число\n'))
        n_2 = float(input('Введите второе число\n'))
        print('Результат равен ', n_1 // n_2)
    elif action == '/':
        n_1 = float(input('Введите первое число\n'))
        n_2 = float(input('Введите второе число\n'))
        print('Результат равен ', n_1 / n_2)
    elif action == '%':
        n_1 = float(input('Введите первое число\n'))
        n_2 = float(input('Введите второе число\n'))
        print('Результат равен ', n_1 % n_2)
    elif action == '~':
        n_1 = float(input('Введите число\n'))
        print('Результат равен ', round(n_1))
    elif action == 'f~':
        n_1 = float(input('Введите число\n'))
        print('Результат равен ', math.floor(n_1))
    elif action == 'c~':
        n_1 = float(input('Введите число\n'))
        print('Результат равен ', math.ceil(n_1))
    elif action == '||':
        n_1 = float(input('Введите число\n'))
        print('Результат равен ', math.fabs(n_1))
    elif action == '√':
        n_1 = float(input('Введите число\n'))
        if n_1 > 0:
            print('Результат равен ', math.sqrt(n_1))
        else:
            print('Ошибка: число не может быть отрицательным.')
    elif action == '^':
        n_1 = float(input('Введите число\n'))
        n_2 = float(input('Введите степень\n'))
        print('Результат равен ', math.pow(n_1, n_2))
    elif action == 'log':
        n_1 = float(input('Введите число\n'))
        if n_1 > 0:
            print('Результат равен ', math.log(n_1))
        else:
            print('Ошибка: число не может быть отрицательным.')
    elif action == 'log10':
        n_1 = float(input('Введите число\n'))
        if n_1 > 0:
            print('Результат равен ', math.log10(n_1))
        else:
            print('Ошибка: число не может быть отрицательным.')
    elif action == 'log(x,b)':
        n_1 = float(input('Введите число\n'))
        n_2 = float(input('Введите основание\n'))
        if n_1 > 0 and n_2 > 0:
            print('Результат равен ', math.log(n_1, n_2))
        else:
            print('Ошибка: число не может быть отрицательным.')
    elif action == 'fact':
        n_1 = int(input('Введите число\n'))
        if n_1 > 0:
            print('Результат равен ', math.factorial(n_1))
        else:
            print('Ошибка: число не может быть отрицательным.')
    elif action == 'tab':
        for i in range(1,11):
            for j in range(1, 11):
                print(i**j, end=' ')
            print()
    else:
        print('Завершение программы')
        break
    s = input('Для продолжения нажмите "далее"\n ')
    if s == 'далее':
        continue
    else:
        print('Завершение программы')
        break