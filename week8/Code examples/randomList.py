# menu driven program to display all of an array, or subsets of it

# CSC 110
import random
HIGH = 100
LOW = 2
COUNT = 15

def main():
    
    # get random values
    list = generateValues(LOW, HIGH, COUNT)

    # get user choice and run their request
    userChoice = menu()
    while userChoice != 'q':
        if userChoice == 'a':
            displayAll(list)
        elif userChoice == 'e':
            displayEven(list)
        else:
            displayOdd(list)

        print ()
        # ask user again what they want to do
        userChoice = menu()

# create and return a list of random integers
# parameter lo, the lowest possible random value
# parameter hi, the highest possible random value
# parameter ct, the amount of values in the list
def generateValues(lo, hi, ct):
    # create an empty list
    holder = []
    for x in range(ct):
        holder.append(random.randint(lo,hi))

    return holder

# prints a menu and then gets and returns user input
# returns either 'q', 'a', 'e', or 'o' for quit/all/even/odd
def menu():
    print ()
    print ( 'a:   print all values' )
    print ( 'e:   print even values' )
    print ( 'o:   print odd values' )
    print ( 'q:   to quit' )

    answer = input("please enter your choice: a/e/o/q ")
    answer = answer.lower()
    while answer != 'a' and answer != 'e' and answer != 'o' and answer != 'q':
        print ( "Invalid input. Please try again" )
        answer = input("please enter your choice: a/e/o/q ")
        answer = answer.lower()

    return answer


# displays the entire content of stuff
def displayAll(stuff):
    for numb in stuff:
        print ( numb )
 

# displays all the odd values in the list stuff
def displayOdd(stuff):
    for numb in stuff:
        if numb % 2 == 1:
            print ( numb )

# displays all the even values in the list stuff
def displayEven(stuff):
    for numb in stuff:
        if numb % 2 == 0:
            print ( numb )

main()
