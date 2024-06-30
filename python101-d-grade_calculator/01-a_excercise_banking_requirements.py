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
import datetime

class BankAccount:
    def __init__(self, account_type, first_name, last_name, dob):
        self.account_type = account_type
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.user_id = self.generate_user_id()
        self.balance = 0
        self.withdraw_limit = 1000

    def generate_user_id(self):
        return f"BCB{random.randint(0, 99999):05d}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.withdraw_limit:
            if self.balance >= amount:
                self.balance -= amount
                return f"Withdrawn ${amount}. New balance: ${self.balance}"
            return "Insufficient funds."
        return f"Invalid withdrawal amount. Limit is ${self.withdraw_limit}"

    def increase_withdraw_limit(self):
        self.withdraw_limit = 5000
        return "Withdrawal limit increased to $5000 CAD."

def create_account():
    account_type = input("Choose account type (1 for Checking, 2 for Savings): ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    dob = input("Enter date of birth (YYYY-MM-DD): ")
    
    account = BankAccount(account_type, first_name, last_name, dob)
    print(f"Congratulations! Welcome to Beautiful Canada Bank, {first_name}!")
    print(f"Your user ID is: {account.user_id}")
    return account

def main():
    accounts = []
    
    while True:
        print("\n1. Create a new account")
        print("2. Access existing account")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            new_account = create_account()
            accounts.append(new_account)
        elif choice == '2':
            user_id = input("Enter your user ID: ")
            account = next((acc for acc in accounts if acc.user_id == user_id), None)
            
            if account:
                while True:
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Increase withdrawal limit")
                    print("4. Remove ATM Card (Exit to main menu)")
                    action = input("Choose an action: ")
                    
                    if action == '1':
                        amount = int(input("Enter deposit amount: "))
                        print(account.deposit(amount))
                    elif action == '2':
                        amount = int(input("Enter withdrawal amount: "))
                        print(account.withdraw(amount))
                    elif action == '3':
                        print(account.increase_withdraw_limit())
                    elif action == '4':
                        print("ATM Card removed. Returning to main menu.")
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Account not found.")
        elif choice == '3':
            print("Thank you for using Beautiful Canada Bank. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()






import functions_framework
from flask import jsonify, request

# ... (include the BankAccount class and other functions from the previous code)

accounts = []  # This will reset on each function call in a serverless environment

@functions_framework.http
def bank_management(request):
    if request.method == 'POST':
        data = request.get_json()
        action = data.get('action')

        if action == 'create_account':
            account = BankAccount(
                data['account_type'],
                data['first_name'],
                data['last_name'],
                data['dob']
            )
            accounts.append(account)
            return jsonify({
                'message': f"Congratulations! Welcome to Beautiful Canada Bank, {account.first_name}!",
                'user_id': account.user_id
            })

        elif action in ['deposit', 'withdraw', 'increase_limit']:
            user_id = data.get('user_id')
            account = next((acc for acc in accounts if acc.user_id == user_id), None)
            
            if not account:
                return jsonify({'error': 'Account not found'}), 404

            if action == 'deposit':
                result = account.deposit(int(data['amount']))
            elif action == 'withdraw':
                result = account.withdraw(int(data['amount']))
            elif action == 'increase_limit':
                result = account.increase_withdraw_limit()

            return jsonify({'message': result})

    return jsonify({'error': 'Invalid request'}), 400