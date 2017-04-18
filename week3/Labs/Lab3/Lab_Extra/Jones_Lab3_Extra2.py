# Last Name
# CSC 110 section 5
# 10/11/16
# Digit addition(4 digits)

#Lab 3

# input section
number = int(input("Please input a 4 digit number. "))
if number > 999 and number < 10000:
    # Operation section
    digit1 = number//1000
    digit2 = number%1000//100
    digit3 = (number%100)//10
    digit4 = number%10
    sumTotal = digit1 + digit2 + digit3 + digit4
    first2 = digit1 + digit2
    last2 = digit3 + digit4
    # Output section
    print("The number was", number, ", the final sum of each digit is", sumTotal, ".")

    if first2 == last2:
        print("The sum of the first two digits equals the sum of the last two")
    else:
        print("The sum of the first two digits does not equal the sum of the last two")
else:
    print("Sorry, you did not enter a 4 digit number")
