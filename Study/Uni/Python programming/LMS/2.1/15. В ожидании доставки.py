hours = int(input())
minutes = int(input())
timeUpTo = int(input())

mins = (minutes + timeUpTo) % 60
hours = ((hours % 24) + (timeUpTo + minutes) // 60)
mins = str(mins)
mins.zfill(2)


print(f"{hours}:{mins}")
