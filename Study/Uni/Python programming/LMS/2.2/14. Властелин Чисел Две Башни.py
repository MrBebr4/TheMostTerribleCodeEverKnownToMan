# запрашиваем ввод
number = int(input())
if 99 < number < 999:
    pass
else:
    print("Invalid number")
    quit()
# Выдрать числа
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

# Find the minimum and maximum valid combinations
minNum = min(isValid)
maxNum = max(isValid)

# Print the results
print(minNum, maxNum)