#Brad Jones - CSC110 - Section 6
# Lab 9: Working with files

print("*"*68)
print("\t\t\t Working with files:")
print("This program will read numbers from a text file of users' choice \n"
      "and preform various math functions with those numbers and display \n"
      "the answer for the user")
print("*"*68)
print()

try:
    userChoice = str(input("Please enter the name of the file you would like to read from: "))
    fileEven = open('fileEven.txt', 'w')
    fileOdd = open('fileOdd.txt', 'w')
    fileSource = open(userChoice,'r')


    totalNumbers = 0
    totalEvenSUM = 0
    totalOddSUM = 0
    totalNeg = 0

    line = fileSource.readline()

    while line != '':
        value = float(line)
        totalNumbers += 1
        
        if value % 2 == 0:
            totalEvenSUM += value
            fileEven.write(str(value)+'\n')
            if value < 0:
                totalNeg += 1
                
        else:
            totalOddSUM += value
            fileOdd.write(str(value)+'\n')
            if value < 0:
                totalNeg += 1
                
        line = fileSource.readline()

    fileSource.close()
    fileEven.close()
    fileOdd.close()

    print("A total quantity of numbers in the file is: ", totalNumbers)
    print("The sum of even numbers is: ", format(totalEvenSUM, '.0f'))
    print("The sum of the odd numbers is: ", format(totalOddSUM, '.0f'))
    print("The number of negative numbers is: ", totalNeg)
    
except IOError as err:
    print(err)
