#Brad Jones
#CSC110 - Section 6
#4/20/2017
#Solving a Quadratic (Roots only)

import math

#Input
num1 = int(input('Enter your first coefficient: '))
num2 = int(input('Enter your second coefficient: '))
num3 = int(input('Enter your third coefficient: '))

#error check
if 0 != num1 or num2 or num3:

    #find discriminant         
    discrim = num2 ** 2 - 4 * num1 * num3


    #discriinant is positive
    if discrim > 0:
        answer1 = (-num2 + math.sqrt((num2 ** 2) - (4 * (num1 * num3)))) / (2 * num1)
        answer2 = (-num2 - math.sqrt((num2 ** 2) - (4 * (num1 * num3)))) / (2 * num1)
        print('This equation has two solutions: ', answer1, ' and ', answer2)


    #discriminant is 0
    if discrim == 0:
        answer1 = (-num2 + math.sqrt(num2 ** 2 - 4 * num1 * num3)) / (2 * num1)
        print('This equation has one solution: ', answer1)


    #discriminant is negative
    else:
        print('This equation has no real solutions.')

    
#error message
else:
    print('This is not the Standard Form of the Quadratic Equation')
    
