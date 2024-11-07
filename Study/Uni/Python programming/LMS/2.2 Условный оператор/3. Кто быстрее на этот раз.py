# Запрашиваем скорость каждого из участников
petya_speed = int(input())
vasya_speed = int(input())
tolya_speed = int(input())

# Сравниваем скорости и выбираем победителя
if vasya_speed > petya_speed and tolya_speed:
    print("Вася")
elif petya_speed > vasya_speed and tolya_speed:
    print("Петя")
elif tolya_speed > vasya_speed and petya_speed:
    print("Толя")
else:
    print("Ничья")
