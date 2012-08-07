def sumOfMultiples(numList,maxNum):
    '''Determines the sum of all the multiples of the numbers in numList less than maxNum
        input:
            numList = list of ints
            maxNum = int
        output:
            sumTotal = int sum of all multiples of numbers in numList less than maxNum
    '''
    sumTotal = 0
    
    for num in numList:
        maxIndex = (maxNum-1)/num
        sumTotal += sumHelper(num,maxIndex)[0]
        
    return sumTotal
        
def sumHelper(num, maxIndex):
    '''Determines the sum of all the multiples of num up to num*maxIndex
        input:
            num = int
            maxIndex = int
        output:
            [sum_maxIndex, x_maxIndex]
                sum_maxIndex = sum of all the multiples of num up to num*maxIndex
                x_maxIndex = num*maxIndex solved recursively
    '''
    
    if maxIndex < 0:
        return ["error", "error"]
    elif maxIndex == 0:
        return [0,0]
    elif maxIndex == 1:
        return [num, 0]
    else:
        [newSum,numAtLowerIndex] = sumHelper(num,maxIndex-1)
        numAtIndex = num + numAtLowerIndex
        return [numAtIndex, numAtIndex + newSum]

if __name__ == "__main__":
    print "Sumhelper(10,0) = " + str(sumHelper(10,0))
    print "Sumhelper(10,0) = " + str(sumHelper(10,2))
    print "Sumhelper(3,3) = " + str(sumHelper(3,3))
    print "SumOfMultiples([10],11) = " + str(sumOfMultiples([10],11)) 