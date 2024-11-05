# Считываем число из ввода пользователя
workingNumber = int(input())

# Инициализируем переменную для хранения результата факториала
endFactorial = 1

# Проверяем, является ли введенное число нулем
if workingNumber == 0:
    print(1) # Если число равно нулю, факториал равен 1

else:

    # Цикл для вычисления факториала числа
    while workingNumber > 0:
        endFactorial = endFactorial * workingNumber  # Умножаем текущий результат факториала на текущее число
        workingNumber -= 1  # Уменьшаем число на 1

    # Выводим окончательный результат факториала
    print(endFactorial)
