# Brad Jones - CSC110 - HW 5
# Converting numbers between numeric systems
# Using functions

# Program intro
print("This program will generate a random number and ask the user to convert")
print("the number into another numeric system. The program will keep track of the users score.")
print()

# Program main menu and input validation
def menu():
    print("Please choose which game you would like to play.")
    print("Mode 1: Convert a decimal number into a random numeric system.")
    print("Mode 2: Convert a number in a random numeric system into decimal.")
    print("")

    # Variables within the scope of the full program
    mode_select = 0
    points = 0
    rounds = 1

    # Input validation loop (allows restart on mode_select reset)
    while mode_select < 1 or mode_select > 2:
        mode_select = int(input("Please enter 1 or 2 to begin: "))
        main(mode_select, points, rounds)
        if mode_select < 1 or mode_select > 2:
            print("Please use 1 or 2 to select your game mode")
            print()

# Main program, accepts menu_select, and score/round accumulators
def main(mode_select, points, rounds):
    # Testing Variables:
    #randNum = 10
    #newSys = 2

    # Real Variables:
    randNum = random.randrange(1,101)
    newSys = random.randrange(2,9)
    SYS = 10
    newNum = convert(randNum, SYS, newSys)

    # Show current round and score.
    print("*" * 48)
    print("\t\t Round:", rounds, "\t\t\t Score", points)
    print("*" * 48)
    print()

    # Convert decimal to (n)umeric system
    if mode_select == 1:
        print("The decimal number is", randNum)
        print("Convert this number to the numeric system:", newSys)
        score = guess(mode_select, newNum)
        print()

    # Convert number in (n)umeric system to decimal
    if mode_select == 2:
        # Mode 2 requires the number to be converted before showing the output
        # User input must match original number (randNum) to score
        print("The number", newNum, "is represented in the numeric system:", newSys)
        score = guess(mode_select, randNum)
        print()

    # Score keeping and output
    if score == True:
        points += 1
        print("Your answer is correct. You have", points, "points.")
        print()
    if score == False:
        print("Your answer is incorrect. You have", points, "points.")
        print()

    # Restart the program, chosing a random mode
    restart = input(" Enter 'Y' to play another round: ")
    if restart == "Y" or "y":
        print()
        mode_select = random.randint(1, 2)
        rounds += 1
        main(mode_select, points, rounds)
    else:
        print("Thanks for playing!")
        print()

# Converts number into new numeric system
def convert(randNum, SYS, newSys):
    copy = randNum
    newNum = 0
    k = 0
    while copy > 0:
        digit = copy % newSys
        newNum += digit * (SYS ** k)
        k += 1
        copy //= newSys
    return newNum

# Prompt user for guess, return correct or incorrect
def guess(mode_select, answer):
    if mode_select == 1:
        userGuess = int(input("Enter the new number that matches this number: "))
    else:
        userGuess = int(input("Enter the decimal number that matches this number: "))
    if userGuess == answer:
        score = True
    else:
        score = False
    return score

# Begin the game
import random
menu()