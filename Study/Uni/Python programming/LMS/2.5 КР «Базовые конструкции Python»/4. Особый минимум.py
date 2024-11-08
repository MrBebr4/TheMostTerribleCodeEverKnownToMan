# Вводим количество чисел в последовательности
N = int(input())

# Вводим числа последовательности
sequence = [int(input()) for _ in range(N)]

# Инициализируем переменную для хранения минимального числа, большего своего предшественника
min_value = None

# Проходим по последовательности, начиная со второго элемента
for i in range(1, N):
    if sequence[i] > sequence[i - 1]:
        if min_value is None or sequence[i] < min_value:
            min_value = sequence[i]

# Выводим результат
if min_value is not None:
    print(min_value)
else:
    print("Нет подходящих чисел")