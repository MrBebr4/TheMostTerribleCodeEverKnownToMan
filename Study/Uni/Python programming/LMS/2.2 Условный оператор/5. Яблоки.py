# Изначальное количество яблок
petyas_apple = 7
vasyas_apple = 6
tolyas_apple = None
genas_apple = None
dimas_apple = None

# Постоянные изменения
petyas_apple = 7 - 3 + 2
vasyas_apple = 6 + 3
tolyas_apple = -4
genas_apple = +2

# Сколько дал дима
dima_gave_petya = int(input())
dima_gave_vasya = int(input())

# Изменения от димы
petyas_apple = petyas_apple + dima_gave_petya
vasyas_apple = vasyas_apple + dima_gave_vasya

# Вывод результата
if petyas_apple > vasyas_apple:
    print("Петя")
elif vasyas_apple > petyas_apple:
    print("Вася")
else:
    print("Ничья")
