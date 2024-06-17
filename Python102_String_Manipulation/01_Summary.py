# 1. Function Definition and String Formatting
def greet(name):
    return f"Hello, {name}!"

# Using the function
print(greet("Alice"))  # Output: Hello, Alice!

"""
In this example, the function greet takes a single parameter name and uses f-string formatting to insert the name into a greeting message. 
F-strings (formatted string literals) allow for easy and readable string interpolation.
"""

# 2. Sum Calculation with List and sum() Function

# Now, let's create a function that takes a list of numbers as an argument and returns a formatted string indicating the balance. 
# We'll use the sum() function to calculate the total.
def calculate_balance(numbers):
    total = sum(numbers)
    return f"Total balance: ${total:.2f}"

# Using the function
print(calculate_balance([100, 150, 200]))  # Output: Total balance: $450.00

"""
Here, sum(numbers) calculates the sum of all elements in the list numbers. 
The string is formatted to show the total balance with two decimal places.
"""

# 3. User Input and Processing

# Finally, let's handle user input, process it, and calculate the sum of a list of numbers. 
# We'll streamline the process into an efficient one-liner.

# Combined single-line version
def process_input():
    total = sum(map(int, input("Enter numbers separated by space: ").split()))
    return f"Total sum: {total}"

# Using the function
print(process_input())

"""
In this code:

input() function gets user input as a string.
split() divides the input string into a list of substrings.
map(int, ...) converts each substring to an integer.
sum(...) calculates the total sum of these integers.
This example demonstrates how to efficiently chain these functions in a single line to process user input and calculate a sum.
"""