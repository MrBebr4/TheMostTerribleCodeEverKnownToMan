# Считываем количество детей
n = int(input())

# Инициализируем переменные для хранения имени победителя и максимальной суммы цифр
winner_name = ""
max_sum = -1

# Считываем имя и число каждого ребенка
for i in range(n):
    name = input()
    number = int(input())
    current_sum = sum(int(digit) for digit in str(number))

    # Если текущая сумма цифр больше или равна максимальной, обновляем победителя
    if current_sum >= max_sum:
        winner_name = name
        max_sum = current_sum

# Выводим имя победителя
print(winner_name)