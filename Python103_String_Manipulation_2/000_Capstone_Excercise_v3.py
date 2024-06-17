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


def task1():
    user_input = input("Enter a string: ")
    return user_input.replace(" ", "+")

def task2():
    user_input = int(input("Enter a number: "))
    if 250 < user_input < 500:
        return True
    else:
        return False

def atm_booth():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    date_of_birth = input("Enter your date of birth: ")

    while True:
        print(f"Welcome {first_name}, what would you like to do today?")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Take out the card")
        choice = input("Enter your choice: ")

        if choice == "1":
            deposit_amount = float(input("How much money would you like to deposit? "))
            print(f"Deposit successful. Your new balance is {deposit_amount}.")
        elif choice == "2":
            balance = float(input("Enter your current balance: "))
            withdraw_amount = float(input("How much money you would like to withdraw? "))
            if withdraw_amount > balance:
                print("Insufficient balance. You cannot withdraw more than you have.")
            elif withdraw_amount > 500:
                print("You cannot withdraw more than 500.")
            else:
                print(f"Withdrawal successful. Your new balance is {balance - withdraw_amount}.")
        elif choice == "3":
            print(f"Thank you so much, have a wonderful day {first_name}.")
            break
        else:
            print("Invalid choice. Please try again.")

atm_booth()