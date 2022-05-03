import sys

'''Part A
=============================================================================
Calculate credit card balance after no payment made for a period of months.
=============================================================================
'''
# Display information, solicit input, and be sure it is proper format
print("Credit card balance, if no payment is made for a designated number of months.")
start_balance = int(input("Enter starting balance: "))
months = int(input("Enter number of months where no payment: "))
purchase_per_month = int(input("Enter purchase amount per month: "))
interest_rate = int(input("Enter interest rate as a percent: ")) 
rate = float(interest_rate/100)/12

# Loop to calculate ending credit card balance
a = 0
n = start_balance
while a < months:
    n = (n+ purchase_per_month) * (1 + rate)
    a = a + 1
    if a == months:
        break
total_balance = n
# Prepare variables as string for output and output results
total_balance = "${:,.2f}".format(total_balance)
print("")
print("Total balance after " + str(months) + " months: " + str(total_balance))


'''Part B
=============================================================================
After a few months, you stop buying and decide to pay off the card.
=============================================================================
'''
# Display information, solicit input, and be sure it is proper format
print("")
print("Check to see if the monthly payment is enough to keep balance from growing.")
monthly_payment = int(input("Enter a monthly payment: "))
print("")


# Check to see if payment is sufficient. If not communicate and quit.
# If sufficient, communicate.
monthly_interest = n * rate
p = monthly_payment
if monthly_payment > monthly_interest:
    p = "${:,.2f}".format(p)
    print("A monthly payment of " + p + " will work.")
else:
    print("This will not work. You will be paying off credit card forever.")
    sys.exit()

# Calculate and display minimum payment
print("")
monthly_interest = "${:,.2f}".format(monthly_interest)
print("The minimum monthly payment for this card is " + monthly_interest)
print("")

'''Part C
=============================================================================
With this monthly payment, determine how long it will take to pay off card.
=============================================================================
'''
# Loop to calculate months needed to pay off card
h = float(n)
e = monthly_payment
y = 0
while h > 0:
    h = (h - e) * (1 + rate)
    y = y + 1
    if h <= 0:
        break
         
# Prepare variables as string for output and output results as months and years

print("It will take " + str(y) + " months to pay off your card balance with " + str(p) + " payment.")
mon = float(y)
yr = mon/12
print("")
print("It will take " + str(round(yr , 2)) + " years to pay off your card balance with " + str(p) + " payment.")