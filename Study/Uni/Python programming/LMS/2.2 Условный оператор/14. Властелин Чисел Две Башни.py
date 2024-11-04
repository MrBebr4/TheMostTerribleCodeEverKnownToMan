# Запрашиваем ввод
number = int(input())

# Проверяем, что число в нужном диапазоне
if 99 < number < 999:
    pass
else:
    print("Invalid number")
    quit()

# Выдрать цифры
firstNum = number // 100
secondNum = (number // 10) % 10
thirdNum = number % 10

# Зоздать все возможные комбинации
combinations = [
    firstNum * 10 + secondNum,
    firstNum * 10 + thirdNum,
    secondNum * 10 + firstNum,
    secondNum * 10 + thirdNum,
    thirdNum * 10 + firstNum,
    thirdNum * 10 + secondNum
]

# Отфильтровываем не подходящие комбинации
isValid = []
for num in combinations:
    if num >= 10:
        isValid.append(num)

# Находим максимальное и минимальное число
minNum = min(isValid)
maxNum = max(isValid)

# Выводим результат
print(minNum, maxNum)