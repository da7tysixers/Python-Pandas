#expenses = [10.50, 8, 5, 15, 20, 5, 3]

#total = sum(expenses)
#sum_total = 0
##for expense in expenses:
 #   sum_total += expense

#print(f"Total expenses: ${sum_total}")
#print('You spent $', sum_total, sep='')
#print('You spent $' + str(total) + ' on your expenses.')


##expensesList = input("Enter your expenses separated by commas: ")
##expenses = [float(expense) for expense in expensesList.split(',')]
##total = sum(expenses)
expensesBook = []
ans = 'Y'
while ans.upper() != 'N':
    expense = float(input("Enter an expense: "))
    expensesBook.append(expense)
    ans = input("Do you want to add another expense? (y/n): ").upper()

total = sum(expensesBook)
print(expensesBook)
print(f"Total expenses: ${total}")
