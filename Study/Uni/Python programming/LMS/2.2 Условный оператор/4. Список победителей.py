# Запрашиваем скорость каждого участника
petyaSpeed = int(input())
vasyaSpeed = int(input())
tolyaSpeed = int(input())

# создаем кортеж участников
participants = [("Петя", petyaSpeed), ("Вася", vasyaSpeed), ("Толя", tolyaSpeed)]

# Отсортируем участников по скорости
participants.sort(key=lambda x: x[1], reverse=True)

# Выводим список победителей
for i, participant in enumerate(participants, start=1):
    print(f"{i}. {participant[0]}")