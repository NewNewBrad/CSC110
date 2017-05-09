# credit_card.py
#
# How long will it take to pay off a credit card balance??
# This program makes use of a loop to perform a SIMULATION
# of a real-world situation.

# CSC 110
# Fall 2011

### Get and validate inputs

interest_multiplier = float(input('Enter an ANNUAL INTEREST RATE ' \
    + 'as a PERCENTAGE, >= zero: ')) / 1200.0
while interest_multiplier < 0:
    interest_multiplier = float(input('TRY AGAIN -- annual ' \
        + 'rate must be >= zero: ')) / 1200.0

initial_balance = float(input('Enter an INITIAL ACCOUNT BALANCE ' \
    + 'in dollars, >= 100: '))
while initial_balance < 100:
    initial_balance = float(input('TRY AGAIN -- initial balance ' \
        + 'must be >= 100: '))

payment = float(input('Enter the MONTHLY PAYMENT to be made, ' \
    + 'in dollars, >= 10: '))
while payment < 10:
    payment = float(input('TRY AGAIN -- monthly payment ' \
        + 'must be >= 10: '))

### Simulate account changes until the account is paid in full

balance = initial_balance # initialize accumulator
months = 0                # initialize counter
total_payments = 0        # initialize accumulator;

# NOTICE that the loop continues as long as the balance is greater than
#        zero, BUT not longer than 1200 months -- a condition necessary
#        to prevent an infinite loop if the payment is too low.
while balance > 0 and months < 1200:
    balance = balance + (balance * interest_multiplier)
    balance -= payment
    total_payments += payment
    months += 1
    # print(balance)  # use to TRACE loop operation

years = months // 12  # integer division on purpose -- whole years only
months = months % 12


### Show results

print('\nAfter ' + str(years) + ' years and ' + str(months) + ' months')
if balance <= 0:
    print('your debt is paid.')
    total_payments += balance # corrects for any excess payment (balance <= 0)
    print('\nTotal interest = $'
          + format((total_payments - initial_balance),',.2f') + '.')
else:
    print('your debt is still not paid off!')
    print('Remaining balance = $' + format(balance, ',.2f') + '.')
print('\nTotal payments = $' + format(total_payments, ',.2f') + '.\n')
