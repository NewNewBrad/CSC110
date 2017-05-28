# increase all values in a list by 2

values = [ 5, 8, 14, 22]

print ( 'Origina list =', values )

# visit each location, by index number
for idx in range(len(values)):
    values[idx]  += 2

print ( 'New list = ', values )
