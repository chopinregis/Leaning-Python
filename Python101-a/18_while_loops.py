## Concept: While Loops
## A while loop in Python repeats a block of code as long as a certain condition is true. It's useful when you don't know beforehand how many times you need to iterate.

# Counting up to five
count = 1
while count <= 5:
    print(count)
    count += 1  # This is the same as count = count + 1

## Exercise 1: While Loops
## Write a while loop that starts with a number x at 10 and decreases it by 1 each time through the loop until x is 0.

x = 10
while x >= 0:
    print(x)
    x -= 1

# in case there is a +=, add a break to stop the code from running indefinitely
x = 10
while x >= 0:
  print(x)
  x += 1  # This line actually increments x to 11 after the first iteration
  if x > 10:  # Add this condition to break out of the loop
    break
