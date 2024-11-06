# Isabell Mora
# UWYO COSC 1010
# 11-05-24
# Lab 08
# Lab Section: 11
# Sources, people worked with, help given to:
# your
# comments
# here
# Write a function that will properly check strings to see if they are an int or
# float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float
# Floats should only have one decimal point in them
def con_to_int(x):
    """Checking for integer"""
    if x.isdigit() or (x[0] == '-' and x[1:].isdigit()):
        return int(x)
    if x.count('.') == 1:
        left, right = x.split('.')
        if (left.isdigit()) or (left[0] == '-' and left[1:].isdigit()) and right.isdigit():
            return float(x)
    return False
print(type(con_to_int("5")))
print(type())
print("*" * 75)
# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to
#evaluate
# Create a function slope_intercept that takes in four parameters
# m, the slope
# b, the intercept
# a lower x bound
# an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number
#X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false
# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list
print("*" * 75)
def slope_inter(m, b, x_lower, x_upper):
    """Checking if bounds are integers"""
    if x_lower is False or x_upper is False or x_lower > x_upper:
        return False
    """Calculating the y value from given values"""
    y_result = []
    for x in range(x_lower, x_upper + 1):
        y = m * x + b
        y_result.append(y)
    return y_result

result = False
while True:
    while True:
        m_input = input("Enter a valid integer for the slope (m) or type 'exit' to quit: ")
        if m_input.lower() == "exit":
            break
        m = con_to_int(m_input)
        if m is not False:
            break
        print("Invalid input. Please enter a valid integer.")
    if m_input.lower() == "exit":
        break

    while True:
        b_input = input("Enter a valid integer for the y-intercept (b) or type 'exit' to quit: ")
        if b_input.lower() == "exit":
            break
        b = con_to_int(b_input)
        if b is not False:
            break
        print("Invalid input. Please enter a valid integer.")
    if b_input.lower() == "exit":
        break

    while True:
        x_lower_input = input("Enter a valid integer for the lower x bound or type 'exit' to quit: ")
        if x_lower_input.lower() == "exit":
            break
        x_lower = con_to_int(x_lower_input)
        if x_lower is not False:
            break
        print("Invalid input. Please enter a valid integer.")
    if x_lower_input.lower() == "exit":
        break

    while True:
        x_upper_input = input("Enter a valid integer for the upper x bound or type 'exit' to quit: ")
        if x_upper_input.lower() == "exit":
            break
        x_upper = con_to_int(x_upper_input)
        if x_upper is not False:
            break
        print("Invalid input. Please enter a valid integer.")
    if x_upper_input.lower() == "exit":
        break

    if x_lower > x_upper:
        print("Invalid bounds: the lower bound should be less than or equal to the upper bound.")
    else:
        result = slope_inter(m, b, x_lower, x_upper)
        break

if result is False:
    print("Please enter valid bounds: ensure that the lower bound is <= to the upper bound")
else:
    print(f"Y-values for x bounds {x_lower} to {x_upper} are: {result}")

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation
# If the number you are trying to take the square root of is negative, return
#null

def pos_squrt(value):
    if value < 0:
        return None
    return value ** 0.5

def squrt(a,b,c):
    """Function for calculating the squareroot for non-negatives"""
    function = b**2 - 4 * a * c
    squrt_calc = pos_squrt(function)
    
    if squrt_calc is None:
        return None

    squrt1 = (-b + squrt_calc) / (2 * a)
    squrt2 = (-b - squrt_calc) / (2 * a)
    return squrt1, squrt2

while True:
    while True:
        a_input = input("Enter a non_zero value for a or type 'exit': ")
        if a_input.lower() == "exit":
            exit()
        a = con_to_int(a_input)
        if a is not False or a != 0:
            break
        print("Please enter valid integer for a")
    while True:
        b_input = input("Enter a value for b or type 'exit': ")
        if b_input.lower() == "exit":
            exit()
        b = con_to_int(b_input)
        if b is not False:
            break
        print("Please enter valid integer for b")
    while True:
        c_input = input("Enter a value for c or type 'exit': ")
        if c_input.lower() == "exit":
            exit()
        c = con_to_int(c_input)
        if c is not False:
            break
    #a = con_to_int(a_input)
    #b = con_to_int(b_input)
    #c = con_to_int(c_input)
    
    #if a is False or b is False or c is False:
        #print("Please enter valid numbers for a, b, c")
        #continue
    result = squrt(a,b,c) 
    if result is None:
        print("No real root exists")
    else:
        squrt1, squrt2 = result
        print(f"The roots are: {squrt1} , {squrt2}")



        
