# Считываем размер таблицы и ширину столбцов
size = int(input())
column_width = int(input())

# Генерируем таблицу умножения
table = [[(i + 1) * (j + 1) for j in range(size)] for i in range(size)]

# Форматируем и выводим таблицу
for i in range(size):
    row = " | ".join(f"{num:^{column_width}}" for num in table[i])
    print(row)
    if i < size - 1:
        print("-" * (size * (column_width + 3) - 1))