"""
Exercise 3: JSON Serialization and Deserialization
Write a Python dictionary that represents a person with a name, age, and favorite_color.
Convert this dictionary to a JSON string and print it.
Take the JSON string from step 2, parse it back into a Python dictionary, and print the name and favorite_color.
"""
import json

python_dict = {'name': 'Benoit', 'age': 35, 'favorite_color': 'green'}

# Convert the dictionary to a JSON string using json.dumps
json_string = json.dumps(python_dict)
print(json_string)  # Output: {"name": "Benoit", "age": 35, "favorite_color": "green"}

# Convert the JSON string back to a Python dictionary using json.loads
python_dict = json.loads(json_string)
print(python_dict)  # Output: {'name': 'Benoit', 'age': 35, 'favorite_color': 'green'}

# Print the name and favorite_color
print(python_dict['name'])  # Output: Benoit
print(python_dict['favorite_color'])  # Output: green
print(f"my name is {python_dict['name']} and my favorite color is {python_dict['favorite_color']}")