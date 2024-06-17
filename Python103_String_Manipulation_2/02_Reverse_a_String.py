# Let's break down the problem of reversing a string into smaller, manageable parts. We'll create a series of exercises to help you build your understanding gradually.

"""
Exercise 1: Reverse a Single Character

Write a function that takes a single character as input and returns the same character. This will help you get comfortable with the syntax and basic structure of a function.
"""

# Example 1: Reverse a Single Character
def single_char(char):
    return char
print(single_char("a"))
print(single_char("b"))

"""
Exercise 2: Reverse a Short String

Write a function that takes a short string (e.g., 3-5 characters) as input and returns the reversed string. You can use the single_char function from Exercise 1 as a building block.
"""

# Example 2: Reverse a Short String
def short_string(string):
    return string[::-1]
print(short_string("abcd"))
print(short_string("wxyz"))
print(short_string("regis"))
print(short_string("lydie"))

def short_string(s):
    # Use single_char to reverse the string
    return "".join([single_char(c) for c in s[::-1]])

print(short_string("abcd"))

"""
Exercise 3: Reverse a Long String

Write a function that takes a long string (e.g., >5 characters) as input and returns the reversed string. You can use the single_char function from Exercise 1 as a building block.
"""

# Example 3: Reverse a Long String
def long_string(string):
    return string[::-1]
print(long_string("abcd"))
print(long_string("regis"))
print(long_string("lydie"))
print(long_string("The quick brown fox jumps over the lazy dog"))

def long_string(s):
    # Use short_string to reverse the string
    return short_string(s[:5]) + short_string(s[5:10]) + short_string(s[10:])
print(long_string("abcd"))
print(long_string("The quick brown fox jumps over the lazy dog"))

#########################################################################

def reverse_string(s):
    """
    Reverses the input string using Python's slicing feature.

    Parameters:
    s (str): The input string to be reversed.

    Returns:
    str: The reversed string.

    Breaking Down the Code:
    - `def` keyword defines a function in Python.
    - `reverse_string` is the name of the function.
    - `s` is the parameter, expected to be a string.
    - `return` statement gives back the reversed string.
    - `s[::-1]` is a slicing operation that reverses the string.

    How to Think About This Function:
    When you want to reverse a string in Python, using slicing is a very concise and efficient way. The `reverse_string` function encapsulates this operation, making it reusable and easy to read.

    Exercise to Practice:
    Try to solve the following exercise using the `reverse_string` function:
    Exercise: Write a function that takes a sentence as input, reverses each word in the sentence, but keeps the words in their original order. For example, "hello world" becomes "olleh dlrow".
    This exercise will help you practice string manipulation and understand how functions can be used to build more complex logic from simple operations.
    """
    return s[::-1]

# Ex excercise:
def reverse_string(string):
	return string[::-1] # Reverse the string

print(reverse_string("I love food"))  # Output: "doof evol I"

"""
Exercise:
Try modifying the function to reverse each word in a sentence individually, but keep the words in the original order. This exercise will help you practice string manipulation further and test your understanding of function calls and string operations.
"""

def reverse_sentence(sentence):
    reversed_words = []  # Create an empty list to hold the reversed words
    for word in sentence.split():  # Split the sentence into words
        reversed_words.append(word[::-1])  # Reverse each word and append to the list
    return ' '.join(reversed_words)  # Join the reversed words back into a sentence

print(reverse_sentence("I love food very much"))

# Output: "much very much food love I"