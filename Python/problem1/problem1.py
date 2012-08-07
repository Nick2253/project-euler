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
        return [num, num]
    else:
        [newSum,numAtLowerIndex] = sumHelper(num,maxIndex-1)
        numAtIndex = num + numAtLowerIndex
        return [numAtIndex + newSum, numAtIndex]

def sumOfMultiplesEasy():
    total = 0
    a = 0
    while a<1000:
        if (a%5==0 or a%3 == 0):
            total += a
        a += 1
    return total

if __name__ == "__main__":
    #print "Sumhelper(10,0) = " + str(sumHelper(10,0)) #[0,0]
    #print "Sumhelper(3,1) = " + str(sumHelper(3,1)) #[3,3]
    #print "Sumhelper(10,2) = " + str(sumHelper(10,2)) #[30,20]
    #print "Sumhelper(3,3) = " + str(sumHelper(3,3)) #[18,9]
    #print "Sumhelper(5,5) = " + str(sumHelper(5,5)) #[75,25]
    #print "SumOfMultiples([3,5],10) = " + str(sumOfMultiples([3,5],10)) #23
    #print "SumOfMultiples([3],1000) = " + str(sumOfMultiples([3],1000))
    print "SumOfMultiples([5],1000) = " + str(sumOfMultiples([5],1000))
    #fast(?) way#
    print "SumOfMultiples([3,5],1000) = " + str(sumOfMultiples([3,5],1000))
    #slow(?) way#
    print "SumOfMultiplesEasy() = " + str(sumOfMultiplesEasy())