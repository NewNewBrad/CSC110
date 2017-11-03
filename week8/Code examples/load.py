# load an array of strings from user input, then display the list

# CSC 110

userStrings = []

word = input('Enter a string, or the word stop to finish: ')
word = word.lower()

while word != 'stop':
    userStrings.append(word)

    # get another input
    word = input('Enter a string, or the word stop to finish: ')
    word = word.lower()

# After user input, display the entire list

print ()
print ()
print ( 'Here are your entries' )
for i in range(len(userStrings)):
    print( 'Index', i, ' -->', userStrings[i] )
