monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

#finding out the monthly savings
monthly_savings = monthly_income - monthly_expenses
print(f"Your monthly savings are ${int(monthly_savings)}.")

#finding out the annual savings with interest
annual_months = 12
annual_interest_rate = 0.05

projected_savings = monthly_savings * annual_months + (monthly_savings * annual_months * annual_interest_rate)
print(f"Projected savings after one year, with interest, is: ${int(projected_savings)}.")
