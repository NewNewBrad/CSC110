#Brad Jones - CSC110 - 5/5/2017
#Calculate the sum of digits in a given number

user_num = int(input("What number do you wish to calculate the digits of? "))
sum = 0
while counter > 0:
    digit = user_num % 10
    sum += digit
    counter //= 10
print("The sum of the digits for", user_num, "is:", sum)
               
