import math

# Get input from user
side_length = float(input("Enter the length of one side of the tetrahedron: "))

# Calculate volume of tetrahedron
volume = (side_length ** 3) / (6 * math.sqrt(2))

# Round result to 3 decimal places
volume = round(volume, 3)

# Print result
print("The volume of the tetrahedron is:", volume)
