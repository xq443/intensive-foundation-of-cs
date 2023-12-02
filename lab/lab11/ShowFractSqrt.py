# ShowFractionSqrt.py
# Xujia Qin
# Nov 30th, 2023
""" Illustrates rectangle averaging as applied to Fractions
"""

from copy import *
from TheFractionClass import *

def sqrtF(a):
    """ Returns a Fraction that approximates the square root
    of a obtained by doing 5 "rectangle averagings."
    
    PreC: a is a Fraction with positive value
    """

   
    x = a
    # Perform 5 rectangle averagings
    for i in range(6):
        # Division operation and 1./2. float need to be defined between Fractions
        x = (x + (a / x)) * Fraction(1,2)  
        
    return x
    

if __name__ == '__main__':
    a = Fraction(9,1)
    x = sqrtF(a)
    print ('Value of the final fraction = ',float(x.num)/float(x.den))
    
    
