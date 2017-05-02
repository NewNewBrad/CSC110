#Brad Jones - CSC110 Section 6 - 4/25/2017
# HW5 - Decision Structures
end = 1
if end == 1:
    import random
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
        #Each loop generates a random number between 1-1,000,000
        max_rando = 0
        for i in range(0, rand_num):
            rando = random.randrange(0,1000001)
            print(rando, "\t", end="")
            if rando > max_rando:
                max_rando = rando
            else:
                print(max_rando)
        max_rando_digit = max_rando
        digit_count = 0
        if max_rando_digit > 0:
            max_rando_digit //= 10
            digit_count += 1
        else:
            print()
            print(max_rando, "has the maximum number of digits that equals", digit_count)

    elif menu_select == 2:
        rand_num = int(input("How many numbers do you want to calculate? "))
        rando_list = []
        import random, math
        for i in range(0, rand_num):
            rando = random.randrange(99, 201)
            print(format(rando), "\t", end= "", )
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
else:
    print("aslkdjfaslfjas")