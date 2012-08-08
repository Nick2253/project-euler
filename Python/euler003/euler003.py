import math

def largestPrimeFactor(x):
    '''Determines the largest prime factor of number x
        input:
            x = int
        output:
            lpf = largest prime factor of x
    '''
    
    if x == 1:
        return 1
    elif x == 0:
        return 0
    
    lpf = 0
    i = 2
    isPrime = True
    
    while i < math.sqrt(x):
        if x%i == 0:
            isPrime = False
            lpf = max([lpf,largestPrimeFactor(i),largestPrimeFactor(x/i)])
        i += 1
        
    if isPrime:
        lpf = x
        
    return lpf
        
if __name__ == "__main__":
    print "lpf(10) = " + str(largestPrimeFactor(10)) #5
    print "lpf(46) = " + str(largestPrimeFactor(46)) #23
    print "lpf(13195) = " + str(largestPrimeFactor(13195)) #29
    print "lpf(600851475143) = " + str(largestPrimeFactor(600851475143)) #??