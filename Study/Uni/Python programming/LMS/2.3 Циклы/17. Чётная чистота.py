# Считываем введенное число
number = input().strip()

# Удаляем четные цифры
result = ''.join(digit for digit in number if int(digit) % 2 != 0)

# Выводим результат
print(result)