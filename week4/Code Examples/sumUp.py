# program to accumulate values until the user enters an exit sentinel

# CSC 110

print ( 'You may enters numbers and they will be summed up.')
print ('To stop the proces, enter 0' )
print ()

# accumulator variables. One accumulates the count, the other, the total.
total = 0
count = 0

# get the user input and update the accumulator variables
value = int( input('Enter a number, or 0 to stop: ') )
while value != 0:
    count += 1
    total += value
    value = int( input('Enter another number, or 0 to stop: ') )

# display
print ()
print ( 'You entered ' + format( count, 'd' ) + ' numbers' )
print ( 'The total = ', format( total, 'd' ) )
