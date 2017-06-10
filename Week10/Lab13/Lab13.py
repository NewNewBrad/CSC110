# Brad Jones
# CSC110 - Section 6
# Working with String - Lab 13


# PART 1 - USER INPUT
print("PART 1 - USER INPUT")
#userInput = "Hello World - Brad Jones Bringing the B words!"
userInput = input("Please input a string: ")
print()


# PART 2 - Print string, 1 character per line
print("PART 2 - PRINT STRING")
for char in userInput:
    print(char)
print()

# PART 3-1 - Print string backwards, on one line
print("PART 3-1 - REVERSE USING SLICE")
reverseString = userInput[::-1]
print(reverseString)
print()

# PART 3-2
print("PART 3-2 - REVERSE USING LOOP") 
for i in range(len(userInput)-1, -1, -1):
    print(userInput[i],end="")
print()
print()

# PART 4
print("PART 4 - STRING LOOP with CONDITIONALS")
for char in userInput:
    if char != " ":
        print(char, end="")
    else:
        print()
print()
print()

# PART 5
print("PART 5 - STRINGS WITHIN FILES")
#userFile = input(str("Enter the name of the file: "))
#textFile = open(userFile, 'r')
textFile = open('TumanYarom.txt', 'r')
textFile_line = textFile.readline()
while textFile_line != "":
    lineList = textFile_line.split()
    vowels = ("A", "E", "I", "O", "U", "a", "e", "i", "o", "u") #vowels tuple
    for i in range(0, len(lineList)):
        thisWord = lineList[i]
        for char in thisWord:
            if char in vowels:
                thisWord = thisWord.replace(char, "")
        print(thisWord)
    textFile_line = textFile.readline()
textFile.close()
print()
print()

# PART 6 ONLY PRINTS BEE BEE BEE BEEE ? Im not sure why yet.
# print("PART 6 - FIND AND REPLACE")
# userInputList = userInput.split()
# print(userInputList)
# for i in range(len(userInputList)):
#     thisWord = userInputList[i]
#     if thisWord == 'B' or 'b':
#         userInputList[i] = 'Bee'
# userInput = ' '.join(userInputList)
#
print(userInput)

