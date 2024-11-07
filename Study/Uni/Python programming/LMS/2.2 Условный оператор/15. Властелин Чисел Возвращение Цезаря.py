# Получаем два числа
first_num = int(input())
second_num = int(input())

# Проверяем, что числа в нужном диапазоне
if first_num and second_num < 100:
    pass
else:
    print("Invalid number")
    quit()

# Выдрать цифры из первого числа
first_num1 = first_num // 10
first_num3 = first_num % 10

# Выдрать цифры из второго числа
second_num1 = second_num // 10
second_num3 = second_num % 10

# Создать список из цифр
nums = [first_num1, first_num3, second_num1, second_num3]

# Найти максимальное, минимальное и среднее число
max_num = max(nums)
min_num = min(nums)
middle_num = sum(nums) - max_num - min_num

# Собрать итоговое число и вывести его
print(max_num * 100 + middle_num * 10 + min_num)