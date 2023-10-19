#ShowTry2.py

""" Illustrates the use of try-except.
    Encourages the user to input a positive integer because
    that is what the factorial function requires
"""
import math

while True:
    N = input('Enter a nonegative integer:  ')
    try:
        # Convert the input string to an int.
        
        N = int(N) 
            
        # Valid input. Terminate the loop.
        if N > 0:
            break
   
    except ValueError:
        # Invalid input. Inform the user and the iteration continues.
        print ('N must have type int')

M = math.factorial(N)
S = math.sqrt(N)
print ('\n\n%1d square root = %1d' % (N,S))

print ('\n\n%1d! = %1d' % (N,M))

