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
      text: The input string.

  Returns:
      The modified string with '+' replacing whitespaces.
  """
  return text.replace(" ", "+")

def is_between(number):
  """Checks if a number is between 250 (inclusive) and 500 (exclusive).

  Args:
      number: The number to check.

  Returns:
      True if the number is within the range, False otherwise.
  """
  return 250 <= number < 500

def atm_booth():
  """Simulates an ATM booth with deposit, withdrawal, and card exit options."""
  first_name = input("Enter your first name: ")
  last_name = input("Enter your last name: ")
  date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")

  # Simulate account balance (replace with actual database interaction if needed)
  balance = 1000  # Initial balance

  while True:
    print(f"\nWelcome, {first_name}! What would you like to do today?")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Take out your card")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
      deposit_amount = float(input("How much money would you like to deposit? "))
      balance += deposit_amount
      print(f"Deposited ${deposit_amount:.2f}. Your new balance is ${balance:.2f}.")

    elif choice == '2':
      withdraw_amount = float(input("How much money would you like to withdraw? "))
      if withdraw_amount > balance or withdraw_amount > 500:
        print("Insufficient funds or withdrawal limit exceeded. Maximum withdrawal is $500 or your current balance.")
      else:
        balance -= withdraw_amount
        print(f"Withdrew ${withdraw_amount:.2f}. Your new balance is ${balance:.2f}.")

    elif choice == '3':
      print(f"Thank you very much, {first_name}. Have a wonderful day!")
      break

    else:
      print("Invalid choice. Please enter a number between 1 and 3.")

# Example usage
text = "This has some spaces"
filled_text = fill_whitespaces(text)
print(f"Original text: {text}")
print(f"Text with '+' replacing spaces: {filled_text}")

number = 300
is_in_range = is_between(number)
print(f"Number {number} is between 250 and 500 (exclusive): {is_in_range}")

atm_booth()  # Run the ATM simulation
