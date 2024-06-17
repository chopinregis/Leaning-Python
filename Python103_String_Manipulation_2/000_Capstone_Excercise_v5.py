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
    """Fills whitespaces in the input text with '+' signs.

    Args:
        text (str): The input text.

    Returns:
        str: The modified text with whitespaces replaced by '+' signs.
    """

    return text.replace(" ", "+")

def check_number_range(number):
    """Checks if the input number is within the range (250, 500).

    Args:
        number (int): The input number.

    Returns:
        bool: True if the number is within the range, False otherwise.
    """

    return 250 < number < 500

class ATM:
    def __init__(self, first_name, last_name, date_of_birth, balance=0):
        """Initializes the ATM object with user information and balance.

        Args:
            first_name (str): User's first name.
            last_name (str): User's last name.
            date_of_birth (str): User's date of birth (formatted string).
            balance (int, optional): Initial account balance. Defaults to 0.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.balance = balance

    def greet(self):
        """Greets the user with a personalized welcome message."""

        print(f"Welcome, {self.first_name}! What would you like to do today?")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Take out your card")

    def deposit(self, amount):
        """Deposits the specified amount into the user's account.

        Args:
            amount (int): The amount to deposit.
        """

        self.balance += amount
        print(f"Successfully deposited ${amount}. Your new balance is ${self.balance}.")

    def withdraw(self, amount):
        """Withdraws the specified amount from the user's account,
        checking for sufficient funds and withdrawal limit.

        Args:
            amount (int): The amount to withdraw.

        Returns:
            bool: True if withdrawal is successful, False otherwise.
        """

        if amount > self.balance:
            print("Insufficient funds. Your current balance is ${self.balance}.")
            return False
        elif amount > 500:
            print("Withdrawal limit exceeded. Maximum withdrawal is $500.")
            return False
        else:
            self.balance -= amount
            print(f"Successfully withdrew ${amount}. Your new balance is ${self.balance}.")
            return True

    def run(self):
        """Runs the ATM program, allowing the user to perform transactions."""

        while True:
            self.greet()
            choice = input("Enter your choice (1-3): ")

            if choice == '1':
                amount = int(input("How much money would you like to deposit? "))
                self.deposit(amount)
            elif choice == '2':
                amount = int(input("How much money would you like to withdraw? "))
                if self.withdraw(amount):
                    # Allow further transactions after successful withdrawal
                    continue
            elif choice == '3':
                print(f"Thank you so much, have a wonderful day {self.first_name}!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")
    atm = ATM(first_name, last_name, date_of_birth)
    atm.run()