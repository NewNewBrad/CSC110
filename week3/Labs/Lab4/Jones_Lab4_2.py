#Brad Jones
#CSC110 - Section 6
#4/20/2017
#BMI Calculator

#Input
weight = float(input('Enter your weight in pounds: '))
height = float(input('Enter your height in inches: '))

#processing
#calculate BMI
BMI = float((weight*703)/(height**2))

if BMI < 18.5:
    print('Your BMI is: ', format(BMI, '.1f'))
    print('You are underweight')

    #returns weight @ 18.5 BMI given users height
    minOPTweight = ((18.5/703)*(height**2))

    print('You need to gain', str(format(minOPTweight - weight, '.1f')), 'pounds to reach optimal BMI')


elif BMI > 25:
    print('Your BMI is: ', format(BMI, '.1f'))
    print('You are overwight')

    #returns weight @ 25 BMI given  users height
    maxOPTweight = ((25/703)*(height**2))

    print('You need to lose', str(format(weight - maxOPTweight, '.1f')), 'pounds to reach optimal BMI.')


else:
    print('Your BMI is: ', format(BMI, '.1f'))
    print('You are at optimal weight')
