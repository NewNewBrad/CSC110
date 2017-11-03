# Group 2
# CSC110 - Section 6
# 4/25/2017
# Finding Factorials

print("Finding Factorial Numbers \n")
num = int(input("Please enter a number to find its factorial: "))
print("\tValue \t\tFactorial ")
fact = 1
if num > 0 and num <= 20:
    for start in range(1, num + 1):
        fact *= start
        start += 0
        print("\t", start, "\t\t", fact, "\t")
elif num == 0:
    print("\t 0 \t\t\t 1 \t")
    print("The factorial of 0 is always 1")
else:
    print("This program can only accept numbers between 0 and 20")
