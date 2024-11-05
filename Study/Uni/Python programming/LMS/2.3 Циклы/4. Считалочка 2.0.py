# Запрашиваем начальное и конечное значения диапазона
arrayStart = int(input())
arrayEnd = int(input())

# Если начальное значение больше конечного, меняем их местами
if arrayStart > arrayEnd:
    arrayStart, arrayEnd = arrayEnd, arrayStart

# Вычисляем длину диапазона
length = arrayEnd - arrayStart + 1

# Инициализируем пустой список для хранения чисел диапазона
line = []

# Заполняем список числами из диапазона
while length > 0:
    line.append(arrayStart)
    arrayStart += 1
    length -= 1

# Выводим числа из списка, разделенные пробелами
print(" ".join(map(str, line)))
