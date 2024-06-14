"""
1. Basic Syntax and Data Types
Understanding Python’s basic syntax, data types (like strings, integers, lists, and dictionaries), and control structures (like if statements, for and while loops) is crucial. Lambda functions often process data that comes in the form of JSON, which maps directly to Python’s dictionaries and lists.
"""

"""
2. Functions
Since AWS Lambda uses the concept of a function as a service, knowing how to define and use functions in Python is essential. You should be comfortable with defining functions using def and return, as well as understanding parameters and return values.
"""

def hello(name):
    return f"Hello, {name}!"

print(hello("Alice"))  # Output: "Hello, Alice!"

"""
3. Handling JSON Data
Many Lambda functions process JSON data, especially when triggered by other AWS services like S3 or API Gateway. You should know how to parse JSON data and serialize it back to a string format. Python’s json library is very helpful for this.
"""

import json

# Parsing JSON string to a Python dictionary
data = json.loads('{"name": "John", "age": 30}')
print(data['name'])  # Output: John

# Converting Python dictionary to JSON string
json_string = json.dumps(data)
print(json_string)  # Output: {"name": "John", "age": 30}

"""
4. Error Handling
When working with cloud functions, handling exceptions is vital to deal with unexpected issues gracefully. Using try, except, and finally blocks can help manage exceptions that may occur during the execution of your function.
"""

try:
    # Code that might throw an exception
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("This code runs no matter what")

"""
5. Logging
For debugging and monitoring Lambda functions, proper logging is essential. Python’s logging module allows you to log messages that can be monitored through CloudWatch.
"""
import logging

logging.basicConfig(level=logging.INFO)

def lambda_handler(event, context):
    logging.info("This is an info message")
    return "Hello, world!"

