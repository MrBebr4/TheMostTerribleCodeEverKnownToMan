# запрашиваем у пользователя два числа до 3-х знаков
while True:
    firstnum = int(input())
    secondnum = int(input())
    if firstnum or secondnum < 999:
        break
    else:
        print("Please enter a 3-digit number or less")
        continue

# переводим числа в строку
firstnum = str(firstnum)
secondnum = str(secondnum)

# заполняем числа нулями слева
firstnum = firstnum.zfill(3)
secondnum = secondnum.zfill(3)

# выдергиваем цифры из чисел порозрядно
try:
    firstnum3 = int(firstnum[2])
except:
    firstnum3 = 0
firstnum2 = int(firstnum[1])
firstnum1 = int(firstnum[0])

# выдергиваем цифры из чисел порозрядно
try:
    secondnum3 = int(secondnum[2])
except:
    secondnum3 = 0
secondnum2 = int(secondnum[1])
secondnum1 = int(secondnum[0])

# складываем числа и находим остаток от деления на 10
sum1 = (firstnum3 + secondnum3) % 10
sum2 = (firstnum2 + secondnum2) % 10
sum3 = (firstnum1 + secondnum1) % 10

# выводим результат
result = f"{sum3}{sum2}{sum1}"
print(result)

# господи, что я наделал