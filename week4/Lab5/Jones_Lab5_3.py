#Brad Jones - CSC110 Section 6 - 4/25/2017
#Tuition Increase Calulator
rate=float(3/100)
year=1
tuition = int(input("Please enter your current yearly tuition amount $"))
years = int(input("Please enter the number of years you will attend: "))
print("This program will now calculate your annual tuition for the next", years, "years")
print("\tYear: \t\t Cost:")
print("-"*32)
if tuition > 0 or years > 0:
    for year in range(1,years+1):
        print("\t", format(year, '.0f'), "\t\t\t$" + format(tuition,'.2f'))
        incr = tuition + tuition * rate
        tuition += tuition * rate
        year += 1
else:
    print("Please enter a valid number")