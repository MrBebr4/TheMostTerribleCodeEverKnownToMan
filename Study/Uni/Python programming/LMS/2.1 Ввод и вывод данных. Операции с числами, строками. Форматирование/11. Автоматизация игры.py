# Запрашивает у пользователя 4-х значное число
num = input()

# Делит введенное число на 4 цифры
one = num[3]
two = num[2]
three = num[1]
four = num[0]

# Выводит на консоль 4 цифры в обратном порядке
print(f"{one}{two}{three}{four}")
