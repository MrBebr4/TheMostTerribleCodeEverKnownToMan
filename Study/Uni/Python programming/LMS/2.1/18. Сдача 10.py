#пробуем вводить числа в двоичной системе счисления
while True:
    try:
        change = int(input(), 2)
        break
    except:
        print("invalidNumber")
        continue
#запрашиваем сумму наличных
cash = int(input())

#вычисляем сдачу
actualChange = cash - change
print(actualChange)