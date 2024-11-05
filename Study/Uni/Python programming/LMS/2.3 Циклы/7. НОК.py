# Определяем функцию для вычисления наибольшего общего делителя (НОД) двух чисел
def gcd(a, b):
    while b:  # Продолжаем цикл, пока b не станет равно нулю
        a, b = b, a % b
    return a  # Возвращаем НОД, который теперь хранится в a


# Определяем функцию для вычисления наименьшего общего кратного (НОК) двух чисел
def lcm(a, b):
    return abs(a * b) // gcd(a, b)


# Считываем первое и второе число из ввода пользователя
num1 = int(input())
num2 = int(input())

# Вычисляем и выводим НОК двух введенных чисел
print(lcm(num1, num2))
