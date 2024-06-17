# Basic Arithmetic Operations

"""
Overview:
This project will involve creating a Python script that performs basic arithmetic operations (addition, subtraction, multiplication) based on user input. 
We'll break it down into stages, with each stage adding complexity to the previous one.
"""

# Stage 1: Input Handling
# Task: Write a function that prompts the user to enter two numbers and returns them as integers.

"""
Exercise:
 - Create a function named get_input() that asks the user for two numbers.
 - Use input() to capture user input and int() to convert the inputs into integers.
 - Return these two integers.
"""
def get_input():
    numbers = input("Enter two numbers separated by a space: ")
    numbers_list = numbers.split()
    return int(numbers_list[0]), int(numbers_list[1])

print(get_input())


# Stage 2: Addition
# Task: Develop a function that takes two numbers as arguments and returns their sum formatted in a descriptive string.

"""
Exercise:
- Define a function sum_numbers(number1, number2) that returns a string like "The addition of both numbers is X", where X is the sum.
"""
def sum_numbers(number1, number2):
    return f"The addition of both numbers is {number1 + number2}"

print(sum_numbers(1, 2))


# Stage 3: Subtraction
#Task: Write a function that subtracts the second number from the first and handles the case where the first number is smaller.

"""
Exercise:

- Create a function subtract_numbers(number1, number2).
- If number1 is less than number2, return a message indicating so.
- Otherwise, return the result of the subtraction in a formatted string.
"""
def subtract_numbers(number1, number2):
    if number1 < number2:
        return "Sorry number 1 is smaller than number 2"
    else:
        return f"The substraction of both numbers is {number1 - number2}"

print(subtract_numbers(1, 2))
print(subtract_numbers(2, 1))


# Stage 4: Multiplication
# Task: Define a function to multiply two numbers and return the result in a formatted string.

"""
Exercise:
Implement multiplication_numbers(number1, number2) that outputs "The multiplication of both numbers is Y".
"""
def multiplication_numbers(number1, number2):
    return f"The multiplication of both numbers is {number1 * number2}"

print(multiplication_numbers(1, 2))

# Stage 5: Integration
# Task: Combine all functions into a single script that performs all operations based on user input.

"""
Exercise:
- Use get_input() to retrieve numbers.
- Call sum_numbers, subtract_numbers, and multiplication_numbers with these numbers.
- Print the results of each operation.
"""
def get_input():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    return number1, number2

def sum_numbers(num1, num2):
    return num1 + num2

def subtract_numbers(num1, num2):
    return num1 - num2

def multiplication_numbers(num1, num2):
    return num1 * num2

def integration():
    number1, number2 = get_input()
    print(f"The sum of {number1} and {number2} is: {sum_numbers(number1, number2)}")
    print(f"The difference of {number1} and {number2} is: {subtract_numbers(number1, number2)}")
    print(f"The product of {number1} and {number2} is: {multiplication_numbers(number1, number2)}")

integration()

"""
In this code:
- The get_input function asks the user to input two numbers and returns them as a tuple.
- The sum_numbers, subtract_numbers, and multiplication_numbers functions perform the respective mathematical operations on the input numbers.
- The integration function calls get_input to get the numbers, then calls the other functions to perform the operations and print the results.

Note:
When you call a function, it executes the code inside the function and returns the result. In this case, the integration function doesn't return anything, so it returns None by default.
So, when you call integration(), it executes the code inside the function and prints the results. But when you call print(integration()), it tries to print the result of the integration function, which is None.
So, in this case, you should simply call integration() without print(), like this:

integration()

This will execute the code inside the integration function and print the results.
"""