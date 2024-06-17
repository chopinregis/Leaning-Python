# Task 1: Create a function that takes an input from the user and fills up the whitespaces with + sign
# Task 2: Create a function that takes a number as an input from the user and checks if
# it is lower than 500 but higher than 250
# Task 3: Create a ATM booth, where you can deposit any amount of money,
# first step is to input your first name and lastname and date of birth
# ----After this step, put a prompt on what the user wants to do, for example say "Welcome Firstname, what would you like to do today? 1. deposit 2. withdraw 3. take out the card"
# second step, it should prompt you to provide if option 1-->"How much money would you like to deposit?"
# third step, after deposit, you can have withdraw option as well, if option 2 --->"How much money you would like to withdraw?"
# you need to also put a limit to withdrawal, you cannot withdraw more than you have in atm or the limit of 500, maximum you can withdraw is 500
# if the user chooses number 3, print "Thank you so much, have a wonderful day Firstname"


def fill_whitespaces(text):
    """Fills whitespaces in a string with '+' signs.

    Args:
        text (str): The input string.

    Returns:
        str: The modified string with '+' replacing whitespaces.
    """

    return text.replace(" ", "+")

def is_between(number, lower_bound, upper_bound):
    """Checks if a number is within a specified range (exclusive).

    Args:
        number (int): The number to check.
        lower_bound (int): The lower bound (excluded).
        upper_bound (int): The upper bound (excluded).

    Returns:
        bool: True if the number is within the range, False otherwise.
    """

    return lower_bound < number < upper_bound

def atm_booth():
    """Simulates an ATM booth with deposit, withdrawal, and card exit options."""

    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    date_of_birth = input("Enter your date of birth: ")

    balance = 0  # Initial balance

    print(f"\nWelcome, {first_name}! What would you like to do today?")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Take out your card")

    while True:
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            deposit_amount = int(input("How much money would you like to deposit? "))
            balance += deposit_amount
            print(f"Deposited ${deposit_amount}. Your new balance is ${balance}")
        elif choice == '2':
            withdrawal_amount = int(input("How much money would you like to withdraw? "))
            if withdrawal_amount <= balance and withdrawal_amount <= 500:
                balance -= withdrawal_amount
                print(f"Withdrawn ${withdrawal_amount}. Your remaining balance is ${balance}")
            else:
                print("Insufficient funds or withdrawal limit exceeded.")
        elif choice == '3':
            print(f"Thank you so much, have a wonderful day {first_name}!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Example usage
text = "This has   spaces"
modified_text = fill_whitespaces(text)
print(modified_text)  # Output: This+has+++spaces

number = 300
is_in_range = is_between(number, 250, 500)
print(is_in_range)  # Output: True

atm_booth()
