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
    electricity=finance_data[month]["electricity_percent"]




# Run the function
manage_finances()