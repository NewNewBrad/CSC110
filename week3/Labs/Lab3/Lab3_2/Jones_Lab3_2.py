# Las Name
# CSC 110, section 05
# This program will calculate sum of 3-d number
# 10/11/2016

# Lab 3

#input section
number = int(input("Please enter 3-d number you would like to calculate: "))
if number > 99 and number < 1000:
    # calculation
    firstDigit = number//100
    secondDigit = number%100//10
    thirdDigit = number%10
    sumOfDigits = firstDigit + secondDigit + thirdDigit
    #output section
    print("The sum of digits of number",number,"is",sumOfDigits)
else:
    print("Sorry, you did not enter a 3-digit number")
