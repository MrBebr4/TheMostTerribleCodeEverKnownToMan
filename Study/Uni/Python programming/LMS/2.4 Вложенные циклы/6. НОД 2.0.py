import math
from functools import reduce

# Функция для вычисления НОД двух чисел с использованием алгоритма Евклида
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Функция для вычисления НОД списка чисел
def gcd_list(numbers):
    return reduce(gcd, numbers)

# Считываем количество чисел
n = int(input())

# Считываем все числа в список
numbers = [int(input()) for _ in range(n)]

# Вычисляем НОД всех чисел в списке
result = gcd_list(numbers)

# Выводим результат
print(result)