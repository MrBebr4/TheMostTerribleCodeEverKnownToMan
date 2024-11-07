# Запрашиваем скорость Васи и Пети
vasya_speed = int(input())
petya_speed = int(input())

# Сравниваем скорости и выбираем победителя
if vasya_speed > petya_speed:
    print("Вася")
elif petya_speed > vasya_speed:
    print("Петя")
else:
    print("Ничья")