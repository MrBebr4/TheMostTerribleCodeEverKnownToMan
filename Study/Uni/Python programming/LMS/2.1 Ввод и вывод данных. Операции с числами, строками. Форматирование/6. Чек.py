# Получаем данные от пользователя
product_name = input()
price_per_kg = float(input())
weight = float(input())
money_given = float(input())

# Вычисляем общую стоимость и сдачу
total_cost = price_per_kg * weight
change = money_given - total_cost

# Печатем чек
print("Чек")
print(f"{product_name} - {weight}кг - {price_per_kg}руб/кг")
print(f"Итого: {total_cost}руб")
print(f"Внесено: {money_given}руб")
print(f"Сдача: {change}руб")