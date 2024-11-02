# Read the average speeds of Petya, Vasya, and Tolya
petya_speed = int(input())
vasya_speed = int(input())
tolya_speed = int(input())

# Create a list of tuples with names and their corresponding speeds
participants = [("Петя", petya_speed), ("Вася", vasya_speed), ("Толя", tolya_speed)]

# Sort the list by speed in descending order
participants.sort(key=lambda x: x[1], reverse=True)

# Print the names in the order they finish
for i, participant in enumerate(participants, start=1):
    print(f"{i}. {participant[0]}")