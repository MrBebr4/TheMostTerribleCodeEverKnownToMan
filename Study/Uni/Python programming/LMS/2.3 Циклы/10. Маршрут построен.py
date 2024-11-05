# Initialize coordinates
xcord = 0
ycord = 0

while True:
    # Read the direction input from the user
    userInput = input()

    # Check if the input is "СТОП" to break the loop immediately
    if userInput == "СТОП":
        break

    # Read the number of steps from the user
    steps = int(input())

    # Update coordinates based on the direction
    if userInput == "СЕВЕР":
        ycord += steps
    elif userInput == "ЮГ":
        ycord -= steps
    elif userInput == "ЗАПАД":
        xcord -= steps
    elif userInput == "ВОСТОК":
        xcord += steps

# Print the final coordinates
print(ycord)
print(xcord)