askTimes = int(input())
numes = []

for i in range(askTimes):
    currentNum = int(input())
    numes.append(currentNum)
print(sum(numes))
