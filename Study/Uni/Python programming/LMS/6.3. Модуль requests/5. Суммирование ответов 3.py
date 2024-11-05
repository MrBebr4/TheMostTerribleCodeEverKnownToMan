import requests

try:
    # Get the server URL from the user
    url = input().strip()
    actualUrl = f"http://{url}"

    # Get the list of paths from the user
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
            # Make a GET request to the server for each path
            response = requests.get(f"{actualUrl}{path}", timeout=5)
            response.raise_for_status()  # Check if the request was successful

            # Decode the server response as JSON
            responseJson = response.json()

            # Check if the response is a list and contains only numbers
            if isinstance(responseJson, list):
                filteredResponse = [item for item in responseJson if isinstance(item, (int, float))]
                totalSum += sum(filteredResponse)

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Error processing JSON: {e}")

    # Print the total sum
    print(totalSum)

except EOFError:
    print("No input received. End of file reached.")