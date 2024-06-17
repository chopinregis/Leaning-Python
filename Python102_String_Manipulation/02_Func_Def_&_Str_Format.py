# Function Definition and String Formatting

"""
Explanation:
Functions in Python are defined using the 'def' keyword, followed by the function name and parentheses containing any parameters the function will take. 
Inside the function, you can execute any number of statements and return a value using the return statement.

String formatting, particularly using f-strings, allows you to easily insert variables into strings. 
An f-string is denoted by prefixing the string with f and using curly braces {} to include variables.
"""

"""
Example:
Here’s a simple example of a function that uses string formatting to greet a user:
"""
def greet(name):
    return f"Hello, {name}! How are you today?"

"""
If you call this function with the name "Alice", like so: greet("Alice"), it will return: "Hello, Alice! How are you today?"
"""
print(greet("Alice"))  # Output: Hello, Alice! How are you today?
print(greet("Bob"))  # Output: Hello, Bob! How are you today?
print(greet("Charlie"))  # Output: Hello, Charlie! How are you today?
print(greet("David"))  # Output: Hello, David! How are you today?

"""
Exercise Task:
Now it’s your turn to practice. 
Write a function named welcome_message that takes two parameters: a name and a city. The function should return a string that says "Welcome [name] to [city]!" using string formatting. For example, if you pass "John" and "New York" to the function, it should return "Welcome John to New York!"
"""

def welcome_message(name, city):
	return f"Welcome {name} to {city}!"

print(welcome_message("John", "New York"))
print(welcome_message("Regis", "Los Angeles"))
print(welcome_message("Emy", "Montreal"))

def welcome_message(name, city, nation, continent):
	return f"Welcome {name} to {city} which is in the {nation} nation, located on {continent} continent!"

print(welcome_message("John", "New York", "American", "North-American"))
print(welcome_message("Regis", "Douala", "Cameroonian", "African"))
print(welcome_message("Emy", "Paris", "French", "European"))