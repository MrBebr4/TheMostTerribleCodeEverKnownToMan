import requests

# Получаем URL сервера от пользователя
url = input("")
actualUrl = f"http://{url}"

totalSum = 0

while True:
    try:
        # Сделать GET-запрос к серверу
        response = requests.get(actualUrl, timeout=5)
        response.raise_for_status()  # Проверить, успешен ли запрос

        # Декодировать ответ сервера
        responseText = response.content.decode('utf-8').strip()

        # Конвертировать ответ в число
        number = int(responseText)

        # Если число 0, то завершить цикл
        if number == 0:
            break

        # Добавить число к общей сумме
        totalSum += number

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        break
    except ValueError as e:
        print(f"Error processing number: {e}")
        break

# Вывести общую сумму
print(totalSum)