#ввод пользователя
item_name = input()
item_price_per_kg = int(input())
item_weight_kg = int(input())
cash_given = int(input())

#меняем типы переменных и добавляем текст
price_string = str(item_weight_kg) + 'кг * ' + str(item_price_per_kg) + 'руб/кг'
total_price_string = str(item_price_per_kg * item_weight_kg) + 'руб'
cash_given_string = str(cash_given) + 'руб'
change_string = str(cash_given - item_price_per_kg * item_weight_kg) + 'руб'

#вывод, числа после > указывают на минимальную длину строки
print('================Чек================')
print(f'Товар: {item_name:>28}')
print(f'Цена: {price_string:>29}')
print(f'Итого: {total_price_string:>28}')
print(f'Внесено: {cash_given_string:>26}')
print(f'Сдача: {change_string:>28}')
print('===================================')