#Brad Jones
#CSC 110 - Section 6
# 4/10/2017
# A small madlib program, written in python.


#Percy Shelley's "Ozymandias"
#
#I met a traveller from an antique land
#Who said: Two vast and trunkless legs of stone
#Stand in the desert. Near them, on the sand,
#Half sunk, a shattered visage lies, whose frown,
#And wrinkled lip, and sneer of cold command,
#Tell that its sculptor well those passions read
#Which yet survive, stamped on these lifeless things,
#The hand that mocked them and the heart that fed:

#And on the pedestal these words appear:
#'My name is Ozymandias, king of kings:
#Look on my works, ye Mighty, and despair!'
#Nothing beside remains. Round the decay
#Of that colossal wreck, boundless and bare
#The lone and level sands stretch far away

#Welcome prompt
print("Welcome to HW 1 for CSC 110 at NSC. This is a Mad Lib by Brad Jones")

#User Input 
user_home = raw_input("Where are you originally from? ")
user_place = raw_input("What is your favorite place in nature? (ex. Mountains"
" Forest, Desert)")
face_expr = raw_input("Name a facial expression you make often: (ex. smile,"  
" sneer, grimace)")
adj1 = raw_input("Enter a positive adjective: ")
user_name = raw_input("Finally, what is your name? ")

#Madlib Output
print("\n\n\t\t I met a traveller from {} \n"
"\t\tWho said: Two vast and trunkless legs of stone \n"
"\t\tStand in the {}. Near them, in the ground, \n"
"\t\tHalf sunk, a shattered visage lies, whose frown, \n"
"\t\tAnd wrinkled lip, and {} of cold command, \n"
"\t\tTell that its sculptor well those passions read \n"
"\t\tWhich yet survive, stamped on these lifeless things, \n"
"\t\tThe hand that mocked them and the heart that fed: \n"
"\n"
"\t\tAnd on the pedestal these words appear: \n"
"\n"
"\t\t'My name is {}, king of kings: \n"
"\t\tLook on my works, ye {}, and despair!' \n"
"\n"
"\t\tNothing beside remains. Round the decay \n"
"\t\tOf that colossal wreck, boundless and bare \n"
"\t\tThe lone and level {} stretch far away.\n"
"\n"
"\n"
"\tPercy Shelley's 'Ozymandias', with a little help from {}.".format(user_home, 
user_place, face_expr, user_name, adj1, user_place, user_name))
