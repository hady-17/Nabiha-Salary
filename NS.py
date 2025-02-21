import random
def manage_finances():
    #create Finance_data dictionary in order to save all  the data
    finance_data = {}
    #creating month var and taking input from the user
    month = input("Enter the month: ")
    #inserting data for the selected month Salary ,Saving,Rent,electricity
    finance_data[month] = {
        "salary": float(input("Enter your salary for the month: ")),
        "savings_percent": float(input("Enter the percentage for savings: ")),
        "rent_percent": float(input("Enter the percentage for rent: ")),
        "electricity_percent": float(input("Enter the percentage for electricity: "))
    }
    
    salary=finance_data[month]["salary"]
    savingPercent=finance_data[month]["savings_percent"]
    rentPercent=finance_data[month]["rent_percent"]
    electricityPercent=finance_data[month]["electricity_percent"]
    #calculate allocation(from percent supplied)
    savings=(savingPercent/100)*salary

    rent=(rentPercent/100)*salary

    electricity=(electricityPercent/100)*salary

    totalExpenses=savings+rent+electricity

    remaining=salary-totalExpenses

    yearlyRent=rent*12

    yearlyElectricity=electricity*12

    #salary squared
    salaryRaise=salary*salary

    #using random to generate random saving amount
    totalExpPerc=savingPercent+rentPercent+electricityPercent
    #random expect the range to be int
    additionalSaving=random.randint(int(totalExpenses),int(salary))
    if(savings!=0):
        leftoverFromExtraSavings = additionalSaving / savings
    else:
        leftoverFromExtraSavings=0

     # Output results
    print("\n--- Finance Report for", month, "---")
    print(f"Salary: ${salary:.2f}")
    print(f"Allocated to Savings: ${savings:.2f}")
    print(f"Allocated to Rent: ${rent:.2f}")
    print(f"Allocated to Electricity: ${electricity:.2f}")
    print(f"Total Expenses: ${totalExpenses:.2f}")
    print(f"Remaining Salary: ${remaining:.2f}")
    print(f"Yearly Rent Estimate: ${yearlyRent:.2f}")
    print(f"Yearly Electricity Estimate: ${yearlyElectricity:.2f}")
    print(f"Salary Squared (Just for Fun): ${salaryRaise:.2f}")
    print(f"With an extra ${additionalSaving}, the leftover from savings allocation would be: {leftoverFromExtraSavings:.2f}")

# Run the function
manage_finances()