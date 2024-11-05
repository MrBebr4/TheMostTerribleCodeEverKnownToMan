# запрашиваем три набора животных
creature1 = input()
creature2 = input()
creature3 = input()

# создаем список животных и объявляем список в котором будут строки с зайкой
creatures = [creature1, creature2, creature3]
hasZayka = []

# проверяем каждый набор на наличие зайки
for creature in creatures:
    if "зайка" in creature:
        hasZayka.append(creature)

# в зависимости от количетсва строк с зайкой выводим результат
if len(hasZayka) > 0:
    print(hasZayka[0], len(hasZayka[0]))
else:
    print("No 'зайка' found")