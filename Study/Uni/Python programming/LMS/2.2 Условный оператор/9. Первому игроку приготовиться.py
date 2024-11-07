# Получаем три строки с именами игроков
name_one = input()
name_two = input()
name_three = input()

# Находим первого игрока по лексикографическому порядку
first_player = min(name_one, name_two, name_three)
print(first_player)