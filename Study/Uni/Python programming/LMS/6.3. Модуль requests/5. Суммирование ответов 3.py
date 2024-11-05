import requests

try:
    # Получить URL сервера от пользователя
    url = input().strip()
    actualUrl = f"http://{url}"

    # Получить список путей от пользователя
    paths = []
    while True:
        try:
            path = input().strip()
            if path == "":
                break
            paths.append(path)
        except EOFError:
            break

    totalSum = 0

    for path in paths:
        try:
            # Сделать GET-запрос к серверу для каждого пути
            response = requests.get(f"{actualUrl}{path}", timeout=5)
            response.raise_for_status()  # Проверить, успешен ли запрос

            # Декодировать ответ сервера как JSON
            responseJson = response.json()

            # Проверить, что ответ является списком и содержит только числа
            if isinstance(responseJson, list):
                filteredResponse = [item for item in responseJson if isinstance(item, (int, float))]
                totalSum += sum(filteredResponse)

        except requests.exceptions.RequestException as e:
            print(f"Ошибка: {e}")
        except ValueError as e:
            print(f"Ошибка обработки JSON: {e}")

    # Вывести общую сумму
    print(totalSum)

except EOFError:
    print("Входные данные не получены. Достигнут конец файла.")