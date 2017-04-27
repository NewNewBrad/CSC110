#Brad Jones - CSC110 Section 6 - 4/25/2017
#Ocean Level Calculator
oLevel = 0
rate = 1.6
y = 0
print("Calculating the amount of Ocean rise over 25 years.")
print("\tYear: \t\t Amount risen:")
for i in range(1,27):
    print("\t", y, "\t\t\t" + format(oLevel,'.2f') + "mm.")
    oLevel += rate
    y += 1
