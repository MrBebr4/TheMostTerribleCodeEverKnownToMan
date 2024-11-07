# Запрашиваем начальное и конечное значение диапазона
array_start = int(input())
array_end = int(input())

# Вычисляем длину диапазона
length = array_end - array_start + 1

# Объявляем пустой список для хранения чисел диапазона
line = []

# Заполняем список числами из диапазона
while length > 0:
    line.append(array_start)
    array_start += 1
    length -= 1

# Выводим числа из списка, разделенные пробелами
print(" ".join(map(str, line)))
