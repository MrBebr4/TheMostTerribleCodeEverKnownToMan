# запрашиваем у пользователя два числа до 3-х знаков
while True:
    first_num = int(input())
    second_num = int(input())
    if first_num or second_num < 999:
        break
    else:
        print("Please enter a 3-digit number or less")
        continue

# переводим числа в строку
first_num = str(first_num)
second_num = str(second_num)

# заполняем числа нулями слева
first_num = first_num.zfill(3)
second_num = second_num.zfill(3)

# выдергиваем цифры из чисел порозрядно
try:
    first_num3 = int(first_num[2])
except:
    first_num3 = 0
first_num2 = int(first_num[1])
first_num1 = int(first_num[0])

# выдергиваем цифры из чисел порозрядно
try:
    second_num3 = int(second_num[2])
except:
    second_num3 = 0
second_num2 = int(second_num[1])
second_num1 = int(second_num[0])

# складываем числа и находим остаток от деления на 10
sum1 = (first_num3 + second_num3) % 10
sum2 = (first_num2 + second_num2) % 10
sum3 = (first_num1 + second_num1) % 10

# выводим результат
result = f"{sum3}{sum2}{sum1}"
print(result)

# господи, что я наделал