import requests

# Получаем URL сервера от пользователя
url = input().strip()
actualUrl = f"http://{url}"

# Получаем ключ от пользователя
key = input().strip()

try:
    # Сделать GET-запрос к серверу
    response = requests.get(actualUrl, timeout=5)
    response.raise_for_status()  # Проверить, успешен ли запрос

    # Декодировать ответ сервера как JSON
    responseJson = response.json()

    # Проверить наличие ключа в JSON объекте и вывести значение
    if key in responseJson:
        print(responseJson[key])
    else:
        print("No data")

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
except ValueError as e:
    print(f"Error processing JSON: {e}")