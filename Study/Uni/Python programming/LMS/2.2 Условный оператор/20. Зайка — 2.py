creature1 = input()
creature2 = input()
creature3 = input()

creatures = [creature1, creature2, creature3]
hasZayka = []

for creature in creatures:
    if "зайка" in creature:
        hasZayka.append(creature)

if len(hasZayka) > 0:
    print(hasZayka[0], len(hasZayka[0]))
else:
    print("No 'зайка' found")