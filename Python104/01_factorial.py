# factorial_number = input("enter a number you want to factorialize: ")


"""
factorial = 1
for i in range(1, int(factorial_number) + 1):
    factorial *= i

print(factorial)
"""

# factorial = n*(n-1)

# for i in range(1, int(factorial_number) + 1):
"""  
num = int(input("Enter The Number to show its factorial: "))
fact = 1
for x in range(1, num+1):
    fact *= x
print(f"The factorial of the number {num} is {fact}")
"""
while True:
    num = int(input("Enter The Number to show its factorial (or enter -1 to stop): "))
    if num == -1:
        break
    fact = 1
    for x in range(1, num+1):
        fact *= x
    print(f"The factorial of the number {num} is {fact}")
