player_ammount = int(input())  # Считываем количество игроков

player_list = []  # Создаем пустой список для хранения имен игроков
i = player_ammount  # Инициализируем счетчик количеством игроков

while i > 0:  # Пока счетчик больше нуля
    player = input()  # Считываем имя игрока
    player_list.append(player)  # Добавляем имя игрока в список
    i -= 1  # Уменьшаем счетчик на единицу

print(max(player_list))  # Выводим имя игрока с максимальным лексикографическим значением
