### Step 2: Defining Functions
### Next, let's discuss how to define a function in Python. A function is a block of organized, reusable code that is used to perform a single, related action. Functions provide better modularity for your application and a high degree of code reusing.

### What is a function?
### A function is defined using the def keyword, followed by the function name and parentheses. Any input parameters or arguments should be placed within these parentheses. You can also define parameters inside these parentheses.

def function_name(parameters):
    """Docstring (optional)"""
    # Code block
    return output  # optional

## function_name: Name of the function.
## parameters: Optional and used to pass values to the function.
## Docstring: Optional and used to describe what the function does.
## Code block: The series of statements that define the function's operations.
## return: Optional and used to return a value from the function.

### Exercise:
### Define a function named greet that takes a name as an argument and prints "Hello, [name]!". For example, if the input is "Alice", the function should print "Hello, Alice!".

def greet(name):
	return f"Hello, {name}!"

print(greet("regis"))
print(greet("Geraldine"))

