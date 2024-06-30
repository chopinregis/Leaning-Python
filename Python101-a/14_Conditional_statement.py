### Concept: Conditional Statements
### Conditional statements in Python are used to execute different actions based on different conditions. The if statement is the simplest form, but you can also have elif (else if) and else for additional condition checks.

temperature = 20
if temperature > 25:
    print("It's hot today.")
elif temperature < 15:
    print("It's cold today.")
else:
    print("It's mild today.")

### Exercise 9: Conditional Statements
### Write a program that checks the variable age. If age is under 13, print "You are a child." If age is between 13 and 19, print "You are a teenager." Otherwise, print "You are an adult." Assume age is 18 for testing purposes.

age = 18
if age < 13:
	print("You are a child!")
elif age >= 13 and age <= 19:
	print("You are a teenager")
else:
	print("You are an adult")
