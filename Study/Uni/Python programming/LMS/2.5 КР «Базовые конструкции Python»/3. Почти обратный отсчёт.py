# Вводим два натуральных числа N и M
N = int(input())
M = int(input())

# Вычисляем шаг
step = (N - M) // 3

# Создаем список чисел от N до M с шагом step
countdown = list(range(N, M - 1, -step))

# Выводим последовательность чисел через точку с запятой и пробел
print("; ".join(map(str, countdown)))

# Выводим "Старт!"
print("Старт!")