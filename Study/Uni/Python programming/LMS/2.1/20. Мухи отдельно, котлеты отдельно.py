totalWeight = int(input())
totalPrice = int(input())
firstPrice = int(input())
secondPrice = int(input())

if firstPrice > secondPrice:
    firstWeight = int((totalPrice - secondPrice) * totalWeight / (firstPrice - secondPrice))
    secondWeight = int(totalWeight - firstWeight)
else:
    print("Invalid price")
    quit()

print(firstWeight, secondWeight)