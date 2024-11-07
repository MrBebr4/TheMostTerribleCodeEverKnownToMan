# получаем числа разных рас
elves_number = int(input())
gnomes_number = int(input())
humna_number = int(input())

# Проверяем, что числа не превышают 100 и в зависимости от условий выводим либо десятки, либо единицы, либо 0. Если услвоия не выполняются, выводим "Invalid number"
if elves_number and gnomes_number and humna_number < 100:
    if elves_number % 10 == gnomes_number % 10 == humna_number % 10:
        print(elves_number % 10)
    elif elves_number // 10 == gnomes_number // 10 == humna_number // 10:
        print(elves_number // 10)
    else:
        print(0)
else:
    print("Invalid number")
    quit()