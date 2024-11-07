def verify_blockchain():
    import sys
    input = sys.stdin.read
    data = input().split()

    # Считываем количество блоков
    N = int(data[0])
    blocks = list(map(int, data[1:]))

    previous_hash = 0

    for i in range(N):
        block = blocks[i]
        # Извлекаем хэш, случайное число и полезную информацию из блока
        hn = block % 256
        rn = (block // 256) % 256
        mn = (block // (256 * 256)) % 256

        # Вычисляем ожидаемый хэш
        expected_hash = (37 * (mn + rn + previous_hash)) % 256

        # Проверяем правильность хэша
        if hn != expected_hash or hn >= 100:
            print(i)
            return

        previous_hash = hn

    # Если все хэши правильные, выводим -1
    print(-1)

verify_blockchain()