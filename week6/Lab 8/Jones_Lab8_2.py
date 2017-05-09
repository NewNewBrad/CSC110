#Brad Jones - CSC 110 - 5/9/2017
# Prime Number Checker

def main():
    import prime
    start=int(input("Enter the begin of the range: "))
    endR=int(input("Enter the end of the range: "))
    if endR>start and start>0:
        print("This is a list of prime numbers from",start,"to",endR)
        for number in range(start,endR+1):
            primeCheck = prime.is_prime(number)
            if primeCheck:
                print(number, "\t", end="")
       
    else:
        print("Incorrect input")

main()
