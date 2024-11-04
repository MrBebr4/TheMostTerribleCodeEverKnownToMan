# запрашиваем пароль
password = int(input())

# Получаем цифры пароля
num1 = str((password % 10) + (password // 10 - password // 100 * 10))
num2 = str((password // 100) + (password // 10 - password // 100 * 10))

# В порядке невозрастания выводим отконкатенированные строки
if num1 > num2:
    print(num1+num2)
elif num1 < num2:
    print(num2+num1)