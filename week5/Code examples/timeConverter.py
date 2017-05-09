# Convert days to hours, days to minutes, and days to seconds
# CSC 110

def main():
    print ( "Days to Converter" )

    days = int( input("Please input the number of days: ") )

    hours = daysToHr(days)
    minutes = daysToMin(days)
    seconds = daysToSec(days)

    print ( format( days, "d" ), "days" )
    print ( " =", format( hours, "d" ), "hours" )
    print ( " =", format( minutes, "d" ), " minutes" )
    print ( " =", format( seconds, "d" ), " seconds" )

# Converts days to hours
# parameter: d - the number of days
# returns: the number of hours
def daysToHr(d):
    return d * 24

# Converts days to minutes
# parameter: d - the number of days
# returns: the number of minutes
def daysToMin(d):
    return daysToHr(d) * 60

# Converts days to seconds
# parameter: d - the number of days
# returns: the number of seconds
def daysToSec(d):
    return daysToMin(d) * 60


main()
    
