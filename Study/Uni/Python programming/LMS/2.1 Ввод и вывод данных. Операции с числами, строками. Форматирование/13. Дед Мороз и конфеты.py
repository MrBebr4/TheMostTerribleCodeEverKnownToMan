# запрашиваем количество детей и конфет
kids = int(input())
candy = int(input())

# расчитваем солько конфет достанется каждому ребенку и сколько конфет останется
candy_per_kid = candy // kids
candy_left = candy % kids

# выводим результат
print(candy_per_kid)
print(candy_left)