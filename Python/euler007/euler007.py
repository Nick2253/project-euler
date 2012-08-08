import math

def isPrime(num):
    '''Determines if num is prime
        input:
            numList = list of ints
            maxNum = int
        output:
            sumTotal = int sum of all multiples of numbers in numList less than maxNum
    '''
    isPrime = True
    i = 2 #We don't care if num is divisible by 1
    
    if num <= 1:
        return False
    
    while (i < (1 + math.sqrt(num)) and i != num): #We add 1 to the sqrt to preclude rounding issues
        if num%i == 0:
            isPrime = False
            break
        i += 1
        
    return isPrime
        
def nPrime(maxIndex):
    '''Determines the maxIndexth prime
        input:
            maxIndex = int
        output:
            prime at maxIndex
    '''
    i = 0
    num = 0
    
    while i < maxIndex:
        num += 1
        if isPrime(num):
            i += 1
            
    return num

if __name__ == "__main__":
    print "isPrime(1) = " + str(isPrime(1))
    print "isPrime(2) = " + str(isPrime(2))
    print "isPrime(10) = " + str(isPrime(10))
    print "isPrime(23) = " + str(isPrime(23))
    print "nPrime(6) = " + str(nPrime(6))
    print "nPrime(10001) = " + str(nPrime(10001))