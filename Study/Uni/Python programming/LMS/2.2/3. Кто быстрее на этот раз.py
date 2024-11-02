#запрашиваем скорость каждого из участников
petyaSpeed = int(input())
vasyaSpeed = int(input())
tolyaSpeed = int(input())

if vasyaSpeed > petyaSpeed and tolyaSpeed:
    print("Вася")
elif petyaSpeed > vasyaSpeed and tolyaSpeed:
    print("Петя")
elif tolyaSpeed > vasyaSpeed and petyaSpeed:
    print("Толя")
else:
    print("Ничья")
