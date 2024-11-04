# Запрашиваем скорость Васи и Пети
vasyaSpeed = int(input())
petyaSpeed = int(input())

# Сравниваем скорости и выбираем победителя
if vasyaSpeed > petyaSpeed:
    print("Вася")
elif petyaSpeed > vasyaSpeed:
    print("Петя")
else:
    print("Ничья")