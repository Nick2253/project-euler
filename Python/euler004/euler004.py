def palindromeFinder(numDigits):
    '''Determines the largest palindrome that is a product of two numbers with numDigits digits
        input:
            numDigits = max digits in numbers
        output:
            largPal = largest palindrome
    '''
    largPal = 0
    
    for num1 in range(10**(numDigits-1),10**(numDigits)):
        for num2 in range(num1,10**(numDigits)):
            if isPalindrome(num1*num2):
                largPal = max(largPal,num1*num2)
        
    return largPal
        
def isPalindrome(number):
    '''Determines if number is a Palindrome
        input:
            number = int
        output:
            boolean
    '''
    return str(number)==str(number)[::-1]

if __name__ == "__main__":
    print "isPalindrome(10) = " + str(isPalindrome(10))
    print "isPalindrome(11911) = " + str(isPalindrome(11911))
    print "isPalindrome(10012) = " + str(isPalindrome(10012))
    print "palindromeFinder(3) = " + str(palindromeFinder(3))