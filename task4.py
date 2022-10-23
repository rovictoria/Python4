# Задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 60 -> 2, 2, 3, 5
import math 

print('1. Поиск простых множителей натурального числа')

def Check_number(N):
    check = True
    for i in range(2, math.ceil(math.sqrt(N))):
        check = bool( N % i)
        if not check:
            break
    return check


def Find_divigers(N):
    main = N
    divigers = []
    for i in range(2, N//2 + 1 ):
        while (N % i == 0):
            if  Check_number(i) and N % i == 0:
                divigers.append(i)
                N /= i
    print(f'1 способ: Простые множители числа N = {main} - {divigers}')

Find_divigers(22)

def Easy_find_divigers(N):
    main = N
    i = 2 
    list = []
    while i <= N:
        if N % i == 0:
            list.append(i)
            N //= i
            i = 2
        else:
            i += 1
    print(f'2 способ: Простые множители числа N = {main} - {list}')

Easy_find_divigers(22)

# Задача 2. В первой строке файла находится информация об ассортименте мороженного, во второй - информация о том, какое мороженное есть на складе. Выведите названия того товара, который закончился.
# 1. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2. «Сливочное», «Вафелька», «Сладкоежка»
# Закончилось: «Бурёнка»
print('2. Остатки мороженого')

def Defic_ice_cream():
    data = open('icecream.txt', encoding = 'utf-8')
    icecream = data.readlines()
    data.close()
    first_str = set(icecream[0].replace('\n', '').split(', '))
    second_str = set(icecream[1].replace('\n', '').split(', '))
    print(f'Ассортимент: {first_str}')
    print(f'На складе: {second_str}')
    print(f'Закончилось: {first_str.difference(second_str)}')

Defic_ice_cream()

# Задача 3. Выведите число π с заданной точностью. Точность вводится пользователем в виде натурального числа. 3 -> 3.142
# 5 -> 3.14159
print('3. Вывод числа π с заданной точностью.')

def Pi_number():
    N = int(input('Введите количество знаков после запятой для пи: '))
    print(round(math.pi, N))

Pi_number()

# Задача 4*. Даны два файла, в каждом из которых находится запись многочлена. Найдите сумму данных многочленов.
# 1. 5x^2 + 3x 2. 3x^2 + x + 8 Результат: 8x^2 + 4x + 8
print('4. Сумма многочленов.')

with open('polyn1.txt', 'w', encoding='utf-8') as file1:
    n = '5x^2 + 3x - 4 = 0'
    file1.write(n)
with open('polyn2.txt', 'w', encoding='utf-8') as file2:
    n = '3x^2 - x + 8 = 0'
    file2.write(n)

with open('polyn1.txt', 'r') as file1:
   polyn1 = file1.readline()
with open('polyn2.txt', 'r') as file2:
   polyn2 = file2.readline()

print(f'Первый многочлен: {polyn1}')
print(f'Второй многочлен: {polyn2}')

# если бы без
# with open('polyn1.txt', 'r') as inf:
#     polyn1 = [str.replace('-', '+ -').split(" + ") for str in map(str.rstrip, inf.readlines())]

# with open('polyn2.txt', 'r') as inf:
#     polyn2 = [str.replace('-', '+ -').split(" + ") for str in map(str.rstrip, inf.readlines())]

import re #регулярные выражения
from sympy import Symbol, collect  #позволяет символьно воспринимать, дальше для х; collect уже для суммы
# установлено отдельно py -m pip install sympy

def Convert_for_Python(pol):
    pol = re.sub(r'(\d)(x)', r'\1*\2', pol)
    pol = pol.replace('^', '**')
    # pol = pol.replace('-','+ -') тогда в подобной корректировке и нет смысла
    pol = pol[:-4:]
    return pol

polyn1 = Convert_for_Python(polyn1)
polyn2 = Convert_for_Python(polyn2)

x = Symbol('x')

result = str(collect(polyn1 + ' + ' + polyn2, x))
result = result.replace('**', '^')
result = result.replace('*', '')
result = result + ' = 0'
print(f'Результат суммы многочленов: {result}')