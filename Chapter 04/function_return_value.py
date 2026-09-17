# function_return_value.py

# --- Function Definition with return 
def add_numbers(num1, num2):
    total = num1 + num2
    return total # Return the calculated sum

# --- Main part of the program ---
# Call the function and store the returned value in a variable
sum_result = add_numbers(15, 7)
print("The function add_numbers(15, 7) returned:", sum_result)

# You can also use the return value directly in expressions
print("The sum of 1.2 and 3.4 is:", add_numbers(1.2, 3.4))