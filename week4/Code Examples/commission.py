# Program to calculate sales commission, and to accumulate a total
# uses loops and functions

def main():
    print ( 'You will be asked to enter sales and commission rate for each ')
    print ('employee. The program will display the commission amount for each' )
    print ( 'and the total for the company' )
    print ()

    repeat = 'y'
    companyTotal = 0

    # repeated get the data for an employee and keep a running total
    while repeat == 'y' or repeat == 'Y':
        companyTotal += processOneEmp()
        print ()
        repeat = input('Is there another employee? Enter y for yes ')

   # display
    print()
    print()
    print ("The company's total commissions = $" + format( companyTotal, '.2f'))

# this function gets the data for one employee,
# calculates commission, and displays it
# returns the commission for the employee
def processOneEmp():

    #input
    print()
    name = input("What is the employee's name? ")
    sale = float(input('Enter the sales for ' + name + ' $') )
    rate = float(input("Enter the commission percentage rate for " + name + ": "))

    #calculation
    total = sale * rate/100.0   #convert from percent to decimal

    # output
    print ( name, 'earned $' + format(total, '.2f') + ' in commissions')

    return total

main()
