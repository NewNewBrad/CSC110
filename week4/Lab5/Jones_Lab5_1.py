##Brad Jones - CSC110 Section 6 - 4/27/2017
##The Wheat and Chessboard problem

print("This program will calculate the number of grains of wheat on a chessboard, \n"
      "if you put 1 grain in the first square, and double that for each following \n"
      "square")
square = 0
wheat_sum = 0
wheat = 1
print(" Square \t\t Grain \t\t Total Grains")
print("-"*72)
for square in range(1, 64):
    wheat_sum += wheat
    wheat *= 2
    square += 1
    print(format(square, '<1'), " \t\t\t ", format(wheat, '<15'), " \t\t\t ", format(wheat_sum, '<15'))
