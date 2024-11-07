# Запрашиваем скорость каждого участника
petya_speed = int(input())
vasya_speed = int(input())
tolya_speed = int(input())

# создаем кортеж участников
participants = [("Петя", petya_speed), ("Вася", vasya_speed), ("Толя", tolya_speed)]

# Отсортируем участников по скорости
participants.sort(key=lambda x: x[1], reverse=True)

# Выводим список победителей
for i, participant in enumerate(participants, start=1):
    print(f"{i}. {participant[0]}")