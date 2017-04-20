#Brad Jones
#CSC110 - Section 6
#4/20/2017
#BMI Calculator

#Input
weight = float(input('Enter your weight in pounds: '))
height = float(input('Enter your height in inches: '))

#processing
BMI = float(weight*703/(height**2))

if BMI < 18.5:
    print('Your BMI is: ', format(BMI))
    print('You are underweight')


elif BMI > 25:
    print('Your BMI is: ', format(BMI))
    print('You are overwight')


else:
    print('Your BMI is: ', format(BMI))
    print('You are at optimal weight')
