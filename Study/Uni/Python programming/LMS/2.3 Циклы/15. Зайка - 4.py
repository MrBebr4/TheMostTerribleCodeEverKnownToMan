amount = int(input())  # Считываем количество строк

roadList = []  # Создаем пустой список для хранения строк с "зайка"

for i in range(amount):  # Запрашиваем строки amount раз
    creature = input()
    if "зайка" in creature:  # Проверяем, содержит ли строка слово "зайка"
        roadList.append(creature)  # Если да, добавляем строку в список

print(len(roadList))  # Выводим количество строк, содержащих "зайка"
