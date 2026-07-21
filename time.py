hour = int(input())
minute = int(input())
add = int(input())

# Convert current time to total minutes
total = hour * 60 + minute + add

# Keep within 24 hours
total %= (24 * 60)

# Convert back to hours and minutes
hour = total // 60
minute = total % 60

print(f"{hour:02d}:{minute:02d}")
