# Инициализируем переменные
current_number = 1
row = 1

# Считываем число
n = int(input())

# Цикл до тех пор, пока мы не напечатаем все числа
while current_number <= n:
    # Вычисляем количество пробелов, необходимых для текущей строки
    spaces = ' ' * (n - row)

    # Генерируем текущую строку чисел
    row_numbers = ' '.join(str(current_number + i) for i in range(row) if current_number + i <= n)

    # Печатаем текущую строку с ведущими пробелами
    print(f"{spaces}{row_numbers}")

    # Обновляем текущее число и строку для следующей итерации
    current_number += row
    row += 1