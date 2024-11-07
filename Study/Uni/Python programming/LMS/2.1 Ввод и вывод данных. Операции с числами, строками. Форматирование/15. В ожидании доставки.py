# Запращивает время доставки и время ожидания
hours = int(input())
minutes = int(input())
time_up_to = int(input())

# Рассчитываем время доставки
mins = (minutes + time_up_to) % 60
hours = ((hours % 24) + (time_up_to + minutes) // 60)
mins = str(mins)
mins.zfill(2)

# Выводим результат
print(f"{hours}:{mins}")
