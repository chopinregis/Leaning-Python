"""
Exercise 1: Variables and Basic Operations
Create a variable age and set it to your age.
Create a variable name and set it to your name in a string.
Print a sentence using these variables that says: "My name is [Your Name] and I am [Your Age] years old."
Create a list of the first 5 even numbers and print it.
Create a dictionary representing a book with keys title, author, and year and print it.
"""

age = 35
name = "Regis"

# Print formatted string with f-string
print(f"My name is {name} and I am {age} years old")

# Create a list of even numbers
even_numbers = [2, 4, 6, 8]  
print(even_numbers)

# Create a dictionary with book information
book = {  
    "title": "Soliyana's boo",
    "author": "Regis",
    "year": "1989"
}

# Print the dictionary directly (cleaner than using f-string for this case)
print(book)

# Print a message with f-string to include the dictionary content
print(f"I just purchased '{book ['title']}' by {book ['author']} which was published in the year {book ['year']} to read.")

