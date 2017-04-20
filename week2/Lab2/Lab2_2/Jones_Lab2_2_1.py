#Brad Jones
#CSC110 - Section 6
#4/17/2017
#Math operators

#Input
num = (int(input("Please enter any number: ")))

#Processing
newNum1 = float((num * 3) + 6)
newNum2 = float(newNum1 / 3)
finalNum = float(num - newNum1)

#Output
print str(num), 'times 3, plus 6 is', str(newNum1) + '. Divided by 3 is', str(newNum2) + '.', num, 'minus', str(newNum2), 'is ', str(finalNum) + '.'
