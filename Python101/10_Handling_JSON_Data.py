"""
Let's move to a very relevant topic for AWS Lambda: handling JSON data. JSON (JavaScript Object Notation) is a lightweight data interchange format that's easy for humans to read and write, and easy for machines to parse and generate.

Python has a built-in module called json that allows you to parse JSON strings and files into Python dictionaries, and vice versa.
"""
# Example of JSON Handling:

import json

# Convert from JSON to Python (Deserialization)
json_string = '{"name": "Alice", "age": 25, "city": "Wonderland"}'
data = json.loads(json_string)
print(data['name'])  # Output: Alice

# Convert from Python to JSON (Serialization)
python_dict = {'name': 'Bob', 'age': 30, 'city': 'Builderland'}
json_output = json.dumps(python_dict)
print(json_output)  # Output: {"name": "Bob", "age": 30, "city": "Builderland"}
