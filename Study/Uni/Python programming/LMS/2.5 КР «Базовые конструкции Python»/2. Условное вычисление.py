# Вводим два целых числа и строку
num1 = int(input())
num2 = int(input())
str1 = input()

# Определяем длину строки
length = len(str1)

# Определяем математическую операцию по длине строки
if length % 6 == 0:
    result = num1 + num2
elif length % 3 == 0:
    result = num1 - num2
elif length % 2 == 0:
    result = num1 * num2
else:
    result = num1 // num2

# Выводим результат
print(result)