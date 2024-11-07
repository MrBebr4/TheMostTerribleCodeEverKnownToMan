def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        while (n % i) == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors

# Считываем введенное число
number = int(input().strip())

# Получаем простые множители
factors = prime_factors(number)

# Выводим результат
print(' * '.join(map(str, factors)))