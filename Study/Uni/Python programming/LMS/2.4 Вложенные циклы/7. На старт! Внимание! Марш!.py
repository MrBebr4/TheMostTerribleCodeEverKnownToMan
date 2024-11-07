timesNum = int(input())
startTime = 3
for i in range(1, timesNum + 1):
    for j in range(startTime, 0, -1):
        print(f"До старта {j} секунд(ы)")
    startTime = startTime + 1
    print(f"Старт {i}!!!")
