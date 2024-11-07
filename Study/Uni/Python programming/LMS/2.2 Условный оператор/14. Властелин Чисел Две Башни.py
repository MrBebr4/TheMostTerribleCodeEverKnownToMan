# Запрашиваем ввод
number = int(input())

# Проверяем, что число в нужном диапазоне
if 99 < number < 999:
    pass
else:
    print("Invalid number")
    quit()

# Выдрать цифры
first_num = number // 100
second_num = (number // 10) % 10
third_num = number % 10

# Зоздать все возможные комбинации
combinations = [
    first_num * 10 + second_num,
    first_num * 10 + third_num,
    second_num * 10 + first_num,
    second_num * 10 + third_num,
    third_num * 10 + first_num,
    third_num * 10 + second_num
]

# Отфильтровываем не подходящие комбинации
is_valid = []
for num in combinations:
    if num >= 10:
        is_valid.append(num)

# Находим максимальное и минимальное число
min_num = min(is_valid)
max_num = max(is_valid)

# Выводим результат
print(min_num, max_num)