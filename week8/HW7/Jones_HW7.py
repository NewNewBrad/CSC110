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

        # File output  header info
        outputFile = open('REPORT - ' + year + '.txt', 'w')
        outputFile.write('*' * 63)
        outputFile.write('\n')
        outputFile.write("\t \t Weather Report for {0} \n".format(year))
        outputFile.write('*' * 63)
        outputFile.write('\n')
        outputFile.write("Month \t Maximum \t Minimum \t Average \t Rain \n")
        outputFile.write('\n')

        #List accumalators
        months = []         #Names of Months
        maxTemps = []       #Highest temp in given month
        minTemps = []       #Lowest temp in given month
        rainDays = []       #Number of rainy days in given month
        avgTemp = []        #Average temp of given month
        monthIndex = 0      #Tracks number of Months processed.

        while line != '':
            #Pull the name of the month from the file and update to Months list
            line = weatherData.readline()
            line = line.rstrip('\n')

            # This is an ugly way to fix a problem I dont understand. The loop was going 1 extra time before this, returning '' err
            if line == '':
                break

            #Add month to Months[]
            months.append(line)

            #Read the number of Days in order to set the range of the for loop
            days = int(weatherData.readline())

            #monthsTemp[] is a list of all temps recorded during the CURRENT month
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

            #Sorts monthsTemp[]
            #Months[i] will match with minTemp[i], maxTemp[i], rainDays[i] and avgTemp[i]
            bubbleSort(monthsTemp)
            minTemp_mo = int(monthsTemp[0])
            maxTemp_mo = int(monthsTemp[len(monthsTemp)-1])

            #Add min temp of each month to the minTemp[]
            minTemps.append(minTemp_mo)

            #Add max temp of each month to the maxTemp[]
            maxTemps.append(maxTemp_mo)

            #Add number of rain days of each month to rainDays[]
            rainDays.append(rainDays_mo)

            #Converts temp list to interger, finds sum, divides by # of days in month
            #to find Average temp of each month
            sumOftemps = sum(int(i) for i in monthsTemp)

            #Add average temp of each month to avgTemp[]
            avgTemp.append(format((sumOftemps/days), '.2f'))

            #File ouput info. Each loop prints new line
            outputFile.write("{:<11} {:<14} {:<14} {:<14} {:<11}\n".format(months[monthIndex], maxTemps[monthIndex], minTemps[monthIndex], avgTemp[monthIndex], rainDays[monthIndex]))

            #Increment to next month loop
            monthIndex += 1

        #Close files
        outputFile.close()
        weatherData.close()

        #Console Output
        maxTempsIndex = maxTemps.index(max(maxTemps))
        print("The maximum temperature for the year was {} in {}".format(max(maxTemps), months[maxTempsIndex]))
        minTempsIndex = minTemps.index(min(minTemps))
        print("The minimum temperature for the year was {} in {}".format(min(minTemps), months[minTempsIndex]))
        maxRainIndex = rainDays.index(max(rainDays))
        print("The maximum number of rainy days was {} in {}".format(max(rainDays), months[maxRainIndex]))
        minRainIndex = rainDays.index(min(rainDays))
        print("The minimum number of rainy days was {} in {}".format(min(rainDays), months[minRainIndex]))

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

main()