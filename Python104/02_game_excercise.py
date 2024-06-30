"""
Exercise python
1. Write a number to check if that is a prime member of, for example 3, 5, 7, 23 etc

2. Write a function to calculate the Fibonacci sequence up to n numbers. 

3. Write a function to find the common elements between two lists.

4. Write a function to sum all the numbers in a list.

5. Design and create an age predication game, the computer will set a random number with the following code

import random

random_int = random.randint(1, 10)

Then you have to predict the number, it will output each time 
“The number you have selected is higher than the actual number” or 
“The number you have selected is lower than the actual number” 
if it is the same number, then print “you hit the jackpot 🎰, 
you get to win 100 dollar” then give the player the chance to play again, 
each time they lose take away 50 dollar, in the beginning each time the player 
try predicting if they miss 3 chances charge 25 dollar, initially there should 
be a condition to put money in, if they are out of money, please show 
“sorry you are out of money, do you want to add more or quit? Type “add” to 
add more money or type “quit” to quit
"""

# Prime Number Check:
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Example usage
print(is_prime(3))   # Output: True
print(is_prime(5))   # Output: True
print(is_prime(7))   # Output: True
print(is_prime(23))  # Output: True
print(is_prime(4))   # Output: False


# Fibonacci Sequence:

def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    return sequence[:n]

# Example usage
print(fibonacci(5))   # Output: [0, 1, 1, 2, 3]
print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# Common Elements Between Two Lists:
def common_elements(list1, list2):
    return list(set(list1) & set(list2))

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(common_elements(list1, list2))  # Output: [4, 5]


# Sum of Numbers in a List:

def sum_list(numbers):
    return sum(numbers)

# Example usage
numbers = [1, 2, 3, 4, 5]
print(sum_list(numbers))  # Output: 15


# Age Prediction Game:

import random

def play_game():
    money = 100
    play = True

    while play:
        print(f"You have ${money}")
        bet = int(input("Enter the amount you want to bet: "))
        if bet > money:
            print("You don't have enough money.")
            continue

        random_int = random.randint(1, 10)
        attempts = 0

        while attempts < 3:
            guess = int(input("Guess the number (1-10): "))
            if guess == random_int:
                print("You hit the jackpot! You win $100.")
                money += 100
                break
            elif guess < random_int:
                print("The number you have selected is lower than the actual number.")
            else:
                print("The number you have selected is higher than the actual number.")
            attempts += 1
            money -= 25

        if attempts == 3:
            print("You used all your attempts. You lose $50.")
            money -= 50

        if money <= 0:
            print("Sorry, you are out of money.")
            choice = input("Do you want to add more money or quit? Type 'add' to add more money or 'quit' to quit: ")
            if choice.lower() == 'add':
                add_money = int(input("Enter the amount you want to add: "))
                money += add_money
            else:
                play = False
        else:
            choice = input("Do you want to play again? (yes/no): ")
            if choice.lower() != 'yes':
                play = False

    print(f"Thanks for playing! You ended with ${money}")

# Start the game
play_game()


"""
In this age prediction game, the player starts with $100. 
They can place a bet and try to guess the randomly generated number between 1 and 10. 
If they guess correctly, they win $100. If they guess incorrectly, they lose $25 for each attempt. 
If they use all three attempts without guessing correctly, they lose an additional $50. 
If the player runs out of money, they have the option to add more money or quit the game. 
The game continues until the player chooses to quit or runs out of money.
"""
