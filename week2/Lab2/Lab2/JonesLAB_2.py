#Brad Jones
#CSC 110 - Section 6
#4/11/2017
#Simple restuartant tip calculator

#PSEUDOCODE
#INPUT >> Amount of the bill & percantage of tip
#PROS >> 
#OUTPUT >> Bill amount, tip percentage, tip in dollars, Bill+tip, tax, Total

#Input Section
bill = float(input("How much was the total of your bill? "))
tipInput = float(input("What percentage would you like to tip "))

#Processing Section
tipPercent = (tipInput / 100)
tipDollars = (bill * tipPercent)
subTotal = (bill + tipDollars)
taxPercent = .095
taxTotal = (bill + (bill * taxPercent))
grandTotal = (taxTotal + tipDollars)

#Output Section
print("The bill totals: $"+ str(format(bill, '.2f')))
print("Your desired tip percantage is:  "+ str(tipInput)+ "%")
print("Your tip totals: $"+ str(format(tipDollars, '.2f')))
print("The subtotal is: $"+ str(format(subTotal, '.2f')))
print("Your total after taxes: $"+ str(format(taxTotal, '.2f')))
print("Your grand total is: $"+ str(format(grandTotal, '.2f')))

