#This program will calculate future value, based on present value,
# annual interest rate, and time horizon

# This program also illustrates the format operator

# CSC 110

print( "Future Value Calculator" )
print(  )
print(  )

# Get the desired future value.
presentValue = float( input('Enter the  prinicpal: ') )

# Get the annual interest rate.
rate = float( input('Enter the annual interest rate [as a decimal]: ') )

# Get the number of years that the money will appreciate.
years = float( input('Enter the number of years the money will grow: ') )

# Calculate the amount this will grow to
futureValue = presentValue * (1.0 + rate)**years

# Display the future value
# notice the syntax when using multiple format operations in
# one print statement
print ( "If you start with ", format( presentValue, '.2f' ), \
        "\nlet it grow for ", format( years, '.1f' ), \
        " years\nat an annual interest rate of ", format( rate, ".2f" ) )
print ( "You will have a total of $", format( futureValue, '.2f' ) )
        


# Test cases, confirmed by hand
# $100 invested at 0.05 annual rate  for 2 years will grow to $110.25
# $500 invested at 0.035 annual rate  for 10 years will grow to $705.30
        
