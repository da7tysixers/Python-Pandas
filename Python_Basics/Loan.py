# Get loan information from the user.
money_owed = float(input("How much money do you owe? \n")) # 50,000
annual_interest_rate = float(input("What is the annual interest rate (as a percentage)? \n")) # 3%
payment = float(input("How much can you pay each month?\n ")) # 1000
months = int(input("How many months do you want to pay off the loan? \n")) # 24


month_rate = annual_interest_rate / 100 / 12

for month in range(months):
    #calculate the total amount paid and the total interest paid
    interest_paid = money_owed * month_rate


    # Add interest to the money owed
    money_owed += interest_paid

    if (money_owed - payment) < 0:
        print("You have paid off the loan!")
        print('You paid off the loan in', month + 1, 'months!')
        break

    #Make Payment
    money_owed -= payment


    print('Paid', payment, 'of which', interest_paid, 'was interst', end=' ')
    print('Now I owe', money_owed)

# You can use the end= ' ' within the print statement to have something printed on the same line as the previous print statement. For example:
print("This is the first part of the sentence", end=' ')
print("and this is the second part of the sentence.")