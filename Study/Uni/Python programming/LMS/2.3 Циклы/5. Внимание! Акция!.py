# Инициализируем пустые списки для хранения цен товаров и скидочных цен
shopListPrice = []
discountedPrice = []

# Запрашиваем цены товаров у пользователя до тех пор, пока не будет введено значение 0
while True:
    price = float(input())
    shopListPrice.append(price)
    if price == 0:
        break

# Применяем скидку 10% к товарам, цена которых больше или равна 500, и добавляем их в список скидочных цен
for i in shopListPrice:
    if i >= 500:
        discountedPrice.append(i * 0.9)
    else:
        discountedPrice.append(i)

# Выводим общую сумму скидочных цен
print(sum(discountedPrice))
