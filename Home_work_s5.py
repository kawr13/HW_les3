'''
: Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел. Из
всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.
'''


def summ(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return summ(a - 1, b + 1)

num1 = int(input('Первое число: '))
num2 = int(input('Второе число: '))
print(summ(num1, num2))


'''Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.
'''

def step(a, b):
    if b == 0:
        return 1
    else:
        return a * step(a, b -1)

num_s1 = int(input('Первое число: '))
num_s2 = int(input('В какую степень: '))
print(step(num_s1, num_s2))
