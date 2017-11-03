# Example of a menu-driven program
# CSC 110

# this function displays the menu and then returns
# the user's choice (either 1, 2, or 3)
def menu():
    choice = 0
    displayMenu()

    #input validation loop
    while choice < 1 or choice > 3:
        choice = int(input("Please enter your option--> "))
        if choice < 1 or choice > 3:
            print ("Invalid input, please try again")
            print ()

    return choice


# this function displays the menu with options 1, 2, or 3
def displayMenu():
    print ("option 1")
    print ("option 2")
    print ("option 3")
    print()


# the main program to display the menu, get the user choice and display
# what they chose
def main():
    userChoice = menu()
    print()
    if userChoice == 1:
        print ('You chose option 1')
    elif userChoice == 2:
        print ('You chose option 2')
    else:
        print ('You chose option 3')
    
main()
