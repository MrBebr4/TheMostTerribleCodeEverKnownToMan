numInp = int(input())
num3 = numInp % 10
num2 = numInp // 10 % 10
num1 = numInp // 100
sumNum = num1 + num3

if sumNum == (num2 * 2):
    print("YES")
else:
    print("NO")