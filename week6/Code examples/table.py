# table.py
#
# prints a multiplication table based on user input

# CSC 110
# Fall 2011

print('This program will print out a multiplication table.\n\n')

top = int(input('Enter a number between 2 and 9: '))
while top < 2 or top > 9:
    print('Sorry, but', top, 'is not valid input')
    top = int(input('Enter a number between 2 and 9: '))

# the outer loop is for each row
for row in range (1, top + 1):

    # the inner loop prints every column in the row
    for col in range(1, top + 1):
        print(row*col, '\t', end='') # notice end='' to suppress newline

    # after the loop is done, print again to move to the next line
    print()
