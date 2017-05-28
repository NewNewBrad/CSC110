##Brad Jones - CSC110 - 5/27/2017
## Working with Lists - Weather Report HW7

def main():
    try:
        #File name input
        #user_File = input(str("Enter the name of the file: "))
        #weatherData = open(user_File, 'r')
        weatherData = open('temperature.txt', 'r')
        line = weatherData.readline()
        line = line.rstrip('\n')
        year = line

        # File output
        outputFile = open('REPORT - ' + year + '.txt', 'w')
        outputFile.write('*' * 63)
        outputFile.write('\n')
        outputFile.write("\t \t Weather Report for {0} \n".format(year))
        outputFile.write('*' * 63)
        outputFile.write('\n')
        outputFile.write("Month \t Maximum \t Minimum \t Average \t Rain \n")
        outputFile.write('\n')

        #Data accumalators
        maxTemp_year = 0
        minTemp_year = 999
        maxrainDays_year = 0
        minrainDays_year = 999
        months = []
        maxTemps = []
        minTemps = []
        rainDays = []
        avgTemp = []
        monthIndex = 0

        while line != '':
            #Pull the name of the month from the file and update to Months list
            line = weatherData.readline()
            line = line.rstrip('\n')
            if line == '': #This is an ugly way to fix a problem I dont understand. The loop was going 1 extra time before this, returning '' err
                break
            months.append(line)
            #print(months)

            #Read the number of Days in order to set the range of the for loop
            days = int(weatherData.readline())

            #Collects temps and number of rain days for a single month
            monthsTemp = []
            rainDays_mo = 0

            #Reads Temps and puts them in monthsTemps[], counts rainy days
            for index in range(days):
                line = weatherData.readline()
                line = line.rstrip('\n')
                monthsTemp.append(line)
                line = weatherData.readline()
                line = line.rstrip('\n')
                if line == "1":
                    rainDays_mo += 1

            #Sort list of temps for 1 month only
            #Months[i] will match with minTemp[i], maxTemp[i], rainDays[i] and avgTemp[i]
            bubbleSort(monthsTemp)
            minTemp_mo = int(monthsTemp[0])
            maxTemp_mo = int(monthsTemp[len(monthsTemp)-1])
            current_mo = str(months[monthIndex])
            print(current_mo)


            #Add min temp of each month to the minTemp list
            minTemps.append(minTemp_mo)
            #Compare the min temp of current month to min temp of year so far
            minTemp_year = is_min(minTemp_year, minTemp_mo)

            #if current min temp is also minTemp for the year, track which month
            if minTemp_year == minTemp_mo:
                minTemp_year_mo = current_mo


            #Add max temp of each month to the maxTemp list
            maxTemps.append(maxTemp_mo)
            #Compare the max temp of current month to max temp of year so far
            maxTemp_year = is_max(int(maxTemp_year), maxTemp_mo)

            #if current max temp is also maxTemp for the year, track which month
            if maxTemp_year == maxTemp_mo:
                maxTemp_year_mo = current_mo


            rainDays.append(rainDays_mo)
            maxrainDays_year = is_max(maxrainDays_year, rainDays_mo)
            if maxrainDays_year == rainDays_mo:
                maxTemp_year_mo = months[monthIndex]


            minrainDays_year = is_min(minrainDays_year, rainDays_mo)
            if minrainDays_year == rainDays_mo:
                minrainDays_year_mo = months[monthIndex]
            #print(rainDays_mo)





            sumOftemps = sum(int(i) for i in monthsTemp) #converts list items to int
            avgTemp.append(format((sumOftemps/days), '.2f'))
            #print(avgTemp)

            outputFile.write("{:<11} {:<14} {:<14} {:<14} {:<11}\n".format(months[monthIndex], maxTemps[monthIndex], minTemps[monthIndex], avgTemp[monthIndex], rainDays[monthIndex]))
            monthIndex += 1

        outputFile.close()
        weatherData.close()
        print(months[0])
        print("The maximum temperature of {} was in {}".format(maxTemp_year, maxTemp_year_mo))
        print("The minimum temperature of {} was in {}".format(minTemp_year, minTemp_year_mo))


    except ValueError as err:
        print(err)

    except IOError as err:
        print(err)


#Sorting a list
def bubbleSort(list):
    for count in range(len(list) - 1, 0, -1):
        for i in range(count):
            if list[i] > list[i + 1]:
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp


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