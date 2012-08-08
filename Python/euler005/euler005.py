import sys

sys.setrecursionlimit(10000)

DEBUG = False

def lcm(x,y):
    '''Determines the lcm of x and y
        input:
            x = positive int
            y = positive int
        output:
            lcm = int lowest common multiple
    '''
    return (x*y)/gcd(x,y)
    
def gcd(x,y):
    '''Determines the gcd of x and y recursively using the Euclidean algorithm
        input:
            x = int
            y = int
        output:
            gcd = int gcd
    '''
    if y == 0:
        return x
    else:
        return gcd(y,x%y)
        
def lcmRange(maxNum):
    '''Determines the lcm of all numbers between 1 and maxNum
        input:
            maxNum = int
        output:
            multiple = int lcm
    '''
    multiple = 1
    
    for x in range(1,maxNum+1):
        multiple = lcm(x,multiple)
        if DEBUG: print "multiple = " + str(multiple)
    
    return multiple

if __name__ == "__main__":
    print "gcd(2,3) = " + str(gcd(2,3)) #1
    print "gcd(2,4) = " + str(gcd(2,4)) #2
    print "lcm(2,4) = " + str(lcm(2,4)) #4
    print "lcm(1,4) = " + str(lcm(1,4)) #4
    print "lcmRange(1) = " + str(lcmRange(1)) #1
    print "lcmRange(4) = " + str(lcmRange(4)) #12
    print "lcmRange(10) = " + str(lcmRange(10)) #2520
    DEBUG = True
    print "lcmRange(20) = " + str(lcmRange(20)) #??