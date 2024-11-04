# Запршашиваем обрабатываемое число
numInp = int(input())

# Получаем цифры числа
num3 = numInp % 10
num2 = numInp // 10 % 10
num1 = numInp // 100
sumNum = num1 + num3

# Проверяем, является ли сумма первой и последней цифры числа в два раза больше средней цифры
if sumNum == (num2 * 2):
    print("YES")
else:
    print("NO")