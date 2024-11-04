# Получаем три строки с именами игроков
nameOne = input()
nameTwo = input()
nameThree = input()

# Находим первого игрока по лексикографическому порядку
firstPlayer = min(nameOne, nameTwo, nameThree)
print(firstPlayer)