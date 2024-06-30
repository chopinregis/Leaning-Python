### Concept: List Comprehension
### List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# Create a new list where each number is squared from the original list
numbers = [1, 2, 3, 4, 5]
squared_numbers = [number ** 2 for number in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

### Exercise 3: List Comprehension
### Using the colors list, create a new list called uppercase_colors that contains all colors converted to uppercase. Use list comprehension to achieve this and then print uppercase_colors.

colors = ["red", "green", "blue"]
print(colors)

for color in colors:
	print(f"Color: {color}")

uppercase_colors = [color.upper() for color in colors]
print(uppercase_colors)

lowercase_colors = [color.lower() for color in colors]
print(lowercase_colors)

capitalizes = [color.title() for color in colors]
print(capitalizes)