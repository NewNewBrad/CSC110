# function to print a block
#illustrates modular decomposition

# CSC 110

def main():
    printBlock()


def topBottom():
    print ('+ - - - - - +' )

def gaps():
    print ( '|           |' )

def printBlock():
    topBottom()
    gaps()
    gaps()
    gaps()
    gaps()
    topBottom()

main()
