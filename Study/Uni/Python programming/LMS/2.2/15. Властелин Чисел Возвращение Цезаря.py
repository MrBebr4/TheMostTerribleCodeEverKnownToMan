firstNum = int(input())
secondNum = int(input())

if firstNum and secondNum < 100:
    pass
else:
    print("Invalid number")
    quit()

firstNum1 = firstNum // 10
firstNum3 = firstNum % 10

secondNum1 = secondNum // 10
secondNum3 = secondNum % 10

nums = [firstNum1, firstNum3, secondNum1, secondNum3]
maxNum = max(nums)
minNum = min(nums)
middleNum = sum(nums) - maxNum - minNum

print(maxNum * 100 + middleNum * 10 + minNum)