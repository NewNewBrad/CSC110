
# gas_mileage_with_functions.py
    
# Demonstrates the recommended structure for programs that
# make use of function definitions.

# CSC 110
# Fall 2011

def main():
    # Introduction
    print('Welcome to the gas mileage calculator!\n')

    # Input with Validation Loops
    user_miles = float(input('Enter the number of miles driven (>=0): '))
    while (user_miles < 0):
        user_miles = float(input('Try again -- miles must be >= 0: '))
    user_gallons = float(input('Enter gallons of gas used (>0): '))
    while (user_gallons <= 0):
        user_gallons = float(input('Try again -- gallons must be > 0: '))

    # Processing (using function call)
    mileage = calculate_gas_mileage(user_miles, user_gallons)

    # Output
    print('\nYou used ' + format(user_gallons, '.1f') \
          + ' gallons of gas to drive ' + format(user_miles, '.1f') \
          + ' miles.\nYour gas mileage is ' + format(mileage, '.1f') \
          + ' mpg.\n\nThanks for using this calculator!')

# Calculates gas mileage in MPG given the number of miles driven
# and the number of gallons of gas used.  [This is a very simple
# function; its main purpose is to demonstrate the structure of a
# program that makes use of functions.]
def calculate_gas_mileage(miles, gallons):
    result = miles / gallons
    return result

# Call the 'main' function to run the program.
# [This should always be the LAST statement in the program.]
main()
