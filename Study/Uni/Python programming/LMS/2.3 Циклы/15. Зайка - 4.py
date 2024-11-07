amount = int(input())  # Считываем количество строк

road_list = []  # Создаем пустой список для хранения строк с "зайка"

for i in range(amount):  # Запрашиваем строки amount раз
    creature = input()
    if "зайка" in creature:  # Проверяем, содержит ли строка слово "зайка"
        road_list.append(creature)  # Если да, добавляем строку в список

print(len(road_list))  # Выводим количество строк, содержащих "зайка"
