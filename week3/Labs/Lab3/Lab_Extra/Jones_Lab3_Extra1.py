# Las Name
# CSC 110, section 05
# This program will calculate sum of 3-d number
# 10/11/2016

# Lab 3

#input section
number = int(input("Please enter 3-d number you would like to calculate: "))
if 99 < number < 1000:
    # calculation
    sumEven = False
    firstDigit = number//100
    secondDigit = number%100//10
    thirdDigit = number%10
    sumOfDigits = firstDigit + secondDigit + thirdDigit
    #output section
    print("The sum of digits of number",number,"is",sumOfDigits)
    if sumOfDigits % 2 == 0:
        print(number, "is an even number")
    else:
        print(number, "is an odd number")

else:
    print("Sorry, you did not enter a 3-digit number")
