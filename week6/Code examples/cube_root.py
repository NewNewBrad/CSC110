
# Sample program illustrating programmer-defined functions
# along with code that calls the functions
#
# The 'cube_root' function uses a 'return' statement.  Its
# only job is to calculate and "return" the cube root of a
# number.  It does not print anything.  Notice that statements
# that "call" the 'cube_root' function need to USE the value
# returned.  They can do this by a) saving it in a variable,
# b) using it in a 'print' statement, or c) using the value in
# ANY general expression.  Imagine that the value returned by
# the function REPLACES the function call wherever it occurs.
# This is EXACTLY the same way you use built-in functions like
# 'input()', 'abs()', 'round()', etc.
#
# The 'show_table' function does NOT use a 'return' statement.
# It's job is to PRINT a table.  Different functions may be
# used in different ways.
#
# CSC 110
# Winter 2013

# The cube_root function calculates and RETURNS the cube root
# of a number.  If the value of 'x' is negative, a negative 
# real number is returned.
def cube_root(x):
    if x < 0:
        result = -( (-x)**(1.0/3.0) )
    else:
        result = x ** (1.0/3.0)
    return result

# Main program
def main():
    print('Let\'s examine the cube roots of some numbers.\n')

    # CALL the function and save the value returned in a variable:
    num = 27
    root = cube_root(num)  # The ARGUMENT is a variable
    print('Cube root of ' + str(num) + ' is ' + format(root, '.1f'))
    root = cube_root(num + 98)  # The argument is an expression
    print(root)

    # Use the function call directly in a 'print' statement:
    print('Cube root of ' + str(num) + ' is ' + format(cube_root(num), '.1f'))

    # Use multiple function calls in an expression:
    print('The answer is', cube_root(8) + cube_root(1000) / 2)

    # Here is a table of some cube roots:
    print('\n     n     cube_root(n)')  # print header row
    num = 8
    print(format(num, '8.1f'), format(cube_root(num), '10.3f'))
    num = 31
    print(format(num, '8.1f'), format(cube_root(num), '10.3f'))
    num = 1727
    print(format(num, '8.1f'), format(cube_root(num), '10.3f'))
    num = 1728
    print(format(num, '8.1f'), format(cube_root(num), '10.3f'))
    num = 1729
    print(format(num, '8.1f'), format(cube_root(num), '10.3f'))

    # Here are a couple of longer tables:
    show_table(0, 1000, 10)
    show_table(42875, 1000000, 20)

# This function shows a table of cube roots.
# The first two parameters are the minimum and maximum values for 'n'.
# The third parameter is the number of rows to show in the table.
def show_table(minN, maxN, rows):
    # Calculate the step size.  There are (rows - 1) intervals:
    step = (maxN - minN) / (rows - 1.0)
    
    print('\n       n     cube_root(n)')  # print header row
    
    # Loop 'rows' times to print the rows in the table:
    for i in range(rows):
        n = minN + i * step  # calculate the value of 'n' for row 'i'
        print(format(n, '12.3f'), format(cube_root(n), '8.3f'))
 

# Run the program
main()
