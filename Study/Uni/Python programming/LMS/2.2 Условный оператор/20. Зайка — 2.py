# запрашиваем три набора животных
creature1 = input()
creature2 = input()
creature3 = input()

# создаем список животных и объявляем список в котором будут строки с зайкой
creatures = [creature1, creature2, creature3]
has_zayka = []

# проверяем каждый набор на наличие зайки
for creature in creatures:
    if "зайка" in creature:
        has_zayka.append(creature)

# в зависимости от количетсва строк с зайкой выводим результат
if len(has_zayka) > 0:
    print(has_zayka[0], len(has_zayka[0]))
else:
    print("No 'зайка' found")