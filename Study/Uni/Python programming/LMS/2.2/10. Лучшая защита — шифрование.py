password = int(input())
num1 = str((password % 10) + (password // 10 - password // 100 * 10))
num2 = str((password // 100) + (password // 10 - password // 100 * 10))
if num1 > num2:
    print(num1+num2)
elif num1 < num2:
    print(num2+num1)