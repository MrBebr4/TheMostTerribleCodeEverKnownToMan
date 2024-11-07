# Запросить скорости
petya_speed = int(input())
vasya_speed = int(input())
tolya_speed = int(input())

# Создать кортеж из скоростей и имен
speeds = [("Petya", petya_speed), ("Vasya", vasya_speed), ("Tolya", tolya_speed)]
speeds.sort(key=lambda x: x[1], reverse=True)

# Вывести имена в порядке финиширования
print(f"{speeds[0][0]: ^24}")
print(f"{speeds[1][0]: ^8}{" ": ^16}")
print(f"{" ": ^16}{speeds[2][0]: ^8}")
print(f'{"II": ^8}{"I": ^8}{"III": ^8}')