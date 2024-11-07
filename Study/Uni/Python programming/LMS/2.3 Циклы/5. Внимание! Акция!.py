# Инициализируем пустые списки для хранения цен товаров и скидочных цен
shop_list_price = []
discounted_price = []

# Запрашиваем цены товаров у пользователя до тех пор, пока не будет введено значение 0
while True:
    price = float(input())
    shop_list_price.append(price)
    if price == 0:
        break

# Применяем скидку 10% к товарам, цена которых больше или равна 500, и добавляем их в список скидочных цен
for i in shop_list_price:
    if i >= 500:
        discounted_price.append(i * 0.9)
    else:
        discounted_price.append(i)

# Выводим общую сумму скидочных цен
print(sum(discounted_price))
