from math import sqrt

def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True

def factorize(n):
    factors=[]
    i=2
    while i<=sqrt(n):
        if n%i==0:
            factors.append(i)
            n//=i
        else:
            i+=1
    if n>1:
        factors.append(n)
    return factors
