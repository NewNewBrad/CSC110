# program to ask user for dimensions of a rectangle and
# calculate area and perimeter
# CSC 110

def main():
    print ("Rectangle calculator")

    # user input
    width = float( input("Please enter the width of the rectangle (ft): ") )
    height = float( input("Please enter the height of the rectangle (ft): ") )

    # do the calculations
    area = rectArea(width, height)
    perim = rectPerimeter(height, width)

    # display
    print ( "A rectange with dimensions " + format(width, '.1f') +" ft by "
            + format(height,'.1f') + " ft")
    print ( "Has perimeter = " + format(perim, '.2f') + " ft")
    print ("and area = " + format( area, '.2f') + " sq ft" )

# Calculate the area of a rectangle
# parameter: w - the width of the rectangle
# parameter: h - the height of the rectangle
# return: the area
def rectArea(w, h):
    return w * h

# Calculate the perimeter of a rectangle
# parameter: h - the height of the rectangle
# parameter: w - the width of the rectangle
# return: the perimeter
def rectPerimeter(h, w):
    return 2 * h + 2 * w


main()
