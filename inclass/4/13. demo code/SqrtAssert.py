# SqrtAssert.py
""" Shows how the assert statement can be used to check
that the preconditions of a function are satisfied
and that what it returns "lives up to" the specifications.
"""

def sqrt(x):
   """ Returns an approximate square root L of x in that
   |L*L - x| <= .001
   
   PreC: x is a positive number.
   """
   assert x>0, 'The sqrt function requires a positive argument.'
   L = float(x) 
   L = (L+x/L)/2
   L = (L+x/L)/2
   L = (L+x/L)/2
   L = (L+x/L)/2
   assert abs(L*L-x)<=.1, 'Inaccurate Square Root'
   return L

if __name__ == '__main__':
    x  = float(input('Enter a positive number: '))
    z = sqrt(x)
    print ('sqrt(%5.3f) = %10.6f' % (x,z))
