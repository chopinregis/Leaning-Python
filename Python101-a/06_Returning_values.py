### Concept: Returning Values
### In Python, the return statement is used to exit a function and optionally pass an expression back to the caller. This allows the function to produce a result that you can use later in your code.

def square(number):
    return number * number

result = square(4)
print(result)  # Outputs 16


### Exercise 6
### Write a function named add_three that takes a single parameter, adds 3 to it, and returns the result. Then, call this function with the number 7 and print the returned value.

def add_three(z):
	return z + 3

result = add_three(7)
print(result)