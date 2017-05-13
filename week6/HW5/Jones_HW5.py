
#Program intro
def main_menu():
    print("This program will generate a random number and ask the user to convert")
    print("the number into another numeric system. The program will keep track of the users score.")
    print()
    mode_select = 0
    mode()

    #Input Validation
    while mode_select < 1 or mode_select > 2:
        mode_select = int(input("Please enter 1 or 2 to begin: "))
        if mode_select < 1 or mode_select > 2:
            print("Please use 1 or 2 to select your game mode")
            print()
    return mode_select


#Mode select menu
def mode():




#Random number generator (1- 100)
def genRandNum():
    randNum = rand.randrange(0,101)
    return randNum

#Random numeric system generator (2,9), Numeric system = 10 if user select mode 2
def genRandSys():
    if userMode == 2:
        randSys = 10
    else:
        randSys = rand.range(1,10)
    return randSys


#Prompts user for guess and returns value
def Guess():
    if userMode == 1:
        UserGuess = input("Enter the new number that matches this number: ")
    if userMode == 2:
        UserGuess = input("Enter the decimal number that matches this number: ")
    return guess




    #Converts Decimal number to numeric system
def mode1():

    sysNum = DecToRand()

def DecToRand():
    copy = randNum
    SysNum = 0
    k = 0
    while copy > 0:
        digit = copy % randSys
        SysNum += digit *(10**k)
        k += 1
        copy // randSys
    return SysNum

def mode2():
    randNum = genRandNum()
    randSys = genRandSys()
    print("The number", randNum, "is represented in the numeric system:", randSys)
    SysNum = RandToDec()
    userGuess = Guess()

def RandToDec():
    copy = randNum
    SysNum = 0
    k = 0
    while copy > 0:
        digit = copy % 10
        SysNum = 0
        k = 0
        copy // randSys
    return SysNum



def main():
    userMode = main_menu()
    print()
    if userMode == 1:
        print("You chose Mode 1: Convert decimal to random numeric system")
        mode1()
    if userMode == 2:
        print("You chose Mode 2: Convert random numeric system to decimal")
        mode2()

main()