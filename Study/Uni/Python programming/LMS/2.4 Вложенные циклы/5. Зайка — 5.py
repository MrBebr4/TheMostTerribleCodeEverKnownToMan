places = int(input())
creatures = ""
placesList = []
timesAmount = 0

for i in range(places):
    while True:
        creatures = input()
        if "ВСЁ" in creatures:
            break
        placesList.append(creatures)
        creatures = ""

for j in placesList:
    if "зайка" in j:
        timesAmount += 1

print(timesAmount)