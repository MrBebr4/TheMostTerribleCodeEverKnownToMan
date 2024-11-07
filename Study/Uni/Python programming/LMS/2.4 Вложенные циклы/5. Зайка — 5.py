places = int(input())
creatures = ""
places_list = []
times_amount = 0

for i in range(places):
    while True:
        creatures = input()
        if "ВСЁ" in creatures:
            break
        places_list.append(creatures)
        creatures = ""

for j in places_list:
    if "зайка" in j:
        times_amount += 1

print(times_amount)