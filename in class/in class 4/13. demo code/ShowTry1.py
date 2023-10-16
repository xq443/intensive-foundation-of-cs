# ShowTry1.py
""" Illustrates the use of try-except.
"""
try:
    from math import sqrt
    print ('In try: AintNoMath.sqrt is available')
except ImportError:
    from math import sqrt
    print ('In except: AintNoMath.sqrt is  not available')

# Code that uses sqrt regardless of its 'source"...
a = 9
x = sqrt(a)
print ('\nThe square root of %8.6f is %8.6f\n' % (a,x))
    
        



