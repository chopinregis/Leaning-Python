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

def income_tax_brackets(income):
    if income <= 5359:
        return income * 0.15
    elif income <= 106717:
        return 5359 * 0.15 + (income - 5359) * 0.205
    elif income <= 164914:
        return 5359 * 0.15 + (106717 - 5359) * 0.205 + (income - 106717) * 0.26
    elif income <= 234609:
        return 5359 * 0.15 + (106717 - 5359) * 0.205 + (164914 - 106717) * 0.26 + (income - 164914) * 0.29
    else:
        return 5359 * 0.15 + (106717 - 5359) * 0.205 + (164914 - 106717) * 0.26 + (234609 - 164914) * 0.29 + (income - 234609) * 0.33


def main():
    # welcome message
    print("Welcome to the Tax Calculator!")

    # get user input
    income = float(input("Enter your annual income: "))

    # calculate federal tax
    federal_tax = income_tax_brackets(income)
    print(f"Your estimated federal income tax is ${federal_tax:.2f}")
    print("\n")
    print("Okay let us calculate your provincial tax.")


def provincial_tax_brackets(income, province):
    if province == "Ontario":
        if income <= 47630:
            return income * 0.0505
        elif income <= 95259:
            return 47630 * 0.0505 + (income - 47630) * 0.0915
        elif income <= 107838:
            return 47630 * 0.0505 + (95259 - 47630) * 0.0915 + (income - 95259) * 0.1116
        elif income <= 129361:
            return 47630 * 0.0505 + (95259 - 47630) * 0.0915 + (107838 - 95259) * 0.1116 + (income - 107838) * 0.1216
        else:
            return 47630 * 0.0505 + (95259 - 47630) * 0.0915 + (107838 - 95259) * 0.1116 + (129361 - 107838) * 0.1216 + (income - 129361) * 0.1325          
    print(f"Your estimated provincial income tax for Ontario is ${provincial_tax_brackets:.2f}")
        
    if province == "Quebec":
        if income <= 49275:
            return income * 0.015
        elif income <= 98450:
            return 49275 * 0.015 + (income - 49275) * 0.02
        elif income <= 117850:
            return 49275 * 0.015 + (98450 - 49275) * 0.02 + (income - 98450) * 0.024
        elif income <= 325301:
            return 49275 * 0.015 + (98450 - 49275) * 0.02 + (117850 - 98450) * 0.024 + (income - 117850) * 0.0325
    print(f"Your estimated provincial income tax for Quebec is ${provincial_tax_brackets:.2f}")
        
    if province == "Alberta":
        if income <= 142292:
            return income * 0.10
        elif income <= 168437:
            return 142292 * 0.10 + (income - 142292) * 0.12
        elif income <= 220728:
            return 142292 * 0.10 + (168437 - 142292) * 0.12 + (income - 168437) * 0.13
        else:
            return 142292 * 0.10 + (168437 - 142292) * 0.12 + (220728 - 168437) * 0.13 + (income - 220728) * 0.14
    print(f"Your estimated provincial income tax for Alberta is ${provincial_tax_brackets:.2f}")
        


def main():
    # welcome message
    print("Welcome to the Tax Calculator!")

    # get user input
    income = float(input("Enter your annual income: "))

    # calculate federal tax
    federal_tax = income_tax_brackets(income)
    print(f"Your estimated federal income tax is ${federal_tax:.2f}")
    print("\n")
    print("Okay let us calculate your provincial tax.")

    #province option
    province = input("Enter your province: ")
    provincial_tax_brackets(income, province)

    while True:
        print("\nProvince Selection:")
        print("1. Ontario")
        print("2. Quebec")
        print("3. Alberta")
        print("4. Exit")

        choice = input("Enter the number of your province or exit: ")

        if choice == '1':
            provincial_tax = income * province
            return provincial_tax
            print(f"Your estimated provincial income tax for Ontario is ${provincial_tax:.2f}")
            
    print(f"Your estimated provincial income tax for Ontario is ${provincial_tax_brackets(income, province):.2f}")



"""
    #province option
    while True:
        print("\nProvince Selection:")
        print("1. Ontario")
        print("2. Quebec")
        print("3. Alberta")
        print("4. Exit")

        choice = input("Enter the number of your province or exit: ") or input("Enter your choice: ")

        if choice == '1':
            provincial_tax = income * province
            return provincial_tax
            print(f"Your estimated provincial income tax for Ontario is ${provincial_tax:.2f}")

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

"""

if __name__ == "__main__":
    main()




 

