#Brad Jones - CSC110 Section 6 - 4/25/2017
#Tuition Increase Calulator
cost = 8000.00
rate = 3/100
y = 0
print("The current tuition is: $" + format(cost,'.2f'))
print("\tYear: \t\t Cost:")
for year in range(1,5):
    print("\t", y, "\t\t\t$" + format(cost,'.2f'))
    incr = cost + cost * rate
    cost += cost * rate
    y += 1
