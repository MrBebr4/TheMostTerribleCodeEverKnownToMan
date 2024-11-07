# Получаем число
number = input()

# Переворачиваем число
flipped_number = number[::-1]

# Сравниваем число и его перевернутый вариант
if flipped_number == number:
    print("YES")
else:
    print("NO")