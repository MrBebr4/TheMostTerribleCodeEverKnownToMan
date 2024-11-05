# Запрашиваем начальное и конечное значение диапазона
arrayStart = int(input())
arrayEnd = int(input())

# Вычисляем длину диапазона
length = arrayEnd - arrayStart + 1

# Объявляем пустой список для хранения чисел диапазона
line = []

# Заполняем список числами из диапазона
while length > 0:
    line.append(arrayStart)
    arrayStart += 1
    length -= 1

# Выводим числа из списка, разделенные пробелами
print(" ".join(map(str, line)))
