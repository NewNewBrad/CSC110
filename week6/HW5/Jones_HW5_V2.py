#Brad Jones - CSC110 - HW 5
#Converting numbers between numeric systems
#Using functions


#Program intro
print("This program will generate a random number and ask the user to convert")
print("the number into another numeric system. The program will keep track of the users score.")
print()


#Menu select and menu input validation
def main():
    print("Please choose which game you would like to play.")
    print("Mode 1: Convert a decimal number into a random numeric system.")
    print("Mode 2: Convert a number in a random numeric system into decimal.")
    print("")
    mode_select = 0
    while mode_select < 1 or mode_select > 2:
        mode_select = int(input("Please enter 1 or 2 to begin: "))
        print()
        if mode_select < 1 or mode_select > 2:
            print("Please use 1 or 2 to select your game mode")
            print()

    if mode_select == 1:
        mode1()

    if mode_select == 2:
        mode2()

#Converts number into new numeric system
def convert(randNum, OrigSys, NewSys):
    copy = randNum
    newNum = 0
    k = 0
    while copy > 0:
        digit = copy % NewSys
        newNum += digit * (OrigSys ** k)
        k += 1
        copy //= NewSys
    return newNum



def mode1():
    randNum = 10
    #randNum = random.randrange(1,101)
    OrigSys = 10
    NewSys = 2
    #NewSys = random.randrange(2,9)

    # Initial Question
    print("The decimal number is", randNum)
    print("Convert this number to the numeric system:", NewSys)

    # Calls convert()
    newNum = convert(randNum, OrigSys, NewSys)

    # Accepts User input
    userGuess = int(input("Enter the new number that matches this number: "))
    output(newNum, userGuess)



def mode2():
    randNum = random.randrange(1,101)
    OrigSys = random.randrange(2,9)
    NewSys = 10
    newNum = convert(randNum, OrigSys, NewSys)
    print("The number", newNum, "is represented in the numeric system:", OrigSys)
    userGuess = int(input("Enter the decimal number that matches this number: "))
    output(randNum, userGuess)



def output(newNum, userGuess):
    # If User is correct
    if userGuess == newNum:
        print("Your answer is correct.", end="")

    # If User is incorrect
    else:
        print("Your answer is incorrect.", end="")

    # continuation of game
    restart = input("Continue? Enter 'Y' to continue.")
    print("*" * 24)
    if restart == "Y" or "y":
        mode1()
    else:
        print("Thanks for playing!")


import random
main()