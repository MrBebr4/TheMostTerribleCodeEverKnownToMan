# Запрашиваем начальное и конечное значения диапазона
array_start = int(input())
array_end = int(input())

# Если начальное значение больше конечного, меняем их местами
if array_start > array_end:
    array_start, array_end = array_end, array_start

# Вычисляем длину диапазона
length = array_end - array_start + 1

# Инициализируем пустой список для хранения чисел диапазона
line = []

# Заполняем список числами из диапазона
while length > 0:
    line.append(array_start)
    array_start += 1
    length -= 1

# Выводим числа из списка, разделенные пробелами
print(" ".join(map(str, line)))
