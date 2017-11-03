# creates a random list of numbers and then displays the average and largest value
# CSC 110
import random

HIGH = 30
LOW = -20
COUNT = 10

def main():
    
    # get random values
    data = generateValues(LOW, HIGH, COUNT)

    ave = getAverage(data)
    largest = getLargest(data)

    print ('List =', data )
    print ()
    print ( 'Average =', ave, ' Largest =', largest )


# create and return a list of random integers
# parameter lo, the lowest possible random value
# parameter hi, the highest possible random value
# parameter ct, the amount of values in the list
def generateValues(lo, hi, ct):
    # create an empty list
    holder = []
    for x in range(ct):
        holder.append(random.randint(lo,hi))

    return holder

# return the average of the values in the list numbers
def getAverage(numbers):

    total = 0
    for value in numbers:
        total += value

    return float(total)/len(numbers)

# return the largest value in the list numbers
def getLargest(numbers):

    # start with the largest at index 0
    largest = numbers[0]

    # now visit the rest of the list and find the largest
    for idx in range(1, len(numbers)):
        # test to see if we found a new larger number
        if numbers[idx] > largest:
            largest = numbers[idx]

    return largest

main()
