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
    divigers = []
    for i in range(2, N//2):
        while (N % i == 0):
            if  Check_number(i) and N % i == 0:
                divigers.append(i)
                N /= i
    print(divigers)

num = 22
Find_divigers(num)

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

    print(f'Закончилось : {first_str.difference(second_str)}')

Defic_ice_cream()

# Задача 3. Выведите число π с заданной точностью. Точность вводится пользователем в виде натурального числа. 3 -> 3.142
# 5 -> 3.14159

def Pi_number():
    N = int(input('Введите количество знаков после запятой для пи: '))
    print(round(math.pi, N))

Pi_number()

# Задача 4*. Даны два файла, в каждом из которых находится запись многочлена. Найдите сумму данных многочленов.
# 1. 5x^2 + 3x 2. 3x^2 + x + 8 Результат: 8x^2 + 4x + 8

# n = '5x^2 + 3x 2'
# n.replace('-', '+-')
# print(n)
# n = n.split('+')
# print(n)

with open('polyndrom1.txt', 'w', encoding='utf-8') as file:
    file.write('5x^2 + 3x')
with open('polyndrom2.txt', 'w', encoding='utf-8') as file:
    file.write('3x^2 + x + 8')

with open('polyndrom1.txt','r') as file:
    polyndrom1 = file.readline()
    list_of_polyndrom1 = polyndrom1.split()


with open('polyndrom2.txt','r') as file:
    polyndrom2 = file.readline()
    list_of_polyndrom2 = polyndrom2.split()

print(f'{list_of_polyndrom1} + {list_of_polyndrom2}')
sum_polyndroms = list_of_polyndrom1 + list_of_polyndrom2

with open('sum_polyndroms.txt', 'w', encoding='utf-8') as file:
    file.write(f'{list_of_polyndrom1} + {list_of_polyndrom2}')
