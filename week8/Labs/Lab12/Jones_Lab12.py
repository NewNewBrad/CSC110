# Brad Jones - CSC110 - 5/25/2017
# Lab 12, Working with Lists

def main():
    try:
        fileName = input("Enter the name of the file: ")
        myFile = open(fileName, 'r')
        index = 0 # how many numbers
        myList = []
        line = myFile.readline()
        while line!= "":
            myList.append(int(line))
            line = myFile.readline()
            
        sumOfNumbers = 0
        for index in range(len(myList)):
            sumOfNumbers+=myList[index]

        average = sumOfNumbers/len(myList)
        print("The sum of elements = ", format(sumOfNumbers), ", average = ", format(average))

            
    except IOError as err:
        print(err)
main()
