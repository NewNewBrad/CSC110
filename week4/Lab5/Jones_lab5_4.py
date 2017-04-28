#Brad Jones - CSC110 Section 6 - 4/25/2017
#Ocean Level Calculator
oLevel = 0
rate = 1.6
count = 1
y = int(input("Enter the number of years you wish to forecast: "))
print("Calculating the amount of Ocean rise over", y, "years.")
print("\tYear: \t\t Amount risen:")
if y > 0 and y <= 25:
    for i in range(1,y + 1):
        print("\t", count, "\t\t\t" + format(oLevel,'.2f') + "mm.")
        oLevel += rate
        count += 1
else:
    print("Please enter a valid number of years (1-25)")