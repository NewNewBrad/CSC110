# Program to calculate mile per gallon based on distance travelled and gallons used
# mpg = miles/gallons
# CSC 110

print ('This program will calculate mpg based on your input')
print ()
print ()

# input section
miles = float( input('How many miles did you travel? ') )
gallons = float( input('How many gallons did you use?') )

# process
mpg = miles/gallons

#output section
print ('You travelled ',miles, 'miles')
print ('You used ', gallons, 'gallons')
print ('Your mpg = ', mpg)
