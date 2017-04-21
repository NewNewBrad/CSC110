#Brad Jones
#CSC110 - Section 6
#4/20/2017
#Solving a Quadratic (Roots only)

import math

#Input
num1 = float(input('Enter your first coefficient: '))
num2 = float(input('Enter your second coefficient: '))
num3 = float(input('Enter your third coefficient: '))

#processing Quadratic possibilities:
#if A=0, B!=0
if num1 == 0 and num2 != 0:
    answer1 = -(num3/num2)
    print('This equation has one solution: ', format(answer1, '.2f'))

#if B=0, A!=0 and (C/A)<0
elif num2 == 0 and num1 != 0 and (num3/num1) < 0:
    answer1 = math.sqrt((-(num3)/num1))
    answer2 = math.sqrt(-(-(num3)/num1))
    print('This equation has two solutions: ', format(answer1, '.2f'), 'and', format(answer2, '.2f'))

#if C=0, A=!0
elif num3 == 0 and num1 !=0:
    answer1 = -((num2)/num1)
    print('This equation has two solutions: ', format(answer1, '.2f'), 'and 0')

#if A or B or C !=0        
elif 0 != num1 or num2 or num3:

    #find discriminant         
    discrim = num2 ** 2 - 4 * num1 * num3


    #discriinant is positive
    if discrim > 0:
        answer1 = (-num2 + math.sqrt((num2 ** 2) - (4 * (num1 * num3)))) / (2 * num1)
        answer2 = (-num2 - math.sqrt((num2 ** 2) - (4 * (num1 * num3)))) / (2 * num1)
        print('This equation has two solutions: ', format(answer1, '.2f'), ' and ', format(answer2, '.2f'))


    #discriminant is 0
    if discrim == 0:
        answer1 = (-num2 + math.sqrt(num2 ** 2 - 4 * num1 * num3)) / (2 * num1)
        print('This equation has one solution: ', format(answer1, '.2f'))


    #discriminant is negative
    else:
        print('This equation has no real solutions.')

    
#if solution is a complex number
else:
    print('This is not the Standard Form of the Quadratic Equation')
    
