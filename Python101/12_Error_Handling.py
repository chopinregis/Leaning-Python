"""
Error Handling
With a solid understanding of JSON handling, let's move on to another crucial aspect of writing robust Python code, especially in cloud environments like AWS Lambda—error handling.

Python uses try-except blocks to handle exceptions, which are errors detected during execution. Proper error handling is essential to ensure your applications can gracefully handle unexpected situations.
"""

# Basic Structure of Try-Except:

try:    
    # Code that might cause an exception
    result = 10 / 0
except ZeroDivisionError:
    print("Attempted to divide by zero.")
    print("You can't divide by zero!")
else:
    print("Everything went well!")
finally:
    print("This code runs no matter what")