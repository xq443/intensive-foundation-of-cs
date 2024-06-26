# ShowFactorialR.py
""" Compares a recursive and nonrecursive implemenatation of
the factorial function.
"""

def Factorial(n):
    """ Returns an int equal to n!
    
    Nonrecursive implementation
    
    PreC: n is a nonnegative int.
    """
    if n<=1:
        return 1
    else:
        z = 1
        for k in range(1,n+1):
            z = k*z
    return z

def FactorialR(n):
    """ Returns an int equal to  n!
    
    Recursive implementation
    
    PreC: n is a nonnegative int.
    """
    #if n==0 or n==1:
    if n <= 1:
        return 1
    else:
        a = FactorialR(n-1)
        return n*a

if __name__ == '__main__':
    """ Compare the two implementations."""
    print ('\n n  Factorial(n)  FactorialR(n)')
    print ('----------------------------------------')
    for n in range(13):
        F1 = Factorial(n)
        F2 = FactorialR(n)
        print ('%2d  %10d   %10d' % (n,F1,F2))
    print (FactorialR(9.5))
    

  
    

