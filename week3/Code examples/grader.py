# This program gets a numeric test score from the
# user and displays the corresponding letter grade.

# CSC 110

# Get a test score from the user.
score = int( input('Enter your test score: ') )

# Determine the grade.
if score < 60:
    print ( 'Your grade is F.' )
elif score < 70:
    print ( 'Your grade is D.' )
elif score < 80:
    print ( 'Your grade is C.' )
elif score < 90:
    print ( 'Your grade is B.' )
else:
    print ( 'Your grade is A.' )
