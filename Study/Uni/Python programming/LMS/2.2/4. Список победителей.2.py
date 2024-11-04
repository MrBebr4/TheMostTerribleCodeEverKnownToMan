# Запраиваем у пользователя скорость трех спортсменов
petyaSpeed = int(input())
vasyaSpeed = int(input())
tolyaSpeed = int(input())

# Создаем список скоростей
speeds = [petyaSpeed, vasyaSpeed, tolyaSpeed]

# Сортируем список по убыванию
speeds.sort(reverse=True)

# Выводим список победителей
for i, speed in enumerate(speeds, start=1):
    print(f"{i}. {speed}")