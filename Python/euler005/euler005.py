def lcm(maxNum):
    '''Determines the lcm of all the numbers between 1 and maxNum
        input:
            maxNum = int
        output:
            multiple = int lowest common multiple
    '''
    multiple = maxNum
    
    for x in range(1,maxNum):
        for y in range(x+1,maxNum+1):
            if y%x == 0:
                break
            elif y == maxNum:
                print (x,y)
                multiple = multiple * x
                
    return multiple

if __name__ == "__main__":
    print "lcm(1) = " + str(lcm(1)) #1
    print "lcm(4) = " + str(lcm(4)) #12
    print "lcm(10) = " + str(lcm(10)) #2520
    print "lcm(20) = " + str(lcm(20)) #??