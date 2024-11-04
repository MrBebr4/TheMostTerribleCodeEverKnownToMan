# получаем длины трех труб
tube1 = int(input())
tube2 = int(input())
tube3 = int(input())

# Проверяем, можно ли из трех труб сделать треугольник
if tube1 + tube2 > tube3 and tube1 + tube3 > tube2 and tube2 + tube3 > tube1:
    print("YES")
else:
    print("NO")