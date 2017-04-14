# This program demonstrates how a value can be
# formatted, rounded to different numbers of
# decimal places, using the %f placeholder


myValue = 1.123456789
 
print ( format( myValue, '.1f' ) )  # Rounded to 1 decimal place
 
print ( format( myValue , '.2f' ) ) # Rounded to 2 decimal places
 
print ( format( myValue , '.3f' ) ) # Rounded to 3 decimal places
 
print ( format( myValue, '.4f' ) )  # Rounded to 4 decimal places
   
print ( format( myValue, '.5f' ) )  # Rounded to 5 decimal places

print ( format( myValue, '.6f' ) )  # Rounded to 6 decimal places

input("Please press enter to continue")
print ()
print ()

# Here are some examples where you can insert a value into a more interesting string
otherValue = 2.724565
print ( 'The other value = ', format( otherValue, 'f' ) ) # notice this doesn't round at all, just inserts the value

print ( 'Here ', format( otherValue, '.4f' ), ' is rounded to 4 decimal places' )
