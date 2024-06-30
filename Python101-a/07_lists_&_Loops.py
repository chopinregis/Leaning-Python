### Concept: Lists
### A list in Python is used to store multiple items in a single variable. Lists are created using square brackets [].

fruits = ["apple", "banana", "cherry"]
print(fruits)

### Exercise 1: Lists
### Create a list named colors containing the strings "red", "green", and "blue". Then, print the list.

colors = ["red", "green", "blue"]
print(colors)

print(f"i like to eat {fruits[0]} fruits")
print(f"my favorite color is {colors[1]} and my favorite fruit is {fruits[2]}")

for color in colors:
	print(color)

for fruit in fruits:
	print(fruit)

### Exercise 2: Loops
### Write a for loop that iterates through the colors list you created and prints each color prefixed with the phrase "Color: ".

for color in colors:
	print(f"Color: {color}")