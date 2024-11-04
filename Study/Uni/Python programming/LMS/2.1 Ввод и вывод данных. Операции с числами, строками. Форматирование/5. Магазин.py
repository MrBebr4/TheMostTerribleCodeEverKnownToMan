# Запрашиваем количество товара, цену и наличные
amount = input()
price = input()
money = input()

# Рассчитываем сдачу (наличные минус стоимость товара)
change = float(money) - float(amount) * float(price)

# Выводим сдачу на консоль
print(change)