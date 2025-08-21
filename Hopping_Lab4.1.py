#Rachel Hopping
#Complete
#Ask the user to input their budget then their individual monthly expenses
#Add a running total then calculate the difference between the budget and expense total
#Display the amount the user is over or under budget

budget = float(input('Enter your monthly budget amount: $'))
total = 0

while (expense := float(input('Enter an expense amount (Enter 0 to quit): $'))) > 0:
    total += expense

net_budget = budget - total

print(f'Monthly budget: ${budget:.2f}')
print(f'Monthly expenses: ${total:.2f}')

#To display the over budget variable as a positive, add a minus sign 
if net_budget < 0:
    print(f'You are ${-net_budget:.2f} over budget this month.')
else:
    print(f'You are ${net_budget:.2f} under budget this month and can spend more money.')
          
