# получаем числа разных рас
elvesNumber = int(input())
gnomesNumber = int(input())
humnaNumber = int(input())

# Проверяем, что числа не превышают 100 и в зависимости от условий выводим либо десятки, либо единицы, либо 0. Если услвоия не выполняются, выводим "Invalid number"
if elvesNumber and gnomesNumber and humnaNumber < 100:
    if elvesNumber % 10 == gnomesNumber % 10 == humnaNumber % 10:
        print(elvesNumber % 10)
    elif elvesNumber // 10 == gnomesNumber // 10 == humnaNumber // 10:
        print(elvesNumber // 10)
    else:
        print(0)
else:
    print("Invalid number")
    quit()