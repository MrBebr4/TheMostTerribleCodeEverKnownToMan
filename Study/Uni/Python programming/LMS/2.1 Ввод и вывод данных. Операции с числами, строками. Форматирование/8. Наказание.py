# Запрашиваем у пользователя количество повторений и фразу
times = int(input())
phrase = input()

# Формируем строку с наказанием
output = f"Я больше никогда не буду писать {phrase}!\n"

# Выводим строку с наказанием указанное количество раз
print(output * times)