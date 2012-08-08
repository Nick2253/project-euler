def sumOfSquares(maxNum):
    '''Determines the sum of all the square of the natural numbers less than maxNum
        input:
            maxNum = int
        output:
            sumTotal = int sum of all squares
    '''
    sumTotal = 0
    
    for num in range(1,maxNum+1):
        sumTotal += num**2
        
    return sumTotal
        
def squareOfSum(maxNum):
    '''Determines the square of the sum of the natural numbers less than maxNum
        input:
            maxNum = int
        output:
            sumTotal = int square of sum
    '''
    
    sumTotal = 0
    
    for num in range(1,maxNum+1):
        sumTotal += num
        
    return sumTotal**2

def sumDiff(maxNum):
    return squareOfSum(maxNum) - sumOfSquares(maxNum)

if __name__ == "__main__":
    print "sumDiff(10) = " + str(sumDiff(10)) #2640
    print "sumDiff(100) = " + str(sumDiff(100)) #??