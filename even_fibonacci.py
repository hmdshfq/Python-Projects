# Problem 2 - Even Fibonacci numbers
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.

# Creating a function for even Fibonacci numbers
def evenFibonacci():
    # Initializing a and b with 1 and 2 respectively as the initial two
    # values for Fibonacci series
    a=1
    b=2
    # c will be the sum of a and b    
    c=0
    # sum will store the sum of even numbers in the Fibonacci series
    sum=0
    # Creating for loop for four million numbers.
    # a will be the first variable to store the upcoming Fibonacci number
    # That is why we make a < 4000000 instead of b or c     
    while a < 4000000:
        # The condition to check whether a has even number or not
        # When a is an even number it adds up to the previous 
        # even number giving the sum of even numbers in the Fibonacci series
        if a%2==0:
            sum = sum+a
        # c advances the Fibonacci series        
        c=a+b
        # swapping of variables for advancing the series
        a=b
        b=c
    # displaying the final sum of even numbers in Fibonacci series    
    print("The even Fibonacci sum is {}".format(sum))    
        
evenFibonacci()
