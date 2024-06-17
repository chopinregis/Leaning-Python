# Sum Calculation with List and sum() Function

"""
Explanation:
The sum() function in Python is used to calculate the total of all the numbers in a list. 
It’s a built-in function that makes it easy to quickly sum up iterables without needing to write a loop.
"""

"""
Example:
Here’s how you could use the sum() function to calculate the total balance given a list of numbers:
"""
def calculate_balance(numbers):
    total = sum(numbers)
    return f"Total balance: ${total:.2f}"
"""
This function takes a list of numbers as an argument and returns a formatted string showing the total in U.S. dollars, rounded to two decimal places.
"""
print(calculate_balance([100, 150, 200]))  # Output: Total balance: $450.00
print(calculate_balance([200, 400, 600]))  # Output: Total balance: $1200.00

"""
Exercise Task:
Now try writing a function called sum_expenses that takes a list of expenses and returns a string that indicates the total sum of these expenses in the format "Total expenses: $[amount]". 
Make sure to format the total as a floating point number with two decimal places.
"""
def sum_expenses(expenses):
    total = sum(expenses)
    return f"Total expenses: ${total:.2f}"

print(sum_expenses([150, 250, 300]))  # Output: Total expenses: $750.00
print(sum_expenses([300, 500, 800]))  # Output: Total expenses: $1700.00

########################################

# Note:
"""
The sum() function expects an iterable object (like a list, tuple, or string) as input, but integers themselves are not iterable.
"""

# 1. Create a List:
"""
Change the sum_exp function to take a list of expenses as input. Inside the function, unpack the list and use sum() on the individual values.
"""
def sum_exp(expenses):
    total = sum(expenses)
    return f"Total of all expenses: ${total:.2f}"

# Call the function with a list of expenses
print(sum_exp([150, 250, 300]))  # Output: Total of all expenses: $750.00

# or Enclose the expenses in a list within the sum_exp function:
def sum_exp(expense1, expense2, expense3):
    expenses = [expense1, expense2, expense3]  # Create a list
    total = sum(expenses)
    return f"Total of all expenses: ${total:.2f}"

# 2. Use the + Operator:
"""
If you specifically want to work with three separate expenses, you can simply use the addition operator (+) to calculate the total.
"""
def sum_exp(expense1, expense2, expense3):
    total = expense1 + expense2 + expense3
    return f"Total of all expenses: ${total:.2f}"

# Call the function with individual arguments
print(sum_exp(150, 250, 300))  # Output: Total of all expenses: $750.00

"""
Choosing the Right Approach:

If you plan to handle a variable number of expenses in the future, using a list as input is more flexible.
If you only need to sum three specific expenses, the + operator approach is simpler.

Additional Tips:

Consider using more descriptive variable names (e.g., expenses instead of expense1, expense2, expense3).
Always test your code with different inputs to ensure it works as expected.
By following these steps, you should be able to resolve the error and successfully calculate the sum of your expenses in Python.
"""