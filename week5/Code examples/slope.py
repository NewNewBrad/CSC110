# Program to calculate the slope between 2 points
# CSC 110

def main():
    print ( "Slope calculator" ) 

    # get the 4 coordinates
    firstX = float( input("Enter the first x-coordinate: ") )
    firstY = float( input("Enter the y coordinate for " + str(firstX) + ": ") ) 

    secondX = float( input("Enter the second x-coordinate: ") )
    secondY = float( input("Enter the y coordinate for " + str(secondX) + ": ") )
  
    # order of arguments is important
    m = slope(firstX, firstY, secondX, secondY)

    # output
    # create strings for the points
    point1 = "(" + format(firstX, '.1f') + ", " + format(firstY, '.1f') + ")"
    point2 = "(" + format(secondX, '.1f') + ", " + format(secondY, '.1f') + ")"

    print ( "Given points " + point1 + " and " + point2 )
    print ( "slope = " +format(m, '.2f'))

# Finds the slope given 2 points.
# This will crash if the points are vertical (x1 equals x2)
# parameters: x1, y1 - the first point
# parameters: x2, y2 - the second point
# returns the slope

def slope(x1, y1, x2, y2):
    return float(y2 - y1)/(x2 - x1)

main()
