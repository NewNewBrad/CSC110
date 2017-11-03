# print a list of powers of 2
# also includes input validation

# CSC 110


top = int( input('Enter a value between 1 and  20: ') )

# an  indefinite loop for input validation
while top < 1 or top > 20:
    print ( 'Error. ', format( top, 'd'), ' is not between 1 and 20. Please try again.' )
    top = int( input('Enter a value between 1 and 20 ') )

# a count controlled loop
for exp in range(0, top + 1):
    value = 2**exp
    print ( '2**', format(exp, 'd'), " = ", format( value, 'd') )
