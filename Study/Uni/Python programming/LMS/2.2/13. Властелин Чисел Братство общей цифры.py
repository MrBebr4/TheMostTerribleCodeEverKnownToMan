elvesNumber = int(input())
gnomesNumber = int(input())
humnaNumber = int(input())
if elvesNumber and gnomesNumber and humnaNumber < 100:
    if elvesNumber % 10 == gnomesNumber % 10 == humnaNumber % 10:
        print(elvesNumber % 10)
    elif elvesNumber // 10 == gnomesNumber // 10 == humnaNumber // 10:
        print(elvesNumber // 10)
    else:
        print(0)
else:
    print("Invalid number")
    quit()