# Переменные
total_weight = int(input())
total_price = int(input())
first_price = int(input())
second_price = int(input())

# Расчет
if first_price > second_price:
    first_weight = int((total_price - second_price) * total_weight / (first_price - second_price))
    second_weight = int(total_weight - first_weight)
else:
    print("Invalid price")
    quit()

# Вывод
print(first_weight, second_weight)