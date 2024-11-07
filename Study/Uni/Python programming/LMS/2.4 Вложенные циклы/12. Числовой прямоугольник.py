# Считываем высоту и ширину прямоугольника
N = int(input())
M = int(input())

# Вычисляем максимальное число, чтобы определить ширину каждого числа
max_num = N * M
num_width = len(str(max_num))

# Инициализируем начальное число
current_num = 1

# Генерируем и выводим числовой прямоугольник
for i in range(N):
    row = []
    for j in range(M):
        row.append(f"{current_num:>{num_width}}")
        current_num += 1
    print(" ".join(row))