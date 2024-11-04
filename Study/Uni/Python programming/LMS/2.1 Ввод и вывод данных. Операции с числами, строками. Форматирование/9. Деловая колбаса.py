# Устанавливаем скорость
speed = 0.5

# Запрашиваем у пользователя время и количество детей
time = int(input())
childrenAmount = int(input())

# Рассчитываем результат (время * скорость * количество детей)
result = time * speed * childrenAmount

# Переводим результат в целое число
result = int(result)

# Выводим результат на консоль
print(result)