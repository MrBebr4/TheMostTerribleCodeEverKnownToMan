# Read the average speeds of Petya, Vasya, and Tolya
petya_speed = int(input())
vasya_speed = int(input())
tolya_speed = int(input())

# Create a list of speeds
speeds = [petya_speed, vasya_speed, tolya_speed]

# Sort the list by speed in descending order
speeds.sort(reverse=True)

# Print the sorted speeds
for i, speed in enumerate(speeds, start=1):
    print(f"{i}. {speed}")