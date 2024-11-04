# Запрашиваем у пользователя год
year = int(input())

# Проверяем, является ли год високосным
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 != 0:
            print("NO")
        else:
            print("YES")
    else:
        print("YES")
else:
    print("NO")