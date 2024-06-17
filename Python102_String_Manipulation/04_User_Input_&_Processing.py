# User Input and Processing
"""
Explanation:
This concept involves getting a string input from the user, processing it to convert it into a list of integers, and then calculating the sum. 
It demonstrates using input handling, string splitting, mapping, and list conversion, all integral for data processing tasks in Python.
"""
# Example:

def process_input():
    numbers = input("Enter numbers separated by spaces: ")
    number_list = map(int, numbers.split())
    total = sum(number_list)
    return f"Total sum: {total}"

print(process_input())
"""
This function asks the user to enter numbers separated by spaces, splits the input into a list of strings, converts each string into an integer, and calculates the total sum.
"""


"""
Exercise Task:
Write a function that prompts the user to input numbers separated by a comma, processes this input to convert it into a list of integers, and returns the sum. 
Name the function sum_comma_separated_input. Be sure to convert the split results appropriately and handle potential spaces after commas.
"""
def sum_comma_separated_input():
    numbers = input("Enter numbers separated by commas: ")
    number_list = map(int, numbers.split(","))
    total = sum(number_list)
    return f"Total sum: {total}"

print(sum_comma_separated_input())