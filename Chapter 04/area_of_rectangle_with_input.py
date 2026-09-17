# rectangle_input.py
# Calculates area of a rectangle area user inputs.

print("Rectangle Area Calculator")

# Get length input from the user
length_str = input("Enter the length of the rectangle: ")
# Convert the input string to a float
length_float = float(length_str)

# Get width input from the user
width_str = input("Enter the width of the rectangle: ")
# Convert the input string to a float
width_float = float(width_str)

# Perform the calculation using the converted float values
area = length_float * width_float

# Display the result
print("The length is:", length_float)
print("The width is:", width_float)
print("The calculated area is:", area)