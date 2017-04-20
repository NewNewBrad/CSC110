#Brad Jones
#CSC110 - Section 6
#4/13/2017

# Calculating the distance light travels
# from the Sun to the Earth

#PSUEDOCODE
#set constant for speed of light(CAPITAL LETTERS)
#set constant for distance from the Sun to the Earth
#Calculate distance/speed = time
#output time

#processing
LIGHTSPD = 3 * 10 ** 8
DIST = 1.5 * 10 ** 11
TIME = int(DIST / LIGHTSPD)
MINUTES = TIME // 60
SECONDS = TIME % 60


#output
print ("The ray of light passes the distance from the Sun \n"
"to the Earth for", MINUTES, "mintutes and", SECONDS,"seconds.")
