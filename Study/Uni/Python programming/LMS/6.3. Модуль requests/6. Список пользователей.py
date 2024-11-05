import requests

try:
    # Получить URL сервера от пользователя
    url = input().strip()
    actualUrl = f"http://{url}/users"

    # Сделать GET-запрос к серверу
    response = requests.get(actualUrl, timeout=5)
    response.raise_for_status()  # Проверить, успешен ли запрос

    # Декодировать ответ сервера как JSON
    users = response.json()

    # Проверить, что ответ является списком
    if isinstance(users, list):
        # Сортировать пользователей по фамилии и имени
        sorted_users = sorted(users, key=lambda x: (x['last_name'], x['first_name']))

        # Вывести список пользователей
        for user in sorted_users:
            print(f"{user['last_name']} {user['first_name']}")

except requests.exceptions.RequestException as e:
    print(f"Ошибка: {e}")
except ValueError as e:
    print(f"Ошибка обработки JSON: {e}")
except EOFError:
    print("Входные данные не получены. Достигнут конец файла.")