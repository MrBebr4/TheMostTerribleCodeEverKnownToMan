# Запращивает время доставки и время ожидания
hours = int(input())
minutes = int(input())
timeUpTo = int(input())

# Рассчитываем время доставки
mins = (minutes + timeUpTo) % 60
hours = ((hours % 24) + (timeUpTo + minutes) // 60)
mins = str(mins)
mins.zfill(2)

# Выводим результат
print(f"{hours}:{mins}")
