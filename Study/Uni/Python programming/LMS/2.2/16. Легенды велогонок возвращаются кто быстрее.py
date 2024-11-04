# запросить скорости
petyaSpeed = int(input())
vasyaSpeed = int(input())
tolyaSpeed = int(input())

# создать кортеж из скоростей и имен
speeds = [("Petya", petyaSpeed), ("Vasya", vasyaSpeed), ("Tolya", tolyaSpeed)]
speeds.sort(key=lambda x: x[1], reverse=True)

# вывести имена в порядке финиширования
print(f"{speeds[0][0]: ^24}")
print(f"{speeds[1][0]: ^8}{" ": ^16}")
print(f"{" ": ^16}{speeds[2][0]: ^8}")
print(f'{"II": ^8}{"I": ^8}{"III": ^8}')