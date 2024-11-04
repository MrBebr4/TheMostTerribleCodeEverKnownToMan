# Изначальное количество яблок
petyasApple = 7
vasyasApple = 6
tolyasApple = None
genasApple = None
dimasApple = None

# Постоянные изменения
petyasApple = 7 - 3 + 2
vasyasApple = 6 + 3
tolyasApple = -4
genasApple = +2

# Сколько дал дима
dimaGavePetya = int(input())
dimaGaveVasya = int(input())

# Изменения от димы
petyasApple = petyasApple + dimaGavePetya
vasyasApple = vasyasApple + dimaGaveVasya

# Вывод результата
if petyasApple > vasyasApple:
    print("Петя")
elif vasyasApple > petyasApple:
    print("Вася")
else:
    print("Ничья")
