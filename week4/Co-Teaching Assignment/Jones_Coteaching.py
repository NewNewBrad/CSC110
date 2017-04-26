# Group 2
# Brad Jones
# CSC110 - Section 6
# 4/25/2017
# Finding Factorials

print("Finding Factorial Numbers \n")
num = int(input("Please enter a positive integer to find it's factorial: "))
print("\tValue: \t\tFactorial: ")
fact = 1
if num > 0:
    for i in range(1, num + 1):
        fact *= i
        i += 0
        print("\t", i, "\t\t", fact, "\t")
elif num == 0:
    print("The factorial of 0 is: 1")
elif num > 100:
    print("The free version of this program only calculates factorials from 0-100")
else:
    print("Invalid input")
