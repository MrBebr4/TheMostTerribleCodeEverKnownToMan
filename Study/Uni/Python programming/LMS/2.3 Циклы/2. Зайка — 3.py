# объявляем список lines в котором будут храниться строки с зайкой
lines = []

# Запрашиваем строрки с зайкой и добавляем их в список lines. После получения строки "Приехали!" завершаем цикл
while True:
    line_str = input()
    if line_str == "Приехали!":
        break
    elif "зайка" in line_str:
        lines.append(line_str)
    else:
        continue

# Выводим количество строк с зайкой
print(len(lines))
