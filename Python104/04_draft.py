def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Test the function
print(is_prime(3))  # True
print(is_prime(5))  # True
print(is_prime(7))  # True
print(is_prime(23)) # True
print(is_prime(10)) # False

###################################
def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence[:n]

# Test the function
print(fibonacci(5))  # [0, 1, 1, 2, 3]
print(fibonacci(10)) # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

####################################

def common_elements(list1, list2):
    return list(set(list1) & set(list2))

# Test the function
print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))  # [3, 4]
print(common_elements(['a', 'b', 'c'], ['c', 'd', 'e']))  # ['c']

####################################

def sum_list(numbers):
    return sum(numbers)

# Test the function
print(sum_list([1, 2, 3, 4]))  # 10
print(sum_list([10, 20, 30]))  # 60

####################################

import random

def age_prediction_game():
    money = int(input("Enter the amount of money you want to start with: "))
    while money > 0:
        random_int = random.randint(1, 10)
        attempts = 3
        while attempts > 0:
            guess = int(input("Guess the number (1-10): "))
            if guess == random_int:
                print("You hit the jackpot 🎰, you get to win 100 dollars!")
                money += 100
                break
            elif guess > random_int:
                print("The number you have selected is higher than the actual number")
            else:
                print("The number you have selected is lower than the actual number")
            attempts -= 1
            if attempts == 0:
                print("You missed 3 chances, charging you 25 dollars.")
                money -= 25
        money -= 50
        print(f"You have {money} dollars left.")
        if money <= 0:
            print("Sorry, you are out of money.")
            choice = input("Do you want to add more money or quit? Type 'add' to add more money or type 'quit' to quit: ")
            if choice == 'add':
                money = int(input("Enter the amount of money you want to add: "))
            else:
                print("Thank you for playing! Goodbye!")
                break

# Run the game
age_prediction_game()
"""
######################
Concepts Covered:
Function Definition: Using def to define a function.
Conditionals: Using if statements to check conditions.
Loops: Using for loops to iterate over a range of numbers.
Mathematical Operations: Using the modulo operator % to find remainders.
Returning Values: Using return to exit a function and provide a result.

#######################

now provide teach me how create variables and outputs and functions using this example, by giving me excercises that I will do in order to get it right. Provide me as many examples until i get it right, for each question i'll provide you with the answer and you will determine if it's right or wrong and provide me with the answer and explanation if it wrong before we move on to the next question.


"""