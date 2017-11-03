# illustrates a list of values

# CSC 110

stuff = [7, 17, -4, 0.5]

# prints in "list" form (with square brackets and commas)
print ( stuff )

# this loop visits every element of the list, by index number
for index in range(len(stuff)):
    print ( 'Index:', index, ' Has value', stuff[index] )

print ()

# this loop will display the squares of the values in the list
# and then their sum
sqSum = 0

# since the algorithm doesn't need index numbers, we can just
# visit every element in the list
for value in stuff:
    sq =  value ** 2
    print ( 'value:', value, ' squared =', sq )
    sqSum +=sq

print ( 'The sum of those values =', sqSum )
