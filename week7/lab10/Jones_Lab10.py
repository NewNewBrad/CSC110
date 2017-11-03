##Brad Jones - CSC110 - Section 6
##5/18/2017
##Lab 10 - Files and functions
## Ask user to input number of random integers amd export them to a txt file. 
import math
import random
import is_prime

def main():
    try:
        userInput = int(input("How many random numbers would you like to generate? "))
        if userInput > 0:
            testFile = open('test.txt', 'w')
            primeFile = open('prime.txt', 'w')
            random.seed(1)
            primeCount = 0
            for i in range(0, userInput):
                randNum = random.randrange(1,100)
                primeCheck = is_prime.is_prime(randNum)
                testFile.write(str(randNum) + '\n')
                if primeCheck:
                    primeFile.write(str(randNum) + '\n')
                    primeCount += 1

            testFile.close()
            primeFile.close()
            
            #Print the contents of test.txt
            print()
            print('*'*48)
            print(" \t All the random numbers generated: ")
            print('*'*48)
            testFile = open('test.txt', 'r')
            numLine = testFile.readline()
            while numLine != '':
                print(numLine, end='')
                numLine = testFile.readline()
            testFile.close()
            print('*'*48)


            #print contents of prime.txt
            print('*'*48)
            print(" \t All the prime numbers generated: ")
            print('*'*48)
            primeFile = open('prime.txt', 'r')
            numLine = primeFile.readline()
            while numLine != '':
                print(numLine, end='')
                numLine = primeFile.readline()
            primeFile.close()
            print('*'*48)

            #print total number of primes in prime.txt
            print('*'*48)
            print(" \t Number of Primes in 'prime.txt': ")
            print('*'*48)
            print(primeCount)
            print('*'*48)
            

        else:
            print("The number should be > 0")
    except ValueError as err:
        print(err)

main()
