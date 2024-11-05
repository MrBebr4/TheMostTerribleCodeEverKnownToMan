# объявляем список lines в котором будут храниться строки с зайкой
lines = []

# Запрашиваем строрки с зайкой и добавляем их в список lines. После получения строки "Приехали!" завершаем цикл
while True:
    lineStr = input()
    if lineStr == "Приехали!":
        break
    elif "зайка" in lineStr:
        lines.append(lineStr)
    else:
        continue

# Выводим количество строк с зайкой
print(len(lines))
