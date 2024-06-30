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
class BankAccount:
    next_id = 0

    def __init__(self, first_name, last_name, dob, account_type):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.account_type = account_type
        self.balance = 0
        self.withdraw_limit = 1000  # Initial withdraw limit is 1000 CAD
        self.user_id = f"BCB{str(BankAccount.next_id).zfill(5)}"
        BankAccount.next_id += 1
        print(f"Congratulations, {self.first_name}! Welcome to Beautiful Canada Bank.")
        print(f"Your user ID is {self.user_id}.")
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} CAD. New balance is {self.balance} CAD.")
        else:
            print("Invalid amount. Please enter a positive integer.")

    def withdraw(self, amount):
        if amount <= self.balance and amount <= self.withdraw_limit:
            self.balance -= amount
            print(f"Withdrew {amount} CAD. Remaining balance is {self.balance} CAD.")
        else:
            print(f"Cannot withdraw. Either balance or limit exceeded. Current balance: {self.balance} CAD, Withdraw limit: {self.withdraw_limit} CAD.")

    def increase_withdraw_limit(self, new_limit):
        if 1000 < new_limit <= 5000:
            self.withdraw_limit = new_limit
            print(f"Withdraw limit increased to {self.withdraw_limit} CAD.")
        else:
            print("Invalid limit. Please choose a limit between 1000 to 5000 CAD.")
    
    def remove_atm_card(self):
        # Simulate removing an ATM card
        print("ATM card has been removed.")

def main():
    print("Welcome to Beautiful Canada Bank")
    account_type = input("Choose account type (1: Checking, 2: Saving): ")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    dob = input("Enter your date of birth (YYYY-MM-DD): ")
    account = BankAccount(first_name, last_name, dob, account_type)

    while True:
        action = input("Choose action (1: Deposit, 2: Withdraw, 3: Remove ATM card, 4: Increase withdraw limit, 5: Exit): ")
        if action == "1":
            amount = int(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif action == "2":
            amount = int(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif action == "3":
            account.remove_atm_card()
        elif action == "4":
            new_limit = int(input("Enter new withdraw limit (up to 5000 CAD): "))
            account.increase_withdraw_limit(new_limit)
        elif action == "5":
            print("Thank you for using Beautiful Canada Bank. Goodbye!")
            break
        else:
            print("Invalid action. Please choose again.")

if __name__ == "__main__":
    main()
