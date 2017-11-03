#Brad Jones - CSC110 Section 6 - 5/4/2017
#HW5 - Decision Structures

menu_select = 0
import math
import random

#menu display and input validation
def menu():
    menu_select = 0
    displayMenu()

    #input validation loop
    while menu_select < 1 or menu_select > 3:
        menu_select = int(input("Please enter your option--> "))
        if menu_select < 1 or menu_select > 3:
            print ("Invalid input, please try again")
            print ()
    return menu_select


# display
def displayMenu():
    print("Choose an option (enter and number in range 0-4):")
    print("1. Find the number that has maximum numbers of digits.")
    print("2. Find the number that has the maximum number of divisors.")
    print("3. Find and display all numbers in given range which are divided by three.")
    print("0. Finish working with the program. \n\n")


# user choice handler
def main():
    user_menu_select = menu()
    print()
    if user_menu_select == 1:
        digit_counter()

    elif user_menu_select == 2:
        divisor_count()

    elif user_menu_select == 3:
        div_range_counter()

    else:
        main()

#Mode 1
def digit_counter():
    rand_select = int(input("How many numbers do you want to calculate? "))
    max_rand = 0
    digit = 0
    # generate random numbers
    for count in range(0, rand_select):
        rand = random.randrange(0, 1000000)
        print(rand, "\t", end="")

        #largest number sorted to the top
        if max_rand < rand:
            max_rand = rand
    print()

    #count digits of the largest number and output
    num = max_rand
    print(max_rand, "is the largest number with ", end="")
    while num > 0:
        digit += 1
        num //= 10
    print(digit, "digits")

def divisor_count():
    rand_select = int(input("How many numbers do you want to calculate? "))
    max_div = 0

    #print table headers
    print("NUM", " |", "Divs")
    print("-" * 13)
    max_div = 0
    max_div_num = 0

    #generate random numbers
    for count in range(0, rand_select):
        rand = random.randrange(100, 201)
        print(rand, "\t", end="")
        div_count = 0

        #count the divisors of each random number
        for num in range(1, rand - 1):
            div_check = rand % num
            if div_check == 0:
                div_count += 1
        print(div_count)

        #largest number of divisors sorted to the top
        if div_count >= max_div:
            max_div = div_count
            max_div_num = rand
    print()

    # output
    print("The number with the most divisors is", max_div_num, "with", max_div, "digits.")

def div_range_counter():
    rand_select1 = 0
    rand_select2 = 0

    # user input and validation
    while rand_select1 < 1 or rand_select1 > 101 or rand_select2 < 1 or rand_select2 > 101:
        rand_select1 = int(input("Enter the first number of the range you wish to find"))
        rand_select2 = int(input("Enter the second number of the range you wish to find"))
        if rand_select1 < 1 or rand_select1 > 101 or rand_select2 < 1 or rand_select2 > 101:
            print("Invalid input, please select between 0 and 100 \n\n")

    #check if 3 is a factor of each number
    print("The values with a divisor of three are: \n")
    for count in range(rand_select1, rand_select2):
        rand = random.randrange(rand_select1, rand_select2 + 1)
        factor_check = rand % 3
        #if 3 is a factor, print the number
        if factor_check == 0:
            print(rand, "\t", end="")
    print()

#start the program
main()