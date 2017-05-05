#Brad Jones - CSC110 Section 6 - 4/25/2017
#HW5 - Decision Structures
menu_select = 0
import math
import random

#menu select screen
print("Choose an option (enter and number in range 0-4):")
print("1. Find the number that has maximum numbers of digits.")
print("2. Find the number that has the maximum number of divisors.")
print("3. Find and display all numbers in given range which are divided by three.")
print("0. Finish working with the program. \n\n")

#input validation loop
while menu_select < 1 or menu_select > 3:
    menu_select = int(input("Please enter a number in range 0-3: "))
    if menu_select < 1 or menu_select > 3:
        print("Invalid input, please try again. \n\n")

#max digits in random pool
if menu_select == 1:
    rand_select = int(input("How many numbers do you want to calculate? "))
    max_rand = 0

    #generate random numbers and find the largest
    for count in range(0, rand_select):
        rand = random.randrange(0, 1000000)
        print(rand, "\t", end="")
        if max_rand < rand:
            max_rand = rand
    print()

    #count digits of largest number
    digit = 0
    digit_count = 0
    if digit >= 0:
        digit = max_rand % 10
        digit_count + 1
    # output
    print(max_rand, "has the maximum number of digits that equal", digit_count)

    #restart program
    #restart = input("Press Y to restart")
    #if restart == "Y" or "y":
    #    menu_select = 0
    #print()


#number of divisors in a random pool
elif menu_select == 2:
    rand_select = int(input("How many numbers do you want to calculate? "))
    max_div = 0

    # generate random numbers
    print("NUM", " |", "Divs")
    print("-" * 13)
    for count in range(0, rand_select):
        rand = random.randrange(100, 201)
        print(rand, "\t", end="")
        div_count = 0
        for num in range(1, rand - 1):
            div_check = rand % num
            if div_check == 0:
                div_count += 1
        print(div_count, "\n")

        # track highest divisor and the number associated
        max_div = 0
        max_div_num = 0
        if max_div < div_count:
            max_div = div_count
            max_div_num = rand
        else:
            max_div += 0

    #output
    print("The number with the most divisors is", max_div_num, "with", max_div, "digits.")

#find numbers within a range that have a factor of three
else:
    rand_select1 = 0
    rand_select2 = 0
    # input validation loop
    while rand_select1 < 1 or rand_select1 > 101 or rand_select2 < 1 or rand_select2 > 101:
        rand_select1 = int(input("Enter the first number of the range you wish to find"))
        rand_select2 = int(input("Enter the second number of the range you wish to find"))
        if rand_select1 < 1 or rand_select1 > 101 or rand_select2 < 1 or rand_select2 > 101:
            print("Invalid input, please select between 0 and 100 \n\n")

    # generate random numbers
    for count in range(rand_select1, rand_select2):
        rand = random.randrange(rand_select1, rand_select2 + 1)
        factor_check = rand % 3
        if factor_check == 0:
            print(rand, "\t", end="")
