#изначальные данные
petyasApple = 7
vasyasApple = 6
tolyasApple = None
genasApple = None
dimasApple = None

#постоянные изменения
petyasApple = 7 - 3 + 2
vasyasApple = 6 + 3
tolyasApple = -4
genasApple = +2

#сколько дал дима
dimaGavePetya = int(input())
dimaGaveVasya = int(input())

#изменения от димы
petyasApple = petyasApple + dimaGavePetya
vasyasApple = vasyasApple + dimaGaveVasya

#вывод результата
if petyasApple > vasyasApple:
    print("Петя")
elif vasyasApple > petyasApple:
    print("Вася")
else:
    print("Ничья")
