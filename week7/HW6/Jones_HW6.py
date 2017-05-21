# Brad Jones - CSC110 - Section 6
# 5/20/2017
# Working with Files - Tornados in Alabama
def main():
    user_File = input(str("Enter the name of the file: "))
    tor_File = open(user_File, 'r')
    #tor_File = open('Tornado.txt', 'r')

    #Accumulator Variables
    totalYEAR = 0
    totalTOR = 0
    totalFAT = 0
    totalINJ = 0

    maxYEAR = 0
    minYEAR = 9999

    maxTOR = 0
    maxTORyear = 0
    minTOR = 9999
    minTORyear = 9999

    maxFAT = 0
    maxFATyear = 0
    minFAT = 9999
    minFATyear = 9999

    maxINJ = 0
    maxINJyear = 0
    minINJ = 9999
    minINJyear = 9999

    #Reading the file, one line at a time
    line = tor_File.readline()
    loop_count = 1
    while line != '':
        #If statments divide data into Year/Tornado/Fatalities/Injuries
        #using loop_count % 4
        #YEAR
        if loop_count % 4 == 1:
            currentValue = int(line) #convert str to int
            currentYEAR = currentValue
            totalYEAR += 1 #years counter

            maxYEAR = is_max(maxYEAR, currentValue)
            minYEAR = is_min(minYEAR, currentValue)

        # # of TORNADOES
        if loop_count % 4 == 2:
            currentValue = int(line)
            totalTOR += currentValue
            minTOR = is_min(minTOR, currentValue)
            maxTOR = is_max(maxTOR,currentValue)

            if maxTOR == currentValue:
                maxTORyear = currentYEAR

            if minTOR == currentValue:
                minTORyear = currentYEAR
            #print(currentValue)

        # # of FATALITIES
        if loop_count % 4 == 3:
            currentValue = int(line)
            totalFAT += currentValue
            minFAT = is_min(minFAT, currentValue)
            maxFAT = is_max(maxFAT, currentValue)

            if maxFAT == currentValue:
                maxFATyear = currentYEAR

            if minFAT == currentValue:
                minFATyear = currentYEAR
                # print(currentValue)

        # # of INJURIES
        if loop_count % 4 == 0:
            currentValue = int(line)
            totalINJ += currentValue
            minINJ = is_min(minINJ, currentValue)
            maxINJ = is_max(maxINJ, currentValue)

            if maxINJ == currentValue:
                maxINJyear = currentYEAR

            if minINJ == currentValue:
                minINJyear = currentYEAR
                # print(currentValue)

        # Add to loop_count; restart loop if line != ''
        loop_count += 1
        line = tor_File.readline()
        

    #Find and format averages
    avgTOR = str(format(totalTOR/totalYEAR, '.0f'))
    avgFAT = str(format(totalFAT/totalYEAR, '.0f'))
    avgINJ = str(format(totalINJ/totalYEAR, '.0f'))
    tor_File.close()

    #File output
    outputFile = open('REPORT - '+user_File, 'w')
    line1 = "For period", str(minYEAR)
    line2 = "to", str(maxYEAR), "in the State of Alabama were: "
    outputFile.write(line1)
    outputFile.write('*'*48)
    outputFile.write(str("Total tornadoes: ", totalTOR))
    outputFile.write("Total fatalities: ", totalFAT)
    outputFile.write("Total injuries: ", totalINJ)

    outputFile.write('*' * 48)
    outputFile.write("Average tornadoes: ", avgTOR)
    outputFile.write("Average fatalities: ", avgFAT)
    outputFile.write("Average Injuries: ", avgINJ)

    outputFile.write('*' * 48)
    outputFile.write("Max tornadoes", maxTOR, "were in", maxTORyear)
    outputFile.write("Min tornadoes", minTOR, "were in", minTORyear)

    outputFile.write('*' * 48)
    outputFile.write("Max fatalities", maxFAT, "were in", maxFATyear)
    outputFile.write("Min fatalities", minFAT, "were in", minFATyear)

    outputFile.write('*' * 48)
    outputFile.write("Max injuries", maxINJ, "were in", maxINJyear)
    outputFile.write("Min injuries", minINJ, "were in", minINJyear)
    outputFile.close()


    




























    #Shell output
    print("For period", str(minYEAR), "to", str(maxYEAR), "in the State of Alabama were: ")
    line1 = "For period", str(minYEAR), "to", str(maxYEAR), "in the State of Alabama were: "
    
    print('*'*48)
    print("Total tornadoes: ", totalTOR)
    print("Total fatalities: ", totalFAT)
    print("Total injuries: ", totalINJ)

    print('*' * 48)
    print("Average tornadoes: ", avgTOR)
    print("Average fatalities: ", avgFAT)
    print("Average Injuries: ", avgINJ)

    print('*' * 48)
    print("Max tornadoes", maxTOR, "were in", maxTORyear)
    print("Min tornadoes", minTOR, "were in", minTORyear)

    print('*' * 48)
    print("Max fatalities", maxFAT, "were in", maxFATyear)
    print("Min fatalities", minFAT, "were in", minFATyear)

    print('*' * 48)
    print("Max injuries", maxINJ, "were in", maxINJyear)
    print("Min injuries", minINJ, "were in", minINJyear)

    print('*' * 48)
    print("An output file named Report -", user_File, "has been created.")


#Compares 2 values and returns the smaller
def is_min(minValue, currentValue):
    #print('running is_min()...')
    if currentValue <= minValue:
        return currentValue
    else:
        return minValue

#Compares 2 values and returns the larger
def is_max(maxValue, currentValue):
    #print('running is_max()')
    if currentValue >= maxValue:
        return currentValue
    else:
        return maxValue


main()
