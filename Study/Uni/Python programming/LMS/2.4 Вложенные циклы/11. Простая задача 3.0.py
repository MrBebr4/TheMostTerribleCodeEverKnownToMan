def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Считываем количество чисел
n = int(input())

# Инициализируем счетчик простых чисел
prime_count = 0

# Считываем числа и проверяем, являются ли они простыми
for _ in range(n):
    number = int(input())
    if is_prime(number):
        prime_count += 1

# Выводим количество простых чисел
print(prime_count)