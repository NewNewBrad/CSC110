# This program gets an item's original price and
# calculates its sale price, with a 20% discount.

# Illustrates a named constant
# Illustrates format string and how to display the % character

# CSC 110

DISCOUNT_RATE = 0.2   

print ( "This program will ask you for an item's price, then display the sale price" )

# Get the item's original price.
originalPrice = float( input("Enter the item's original price: ") )

# Calculate the amount of the discount.
discount = originalPrice * DISCOUNT_RATE

# Calculate the sale price.
salePrice = originalPrice - discount

# Display the sale price.
print ( "Your product's original price is ", format( originalPrice, '.2f' ) )
print ( "With a ", format( DISCOUNT_RATE * 100, '.1f' ), "% discount of $", format( discount, '.2f' ), \
        " the sale price is $", format( salePrice, '.2f'), sep='' )



# test cases, confirmed by hand
# original price of $100, 20% discount is $20, producing a sale price of $80
# original price of $22, 20% discount is $4.40, producing a sale price of $17.60
# original price of $55, 20% discount is $11, producing a sale price of $44
