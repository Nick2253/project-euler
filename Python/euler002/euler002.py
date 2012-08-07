def fibEvenSum(maxNum):
    '''Determines the sum of all the even Fibonocci numbers in numList less than maxNum
        input:
            maxNum = int
        output:
            sumTotal = int sum of all even Fib numbers less than maxNum
    '''
    sumTotal = 0 #would be 1 for sum of all fib numbers because fn_1 starts at 1
    fn = 0
    fn_1 = 1
    fn_2 = 0
    
    if maxNum < 0:
        return "error"
    elif maxNum == 1:
        return 0
    
    while fn < maxNum:
        if fn%2 == 0:
            sumTotal += fn
        fn = fn_1 + fn_2
        fn_2 = fn_1
        fn_1 = fn
        
    return sumTotal

if __name__ == "__main__":
    print "fibEvenSum(2) = " + str(fibEvenSum(2)) #0
    print "fibEvenSum(3) = " + str(fibEvenSum(3)) #2
    print "fibEvenSum(55) = " + str(fibEvenSum(55)) #44    
    print "fibEvenSum(4,000,000) = " + str(fibEvenSum(4000000)) #??