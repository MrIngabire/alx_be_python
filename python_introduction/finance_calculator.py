monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

#calculate monthly saving

monthly_savings = monthly_income - monthly_expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#printing results

print (f"Your monthly savings are ${Monthly Savings}.")
print (f"Projected savings after one year, with interest, is: ${Projected Savings}.")