import requests

# Получаем URL сервера от пользователя
url = input("")
actualUrl = f"http://{url}"

totalSum = 0

try:
    # Сделать GET-запрос к серверу
    response = requests.get(actualUrl, timeout=5)
    response.raise_for_status()  # Проверить, успешен ли запрос

    # Декодировать ответ сервера как JSON
    responseText = response.json()

    # Конвертировать ответ в числа и отфильтровать только целые числа
    filteredResponseText = [item for item in responseText if isinstance(item, int)]

    # Добавить числа к общей сумме
    totalSum += sum(filteredResponseText)

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
except ValueError as e:
    print(f"Error processing number: {e}")

# Вывести общую сумму
print(totalSum)