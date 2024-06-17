"""
Exercise 4: Exception Handling Practice
Write a function that takes two parameters, dividend and divisor.
In the function, attempt to divide dividend by divisor.
Use a try-except block to catch a division by zero error.
Return the result of the division if successful, or a message saying "Cannot divide by zero" if a division by zero error occurs.
Test your function by calling it with 10 as the dividend and 0 as the divisor, and then with 10 and 2
"""

def divide(dividend, divisor):
    try:
        return dividend / divisor
    except ZeroDivisionError:
        return "Cannot divide by zero"  # Now returning a string instead of printing

# Store the results in variables and print them
result1 = divide(10, 0)
result2 = divide(10, 2)
print("Result of 10 / 0 is:", result1)
print("Result of 10 / 2 is:", result2)
