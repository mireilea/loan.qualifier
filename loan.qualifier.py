def loan_qualifier():

    """
    Function to ask users for monthly salary and years of employment
    automatically calculates annual income and either approves or decline them a loan.

    """

    salary = int(input("enter your monthly salary:"))
    years_employed = int(input("enter the number of years employed:"))
    annual_income = salary * 12

    if (annual_income >= 50000) and (years_employed >= 3):
        print("you qualify for a loan")

    elif annual_income <= 50000:
        print("your income must be 50000 or more, you don't qualify for a loan")

    elif years_employed <= 3:
        print("you must be employed for 3 years or more, you don't qualify for a loan")

    else:
        print()