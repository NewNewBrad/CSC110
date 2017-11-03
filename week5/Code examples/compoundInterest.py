# Program to calculate future value for a given principal amount
# Compounding annually at 3 different interest rates over 10 years

# CSC110

# Constants used in the calculations
RATE5 = 0.05
RATE7 = 0.07
RATE10 = 0.1
YEARS = 10

def main():

    intro()

    # get starting prinicipal
    principal = float( input("Please enter starting value: $") )

    # calculate the future values
    future5 = compound(principal, RATE5, YEARS)
    future7 = compound(principal, RATE7, YEARS)
    future10 = compound(principal, RATE10, YEARS)

    # display
    print ()
    print ( '----------------------------------' )
    print ('$'+format(principal, ".2f"), "compounded annually over", \
           format(YEARS,"d"),"years")
    print 
    display(RATE5 * 100, future5)
    display(RATE7 * 100, future7)
    display(RATE10 * 100, future10)



# display program introduction

def intro():
    print ( "This program calculates future value compounded annually over", \
            YEARS, "years" )
    print ( "using 3 different interest rates." )




# Computes and returns the future value of some starting principal
# compounded annually
# parameter: p - starting principal
# parameter: r - annual interest rate (as a decimal)
# parameter: t - time, in years

def compound(p, r, t):
    fv = p * (1 + r)**t
    return fv



# Displays the given values formatted on one line
# parameter: rate - interest rate (as a percent)
# parameter: fv - future value at that interest rate
def display(rate, fv):
    print ( format(rate, '.1f') + '% interest rate\tfuture value = $', \
            format(fv, '.2f'))



main()
    

    
