# Получаем число
number = input()

# Переворачиваем число
flippedNumber = number[::-1]

# Сравниваем число и его перевернутый вариант
if flippedNumber == number:
    print("YES")
else:
    print("NO")