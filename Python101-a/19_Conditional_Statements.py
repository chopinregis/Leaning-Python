### Concept: If, Elif, and Else Statements
### These are conditional statements that allow your program to execute different blocks of code based on different conditions.

age = 18
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")

### Exercise 2: Conditional Statements
### Create a variable temperature and set it to a value. Write a series of if, elif, and else statements to print:

### - "It's hot" if the temperature is above 30.
### - "It's warm" if the temperature is between 20 and 30.
### - "It's cold" if the temperature is below 20.

temperature = 25
if temperature >= 30:
	print("It's hot")
elif temperature >= 20 and temperature <= 30:
	print("It's warm")
else:
	print("It's cold")

# or insteand of using 'and'

temperature = 25  # You can change this value to test different outputs
if temperature > 30:
    print("It's hot")
elif temperature >= 20:
    print("It's warm")
else:
    print("It's cold")
