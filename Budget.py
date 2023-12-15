# Initialize variables
count = 0
total_income = 0
total_expenses = 0

# Input multiple incomes
num_incomes = int(input("Enter the number of sources of income: "))
for i in range(num_incomes):
    income = float(input(f"Enter income {i+1}: $"))
    total_income += income

# Fixed Costs
count = 0
while count < 1:
    count += 1
    # Input account balances
    checking_balance = float(input('Enter Checking Account Balance: $'))
    savings_balance = float(input('Enter Savings Account Balance: $'))

    # Variable Costs
    water_bill = float(input('Enter Water Bill: $'))
    power_bill = float(input('Enter Power Bill: $'))
    entertainment = float(input('Enter Entertainment Amount: $'))
    groceries = float(input('Enter Groceries: $'))
    phone_bill = float(input('Enter Phone Bill: $'))
    mortgage = float(input('Enter Mortgage: $'))
    car_insurance = float(input('Enter Car Insurance: $'))

    # Calculate remaining cash after expenses
    total_expenses = (
        water_bill + power_bill + entertainment +
        groceries + phone_bill + mortgage + car_insurance
    )
    remaining_cash = checking_balance + total_income - total_expenses

    #Calculate percentages
    water_bill_percentage = ( water_bill/total_expenses) * 100
    power_bill_percentage = (power_bill/total_expenses) *100
    entertainment_percentage = (entertainment/total_expenses) * 100
    groceries_percentage = (groceries/total_expenses)*100
    phone_bill_percentage = (phone_bill/total_expenses) * 100
    mortgage_percentage = (phone_bill / total_expenses) * 100
    car_insurance_percentage = (car_insurance / total_expenses) * 100

    #Prints Percentages
    print('Water Bill Percent',round(water_bill_percentage), '%')
    print('Power Bill Percent', round(power_bill_percentage), '%')
    print('Entertainment Percent', round(entertainment_percentage), '%')
    print('Groceries Percent', round(groceries_percentage), '%')
    print('Phone Bill Percent', round(phone_bill_percentage), '%')
    print('Mortgage Percent',round(mortgage_percentage),'%')
    print('Car Insurance Percent', round(car_insurance_percentage), '%')

    # Check if within budget
    if remaining_cash > 0:
        print(f'You stayed within your budget. Remaining cash: ${remaining_cash:,.2f}')
    elif remaining_cash < 0:
        print(f'You went over your budget. Remaining balance: ${remaining_cash:,.2f}')
    else:
        print('You used your entire budget. Consider adjusting your spending.')
