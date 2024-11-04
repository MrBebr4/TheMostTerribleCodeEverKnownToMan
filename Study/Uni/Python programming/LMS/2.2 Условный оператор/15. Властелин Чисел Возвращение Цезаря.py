# Получаем два числа
firstNum = int(input())
secondNum = int(input())

# Проверяем, что числа в нужном диапазоне
if firstNum and secondNum < 100:
    pass
else:
    print("Invalid number")
    quit()

# Выдрать цифры из первого числа
firstNum1 = firstNum // 10
firstNum3 = firstNum % 10

# Выдрать цифры из второго числа
secondNum1 = secondNum // 10
secondNum3 = secondNum % 10

# Создать список из цифр
nums = [firstNum1, firstNum3, secondNum1, secondNum3]

# Найти максимальное, минимальное и среднее число
maxNum = max(nums)
minNum = min(nums)
middleNum = sum(nums) - maxNum - minNum

# Собрать итоговое число и вывести его
print(maxNum * 100 + middleNum * 10 + minNum)