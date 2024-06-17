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


def replace_whitespaces():
    # Task 1: Replace all whitespaces in the input string with a '+'
    user_input = input("Enter a string: ")
    modified_input = user_input.replace(' ', '+')
    print("Modified String:", modified_input)

def check_number():
    # Task 2: Check if the number is between 250 and 500
    number = int(input("Enter a number: "))
    if 250 < number < 500:
        print("The number is between 250 and 500.")
    else:
        print("The number is not in the range between 250 and 500.")

class ATM:
    def __init__(self):
        self.balance = 0
        self.user_firstname = ""
    
    def setup_account(self):
        # Collect user details
        self.user_firstname = input("Enter your first name: ")
        lastname = input("Enter your last name: ")
        dob = input("Enter your date of birth (YYYY-MM-DD): ")
        print(f"Welcome {self.user_firstname}, your account is set up.")
    
    def atm_menu(self):
        # Display ATM options
        response = input(f"Welcome {self.user_firstname}, what would you like to do today? 1. Deposit 2. Withdraw 3. Take out the card: ")
        if response == "1":
            self.deposit()
        elif response == "2":
            self.withdraw()
        elif response == "3":
            self.exit_atm()
        else:
            print("Invalid option selected.")
    
    def deposit(self):
        # Handle deposit action
        amount = float(input("How much money would you like to deposit? "))
        self.balance += amount
        print(f"Your new balance is ${self.balance:.2f}")
    
    def withdraw(self):
        # Handle withdrawal action
        amount = float(input("How much money would you like to withdraw? "))
        if amount > self.balance or amount > 500:
            print("You cannot withdraw more than the balance or more than $500.")
        else:
            self.balance -= amount
            print(f"${amount:.2f} has been withdrawn. Your new balance is ${self.balance:.2f}")
    
    def exit_atm(self):
        # Exit the ATM
        print(f"Thank you so much, have a wonderful day {self.user_firstname}")

# Example usage
if __name__ == "__main__":
    replace_whitespaces()
    check_number()
    atm = ATM()
    atm.setup_account()
    atm.atm_menu()
