# Пробуем вводить числа в двоичной системе счисления
while True:
    try:
        change = int(input(), 2)
        break
    except:
        print("invalidNumber")
        continue

# Запрашиваем сумму наличных
cash = int(input())

# Вычисляем сдачу
actual_change = cash - change
print(actual_change)