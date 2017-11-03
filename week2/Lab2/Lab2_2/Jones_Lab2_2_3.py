#Brad Jones
#CSC110 - Section 6
#4/13/2017

#Prince change comparison tool.

origPrice = float(input("Enter the price of your item: $"))
modifier = float(input("Enter the percentage you want to modify the price: "))
percent = modifier / 100
incrPrice = int(origPrice + origPrice * percent)
newPrice = int(incrPrice + incrPrice * (-1 * percent))
print("After increaseing the price by", modifier, "%, and then reducing that price \n"
      "by", modifier, "%, your new price is: $",  newPrice)
