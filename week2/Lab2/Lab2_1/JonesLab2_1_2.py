#Brad Jones
#CSC111 - Section 6
#4/12/2017

#Calculating the sum of a numbers digits

#input
num = int(input('Please type any 3-digit number: '))


#processing
digit1 = num // 100
digit2 = num % 100 // 10
digit3 = num % 10
num = digit1 + digit2 + digit3

#output
print 'The sum of the digits is: ', num
