#Brad Jones - CSC 110 - 5/9/2017
# Prime Number Checker
import math

def main():
    num = -1
    while num < 0 or num > 999983:
        num = int(input("Please enter a number to determine if it is prime: "))
        if num < 0 or num > 999983:
            print("Please choose a number between 0 and 1000000")
    
    primeCheck = is_prime(num)
    
    if primeCheck:
        print(num, "is a prime number")
    else:
        print(num, "is NOT a prime number")

def is_prime(num):
    if num == 2:
        return True
    if num % 2 == 0 or num <= 1:
        return False

    sqrt = int(math.sqrt(num)) + 1

    for i in range(3, sqrt, 2):
        if num % i == 0:
            return False
    return True

main()    
