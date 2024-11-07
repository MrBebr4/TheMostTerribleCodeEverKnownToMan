def guess_number():
    low, high = 1, 1000
    attempts = 0

    while attempts < 10:
        guess = (low + high) // 2
        print(guess)
        response = input().strip()

        if response == "Угадал!":
            break
        elif response == "Больше":
            low = guess + 1
        elif response == "Меньше":
            high = guess - 1

        attempts += 1

guess_number()