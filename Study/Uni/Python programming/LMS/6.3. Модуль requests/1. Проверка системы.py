import requests

try:
    # Отправляем GET-запрос к серверу
    response = requests.get('http://127.0.0.1:5000', timeout=5)
    response.raise_for_status()  # Проверяем, успешен ли запрос
    # Декодируем и выводим ответ сервера
    print(response.content.decode('utf-8'))
except requests.exceptions.RequestException as e:
    # Выводим сообщение об ошибке, если запрос не удался
    print(f"Произошла ошибка: {e}")