# This program converts user input cups to fluid ounces.
# CSC 110

OZ_PER_CUP = 8

def main():
    intro()
    # Get the number of cups.
    cupsInput = float( input('Enter the number of cups: ') )
    
    # Convert the cups to ounces.
    ounces =  cupsToOunces(cupsInput)
    
    # display the conversion
    print (format(cupsInput, ".1f"), " cups =", format(ounces, ".1f"),"oz")
   

# The intro function displays an introductory screen.
def intro():
    print ( 'This program converts measurements' )
    print ( 'in cups to fluid ounces. For your' )
    print ( 'reference the formula is:') 
    print ( '    1 cup = 8 fluid ounces' )
    print ()

# Converts from cups to ounces
# parameter: cups - number of cups to convert
# return: the number of equivalent ounces
def cupsToOunces(cups):
    oz = cups * OZ_PER_CUP
    return oz

# Call the main function.
main()
