times_ask = int(input())
polindromes = []
for _ in range(times_ask):
    number = input()
    if number == number[::-1]:
        polindromes.append(number)
    else:
        pass

print(len(polindromes))