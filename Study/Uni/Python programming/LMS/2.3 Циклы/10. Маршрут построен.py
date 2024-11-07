# Initialize coordinates
xcord = 0
ycord = 0

while True:
    # Read the direction input from the user
    user_input = input()

    # Check if the input is "СТОП" to break the loop immediately
    if user_input == "СТОП":
        break

    # Read the number of steps from the user
    steps = int(input())

    # Update coordinates based on the direction
    if user_input == "СЕВЕР":
        ycord += steps
    elif user_input == "ЮГ":
        ycord -= steps
    elif user_input == "ЗАПАД":
        xcord -= steps
    elif user_input == "ВОСТОК":
        xcord += steps

# Print the final coordinates
print(ycord)
print(xcord)