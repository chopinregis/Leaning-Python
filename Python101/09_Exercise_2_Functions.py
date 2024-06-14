"""
Exercise 2: Writing and Using Functions
Write a function named multiply that takes two parameters and returns their product.
Call this function with two numbers of your choice and print the result.
Write a function is_even that checks whether a number is even. The function should return True if the number is even, and False otherwise.
Test this function by printing the result for 4 and 7.
"""
def multiply(num1, num2):
    return num1 * num2

print(multiply(4, 7))
print(multiply(8, 10))

def is_even(num):
    if num % 2 == 0:
        return True
    else: 
        return False
    
print(is_even(4))
print(is_even(7))