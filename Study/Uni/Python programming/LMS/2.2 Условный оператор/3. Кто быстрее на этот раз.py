# Запрашиваем скорость каждого из участников
petyaSpeed = int(input())
vasyaSpeed = int(input())
tolyaSpeed = int(input())

# Сравниваем скорости и выбираем победителя
if vasyaSpeed > petyaSpeed and tolyaSpeed:
    print("Вася")
elif petyaSpeed > vasyaSpeed and tolyaSpeed:
    print("Петя")
elif tolyaSpeed > vasyaSpeed and petyaSpeed:
    print("Толя")
else:
    print("Ничья")
