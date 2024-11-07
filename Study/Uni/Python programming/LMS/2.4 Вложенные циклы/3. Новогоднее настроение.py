# Считываем количество чисел в математической ёлке
num = int(input())

current_number = 1  # Начальное число
row_length = 1  # Длина текущей строки

# Пока текущее число не превысит введенное количество чисел
while current_number <= num:
    # Печатаем числа в текущей строке
    for i in range(row_length):
        if current_number > num:
            break
        print(current_number, end=' ')
        current_number += 1
    print()  # Переход на новую строку
    row_length += 1  # Увеличиваем длину следующей строки