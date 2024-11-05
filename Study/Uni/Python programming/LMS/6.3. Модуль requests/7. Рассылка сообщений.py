import requests

try:
    # Get the server URL from the user
    url = input().strip()
    user_id = input().strip()
    message_template = []

    # Get the message template
    while True:
        try:
            line = input().strip()
            if line == "":
                break
            message_template.append(line)
        except EOFError:
            break

    actualUrl = f"http://{url}/users/{user_id}"

    # Make a GET request to the server
    response = requests.get(actualUrl, timeout=5)
    if response.status_code == 404:
        print("Пользователь не найден")
    else:
        response.raise_for_status()  # Check if the request was successful

        # Decode the server's response as JSON
        user = response.json()

        # Prepare the message
        message = "\n".join(message_template).format(
            id=user.get("id"),
            username=user.get("username"),
            last_name=user.get("last_name"),
            first_name=user.get("first_name"),
            email=user.get("email")
        )

        # Print the prepared message
        print(message)

except requests.exceptions.RequestException as e:
    print(f"Ошибка: {e}")
except ValueError as e:
    print(f"Ошибка обработки JSON: {e}")
except EOFError:
    print("Входные данные не получены. Достигнут конец файла.")