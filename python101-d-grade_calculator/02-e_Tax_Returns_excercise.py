"""
Problem Statement - 30 marks
You are required to write a Python script that calculates the federal and provincial tax for an individual in Canada based on their annual income. The script should:
1.	Prompt the user to input their annual income.
2.	Calculate the federal tax based on the provided federal tax brackets and rates.
3.	Calculate the provincial tax based on the provided provincial tax brackets and rates for a given province (e.g., Ontario).
4.	Sum the federal and provincial taxes to provide the total tax owed.
5.	Output the federal tax, provincial tax, and total tax.
Federal Tax Brackets and Rates (2023)
	•	15% on the first $53,359 of taxable income
	•	20.5% on the next $53,359 of taxable income (from $53,359 to $106,717)
	•	26% on the next $58,197 of taxable income (from $106,717 to $164,914)
	•	29% on the next $69,695 of taxable income (from $164,914 to $234,609)
	•	33% of taxable income over $234,609
Provincial Tax Brackets and Rates for Ontario (2023)
	•	5.05% on the first $47,630 of taxable income
	•	9.15% on the next $47,629 of taxable income (from $47,630 to $95,259)
	•	11.16% on the next $12,579 of taxable income (from $95,259 to $107,838)
	•	12.16% on the next $21,523 of taxable income (from $107,838 to $129,361)
	•	13.16% of taxable income over $129,361
Provincial Tax Brackets and Rates for Quebec (2023)
	•	15% on the first $49,275 of taxable income
	•	20% on the next $49,275 of taxable income (from $49,275 to $98,540)
	•	24% on the next $19,310 of taxable income (from $98,540 to $117,850)
	•	25.75% of taxable income over $117,850
Provincial Tax Brackets and Rates for Alberta (2023)
	•	10% on the first $142,292 of taxable income
	•	12% on the next $26,145 of taxable income (from $142,292 to $168,437)
	•	13% on the next $52,291 of taxable income (from $168,437 to $220,728)
	•	14% on the next $104,573 of taxable income (from $220,728 to $325,301)
	•	15% of taxable income over $325,301
1.	calculate_federal_tax: This function calculates the federal tax based on the provided brackets and rates.
2.	calculate_provincial_tax: This function calculates the provincial tax for Ontario based on the provided brackets and rates
"""

# Global variables for federal tax brackets
FEDERAL_BRACKET_1 = 5359
FEDERAL_BRACKET_2 = 106717
FEDERAL_BRACKET_3 = 164914
FEDERAL_BRACKET_4 = 234609
FEDERAL_RATE_1 = 0.15
FEDERAL_RATE_2 = 0.205
FEDERAL_RATE_3 = 0.26
FEDERAL_RATE_4 = 0.29
FEDERAL_RATE_5 = 0.33

# Global variables for Ontario tax brackets
ONTARIO_BRACKET_1 = 47630
ONTARIO_BRACKET_2 = 95259
ONTARIO_BRACKET_3 = 107838
ONTARIO_BRACKET_4 = 129361
ONTARIO_RATE_1 = 0.0505
ONTARIO_RATE_2 = 0.0915
ONTARIO_RATE_3 = 0.1116
ONTARIO_RATE_4 = 0.1216
ONTARIO_RATE_5 = 0.1325

# Global variables for Quebec tax brackets
QUEBEC_BRACKET_1 = 49275
QUEBEC_BRACKET_2 = 98450
QUEBEC_BRACKET_3 = 117850
QUEBEC_BRACKET_4 = 325301
QUEBEC_RATE_1 = 0.015
QUEBEC_RATE_2 = 0.02
QUEBEC_RATE_3 = 0.024
QUEBEC_RATE_4 = 0.0325
QUEBEC_RATE_5 = 0.0355

# Global variables for Alberta tax brackets
ALBERTA_BRACKET_1 = 142292
ALBERTA_BRACKET_2 = 168437
ALBERTA_BRACKET_3 = 220728
ALBERTA_RATE_1 = 0.10
ALBERTA_RATE_2 = 0.12
ALBERTA_RATE_3 = 0.13
ALBERTA_RATE_4 = 0.14




def income_tax_brackets(income):
    if income <= FEDERAL_BRACKET_1:
        return income * FEDERAL_RATE_1
    elif income <= FEDERAL_BRACKET_2:
        return FEDERAL_BRACKET_1 * FEDERAL_RATE_1 + (income - FEDERAL_BRACKET_1) * FEDERAL_RATE_2
    elif income <= FEDERAL_BRACKET_3:
        return FEDERAL_BRACKET_1 * FEDERAL_RATE_1 + (FEDERAL_BRACKET_2 - FEDERAL_BRACKET_1) * FEDERAL_RATE_2 + (income - FEDERAL_BRACKET_2) * FEDERAL_RATE_3
    elif income <= FEDERAL_BRACKET_4:
        return FEDERAL_BRACKET_1 * FEDERAL_RATE_1 + (FEDERAL_BRACKET_2 - FEDERAL_BRACKET_1) * FEDERAL_RATE_2 + (FEDERAL_BRACKET_3 - FEDERAL_BRACKET_2) * FEDERAL_RATE_3 + (income - FEDERAL_BRACKET_3) * FEDERAL_RATE_4
    else:
        return FEDERAL_BRACKET_1 * FEDERAL_RATE_1 + (FEDERAL_BRACKET_2 - FEDERAL_BRACKET_1) * FEDERAL_RATE_2 + (FEDERAL_BRACKET_3 - FEDERAL_BRACKET_2) * FEDERAL_RATE_3 + (FEDERAL_BRACKET_4 - FEDERAL_BRACKET_3) * FEDERAL_RATE_4 + (income - FEDERAL_BRACKET_4) * FEDERAL_RATE_5

def provincial_tax_brackets(income, province):
    if province == "Ontario":
        if income <= ONTARIO_BRACKET_1:
            return income * ONTARIO_RATE_1
        elif income <= ONTARIO_BRACKET_2:
            return ONTARIO_BRACKET_1 * ONTARIO_RATE_1 + (income - ONTARIO_BRACKET_1) * ONTARIO_RATE_2
        elif income <= ONTARIO_BRACKET_3:
            return ONTARIO_BRACKET_1 * ONTARIO_RATE_1 + (ONTARIO_BRACKET_2 - ONTARIO_BRACKET_1) * ONTARIO_RATE_2 + (income - ONTARIO_BRACKET_2) * ONTARIO_RATE_3
        elif income <= ONTARIO_BRACKET_4:
            return ONTARIO_BRACKET_1 * ONTARIO_RATE_1 + (ONTARIO_BRACKET_2 - ONTARIO_BRACKET_1) * ONTARIO_RATE_2 + (ONTARIO_BRACKET_3 - ONTARIO_BRACKET_2) * ONTARIO_RATE_3 + (income - ONTARIO_BRACKET_3) * ONTARIO_RATE_4
        else:
            return ONTARIO_BRACKET_1 * ONTARIO_RATE_1 + (ONTARIO_BRACKET_2 - ONTARIO_BRACKET_1) * ONTARIO_RATE_2 + (ONTARIO_BRACKET_3 - ONTARIO_BRACKET_2) * ONTARIO_RATE_3 + (ONTARIO_BRACKET_4 - ONTARIO_BRACKET_3) * ONTARIO_RATE_4 + (income - ONTARIO_BRACKET_4) * ONTARIO_RATE_5
    elif province == "Quebec":
        if income <= QUEBEC_BRACKET_1:
            return income * QUEBEC_BRACKET_1
        elif income <= QUEBEC_BRACKET_2:
            return QUEBEC_BRACKET_1 * QUEBEC_RATE_1 + (income - QUEBEC_BRACKET_1) * QUEBEC_RATE_2
        elif income <= QUEBEC_BRACKET_3:
            return QUEBEC_BRACKET_1 * QUEBEC_RATE_1 + (QUEBEC_BRACKET_2 - QUEBEC_BRACKET_1) * QUEBEC_RATE_2 + (income - QUEBEC_BRACKET_2) * QUEBEC_RATE_3
        elif income <= QUEBEC_BRACKET_4:
            return QUEBEC_BRACKET_1 * QUEBEC_RATE_1 + (QUEBEC_BRACKET_2 - QUEBEC_BRACKET_1) * QUEBEC_RATE_2 + (QUEBEC_BRACKET_3 - QUEBEC_BRACKET_2) * QUEBEC_RATE_3 + (income - QUEBEC_BRACKET_3) * QUEBEC_RATE_4
        else:
            return QUEBEC_BRACKET_1 * QUEBEC_RATE_1 + (QUEBEC_BRACKET_2 - QUEBEC_BRACKET_1) * QUEBEC_RATE_2 + (QUEBEC_BRACKET_3 - QUEBEC_BRACKET_2) * QUEBEC_RATE_3 + (QUEBEC_BRACKET_4 - QUEBEC_BRACKET_3) * QUEBEC_RATE_4 + (income - QUEBEC_BRACKET_4) * QUEBEC_RATE_5
    elif province == "Alberta":
        if income <= ALBERTA_BRACKET_1:
            return income * ALBERTA_RATE_1
        elif income <= ALBERTA_BRACKET_2:
            return ALBERTA_BRACKET_1 * ALBERTA_RATE_1 + (income - ALBERTA_BRACKET_1) * ALBERTA_RATE_2
        elif income <= ALBERTA_BRACKET_3:
            return ALBERTA_BRACKET_1 * ALBERTA_RATE_1 + (ALBERTA_BRACKET_2 - ALBERTA_BRACKET_1) * ALBERTA_RATE_2 + (income - ALBERTA_BRACKET_2) * ALBERTA_RATE_3
        else:
            return ALBERTA_BRACKET_1 * ALBERTA_RATE_1 + (ALBERTA_BRACKET_2 - ALBERTA_BRACKET_1) * ALBERTA_RATE_2 + (ALBERTA_BRACKET_3 - ALBERTA_BRACKET_2) * ALBERTA_RATE_3 + (income - ALBERTA_BRACKET_3) * ALBERTA_RATE_4
    else:
        return None  # Return None for unsupported provinces

def main():
    print("Welcome to the Tax Calculator!")

    # Get user input
    while True:
        try:
            income = float(input("Enter your annual income: $"))
            if income < 0:
                print("Income cannot be negative. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Calculate federal tax
    federal_tax = income_tax_brackets(income)
    print(f"Your estimated federal income tax is ${federal_tax:.2f}")

    print("\nNow let's calculate your provincial tax.")

    # Province selection
    while True:
        print("\nProvince Selection:")
        print("1. Ontario")
        print("2. Quebec")
        print("3. Alberta")
        print("4. Exit")

        choice = input("Enter the number of your province or exit: ")

        if choice == '4':
            print("Thank you for using the Tax Calculator!")
            break

        province_map = {'1': 'Ontario', '2': 'Quebec', '3': 'Alberta'}
        if choice in province_map:
            province = province_map[choice]
            provincial_tax = provincial_tax_brackets(income, province)
            if provincial_tax is not None:
                print(f"Your estimated provincial income tax for {province} is ${provincial_tax:.2f}")
                total_tax = federal_tax + provincial_tax
                print(f"\nYour estimated federal income tax is ${federal_tax:.2f}")
                print(f"\nYour total estimated income tax is ${total_tax:.2f}")
            else:
                print(f"Tax calculation for {province} is not supported.")
        else:
            print("Invalid selection. Please choose 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()

"""
I understand you're looking for a clearer way to express these requirements. Here's a more structured and comprehensive rewrite:

1. Declare Global Constants for Tax Brackets and Rates:
   - Define all tax bracket limits and tax rates as global constants.
   - Place these declarations at the top of your Python file, outside of any function.
   - Use all-uppercase names for these constants to follow Python naming conventions for constants.

2. Example of Global Constant Declarations:
   ```python
   # Federal Tax Brackets
   FEDERAL_FIRST_BRACKET_LIMIT = 49275
   FEDERAL_SECOND_BRACKET_LIMIT = 98540
   FEDERAL_THIRD_BRACKET_LIMIT = 151978
   FEDERAL_FOURTH_BRACKET_LIMIT = 216511

   # Federal Tax Rates
   FEDERAL_FIRST_RATE = 0.15
   FEDERAL_SECOND_RATE = 0.205
   FEDERAL_THIRD_RATE = 0.26
   FEDERAL_FOURTH_RATE = 0.29
   FEDERAL_FIFTH_RATE = 0.33

   # Similar constants for provincial tax brackets and rates
   ```

3. Usage in Functions:
   - Use these global constants in your tax calculation functions.
   - You don't need to pass these constants as parameters to your functions.

4. Example Function Using Global Constants:
   ```python
   def calculate_federal_tax(income):
       if income <= FEDERAL_FIRST_BRACKET_LIMIT:
           return income * FEDERAL_FIRST_RATE
       elif income <= FEDERAL_SECOND_BRACKET_LIMIT:
           return FEDERAL_FIRST_BRACKET_LIMIT * FEDERAL_FIRST_RATE + \
                  (income - FEDERAL_FIRST_BRACKET_LIMIT) * FEDERAL_SECOND_RATE
       # Continue for other brackets...
   ```

5. Benefits of This Approach:
   - Improves code readability and maintainability.
   - Makes it easier to update tax brackets and rates in the future.
   - Reduces the likelihood of errors from hardcoded values within functions.

6. Note on Global Variables:
   - While these are technically global variables, they are constants and won't be modified during program execution.
   - This use of global constants is generally considered good practice for configuration values like tax rates and brackets.

By structuring your code this way, you'll have a clear separation between your configuration data (tax brackets and rates) and your logic (tax calculation functions), making your code more organized and easier to maintain.

"""

