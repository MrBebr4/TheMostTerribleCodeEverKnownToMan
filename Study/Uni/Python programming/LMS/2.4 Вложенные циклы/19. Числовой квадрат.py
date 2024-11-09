# Считываем введенное число
N = int(input())

# Инициализируем квадрат
square = [[0] * N for _ in range(N)]

# Заполняем квадрат
for i in range(N):
    for j in range(N):
        square[i][j] = min(i, j, N - 1 - i, N - 1 - j) + 1

# Печатаем квадрат
for row in square:
    print(' '.join(map(str, row)))