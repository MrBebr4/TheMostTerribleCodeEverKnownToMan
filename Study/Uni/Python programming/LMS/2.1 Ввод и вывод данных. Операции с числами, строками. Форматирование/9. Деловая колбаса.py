# Устанавливаем скорость
speed = 0.5

# Запрашиваем у пользователя время и количество детей
time = int(input())
children_amount = int(input())

# Рассчитываем результат (время * скорость * количество детей)
result = time * speed * children_amount

# Переводим результат в целое число
result = int(result)

# Выводим результат на консоль
print(result)