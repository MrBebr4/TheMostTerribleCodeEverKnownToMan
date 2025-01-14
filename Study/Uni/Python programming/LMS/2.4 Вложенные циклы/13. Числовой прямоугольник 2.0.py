# Считываем высоту и ширину прямоугольника
N = int(input())
M = int(input())

# Вычисляем максимальное число, чтобы определить ширину каждого числа
max_num = N * M
num_width = len(str(max_num))

# Инициализируем матрицу для хранения чисел
matrix = [[0] * M for _ in range(N)]

# Заполняем матрицу числами по столбцам
current_num = 1
for j in range(M):
    for i in range(N):
        matrix[i][j] = current_num
        current_num += 1

# Выводим числовой прямоугольник
for row in matrix:
    print(" ".join(f"{num:>{num_width}}" for num in row))