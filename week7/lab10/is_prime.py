import math
def is_prime(n):
    flag = True
    if n > 1 and ( n==2 or n%2!=0 ) and (n %10!=5 or n==5):
        for div in range(3,int(math.sqrt(n))+1,2):
            if n % div == 0:
                flag = False
                break
    else:
        flag = False
    return flag
