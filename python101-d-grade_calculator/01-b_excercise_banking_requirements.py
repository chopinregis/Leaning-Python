"""
Bank Management System Python Code: Additional Brownie point, deploy it in Cloud Functions
Create a Bank Management system for 'Beautiful Canada Bank' Where
1. Each time a new client joins, they are given an option to choose '1. Create a checking account 2. Create a saving account
2. Then they are asked for their first name, last name and date of birth
3. Provide a 'Congratulations' Welcome email for joining the Beautiful Canada Bank
4. Each time a user creates an account, save this information, generate an user id, for example BCB00000, BCB00001, BCB00002
5. Please then provide an option to 1. Deposit 2. Withdraw 3. Remove the ATM Card
6. Deposit only integer amount no minimum or maximum deposity
7. Withdraw no minimum and Maximum 1000 CAD, please provide an option 'Do you want to increase the Withdraw limit? Maximum limit would be 5000 CAD
"""
import random
import string

class Account:
  def __init__(self, first_name, last_name, dob, account_type):
    self.first_name = first_name
    self.last_name = last_name
    self.dob = dob
    self.account_type = account_type
    self.balance = 0
    self.user_id = self.generate_user_id()
    self.atm_card = True

  def generate_user_id(self):
    # Generate a random alphanumeric user ID (BCB + 5 digits)
    return "BCB" + ''.join(random.choices(string.digits, k=5))

  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
      print(f"Successfully deposited ${amount}. Your new balance is ${self.balance}")
    else:
      print("Deposit amount must be a positive integer.")

  def withdraw(self, amount):
    if 0 < amount <= 1000:
      if self.balance >= amount:
        self.balance -= amount
        print(f"Successfully withdrew ${amount}. Your new balance is ${self.balance}")
      else:
        print("Insufficient funds.")
    elif amount > 1000:
      # Offer to increase withdrawal limit
      increase_limit = input("Withdrawal limit exceeded. Do you want to increase the limit to $5000? (y/n): ").lower()
      if increase_limit == 'y':
        self.withdraw(amount)  # Recursive call with potentially higher limit
      else:
        print("Withdrawal declined.")
    else:
      print("Withdrawal amount must be a positive integer.")

  def remove_atm_card(self):
    self.atm_card = False
    print("ATM card removed successfully.")

def main():
  # Welcome message
  print("Welcome to Beautiful Canada Bank!")

  # Create a new account
  account_type = input("Select account type (1. Checking, 2. Savings): ")
  if account_type == '1':
    account_type = "Checking"
  elif account_type == '2':
    account_type = "Savings"
  else:
    print("Invalid selection. Please choose 1 or 2.")
    return

  first_name = input("Enter your first name: ")
  last_name = input("Enter your last name: ")
  dob = input("Enter your date of birth (YYYY-MM-DD): ")

  # Create account object and display user ID
  new_account = Account(first_name, last_name, dob, account_type)
  print(f"Congratulations {new_account.first_name}! Your account has been created. Your user ID is: {new_account.user_id}")

  # User options
  while True:
    print("\nMenu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Remove ATM Card")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
      amount = int(input("Enter deposit amount: "))
      new_account.deposit(amount)
    elif choice == '2':
      amount = int(input("Enter withdrawal amount: "))
      new_account.withdraw(amount)
    elif choice == '3':
      new_account.remove_atm_card()
    elif choice == '4':
      print("Thank you for banking with Beautiful Canada Bank!")
      break
    else:
      print("Invalid selection. Please choose 1, 2, 3, or 4.")

if __name__ == "__main__":
  main()
