#Brad Jones - CSC110 Section 6 - 4/25/2017
# HW5 - Decision Structures

#Menu Select Screen
print("Choose an option (enter and number in range 0-4):")
print("1. Find the number that has maximum numbers of digits.")
print("2. Find the number that has the maximum number of divisors.")
print("3. Find and display all numbers in given range which are divided by three.")
print("0. Finish working with the program. \n")
menu_select = int(input("Please enter a number in range 0-3: "))


#Option 1: maximum digits of X number of random numbers
if menu_select == 1:
    rand_num = int(input("How many numbers do you want to calculate? "))
    #Could have done this with multiple if statements but a list
    #seems like the faster/easier way.
    rando_list = []
    import random
    #Each loop generates a random number between 1-1,000,000
    for i in range(0, rand_num):
        rando = random.randrange(0,1000001)
        print(format(rando), "\t", end="",)
        #Each loop also adds the random number to the end of the list (rando_list)
        rando_list.append(rando)
    #max() will find the largest value in the list, which by definition has the largest number of digits
    #if 2 or more random numbers have the same amount of digits, this will display the largest of them
    max_rando = max(rando_list)
    #len() raturns the number of digits in the largest value
    max_rando_digits = len(str(max_rando))
    print("\n")
    #print the output, end of program
    print(max_rando, "has the maximum number of digits that equals", max_rando_digits)

elif menu_select == 2:
    rand_num = int(input("How many numbers do you want to calculate? "))
    rando_list = []
    import random, math
    for i in range(0, rand_num):
        rando = random.randrange(99, 201)
        print(format(rando), "\t", end="", )
        counter = 1
            while counter <= math.sqrt(rando):
                if rando % counter == 0:

    rando_list.append(rando)

elif menu_select == 3:
    int(input("Enter beginning of a range: "))
    int(input("Enter the end of a range: "))

elif menu_select == 0:
    print("Thank you for playing!")

else:
    print("Please select a number between 0 and 3")