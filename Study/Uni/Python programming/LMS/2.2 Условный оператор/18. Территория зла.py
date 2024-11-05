# Запрашиваем длины сторон треугольника
first = int(input())
second = int(input())
third = int(input())

# Проверяем, является ли треугольник прямоугольным
if first**2 + second**2 == third**2 or first**2 + third**2 == second**2 or second**2 + third**2 == first**2:
    print("100%")
# Проверяем, является ли треугольник остроугольным
elif first**2 + second**2 > third**2 and first**2 + third**2 > second**2 and second**2 + third**2 > first**2:
    print("крайне мала")
# Если не прямоугольный и не остроугольный, значит тупоугольный
else:
    print("велика")